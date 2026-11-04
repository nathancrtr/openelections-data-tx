# Worklog, batch 2 (Bailey through Irion), 2024 general precinct results

Session date: 2026-11-04. Times are wall-clock estimates for this session,
including the parallel source searches (five searches ran at once, roughly
10 to 14 minutes each).

## Setup and the statewide SOS question

| step | minutes | method | result |
|---|---|---|---|
| Re-read issue #458, inspect existing 2024 files and test suite | 10 | GitHub search API, repo files, cloned `openelections-data-tests` v2.2.0 | 70 counties still unchecked, none claimed in comments; built a CSV writer, a TLC reconciliation script and a four-test runner, validated on Archer and Walker |
| Statewide SOS precinct-by-precinct filing download | 20 | SOS page with browser user agent, both SOS domains, guessed successor URLs, SOS forms index, web search, Wayback availability API | Not found. SOS page is gone (their 403 "file not found" page); Wayback has a 2024-02-28 capture but the archive is unreachable from this environment. Details in the sources fork's `2024/general/SOURCES-2024-found.md`. |
| TLC 2024 General VTD data download and parsing | 5 | Capitol Data Portal API, 82 MB zip | Working reference for reconciliation |

## Counties

| county | minutes | method | result |
|---|---|---|---|
| Bailey | 12 (search) | county CIRA site, guessed file names, web search | Not found. Official ES&S summary only. Contact recorded. |
| Bee | 14 (search) | county CivicPlus site, CIRA mirror, IQM2 agenda portal (canvass packet and minutes) | Not found. Hart cumulative report and canvass minutes without returns. Contact recorded. |
| Blanco | 12 (search) | county CIRA site, 16 guessed precinct-report file names | Not found. SOS canvass report (county totals) and ENR report. Contact recorded. |
| Briscoe | 10 (search) | county CIRA site | Not found. The page links an unofficial results PDF and a CVR xlsx for Nov 2024 but both 404. Contact recorded. |
| Castro | 10 (search) | county CIRA site, minutes server | Not found. Nothing from 2024 online; minutes server unreachable. Contact recorded. |
| Childress | 14 (search) | county site (found via SOS directory email domain), minutes | Not found. Nov 18 canvass minutes with SOS canvass entry, county totals; single countywide vote center. Contact recorded. |
| Clay | 10 (search) + 15 (convert) | county site links to Clarity ENR; parsed `detail.xml` | Done. 16 precincts, four vote types. All four tests pass. President and Senate match TLC exactly. |
| Crane | 12 (search) | county CIRA site, 10 guessed file names | Not found. Election-night ES&S summary only. Contact recorded. |
| Crockett | 12 (search) | county CIRA site, minutes | Not found. Canvass minutes without figures. Contact recorded. |
| Crosby | 10 (search) | county CIRA site, 14 guessed file names | Not found. No Nov 2024 results of any kind online. Contact recorded. |
| Culberson | 10 (search) | county site | Not found. Hart cumulative report only. Contact recorded. |
| Dallam | 12 (search) | county site, 18 guessed file names | Not found. Site now links only Nov 2026 results. Contact recorded. |
| Deaf Smith | 10 (search) | county CIRA site | Not found. Only 2025 and 2026 cumulative reports remain. Contact recorded. |
| Dickens | 12 (search) | county CIRA site, minutes | Not found. Hart cumulative report, canvass minutes without figures. Contact recorded. |
| Donley | 12 (search) | county site, minutes page | Not found. SOS unofficial results form (county totals), turnout-by-precinct sheet. Contact recorded. |
| Edwards | 14 (search) | county site, minutes | Not found. ES&S unofficial summary (misnamed "2025"), canvass minutes without figures. Contact recorded. |
| Erath | 14 (search) + 25 (convert) | county Archive Center (via the civicplus alias, the main domain blocks scripts); aggregated the cast vote record xlsx | Done with a caveat. 21 precincts, 18,441 ballots, no method breakdown. All four tests pass. All candidate totals and Trump's per-precinct counts match TLC exactly. |
| Fisher | 14 (search) | county site, canvass minutes (24 pp) | Not found. Official ES&S summary and SOS canvass report, county totals. Contact recorded. |
| Frio | 14 (search) | county site, minutes (docx) | Not found. SOS canvass report and unofficial results form, county totals. Contact recorded. |
| Hansford | 10 (search) | county site | Not found. No results for any election online. Contact recorded. |
| Hartley | 12 (search) | county CIRA site | Not found. Election-night ES&S summary and reconciliation form. Contact recorded. |
| Haskell | 12 (search) + 35 (OCR and convert) + 10 (review) | county site; scanned grid PDF, two OCR engines (tesseract 5.3.4 and rapidocr) with arithmetic cross-checks | Done. 10 precincts, mail/early/election-day columns from the per-method sections. Two engines agreed on 67 to 82% of cells per section; row sums and cross-section equalities settled the rest except four cells read visually from 300 dpi strips (listed in the PR draft); two of those were re-checked visually in review. No unresolved cells. All four tests pass. President and Senate match TLC exactly. Seven source-internal inconsistencies kept as printed and listed. |
| Howard | 14 (search) | old CIRA site, new CivicPlus site, CivicClerk portal, minutes | Not found. ES&S election-night summary and EV report, canvass minutes without the report. Contact recorded. |
| Hudspeth | 12 (search) | county site | Not found. Hart cumulative report. Contact recorded. |
| Irion | 12 (search) | county CivicPlus site, agendas | Not found. Site holds only 2026 results. Contact recorded. |

## Judgement on whether the next batch is worth running

Of 25 counties, 3 had anything precinct-level online, and one of those (Erath)
is a cast vote record rather than a report. The other 22 mostly post a
county-wide summary and nothing else, and several that did post precinct
reports for other elections (Bailey, Blanco, Briscoe, Culberson, Dickens,
Edwards, Fisher, Frio, Hudspeth, Irion) skipped Nov 2024, which suggests
records requests, or the SOS filing export, will be needed for most of the
remaining small counties. A batch-3 session should expect a similar hit rate
from web search alone.
