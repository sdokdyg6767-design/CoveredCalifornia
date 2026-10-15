# Carrier Regulatory and Financial Sources (DMHC, California Department of Insurance, NAIC)

- **Retrieved:** 2026-10-13
- **Type:** External database / data source guide

## Summary

California splits health-plan regulation between three bodies, and which one regulates a carrier determines which filings are public: **Covered California** certifies and regulates individual-market QHPs, **DMHC** regulates HMOs and Medi-Cal plans, and the **California Department of Insurance** regulates PPO insurers, dental insurers and the off-exchange market. DOI is the only one of the three publishing downloadable machine-readable filing data on open URLs. Important structural caveat: DOI's headline rate-filing workbook turned out on inspection to contain **no health line-of-business filings at all**, and DMHC's site is blocked by an edge WAF from this environment, so its datasets could not be verified here.

## Key Facts

| Attribute | Detail |
| --- | --- |
| Publishers | California Department of Managed Health Care (DMHC); California Department of Insurance (DOI); NAIC |
| DMHC URL | https://dmhc.ca.gov/ — **returns HTTP 403 to every client tested** (Akamai "Access Denied") |
| DOI URL | https://www.insurance.ca.gov/ — 200 OK |
| DOI viewing room | https://www.insurance.ca.gov/01-consumers/135-viewing-room — 200 OK |
| NAIC URL | https://content.naic.org/ — **returns HTTP 403 to every client tested** |
| Access | Free, no registration. No API keys on any of the verified endpoints |
| Coverage | DMHC: HMO and Medi-Cal managed care. DOI: PPO, dental, accident-and-health, and all other licensed classes. NAIC: multistate, filer-reported |
| Current as of | DOI rate-filing approval list current through 9/30/2026. DOI dental MLR reports current through 2021 |
| Update cadence | DOI approval list: rolling year-to-date workbook. DMHC: annual and quarterly (unverified). NAIC: annual statutory filings (unverified) |
| Machine-readable | DOI: XLS/XLSX workbooks on direct URLs. DMHC and NAIC: not verified |
| Volume | DOI approval workbook 3,994 rows × 13 columns, 272,952 bytes |

## What it contains

### California Department of Insurance (verified live)

**Virtual Viewing Room** — https://www.insurance.ca.gov/01-consumers/135-viewing-room (also at https://www.insurance.ca.gov/0250-insurers/0800-rate-filings/0050-viewing-room/index.cfm). The site's own navigation blurb, quoted verbatim: *"This virtual viewing room allows you to see insurance company rate filings, examination reports, and related information."* This is the single most valuable DOI resource for carrier oversight documents. Its internal contents could not be enumerated in this pass (the page returned no data tables to a plain HTTP fetch), so treat its filing inventory as unverified.

**Rate Filing Approval Lists** — https://www.insurance.ca.gov/0250-insurers/0800-rate-filings/0100-rate-filing-lists/rate-filing-approvals/index.cfm (200). Publishes a rolling year-to-date Excel workbook of closed rate filings. Verified files on that page, most recent first:

| File | URL | Status |
| --- | --- | --- |
| Approval Closed List YTD 9-30-26 | `.../rate-filing-approvals/upload/Approval-Closed-List-YTD-9-30-26.xlsx` | **200, 272,952 bytes, downloaded and parsed** |
| Approval Closed List YTD 12-31-25 | `.../upload/Approval-Closed-List-YTD-12-31-25.xlsx` | linked |
| Approval Closed List YTD 12-31-24 through 12-31-19 | `.../upload/Approval-Closed-List-YTD-12-31-{19..24}.{xls|xlsx}` | linked |

Verified column headers, verbatim from row 1 of `Approval-Closed-List-YTD-9-30-26.xlsx`:

```
FILE | NAME | GRP # | NAIC # | LINE TYPE | LINE CODE | PROGRAM | FILING TYPE | % RATE CHNG REQ | % RATE CHNG APPVD | STATUS | CLOSED DATE | SERFF FILING #
```

Verified data rows, verbatim:

```
25-2257 | ACCELERANT NATIONAL INSURANCE COMPANY | 4997 | 10220 | COMMERCIAL | MULTI-PERIL | MINICO ARTISAN CONTRACTORS | RULE AND FORMS | APPROVED | 46029 | SPRO-G134724465
26-891 | ACCELERANT NATIONAL INSURANCE COMPANY | 4997 | 10220 | COMMERCIAL | INLAND MARINE | AAIS INLAND MARINE GUIDE | RULE CHANGE | APPROVED | 46225 | SPRO-G134963620
```

`CLOSED DATE` is stored as a serial number (46029, 46225) that must be converted from the 1900 date system.

**Two findings that materially change how this source should be used:**

1. **No health filings in the current workbook.** The workbook's `LINE TYPE` column has exactly two distinct values across all 3,994 rows: `COMMERCIAL` and `PERSONAL`. Every health-related program name I found is either a D&O product for healthcare organizations (Allied World Assurance's `FORCEFIELD HEALTHCARE ORG.(D&O, EPL)`), a captive-state pet insurer (`AMERICAN PET INSURANCE COMPANY`), or pet/healthcare professional liability. There are **no accident-and-health rate filings in this file.** Anyone who assumes this workbook contains health-plan rate increases will be wrong.
2. **The `NAIC #` and `GRP #` columns are a free carrier-identifier crosswalk.** Verified mappings include NAIC 10220 / group 4997 = Accelerant National Insurance Company; NAIC 19489 / group 158 = Allied World Assurance Company (U.S.) Inc.; NAIC 16624 / group 158 = Allied World Specialty Insurance Company; NAIC 12190 / group 5008 = American Pet Insurance Company; NAIC 37273 / group 3416 = Axis Insurance Company. This is directly useful for joining DOI records to the CMS SBE `ISSUER ID` values, which are NAIC-based.

**Dental Medical Loss Ratio (MLR) reports** — https://www.insurance.ca.gov/01-consumers/110-health/60-resources/10-dmlr/Index.cfm (200). Per-dental-carrier Excel workbooks, published annually. Verified live files:

- `https://www.insurance.ca.gov/01-consumers/110-health/60-resources/10-dmlr/2021/upload/Blue-Shield-of-CA-Life-Health-Insurance-Company-2021-Dental-MLR-Report.xlsx` (200, 181,983 bytes)
- `https://www.insurance.ca.gov/01-consumers/110-health/60-resources/upload/Blue-Shield-of-CA-Life-Health-Insurance-Company-2020-Dental-MLR-Report.xlsx` (200, 135,075 bytes)

Also verified present for 2021: Aetna Life Insurance Company, Ameritas Life Insurance Corp, Anthem Blue Cross Life & Health Insurance Company, BCS Insurance Company, Chesapeake Life Insurance Company, Cigna Health & Life Insurance Company, Colonial Life & Accident Insurance Company, Connecticut General Life Insurance Company, Dentegra Insurance Company, First Health Life & Health Insurance Company, Golden Rule Insurance Company, and others.

**Other verified DOI pages:**

- License status inquiry: https://www.insurance.ca.gov/0200-industry/0008-check-license-status/ (200) — redirects from the consumer path `/01-consumers/103-check-license-status`
- Health insurance landing: https://www.insurance.ca.gov/01-consumers/110-health/ (200)
- HMO/PPO carrier list for consumers: https://www.insurance.ca.gov/01-consumers/110-health/20-look/hcpcarriers.cfm (200)
- Health Insurance Covered Lives Report: https://www.insurance.ca.gov/01-consumers/110-health/coveredlivesrpt.cfm (200)
- Rate Filings and Review: https://www.insurance.ca.gov/01-consumers/110-health/70-rates/index.cfm (200)
- Health Insurance Mergers: https://www.insurance.ca.gov/01-consumers/110-health/60-resources/Health-Insurance-Mergers.cfm (200)
- Data & Reports: https://www.insurance.ca.gov/0250-insurers/0600-data-reports/ (200)
- Statistical plans: https://www.insurance.ca.gov/0400-news/0200-studies-reports/1100-statistical-plans/index.cfm (200)
- Sitemap: https://www.insurance.ca.gov/sitemap.xml (200, valid)

### California Department of Managed Health Care (not verified)

Every DMHC URL tested returned HTTP 403, from both a plain HTTP client and an independent fetch path:

- `https://dmhc.ca.gov/` → 403
- `https://www.dmhc.ca.gov/` → 403
- `https://dmhc.ca.gov/Reports.aspx` → 403
- `https://dmhc.ca.gov/About/NewsRoom.aspx` → 403
- `https://dmhc.ca.gov/Regulatory/HealthPlanData.aspx` → 403
- `https://dmhc.ca.gov/DataAndReports` → 403

The error body identifies the blocker: an Akamai edge reference (`errors.edgesuite.net`), returned as *"Access Denied"* even with full browser-style request headers. This is consistent with a WAF rule blocking non-browser clients or a specific network range, not with the pages being gone. DMHC is the regulator of record for HMOs and Medi-Cal managed care, so its annual HMO enrollment reports, plan-level financial statements and enforcement records are exactly the right sources for HMO carrier health — but I could not open a single one and am therefore describing it as unverified rather than reporting contents I did not see.

### NAIC (not verified)

- `https://naic.org/` → 403
- `https://content.naic.org/` → 403
- `https://content.naic.org/company-information` → 403

NAIC blocks automated clients as a matter of course and requires registration for much of its company-level content, including financial statements. The NAIC Company Profile lookup is the standard public route to a carrier's statutory financials, but I could not verify either its availability or its access terms from here.

## What it does NOT contain

1. **DOI does not regulate Covered California QHPs.** Individual-market QHPs are certified and regulated by Covered California itself. DOI's filings cover a different population — PPO, dental, off-exchange and accident-and-health insurers. Do not treat a DOI filing as evidence about a QHP.
2. **DOI's rate-filing approval workbook contains no health filings.** Verified: only `COMMERCIAL` and `PERSONAL` line types across all 3,994 rows. This is the most important negative finding in this file.
3. **DMHC contents are entirely unverified here.** Everything known about DMHC's public datasets in this guide is background knowledge, not something I retrieved. The URLs above are unverified and may be wrong, may have moved, or may be blocked permanently.
4. **NAIC contents and pricing are unverified.** NAIC's statutory financial data may require paid membership or registration.
5. **No enrolled-lives or enrollment counts in the DOI approval workbook.** It is a filing-status register, not an enrollment database. Use Covered California or DHCS for enrollment.
6. **The dental MLR series stops at 2021.** Only 2020 and 2021 workbooks are linked. Do not assume newer years exist.
7. **No enforcement actions for QHP carriers anywhere in these sources.** QHP carrier enforcement is a Covered California function and I found no public enforcement database for it in this pass.
8. **The DOI Viewing Room contents are unverified.** The page loads; its filing inventory did not render to a plain HTTP client.

## Questions it can answer that coveredca.com cannot

1. Which California insurance entities hold which license, and is that license current? (DOI license status inquiry.)
2. Which insurers have had rate filings approved, at what requested rate change and what approved rate change, for which programs? (DOI approval workbook — for commercial and personal lines, not health.)
3. What is each dental insurer's medical loss ratio in California? (DOI dental MLR workbooks, 2020–2021.)
4. What is the NAIC company number for a given California carrier, allowing a join to CMS SBE `ISSUER ID`? (DOI workbook `NAIC #` and `GRP #` columns.)
5. Which health insurers are authorized to operate in California, and what are their HMO/PPO authorizations? (DOI HMO/PPO carrier list, unverified for content.)
6. How many covered lives does each California health insurer report? (DOI Health Insurance Covered Lives Report.)
7. Have two California health insurers proposed or completed a merger? (DOI Health Insurance Mergers page.)

## How to use it

**Step 1 — download the current rate-filing approval workbook.**

```powershell
$u = 'https://www.insurance.ca.gov/0250-insurers/0800-rate-filings/0100-rate-filing-lists/rate-filing-approvals/upload/Approval-Closed-List-YTD-9-30-26.xlsx'
curl.exe -g -s -L -o "$env:TEMP\cdi_approvals.xlsx" $u
```

Note the filename carries a rolling date, not a plan year. Re-fetch the approvals index page to discover the current filename rather than guessing.

**Step 2 — build the NAIC crosswalk before joining to CMS data.**

```powershell
$x = Import-Excel -Path "$env:TEMP\cdi_approvals.xlsx"   # or open in Excel/LibreOffice
$x | Select-Object 'FILE','NAME','GRP #','NAIC #','LINE TYPE','LINE CODE','PROGRAM','FILING TYPE','% RATE CHNG REQ','% RATE CHNG APPVD','STATUS','CLOSED DATE','SERFF FILING #' |
  Sort-Object 'NAIC #' -Unique
```

Match on `NAIC #` against the CMS SBE QHP PUF `ISSUER ID` — but note that DOI's NAIC numbers here belong to property/casualty carriers, so the join will only resolve for entities that are licensed in both capacities.

**Step 3 — read the dental MLR workbooks.** Download any of the per-carrier XLSX files from the DMLR index and read the medical loss ratio, premium and paid-claims columns directly.

**Step 4 — check a carrier's license status.** Use https://www.insurance.ca.gov/0200-industry/0008-check-license-status/ and search by license number or company name. The form did not render a `<form>` element to a plain HTTP client in this pass, so it likely requires a browser or a postback; use a browser.

**Step 5 — for QHP carrier financial condition, you are largely out of luck.** Covered California does not publish QHP rate filings or carrier financial statements as a machine-readable series, DMHC does not regulate QHPs, and DOI's health rate filings are not in the workbook. Documented "Actuarial Rate Justification" reports for the California individual market — standard public in many other states — were not located in this pass. If you need QHP rate justification detail, a California Public Records Act request to Covered California is the realistic route.

## Status and caveats

**Verified live on 2026-10-13 (DOI):** `insurance.ca.gov` root, license status inquiry, health insurance landing, HMO/PPO carrier list, Covered Lives Report, Rate Filings and Review, Health Insurance Mergers, Data & Reports, Statistical Plans, Rate Filing Approval index, Virtual Viewing Room (both URLs), DMLR index, sitemap, and the `Approval-Closed-List-YTD-9-30-26.xlsx` workbook (downloaded and parsed), and two Blue Shield dental MLR workbooks.

**Verified blocked (HTTP 403, both a plain client and an independent fetch path):** all DMHC URLs including `dmhc.ca.gov/`, `www.dmhc.ca.gov/`, `Reports.aspx`, `About/NewsRoom.aspx`, `Regulatory/HealthPlanData.aspx`, `DataAndReports`; all NAIC URLs including `naic.org/`, `content.naic.org/`, `content.naic.org/company-information`. DMHC's block originates at an Akamai edge.

**HTTP status quirk:** many `insurance.ca.gov` paths return **HTTP 200 while serving the site's `/404.html` error page**. A bare status check is not sufficient — I confirmed this with `/01-consumers/105-type/95-guides/01-health/`, `/01-licenses/`, and `/01-consumers/110-health/0500-health-insurers-in-california/`, all of which returned 200 with `final=https://www.insurance.ca.gov/404.html`. Always check the effective URL, not just the status code.

**Staleness:** DOI approval list current to 9/30/2026 (current); dental MLR stale by five years (2021); DOI other reports not date-verified.

**Licensing/terms:** DOI pages carry a Google Custom Search widget (`www.google.com/cse`) and standard state public-records terms. No paywall observed on any verified endpoint.

**Unverified, explicitly:** all DMHC datasets; all NAIC datasets; the DOI Viewing Room filing inventory; the contents of the DOI Data & Reports page; the HMO/PPO carrier list contents; the Covered Lives Report contents; whether any QHP-specific rate filings are public anywhere. Do not cite any of these as containing what it is believed to contain without opening it.

## Sources

- [California Department of Insurance (live)](https://www.insurance.ca.gov/)
- [DOI Virtual Viewing Room — rate filings and examination reports (live)](https://www.insurance.ca.gov/01-consumers/135-viewing-room)
- [DOI Virtual Viewing Room, alternate path (live)](https://www.insurance.ca.gov/0250-insurers/0800-rate-filings/0050-viewing-room/index.cfm)
- [DOI Rate Filing Approval Lists index (live)](https://www.insurance.ca.gov/0250-insurers/0800-rate-filings/0100-rate-filing-lists/rate-filing-approvals/index.cfm)
- [DOI Approval Closed List YTD 9-30-26, XLSX (verified live, downloaded and parsed)](https://www.insurance.ca.gov/0250-insurers/0800-rate-filings/0100-rate-filing-lists/rate-filing-approvals/upload/Approval-Closed-List-YTD-9-30-26.xlsx)
- [DOI Rate Filings home](https://www.insurance.ca.gov/0250-insurers/0800-rate-filings/)
- [DOI Dental Medical Loss Ratio reports index (live)](https://www.insurance.ca.gov/01-consumers/110-health/60-resources/10-dmlr/Index.cfm)
- [Blue Shield of CA 2021 Dental MLR Report, XLSX (verified live)](https://www.insurance.ca.gov/01-consumers/110-health/60-resources/10-dmlr/2021/upload/Blue-Shield-of-CA-Life-Health-Insurance-Company-2021-Dental-MLR-Report.xlsx)
- [DOI License Status Inquiry (live)](https://www.insurance.ca.gov/0200-industry/0008-check-license-status/)
- [DOI Health Insurance Information (live)](https://www.insurance.ca.gov/01-consumers/110-health/)
- [DOI HMO/PPO carrier list for consumers (live)](https://www.insurance.ca.gov/01-consumers/110-health/20-look/hcpcarriers.cfm)
- [DOI Health Insurance Covered Lives Report (live)](https://www.insurance.ca.gov/01-consumers/110-health/coveredlivesrpt.cfm)
- [DOI Health Insurance Mergers (live)](https://www.insurance.ca.gov/01-consumers/110-health/60-resources/Health-Insurance-Mergers.cfm)
- [DOI Data & Reports (live)](https://www.insurance.ca.gov/0250-insurers/0600-data-reports/)
- [DOI Statistical Plans (live)](https://www.insurance.ca.gov/0400-news/0200-studies-reports/1100-statistical-plans/index.cfm)
- [DOI sitemap (live)](https://www.insurance.ca.gov/sitemap.xml)
- [California DMHC — HTTP 403, blocked from this environment](https://dmhc.ca.gov/)
- [NAIC Content — HTTP 403, blocked from this environment](https://content.naic.org/)