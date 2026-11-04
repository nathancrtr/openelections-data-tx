# per page: detect header band+columns, OCR headers, crop table, tesseract psm6 & psm4 tsv
import json, os, sys, subprocess
from PIL import Image
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cols import header_band, columns, ocr_header
os.environ['OMP_THREAD_LIMIT']='1'
base=os.path.dirname(os.path.abspath(__file__))
os.makedirs(f'{base}/meta',exist_ok=True); os.makedirs(f'{base}/tbl',exist_ok=True)
for pg in range(int(sys.argv[1]), int(sys.argv[2])+1):
    im=Image.open(f'{base}/rot/p-{pg:02d}.png').convert('L'); a=np.array(im)
    b=header_band(a)
    if not b:
        json.dump({'band':None},open(f'{base}/meta/p-{pg:02d}.json','w')); print(pg,'no band'); continue
    runs=columns(a,*b)
    heads=[ocr_header(im,r,*b) for r in runs]
    y1=b[1]
    crop=im.crop((0,y1,im.size[0],im.size[1])); crop.save(f'{base}/tbl/p-{pg:02d}.png')
    for psm in ('6','4'):
        subprocess.run(['tesseract',f'{base}/tbl/p-{pg:02d}.png',f'{base}/tess/p-{pg:02d}-{psm}','--psm',psm,'tsv'],capture_output=True)
    json.dump({'band':b,'cols':runs,'heads':heads,'crop_y':y1},open(f'{base}/meta/p-{pg:02d}.json','w'))
    print(pg,len(runs),heads,flush=True)
