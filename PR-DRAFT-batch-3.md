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

POLK_CHECKS_PLACEHOLDER

## Known issues

POLK_ISSUES_PLACEHOLDER

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
