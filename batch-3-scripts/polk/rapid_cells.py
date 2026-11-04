import json, os, sys
import numpy as np
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
base=os.path.dirname(os.path.abspath(__file__))
eng=RapidOCR()
d=json.load(open(f'{base}/tess_parsed.json'))
CFGS=[(10,10,1,True,170),(10,10,1,True,200),(10,10,1.5,True,170),(10,10,0.8,True,170)]
def variant(crop,bb,padx,pady,scale,bin,thr):
    xa,y0,xb,y1=bb
    c=crop.crop((max(0,xa-padx),max(0,y0-pady),xb+padx+1,y1+pady+1))
    if bin: c=c.point(lambda v:255 if v>thr else 0)
    w,h=c.size; c=c.resize((max(8,int(w*scale)),max(8,int(h*scale))),Image.LANCZOS)
    return np.array(c.convert('RGB'))
out={}
for pg in range(2,66):
    p=d[str(pg)]['p6']
    if not p: continue
    im=Image.open(f'{base}/rot/p-{pg:02d}.png').convert('L')
    cols=p['cols']; heads=p['heads']
    res={}
    for ri,r in enumerate(p['rows']):
        yc=r['yc']
        for ci,(x0,x1) in enumerate(cols):
            if 'Turnout' in heads[ci]: continue
            crop=im.crop((x0-6,int(yc)-30,x1+6,int(yc)+30)); a=np.array(crop)
            ink=np.where(a<150)
            if len(ink[0])==0: res[f'{ri},{ci}']=['<blank>']; continue
            bb=(ink[1].min(),ink[0].min(),ink[1].max(),ink[0].max())
            outs=[]
            for cfg in CFGS:
                rr=eng.text_recognizer([variant(crop,bb,*cfg)])[0][0]
                outs.append(rr[0])
            res[f'{ri},{ci}']=outs
    out[pg]=res
    print(pg,len(res),flush=True)
    json.dump(out,open(f'{base}/rapid_cells.json','w'))
