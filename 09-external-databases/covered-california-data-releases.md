# Covered California Data Releases (Enrollment, Member Profiles, Reports)

- **Retrieved:** 2026-10-13
- **Type:** External database / data source guide

## Summary

Covered California — unlike coveredca.com, its consumer-facing marketing site — maintains a separate research portal at `hbex.coveredca.com` that publishes the agency's own enrollment data: a monthly effectuated-enrollment dashboard, quarterly "Active Member Profile" Excel workbooks with enrollment crosstabbed by carrier, county, ZIP code, legislative district and metal tier, plan quality performance reports, and audited financial statements. The single most useful artifact is the quarterly Active Member Profile workbook, whose `QHP` sheet is the only public source anywhere that breaks California enrollment down **by health plan**, and whose `Zipcode` sheet is the only public source that breaks it down **by ZIP code**.

## Key Facts

| Attribute | Detail |
| --- | --- |
| Publisher | Covered California (California Health Benefit Exchange), State of California |
| Main URL | https://hbex.coveredca.com/data-research/ |
| Enrollment dashboard | https://hbex.coveredca.com/data-research/dashboards/membership-dashboard/ |
| Open-enrollment dashboard | https://hbex.coveredca.com/data-research/dashboards/open-enrollment-and-renewal-dashboard/ |
| Press releases | https://www.coveredca.com/press-releases (redirects from `/newsroom/`) |
| Access | Free, no registration. Tableau dashboards require an embedded JWT token fetched from `https://hbex-fth3bjb0gga4f9h4.a02.azurefd.net/api/tableau_token_endpoint`; **PDF exports work without the Tableau app** |
| Coverage | Individual-market Covered California enrollees; statewide, by region, county, ZIP, legislative district, QHP, product, and month |
| Current as of | Monthly dashboard through September 2026 (PDF, verified live). Quarterly Active Member Profile through December 2023 (series appears discontinued) |
| Update cadence | Enrollment dashboard: monthly. Active Member Profile: quarterly (ended Q4 2023). Financial reports: quarterly + annual |
| Machine-readable | Excel (.xlsx) for member profiles; PDF + Tableau for dashboards; PDF/XLSX for reports. **No CSV or JSON endpoint and no public API.** |
| Volume | Active Member Profile workbook ≈ 2.1 MB, 12 worksheets. Membership Dashboard PDF ≈ 312 KB |

## What it contains

### Monthly Membership Dashboard (freshest enrollment data)

https://hbex.coveredca.com/data-research/dashboards/membership-dashboard/

Page text, verbatim: *"The Membership Dashboard reports monthly counts of consumers enrolled in a Covered California health plan since 2019. Effectuated enrollments include consumers who have paid their first month's premium following plan selection; this is also referred to as 'active health coverage'. Data is refreshed monthly and includes counts of effectuated consumers as of the date of publication."*

Also verbatim, and directly relevant to 2026 analysis: *"Following the expiration of federal enhanced premium tax credits (ePTCs) at the end of the 2025 plan year, 2026 data will track changes in new effectuations and terminations as the year progresses. Termination rates throughout 2026 may increase compared to prior years... Termination data may take up to three months to fully settle as carrier transactions are processed, so data will be refreshed monthly with new months added after a three-month settling period."*

- Live PDF (verified 200, 311,826 bytes): https://hbex.coveredca.com/data-research/dashboards/Public-Membership-Dashboard-September-2026.pdf
- July 2026 also verified live: https://hbex.coveredca.com/data-research/dashboards/Public-Membership-Dashboard-July-2026.pdf (317,500 bytes)
- August 2026 and October 2026 tested → **404** at this naming pattern
- Tableau view backing the dashboard: `https://10ay.online.tableau.com/t/cca_eqt/views/publicmembershipdashboardSeptember2026/Summary`
- Contact published by the agency: externalaffairs@covered.ca.gov

### Active Member Profile (the carrier-level and ZIP-level file)

Library index: https://hbex.coveredca.com/data-research/ (section "Active Member Profiles")
Base path for files: `https://hbex.coveredca.com/data-research/library/active-member-profiles/`

Verified-live files (200 OK):

| Coverage month | File | Size |
| --- | --- | --- |
| December 2023 | `CC_Membership_Profile_2023_12_R20240315.xlsx` | 2,113,217 bytes |
| September 2023 | `CC_Membership_Profile_2023_09_R20231229.xlsx` | 2,115,046 bytes |
| June 2023 | `CC_Membership_Profile_2023_06_R20230922_Rev1.xlsx` | 2,048,869 bytes |
| December 2022 | `CC_Membership_Profile_2022_12_R20230330_Rev1.xlsx` | 2,226,166 bytes |

Older quarters (2014 Q2 through 2023 Q1) also exist under a different subpath, `https://hbex.coveredca.com/data-research/library/`, using names such as `CC_Membership_Profile_2023_03_R20230619%20-%20Copy3.xlsx` and `CC_Membership_Profile_2021_12_R20220328.xlsx`. Note the subpath moved at some point in 2023 — files under `/library/` and files under `/library/active-member-profiles/` are both linked from the same index page.

**Workbook worksheets (12, verified by opening the file):** `Statewide`, `Statewide-Financial`, `Statewide CrossTabs`, `Region`, `QHP`, `County`, `Product by Region`, `Zipcode`, `Legislative District`, `Dental`, `Product by Region Dental`, `Monthly`.

Header text, verbatim: *"Coverage Month: December 2023 | Geography: Statewide by Qualified Health Plan | Data as of: 3/1/2024"*. Also verbatim: *"The report reflects data as of 3/1/2024. There may be data lags and on-going reconciliations between Covered California and health plans. All cells rounded to nearest 10 consistent with privacy policy and as a result, grand totals shown may differ slightly from individual totals due to rounding."* And: *"As of 2022, California provides a $1 per member per month premium to all enrollees in Qualified Health Plans. As a result, this report counts as 'Unsubsidized' enrollees who have only received the State Premium Credit, and do not receive any Federal APTC or California state subsidies."*

**The `QHP` sheet** crosstabs enrollment by carrier for every demographic and financial breakdown. Verified carrier column headers (12): Aetna Health CVS; Anthem Blue Cross of California; Blue Shield of California; Chinese Community Health Plan; Health Net; Kaiser Permanente; L.A. Care Health Plan; Molina Healthcare; Oscar Health Plan of California; Sharp Health Plan; Valley Health Plan; Western Health Advantage; plus TOTAL.

Verified sample row from the "Net Premium Brackets by Qualified Health Plan" block — enrollees in the `$0` net premium bracket, December 2023: Aetna 910; Anthem Blue Cross of California 71,670; Blue Shield of California 68,700; Chinese Community Health Plan 980; Health Net 9,240; Kaiser Permanente 102,000; L.A. Care Health Plan 55,640; Molina Healthcare 24,740; Oscar Health Plan of California 880; Sharp Health Plan 1,160; Valley Health Plan 8,660; Western Health Advantage 1,930; **TOTAL 346,510**. The same block shows the `$100–$250` bracket totalling 372,700 — i.e. more than a third of December 2023 enrollees paid between $101 and $250 per month in net premium.

Verified metal-level crosstab (December 2023 statewide, from the same sheet), showing among other rows `Silver` 240 enrollees, `Silver - Enhanced 73` 110, `Silver - Enhanced 87` 320, `Silver - Enhanced 94` 570, `Gold` 230, `Platinum` 60, with a `Grand Total` row of 1,647,680 on the corresponding table.

**The `Zipcode` sheet** has a two-column table `Zipcode | Enrollees`. Verified rows: 90001 = 1,020; 90002 = 850; 90003 = 1,110; 90004 = 3,170; 90005 = 1,940; 90006 = 2,200; 90007 = 690; 90008 = 970; 90009 = 20; 90010 = 440; 90011 = 1,690; 90012 = 1,410; 90013 = 610; 90014 = 460; 90015 = 1,050. Footnote, verbatim: *"Zip codes that cannot be designated for certain enrollees or exist outside of California are excluded."*

### Other report series on the portal

- **Open Enrollment and Renewal Dashboard** — https://hbex.coveredca.com/data-research/dashboards/open-enrollment-and-renewal-dashboard/. Tableau view `OEDashboardFORPUBLISHING/EnrollmentSummary`. The PDF link on that page (`https://hbex.coveredca.com/data-research/dashboards/oe_dashboard.pdf`) is **currently broken (HTTP 404, "The specified blob does not exist")** on the agency's own live page. The methodology PDF at the same path is live: `https://hbex.coveredca.com/data-research/dashboards/dashboard-methodology.pdf` (200, 132,483 bytes).
- **Health Plan Performance Report** — https://hbex.coveredca.com/data-research/plan-performance-reports/ (page live; sections "Plan Performance Report Resources" and "Archives"). This is the quality/compliance scorecard for participating carriers.
- **Financial Reports** — https://hbex.coveredca.com/financial-reports/. Audited financial statements, quarterly reports, budget reports, and Form 801 payment-to-agency reports from 2014 onward. Verified live example: `https://hbex.coveredca.com/financial-reports/PDFs/2020/fy-2020-21-annual-report-final.pdf`.
- **Ombuds Annual Reports** — https://hbex.coveredca.com/ombuds-annual-reports/. Verified live: `https://hbex.coveredca.com/pdfs/Ombuds-Report-FY24-25-Final.pdf` (200, 627,203 bytes), plus FY19-20 through FY24-25.
- **Legislative Reports / Medical Transitioner Profiles / Actuarial and Proposition 22 studies** — linked from the Data & Research index, e.g. `https://hbex.coveredca.com/data-research/Final Release - Proposition 22 Average Bronze Premium 2024_20230830.pdf` and `https://hbex.coveredca.com/data-research/Final Release - Individual Shared Responsibility Penalty 2024_20230831.pdf`.

## What it does NOT contain

1. **No 2027 plan-year data of any kind.** Nothing on this portal is prospective. The most recent enrollment figure is effectuated enrollment through September 2026; the most recent member-profile file is December 2023.
2. **No plan-level detail.** The `QHP` sheet is by *health plan* (carrier), not by individual plan design. It cannot tell you how many members a specific Bronze HMO has versus a Silver PPO from the same carrier, except indirectly through the metal-level crosstab within each carrier's column.
3. **No premiums.** Covered California publishes *net premium brackets* (e.g. "$100 and less than or equal to $250") for enrolled members, not the filed gross premiums by age, rating area and tier. For actual premium amounts you must use the CMS SBE QHP PUF.
4. **No ZIP-to-carrier matrix.** The `Zipcode` sheet gives total enrollees per ZIP only. There is no published crosstab of carrier × ZIP enrollment.
5. **The Active Member Profile series appears to have stopped after December 2023.** `CC_Membership_Profile_2024_03_R20240614.xlsx` returns 404, and no 2024 or later file is linked from the index. The agency appears to have shifted to the monthly Tableau Membership Dashboard. Treat the quarterly series as discontinued, not merely delayed.
6. **Privacy suppression.** All cells are rounded to the nearest 10 for cells below the disclosure threshold, so small carriers (Oscar at 880 in one bracket, Western Health Advantage at 1,930) cannot be analysed precisely, and row sums will not reconcile exactly.
7. **Not a substitute for rate filings.** Individual-market rate and form filings with Covered California are not published here as "Actuarial Rate Justification" reports. I found no public ARJR series for the California individual market on this portal during this pass — see Status and caveats.
8. **`data.coveredca.gov` does not exist.** DNS resolution fails (curl exit with HTTP code 000). There is no separate Covered California open-data portal.

## Questions it can answer that coveredca.com cannot

1. How many Covered California enrollees does each of the 12 participating carriers have, broken out by age, income, race/ethnicity, language, and region? (December 2023 and earlier, from the `QHP` sheet.)
2. How is net premium distributed across carriers — what share of each carrier's members pay $0 versus $100–$250 per month? (From the "Net Premium Brackets by Qualified Health Plan" block.)
3. How many Covered California enrollees live in each California ZIP code? (From the `Zipcode` sheet; the only public ZIP-level enrollment source.)
4. How many Covered California enrollees live in each county, region, and state legislative district? (From the `County`, `Region`, and `Legislative District` sheets.)
5. How many Covered California members are in each metal tier, and how do enhanced Silver variants (`Silver - Enhanced 73/87/94`) distribute across carriers?
6. How did effectuated enrollment and terminations change month to month through the first year after the federal enhanced premium tax credits expired at the end of 2025? (From the monthly Membership Dashboard, which the agency explicitly warns will show elevated 2026 terminations.)
7. How many Dental-only members does each carrier have? (From the `Dental` and `Product by Region Dental` sheets.)
8. What is Covered California the agency's own audited financial position, quarterly cash flow, and payments to the agency under Form 801? (From the Financial Reports section.)

## How to use it

**Step 1 — get the current monthly enrollment number.** Open https://hbex.coveredca.com/data-research/dashboards/membership-dashboard/ and follow the "For a PDF version of this dashboard, please click here" link. As of 2026-10-13 that resolves to:

```
https://hbex.coveredca.com/data-research/dashboards/Public-Membership-Dashboard-September-2026.pdf
```

The URL pattern is `Public-Membership-Dashboard-{Month}-{Year}.pdf`. If a month returns 404, either the month is not yet published or, more likely per the agency's own note, the data has not finished its three-month settling period.

**Step 2 — get carrier-level enrollment history.**

```powershell
$u = 'https://hbex.coveredca.com/data-research/library/active-member-profiles/CC_Membership_Profile_2023_12_R20240315.xlsx'
curl.exe -L -o "$env:TEMP\cc_active_member_profile.xlsx" $u
```

Open in Excel/LibreOffice and read the `QHP` worksheet. Carrier names run across row headers of each crosstab block; the `Statewide` worksheet has the same breakdowns without the carrier split.

**Step 3 — get ZIP-level enrollment.**

Same workbook, `Zipcode` worksheet: two columns, `Zipcode` and `Enrollees`. Join to a ZIP-to-county crosswalk to attribute these counts geographically.

**Step 4 — use the Tableau dashboards interactively (optional).** The dashboards are Tableau views hosted at `10ay.online.tableau.com`. The page fetches a JWT from `https://hbex-fth3bjb0gga4f9h4.a02.azurefd.net/api/tableau_token_endpoint` and passes it to the embed. For automated extraction prefer the PDF export, which needs no token.

## Status and caveats

**Verified live on 2026-10-13:** `https://hbex.coveredca.com/data-research/`; `.../dashboards/membership-dashboard/`; `.../dashboards/open-enrollment-and-renewal-dashboard/`; `.../plan-performance-reports/`; `https://hbex.coveredca.com/financial-reports/`; `https://hbex.coveredca.com/ombuds-annual-reports/`; the September 2026 and July 2026 Membership Dashboard PDFs; the four Active Member Profile workbooks listed above; `dashboard-methodology.pdf`; `Ombuds-Report-FY24-25-Final.pdf`.

**Confirmed broken on 2026-10-13:**
- `https://hbex.coveredca.com/data-research/dashboards/oe_dashboard.pdf` → HTTP 404 ("The specified blob does not exist"). This is the PDF link published on the agency's own live Open Enrollment and Renewal Dashboard page, so the dead link is a CMS-side asset problem, not a mistyped URL by the reader.
- `https://www.coveredca.com/about/covered-california-data/` → 404.
- `https://www.coveredca.com/newsroom/library/` → 404.
- `https://www.coveredca.com/newsroom/` → **308 redirect** to `https://www.coveredca.com/press-releases`. Always follow redirects; many old Covered California citations point at `/newsroom/`.
- `https://www.coveredca.com/about/` → **308 redirect** to `https://www.coveredca.com/about-covered-california`.
- `https://data.coveredca.gov/` → **does not resolve** (no such host). Do not cite this domain.

**Staleness:** the quarterly member-profile series is two-plus years stale (last coverage month December 2023, last revised 2024-03-15). The monthly dashboard is current. If you need carrier-level enrollment for 2026, the Monthly Membership Dashboard is the only current Covered California source and you must accept its aggregate (non-carrier) granularity, or table a public-records request to externalaffairs@covered.ca.gov.

**Licensing/terms:** no registration, no API key, no stated redistribution restriction on the public reports. Membership data is suppressed to the nearest 10 for privacy; do not attempt to reverse-engineer suppressed cells.

**Unverified:** the file listing behind the Health Plan Performance Report "Resources" and "Archives" sections was not enumerated (the page's links are rendered in a way my HTML fetch did not expose). Treat the existence of plan-level quality scorecards as likely but not confirmed in this pass. Likewise, I did not locate any public "Actuarial Rate Justification" report series for the California individual market on this portal; if one exists it is probably restricted to certified agents.

## Sources

- [Covered California Data & Research portal (live)](https://hbex.coveredca.com/data-research/)
- [Covered California Membership Dashboard (monthly effectuated enrollment)](https://hbex.coveredca.com/data-research/dashboards/membership-dashboard/)
- [Public Membership Dashboard, September 2026 (PDF, verified live)](https://hbex.coveredca.com/data-research/dashboards/Public-Membership-Dashboard-September-2026.pdf)
- [Public Membership Dashboard, July 2026 (PDF, verified live)](https://hbex.coveredca.com/data-research/dashboards/Public-Membership-Dashboard-July-2026.pdf)
- [Open Enrollment and Renewal Dashboard](https://hbex.coveredca.com/data-research/dashboards/open-enrollment-and-renewal-dashboard/)
- [Dashboard Methodology (PDF, verified live)](https://hbex.coveredca.com/data-research/dashboards/dashboard-methodology.pdf)
- [Open Enrollment Dashboard PDF — linked from the live page but 404](https://hbex.coveredca.com/data-research/dashboards/oe_dashboard.pdf)
- [Health Plan Performance Report](https://hbex.coveredca.com/data-research/plan-performance-reports/)
- [Covered California Financial Reports](https://hbex.coveredca.com/financial-reports/)
- [Covered California Ombuds Annual Reports](https://hbex.coveredca.com/ombuds-annual-reports/)
- [Active Member Profile, December 2023 (XLSX, verified live, parsed)](https://hbex.coveredca.com/data-research/library/active-member-profiles/CC_Membership_Profile_2023_12_R20240315.xlsx)
- [Active Member Profile, September 2023 (XLSX, verified live)](https://hbex.coveredca.com/data-research/library/active-member-profiles/CC_Membership_Profile_2023_09_R20231229.xlsx)
- [Active Member Profile, June 2023 (XLSX, verified live)](https://hbex.coveredca.com/data-research/library/active-member-profiles/CC_Membership_Profile_2023_06_R20230922_Rev1.xlsx)
- [Active Member Profile, December 2022 (XLSX, verified live)](https://hbex.coveredca.com/data-research/library/active-member-profiles/CC_Membership_Profile_2022_12_R20230330_Rev1.xlsx)
- [Covered California press releases (target of the /newsroom/ redirect)](https://www.coveredca.com/press-releases)
- [Proposition 22 Average Bronze Premium study, 2024 (PDF)](https://hbex.coveredca.com/data-research/Final%20Release%20-%20Proposition%2022%20Average%20Bronze%20Premium%2024_20230830.pdf)