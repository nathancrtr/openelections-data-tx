# Reconciliation of batch-1 county files against the Texas Legislative Council 2024 General VTD returns

Source: `2024_General_Election_Returns.csv` from https://data.capitol.texas.gov/dataset/comprehensive-election-datasets-compressed-format (2024 General VTDs Election Data zip, downloaded 2026-11-04). TLC compiles it from county and Secretary of State returns and warns of small differences. For each county the file's President and U.S. Senate votes are summed by candidate and compared with the county's VTD sum. TLC credits write-in candidates individually (Andrus and Roche for Senate); our files carry one Write-ins row, so write-in rows are summed on the TLC side. Every non-zero difference below is in a write-in row, except Cochran (see the PR draft) and the write-in rows where TLC carries no write-in votes at all.

Webb was also checked precinct by precinct: all 1,115 cells of President, U.S. Senate, U.S. House 28, Railroad Commissioner and State Representative 42/80 that TLC carries for a Webb VTD (VTD splits A/B/C summed) match the file, and Ballots Cast matches TLC turnout (TotalTO) in all 78 precincts.

| county | office | candidate | our file | TLC VTD sum | diff |
|---|---|---|---|---|---|
| Cochran | President | Trump | 777 | 735 | +42 |
| Cochran | President | Harris | 158 | 148 | +10 |
| Cochran | President | Oliver | 11 | 9 | +2 |
| Cochran | President | Stein | 1 | 1 | +0 |
| Cochran | President | Write-ins | 0 | 0 | +0 |
| Cochran | U.S. Senate | Cruz | 749 | 706 | +43 |
| Cochran | U.S. Senate | Allred | 159 | 149 | +10 |
| Cochran | U.S. Senate | Brown | 25 | 24 | +1 |
| Cochran | U.S. Senate | Write-ins | 1 | 1 | +0 |
| Hill | President | Trump | 13669 | 13669 | +0 |
| Hill | President | Harris | 2919 | 2919 | +0 |
| Hill | President | Oliver | 78 | 78 | +0 |
| Hill | President | Stein | 37 | 37 | +0 |
| Hill | President | Write-ins | 3 | 3 | +0 |
| Hill | U.S. Senate | Cruz | 13104 | 13104 | +0 |
| Hill | U.S. Senate | Allred | 3223 | 3223 | +0 |
| Hill | U.S. Senate | Brown | 327 | 327 | +0 |
| Hill | U.S. Senate | Write-ins | 4 | 4 | +0 |
| McMullen | President | Trump | 448 | 448 | +0 |
| McMullen | President | Harris | 37 | 37 | +0 |
| McMullen | President | Oliver | 2 | 2 | +0 |
| McMullen | President | Stein | 0 | 0 | +0 |
| McMullen | President | Write-ins | 1 | 0 | +1 |
| McMullen | U.S. Senate | Cruz | 423 | 423 | +0 |
| McMullen | U.S. Senate | Allred | 48 | 48 | +0 |
| McMullen | U.S. Senate | Brown | 5 | 5 | +0 |
| McMullen | U.S. Senate | Write-ins | 0 | 0 | +0 |
| Newton | President | Trump | 4781 | 4781 | +0 |
| Newton | President | Harris | 952 | 952 | +0 |
| Newton | President | Oliver | 7 | 7 | +0 |
| Newton | President | Stein | 9 | 9 | +0 |
| Newton | President | Write-ins | 2 | 2 | +0 |
| Newton | U.S. Senate | Cruz | 4650 | 4650 | +0 |
| Newton | U.S. Senate | Allred | 972 | 972 | +0 |
| Newton | U.S. Senate | Brown | 68 | 68 | +0 |
| Newton | U.S. Senate | Write-ins | 2 | 1 | +1 |
| Terrell | President | Trump | 314 | 314 | +0 |
| Terrell | President | Harris | 91 | 91 | +0 |
| Terrell | President | Oliver | 0 | 0 | +0 |
| Terrell | President | Stein | 0 | 0 | +0 |
| Terrell | President | Write-ins | 0 | 0 | +0 |
| Terrell | U.S. Senate | Cruz | 301 | 301 | +0 |
| Terrell | U.S. Senate | Allred | 92 | 92 | +0 |
| Terrell | U.S. Senate | Brown | 7 | 7 | +0 |
| Terrell | U.S. Senate | Write-ins | 0 | 0 | +0 |
| Webb | President | Trump | 33397 | 33397 | +0 |
| Webb | President | Harris | 31996 | 31996 | +0 |
| Webb | President | Oliver | 227 | 227 | +0 |
| Webb | President | Stein | 283 | 283 | +0 |
| Webb | President | Write-ins | 92 | 92 | +0 |
| Webb | U.S. Senate | Cruz | 28135 | 28135 | +0 |
| Webb | U.S. Senate | Allred | 33794 | 33794 | +0 |
| Webb | U.S. Senate | Brown | 1808 | 1808 | +0 |
| Webb | U.S. Senate | Write-ins | 51 | 0 | +51 |
| Wichita | President | Trump | 31818 | 31818 | +0 |
| Wichita | President | Harris | 12237 | 12237 | +0 |
| Wichita | President | Oliver | 295 | 295 | +0 |
| Wichita | President | Stein | 147 | 147 | +0 |
| Wichita | President | Write-ins | 33 | 33 | +0 |
| Wichita | U.S. Senate | Cruz | 30711 | 30711 | +0 |
| Wichita | U.S. Senate | Allred | 12545 | 12545 | +0 |
| Wichita | U.S. Senate | Brown | 987 | 987 | +0 |
| Wichita | U.S. Senate | Write-ins | 14 | 14 | +0 |
| Wilson | President | Trump | 20894 | 20894 | +0 |
| Wilson | President | Harris | 6247 | 6247 | +0 |
| Wilson | President | Oliver | 80 | 80 | +0 |
| Wilson | President | Stein | 49 | 49 | +0 |
| Wilson | President | Write-ins | 50 | 50 | +0 |
| Wilson | U.S. Senate | Cruz | 19783 | 19783 | +0 |
| Wilson | U.S. Senate | Allred | 6802 | 6802 | +0 |
| Wilson | U.S. Senate | Brown | 544 | 544 | +0 |
| Wilson | U.S. Senate | Write-ins | 26 | 0 | +26 |
| Yoakum | President | Trump | 2039 | 2039 | +0 |
| Yoakum | President | Harris | 342 | 342 | +0 |
| Yoakum | President | Oliver | 7 | 7 | +0 |
| Yoakum | President | Stein | 5 | 5 | +0 |
| Yoakum | President | Write-ins | 4 | 4 | +0 |
| Yoakum | U.S. Senate | Cruz | 1928 | 1928 | +0 |
| Yoakum | U.S. Senate | Allred | 357 | 357 | +0 |
| Yoakum | U.S. Senate | Brown | 56 | 56 | +0 |
| Yoakum | U.S. Senate | Write-ins | 2 | 0 | +2 |
