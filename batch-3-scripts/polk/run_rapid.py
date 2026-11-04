import json, sys
from rapidocr_onnxruntime import RapidOCR
eng = RapidOCR()
base='/tmp/claude-0/-home-user/e8b9568f-2f39-5204-a78e-f8875e08ac54/scratchpad/polk'
for i in range(2,74):
    res, _ = eng(f'{base}/rot/p-{i:02d}.png')
    out = [[box, txt, float(sc)] for box, txt, sc in (res or [])]
    json.dump(out, open(f'{base}/rapid/p-{i:02d}.json','w'))
    print(i, len(out), flush=True)
open(f'{base}/rapid/DONE','w').write('done')
