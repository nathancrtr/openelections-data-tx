# PR draft: 2024 general election precinct results, 13 counties

Unified draft covering all three batches. Nothing has been posted to any
OpenElections repository; the owner opens the PR. The per-batch drafts
(`PR-DRAFT-batch-1.md`, `-2.md`, `-3.md`) carry the full per-county detail
and are the place to copy from if the owner prefers three PRs.

Branch: `2024-general-all` in `nathancrtr/openelections-data-tx` (this repo)
and in `nathancrtr/openelections-sources-tx` (new source files for Clay,
Erath, Haskell and Polk, plus the source logs).

## Suggested title

Add 2024 general precinct results for 13 counties (Clay, Cochran, Erath,
Haskell, Hill, McMullen, Newton, Polk, Terrell, Webb, Wichita, Wilson,
Yoakum)

## Suggested body

Precinct-level results for the November 5, 2024 general election for 13 of
the 70 counties still open on #458. Nine come from source files already in
openelections-sources-tx; four (Clay, Erath, Haskell, Polk) from documents
found on county sites or in commissioners court canvass packets, now added
to the sources repo.

| county | source | official? | precincts | method columns | notes |
|---|---|---|---|---|---|
| Clay | Clarity ENR precinct detail XML (version 353790) | unlabelled, pre-canvass; matches TLC exactly | 16 | absentee, early_voting, election_day, provisional | |
| Cochran | county tally sheet PDF | unofficial | 5 boxes + Early Voting + Mail | absentee, early_voting, election_day | source caveat, see known issues |
| Erath | county cast vote record xlsx, aggregated | unlabelled; matches TLC exactly | 21 | none | write-in rows are ballots with a write-in mark, see known issues |
| Haskell | scanned county spreadsheet "GENERAL ELECTION BBM, EV & ED" | unlabelled | 10 | early_voting, election_day, mail | OCR, see notes |
| Hill | Hart precinct-by-precinct PDF | official | 13 | absentee, early_voting, election_day | |
| McMullen | scanned Electionware summary reports | unofficial (11/18/2024 run) | 4 + Early Voting + Mail | absentee, early_voting, election_day | OCR, see notes |
| Newton | official canvass PDF | official | 21 voting boxes | early_voting, election_day | |
| Polk | commissioners court canvass packet, ES&S Canvass Results Report | official (11/15/2024 run) | 42 (22 precincts split by ISD and city) | absentee, early_voting, election_day on Ballots Cast only | OCR; all 26 contests included |
| Terrell | three xlsx tally sheets | unlabelled | 4 | absentee, early_voting, election_day | parties from SOS certification |
| Webb | scanned Electionware PCT by PCT tables | unofficial (11/13/2024 run) | 78 | none | OCR, see notes |
| Wichita | Hart precinct results report PDF | official | 52 precinct splits | absentee, early_voting, election_day | |
| Wilson | fixed-width text export | unlabelled | 13 | absentee, early_voting, election_day | |
| Yoakum | SOS precinct-by-precinct CSV export | unlabelled | 6 | absentee, early_voting, election_day (inferred order) | |

Checks on every file: the four data tests at openelections-data-tests
v2.2.0; precinct count against the source; every source page parsed; the
source's own totals matched before any external check; and President and
U.S. Senate totals by candidate against the Texas Legislative Council 2024
General VTD returns (per-county tables in
`2024/counties/RECONCILIATION-2024.md` on the branch, not meant for merge).
Every named candidate matches TLC exactly in all 13 counties except
Cochran. Erath (Trump, all 21 precincts) and Webb (1,115 cells across five
offices, plus ballots cast in all 78 precincts) were also checked precinct
by precinct against TLC.

## Decisions for the owner

- **Cochran**: the tally sheet's EV column equals EV + mail in every
  contest, so its totals double-count mail ballots and the county comes out
  about 5% above TLC (Trump 777 vs 735, Cruz 749 vs 706). Subtracting the
  mail column from EV reproduces TLC within one vote. The file is the sheet
  as printed. Hold it, or accept it with this note.
- **Write-in style is not uniform.** Eleven files use one `Write-ins` row
  per precinct and office as #458 asks. Haskell and Polk carry the certified
  write-in candidates by name (Haskell following the existing Archer file;
  in Haskell the Sheriff race was won by write-in CJ Saucedo, 1,187 to 937).
  Collapsing them is a one-line change if a single row is preferred.
- **Offices.** Twelve files carry the offices #458 lists (plus Registered
  Voters and Ballots Cast where the source has them). Polk carries all 26
  contests in its canvass report.
- **Erath write-ins.** The CVR's write-in rows count ballots with a write-in
  mark. For President that equals the certified write-in total (50, matching
  TLC); for U.S. House 25 it is 428 against 23 credited by TLC. Drop the
  U.S. House write-in rows if that is unwanted.
- **Official status.** Clay, Erath, Haskell, Terrell, Wilson and Yoakum
  sources carry no official/unofficial label; McMullen and Webb are
  unofficial runs (county totals match TLC exactly, so the figures were not
  changed at canvass); Cochran is unofficial. Hill, Newton, Polk and Wichita
  are official.

## Known issues kept as the sources print them

- Cochran: U.S. House Nathan Lewis TOTAL prints 5 where its columns sum to 53.
- Haskell: seven cells where the per-method sections and the combined grid
  disagree, listed in `PR-DRAFT-batch-2.md`; the file follows the per-method
  sections. Names as printed (`Jody C. Arrington`, `Christoper Keith`).
- Polk: "Total Ballots Cast" differs from Cast Votes + Under + Over in four
  ISD sub-precincts; the report header says 24,381 ballots and its Totals
  row 24,361; Registered Voters prints 0 for ISD/city sub-precincts. All
  kept as printed.
- Terrell: candidate names as typed in the sheets (`COLIN ALRED`, `HOLLY
  TALYLOR`); "SHERIFF/COUNTY TAX ASSESSOR-COLLECTOR" is one combined office.
- Yoakum: the export's three unlabelled rows per precinct were taken as
  absentee, early voting, election day in that order; totals do not depend
  on it.
- Newton: Early Vote and Election Day sections only (mail is inside Early
  Vote); provisional row not carried; no registered voters in the canvass.
- Wichita: header says 53 precincts, 52 appear; county totals match TLC
  exactly. Report typo "ASSESOR" normalised.
- Webb and McMullen: registered voters print as 0 and are not carried.
- Precinct names are as the sources print them (`401-01`, `SE HENRIETT`,
  `102-CTYW1`, `4 - LVISD`, `Box 101`).

## OCR notes (four scanned sources)

Each scanned source was read by two independent engines or modes and a
value was accepted only on agreement or when the document's own arithmetic
(candidate sums, printed percentages, printed totals rows) left one
possibility. Cells settled by a visual read of the scan are listed with the
arithmetic they satisfy:

- McMullen (`PR-DRAFT-batch-1.md`): 4 visual reads, 3 arithmetic-resolved cells.
- Webb (`PR-DRAFT-batch-1.md`): 7 visual reads; column sums match the
  report's printed Totals row for every required column; 1,115 cells match
  TLC per precinct.
- Haskell (`PR-DRAFT-batch-2.md`): 4 visual reads, two re-checked by a
  second reader; no unresolved cells.
- Polk (`PR-DRAFT-batch-3.md`): 8,479 numeric cells, all two-engine
  agreements except one confirmed by eye; every column matches the report's
  Totals row and the county cumulative report.

## Not included

- Rains: the file in openelections-sources-tx is a Hart export of local
  contests only; the county posts cumulative reports only. Records-request
  contact in the sources branch.
- 56 further counties with nothing precinct-level online (22 from Bailey to
  Irion, 34 from Jackson to Zapata). Each has its closest online document
  and records-request contact in
  `openelections-sources-tx/2024/general/SOURCES-2024-found.md` and the
  per-batch logs next to it. Karnes states its precinct report is available
  in person only.
- The statewide SOS 67.017 filing download was not found; see
  `SOS-STATEWIDE-FILING-NOTE.md`.
