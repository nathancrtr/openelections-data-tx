# Statewide SOS precinct-by-precinct filing for 2024: not found online

Checked 2026-11-04 (Batch 3), time-boxed to 30 minutes.

- `https://www.sos.state.tx.us/elections/laws/precinct-by-precinct-report.shtml`
  and the `sos.texas.gov` mirror both return HTTP 403 to a plain fetch, to a
  fetch with a Chrome user agent, and to the session's web-fetch tool. Left to
  the owner as the brief says.
- Web search found no public download of the county filings made under
  Election Code 67.017 for the November 5, 2024 general election. Search hits
  are only individual county PDFs and the Texas Legislative Council (TLC)
  Capitol Data Portal VTD dataset.
- The 2022 source file names in this fork
  (`KING_COUNTY-2022_NOVEMBER_8TH_GENERAL_ELECTION_1182022-...`) match an
  export-with-metadata naming scheme (county, election name, election date,
  original filename), which is consistent with the SOS providing the filed
  returns on request rather than publishing them. The commit that added them
  (`36409b1`, 2022-12-30, "added 2022 general sources") carries no URL.
- Redistricting Data Hub's 2024 Texas VTD file cites the Capitol Data Portal
  as its source, not the SOS filings.

Conclusion: no statewide URL to proceed from. Batches 2 and 3 proceed county
by county. A public-information request to the SOS Elections Division for the
2024 general election 67.017 filings would be the single-shot alternative and
is the owner's call.
