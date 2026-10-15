# California Health Data Open Portals (data.ca.gov and data.chhs.ca.gov)

- **Retrieved:** 2026-10-13
- **Type:** External database / data source guide

## Summary

California runs a single CKAN open-data platform, reachable at `data.ca.gov`, whose catalogue indexes more than 240 health datasets and whose actual resource files are served from the Department of Health Care Services portal at `data.chhs.ca.gov`. That catalogue contains the only state-published machine-readable series for Covered California enrollment broken out **by health plan**, **by metal tier**, **by Silver plan variant**, and **by rating region**, all keyed to a statutory reporting mandate. This is the closest thing California publishes to an official carrier-level enrollment database, and it is CSV with a queryable API.

## Key Facts

| Attribute | Detail |
| --- | --- |
| Publisher | State of California, California Health and Human Services Agency (CHHS) / Department of Health Care Services (DHCS) |
| Catalogue URL | https://data.ca.gov/ |
| Resource host (actual files) | https://data.chhs.ca.gov/ |
| CKAN API | `https://data.chhs.ca.gov/api/3/action/package_search?q=<terms>&rows=N` (also reachable on the data.ca.gov origin) |
| Access | Free, no registration, no API key |
| Coverage | Medi-Cal (enrollment, eligibility, managed care plans, providers, rates) and Covered California (plan selection by carrier, metal tier, rating region); DHCS, HCAI, and other California health agencies |
| Current as of | Medi-Cal Managed Care Enrollment Report metadata modified 2026-10-13 18:05 UTC with a September 2026 data file; Covered California datasets modified 2026-10-08 with 2026 Q2 data; Medi-Cal Certified Eligibles modified 2026-10-12 with a September 2026 file |
| Update cadence | Monthly for most enrollment series; quarterly for Covered California reporting-period series |
| Machine-readable | CSV (Open Data Portal convention), plus ZIP bundles. DataStore API for preview/filtering. GIS API for geospatial layers |
| Volume | 248 datasets matching "medi-cal" alone; 103 matching "covered california"; individual files 20–60 KB |

## What it contains

### Covered California series (the ones coveredca.com does not publish)

Verified dataset pages and CSV resources, all returning HTTP 200 on 2026-10-13:

| Dataset | CKAN name | CSV resource |
| --- | --- | --- |
| Qualified Health Plans (QHPs) Selected by Covered California Enrollees | `qualified-health-plans-qhps-selected-by-covered-california-enrollees` | https://data.chhs.ca.gov/dataset/edfa74cb-5edd-43a5-906b-4ff93262b1c4/resource/795c45fc-8a27-484a-bd32-fa03175dbc5b/download/4.1-qhp-2026-q2_odp.csv (200, 54,100 bytes, 971 data rows) |
| Covered California Enrollees by Metal Tier | `covered-california-enrollees-by-metal-tier` | https://data.chhs.ca.gov/dataset/b2282050-4fd7-418c-a466-726bc48da39e/resource/16feaa72-0827-4587-80f1-78d77adfaa84/download/4.3-metal-tier-q2-2026_odp.csv (200, 19,463 bytes, 429 data rows) |
| Covered California Enrollees by Rating Region | `covered-california-enrollees-by-rating-region` | https://data.chhs.ca.gov/dataset/59d54d7e-01fa-4010-959c-535474764daa/resource/80e8a68e-6f84-4f0a-b963-77776a6b07d3/download/4.2-regions-q2-2026_odp.csv |
| Covered California Enrollees by Silver Plan | `covered-california-enrollees-by-silver-plan` | https://data.chhs.ca.gov/dataset/a2034ac5-4ba7-4ebc-a2f4-787842e447ed/resource/a47c41bc-6cee-4bda-8c1e-d3532f92f76a/download/4.4-silver-q2-2026_odp.csv |

Statutory basis, quoted verbatim from the dataset notes: *"This dataset is part of public reporting requirements set forth by the California Welfare and Institutions Code 14102.5."*

**QHP-selected dataset columns:** `Year, Reporting Period, Health Plan , Subsidy, Number of Eligible Individuals Who Selected Plan`. Verified real rows:

```
2026,2026 Q2,Kaiser Permanente,Subsidized,"38,948"
2026,2026 Q2,Kaiser Permanente,Unsubsidized,"8,790"
2026,2026 Q2,Blue Shield of California,Subsidized,"19,089"
2026,2026 Q2,Blue Shield of California,Unsubsidized,"7,068"
2026,2026 Q2,L.A. Care Health Plan,Subsidized,"11,989"
2026,2026 Q2,L.A. Care Health Plan,Unsubsidized,"1,203"
2026,2026 Q2,Anthem Blue Cross of California,Subsidized,"5,919"
2026,2026 Q2,Anthem Blue Cross of California,Unsubsidized,"997"
2026,2026 Q2,Health Net,Subsidized,"5,396"
2026,2026 Q2,Health Net,Unsubsidized,"1,053"
2026,2022 Q2,Molina HealthCare,Subsidized,"25,765"
```

Carriers appearing in the 2026 Q2 rows: Anthem Blue Cross of California, Blue Shield of California, Chinese Community Health Plan, Health Net, Inland Empire Health Plan, Kaiser Permanente, L.A. Care Health Plan, Molina HealthCare, SHARP Health Plan, Valley Health Plan, Western Health Advantage.

**Metal tier dataset columns:** `Year, Quarter Reporting, Metal Level, Subsidy, Number of Eligible Individuals Who Selected Plan`. Verified real rows: `2016,2016 Q1,Bronze,Subsidized,57,058`; `2016,2016 Q1,Silver,Subsidized,97,476`; `2016,2016 Q1,Minimum Coverage,Unsubsidized,2,808`; `2016,2016 Q1,Platinum,Subsidized,3,788`. The rating-region dataset's notes confirm California uses **19 rating regions**: *"California is comprised of 19 rating regions, and each region has different pricing and health insurance options."*

### Medi-Cal series

248 datasets match "medi-cal". Verified examples with live CSV resources:

| Dataset | CKAN name | CSV resource |
| --- | --- | --- |
| Medi-Cal Managed Care Enrollment Report | `medi-cal-managed-care-enrollment-report` | https://data.chhs.ca.gov/dataset/c6ccef54-e7a9-4ebd-b79a-850b72c4dd8c/resource/95358a7a-2c9d-41c6-a0e0-405a7e5c5f18/download/open-data-portal-managed-care-enrollment-count-september-2026.csv |
| Medi-Cal Enrollment by Eligibility Group | `medi-cal-enrollment-by-eligibility-group` | https://data.chhs.ca.gov/dataset/746835c6-17f4-43f0-b98b-f972cf6ee512/resource/d33eee4a-4c17-48da-8099-3fd2bac29ac2/download/7.1-total-medi-cal-enrollment-q2-2026-odp.csv |
| Medi-Cal Certified Eligibles Data by Month with Demographics | `medi-cal-certified-eligibles-with-demographics-by-month` | https://data.chhs.ca.gov/dataset/8c897320-ba87-4574-bc37-bae974191c35/resource/cc08b60f-393f-4e37-9b3e-976d7a9f2a72/download/t1_eligibility_by_age_group_sex_201001_sept2026.csv |
| Medi-Cal Annual Renewals by County | `medi-cal-annual-renewals-by-county` | https://data.chhs.ca.gov/dataset/6160a936-001a-4c45-a531-527e28096cee/resource/25736aa0-3f63-4d74-aaa6-5b432d53cbc0/download/med-abx11-5.1-renewal-jan-2026-and-feb-2026-cdo_v2.csv |
| Medi-Cal Managed Care Provider Listing | `medi-cal-mc-provider-listing` | https://data.chhs.ca.gov/dataset/77c2ec7a-b421-4ffc-8842-13caf384bea7/resource/da5eee46-b040-45cc-8f92-3a7601342cf6/download/mc_providerlist_0725.csv |
| Race/Ethnicity of Newly Medi-Cal Eligible Individuals | `race-ethnicity-of-newly-medi-cal-eligible-individuals` | https://data.chhs.ca.gov/dataset/e739e93f-4002-4fb6-a271-e1fb90f95378/resource/156a3a30-b86e-441a-bc9a-d4105a43df3c/download/3.8-medi-cal-ethnicity-q2-2026-odp.csv |
| Medi-Cal Managed Care Supplemental Rates – Hepatitis C | `medi-cal-managed-care-supplemental-rates-hepatitis-c` | https://data.chhs.ca.gov/dataset/e85e432c-1bb1-4fd1-80b2-fc3befde2565/resource/da22158f-012a-4502-8b72-834ae3844695/download/hepatitis_c_rates_2017-18.csv |

Other live portals verified alongside: https://www.dhcs.ca.gov/data-reports/ (200) and https://www.dhcs.ca.gov/data-reports/medi-cal-eligibility-statistics/ (200). One dataset is served from a GIS endpoint instead of CKAN storage: the Medi-Cal Dental FFS Provider Listing at `https://gis.dhcs.ca.gov/api/download/v1/items/7d8d878c35224e9bb22749b3d3d33cc1/csv?layers=0`.

## What it does NOT contain

1. **No premium amounts and no plan-level detail.** The Covered California datasets stop at carrier name, metal tier, rating region, and subsidy status. There is no price, no plan ID, no benefit design, no network, no service area. For premium dollars by age and rating area you must use the CMS SBE QHP PUF.
2. **The Covered California "enrollees" figures are NEW plan selections in a reporting period, not total enrollment.** This is the single biggest misreading risk. The notes define the population as individuals *"who selected and enrolled in a QHP, and paid their first premium"* during the reporting period. The data proves it: in the metal-tier file, `2016 Q1 Bronze Subsidized = 57,058` but `2016 Q2 Bronze Subsidized = 9,508` — Q1 is the open-enrollment surge, Q2 is not. Reading these as a stock would overstate or understate enrollment by orders of magnitude. Sum across quarters to approximate gross effectuations; do not read any single row as total enrollment.
3. **No county or ZIP breakout for Covered California.** The geography series is by *rating region* (19 regions), not county and not ZIP.
4. **No carrier crosswalk to CMS issuer IDs.** Health plan names here ("SHARP Health Plan", "Molina HealthCare") do not map to the CMS SBE `ISSUER ID` values without manual matching.
5. **Inconsistent carrier roster over time.** Inland Empire Health Plan appears in 2026 Q2 but not in the 2016 rows; Aetna/CVS and Oscar appear in earlier periods and are absent from the 2026 Q2 rows shown. The carrier list is a snapshot per period, not a fixed panel.
6. **Numbers arrive as formatted strings.** Values are quoted strings containing thousands separators and stray padding, e.g. `" 40,600 "` and ` 959 `. Strip non-numeric characters before arithmetic.
7. **`data.ca.gov` is a catalogue, not the file store.** Following a data.ca.gov resource link lands you on `data.chhs.ca.gov`, a different host. Scripts that hard-code the origin will break.
8. **Data-quality caveats in the source itself.** The portal notes state Covered California data comes from CalHEERS, so it carries the same lag and reconciliation issues Covered California flags in its own reports.

## Questions it can answer that coveredca.com cannot

1. How many people selected each California QHP in 2026 Q2, split into subsidized and unsubsidized enrollees, carrier by carrier?
2. How has each carrier's share of new Covered California enrollment shifted quarter by quarter since 2016 Q1? (The QHP-selected dataset has 971 rows of Year × Quarter × Health Plan × Subsidy history.)
3. How many enrollees choose each metal tier, and how is the choice split subsidized vs unsubsidized?
4. How does plan selection distribute across California's 19 rating regions — is the premium-driven geography visible in enrollment?
5. How many people choose each of the four Silver plan variants (Silver 70, enhanced Silver 73, 84, 94)?
6. Which carriers gained or lost market share in the quarters immediately after the federal enhanced premium tax credits expired at the end of 2025? (Compare 2025 Q4, 2026 Q1, 2026 Q2.)
7. How many Medi-Cal enrollees are in managed care by plan and by month, through September 2026?
8. How many Medi-Cal-certified eligible individuals exist by age group and sex each month since 2010?

## How to use it

**Step 1 — search the catalogue via the CKAN API.**

```powershell
Invoke-RestMethod 'https://data.chhs.ca.gov/api/3/action/package_search?q=covered%20california%20enrollees&rows=20'
```

**Step 2 — get resource URLs for a dataset.**

```powershell
$j = Invoke-RestMethod 'https://data.chhs.ca.gov/api/3/action/package_show?id=qualified-health-plans-qhps-selected-by-covered-california-enrollees'
$j.result.resources | Select-Object name, format, url, created
```

**Step 3 — download and parse (strip the formatting artifacts).**

```powershell
$u = 'https://data.chhs.ca.gov/dataset/edfa74cb-5edd-43a5-906b-4ff93262b1c4/resource/795c45fc-8a27-484a-bd32-fa03175dbc5b/download/4.1-qhp-2026-q2_odp.csv'
$rows = curl.exe -s -L $u | ConvertFrom-Csv
$rows | Where-Object { $_.'Reporting Period' -eq '2026 Q2' } |
  ForEach-Object {
    [pscustomobject]@{
      HealthPlan = $_.'Health Plan '
      Subsidy    = $_.Subsidy
      Enrollees  = [int](($_.'Number of Eligible Individuals Who Selected Plan' -replace '[^0-9]','') )
    }
  }
```

Note the trailing space in the source header `Health Plan ` — it will break naive column lookups.

**Step 4 — preview without downloading.** CKAN DataStore endpoints support filtering:
`https://data.chhs.ca.gov/api/3/action/datastore_search?resource_id=<resource_uuid>&limit=50`

**Step 5 — geospatial layers.** Provider-location datasets come from a GIS API rather than CKAN storage, e.g. `https://gis.dhcs.ca.gov/api/download/v1/items/<item-id>/csv?layers=0`.

## Status and caveats

**Verified live on 2026-10-13:** `https://data.ca.gov/` (200); `https://data.chhs.ca.gov/` (200); CKAN `package_search` API on both origins (200); the four Covered California CSV resources (200, downloaded and parsed); `https://www.dhcs.ca.gov/data-reports/` (200); `https://www.dhcs.ca.gov/data-reports/medi-cal-eligibility-statistics/` (200).

**Do not resolve — no such host:** `healthdata.ca.gov`, `data.hhs.ca.gov`, and `data.health.ca.gov` all fail DNS resolution. Earlier guidance suggesting a consolidated `healthdata.ca.gov` portal does not match the live environment as of this date; the working CHHS host is `data.chhs.ca.gov`.

**Staleness:** the Covered California series is quarterly and the latest published period is **2026 Q2**. Because these are new-selection counts rather than stock enrollment, they cannot substitute for Covered California's own monthly Membership Dashboard when you need a current enrollment total.

**Licensing/terms:** CKAN default licence, no registration, no rate limit published. Public reporting requirement under Welfare and Institutions Code 14102.5, so the data is statutorily public.

**Quality flags:** use `$values = $_ -replace '[^0-9]',''` before casting; treat the carrier roster as time-varying; do not join these health-plan names directly to CMS `ISSUER ID` without a manual mapping.

**Not attempted:** I did not enumerate all 248 "medi-cal" datasets or drill into HCAI and Department of Health Care Access datasets. The API makes that enumeration trivial if needed.

## Sources

- [California Open Data portal — data.ca.gov (live)](https://data.ca.gov/)
- [California Health and Human Services Open Data portal — data.chhs.ca.gov (live, actual resource host)](https://data.chhs.ca.gov/)
- [CKAN API — package_search on data.chhs.ca.gov](https://data.chhs.ca.gov/api/3/action/package_search?q=medi-cal&rows=20)
- [QHPs Selected by Covered California Enrollees — CSV (verified live, parsed)](https://data.chhs.ca.gov/dataset/edfa74cb-5edd-43a5-906b-4ff93262b1c4/resource/795c45fc-8a27-484a-bd32-fa03175dbc5b/download/4.1-qhp-2026-q2_odp.csv)
- [Covered California Enrollees by Metal Tier — CSV (verified live, parsed)](https://data.chhs.ca.gov/dataset/b2282050-4fd7-418c-a466-726bc48da39e/resource/16feaa72-0827-4587-80f1-78d77adfaa84/download/4.3-metal-tier-q2-2026_odp.csv)
- [Covered California Enrollees by Rating Region — CSV](https://data.chhs.ca.gov/dataset/59d54d7e-01fa-4010-959c-535474764daa/resource/80e8a68e-6f84-4f0a-b963-77776a6b07d3/download/4.2-regions-q2-2026_odp.csv)
- [Covered California Enrollees by Silver Plan — CSV](https://data.chhs.ca.gov/dataset/a2034ac5-4ba7-4ebc-a2f4-787842e447ed/resource/a47c41bc-6cee-4bda-8c1e-d3532f92f76a/download/4.4-silver-q2-2026_odp.csv)
- [Medi-Cal Managed Care Enrollment Report — September 2026 CSV](https://data.chhs.ca.gov/dataset/c6ccef54-e7a9-4ebd-b79a-850b72c4dd8c/resource/95358a7a-2c9d-41c6-a0e0-405a7e5c5f18/download/open-data-portal-managed-care-enrollment-count-september-2026.csv)
- [Medi-Cal Enrollment by Eligibility Group — 2026 Q2 CSV](https://data.chhs.ca.gov/dataset/746835c6-17f4-43f0-b98b-f972cf6ee512/resource/d33eee4a-4c17-48da-8099-3fd2bac29ac2/download/7.1-total-medi-cal-enrollment-q2-2026-odp.csv)
- [Medi-Cal Certified Eligibles by Month with Demographics — September 2026 CSV](https://data.chhs.ca.gov/dataset/8c897320-ba87-4574-bc37-bae974191c35/resource/cc08b60f-393f-4e37-9b3e-976d7a9f2a72/download/t1_eligibility_by_age_group_sex_201001_sept2026.csv)
- [DHCS Data and Reports](https://www.dhcs.ca.gov/data-reports/)
- [DHCS Medi-Cal Eligibility Statistics](https://www.dhcs.ca.gov/data-reports/medi-cal-eligibility-statistics/)
- [DHCS GIS API — Medi-Cal Dental FFS Provider Listing CSV](https://gis.dhcs.ca.gov/api/download/v1/items/7d8d878c35224e9bb22749b3d3d33cc1/csv?layers=0)