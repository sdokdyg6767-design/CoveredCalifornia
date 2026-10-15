# CMS Marketplace Public Use Files (Exchange PUFs and State-Based Exchange QHP PUFs)

- **Retrieved:** 2026-10-13
- **Type:** External database / data source guide

## Summary

The Centers for Medicare & Medicaid Services (CMS) publishes downloadable Public Use Files (PUFs) containing every certified Qualified Health Plan (QHP) in the United States: one row per plan, per county, per rating area, per age, per household tier. Because California is a State-Based Exchange (SBE), California plan data is **not** in the federal Exchange PUFs — it is in the separate **SBE QHP PUF** series, one ZIP per state, which includes a complete California ZIP. This is the single most authoritative machine-readable source for "how many plans does each carrier offer in California", "which counties and ZIP codes does each carrier serve", and "what are the actual monthly premiums by rating area, age, and household tier" — none of which coveredca.com publishes.

## Key Facts

| Attribute | Detail |
| --- | --- |
| Publisher | CMS Center for Consumer Information and Insurance Oversight (CCIIO) |
| URL (California / SBE states) | https://www.cms.gov/marketplace/resources/data/state-based-public-use-files |
| URL (federal Exchange states) | https://www.cms.gov/marketplace/resources/data/public-use-files |
| Access | Free, no registration |
| Coverage | All 50 states + DC; per-state ZIPs for the 19 SBE states including California; 2014–2026 plan years published |
| Current as of | 2026 plan year (data current as of June 03 2026 for SBE files; Exchange PUF page last modified 08/26/2026) |
| Update cadence | Annual release per plan year, plus periodic mid-year corrections (issuer data corrections, SHOP quarterly rate updates) |
| Machine-readable | CSV inside ZIP; data dictionaries as PDF inside ZIP |
| Volume | California 2026 ZIP is 1,025,734 bytes compressed / ~33 MB uncompressed across 6 CSVs; CARates alone is 93,840 data rows |

**Is 2027 plan-year data published as of 2026-10-13? NO.** Verified: the SBE PUF page has year sections labeled "2026 SBE QHP PUF Datasets" down to "2016 SBE QHP PUF Datasets" and **no 2027 section**. The federal Exchange PUF page's own "Further Information" paragraph reads "The plan year 2026 Exchange PUFs will be updated regularly..." — 2026 is the latest. Test URLs for 2027 assets all return HTTP 404:
- `https://www.cms.gov/files/zip/californiasbpuf2027.zip` → 404
- `https://www.cms.gov/files/zip/sbe-puf-files-2027.zip` → 404
- `https://www.cms.gov/files/zip/2027-sbe-qhp-puf-data-dictionary.zip` → 404
- `https://www.cms.gov/files/document/planattributes-datadictionary-py27.pdf` → 404 (the py26 version returns 200)

**Plan-year timing evidence:** the California 2026 file was imported `1/13/2026` (`IMPORT DATE` in every CSV row) for plans effective `1/1/2026`. The California 2025 file was imported `01-13-2025`. Based on this two-year pattern, plan-year 2027 California data would be expected around January 2027, after 2027 SERFF rate filings are approved. Treat that as an inference from observed behavior, not a CMS commitment.

## What it contains

### Primary source for California: SBE QHP PUF

Download page: https://www.cms.gov/marketplace/resources/data/state-based-public-use-files

California ZIPs (all verified by HTTP HEAD/GET on 2026-10-13):

| Plan year | URL | Status |
| --- | --- | --- |
| 2026 | https://www.cms.gov/files/zip/californiasbpuf2026.zip | 200, 1,025,734 bytes |
| 2025 | https://www.cms.gov/files/zip/californiasbepuf2025.zip | 200, 1,021,038 bytes |
| 2024 | https://www.cms.gov/files/zip/californiasbepuf2024.zip | link present on page |
| 2023 | https://www.cms.gov/files/zip/california-sbe-qhp-puf-2023.zip | 200, 877,444 bytes |
| 2022 | https://www.cms.gov/files/zip/californiasbepuf2022.zip | link present on page |
| 2021 | https://www.cms.gov/files/zip/pufca2021.zip | 200, 1,463,444 bytes |

**Naming gotcha worth knowing:** the 2026 California filename is `californiasbpuf2026.zip` — "sbpuf", not "sbepuf". Every other state and every prior year uses `sbepuf`. The naive construction `californiasbepuf2026.zip` returns **404** even though the data exists. This is the single most likely reason a researcher concludes the 2026 California data was never published.

Contents of `californiasbpuf2026.zip` (file names embed a MMDDYYYY load stamp):

| File | Uncompressed bytes | Rows (verified) | Purpose |
| --- | --- | --- | --- |
| `CAPlans05052026.csv` | 1,173,090 | 1,010 data rows | One row per plan variant; 154 columns |
| `CARates05052026.csv` | 13,127,074 | 93,840 data rows | Monthly premium by plan, rating area, age, tobacco, tier |
| `CABenefits05052026.csv` | 18,128,622 | — | Every EHB cost-sharing line item per plan and service category |
| `CAServiceAreas05052026.csv` | 351,947 | 1,182 data rows | Issuer → county → ZIP service geography |
| `CANetworks05052026.csv` | 2,671 | — | Network IDs, network tier, multi-plan/network flags |
| `CABusinessRules05052026.csv` | 349 | — | Maximum out-of-pocket and deductible business-rule reference |

**Naming convention:** `<STATE><FileType><MMDDYYYY>.csv`, e.g. `CAPlans05052026.csv` = California Plans file loaded 2026-05-05. Note the internal `IMPORT DATE` column reads `01-13-2026` while the filename reads `05052026` — the filename stamp is the CMS refresh date, the column is the SERFF import date. Use the filename for version tracking.

**2026 California verified counts** (from `CAPlans05052026.csv`):

- 1,010 plan rows, 14 distinct `ISSUER ID` values: 18126, 27603, 40513, 47579, 51396, 62683, 67138, 68744, 70285, 84014, 92499, 92815, 93689, 97389
- Plan counts per issuer: 70285 = 524 plans, 67138 = 206, 40513 = 52, 92499 = 49, 47579 = 38, 27603 = 37, 93689 = 32, 18126 = 16, 51396 = 16, 84014 = 16, 92815 = 16, 62683 = 6, 68744 = 1, 97389 = 1
- Metal levels: Silver 364, Gold 228, Platinum 221, Expanded Bronze 147, High 29, Catastrophic 21
- Plan types: HMO 840, PPO 151, EPO 19 (sums to 1,010)
- 19 rating areas (`Rating Area 1` … `Rating Area 19`)
- 59 distinct counties in the service-area file; 85 distinct `SERVICE AREA ID` values

> **Second-pass correction (2026-10-14).** An earlier draft stated plan types as "HMO 857, PPO 151, EPO 19". Those figures summed to 1,027, which contradicted the 1,010 verified plan rows. Re-parsing `CAPlans05052026.csv` gives **HMO 840, PPO 151, EPO 19 = 1,010**. Corrected above.
>
> Every other figure in this section was independently re-derived from the downloaded ZIP on 2026-10-14 and matched exactly: 1,010 plan rows; 93,840 rate rows; 1,182 service-area rows; 14 issuer IDs and every per-issuer plan count; all six metal-level counts; 19 `RATING AREA ID` values; and the Molina Expanded Bronze age-27 range of $345.36–$400.74 across 6 rating areas.

**Real example rows** (verbatim from `CAPlans05052026.csv`, row 1): `BUSINESS YEAR = 2026`, `STATE CODE = CA`, `ISSUER ID = 18126`, `PLAN MARKETING NAME = Platinum 90 HMO`, `HIOS PRODUCT ID = 18126CA001`, `SERVICE AREA ID = CAS001`, `PLAN TYPE = HMO`, `METAL LEVEL = Platinum`, `PLAN ID = 18126CA0010001-01`, `AV CALCULATOR OUTPUT NUMBER = 0.919208836`, `TEHB INN TIER 1 INDIVIDUAL MOOP = $5,000`, `PLAN EFFECTIVE DATE = 1/1/2026`, `PLAN EXPIRATION DATE = 12/31/2026`.

**Real premium example** (verbatim from `CARates05052026.csv`): `BUSINESS YEAR = 2026`, `ISSUER ID = 18126`, `PLAN ID = 18126CA0010001`, `RATING AREA ID = Rating Area 13`, `TOBACCO = No Preference`, `AGE = 0-14`, `QHP_NON_QHP_TYPE_ID = On the Exchange`, `INDIVIDUAL RATE = 412.55`, `RATE EFFECTIVE DATE = 2026-01-01`, `RATE EXPIRATION = 2026-12-31`.

Verified 2026 California monthly individual premiums for a 27-year-old, non-tobacco, across all 19 rating areas:

| Issuer | Metal | Plans/rating areas | Min 27-yr individual rate | Max |
| --- | --- | --- | --- | --- |
| 18126 (Molina) | Expanded Bronze | 6 | $345.36 | $400.74 |
| 18126 (Molina) | Silver | 6 | $376.78 | $437.19 |
| 18126 (Molina) | Gold | 6 | $430.21 | $499.19 |
| 18126 (Molina) | Platinum | 6 | $487.07 | $565.17 |
| 27603 (Blue Cross of California / Anthem BC) | Expanded Bronze | 32 | $343.54 | $775.91 |
| 27603 | Silver | 19 | $398.90 | $900.37 |
| 27603 | Platinum | 19 | $724.52 | $1,632.14 |
| 70285 | Expanded Bronze | 150 | $310.46 | $729.18 |
| 70285 | Silver | 187 | $367.50 | $900.09 |
| 70285 | Platinum | 149 | $462.66 | $1,479.62 |

### Geography and carrier names

`CAServiceAreas05052026.csv` carries the carrier names that `CAPlans` omits. Verified `ISSUER ID` → `SERVICE AREA NAME` mapping:

| ISSUER ID | Service area names observed |
| --- | --- |
| 18126 | Molina Marketplace |
| 27603 | Blue Cross of California(Anthem BC)Dental / Blue Cross of California(Anthem BC)DentalHMO / Blue Cross of California(Anthem BC)1,2,3,…,14 |
| 40513 | SHOP / INDIVIDUAL |
| 47579 | San Francisco / San Mateo / SF and SM County |
| 51396 | QHP IEHP 1 |
| 62683 | PPO INDIVIDUAL / PPO SHOP / DHMO INDIVIDUAL |
| 67138 | Ambetter PPO 1 / Ambetter PPO 2 / Ambetter PPO 3 |
| 68744 | Dental |
| 70285 | PPO Service Region / Dental Statewide / Full PPO for CCSB |
| 84014 | QHP Region 7 |
| 92499 | Region 19 HMO 1 / Region 19 HMO 2 |
| 92815 | LACC Service Area |
| 93689 | WHA NETWORK |
| 97389 | CDN CC DHMO Network |

Columns (19): `BUSINESS YEAR, STATE CODE, ISSUER ID, SOURCE NAME, VERSION NUMBER, IMPORT DATE, SERVICE AREA ID, SERVICE AREA NAME, COVER ENTIRE STATE, COUNTY, COUNTY NAME, PARTIAL COUNTY, ZIP CODE, PARTIAL COUNTY JUSTIFICATION, MARKET COVERAGE, DENTAL PLAN ONLY`.

Verified row showing the ZIP-level detail: `SERVICE AREA ID = CAS001`, `SERVICE AREA NAME = Molina Marketplace`, `COUNTY = Los Angeles - 06037`, `COUNTY NAME = Los Angeles`, `PARTIAL COUNTY = true`, `ZIP CODE = 90001, 90002, … 91801, 91803` (a single comma-separated cell listing roughly 800 LA ZIPs), `PARTIAL COUNTY JUSTIFICATION = 18126 2025-04-30 PY2026 SuppDoc_ServiceArea_PartialCounty`.

### Secondary source: Exchange PUFs (federal states, NOT California)

Download page: https://www.cms.gov/marketplace/resources/data/public-use-files (page last modified 08/26/2026). Files are at `https://download.cms.gov/marketplace-puf/<plan-year>/<slug>.zip`, with slugs: `plan-attributes-puf.zip`, `benefits-and-cost-sharing-puf.zip`, `rate-puf.zip`, `service-area-puf.zip`, `business-rules-puf.zip`, `network-puf.zip`, `plan-id-crosswalk-puf.zip`, `machine-readable-url-puf.zip`, `transparency-in-coverage-puf.zip`. Years 2014–2026 are published, e.g. `https://download.cms.gov/marketplace-puf/2026/plan-attributes-puf.zip`. **California is absent from these files** because Covered California is an SBE.

## What it does NOT contain

1. **No 2027 data.** Neither the SBE QHP PUF nor the Exchange PUF series has published plan-year 2027 files as of 2026-10-13. There are no 2027 data dictionaries either. Any claim of "2027 California premiums" sourced from CMS PUFs as of this date is unsupported.
2. **California is not in the Exchange PUFs.** If you download the federal `plan-attributes-puf.zip` you will not find a single California plan. Use the SBE ZIP.
3. **No enrollment counts.** The PUFs describe plans, not people. There is no member, enrollment-effectuation, or persistency field anywhere in the six California CSVs.
4. **No actual premiums paid, only filed rates.** `INDIVIDUAL RATE` is the approved filed monthly premium for that age/tier/rating area. It excludes any subsidy, American Indian cost-sharing exemption, employer contribution, or extra assistance and does not reflect what a given enrollee actually paid.
5. **ZIP coverage is sparse and one-directional.** Only 53 of the 1,182 service-area rows carry a populated `ZIP CODE` value; the rest are county-level with `PARTIAL COUNTY = false`. A blank `ZIP CODE` does not mean the carrier does not serve the county — it means the county is served in full. Treat `ZIP CODE` as a partial-county refinement, not as the complete ZIP list.
6. **`ISSUER ID` is a CMS NAIC-based identifier, not a Covered California carrier name**, and `CAPlans` does not carry an issuer name field at all (the `ISSUER NAME` column exists in the header but is empty in every row). You must build the name mapping from `CAServiceAreas` service-area names, which are inconsistently formatted.
7. **No rating-area geography table.** `CARates` uses `Rating Area 1`–`Rating Area 19` as opaque labels. Mapping a rating area to counties or ZIPs is **not** included in the PUF and requires the separate Covered California or SERFF rating-area geography file. Premiums by literal ZIP code are therefore not directly derivable from the PUF alone.
8. **SHIP (small-group) and dental plans are mixed in.** Several issuers carry `MARKET COVERAGE = Individual/SHOP (Small Group)` and there are dental-only service areas (`DENTAL PLAN ONLY = Yes`). Filter before counting.
9. **Stale relative to mid-year corrections.** The California 2026 files were loaded 2026-05-05. Issuer corrections approved after that date are not reflected.

## Questions it can answer that coveredca.com cannot

1. How many plans does each California carrier offer in plan year 2026, broken out by metal tier and plan type? (Answerable: 1,010 plan rows across 14 issuer IDs, full crosstab available.)
2. Which counties and which ZIP codes does Molina serve in California, and which of those are partial-county? (Answerable from `CAServiceAreas` with `PARTIAL COUNTY` flag.)
3. What is the cheapest 27-year-old Expanded Bronze monthly premium in Los Angeles for a specific carrier in 2026, by rating area? (Answerable for rating areas; requires a rating-area geography crosswalk to translate to a ZIP.)
4. Does Molina's service territory in Los Angeles County match its 2027 announced exit from northeast LA and Orange County — and how many of its 16 plans sit in service areas that overlap those ZIPs?
5. How wide is the premium spread between the cheapest and most expensive Platinum plan in a given California county for a given age and household composition?
6. Which issuers offer only PPO (no HMO), and which offer only HMO? (`PLAN TYPE` crosstab against `ISSUER ID`.)
7. What is the individual actuarial value (`AV CALCULATOR OUTPUT NUMBER`) of each plan, enabling metal-tier comparison independent of marketing name?
8. What are the exact out-of-pocket maximums and deductibles for a specific plan, at the EHB and DEHB (dental) levels separately?

## How to use it

**Step 1 — get California data for the most recent published plan year.**

```powershell
# 2026 (note the "sbpuf" filename)
Invoke-WebRequest -Uri 'https://www.cms.gov/files/zip/californiasbpuf2026.zip' `
  -OutFile "$env:TEMP\ca2026.zip" -UseBasicParsing
Expand-Archive "$env:TEMP\ca2026.zip" "$env:TEMP\ca2026" -Force
```

**Step 2 — plan counts per carrier per metal tier.**

```powershell
$plans = Import-Csv "$env:TEMP\ca2026\CAPlans05052026.csv"
$plans | Group-Object 'ISSUER ID','METAL LEVEL' |
  Select-Object Count, Name | Sort-Object Name
```

**Step 3 — carrier name lookup.**

```powershell
$sa = Import-Csv "$env:TEMP\ca2026\CAServiceAreas05052026.csv"
$sa | Select-Object 'ISSUER ID','SERVICE AREA NAME' -Unique
```

**Step 4 — service geography for one carrier.**

```powershell
$sa | Where-Object { $_.'ISSUER ID' -eq '18126' } |
  Select-Object 'SERVICE AREA NAME','COUNTY NAME','PARTIAL COUNTY','ZIP CODE'
```

**Step 5 — premiums for one plan, one age, all rating areas.**

```powershell
$rates = Import-Csv "$env:TEMP\ca2026\CARates05052026.csv"
$rates | Where-Object { $_.'ISSUER ID' -eq '18126' -and $_.'AGE' -eq '27' } |
  Select-Object 'PLAN ID','RATING AREA ID','INDIVIDUAL RATE','COUPLE',
                'PRIMARY SUBSCRIBER AND ONE DEPENDENT'
```

**Join keys (exact names, SBE QHP PUF):**

| Join | Key | Notes |
| --- | --- | --- |
| CAPlans ↔ CARates | `STANDARD COMPONENT ID` (in CAPlans) = `PLAN ID` (in CARates) | **The two files name the same key differently.** `CAPlans` also has a `PLAN ID` column, but it is the *variant* ID (`18126CA0010001-01`) and does **not** appear in `CARates`. Joining on CAPlans.`PLAN ID` to CARates.`PLAN ID` silently yields near-zero rows. |
| CAPlans ↔ CAServiceAreas | `ISSUER ID` + `SERVICE AREA ID` | Not to plan level; a service area covers many plans. |
| CARates ↔ CAServiceAreas | `ISSUER ID` + `RATING AREA ID` → counties | **No direct join key exists.** `RATING AREA ID` does not appear in the service-area file. An external rating-area geography table is required. |
| Everything ↔ issuer identity | `ISSUER ID` | Five-digit CMS/NAIC-style issuer ID. |

**Filtering parameters:** there is no query API. These are static ZIP files of CSVs. The only machine-readable access path is HTTP GET on the ZIP. The Socrata-style catalog endpoints that historically served CMS data (`https://data.cms.gov/data/api/catalog/v1`) now return the client-rendered data.cms.gov HTML shell rather than JSON, and the CMS Provider Data Catalog API (`https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items`, 237 entries verified) contains only hospital/physician/facility datasets — **no marketplace or plan datasets at all**.

**Data dictionaries** (needed to decode column names): `https://www.cms.gov/files/zip/sbe-puf-files-2026.zip` (200, 2,721,009 bytes) contains six PDFs — `2026 Plan PUF Data Dictionary.pdf`, `2026 Rate PUF Data Dictionary.pdf`, `2026 Service Area PUF Data Dictionary.pdf`, `2026 Network PUF Data Dictionary.pdf`, `2026 Business Rules PUF Data Dictionary.pdf`, `2026 BeneCS PUF Data Dictionary.pdf`. Also `https://www.cms.gov/files/document/planattributes-datadictionary-py26.pdf` (200, 458,535 bytes) and `https://www.cms.gov/files/document/exchange-pufs-faqs-py26.pdf` (200, 145,422 bytes).

## Status and caveats

**Verified live on 2026-10-13:** `https://www.cms.gov/marketplace/resources/data/state-based-public-use-files` (200; page last modified 06/26/2026 08:37 AM); `https://www.cms.gov/marketplace/resources/data/public-use-files` (200; last modified 08/26/2026 09:27 AM); `californiasbpuf2026.zip` (200, downloaded and parsed); `californiasbepuf2025.zip` (200, downloaded and parsed); `sbe-puf-files-2026.zip` (200, downloaded and listed).

**Confirmed dead (HTTP 404, verified 2026-10-13):** all four `www.cms.gov/marketplace/data*` URLs, `www.cms.gov/marketplace/data/public-use-files`, `www.cms.gov/marketplace/data/browsable-data`, `www.cms.gov/marketplace/data/downloads`, `www.cms.gov/marketplace/compendium`, `www.cms.gov/marketplace/compendium-data-reporting`, `www.cms.gov/marketplace/information-partners/public-use-files`, `www.cms.gov/marketplace/plan-management-puf`, `www.cms.gov/marketplace/plan-management-data`, `www.cms.gov/marketplace/data-research`, `www.cms.gov/files/zip/attributes-2026-2027.zip`, and the bare host root `https://download.cms.gov/` (404 at root; the `marketplace-puf/...` paths under it are linked from the live page but were not individually downloaded during this pass).

**Known CMS defect:** the California 2026 hyperlink on the SBE PUF page points to `californiasbpuf2026.zip`, which differs from the naming convention used for all other states and years. The plausible alternative `californiasbepuf2026.zip` 404s. Copy the link from the page rather than constructing it.

**Licensing/terms:** the PUF download page carries a disclaimer and a DUA/disclaimer PDF for SBE files (`/files/document/sbe-qhp-puf-disclaimagree-py26.pdf`). Treat the data as public but attribute CMS CCIIO and do not republish as a CMS product.

**Not verified:** the individual `download.cms.gov/marketplace-puf/2026/*.zip` files were read from the live page's href list but not downloaded in this pass, because they contain no California rows. Treat their availability as highly likely but not independently confirmed here.

## Sources

- [CMS — State-Based Exchange QHP Public Use Files (live)](https://www.cms.gov/marketplace/resources/data/state-based-public-use-files)
- [CMS — Health Insurance Exchange Public Use Files (live)](https://www.cms.gov/marketplace/resources/data/public-use-files)
- [California 2026 SBE QHP PUF ZIP (verified live, note filename)](https://www.cms.gov/files/zip/californiasbpuf2026.zip)
- [California 2025 SBE QHP PUF ZIP (verified live, downloaded and parsed)](https://www.cms.gov/files/zip/californiasbepuf2025.zip)
- [California 2023 SBE QHP PUF ZIP](https://www.cms.gov/files/zip/california-sbe-qhp-puf-2023.zip)
- [California 2021 SBE QHP PUF ZIP](https://www.cms.gov/files/zip/pufca2021.zip)
- [2026 SBE QHP PUF data dictionaries (all six PDFs)](https://www.cms.gov/files/zip/sbe-puf-files-2026.zip)
- [2025 SBE QHP PUF data dictionary](https://www.cms.gov/files/zip/2025-sbe-qhp-puf-datadictionary.zip)
- [CMS Plan Attributes data dictionary, PY2026](https://www.cms.gov/files/document/planattributes-datadictionary-py26.pdf)
- [CMS Exchange PUFs FAQ, PY2026](https://www.cms.gov/files/document/exchange-pufs-faqs-py26.pdf)
- [CMS — Marketplace landing page](https://www.cms.gov/marketplace)
- [CMS Data (data.cms.gov) — client-rendered shell, content not reachable via plain fetch](https://data.cms.gov/)
- [CMS Provider Data Catalog API — 237 entries, none marketplace-related](https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items)