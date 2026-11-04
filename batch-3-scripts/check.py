"""Run the four CI tests and the TLC reconciliation on one county file.
   python3 -I check.py <County>"""
import sys, os, json, subprocess, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from oe import out_path, sum_by_candidate, DATA_REPO, PSEUDO
S = '/tmp/claude-0/-home-user/e8b9568f-2f39-5204-a78e-f8875e08ac54/scratchpad'
county = sys.argv[1]
path = out_path(county)
rel = os.path.relpath(path, DATA_REPO)
ok = True
for t in ['file_format', 'duplicate_entries', 'missing_values', 'vote_breakdown_totals']:
    p = subprocess.run([sys.executable, f'{S}/tests/openelections-data-tests/run_tests.py', t, DATA_REPO, '--files', rel],
                       capture_output=True, text=True)
    res = 'OK' if p.returncode == 0 and 'OK' in p.stdout + p.stderr else 'FAIL'
    if res != 'OK':
        ok = False
        print(f"[{t}] FAIL\n{p.stdout[-1500:]}{p.stderr[-1500:]}")
    else:
        print(f"[{t}] OK")

tlc = json.load(open(f'{S}/tlc/batch3_tlc.json'))[county]
mine = sum_by_candidate(path)
LAST = {'Donald J. Trump': 'Trump', 'Kamala D. Harris': 'Harris', 'Chase Oliver': 'Oliver', 'Jill Stein': 'Stein',
        'Ted Cruz': 'Cruz', 'Colin Allred': 'Allred', 'Ted Brown': 'Brown'}
OFF = {'President': 'President', 'U.S. Senate': 'U.S. Sen'}
print(f"\nTLC reconciliation for {county} (TLC VTDs: {len(tlc['vtds'])})")
rows = []
worst = 0.0
for (office, party, cand), v in sorted(mine.items()):
    if cand in PSEUDO or cand not in LAST:
        continue
    key = f"{OFF[office]}|{LAST[cand]}|{party[0]}"
    t = tlc['totals'].get(key)
    d = None if t is None else v - t
    rows.append((office, cand, v, t, d))
    print(f"  {office:12s} {cand:18s} file={v:7d} tlc={t} diff={d}")
tot_file = sum(v for (o, p, c), v in mine.items() if o == 'President' and c not in PSEUDO)
tot_tlc = sum(v for k, v in tlc['totals'].items() if k.startswith('President|'))
absdiff = sum(abs(d) for *_, d in rows if d is not None)
print(f"  President total file={tot_file} tlc={tot_tlc}; sum |diff| over listed candidates = {absdiff} ({100*absdiff/max(tot_tlc,1):.3f}% of TLC president votes)")
precs = sorted({r['precinct'] for r in csv.DictReader(open(path))})
print(f"  precincts in file: {len(precs)}")
print("RESULT:", "OK" if ok else "TESTS FAILED")
