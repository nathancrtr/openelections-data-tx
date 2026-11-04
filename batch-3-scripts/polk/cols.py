from PIL import Image
import numpy as np, subprocess, tempfile, os, re
def header_band(a):
    rowfrac=((a>150)&(a<240)).mean(axis=1)
    on=rowfrac>0.08
    y=0; h=len(on)
    while y<h:
        if on[y]:
            s=y
            while y<h and on[y]: y+=1
            if y-s>300: return s,y
        else: y+=1
    return None
def columns(a,y0,y1):
    frac=(a[y0+15:y1-15]>236).mean(axis=0)
    gap=frac>0.6
    runs=[];start=None
    for x,v in enumerate(~gap):
        if v and start is None: start=x
        if not v and start is not None:
            if runs and start-runs[-1][1]<=1: runs[-1]=(runs[-1][0],x)
            elif x-start>40: runs.append((start,x))
            start=None
    # drop page-margin runs: boxes must be darker than background
    med=np.median(a[y0+15:y1-15],axis=0)
    runs=[(x0,x1) for x0,x1 in runs if np.median(med[x0:x1])<238 and x1-x0>40]
    return runs
def ocr_header(im, box, y0, y1):
    x0,x1=box
    crop=im.crop((x0,y0,x1,y1)).rotate(-90,expand=True)
    with tempfile.NamedTemporaryFile(suffix='.png',delete=False) as f:
        crop.save(f.name)
        txt=subprocess.run(['tesseract',f.name,'-','--psm','6'],capture_output=True,text=True).stdout
    os.unlink(f.name)
    txt=' '.join(txt.split())
    return txt
def page_columns(pg, base='.'):
    im=Image.open(f'{base}/rot/p-{pg:02d}.png').convert('L')
    a=np.array(im)
    b=header_band(a)
    if not b: return None
    runs=columns(a,*b)
    heads=[ocr_header(im,r,*b) for r in runs]
    return b, runs, heads
if __name__=='__main__':
    import sys
    for pg in sys.argv[1:]:
        r=page_columns(int(pg))
        print(pg, r[0]); 
        for run,h in zip(r[1],r[2]): print('   ',run,repr(h))
