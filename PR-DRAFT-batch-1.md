# PR draft: 2024 general precinct results, batch 1 (ten counties that had a source file)

Draft text for the owner to use; nothing has been posted to any OpenElections
repository. Branch `2024-general-batch-1` in `nathancrtr/openelections-data-tx`
(this repo) and `nathancrtr/openelections-sources-tx` (source notes).

## Suggested PR title

Add 2024 general precinct results for Hill, McMullen, Newton, Terrell, Webb,
Wichita, Wilson, Yoakum (and Cochran with a source caveat)

## Suggested PR body

Precinct-level results for the November 5, 2024 general election, converted
from the source files already in openelections-sources-tx. Offices included:
Registered Voters and Ballots Cast where the source has them, President,
U.S. Senate, U.S. House, Railroad Commissioner, State Senate, State
Representative, County Attorney, Sheriff, County Tax Assessor-Collector.
Write-ins are one `Write-ins` row per precinct and office; over/under votes
are `Over Votes` / `Under Votes` rows. Parties are REP/DEM/LIB/GRN/IND.

| county | source (openelections-sources-tx, 2024/general) | official? | precincts | method columns | data tests | TLC reconciliation |
|---|---|---|---|---|---|---|
| Hill | `2024 Hill County, TX precinct-level results.pdf` (Hart precinct-by-precinct, 65 pp) | official | 13 | absentee, early_voting, election_day | pass | exact |
| McMullen | `2024 McMullen County, TX precinct-level results.pdf` (scanned Electionware summary reports) | unofficial (11/18/2024 run) | 4 + Early Voting + Mail | absentee, early_voting, election_day | pass | exact (1 President write-in TLC does not credit) |
| Newton | `2024 Newton County, TX precinct-level results.pdf` (official canvass) | official | 21 voting boxes (11, 13, 21 combined) | early_voting, election_day | pass | exact (1 Senate write-in) |
| Terrell | three `2024 Terrell County, TX precinct-level results *.xlsx` | unstated | 4 | absentee, early_voting, election_day | pass | exact |
| Webb | `2024 Webb County, TX precinct-level results.pdf` (scanned Electionware PCT by PCT, 88 pp) | unofficial (11/13/2024 run) | 78 | none (totals only) | see below | see below |
| Wichita | `2024 Wichita County, TX precinct-level results.pdf` (Hart precinct results report, 375 pp) | official | 52 | absentee, early_voting, election_day | pass | exact; also 0 differences against the county summary PDF for President and U.S. Senate |
| Wilson | `2024 Wilson County, TX precinct-level results.txt` (fixed-width export) | unstated | 13 | absentee, early_voting, election_day | pass | exact (26 Senate write-ins TLC does not credit) |
| Yoakum | `2024 Yoakum County, TX precinct-level results.csv` (SOS precinct-by-precinct export) | unstated | 6 | absentee, early_voting, election_day (see note) | pass | exact (2 Senate write-ins) |
| Cochran | `2024 Cochran County, TX precinct-level results.pdf` (tally sheet) | unofficial | 5 boxes + Early Voting + Mail | absentee, early_voting, election_day | pass | +5%, see known issues |

"TLC reconciliation" compares each file's President and U.S. Senate
candidate totals with the Texas Legislative Council 2024 General VTD returns
(details in `2024/counties/RECONCILIATION-2024.md` on the branch, not meant
for upstream).

Checks run on every file: the four data tests at
openelections-data-tests v2.2.0 (file_format, duplicate_entries,
missing_values, vote_breakdown_totals); precinct count against the source;
every source page parsed (page counts asserted for the PDFs); the source's
own totals rows or columns matched before the external reconciliation.

## Not included

- **Rains**: the file in openelections-sources-tx is a Hart export of local
  contests only (Proposition A, school trustee, mayor, city council); it has
  no general election contest. The county posts only cumulative reports for
  November 2024. Records-request contact is in the sources branch
  (`2024/general/SOURCES-2024-found.md`).

## Known issues (kept as the source prints them)

- **Cochran**: the tally sheet's EV column exceeds the EV ballots cast in
  every contest and equals EV + mail; its TOTAL column therefore
  double-counts mail ballots, and county totals come out about 5% above TLC
  (Trump 777 vs 735, Cruz 749 vs 706). Subtracting the BBM column from EV
  reproduces TLC within one vote for every President and Senate candidate.
  The file reproduces the sheet as printed: `Early Voting` and `Mail`
  pseudo-precincts plus five election-day boxes. Also as printed: U.S. House
  Nathan Lewis TOTAL is 5 where the columns sum to 53. Recommend holding
  Cochran until an official precinct report is obtained, or accepting it
  with this note.
- **Yoakum**: the SOS export has three rows per precinct with no vote-type
  label. They were taken as absentee, early voting, election day in that
  order (the standard order of that export; magnitudes 7 / 494 / 132 ballots
  for precinct 101 are consistent with it). Totals do not depend on the
  assumption.
- **Terrell**: no party labels in the sheets; parties were filled from the
  Texas SOS 2024 ballot certification. Candidate names kept as typed in the
  sheets, including "COLIN ALRED" and "HOLLY TALYLOR". The sheets combine
  "SHERIFF/COUNTY TAX ASSESSOR-COLLECTOR" into one office; the file uses
  that combined office name.
- **Newton**: the canvass has Early Vote and Election Day sections only
  (mail ballots are inside Early Vote); the Provisional Ballots row is not
  carried. Registered voters are not in the canvass.
- **Wichita**: the report header says 53 precincts reporting; 52 precinct
  splits appear in the report and the county totals match TLC exactly, so
  nothing is missing. Precinct names are the report's split codes
  (`102-CTYW1` etc.). The report's "COUNTY TAX ASSESOR-COLLECTOR" typo is
  normalised. No registered-voter or ballots-cast figures per precinct in
  the report.
- **Hill**: Jill Stein's party code GRE normalised to GRN.
- **McMullen**: early voting and mail are county-wide (`Early Voting` and
  `Mail` pseudo-precincts); election-day votes are per precinct (`Pct 1` to
  `Pct 4`). The Pct 3 report has no handwritten label; it was identified by
  being the only election-day report with the County Commissioner Pct 3
  contest. Registered voters print as 0. Four cells were read by eye after
  the OCR passes disagreed, each listed in the OCR notes below.
- **Webb**: see the Webb section below.

## OCR notes, McMullen

Two tesseract passes (page segmentation modes 6 and 11, 2x upscale) plus a
template digit reader on every numeric cell; a value was accepted only when
the passes agreed or the row arithmetic (TOTAL = Absentee + Early Voting,
candidates + write-ins = Total Votes Cast) picked a unique reading, and
every row's printed percentage was re-derived from the accepted totals.
Visual reads:

- report Pct 4, Ballots Cast - Total: 28 (two passes read 2, one read 28).
- report Pct 4, Sheriff, Overvotes row: 0 0.00% 0 (line missed by tesseract).
- report Pct 1, Railroad Commissioner, Hawk Dunlap: 0 0.00% 0 (percentage misread as 9.00%).
- report Pct 4, Sheriff, Emmett "Bubba" Shelton: 24 85.71% 24 (percentage misread as 85.74%).

Arithmetic-resolved cells (passes disagreed, sum decided): EV report U.S.
House Jay Furman absentee 17 (one pass read 7); Pct 4 U.S. House Jay Furman
election day 18 (template reader 13); Pct 4 U.S. House undervotes 0 (one
pass read 6).

## Webb

(filled in below once the Webb conversion is complete)
