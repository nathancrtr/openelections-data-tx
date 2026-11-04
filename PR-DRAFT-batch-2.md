# PR draft, batch 2: 2024 general precinct results for Clay, Erath, Haskell

(Not opened. Text for the owner to use or edit. Companion PR in
`openelections-sources-tx` adds the three source files and
`2024/general/SOURCES-2024-found.md`.)

## Title

2024 general: add Clay, Erath and Haskell precinct results

## Body

Adds three county files for #458.

**Clay** (`20241105__tx__general__clay__precinct.csv`). Converted from the
county's Clarity ENR precinct detail XML (version 353790, timestamped
11/8/2024), linked from the county elections page. 16 precincts, with
`absentee`, `early_voting`, `election_day` and `provisional` columns. Ballots
Cast per precinct from the export's turnout block (no registered-voter
figures in the export). Offices: President, U.S. Senate, U.S. House 13,
Railroad Commissioner, State Senate 30, State Representative 69, County
Attorney, Sheriff, County Tax Assessor-Collector. Write-ins are the export's
single "Write-in" choice per contest.

**Erath** (`20241105__tx__general__erath__precinct.csv`). The county did not
post a precinct results report for November 2024; it posted the cast vote
record (one row per ballot, 18,441 ballots) in its Archive Center. This file
is that CVR aggregated by its Precinct column: 21 precincts, no vote-method
breakdown. Ballots Cast is the ballot count per precinct. Rows for `Over
Votes`, `Under Votes` and `Write-ins` come from the CVR's `overvote`,
`undervote` and blank cells respectively. Same offices as Clay except U.S.
House 25 and State Representative 59, and no State Senate contest on the
ballot. Every candidate total for President, U.S. Senate, U.S. House,
Railroad Commissioner and State Representative matches the TLC 2024 General
VTD data exactly, and Trump's count matches TLC in every one of the 21 VTDs.

**Haskell** (`20241105__tx__general__haskell__precinct.csv`). Converted from the county's scanned
spreadsheet "GENERAL ELECTION BBM, EV & ED 11/5/2024" (17 pages, image only).
The document has separate ballots-by-mail, early-voting and election-day
sections by precinct, so the file has `early_voting`, `election_day` and
`mail` columns for all 10 precincts. Numbers were read by two OCR engines
(tesseract 5.3.4 and rapidocr) cell by cell and accepted only where the
engines agreed or where the row's printed total and the cross-section sums
left one possibility; four cells were settled by a visual read of the scan
(Peter Sonski mail row all 0; Ted Brown early voting Haskell Pct 2 = 5 and
Pct 3 = 6; Richard McKibbin early voting Haskell Pct 1 = 0; Eddie Espinoza
printed mail total 0), two of which were re-checked by a second reader. No
cells are unresolved. Offices: President, U.S. Senate, U.S. House 19,
Railroad Commissioner, State Representative 69, County Attorney, Sheriff,
County Tax Assessor-Collector (no State Senate contest). The source lists
certified write-in candidates by name, so they appear by name with an empty
party, as in the Archer file; the Sheriff race was won by write-in CJ Saucedo
(1,187 to 937). The source has no registered-voter or ballots-cast rows.

## Checks

- `openelections-data-tests` v2.2.0: `file_format`, `duplicate_entries`,
  `missing_values`, `vote_breakdown_totals` all pass on each file.
- Reconciliation against the Texas Legislative Council's 2024 General VTD
  data (President and U.S. Senate by candidate): Clay and Erath match exactly
  on every candidate. Haskell matches exactly on every named candidate (the one presidential write-in vote is on the De la Cruz row). The per-county tables are in
  `2024/counties/RECONCILIATION-2024.md` on the branch (not meant for merge).
- Precinct counts: Clay 16 (TLC 16; SOS voter-registration page lists 17),
  Erath 21 (TLC 21; SOS lists 22), Haskell 10 (TLC 10; SOS lists 11).

## Known issues and things I was unsure of

- Erath's "Write-ins" rows count ballots with a write-in mark, not votes
  credited to a certified write-in candidate. For President this equals the
  official write-in total (50, matching TLC). For U.S. House 25 it is 428,
  while TLC credits the certified write-in (Hagg) with 23; the rest are
  marks for names that were not certified. If that is unwanted, drop the
  U.S. House write-in rows.
- Erath's CVR carries no official/unofficial label. It was posted by the
  county as the record of the canvassed election and matches TLC exactly.
- Clay's export is dated before the canvass and carries no label; totals
  match TLC exactly, so it is at least consistent with the certified
  returns. The county elections administrator can confirm.
- Precinct names are as the sources print them (`SE HENRIETT`, `Precinct No.
  10`, `Haskell Pct 1`).
- Only the offices listed in #458 were converted (plus Ballots Cast). The
  Clay and Erath sources also carry judicial, SBOE, commissioner, constable
  and ISD contests, which could be added later from the same sources.
- Haskell source-internal inconsistencies, kept as printed (file values
  come from the per-method sections, pages 4 to 13; the combined grid on
  pages 1 to 3 differs in these cells):
  - Eddie Espinoza (Railroad Commissioner), mail: precinct cells 0 0 2 0 1
    0 0 0 0 0 but the printed mail total is 0, and the grid's TOTAL is 35.
    File total 38.
  - Bernard Johnson (U.S. House 19), early voting: section cells and
    section total 52; grid EV column 53, grid TOTAL 85. File total 84.
  - Nathan Lewis (U.S. House 19), early voting: section 90; grid 88, TOTAL
    133. File total 135.
  - Jill Stein, election day: section has Haskell Pct 4 = 1 and Rule Pct 5
    = 1; grid shows 0 in every ED cell and TOTAL 1. File 3, which is also
    TLC's figure.
  - Claudia De la Cruz (write-in), election day: section has Sagerton Pct
    10 = 1; grid 0. File 1, matching TLC's write-in count.
  - Tracy Andrus and Analisa Roche (Senate write-ins): grid TOTAL prints 2
    and 1 although its own cells sum to 4 and 2. File 4 and 2.
  - Pages 14 to 17 (a BBM/EV summary) disagree with the rest of the
    document in several cells (e.g. Allred EV 235 vs 230) and look like a
    different tally run; not used.
- Haskell names are spelled as the source prints them: `Jody C. Arrington`
  (other counties' files use `Jodey C. Arrington`) and `Christoper Keith`.
  `CJ Saucedo` is a visual read; the scan's "CJ" is smudged.
- Haskell's source carries no official/unofficial label.

## Sources

- Clay: https://results.enr.clarityelections.com/TX/Clay/122307/353790/reports/detailxml.zip
- Erath: https://www.co.erath.tx.us/ArchiveCenter/ViewFile/Item/1703
- Haskell: https://www.haskellcountytx.gov/upload/page/7706/precinct%20by%20precinct%20for%20nov%202024%20election.pdf
