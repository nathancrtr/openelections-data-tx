# Reconciliation of the 2024 general county files against the Texas Legislative Council 2024 General VTD returns (all batches)

Reference: `2024_General_Election_Returns.csv` in the 2024 General VTDs Election Data zip from https://data.capitol.texas.gov/dataset/comprehensive-election-datasets-compressed-format (resource dated 2025-02-25, downloaded 2026-11-04). Each session summed its county files' President and U.S. Senate rows by candidate and compared them with the county's VTD sum. The three per-batch records follow unchanged (`RECONCILIATION-2024-batch-1.md`, `-2.md`, `-3.md`). A fourth pass at the end re-ran the same comparison on all 13 files with one script; result: every named candidate matches TLC exactly in 12 counties; Cochran differs (+42 Trump, +10 Harris, +2 Oliver, +43 Cruz, +10 Allred, +1 Brown) because its tally sheet's EV column includes mail ballots. Remaining differences are write-in rows only: TLC credits no Senate write-ins in Clay (2), Erath (8), Webb (51), Wilson (26), Yoakum (2) and one fewer in Newton; Haskell and Polk list write-in candidates by name rather than as a Write-ins row, so the summed check shows TLC's 1 and 7 (President) and 6 and 5 (Senate) write-in votes against 0.

Not for the upstream PR.

---

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

---

# Reconciliation of batch 2 county files against TLC 2024 General VTD data

Reference: Texas Legislative Council, Capitol Data Portal, "2024 General VTDs Election Data" (`2024_General_Election_Returns.csv` inside `2024-general-vtds-election-data.zip`, resource updated 2025-02-25), from `https://data.capitol.texas.gov/dataset/comprehensive-election-datasets-compressed-format`. Downloaded 2026-11-04.

Method: sum each county file's President and U.S. Senate rows by candidate (matched on surname) and compare with the sum of that county's VTD rows in the TLC file. TLC lists certified write-in candidates by name (Andrus, Roche) with zero votes; those rows are omitted. The threshold from the brief is 0.5% of the county's President votes.

## Clay

Precincts in file: 16; TLC VTDs: 16

| office | candidate | file | TLC | diff |
|---|---|---|---|---|
| President | Harris | 584 | 584 | +0 |
| President | Oliver | 21 | 21 | +0 |
| President | Stein | 13 | 13 | +0 |
| President | Trump | 5288 | 5288 | +0 |
| President | Write-In | 12 | 12 | +0 |
| U.S. Senate | Allred | 663 | 663 | +0 |
| U.S. Senate | Brown | 88 | 88 | +0 |
| U.S. Senate | Cruz | 5128 | 5128 | +0 |
| U.S. Senate | Write-In | 2 | 0 | +2 |

Largest candidate difference: 2 (0.034% of county President votes). OK

Note: TLC has no Senate write-in row for Clay; the file's 2 Senate write-in votes come from the county's Clarity export.

## Erath

Precincts in file: 21; TLC VTDs: 21

| office | candidate | file | TLC | diff |
|---|---|---|---|---|
| President | Harris | 2871 | 2871 | +0 |
| President | Oliver | 95 | 95 | +0 |
| President | Stein | 35 | 35 | +0 |
| President | Trump | 15349 | 15349 | +0 |
| President | Write-In | 50 | 50 | +0 |
| U.S. Senate | Allred | 3126 | 3126 | +0 |
| U.S. Senate | Brown | 380 | 380 | +0 |
| U.S. Senate | Cruz | 14672 | 14672 | +0 |
| U.S. Senate | Write-In | 8 | 0 | +8 |

Largest candidate difference: 8 (0.044% of county President votes). OK

Note: TLC has no Senate write-in row for Erath. Erath's per-precinct Trump counts were also compared VTD by VTD against TLC: all 21 precincts match exactly.

## Haskell

Precincts in file: 10; TLC VTDs: 10

| office | candidate | file | TLC | diff |
|---|---|---|---|---|
| President | Harris | 312 | 312 | +0 |
| President | Oliver | 12 | 12 | +0 |
| President | Stein | 3 | 3 | +0 |
| President | Trump | 1915 | 1915 | +0 |
| President | Write-In | 0 | 1 | -1 |
| U.S. Senate | Allred | 357 | 357 | +0 |
| U.S. Senate | Brown | 39 | 39 | +0 |
| U.S. Senate | Cruz | 1823 | 1823 | +0 |

Largest candidate difference: 1 (0.045% of county President votes). OK

Note: the file lists write-in candidates by name, so the script's `Write-In` line reads 0; the one presidential write-in vote is on the Claudia De la Cruz row (Sagerton Pct 10, election day), matching TLC's 1. TLC lists the certified Senate write-ins Andrus and Roche with 0 votes; the file carries the source's 4 and 2. Stein's 3 and the De la Cruz vote come from the per-method sections of the source, which TLC agrees with; the source's combined grid prints 1 and 0 for them (see the PR draft's known issues).

---

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
