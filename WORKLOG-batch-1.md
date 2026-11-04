# Work log, 2024 general precinct results, batch 1 (counties with a source file)

Session of 2026-11-04. Times are wall-clock estimates for the agent run,
including tool setup and retries. "Method" names the parser written for the
county; all parsers live outside the repo (scratch) and can be shared on
request.

| county | minutes | method | result |
|---|---|---|---|
| (setup) | 20 | clone data tests v2.2.0, download TLC 2024 General VTD returns, SOS 2024 ballot certification (for party labels), survey existing file conventions | shared writer + checks |
| Yoakum | 15 | csv: SOS precinct-by-precinct export; three unlabeled vote-type rows per precinct taken as absentee / early / election day in that order | done; 4 tests pass; TLC exact except 2 Senate write-ins TLC does not credit |
| Terrell | 20 | three xlsx tally sheets (EV in person, election day, mail); parties from SOS certification; source TOTAL VOTES column verified | done; tests pass; TLC exact |
| Wilson | 15 | fixed-width txt (contest / candidate / precinct, total + 3 methods per line) | done; tests pass; TLC exact except Senate write-ins (26) TLC does not credit |
| Hill | 25 | Hart "Precinct by Precinct" PDF (text), 65 pages, pdftotext -layout parser; Cast Votes rows checked per method | done; tests pass; TLC exact |
| Wichita | 20 | same Hart parser, 375 pages, 52 precinct splits; also checked against the county summary PDF (259 President/Senate cells, 0 differences) | done; tests pass; TLC exact; header says 53 precincts, 52 appear in the report |
| Newton | 35 | official canvass PDF (text), pdfplumber column assignment; Early Vote + Election Day sections checked against Grand Totals cell by cell | done; tests pass; TLC exact except 1 Senate write-in |
| Cochran | 30 | unofficial tally sheet PDF (text), pdfplumber column assignment, parties from SOS certification | converted as printed, but the EV column double-counts mail ballots; county totals +5% vs TLC; needs owner decision / better source |
| McMullen | 110 | scanned Electionware summary reports (5 reports, duplex scan); tesseract psm 6 and psm 11 at 2x plus a template digit reader; every row checked against printed percentage and candidate sums; 4 cells read visually (listed in PR draft) | done; tests pass; TLC exact except 1 President write-in |
| Webb | 230 | scanned Electionware "PCT by PCT" tables, 88 pages, 78 precincts; deskew, per-cell template digit reader + tesseract, row arithmetic, printed Totals row, TLC per-VTD check | done; tests pass; TLC exact in all 1,115 compared cells and county totals; 7 cells read by eye (PR draft) |
| Rains | 15 | existing csv is a local-election report (no general contests); county site has only cumulative reports | not done; records-request contact recorded in sources fork |

Lessons for the next batch:

- Hart "Precinct by Precinct" PDFs (Hill, Wichita) and SOS export CSVs
  (Yoakum) convert in minutes with the shared parser; prioritise counties
  whose source is one of these.
- Scanned Electionware reports are feasible but expensive (2 to 4 hours
  each, most of it building the cell-reading pipeline, which now exists);
  a text PDF or the SOS precinct-by-precinct filing would be far cheaper,
  so the statewide-filing question (batches 2 and 3) matters.
- For scanned tables, OCR engines misread this font's 5/6/9/0 and 3/8 at
  200 dpi; a template reader trained on the document's own digits plus the
  table's row arithmetic and printed totals was what made Webb verifiable.
- Tesseract on this machine must be run with `OMP_THREAD_LIMIT=1`; without
  it a page took 60x longer.
