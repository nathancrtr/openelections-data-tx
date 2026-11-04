"""Polk County, TX 2024 general: canvass packet (ES&S Canvass Results Report, scanned) -> OpenElections precinct CSV.
Numbers come from cells_final.json (tesseract + rapidocr agreement per cell, see polk/resolve.py)."""
import sys, os, json, re, collections, difflib
sys.path.insert(0, '/tmp/claude-0/-home-user/e8b9568f-2f39-5204-a78e-f8875e08ac54/scratchpad/scripts')
from oe import Row, write_csv, STATEWIDE
P='/tmp/claude-0/-home-user/e8b9568f-2f39-5204-a78e-f8875e08ac54/scratchpad/polk'
F=json.load(open(f'{P}/cells_final.json'))
pages=F['pages']; titles=json.load(open(f'{P}/titles_rapid.json'))
def tkey(t): return re.sub(r'[^a-z0-9]','',t.lower())
OFFICES={  # normalized title key -> (office, district)
 'presidentandvicepresident':('President',''),
 'unitedstatessenator':('U.S. Senate',''),
 'unitedstatesrepresentativedistrict8':('U.S. House','8'),
 'railroadcommissioner':('Railroad Commissioner',''),
 'justicesupremecourtplace2':('Justice, Supreme Court, Place 2',''),
 'justicesupremecourtplace4':('Justice, Supreme Court, Place 4',''),
 'justicesupremecourtplace6':('Justice, Supreme Court, Place 6',''),
 'presidingjudgecourtofcriminalappeals':('Presiding Judge, Court of Criminal Appeals',''),
 'judgecourtofcriminalappealsplace7':('Judge, Court of Criminal Appeals, Place 7',''),
 'judgecourtofcriminalappealsplace8':('Judge, Court of Criminal Appeals, Place 8',''),
 'staterepresentativedistrict9':('State Representative','9'),
 'justice9thcourtofappealsdistrictplace3':('Justice, 9th Court of Appeals District, Place 3',''),
 'justice9thcourtofappealsdistrictplace4':('Justice, 9th Court of Appeals District, Place 4',''),
 'districtjudge411thjudicialdistrict':('District Judge, 411th Judicial District',''),
 'sheriff':('Sheriff',''),
 'countytaxassessorcollector':('County Tax Assessor-Collector',''),
 'countycommissionerprecinct1':('County Commissioner Pct 1',''),
 'countycommissionerprecinct3':('County Commissioner Pct 3',''),
 'constableprecinct1':('Constable Pct 1',''),
 'constableprecinct2':('Constable Pct 2',''),
 'constableprecinct3':('Constable Pct 3',''),
 'constableprecinct4':('Constable Pct 4',''),
 'livingstonindependentschooldistrictschoolboardmembervotefornoneonetwoorthree':('Livingston Independent School District School Board Member',''),
 'leggettindependentschooldistrictschoolboardvotefornoneonetwothreeorfour':('Leggett Independent School District School Board',''),
 'cityoflivingstonmayorvotefornoneorone':('City of Livingston Mayor',''),
 'cityoflivingstonaldermanvotefornoneoneortwo':('City of Livingston Alderman',''),
}
STD={'Cast Votes':'cast','Undervotes':'under','Overvotes':'over','Absentee Voting Ballots Cast':'absentee','Early Voting Ballots Cast':'early_voting',
     'Election Day Voting Ballots Cast':'election_day','Total Ballots Cast':'total_ballots','Registered Voters':'registered','Turnout Percentage':'turnout'}
def std_head(h):
    k=tkey(h)
    for s,v in STD.items():
        if tkey(s)==k: return v
    return None
def parse_cand(h):
    h=' '.join(h.split())
    if h.endswith('(W)'): return h[:-3].strip()+' (W)', ''
    m=re.match(r'^(.*),\s*(REP|DEM|LIB|GRN|IND)$',h)
    if m: return m.group(1).strip(), m.group(2)
    return h, ''
# group pages into contests
contests=collections.OrderedDict()   # key -> dict(office,district,rows: label -> {colname: value}, cols order)
consumed=[]
header_fixes=[]
for pg in sorted(pages, key=int):
    d=pages[pg]; k=tkey(titles[pg])
    if k not in OFFICES: raise SystemExit(f'unknown title p{pg}: {titles[pg]}')
    office,dist=OFFICES[k]
    c=contests.setdefault(k,dict(office=office,district=dist,rows=collections.OrderedDict(),cands=[],pages=[]))
    c['pages'].append(int(pg)); consumed.append(int(pg))
    heads=list(d['heads']); labels=d['labels']
    first_is_cont = std_head(heads[0]) in ('early_voting','election_day','total_ballots','registered','turnout')
    # canonicalize OCR'd candidate headers against the first page of this contest with the same column layout (by position)
    ref=c.setdefault('ref_heads',{}).get(len(heads))
    if ref is None: c['ref_heads'][len(heads)]=heads
    else:
        for i,h in enumerate(heads):
            if h!=ref[i]:
                r=difflib.SequenceMatcher(None,h,ref[i]).ratio()
                assert r>0.8, (pg,h,ref[i],r)
                header_fixes.append((int(pg),h,'->',ref[i]))
                heads[i]=ref[i]
    if first_is_cont:
        # continuation of previous page's rows: labels must match the last len(labels) rows of this contest
        prev=list(c['rows'].keys())[-len(labels):]
        assert prev==labels, (pg, prev, labels)
    for ri,lab in enumerate(labels):
        assert lab is not None, (pg,ri)
        row=c['rows'].setdefault(lab,{})
        for ci,h in enumerate(heads):
            s=std_head(h)
            if s=='turnout': continue
            name=s or h
            if not s and h not in c['cands']: c['cands'].append(h)
            v=d['cells'].get(f'{ri},{ci}')
            assert name not in row, (pg,lab,name)
            row[name]=v
print('header OCR variants normalized by position:',header_fixes)
print('pages consumed:', len(consumed), 'of canvass pages 2-65 (64); total PDF pages 73 (p1 certificate, p66 end-of-report, p67-73 cumulative report)')
# checks
problems=[]
rows=[]
precincts=[l for l in contests['presidentandvicepresident']['rows'] if l!='Totals']
print('precincts (President contest):', len(precincts))
# Registered voters / ballots cast from President (county-wide) contest; verify identical across all county-wide contests
pres=contests['presidentandvicepresident']['rows']
for k,c in contests.items():
    for lab,row in c['rows'].items():
        if lab in pres and len(c['rows'])==len(pres):
            for f in ('absentee','early_voting','election_day','total_ballots','registered'):
                if row.get(f)!=pres[lab].get(f): problems.append(f'ballots/RV differ from President: {c["office"]} {lab} {f}: {row.get(f)} vs {pres[lab].get(f)}')
for lab in precincts:
    r=pres[lab]
    rows.append(Row(precinct=lab, office='Registered Voters', votes=r['registered']))
    rows.append(Row(precinct=lab, office='Ballots Cast', votes=r['total_ballots'], methods=dict(absentee=r['absentee'],early_voting=r['early_voting'],election_day=r['election_day'])))
    if r['absentee']+r['early_voting']+r['election_day']!=r['total_ballots']: problems.append(f'ballots cast method split != total: {lab} {r}')
for k,c in contests.items():
    office,dist=c['office'],c['district']
    canon={}
    if office in STATEWIDE:
        for party,name in STATEWIDE[office]:
            canon[party]=name
    sums=collections.Counter()
    for lab,row in c['rows'].items():
        if lab=='Totals': continue
        cast=0
        for h in c['cands']:
            name,party=parse_cand(h)
            if party in canon: name=canon[party]
            v=row[h]; cast+=v
            rows.append(Row(precinct=lab, office=office, district=dist, party=party, candidate=name, votes=v))
            sums[h]+=v
        rows.append(Row(precinct=lab, office=office, district=dist, candidate='Under Votes', votes=row['under']))
        rows.append(Row(precinct=lab, office=office, district=dist, candidate='Over Votes', votes=row['over']))
        sums['under']+=row['under']; sums['over']+=row['over']; sums['cast']+=row['cast']
        if cast!=row['cast']: problems.append(f'candidate sum != Cast Votes: {office} {lab}: {cast} vs {row["cast"]}')
        if row['cast']+row['under']+row['over']!=row['total_ballots']: problems.append(f'cast+under+over != total ballots: {office} {lab}: {row["cast"]}+{row["under"]}+{row["over"]} vs {row["total_ballots"]}')
    tot=c['rows'].get('Totals')
    if not tot: problems.append(f'no Totals row for {office}'); continue
    for h in c['cands']+['under','over','cast']:
        if sums[h]!=tot[h]: problems.append(f'precinct sum != source Totals: {office} [{h}]: {sums[h]} vs {tot[h]}')
    for f in ('absentee','early_voting','election_day','total_ballots','registered'):
        s=sum(row[f] for lab,row in c['rows'].items() if lab!='Totals')
        if s!=tot[f]: problems.append(f'precinct sum != source Totals: {office} [{f}]: {s} vs {tot[f]}')
path=write_csv('Polk', rows, methods=['absentee','early_voting','election_day'])
print('wrote',path,len(rows),'rows')
print('offices:',[ (c['office'],c['district'],len([l for l in c['rows'] if l!='Totals']),'precincts',c['cands']) for c in contests.values()])
print('PROBLEMS:',len(problems))
for p in problems: print('  ',p)
json.dump({k:dict(office=c['office'],district=c['district'],cands=c['cands'],totals=c['rows'].get('Totals')) for k,c in contests.items()},open(f'{P}/contest_totals.json','w'),indent=1)
