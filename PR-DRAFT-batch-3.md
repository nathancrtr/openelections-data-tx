# PR draft, Batch 3 (Jackson through Zapata), 2024 general election precinct results

Not to be opened by the session; the owner posts it.

## Counties in this PR

- Polk County: `2024/counties/20241105__tx__general__polk__precinct.csv`

## Sources

- Polk: Commissioners Court special meeting packet of 2024-11-18 (CivicClerk,
  `https://polkcotx.api.civicclerk.com/v1/Meetings/GetMeetingFileStream(fileId=1835,plainText=false)`),
  which contains the signed canvass certificate and the ES&S "Canvass Results
  Report", Official Results, run 11/15/2024, 42 of 42 precincts. The packet is a
  scan with a garbled text layer, so the numbers were read by two OCR engines
  (tesseract 5.3.4 and RapidOCR) and cross-checked; see "Known issues".
  Saved in openelections-sources-tx as
  `2024/general/2024 Polk County, TX precinct-level results.pdf`
  (SHA-256 `7168439eacfe773c66c3a8d0fc0dca8a3d5b12357f750cae8e811db83c90ae6f`)
  with the county's unofficial election-night cumulative report as
  `... precinct-level results summary.pdf`.

## Checks

- `file_format`, `duplicate_entries`, `missing_values`, `vote_breakdown_totals`
  (openelections-data-tests v2.2.0): all OK.
- Source totals: the sum of the 42 precinct rows equals the report's own
  Totals row for every contest, every candidate, Under/Over Votes, Cast Votes,
  and the ballots-cast and registered-voter columns (zero mismatches).
- TLC Capitol Data Portal VTD dataset: President and U.S. Senate match by
  candidate with difference 0 (see `2024/counties/RECONCILIATION-2024.md`).
- Pages: 73 in the packet; 64 canvass pages (2 to 65) parsed, pages 67 to 73
  (official cumulative report) used for a second cross-check, pages 1 and 66
  are the certificate and "End of report".
- Precincts: 42 in the source headings, 42 in the file.
- OCR: every number was read by tesseract and RapidOCR and accepted only when
  the two agreed. Of 8,479 numeric cells, 8,345 agreed on the first pass, 133
  agreed after a fallback mode or a tighter crop, and one cell needed a
  decision (below).

## Known issues

- One OCR cell was not a clean two-engine agreement: Railroad Commissioner,
  precinct "21 - CITY-LVISD", Eddie Espinoza. Tesseract read 1 in every mode;
  RapidOCR read 1 in cell mode and 7 in block mode. The file carries 1, which
  equals Cast Votes minus the other candidates and which a reviewer confirmed
  by looking at page 15 of the packet.
- The report's "Total Ballots Cast" differs from Cast Votes + Under + Over in
  four precincts: 8 - LVISD (364 vs 365), 19 - LVISD (1,774 vs 1,782),
  20 - LVISD (1,692 vs 1,700), 22 - LVISD (1,959 vs 1,962). The report header
  says 24,381 ballots and its Totals row 24,361; the file keeps the printed
  figures in both places (Ballots Cast rows use Total Ballots Cast, which does
  sum to absentee + early + election day in all 42 precincts).
- Registered Voters is printed as 0 for the ISD/city sub-precincts (for
  example "1 - LVISD"); kept as 0.
- Candidate votes have no per-precinct method split in this report; only
  Ballots Cast does. Method cells on candidate rows are empty, as in the
  Archer file.
- All 26 contests in the report are included (statewide judicial, 9th Court
  of Appeals, 411th District Judge, commissioners, constables, Livingston and
  Leggett ISD boards, City of Livingston mayor and alderman), not only the
  offices the issue asks for.
- The converter and OCR pipeline are under `batch-3-scripts/` on this branch
  (not for the upstream PR), with `polk/resolve.log` listing every cell that
  needed a fallback.

## Counties searched with no precinct-level file online (29)

Jackson, Karnes, Kent, King, Kinney, Kleberg, Knox, Lavaca, Lipscomb, Loving,
Marion, Mason, Maverick, Morris, Navarro, Pecos, Presidio, Real, Roberts,
Runnels, Schleicher, Shackelford, Shelby, Sherman, Somervell, Sterling,
Trinity, Upton, Uvalde, Wheeler, Wilbarger, Willacy, Young, Zapata.

For each, the county's own site, clerk or elections-administrator page,
commissioners court canvass agenda/minutes/packet, and vendor results pages
were checked; what is online is at most a county-wide cumulative or summary
report. The records-request contact for each county (office, name, email,
phone, address, from the county's site) is in
`openelections-sources-tx/2024/general/SOURCES-2024-found.md`. Karnes posts a
notice that its precinct (box) report is available only in person at the
elections office. Somervell's site could not be reached from this session's
network at all, so that one may simply need a retry.
