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
