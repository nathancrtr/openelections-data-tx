# stage 1: per page, rows (from tesseract labels) and tesseract cell values (psm6, psm4)
import json, os, re, csv, sys
base=os.path.dirname(os.path.abspath(__file__))
CANON=['1','1 - LVISD','2 - LVISD','3','3 - LVISD','4 - CITY-LVISD','4 - LVISD','5 - LVISD','6','6 - LVISD','7 - CITY-LVISD',
 '8 - LEGGISD','8 - CITY-LVISD','8 - LVISD','9','9 - LVISD','9 - LEGGISD','10','11','11 - LEGGISD','12','13','14','14 - LVISD','14 - LEGGISD',
 '15','15 - CITY-LVISD','15 - LVISD','16','16 - CITY-LVISD','16 - LVISD','17','17 - LVISD','18 - CITY-LVISD','18 - LVISD','19 - LVISD',
 '20','20 - LVISD','21','21 - CITY-LVISD','21 - LVISD','22 - LVISD','Totals']
def norm_label(s):
    s=s.upper().replace(' ','').replace('—','-').replace('–','-').replace('_','-')
    s=re.sub(r'^[^0-9A-Z]+','',s)
    # leading digits may be misread
    m=re.match(r'^([0-9OIL|]+)(.*)$',s)
    if m:
        d=m.group(1).replace('O','0').replace('I','1').replace('L','1').replace('|','1'); s=d+m.group(2)
    s=s.replace('LV1SD','LVISD').replace('LEGG1SD','LEGGISD').replace('C1TY','CITY')
    return s
CANON_N={norm_label(c):c for c in CANON}
def read_tsv(path):
    rows=[]
    with open(path, newline='') as f:
        for r in csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE):
            if r['text'] is None or r['text'].strip()=='' or int(r['level'])!=5: continue
            rows.append(dict(x=int(r['left']),y=int(r['top']),w=int(r['width']),h=int(r['height']),text=r['text'],conf=float(r['conf']),
                             line=(r['block_num'],r['par_num'],r['line_num'])))
    return rows
NUM=re.compile(r'^([0-9][0-9,]*)$')
def parse_page(pg, psm):
    m=json.load(open(f'{base}/meta/p-{pg:02d}.json'))
    if not m.get('band'): return None
    cy=m['crop_y']; cols=m['cols']
    words=read_tsv(f'{base}/tess/p-{pg:02d}-{psm}.tsv')
    for w in words: w['y']+=cy; w['xc']=w['x']+w['w']/2; w['yc']=w['y']+w['h']/2
    label_x_max=cols[0][0]-30
    # label words: group into lines by y
    lab=[w for w in words if w['x']<label_x_max and w['x']>50]
    lab.sort(key=lambda w:w['yc'])
    rows=[]
    for w in lab:
        if rows and abs(w['yc']-rows[-1]['yc'])<22:
            rows[-1]['words'].append(w); rows[-1]['yc']=sum(x['yc'] for x in rows[-1]['words'])/len(rows[-1]['words'])
        else: rows.append(dict(yc=w['yc'],words=[w]))
    out_rows=[]
    for r in rows:
        txt=' '.join(w['text'] for w in sorted(r['words'],key=lambda w:w['x']))
        n=norm_label(txt)
        canon=CANON_N.get(n)
        if canon is None and n.startswith('TOTAL'): canon='Totals'
        out_rows.append(dict(yc=r['yc'],raw=txt,label=canon))
    # cells
    cells={}
    extras=[]
    for w in words:
        if w['x']<label_x_max: continue
        mm=NUM.match(w['text'])
        if not mm: 
            if re.search(r'\d',w['text']) and not w['text'].endswith('%'): extras.append((w['text'],w['x'],w['y']))
            continue
        ci=None
        for i,(x0,x1) in enumerate(cols):
            if x0-8<=w['xc']<=x1+8: ci=i;break
        ri=None
        for i,r in enumerate(out_rows):
            if abs(r['yc']-w['yc'])<25: ri=i;break
        if ci is None or ri is None: extras.append((w['text'],w['x'],w['y'],ci,ri)); continue
        val=int(mm.group(1).replace(',',''))
        if (ri,ci) in cells: extras.append(('dup',w['text'],cells[(ri,ci)],ri,ci))
        cells[(ri,ci)]=val
    return dict(rows=out_rows,cells={f'{r},{c}':v for (r,c),v in cells.items()},extras=extras,cols=cols,heads=m['heads'])
if __name__=='__main__':
    res={}
    for pg in range(2,66):
        p6=parse_page(pg,'6'); p4=parse_page(pg,'4')
        res[pg]=dict(p6=p6,p4=p4)
        if p6:
            labs=[r['label'] for r in p6['rows']]
            bad=[r['raw'] for r in p6['rows'] if r['label'] is None]
            print(pg,len(p6['rows']),'cells',len(p6['cells']),'expected',len(p6['rows'])*len(p6['cols']),'bad labels',bad,'extras',p6['extras'][:5])
    json.dump(res,open(f'{base}/tess_parsed.json','w'))
