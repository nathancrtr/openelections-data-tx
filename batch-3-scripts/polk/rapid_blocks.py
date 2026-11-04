# rapid pass B: detection+recognition on 3-column blocks, upscaled 2x, several DB thresholds; map boxes to cells
import json, os, sys
import numpy as np
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
base=os.path.dirname(os.path.abspath(__file__))
eng=RapidOCR()
d=json.load(open(f'{base}/tess_parsed.json'))
CFG=[(0.1,0.2,2.0,2),(0.3,0.5,1.6,2),(0.1,0.2,2.0,1.5)]
out={}
for pg in range(2,66):
    p=d[str(pg)]['p6']
    if not p: continue
    im=Image.open(f'{base}/rot/p-{pg:02d}.png').convert('L')
    cols=p['cols']; rows=p['rows']; heads=p['heads']
    y0=int(rows[0]['yc'])-35; y1=int(rows[-1]['yc'])+35
    res={}
    for ca in range(0,len(cols),3):
        cb=min(ca+3,len(cols))
        x0=cols[ca][0]-10; x1=cols[cb-1][1]+10
        for thr,bt,un,scale in CFG:
            crop=im.crop((x0,y0,x1,y1)); crop=crop.resize((int(crop.size[0]*scale),int(crop.size[1]*scale)),Image.LANCZOS)
            eng.text_detector.postprocess_op.thresh=thr
            r,_=eng(np.array(crop.convert('RGB')),box_thresh=bt,unclip_ratio=un,text_score=0.1)
            for box,txt,sc in (r or []):
                xc=x0+sum(pt[0] for pt in box)/4/scale; yc=y0+sum(pt[1] for pt in box)/4/scale
                ci=next((i for i in range(ca,cb) if cols[i][0]-8<=xc<=cols[i][1]+8),None)
                ri=next((i for i,rr in enumerate(rows) if abs(rr['yc']-yc)<25),None)
                if ci is None or ri is None: continue
                res.setdefault(f'{ri},{ci}',[]).append(txt)
    out[pg]=res
    print(pg,len(res),flush=True)
    json.dump(out,open(f'{base}/rapid_blocks.json','w'))
