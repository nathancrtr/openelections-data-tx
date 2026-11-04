# WORKLOG, Batch 3 (Jackson through Zapata), 2026-11-04

Branch: `claude/inspiring-keller-5e2b7y` in both forks (the harness fixed the
branch name; the brief's `2024-general-batch-3` name was not used).

Method for the source hunt: seven parallel searches, one per group of five
counties, each working the county elections page, clerk/EA page, commissioners
court canvass agendas, minutes and packets (CivicClerk, towncloud, easydocs,
destinyhosted, boardbook), vendor results sites (Clarity/ENR), and web search.
Then a second pass with a headless browser on the counties whose pages had
blocked plain fetches or that post precinct reports for other elections.
Limits of this session's network: web.archive.org blocked; the SOS
precinct-by-precinct page returns 403; www.co.somervell.tx.us returned 503.

| County | Minutes | Method | Result |
|---|---|---|---|
| (statewide SOS filing) | 25 | web search, SOS page fetch, 2022 file-name provenance | not online; see SOS-STATEWIDE-FILING-NOTE.md |
| Jackson | 2 | hunt: county page links only to SOS county-level site; minutes without canvass | not found; records-request contact recorded |
| Karnes | 6 | hunt + second pass: official cumulative only; county notice says precinct (box) report is available in person only | not found; records-request contact recorded |
| Kent | 2 | hunt: elections page has 2025-26 only; canvass agenda, no minutes | not found; records-request contact recorded |
| King | 2 | hunt: posts 2020 precinct results, nothing for 2024 | not found; records-request contact recorded |
| Kinney | 2 | hunt: unofficial ES&S summary, county totals only | not found; records-request contact recorded |
| Kleberg | 7 | hunt + second pass: SOS canvass form + ES&S EL45A, county totals only; ~330 links enumerated | not found; records-request contact recorded |
| Knox | 2 | hunt: site has 2026 material only | not found; records-request contact recorded |
| Lavaca | 2 | hunt: archive has no Nov 2024 section; minutes acknowledge canvass | not found; records-request contact recorded |
| Lipscomb | 2 | hunt: Hart official cumulative, county totals only | not found; records-request contact recorded |
| Loving | 2 | hunt: only 2026 results posted | not found; records-request contact recorded |
| Marion | 3 | hunt: Hart official cumulative, county totals only | not found; records-request contact recorded |
| Mason | 3 | hunt: unofficial ES&S summary; canvass packet has no report | not found; records-request contact recorded |
| Maverick | 7 | hunt + second pass: site has 2026 only; agenda portal exposes agendas without packets | not found; records-request contact recorded |
| Morris | 3 | hunt: official ES&S summary (scanned), county totals only | not found; records-request contact recorded |
| Navarro | 6 | hunt + second pass: official ES&S summary; county posts PCT BY PCT for other elections, not Nov 2024; 20 guessed names 404 | not found; records-request contact recorded |
| Pecos | 2 | hunt: official ES&S summary (scanned), county totals only | not found; records-request contact recorded |
| Polk | 2 | hunt: official canvass packet (CivicClerk), ES&S Canvass Results Report by precinct, 73 pp scanned | found; converted (see Polk row below) |
| Presidio | 2 | hunt: no county file; newspaper (Big Bend Sentinel) unofficial sheet only, not used | not found; records-request contact recorded |
| Real | 2 | hunt: SOS canvass report (scanned) + unofficial summary, county totals only | not found; records-request contact recorded |
| Roberts | 2 | hunt: only Nov 2026 results posted | not found; records-request contact recorded |
| Runnels | 3 | hunt: towncloud minutes/packets have no tabulation | not found; records-request contact recorded |
| Schleicher | 3 | hunt: 2024 unofficial-results link overwritten with 2026 file | not found; records-request contact recorded |
| Shackelford | 3 | hunt: page carries 2025-26 only | not found; records-request contact recorded |
| Shelby | 3 | hunt: unofficial ES&S summary (scanned), county totals only | not found; records-request contact recorded |
| Sherman | 3 | hunt: official ES&S summary, county TOTAL column only | not found; records-request contact recorded |
| Somervell | 7 | hunt + second pass: county site unreachable from this network (TLS reset / 503); cira mirror 403 | not found; records-request contact recorded |
| Sterling | 2 | hunt: page has 2024 primary/runoff but no Nov 2024 | not found; records-request contact recorded |
| Trinity | 2 | hunt: archive has 2016/2018/2022 canvasses only; agenda item without data | not found; records-request contact recorded |
| Upton | 2 | hunt: page carries 2026 cycle only | not found; records-request contact recorded |
| Uvalde | 6 | hunt + second pass: Drive folder of past results (73 items) skips Nov 2024; minutes omit the attached returns | not found; records-request contact recorded |
| Wheeler | 2 | hunt: official Hart cumulative (scanned), county totals only | not found; records-request contact recorded |
| Wilbarger | 2 | hunt: official cumulative (scanned), county totals only | not found; records-request contact recorded |
| Willacy | 2 | hunt: no results posted; canvass meeting posting has no returns | not found; records-request contact recorded |
| Young | 7 | hunt + second pass: unofficial Hart cumulative, county totals only; 68 links enumerated | not found; records-request contact recorded |
| Zapata | 2 | hunt: unofficial cumulative (scanned), county totals only | not found; records-request contact recorded |
| Polk (conversion) | 150 (agent wall-clock, mostly OCR runs) | 73-page scanned canvass packet: pdftoppm 300 dpi, tesseract + RapidOCR per cell, accept only on agreement; sums checked against the report's Totals rows and the cumulative report; TLC diff 0 | done; 4 tests pass; 1 flagged cell confirmed by eye |

Minutes above are agent wall-clock, prorated across a group of five counties
(plus the second pass where one ran). Total hunt wall-clock: about 80 minutes
for the first pass (seven groups in parallel) and 29 minutes for the second pass.
