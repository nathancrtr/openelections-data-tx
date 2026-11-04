"""Helpers for writing OpenElections TX 2024 county precinct CSVs and checking them.

Usage from a converter:
    import sys; sys.path.insert(0, '/tmp/claude-0/-home-user/e8b9568f-2f39-5204-a78e-f8875e08ac54/scratchpad/scripts')
    from oe import Row, write_csv
    rows = [Row(precinct='101', office='President', party='REP', candidate='Donald J. Trump', votes=976, early_voting=767, election_day=192, absentee=17), ...]
    write_csv('Jackson', rows, methods=['absentee','early_voting','election_day'])
"""
import csv, io, os, re, sys
from dataclasses import dataclass, field

DATA_REPO = '/home/user/openelections-data-tx'

# canonical names (as used by the 184 finished 2024 files)
STATEWIDE = {
    'President': [('REP', 'Donald J. Trump'), ('DEM', 'Kamala D. Harris'), ('LIB', 'Chase Oliver'), ('GRN', 'Jill Stein')],
    'U.S. Senate': [('REP', 'Ted Cruz'), ('DEM', 'Colin Allred'), ('LIB', 'Ted Brown')],
    'Railroad Commissioner': [('REP', 'Christi Craddick'), ('DEM', 'Katherine Culbert'), ('LIB', 'Hawk Dunlap'), ('GRN', 'Eddie Espinoza')],
}
PSEUDO = ('Write-ins', 'Over Votes', 'Under Votes')
ALL_METHODS = ['absentee', 'early_voting', 'election_day', 'provisional', 'mail']

@dataclass
class Row:
    precinct: str
    office: str
    votes: int
    district: str = ''
    party: str = ''
    candidate: str = ''
    methods: dict = field(default_factory=dict)   # e.g. {'early_voting': 10, 'election_day': 5, 'absentee': 1}

def county_slug(county):
    return county.lower().replace(' ', '_')

def out_path(county):
    return os.path.join(DATA_REPO, '2024', 'counties', f"20241105__tx__general__{county_slug(county)}__precinct.csv")

def _q(s):
    """quote a string field the way the finished files do"""
    s = str(s)
    return '"' + s.replace('"', '""') + '"'

def write_csv(county, rows, methods=None, path=None):
    """methods: ordered list of method column names to emit (subset of ALL_METHODS or other lowercase names).
    Registered Voters rows get empty method cells; everything else gets the row's method values (empty if missing)."""
    path = path or out_path(county)
    methods = methods or []
    header = ['county', 'precinct', 'office', 'district', 'party', 'candidate', 'votes'] + methods
    lines = [','.join(header)]
    for r in rows:
        cells = [county, str(r.precinct), _q(r.office), str(r.district), str(r.party),
                 _q(r.candidate) if r.candidate else '', str(r.votes)]
        for m in methods:
            v = r.methods.get(m, '')
            cells.append('' if v == '' or v is None else str(v))
        lines.append(','.join(cells))
    with open(path, 'w', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    return path

def read_csv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def sum_by_candidate(path, offices=('President', 'U.S. Senate')):
    out = {}
    for r in read_csv(path):
        if r['office'] in offices:
            k = (r['office'], r['party'], r['candidate'])
            out[k] = out.get(k, 0) + int(float(r['votes']))
    return out
