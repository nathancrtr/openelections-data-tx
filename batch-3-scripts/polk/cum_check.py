"""Cross-check canvass contest totals against the Official Cumulative Results Report (pages 67-73), OCR'd with tesseract (psm 6) and rapidocr."""
import json,re,os
base=os.path.dirname(os.path.abspath(__file__))
C=json.load(open(f'{base}/contest_totals.json'))
def key(s): return re.sub(r'[^a-z0-9]','',s.lower())
def lines_for(eng):
    out=[]
    for pg in range(67,74):
        if eng=='tess':
            out+=[l.strip() for l in open(f'{base}/cum/p-{pg}.txt')]
        else:
            d=json.load(open(f'{base}/rapid/p-{pg:02d}.json'))
            items=sorted([((min(p[1] for p in b)+max(p[1] for p in b))/2, min(p[0] for p in b), t) for b,t,s in d])
            cur=[]
            for y,x,t in items:
                if cur and abs(y-cur[-1][0])>22:
                    out.append(' '.join(t for _,_,t in sorted(cur,key=lambda z:z[1]))); cur=[]
                cur.append((y,x,t))
            if cur: out.append(' '.join(t for _,_,t in sorted(cur,key=lambda z:z[1])))
    return out
title_keys={key(re.sub(r'\s*-\s*Vote for.*$','',t)):k for k,t in [(k,k) for k in C]}
res=[]
for eng in ('tess','rapid'):
    L=lines_for(eng)
    # section boundaries: a line whose key starts with a contest key (titles are unique prefixes after removing 'vote for' text)
    sections={}; cur=None
    for l in L:
        k=key(l)
        hit=[ck for ck in C if k.startswith(ck[:min(len(ck),40)]) and len(k)<=len(ck)+30]
        if hit:
            cur=max(hit,key=len); sections.setdefault(cur,[]); continue
        if cur: sections[cur].append(l)
    for ck,c in C.items():
        tot=c['totals']; sec=sections.get(ck,[])
        def find(name):
            nk=key(name)
            for l in sec:
                lk=key(l)
                if lk.startswith(nk[:max(6,len(nk)-2)]) or (len(nk)>8 and nk[:8] in lk[:len(nk)+4]):
                    nums=re.findall(r'\d[\d,]*',l)
                    nums=[n.replace(',','') for n in nums]
                    return l,nums
            return None,[]
        for h in c['cands']:
            name=re.sub(r',\s*(REP|DEM|LIB|GRN)$','',h)
            l,nums=find(name)
            # candidate line: n1 p1 n2 p2 n3 p3 n4 p4 -> total is the 7th numeric token when percentages have decimals
            toks=re.findall(r'[\d,]+(?:\.\d+)?%?',l or '')
            vals=[t for t in toks if not t.endswith('%')]
            v=int(vals[3].replace(',','')) if len(vals)>=4 and vals[3].replace(',','').isdigit() else None
            res.append((c['office'],name,eng,v,tot[h],'OK' if v==tot[h] else 'DIFF'))
        for lab,fk in (('under','Undervotes'),('over','Overvotes')):
            l,nums=find(fk)
            v=int(nums[-1]) if nums and nums[-1].isdigit() else None
            res.append((c['office'],fk,eng,v,tot[lab],'OK' if v==tot[lab] else 'DIFF'))
ok=sum(1 for r in res if r[-1]=='OK'); print('cumulative-report cross-check: OK',ok,'of',len(res))
for r in res:
    if r[-1]!='OK': print('  DIFF/unparsed:',r)
