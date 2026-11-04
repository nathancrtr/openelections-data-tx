"""Stage 3: combine tesseract (psm6/psm4, cell psm7 fallback) and rapidocr ensemble per cell; resolve row labels.
Writes cells_final.json: {page: {rows:[labels], cols:[heads], cells:{'r,c':value}, issues:[...]}}"""
import json, os, re, subprocess, sys, tempfile, collections
import numpy as np
from PIL import Image
base=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,base)
from parse_tess import norm_label, CANON_N, CANON, read_tsv, NUM
from rapidocr_onnxruntime import RapidOCR
ENG=RapidOCR()
os.environ['OMP_THREAD_LIMIT']='1'
T=json.load(open(f'{base}/tess_parsed.json'))
R=json.load(open(f'{base}/rapid_cells.json'))
RB=json.load(open(f'{base}/rapid_blocks.json'))
ZERO_LIKE={'o','O','。','〇','０','Ο','ο'}
FW=str.maketrans('０１２３４５６７８９','0123456789')
def norm_rapid(s):
    s=s.strip().translate(FW)
    if s in ZERO_LIKE: return 0, 'zero-like'
    s=re.sub(r'^(\d{1,3})[.,](\d{3})$',r'\1\2',s)
    s=s.replace(',','')
    if s.isdigit(): return int(s), 'num'
    return None, s
def rapid_vote(outs):
    if outs==['<blank>']: return None, 'blank', []
    vals=[]; notes=[]
    for o in outs:
        v,n=norm_rapid(o)
        if v is not None: vals.append(v); notes.append(n)
    if not vals: return None, 'nonnumeric', outs
    c=collections.Counter(vals).most_common()
    if len(c)>1 and c[0][1]==c[1][1]: return None, 'tie', outs
    if c[0][1]<2: return None, 'single', outs
    note='zero-like' if any(n=='zero-like' and vals[i]==c[0][0] for i,n in enumerate(notes)) else 'num'
    return c[0][0], note, outs
def tess_cell(pg, x0,x1,yc, psm='7'):
    im=Image.open(f'{base}/rot/p-{pg:02d}.png').convert('L')
    crop=im.crop((x0-6,int(yc)-30,x1+6,int(yc)+30)); a=np.array(crop)
    ink=np.where(a<150)
    if len(ink[0])==0: return None
    c=crop.crop((max(0,ink[1].min()-15),max(0,ink[0].min()-12),ink[1].max()+16,ink[0].max()+13))
    w,h=c.size; c=c.resize((w*3,h*3),Image.LANCZOS)
    canvas=Image.new('L',(c.size[0]+80,c.size[1]+40),255); canvas.paste(c,(40,20))
    with tempfile.NamedTemporaryFile(suffix='.png',delete=False) as f:
        canvas.save(f.name)
        txt=subprocess.run(['tesseract',f.name,'-','--psm',psm,'-c','tessedit_char_whitelist=0123456789,'],capture_output=True,text=True).stdout.strip()
    os.unlink(f.name)
    txt=txt.replace(',','').replace(' ','')
    return int(txt) if txt.isdigit() else None
def tess_w_cells(pg, psm, rows, cols):
    m=json.load(open(f'{base}/meta/p-{pg:02d}.json')); cy=m['crop_y']
    cells={}
    for w in read_tsv(f'{base}/tess/p-{pg:02d}-{psm}.tsv'):
        mm=NUM.match(w['text'])
        if not mm: continue
        xc=w['x']+w['w']/2; yc=w['y']+cy+w['h']/2
        if xc<cols[0][0]-30: continue
        ci=next((i for i,(x0,x1) in enumerate(cols) if x0-8<=xc<=x1+8),None)
        ri=next((i for i,r in enumerate(rows) if abs(r['yc']-yc)<25),None)
        if ci is None or ri is None: continue
        cells.setdefault((ri,ci),int(mm.group(1).replace(',','')))
    return cells
def rapid_extra(pg, rows, cols, ri, ci):
    im=Image.open(f'{base}/rot/p-{pg:02d}.png').convert('L')
    ca=max(0,ci-1); cb=min(len(cols),ci+2)
    ra=max(0,ri-3); rb=min(len(rows),ri+4)
    x0=cols[ca][0]-10; x1=cols[cb-1][1]+10; y0=int(rows[ra]['yc'])-35; y1=int(rows[rb-1]['yc'])+35
    outs=[]
    for thr,bt,un,scale in [(0.05,0.1,2.0,3),(0.1,0.2,2.0,3),(0.05,0.1,1.6,2.5),(0.2,0.3,1.8,2)]:
        crop=im.crop((x0,y0,x1,y1)); crop=crop.resize((int(crop.size[0]*scale),int(crop.size[1]*scale)),Image.LANCZOS)
        ENG.text_detector.postprocess_op.thresh=thr
        r,_=ENG(np.array(crop.convert('RGB')),box_thresh=bt,unclip_ratio=un,text_score=0.1)
        for box,txt,sc in (r or []):
            xc=x0+sum(pt[0] for pt in box)/4/scale; yc=y0+sum(pt[1] for pt in box)/4/scale
            if cols[ci][0]-8<=xc<=cols[ci][1]+8 and abs(rows[ri]['yc']-yc)<25: outs.append(txt)
    return outs
def tess_extra(pg, rows, cols, ri, ci):
    im=Image.open(f'{base}/rot/p-{pg:02d}.png').convert('L')
    ca=max(0,ci-1); cb=min(len(cols),ci+2)
    ra=max(0,ri-3); rb=min(len(rows),ri+4)
    x0=cols[ca][0]-10; x1=cols[cb-1][1]+10; y0=int(rows[ra]['yc'])-35; y1=int(rows[rb-1]['yc'])+35
    outs=[]
    for scale in (2,3):
        for wl in (False,True):
            crop=im.crop((x0,y0,x1,y1)); crop=crop.resize((crop.size[0]*scale,crop.size[1]*scale),Image.LANCZOS)
            with tempfile.NamedTemporaryFile(suffix='.png',delete=False) as f:
                crop.save(f.name)
                args=['tesseract',f.name,f.name[:-4],'--psm','6']+(['-c','tessedit_char_whitelist=0123456789,'] if wl else [])+['tsv']
                subprocess.run(args,capture_output=True)
            for w in read_tsv(f.name[:-4]+'.tsv'):
                mm=NUM.match(w['text'])
                if not mm: continue
                xc=x0+(w['x']+w['w']/2)/scale; yc=y0+(w['y']+w['h']/2)/scale
                if cols[ci][0]-8<=xc<=cols[ci][1]+8 and abs(rows[ri]['yc']-yc)<25: outs.append(int(mm.group(1).replace(',','')))
            os.unlink(f.name); os.unlink(f.name[:-4]+'.tsv')
    return outs
def last_resort(pg, rows, cols, ri, ci):
    yc=rows[ri]['yc']; x0,x1=cols[ci]; xl=cols[max(0,ci-1)][0]-10
    im=Image.open(f'{base}/rot/p-{pg:02d}.png').convert('L')
    tess=[]; rap=[]
    for scale in (2,3,4):
        for thr in (None,170,200):
            crop=im.crop((xl,int(yc)-30,x1+10,int(yc)+30))
            if thr: crop=crop.point(lambda v:255 if v>thr else 0)
            crop=crop.resize((crop.size[0]*scale,crop.size[1]*scale),Image.LANCZOS)
            canvas=Image.new('L',(crop.size[0]+80,crop.size[1]+60),255); canvas.paste(crop,(40,30))
            with tempfile.NamedTemporaryFile(suffix='.png',delete=False) as f:
                canvas.save(f.name)
                for wl in (False,True):
                    args=['tesseract',f.name,f.name[:-4],'--psm','7']+(['-c','tessedit_char_whitelist=0123456789,'] if wl else [])+['tsv']
                    subprocess.run(args,capture_output=True)
                    for w in read_tsv(f.name[:-4]+'.tsv'):
                        mm=NUM.match(w['text'])
                        if not mm: continue
                        xc=xl+(w['x']-40+w['w']/2)/scale
                        if x0-8<=xc<=x1+8: tess.append(int(mm.group(1).replace(',','')))
            os.unlink(f.name); os.unlink(f.name[:-4]+'.tsv')
            for th,bt,un in [(0.1,0.2,2.0),(0.3,0.5,1.6)]:
                ENG.text_detector.postprocess_op.thresh=th
                r,_=ENG(np.array(canvas.convert('RGB')),box_thresh=bt,unclip_ratio=un,text_score=0.1)
                for box,txt,sc in (r or []):
                    xc=xl+(sum(pt[0] for pt in box)/4-40)/scale
                    if x0-8<=xc<=x1+8: rap.append(txt)
    tc=collections.Counter(tess).most_common()
    tv=tc[0][0] if tc and (len(tc)==1 or tc[0][1]>tc[1][1]) else None
    rv,_,_=rapid_vote(rap) if rap else (None,None,None)
    return tv, rv, tess, rap
def rapid_labels(pg):
    d=json.load(open(f'{base}/rapid/p-{pg:02d}.json'))
    out=[]
    for box,txt,sc in d:
        xs=[p[0] for p in box]; ys=[p[1] for p in box]
        if min(xs)<560 and min(xs)>50 and min(ys)>1200: out.append(((min(ys)+max(ys))/2, txt))
    return out
final={}
issues=[]
unresolved_readings={}
stats=collections.Counter()
for pg in range(2,66):
    p6=T[str(pg)]['p6']; p4=T[str(pg)]['p4']
    if not p6: continue
    rc=R[str(pg)]
    rl=rapid_labels(pg)
    labels=[]
    for ri,r in enumerate(p6['rows']):
        cand=[r['label']]
        for r4 in p4['rows']:
            if abs(r4['yc']-r['yc'])<22: cand.append(r4['label'])
        rr=[norm_label(t) for y,t in rl if abs(y-r['yc'])<25]
        rlab=[CANON_N.get(n, 'Totals' if n.startswith('TOTAL') else None) for n in rr]
        cand+=rlab
        cand=[c for c in cand if c]
        cnt=collections.Counter(cand).most_common()
        if not cnt: labels.append(None); issues.append((pg,ri,'label unresolved',r['raw'],rr)); continue
        lab=cnt[0][0]
        if r['label']!=lab or len(cnt)>1: issues.append((pg,ri,'label resolved by vote',r['raw'],cand,'->',lab))
        labels.append(lab)
    # fill a single unresolved label from the contiguous CANON sequence (20-row pages)
    if None in labels and len(labels)==20:
        known=[(i,CANON.index(l)) for i,l in enumerate(labels) if l]
        start=known[0][1]-known[0][0]
        if all(ci-i==start for i,ci in known):
            for i,l in enumerate(labels):
                if l is None:
                    labels[i]=CANON[start+i]; issues.append((pg,i,'label filled from sequence position ->',labels[i]))
    # sequence sanity
    idx=[CANON.index(l) for l in labels if l]
    if idx!=sorted(idx): issues.append((pg,'labels out of order',labels))
    cells={}
    cols=p6['cols']; heads=p6['heads']
    w6=tess_w_cells(pg,'6w',p6['rows'],cols); w4=tess_w_cells(pg,'4w',p6['rows'],cols)
    for ri in range(len(labels)):
        for ci,h in enumerate(heads):
            if 'Turnout' in h: continue
            k=f'{ri},{ci}'
            t6=p6['cells'].get(k); t4=p4['cells'].get(k)
            routs_all=rc.get(k,['<blank>'])
            if routs_all!=['<blank>']: routs_all=routs_all+RB.get(str(pg),{}).get(k,[])
            rv,rnote,routs=rapid_vote(routs_all)
            if rnote=='zero-like': stats['rapid zero-like']+=1
            if t6 is not None and rv is not None and t6==rv:
                cells[k]=t6; stats['agree t6']+=1; continue
            # fallback tesseract psm4 then cell-level psm7/8
            t7=tess_cell(pg,*cols[ci],p6['rows'][ri]['yc'],'7')
            t8=tess_cell(pg,*cols[ci],p6['rows'][ri]['yc'],'8')
            t6w=w6.get((ri,ci)); t4w=w4.get((ri,ci))
            tvals=[v for v in (t6,t4,t6w,t4w,t7,t8) if v is not None]
            if rv is None or rv not in tvals:
                extra=rapid_extra(pg,p6['rows'],cols,ri,ci)
                routs_all=routs_all+extra
                rv,rnote,routs=rapid_vote(routs_all)
            tx=None
            if rv is not None and rv not in tvals:
                tx=tess_extra(pg,p6['rows'],cols,ri,ci)
                # the block reading counts only if tesseract gives a clear majority there
                cc=collections.Counter(tx).most_common()
                if cc and cc[0][1]>=2 and (len(cc)==1 or cc[0][1]>cc[1][1]): tvals.append(cc[0][0])
            if rv is not None and rv in tvals:
                cells[k]=rv; stats['agree fallback']+=1
                issues.append((pg,labels[ri],heads[ci],'resolved via fallback',dict(t6=t6,t4=t4,t6w=t6w,t4w=t4w,t7=t7,t8=t8,tblock=tx,rapid=routs,final=rv)))
                continue
            if rv is None and rnote=='blank' and t6 is None and t4 is None:
                cells[k]=None; stats['blank']+=1; issues.append((pg,labels[ri],heads[ci],'blank cell')); continue
            ltv,lrv,ltess,lrap=last_resort(pg,p6['rows'],cols,ri,ci)
            if ltv is not None and ltv==lrv:
                cells[k]=ltv; stats['agree last-resort (2-cell context crop)']+=1
                issues.append((pg,labels[ri],heads[ci],'resolved via last-resort 2-cell crop',dict(t6=t6,t4=t4,t6w=t6w,t4w=t4w,t7=t7,t8=t8,tblock=tx,rapid=routs,last_tess=collections.Counter(ltess).most_common(),last_rapid=collections.Counter(lrap).most_common(),final=ltv)))
                continue
            cells[k]=None; stats['UNRESOLVED']+=1
            unresolved_readings[(pg,k)]=set(tvals+[v for v in ltess])|{v for v in [rv,lrv] if v is not None}|{norm_rapid(o)[0] for o in routs+lrap if norm_rapid(o)[0] is not None}
            issues.append((pg,labels[ri],heads[ci],'UNRESOLVED',dict(t6=t6,t4=t4,t6w=t6w,t4w=t4w,t7=t7,t8=t8,tblock=tx,rapid=routs,last_tess=collections.Counter(ltess).most_common(),last_rapid=collections.Counter(lrap).most_common())))
    # arithmetic tie-break: a lone unresolved candidate cell in a row is determined by Cast Votes - other candidates,
    # accepted only if that value is one of the engines' readings for the cell
    cand_cols=[i for i,h in enumerate(heads) if h not in ('Cast Votes','Undervotes','Overvotes') and 'Ballots' not in h and 'Registered' not in h and 'Turnout' not in h]
    if 'Cast Votes' in heads:
        cci=heads.index('Cast Votes')
        for ri in range(len(labels)):
            missing=[ci for ci in cand_cols if cells.get(f'{ri},{ci}') is None]
            if len(missing)==1 and cells.get(f'{ri},{cci}') is not None and all(cells.get(f'{ri},{ci}') is not None for ci in cand_cols if ci!=missing[0]):
                ci=missing[0]; derived=cells[f'{ri},{cci}']-sum(cells[f'{ri},{c}'] for c in cand_cols if c!=ci)
                reads=unresolved_readings.get((pg,f'{ri},{ci}'),set())
                if derived in reads:
                    cells[f'{ri},{ci}']=derived; stats['UNRESOLVED']-=1; stats['resolved by row arithmetic + engine reading']+=1
                    issues.append((pg,labels[ri],heads[ci],'resolved by row arithmetic (Cast Votes minus other candidates) = engine reading',derived,'readings seen:',sorted(reads)))
    final[pg]=dict(labels=labels,heads=heads,cells=cells)
    print(pg,dict(stats),flush=True)
json.dump(dict(pages=final,issues=issues,stats=stats),open(f'{base}/cells_final.json','w'),indent=0,default=str)
print(stats)
for i in issues: print(i)
