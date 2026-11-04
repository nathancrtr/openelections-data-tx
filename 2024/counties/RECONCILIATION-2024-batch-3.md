# Reconciliation to the Texas Legislative Council VTD dataset, Batch 3

Independent total: "2024 General VTDs Election Data" from the Capitol Data
Portal (`2024-general-vtds-election-data.zip`, file
`2024_General_Election_Returns.csv`, dated 2025-02-25), summed by county and
candidate for President and U.S. Senate. The county file is summed over its
precinct rows for the same offices. Difference = file minus TLC.

| County | Office | Candidate | File | TLC | Diff |
|---|---|---|---|---|---|
| Polk | President | Donald J. Trump (REP) | 19216 | 19216 | 0 |
| Polk | President | Kamala D. Harris (DEM) | 4910 | 4910 | 0 |
| Polk | President | Chase Oliver (LIB) | 100 | 100 | 0 |
| Polk | President | Jill Stein (GRN) | 59 | 59 | 0 |
| Polk | U.S. Senate | Ted Cruz (REP) | 18596 | 18596 | 0 |
| Polk | U.S. Senate | Colin Allred (DEM) | 5106 | 5106 | 0 |
| Polk | U.S. Senate | Ted Brown (LIB) | 436 | 436 | 0 |

Polk: 42 precinct rows in the file (TLC has 22 VTDs; the county's canvass
splits precincts by ISD and city, e.g. "4 - LVISD", "4 - CITY-LVISD").
Difference 0.000% of the county's President votes.

No other county in this batch has a precinct-level source, so no other rows.
