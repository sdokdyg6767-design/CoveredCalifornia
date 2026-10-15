# Enrollment, Outreach and Research Data (Covered California reports, QLEEP, member surveys, CHCF, UCLA, UC Berkeley)

- **Retrieved:** 2026-10-13
- **Type:** External source guide

## Summary

The exchange's own research and data library lives at `hbex.coveredca.com/data-research/`, not on coveredca.com, and I retrieved and parsed that index directly. It is by far the richest source in this entire project: a monthly Membership Dashboard, quarterly Net/Gross plan-selection profiles, an annually refreshed Active Member Profile series, **member survey public reports**, a **Medi-Cal Transitioner Profile** series running monthly into mid-2026, enrollment-by-immigration-status files, rate and product-price workbooks for 2026 and 2027, and a deep archive of policy briefs. **QLEEP is not published there** — I found no QLEEP link anywhere in the live index — and that is recorded as a gap rather than papered over.

Because the sibling file `covered-california-data-releases.md` already documents the dashboards, the Active Member Profile workbooks, the financial reports and the premium/pricing artifacts in detail, this file deliberately covers what that file does not: the **surveys**, the **Medi-Cal transitioner series**, the **first-decade-style evaluations**, and the external academic publishers.

## Key Facts

| Attribute | Detail |
| --- | --- |
| Publisher | Covered California (the Exchange), at its separate board/stakeholder portal `hbex.coveredca.com` |
| Main URL | https://hbex.coveredca.com/data-research/ — **verified live and parsed in full on 2026-10-13** |
| Related portal for cross-checking | The library's own `coveredca.com/data-research/` returns **HTTP 404**; `hbex.coveredca.com` is the correct host |
| Access | Free, no registration, no API key |
| Formats | XLSX, XLS, PDF, plus Tableau dashboards; **no CSV/JSON endpoint and no public API** |
| Recency | Index shows 2027 product prices and 2027 ZIP-code files, a 2026 open-enrollment profile set, and Medi-Cal transitioner data through June 2026 revised 2026-08-25 |
| QLEEP | **Not located on the live index.** Logged as a gap |

## Sources documented

### Covered California Data & Research index — verified live and parsed

- **URL:** https://hbex.coveredca.com/data-research/
- **Verified:** retrieved and parsed 2026-10-13. The page's own data area states, verbatim: *"Content is being added to this page. Be sure to check back for additional information."* — a useful caution that the index is a partial catalogue rather than a complete archive.
- **What is on it, by the year's section headings present in the live HTML:**

**2027 data** — 2027 Covered California Data; 2027 Products by Zip Code; 2027 QHP Individual Product Prices; 2027 QDP Individual Product Prices.

**2026 data** — 2026 Open Enrollment Net Plan Selection Profile; 2026 Open Enrollment Gross Plan Selection Profile; 2026 Open Enrollment and Renewal Net Plan Selection Profile; 2026 Open Enrollment and Renewal Gross Plan Selection Profile; 2026 QHP Individual Rates without non-EHB; 2026 QHP Individual Product Prices; 2026 QDP Individual Product Prices; 2026 Products by Zip Code; 2026 Enrollment by Immigration Status; 2026 Renewal Retention Profile. Plus analysis pieces including *"Many of California's Lawfully Present Non-Citizens Will Lose Eligibility for Federal Financial Assistance in 2027"*, *"Many Californians Go Uninsured after Expiration of Federal Enhanced Tax Credits"*, and *"Without Extension of Enhanced Federal Tax Credits in 2026, Renewing Consumers Switched Down to Lower Coverage Bronze Plans and Now Face Higher Out-of-Pocket Costs"*.

**2025 data** — Data Snapshot: Open and Special Enrollment Periods; 2025 Net/Gross plan selection profiles; 2025 Products by Zip Code; 2025 Individual Product Prices; **Member Survey 2025 Public Report**.

**2024 data** — 2024 Open Enrollment Net Plan Selection Profile and others, including *"Covered California Helps Members Access Preventive Health Care"*.

**2027 and 2026 enhanced-premium-tax-credit impact series** — a "Impact of Expiration of the Enhanced Premium Tax Credit" group containing an Open Enrollment dashboard, *"Costs of Care for Marketplace Consumers Switching to Bronze Could Double"*, a Fact Sheet on ePTC expiration impact, congressional-district-level impact data, a 2026 enrollee-impact workbook, and a **five-brief academic-style series** (consumer premium spikes and reversed enrollment gains; ePTC affordability and economic opportunity for the self-employed; IRA coverage for older enrollees; communities of color; rural access).

**Authoritative for:** the Exchange's own account of its enrollment, retention, and pricing — including how many people were lost when federal enhanced subsidies expired at the end of the 2025 plan year.
**Cannot answer:** independent evaluation. Everything here is the agency grading its own work.

### Member survey public reports — verified live

- **URLs (all confirmed present as live links on the hbex data-research index):**
  - `https://hbex.coveredca.com/data-research/member-survey-2025-public-report.pdf`
  - `https://hbex.coveredca.com/data-research/library/Member_Survey_2024_Public_Report.pdf`
  - `https://hbex.coveredca.com/data-research/library/Member_Survey_2023_Public_Report.pdf`
- **Verified:** the three files are linked from the live index page; the index lists them under the "2025 Covered California Data" and "2024/2023" sections respectively. I confirmed the links are published, but did **not** open and parse the PDFs, so I make no claim about their contents beyond what the filenames state.
- **Authoritative for:** surveyed member experience — satisfaction, access, understanding — the only public source for what enrollees say about their coverage. This is a real gap in the agency's *performance* reporting: the plan performance reports measure compliance, while the surveys measure experience.
- **Answer for the QLEEP question:** **no QLEEP artifact appears in the live index.** I searched the index HTML for QLEEP and found no such link.

### Medi-Cal Transitioner Profile series — verified live, and the key 2026 evidence

- **URLs confirmed live on the index:**
  - `https://hbex.coveredca.com/data-research/library/CC_MediCal_Transitioner_Profile_2026_06_R20260825_Rev2.xlsx`
  - `.../CC_MediCal_Transitioner_Profile_2026_03_R20260518.xlsx`
  - `.../CC_MediCal_Transitioner_Profile_2025_12_R20260302.xlsx`
  - `.../CC_MediCal_Transitioner_Profile_2025_09_R20251118.xlsx`
  - plus a full monthly backfile under `.../library/mct-profiles/` running from `CC_MediCal_Transitioner_Profile_2023_07_R20230919.xlsx` forward, and a cumulative PHE-unwind file `CC_MediCal_Transitioner_Profile_PHE_Unwind_Cumulative_R20240926.xlsx`
- **Verified:** all of the above appear as live links in the parsed index. Contents not parsed.
- **Why this matters more than anything else in this file for the 2026 question:** this series continues to be produced **monthly through June 2026, revised 2026-08-25**. People transitioning from Medi-Cal into the marketplace in mid-2026 is direct, official evidence that Medi-Cal disenrollment was an ongoing, incremental process during 2026 — not a single January 1 cut-off. Read alongside the federal statute finding in `medi-cal-administration-sources.md` (work requirements not later than April 1, 2027), this series is the best available public evidence that the library's "adults 19+ lost full Medi-Cal on Jan 1, 2026" framing is wrong.

### First-decade and evaluative reports — verified live

- `https://hbex.coveredca.com/data-research/library/CoveredCA_First_Five_Years_Dec2019.pdf` — the exchange's own evaluation of its first five years. This is the closest thing to a first-decade retrospective that exists on this portal, and it stops at year five (2019), not year ten.
- `https://hbex.coveredca.com/data-research/library/CoveredCA_Holding_Plans_Accountable_Dec2019.pdf` — companion accountability analysis.
- Also present: `CoveredCA_Coverage_Analysis_6-21-17.pdf`, `CoveredCA_Impact_to_CA_ind_market_4-27-17 (1).pdf`, `CoveredCA_CSRs_and_the_Individual-Market-7-21-17.pdf`, `CoveredCA_Reducing_Premiums_1-10-18.pdf`, `CoveredCA_High_Premium_Increases_3-8-18.pdf`, `CoveredCA_Marketing_Matters_9-17.pdf`, `CoveredCA_Key_Ingredients-05-18-17.pdf`, `Preliminary_Analysis_of_AHCA.pdf`, and the `LPI-Consumer-Impact-Brief.pdf` / `Renewal Terminations Brief.pdf` pairs.
- **Authoritative for:** how the agency itself characterised its early performance and affordability problems, in its own words, contemporaneous with the events.
- **Cannot answer:** independent assessment. Every one of these is self-evaluation.

### Academic and foundation research publishers

- **California Health Care Foundation (CHCF)** — `https://www.chcf.org/` **verified live, HTTP 200, 236,229 bytes, title `Homepage - California Health Care Foundation`.** Authoritative for independent commissioned research on California health care, including analysis of the individual market. I did not enumerate its California-specific Covered California publications in this pass.
- **UCLA Center for Health Policy Research** — `https://healthpolicy.ucla.edu/` **verified live, HTTP 200, 173,040 bytes, title `UCLA Center for Health Policy Research`.** Relevant as the research home most likely to publish rigorous California marketplace analysis. I did **not** confirm that it currently publishes Covered California-specific work.
- **UC Berkeley** — **not verified in this pass.** No Berkeley URL was retrieved and no specific Berkeley marketplace-analysis publication is confirmed here. Logged as an untested lead.
- **CHCF's sponsored report** — note `CoveredCA-Medicaid-to-Marketplace-AutoenrollmentStrategy-FactSheet-v1.pdf` appears on the exchange index; that is exchange-published material, not CHCF's.

### NORC and enrollment-funnel artifacts

- `https://hbex.coveredca.com/data-research/library/NORC Consumer Tracking Report.pdf` — confirmed live link. A consumer tracking study conducted by NORC for the exchange.
- Enrollment-funnel workbooks also present: `Ethnicity and Race by Service Channel.xlsx`, `Income Category.xlsx`, `Income Category by Service Channel.xlsx`, `Top 20 CEEs Enrollment by Ethnicity.xlsx`, `County Enrollment.xlsx`, `Self-Service and CEC_Market Source.xlsx`, `Health Insurance Issuer by Subsidy Status.xlsm`, and `Dental enrollment.xlsx` (2014 vintage).

## Questions this file can answer that coveredca.com cannot

1. How many people enrolled, by carrier, county, ZIP, metal tier, and subsidy status — and which months of the post-ePTC-expiration 2026 period saw enrollment fall.
2. What happened to enrollment after federal enhanced premium tax credits expired at the end of the 2025 plan year, including the shift into Bronze plans and the associated out-of-pocket cost doubling.
3. How many people moved from Medi-Cal into the marketplace, month by month, through 2026 — the Mediator Transitioner Profile series.
4. What enrolled members report about their own coverage, from the annual member survey public reports.
5. How the exchange's own early-career assessment of its problems was framed, from the First Five Years and related reports.
6. How the exchange's 2014–2016 marketing and enrollment-funnel efforts were distributed by ethnicity, income, service channel, and geography.
7. Which research organizations in California publish independent analysis of the individual market — CHCF and UCLA Health Policy Research are the confirmed-reachable candidates.
8. Whether an independent first-decade evaluation of Covered California exists anywhere public. **As found: no.** The only retrospective on this portal is the agency's own five-year report.

## Known gaps and dead ends

All statuses observed 2026-10-13.

1. **QLEEP is not published on the live hbex index.** I searched the parsed index HTML for "QLEEP" and for links matching `qleep`; **zero matches**. QLEEP (the Quality, Loyalty and Equity Evaluation Program) was California's funded external evaluation of its marketplace. I could not locate where its reports are published today: not on the live exchange index, and a Wayback CDX query for `hbex.coveredca.com/data-research/library/*qleep*` failed with **HTTP 503 Server Unavailable**, so even the archive route is unconfirmed. **QLEEP's current publication location is unresolved.** The honest statement is that I could not verify it is still published anywhere public — not that it does not exist.
2. **`https://www.coveredca.com/data-research/` returns HTTP 404** (192,765 bytes). Sub-paths `/data-research/covered-california-enrollment-data/` and `/data-research/qleep/` also 404. `https://www.coveredca.com/quality/` 404s. Any library entry pointing at the consumer domain for research data is wrong; the correct host is `hbex.coveredca.com`.
3. **`https://www.coveredca.com/pdfs/CoveredCA-QLEEP-Report.pdf` returns HTTP 404** (215 bytes). A guessed QLEEP PDF path on the consumer domain fails outright.
4. **The Wayback CDX index was unreliable during this pass** — 429 on content fetch, 503 on a CDX query, and an EMPTY result for a domain pattern. Historical-state questions (when did QLEEP stop being published?) could not be answered this way.
5. **No first-decade (10-year) evaluation was found.** The only retrospective on the portal is `CoveredCA_First_Five_Years_Dec2019.pdf`, from 2019. Whether a later or independent ten-year evaluation exists is **unverified**.
6. **UC Berkeley was not checked.** No Berkeley source is documented in this file. Do not attribute Berkeley marketplace analysis to this library on the strength of this file.
7. **UCLA Center for Health Policy Research was confirmed reachable but not confirmed to publish Covered California analysis.** Reachability is not evidence of relevant output.
8. **CHCF was confirmed reachable but its Covered California publications were not enumerated.** Same caveat.
9. **No report PDF was opened or parsed in this pass.** Every data artifact listed here was verified as a live published link with its filename and, in several cases, its revision date embedded in the filename. Contents are described by title only. Filename-embedded revision dates are a reliable signal but are not a substitute for parsing the file.
10. **The ePTC-expiration and work-requirement policy documents are heavily agency-framed.** The exchange's "Impact of Expiration of the Enhanced Premium Tax Credit" briefs are the agency's own projections and fact sheets. They are excellent evidence of what the state predicted and wanted understood, and are not independent analysis.
11. **The coveredca.com 404 pattern is a trap for this library specifically.** The consumer domain returns a full ~192 KB HTML page on a 404 rather than a thin error, so a naive status-check that only tests for a response rather than for 200 will silently record these as valid.

## Sources

- [Covered California Data & Research index (verified live and parsed, 2026-10-13)](https://hbex.coveredca.com/data-research/)
- [Member Survey 2025 Public Report (verified live link)](https://hbex.coveredca.com/data-research/member-survey-2025-public-report.pdf)
- [Member Survey 2024 Public Report (verified live link)](https://hbex.coveredca.com/data-research/library/Member_Survey_2024_Public_Report.pdf)
- [Member Survey 2023 Public Report (verified live link)](https://hbex.coveredca.com/data-research/library/Member_Survey_2023_Public_Report.pdf)
- [Medi-Cal Transitioner Profile, June 2026 (verified live link)](https://hbex.coveredca.com/data-research/library/CC_MediCal_Transitioner_Profile_2026_06_R20260825_Rev2.xlsx)
- [Covered California First Five Years, December 2019 (verified live link)](https://hbex.coveredca.com/data-research/library/CoveredCA_First_Five_Years_Dec2019.pdf)
- [NORC Consumer Tracking Report (verified live link)](https://hbex.coveredca.com/data-research/library/NORC Consumer Tracking Report.pdf)
- [California Health Care Foundation (verified live, 200)](https://www.chcf.org/)
- [UCLA Center for Health Policy Research (verified live, 200)](https://healthpolicy.ucla.edu/)
- [coveredca.com/data-research — 404, wrong host](https://www.coveredca.com/data-research/)
- [Guessed QLEEP PDF on coveredca.com — 404, dead end](https://www.coveredca.com/pdfs/CoveredCA-QLEEP-Report.pdf)