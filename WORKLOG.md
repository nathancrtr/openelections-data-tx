# Work log, 2024 general election precinct results (all three batches)

Three sessions ran on 2026-11-04 against the 70 counties still unchecked on
issue openelections/openelections-data-tx#458. This file is the unified
record; the per-batch logs with per-county minutes and methods are
`WORKLOG-batch-1.md`, `WORKLOG-batch-2.md` and `WORKLOG-batch-3.md`.

## Outcome in one table

| | counties | precinct files produced | not done |
|---|---|---|---|
| Batch 1 (had a source file) | 10 | 9: Hill, McMullen, Newton, Terrell, Webb, Wichita, Wilson, Yoakum, and Cochran with a source caveat | Rains (its "source" is a local-election report) |
| Batch 2 (Bailey to Irion, source hunt) | 25 | 3: Clay, Erath, Haskell | 22 (nothing precinct-level online) |
| Batch 3 (Jackson to Zapata, source hunt) | 35 | 1: Polk | 34 (nothing precinct-level online) |
| Total | 70 | 13 | 57 |

Every produced file passes the four data tests at
openelections-data-tests v2.2.0 and reconciles to the Texas Legislative
Council 2024 General VTD returns for every named President and U.S. Senate
candidate (differences only in write-in rows, which TLC credits
differently). Cochran is the one file whose county totals disagree with TLC
(+5%), for a reason in the source itself; see the PR draft.

## Statewide SOS filing (Election Code 67.017)

Both source-hunt batches spent their time box on it and reached the same
answer: no public download exists. The SOS page returns the SOS not-found
page to every fetch, the Wayback Machine was unreachable from these
sessions, and the 2022 file names in the sources repo look like an export
from the filing system rather than a public page. The single-shot
alternative is a public-information request to the SOS Elections Division
(elections@sos.texas.gov, 512-463-5650); that is the owner's call. Details:
`SOS-STATEWIDE-FILING-NOTE.md` (batch 3) and the statewide section of
`SOURCES-2024-found-batch-2.md` in the sources fork.

## County status (70)

Minutes are agent wall-clock from the per-batch logs. "Contact recorded"
means the records-request office, name, phone, email and address are in the
sources fork under `2024/general/SOURCES-2024-found-batch-N.md`.

| county | batch | minutes | source | result |
|---|---|---|---|---|
| Bailey | 2 | 12 | ES&S official summary only | contact recorded |
| Bee | 2 | 14 | Hart cumulative, canvass minutes without returns | contact recorded |
| Blanco | 2 | 12 | SOS canvass report, ENR report (county totals) | contact recorded |
| Briscoe | 2 | 10 | Nov 2024 links on county page 404 | contact recorded |
| Castro | 2 | 10 | nothing from 2024 online | contact recorded |
| Childress | 2 | 14 | canvass minutes with SOS canvass entry (county totals; single vote center) | contact recorded |
| Clay | 2 | 25 | Clarity ENR precinct detail XML | done, 16 precincts, 4 vote types |
| Cochran | 1 | 30 | unofficial tally sheet PDF | converted as printed; EV column double-counts mail; owner decision |
| Crane | 2 | 12 | ES&S election-night summary | contact recorded |
| Crockett | 2 | 12 | canvass minutes without figures | contact recorded |
| Crosby | 2 | 10 | no Nov 2024 results online | contact recorded |
| Culberson | 2 | 10 | Hart cumulative | contact recorded |
| Dallam | 2 | 12 | site now links Nov 2026 only | contact recorded |
| Deaf Smith | 2 | 10 | 2025 and 2026 cumulative only | contact recorded |
| Dickens | 2 | 12 | Hart cumulative, minutes without figures | contact recorded |
| Donley | 2 | 12 | SOS unofficial results form, turnout by precinct | contact recorded |
| Edwards | 2 | 14 | ES&S unofficial summary, minutes without figures | contact recorded |
| Erath | 2 | 39 | cast vote record xlsx, aggregated by precinct | done, 21 precincts, totals only |
| Fisher | 2 | 14 | ES&S official summary, SOS canvass report | contact recorded |
| Frio | 2 | 14 | SOS canvass report, unofficial results form | contact recorded |
| Hansford | 2 | 10 | no results for any election online | contact recorded |
| Hartley | 2 | 12 | ES&S election-night summary, reconciliation form | contact recorded |
| Haskell | 2 | 57 | scanned spreadsheet grid, two OCR engines | done, 10 precincts, mail / early / election day |
| Hill | 1 | 25 | Hart precinct-by-precinct PDF (text) | done, 13 precincts |
| Howard | 2 | 14 | ES&S election-night summary and EV report | contact recorded |
| Hudspeth | 2 | 12 | Hart cumulative | contact recorded |
| Irion | 2 | 12 | site holds 2026 results only | contact recorded |
| Jackson | 3 | 2 | county links only to SOS county-level site | contact recorded |
| Karnes | 3 | 6 | official cumulative; precinct report available in person only | contact recorded |
| Kent | 3 | 2 | 2025-26 only; canvass agenda without minutes | contact recorded |
| King | 3 | 2 | 2020 precinct results posted, nothing for 2024 | contact recorded |
| Kinney | 3 | 2 | ES&S unofficial summary | contact recorded |
| Kleberg | 3 | 7 | SOS canvass form, ES&S EL45A (county totals) | contact recorded |
| Knox | 3 | 2 | 2026 material only | contact recorded |
| Lavaca | 3 | 2 | archive has no Nov 2024 section | contact recorded |
| Lipscomb | 3 | 2 | Hart official cumulative | contact recorded |
| Loving | 3 | 2 | 2026 results only | contact recorded |
| Marion | 3 | 3 | Hart official cumulative | contact recorded |
| Mason | 3 | 3 | ES&S unofficial summary; canvass packet without report | contact recorded |
| Maverick | 3 | 7 | 2026 only; agenda portal without packets | contact recorded |
| McMullen | 1 | 110 | scanned Electionware summary reports, OCR | done, 4 precincts plus county-wide early voting and mail |
| Morris | 3 | 3 | ES&S official summary (scanned) | contact recorded |
| Navarro | 3 | 6 | ES&S official summary; PCT BY PCT posted for other elections only | contact recorded |
| Newton | 1 | 35 | official canvass PDF (text) | done, 21 voting boxes |
| Pecos | 3 | 2 | ES&S official summary (scanned) | contact recorded |
| Polk | 3 | 152 | commissioners court canvass packet (ES&S Canvass Results Report, scanned), OCR | done, 42 precinct splits, all contests |
| Presidio | 3 | 2 | newspaper unofficial sheet only, not used | contact recorded |
| Rains | 1 | 15 | existing csv is a local-election report; county posts cumulative only | contact recorded |
| Real | 3 | 2 | SOS canvass report (scanned), unofficial summary | contact recorded |
| Roberts | 3 | 2 | Nov 2026 results only | contact recorded |
| Runnels | 3 | 3 | towncloud minutes and packets without tabulation | contact recorded |
| Schleicher | 3 | 3 | 2024 link overwritten with 2026 file | contact recorded |
| Shackelford | 3 | 3 | 2025-26 only | contact recorded |
| Shelby | 3 | 3 | ES&S unofficial summary (scanned) | contact recorded |
| Sherman | 3 | 3 | ES&S official summary, county total only | contact recorded |
| Somervell | 3 | 7 | county site unreachable from the session network; retry elsewhere | contact recorded |
| Sterling | 3 | 2 | 2024 primary and runoff only | contact recorded |
| Terrell | 1 | 20 | three xlsx tally sheets | done, 4 precincts, 3 vote types |
| Trinity | 3 | 2 | archive has 2016, 2018, 2022 canvasses only | contact recorded |
| Upton | 3 | 2 | 2026 cycle only | contact recorded |
| Uvalde | 3 | 6 | Drive folder of past results skips Nov 2024 | contact recorded |
| Webb | 1 | 230 | scanned Electionware PCT by PCT tables, OCR | done, 78 precincts, totals only |
| Wheeler | 3 | 2 | Hart official cumulative (scanned) | contact recorded |
| Wichita | 1 | 20 | Hart precinct results report PDF (text) | done, 52 precinct splits |
| Wilbarger | 3 | 2 | official cumulative (scanned) | contact recorded |
| Willacy | 3 | 2 | no results posted | contact recorded |
| Wilson | 1 | 15 | fixed-width text export | done, 13 precincts |
| Yoakum | 1 | 15 | SOS precinct-by-precinct CSV export | done, 6 precincts |
| Young | 3 | 7 | Hart unofficial cumulative | contact recorded |
| Zapata | 3 | 2 | unofficial cumulative (scanned) | contact recorded |

## Is another batch worth running?

Not from the web alone. Of the 60 counties without a source file, 4 had
anything precinct-level online, and several that post precinct reports for
other elections skipped November 2024. The remaining 57 need either the SOS
67.017 filings (one request) or 57 county records requests; the contacts are
collected. Converting whatever arrives is cheap when it is a text PDF or an
export (minutes per county with the parsers from these sessions) and
expensive when it is a scan (two to four hours each; the cell-reading
pipelines built for Webb, McMullen, Haskell and Polk are reusable).

Operational notes for whoever runs the next pass: tesseract on these
machines needs `OMP_THREAD_LIMIT=1` or it runs about 60x slower; the
Wayback Machine and some county sites (Webb agenda server, Somervell) were
unreachable from the session network and are worth a retry from elsewhere.
