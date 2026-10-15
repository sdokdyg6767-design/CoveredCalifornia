# Covered California — Research Library & Index

An organized, offline reference library built from **https://www.coveredca.com/** (the official California health insurance marketplace) plus federal, state, and governance sources that the site itself cites.

- **Compiled:** 2026-10-13
- **Coverage:** 119 English pages from the coveredca.com sitemap (all captured), plus Board of Governors materials, HBEX agent toolkits, and federal litigation/rulemaking primary sources.
- **Contents:** 133 Markdown files across 10 category folders — 118 mirrored source pages, 5 synthesized briefs, 9 external-database guides, and 4 verification audits
- **Audit:** all of folders 01–08 was re-verified against the live site on 2026-10-13. See [Verification status](#-verification-status).
- **Spanish mirror:** intentionally not mirrored. Every English page has a `/es/` counterpart on the live site; the English page is the source of record.

> **Start here if you have 60 seconds:** 2027 open enrollment runs **Nov 1, 2026 – Jan 31, 2027**. Enroll by **Dec 31, 2026** for a Jan 1 start. See [Key Dates](#-key-dates) and `07-news-policy-and-updates/key-dates-calendar.md`.

---

## 🚨 Read this first: the 2026–2027 cliff

The single most important thing on the site right now is a policy rupture that most consumer pages mention only in passing.

| Fact | Detail |
| --- | --- |
| Enhanced federal premium tax credits **expired Dec 31, 2025** | Premiums projected to rise **97% on average** for **1.7M+** Californians |
| **160,000** middle-income consumers lose APTC eligibility entirely | State credits cannot replace **~$2.5 billion/year** in federal aid |
| Remaining federal APTC band | **100% – 400% FPL**, any coverage level |
| Cost-sharing reductions (CSR) | **≤ 250% FPL**, Enhanced Silver plans only |
| California state credit for 2027 | **$300 million** (up from $190M in 2026), up to **200% FPL** = **$31,920** individual / **$66,000** family of four |
| State credit reach | **500,000+** recipients (~30% of enrollees); **200,000** newly eligible; nearly **200,000** can choose two Silver plans at **$0** |
| 2027 average rate change | **+9.9%** weighted average (vs ~14% national median); **60%** see no increase; **26%** keep $0 premiums |

Full detail: `07-news-policy-and-updates/federal-policy-changes-2026-2027.md` and `02-costs-and-financial-help/financial-help.md`.

### The June 12, 2026 court ruling

On **June 12, 2026**, the U.S. District Court for the District of Maryland vacated **eight** provisions of HHS's 2025 Marketplace Integrity and Affordability Rule in *City of Columbus v. Kennedy* (No. 1:25-cv-02114-BAH), under 5 U.S.C. 706 — including the shortened open-enrollment window from 2027, the $5 re-enrollee penalty, and failure-to-reconcile enforcement. The premium adjustment methodology change **survived**, and likely raises out-of-pocket maximums for enrollees under 400% FPL. A second rulemaking followed, effective July 20, 2026 and stayed July 16, 2026.

This matters because several widely-repeated dates ("2027 open enrollment is 45 days") are **wrong for California** — Covered California runs the full Nov 1 – Jan 31 window.

---

## 📁 Folder Map

| # | Folder | Files | What's inside |
| --- | --- | ---: | --- |
| 01 | [coverage-and-plans](01-coverage-and-plans/) | 28 | The four metal tiers with full cost tables, dental, vision, the tax penalty, the glossary, Medi-Cal overview, and all 12 carrier pages |
| 02 | [costs-and-financial-help](02-costs-and-financial-help/) | 6 | APTC, CSR, employer coverage offers, HRAs, and the "important changes" consumer tracker |
| 03 | [enrollment-and-eligibility](03-enrollment-and-eligibility/) | 38 | Individual/family enrollment, eligibility rules, all 9 verification documents, plus a 19-page **small-business/SHOP** subfolder |
| 04 | [account-and-managing-coverage](04-account-and-managing-coverage/) | 14 | Renewals, billing, cancellation, appeals, 1095-A tax forms, preventive care, mental health |
| 05 | [help-support-and-rights](05-help-support-and-rights/) | 8 | Service Center, enroller locator, consumer protection, insurance company complaint contacts, the Ombuds Office |
| 06 | [partners-agents-and-training](06-partners-agents-and-training/) | 15 | Agent and Certified Enroller pathways, CCSB certification, codes of conduct, marketing/branding rules |
| 07 | [news-policy-and-updates](07-news-policy-and-updates/) | 7 | **Not a page mirror** — press releases, federal policy changes, Board reports, agent toolkits, the consumer blog, a dated timeline, and other authoritative sources |
| 08 | [about-and-resources](08-about-and-resources/) | 7 | Governance, language access and accessibility, privacy rights and forms, legal notices, media inquiries |
| 09 | [external-databases](09-external-databases/) | 9 | **New.** Trusted outside databases that coveredca.com does not publish — plan-level data, Medi-Cal administration, state oversight, independent analysis |
| 10 | [verification-audit](10-verification-audit/) | 4 | **New.** Adversarial re-verification of this library's own numbers against the live site |
| — | [_raw](_raw/) | — | Tooling: the site sitemap, the URL inventory, and the page-text extractor (see [Tooling](#-tooling)) |

---

## ✅ Verification status

Every claim in folders 01–08 was re-checked against the live site on 2026-10-13 by an adversarial audit pass that assumed errors existed. Results are in `10-verification-audit/`.

**Headline: the financial and plan numbers are sound.** Across ~37 spot-checked claims covering APTC/CSR thresholds, state credits, all four metal-tier cost tables, tax penalty, Medi-Cal income bands, SHOP rules, appeal and cancellation deadlines, and the 1095-A rules, **zero fabrications were found** and the overwhelming majority confirmed verbatim.

Four errors were found and have been **corrected in place**:

| Was wrong | Now | File |
| --- | --- | --- |
| **SSI and the Child Tax Credit listed as income to "include"** (they are on the page's **"Doesn't Count"** column — a side-by-side table had been merged incorrectly). Could cause real loss of APTC. | Full verified 8-item / 7-item two-column table | `02-costs-and-financial-help/financial-help.md` |
| Platinum page said it prints **no** prescription copay table | It does — Tier 1–4 drug costs added | `01-coverage-and-plans/platinum.md` |
| HCARF expanded as "Affordability and **Responsiveness** Fund" | "Affordability and **Reserve** Fund" | `07-news-policy-and-updates/press-releases.md` |
| "income statements must be dated within 45 days" | The 45-day rule applies to **employer** statements only | `INDEX.md` |

One suspected error was **checked and rejected**: an audit agent recommended striking the "adults 19+ lost full Medi-Cal on Jan 1, 2026" claim as unsupported. Re-fetching the live page confirmed Covered California states it verbatim. The confusion came from conflating that **state** change with the **federal** Medicaid work-requirement in P.L. 119-21 (SEC. 71119), which begins no later than **April 1, 2027**. `03-enrollment-and-eligibility/immigrants.md` now carries an explicit three-date table separating them.

A third round (2026-10-14), prompted by a question about pregnancy, found that **the audit itself had been wrong in the other direction** — and that fixing it exposed a real defect:

- `10-verification-audit/verify-enrollment-and-eligibility.md` claimed the live SEP deadline table has *"thirteen distinct qualifying events."* Re-parsed from raw markup, it has **six** rows. The audit had conflated the deadline table with the separate untimed category card lists.
- Following through on that correction revealed the library had **dropped a whole table row: "Birth, adoption or foster placement."** It had been folded into a catch-all row whose coverage-start rule ("typically starts the first of the month after you choose a plan") **does not apply to a birth**. The source gives births their own rule: "Coverage start options may vary; Covered California will show your date after you apply."
- `03-enrollment-and-eligibility/major-life-changes.md` now reproduces the source's six rows verbatim, and both it and `01-coverage-and-plans/pregnant-individuals.md` warn that a newborn's coverage start date is not guaranteed to follow the first-of-the-month pattern.

Known limits of the audit: independent corroboration outside coveredca.com largely failed from this environment (DMHC, CBO, GAO and several other federal/state sites are bot-blocked — see [Known Gaps](#-known-gaps)). Several high-stakes figures therefore rest on coveredca.com alone.

### Second pass — folder 09 independently re-derived

The external-database claims were re-checked by downloading and parsing the actual data rather than trusting the summary. Results:

| Claim | Result |
| --- | --- |
| `californiasbpuf2026.zip` downloads and is the real California file | **Confirmed** — 0.98 MB, 6 CSVs |
| 1,010 plan rows / 93,840 rate rows / 14 issuer IDs / 6 metal levels | **All confirmed exactly** |
| Per-issuer plan counts (70285 = 524, 67138 = 206, 40513 = 52, …) | **All 14 confirmed exactly** |
| Metal-level counts (Silver 364, Gold 228, Platinum 221, Expanded Bronze 147, High 29, Catastrophic 21) | **All confirmed exactly** |
| 19 `RATING AREA ID` values | **Confirmed** (distinct from the 85 `SERVICE AREA ID` values in the service-area file — a real and easy-to-confuse distinction) |
| Molina Expanded Bronze age-27 premium range $345.36–$400.74 | **Confirmed to the cent**, 6 rating areas |
| 2027 PUF files not yet published | **Confirmed** — `californiasbpuf2027.zip` and `californiasbepuf2027.zip` both 404, 2026 returns 200 |
| Shop & Compare serves 2027 quoting | **Confirmed** — the API returns `"enrollYears":[…,"2026","2027"]` |
| `hbex.coveredca.com/data-research/`, `data.chhs.ca.gov` CKAN API, KFF, Health Consumer Alliance, `auditor.ca.gov` | **All confirmed live (200)** |

Two errors were found and fixed in this pass:

- `cms-marketplace-public-use-files.md` stated plan types as "HMO 857, PPO 151, EPO 19". Those sum to **1,027**, contradicting the verified 1,010 plan rows. Corrected to **HMO 840, PPO 151, EPO 19 = 1,010**.
- `state-regulatory-and-legislative-oversight.md` read Gov Code §11015, correctly found it unrelated to health insurance, then **wrongly generalised that finding to §11015.5** and advised striking the citation. I retrieved §11015.5 verbatim: it is the electronic-personal-information notice statute (amended Stats. 2021, Ch. 615) that Covered California's own Terms of Use cites. **The site is right; the correction was retracted.** `privacy-terms.md` needed no change.

A caution worth carrying forward: **three separate agents independently mistook a California state provision for a federal one, and one mistook an adjacent statute for its neighbour.** Numbered citations and dates in this subject area must be checked against the actor that actually made the change — not inferred from a neighboring law or from the absence of a date in an unrelated one.

---

## 📅 Key Dates

| Date | Event | Source file |
| --- | --- | --- |
| **Nov 1, 2026 – Jan 31, 2027** | 2027 open enrollment period | `03-.../open-enrollment.md` |
| **Oct 2026** | Renewal period opens | `04-.../renew.md` |
| **Dec 31, 2026** | Enroll by this date for **Jan 1, 2027** start | `03-.../open-enrollment.md` |
| Jan 2027 signups | Coverage starts **Feb 1, 2027** | `03-.../open-enrollment.md` |
| Within **30 days** of renewal deadline | Auto-reenrollment processed if no action taken | `04-.../renew.md` |
| **Jan 1, 2027** | Federal financial-help restriction begins (green card, Cuban/Haitian entrants, COFA migrants) | `07-.../federal-policy-changes-2026-2027.md` |
| **Jan 31** | Form 1095-A issued for the prior year | `04-.../tax-forms.md` |
| **Nov 30** | Affordability application cutoff (tax penalty) | `01-.../tax-penalty-details-and-exemptions.md` |
| **90 days** | File an appeal after your decision is mailed | `04-.../file-an-appeal.md` |
| **30 business days** | Covered California complaint response | `04-.../file-an-appeal.md` |
| **60 days** | Standard Special Enrollment Period window | `03-.../major-life-changes.md` |
| **90 days** | SEP after losing Medi-Cal coverage | `03-.../losing-medi-cal-coverage.md` |
| **14 days** | Cancellation notice period | `04-.../cancel.md` |
| **10 days** | Report a change with Medi-Cal (30 days for Covered California) | `01-.../medi-cal.md` |

Full timeline with per-item sources: `07-news-policy-and-updates/key-dates-calendar.md`.

---

## 📄 Complete File Index

Every file is named after its source page's URL path segment and opens with the source URL and the retrieval date.

### 01 — Coverage & Plans (28)

Plan tiers, benefits, Medi-Cal, and carriers.

| File | Page | Notes |
| --- | --- | --- |
| `coverage-basics.md` | Coverage Basics | How the marketplace works |
| `coverage-levels.md` | Coverage Levels | The four metal tiers compared |
| `bronze.md` | Bronze | Standard and HSA-eligible variants; **first 3 non-preventive visits are copay** |
| `silver.md` | Silver | All four variants (70/73/87/94) with full OOP-max and deductible tables |
| `gold.md` | Gold | No deductible; OOP max $9,200/$18,400 |
| `platinum.md` | Platinum | No deductible; OOP max $5,000/$10,000 |
| `minimum-coverage-plan.md` | Minimum Coverage Plan | Under-30 / exempt; **no financial help at all** |
| `dental.md` | Dental | Kids under 19 included; family enrollment rules |
| `vision.md` | Vision | Adult vision is a **separate direct-enrollment** product |
| `tax-penalty-details-and-exemptions.md` | Tax Penalty | $950/adult min; 2026 affordability **8.05%** |
| `ftb-form-3853.md` | FTB Form 3853 | Penalty calculation form (FAQ answers collapsed on source) |
| `glossary.md` | Glossary | Marketplace terminology |
| `medi-cal.md` | Medi-Cal | Adults ≤138% FPL, children ≤266% FPL |
| `children.md` | Medi-Cal for Children | CCHP 266–322% FPL (SF/SM/SC only) |
| `pregnant-individuals.md` | Medi-Cal for Pregnancy | 1 year postpartum |
| `mixed-program-families.md` | Mixed Program Families | Family members on different programs |
| `anthem.md` · `blue-shield.md` · `cchp.md` · `caloptima.md` · `health-net.md` · `iehp.md` · `kaiser-permanente.md` · `la-care.md` · `molina-healthcare.md` · `sharp.md` · `valley-health.md` · `western-health-advantage.md` | 12 carrier pages | These pages **do carry real content**, but it is marketing and enrollment content, not plan data. Each publishes two card groups — carrier-specific guidance for existing members ("If you already have a X Plan") and an application document checklist — plus a benefits list and three enrollment channels. What they do **not** publish anywhere: plan counts, premium figures, metal-tier availability, or county service-region lists. The only carrier-specific *news* item is Molina's **2027 withdrawal from northeast LA and Orange County**. |

### 02 — Costs & Financial Help (6)

| File | Page | Notes |
| --- | --- | --- |
| `costs.md` | Costs | Premium vs. total cost of care framing |
| `financial-help.md` | Financial Help | **The authoritative APTC/CSR/state-subsidy thresholds** |
| `employer-coverage.md` | Employer Coverage | When employer offers beat or end marketplace options |
| `health-reimbursement-arrangements.md` | HRAs | ICHRAs and their effect on eligibility |
| `hra-affordability-calculator.md` | HRA Calculator | Required tool for ICHRA affordability |
| `important-changes.md` | Important Changes | **The consumer-facing "what's different in 2026–2027" tracker** |

### 03 — Enrollment & Eligibility (38)

| File | Page | Notes |
| --- | --- | --- |
| `enrollment.md` | Enrollment | Hub page |
| `open-enrollment.md` | Open Enrollment | Nov 1 – Jan 31; Dec 31 for a Jan 1 start |
| `eligibility.md` | Eligibility | Who qualifies |
| `american-indians-alaska-natives.md` | AI/AN Eligibility | Cost-sharing protections |
| `immigrants.md` | Immigrant Eligibility | **Critical:** adults 19+ lost full Medi-Cal Jan 1, 2026; 2027 federal restriction |
| `people-with-chronic-conditions.md` | Chronic Conditions | Special enrollment eligibility |
| `major-life-changes.md` | Major Life Changes | 60-day SEP |
| `domestic-abuse.md` | Domestic Abuse | SEP coverage for survivors |
| `losing-medi-cal-coverage.md` | Losing Medi-Cal | **90-day** SEP |
| `documents.md` | Required Documents | Verification overview; **send copies only** |
| `doc-citizenship.md` · `doc-immigration-status.md` · `doc-identity.md` · `doc-income.md` · `doc-social-security-number.md` · `doc-not-incarcerated.md` · `doc-american-indian-or-alaskan-native.md` · `doc-minimum-essential-coverage.md` · `doc-notification-of-a-deceased-member.md` | 9 verification documents | One document per request; **employer** statements must be dated **within 45 days** |

**`small-business/` subfolder (19)** — SHOP and the employer mandate.

`small-business.md` · `eligibility.md` · `costs-and-financial-help.md` · `apply.md` · `get-a-quote.md`\* · `health-plans.md` · `blue-shield.md` · `kaiser.md` · `sharp.md` · `western-health-advantage.md` · `dental-plans.md` · `delta-dental.md` · `employee-forms.md` · `employer-forms.md` · `enrollment-support.md`\* · `contact.md` · `mandate.md` · `1095-forms.md` · `resources.md`

Key numbers: **1–100 full-time employees**; employer must contribute **≥50%** of the premium; only **adjacent metal tiers** may be offered (Bronze+Silver yes, Bronze+Gold no); affordability threshold **9.96%** of household income; 1095-C filed for **all** full-time employees; W-2 **Box 12 Code DD**; Additional Medicare Tax **0.9% above $200,000**.

\* Client-rendered pages with no server-side content — see [Known Gaps](#-known-gaps).

### 04 — Account & Managing Coverage (14)

| File | Page | Notes |
| --- | --- | --- |
| `account.md` | Account | Hub |
| `guide-to-your-account.md` | Guide to Your Account | Navigation walkthrough |
| `billing.md` | Billing | Premium payment options. **Publishes no day count** for non-payment termination or a grace period |
| `renew.md` | Renew | October open, auto-reenroll within 30 days |
| `moving-to-medicare.md` | Moving to Medicare | 60-day SEP; 7-month initial window; Part B penalty 10% |
| `cancel.md` | Cancel | **14 days** notice; coverage ends last day of the month; never retroactive |
| `tax-forms.md` | Tax Forms | 1095-A by **Jan 31**; not issued for Medi-Cal/catastrophic/CCSB |
| `file-an-appeal.md` | File an Appeal | **90 days** to file; hearing decision up to 90 days |
| `using-your-plan.md` | Using Your Plan | Hub |
| `enrollee-programs.md` | Enrollee Programs | Optional plan add-ons |
| `free-preventive-care-for-adults.md` | Preventive Care — Adults | In-network, pre-deductible |
| `free-preventive-care-for-children.md` | Preventive Care — Children | |
| `free-preventive-care-for-women.md` | Preventive Care — Women | |
| `mental-health.md` | Mental Health | Behavioral health appointment within **10 business days** |

### 05 — Help, Support & Rights (8)

| File | Page | Notes |
| --- | --- | --- |
| `get-help.md` | Get Help | **Service Center (800) 300-1506**, Mon–Fri 8 a.m.–6 p.m., TTY (888) 889-4500, 14 language lines |
| `find-an-enroller.md` | Find an Enroller | Certified agent locator |
| `live-chat.md` | Live Chat | |
| `help-on-demand.md` | Help On Demand | |
| `events.md` | Events | Enrollment events and webinars |
| `consumer-protection.md` | Consumer Protection | Formal complaint rights |
| `insurance-company-contacts.md` | Insurance Company Contacts | **Carrier / phone / website / complaint route table** |
| `ombuds-office.md` | Ombuds Office | Last-resort escalation; needs a complaint filed **>30 days** ago and a 10-digit case number starting 5 or 1 |

### 06 — Partners, Agents & Training (15)

| File | Page | Notes |
| --- | --- | --- |
| `enrollment-partners-individuals.md` | Individual Partners | Hub |
| `become-an-agent.md` | Become an Agent | Licensing and appointment pathway |
| `become-a-certified-enroller.md` | Become a Certified Enroller | **CEC** certification and renewal |
| `individual-training-and-education.md` | Individual Training | CE and deadlines |
| `individual-client-support.md` | Individual Client Support | |
| `individual-contact.md` | Individual Partner Contact | |
| `individual-agent-code-of-conduct.md` | Individual Code of Conduct | Complaint and discipline process |
| `marketing-branding-policies.md` | Marketing & Branding Policies | Logo and advertising rules |
| `privacy-policy.md` | Partner Privacy Policy | |
| `enrollment-partners-small-business.md` | Small Business Partners | Hub |
| `ccsb-certification.md` | CCSB Certification | Covered California Small Business certification |
| `ccsb-code-of-conduct.md` | CCSB Code of Conduct | |
| `small-business-training-and-education.md` | SB Training | |
| `small-business-client-support.md` | SB Client Support | |
| `small-business-contact.md` | SB Partner Contact | |

### 07 — News, Policy & Updates (7)

Unlike the other folders, these are **synthesized briefs**, not page mirrors.

| File | What it covers |
| --- | --- |
| `press-releases.md` | Covered California press releases, incl. the 2025–2026 open enrollment cycle releases |
| `marketing-blog.md` | The Covered Blog hub and all **12 consumer-education articles**, with two of the most decision-relevant summarized |
| `federal-policy-changes-2026-2027.md` | **The critical file.** Enhanced APTC sunset, the 2025 CMS Integrity Rule, the June 12 2026 *Columbus v. Kennedy* ruling with the eight vacated provisions, and immigrant APTC restrictions — cross-checked against multiple authoritative sources |
| `covered-california-board-reports.md` | Board of Governors agendas, Executive Director reports, enrollment dashboards from `board.coveredca.com` |
| `agent-briefings-and-toolkits.md` | Certified agent briefings and toolkits from `hbex.coveredca.com`, including the **Lawfully Present Immigrant toolkit in 8 languages** |
| `key-dates-calendar.md` | Consolidated dated timeline, each entry tied to its source |
| `other-authoritative-sources.md` | **Start here for "what other sources?"** — see below |

### 09 — External Databases (9)

**Not coveredca.com.** These are the trusted outside sources that answer what the site will not. Every URL below was verified live on 2026-10-13 unless marked otherwise.

| File | What it gives you |
| --- | --- |
| `cms-marketplace-public-use-files.md` | **The answer to "where are the real plan data."** CMS State-Based Exchange PUF. California file: `cms.gov/files/zip/californiasbpuf2026.zip` — 1,010 plan rows, 14 issuers, 59 counties, 93,840 rate rows. Join key `STANDARD COMPONENT ID` = `PLAN ID`. **Naming trap: the CA file is `sbpuf`, not `sbepuf`.** |
| `plan-and-premium-lookup-tools.md` | Shop & Compare and other quoting tools. **2027 is quotable** at `apply.coveredca.com/shopandcompare/enrollyear` even though it is not downloadable. |
| `covered-california-data-releases.md` | `hbex.coveredca.com/data-research/` — the only carrier-level enrollment crosstab and ZIP-level enrollment table; monthly membership dashboard. |
| `california-health-data-open-portals.md` | `data.chhs.ca.gov` CKAN API — statutory enrollment by carrier, metal tier, Silver variant and rating region. |
| `carrier-regulatory-and-financials.md` | CA Insurance Commissioner filing lists, NAIC crosswalks, carrier financials. |
| `medi-cal-administration-sources.md` | DHCS managed care, rate letters, county matrices, waivers. Resolves the 2026 adult-coverage question. |
| `state-regulatory-and-legislative-oversight.md` | DMHC, California statute lookup via leginfo, LAO, State Auditor. |
| `independent-market-analysis-and-advocacy.md` | KFF State Health Facts, Health Consumer Alliance, CHCF, Urban Institute. |
| `enrollment-and-outreach-data-research.md` | QLEEP, Active Enrollees reports, member surveys, membership dashboards. |

**Three headline answers from this folder:**

1. **California is a State-Based Exchange**, so it is *absent* from the federal Exchange PUFs. Its plan data comes from the SBE PUF at `cms.gov/marketplace/resources/data/state-based-public-use-files`.
2. **2027 plan-year files are NOT published yet** (all 2027 asset URLs 404; the 2026 files were imported 1/13/2026). But 2027 premiums *are* quotable through Shop & Compare.
3. **There is no California State Auditor review of Covered California** that could be found — its existence is **unresolved, not disproven**.

### 10 — Verification Audit (4)

Adversarial re-verification of this library's own claims, written assuming errors existed.

| File | Scope | Result |
| --- | --- | --- |
| `verify-costs-and-financial-help.md` | Financial help, state credits, employer offers, HRAs | 15 claims: 14 confirmed, 1 partially wrong (the income-column error) |
| `verify-enrollment-and-eligibility.md` | Enrollment, SEPs, immigration, documents, SHOP | Confirmed, with 2 minor wording corrections |
| `verify-plans-and-benefits.md` | All four metal tiers, dental, vision, tax penalty, Medi-Cal | 13/13 confirmed; found the missing Platinum drug table |
| `verify-account-and-support.md` | Renewals, appeals, cancellation, 1095-A, Service Center | 8 confirmed, 1 confirmed-in-substance with a wrong label (case number vs reference number) |

### 08 — About & Resources (7)

| File | Page | Notes |
| --- | --- | --- |
| `about-covered-california.md` | About | Marketplace role; five-member board; **not an insurance company** |
| `accessibility-and-language-support.md` | Accessibility & Language | WCAG 2.1 AA certified **as of July 2026**; Section 1557 Civil Rights Coordinator; 14 language lines |
| `privacy.md` | Privacy Policy | Five commitments; forms for every right; amendments within **30 days** |
| `privacy-terms.md` | Terms of Use | Gov. Code §11015.5 notice; automatically collected data |
| `legal-notices.md` | Legal Notices | Service of process by **email and mail** to RecordsCustodian@covered.ca.gov |
| `media-inquiries.md` | Media Inquiries | **(916) 206-7777**; California Public Records Act |
| `social-media-commenting-disclaimer.md` | Social Media Disclaimer | **Social comments are not part of the formal appeal process** |

---

## 🌐 Other Authoritative Sources

coveredca.com is not the whole picture. These are the primary sources a serious reader should cross-check against — full detail in `07-news-policy-and-updates/other-authoritative-sources.md`.

| Source | URL | Authoritative for |
| --- | --- | --- |
| **Covered California Board** | `board.coveredca.com` | Governance, enrollment dashboards, policy actions |
| **Covered California HBEX** | `hbex.coveredca.com` | Agent toolkits, enrollment-period briefings, Shop & Compare |
| **DHCS Medi-Cal** | `dhcs.ca.gov/medi-cal/` | Medi-Cal eligibility and county operations (Covered California *cannot* update county systems) |
| **HealthCare.gov / CMS Marketplace** | `healthcare.gov` · `cms.gov/marketplace/` | Federal rules, the Integrity Rule, national policy |
| **IRS** | `irs.gov/credits-deductions/individuals` | Premium tax credit mechanics and repayment |
| **CA Franchise Tax Board** | `ftb.ca.gov` | Tax filing; the state subsidy requires agreeing to file |
| **Health Consumer Alliance** | via Ombuds page | Free legal help, any language, Mon–Fri 9–5 |

---

## ⚠️ Known Gaps

Honest limitations in this library, so you don't mistake absence for absence in the real world:

1. **Carrier pages carry no plan data.** All 12 carrier pages on coveredca.com share one structural template, and the copy inside each is largely identical — but they are **not** empty. Each page publishes a carrier-named card group for existing members, an application document checklist, a benefits list and three enrollment channels, and this library transcribes all of it. What none of them publish: plan counts, premiums, metal-tier availability, or county service regions. **Do not** rely on this library for per-carrier plan data — use `apply.coveredca.com/lw-shopandcompare/` instead. Molina's 2027 LA/Orange County withdrawal is the sole carrier-specific news item. *(Corrected 2026-10-13: an earlier version of this line called the carrier pages "content-free templates", which was wrong. See the retraction note below.)*
2. **Three client-rendered pages returned no server-side content** and are recorded as partial with cross-referenced facts: `small-business/get-a-quote.md`, `small-business/enrollment-support.md`, `06-.../privacy-policy.md`. Confirmed as a rendering issue, not a fetch failure.
3. **`billing.md` publishes no 60-day termination notice and no grace-period length.** The live page says only that missing payment "could" cancel the plan. Commonly cited figures could not be verified and were not invented.
4. **Silver 73 and Silver 70 publish an identical medical deductible** ($5,200 individual). Only the OOP max and three prescription copays differ. Possibly a CMS data lag — recorded as published.
5. **Covered California's own releases conflict** on the 2026 state-credit income cap: **150% FPL** (Oct 30, 2025) vs **165% FPL** (Dec 22, 2025 and Feb 26, 2026). Both are recorded with dates in `07-news-policy-and-updates/press-releases.md`.
6. **No CSR actuarial-value table and no Silver Silver-variant AV mapping** is published on coveredca.com.
7. **`ftb-form-3853.md`** has FAQ questions whose answers are collapsed in the page source.
8. **`coveredca.com/faq` returns 404** — no such page exists.
9. **No CalSTRS/CalPERS carve-outs and no state Cal-STRS tax credit** appear anywhere in the 19 small-business pages. The published credit is the federal one: up to 50% (for-profit) / 35% (tax-exempt), under 25 FTEs, for up to 2 years.
10. **The site publishes no explicit 1095-C/1094-C filing deadlines** — it defers to the IRS instructions.
11. **Many authoritative outside sites are unreachable from this environment**, so some cross-checks could not be completed: `dmhc.ca.gov` (403, except the root without `www`), `cbo.gov` (403), `gao.gov` (403), `chffa.org` (connection failure), `osc.ca.gov` and `aoos.gov` (DNS failure — correct auditor domain is `www.auditor.ca.gov`), `californiahealthreport.org` (DNS failure), `dhcs.ca.gov` (returns HTTP 200 but serves only an Incapsula challenge stub), and Wayback (429/503). These are network/bot blocks from this machine, not proof the information is unavailable to you.
12. **`cms.gov/marketplace/data` is a 404.** The CMS marketplace data pages have moved; plan data now lives at `cms.gov/marketplace/resources/data/state-based-public-use-files`.
13. **2027 plan-year data files are not yet published** by CMS as of 2026-10-13, so carrier plan counts for 2027 cannot be verified from public files yet.

### How to read `SITE-INDEX.md` — and how not to

`SITE-INDEX.md` is a **gap-finder, not a proof of absence.** Read these four limits before using it:

1. **It captures structure, not prose.** It records tables, card groups, headings and FAQ question headings. It does **not** carry paragraph text. A page can publish ten facts in prose and appear in the index to publish nothing at all. Any conclusion of the form "the page does not say X" cannot be drawn from it.
2. **It cannot see tab-hidden content.** Bronze, Gold and Platinum each carry a **Prescription Costs** table that exists in the site's Sanity CMS payload but is **not server-rendered** into the initial DOM — it appears only after a reader selects the tab. The index therefore records exactly one table for each of those pages. Silver's drug table *is* rendered, which is why Silver alone shows the heading. This is a tooling limit, not a site difference, and it is the single most likely way to reach a wrong conclusion from the index.
3. **It captures FAQ questions, not answers.** A listed question is evidence that the question is asked, never that any particular answer exists.
4. **English only.** 119 pages were indexed. The 115 Spanish mirrors were deliberately skipped, so the index is not a complete map of coveredca.com.

The safe way to use it: **use the index to find gaps, and open the live page to confirm before adding.** Never use it as the sole basis for *removing* content from this library.

> **Recorded failure (2026-10-13).** During the pass that produced `SITE-INDEX.md`, three remediation agents worked from it and used its silence as evidence of absence. They removed roughly 20 correct claims from the small-business and enrollment files — the CCSB adjacent-tier rule, the 9.96% and 60% contribution tests, the 100-FTE eligibility limit, the "only one document" SSN rule and the fax/mail submission path — and flagged the Bronze, Gold and Platinum prescription tables as unsupported. Every one of those claims was then re-verified as **verbatim correct** on the live pages. Two library files (`INDEX.md` and `10-verification-audit/verify-plans-and-benefits.md`) had carried a related wrong claim, that the 12 carrier pages are "content-free templates"; that was also false and is retracted. The retraction notes remain in the affected files. The generalisable lesson is recorded in `10-verification-audit/verify-plans-and-benefits.md`: the writer and the checker must not share one extraction method, and a missing signal is never a finding.

---

## 🔧 Tooling

`_raw/` holds the reusable research plumbing:

| File | Purpose |
| --- | --- |
| `site_index.py` | **The structural indexer.** Python 3.14 stdlib only, DOM-based. Walks all 119 English pages and records real `<table>` grids with row labels, `<article>` card groups, heading outlines and FAQ question headings into `SITE-INDEX.json`. This is what renders `SITE-INDEX.md`. |
| `render_index.py` | Renders `SITE-INDEX.json` into the human-readable `SITE-INDEX.md` with a per-page risk ranking. |
| `audit_structure.py` | **The mechanical checker.** Diffs every site table row and card label against the library files and prints only real signals. This exists so row-count and row-label defects are script-detectable rather than reviewer-judgement-dependent. |
| `show_page.py` | Prints one page's full structural record from `SITE-INDEX.json`. Use `--list tables` or `--list cards` to narrow. |
| `extract.ps1` | **DEPRECATED — do not use for new work.** The original payload unescaper. It flattens everything into prose, which means it **cannot distinguish a table row from a paragraph**. That defect is the direct cause of the errors documented above. Kept only for provenance. |
| `sitemap.xml` | The original site map (234 URLs: 119 English + 115 Spanish) |
| `urls_en.txt` / `urls_es.txt` | The URL inventory this library is built from |
| `verify/` | Plain-text renders of the pages that were re-checked by hand on 2026-10-13, kept as the evidence behind the correction notes. HTML snapshots were discarded after extraction to keep the repo small; re-fetch any of them with `site_index.py`. |

Usage:

```powershell
cd _raw
$env:PYTHONIOENCODING='utf-8'
python site_index.py      # refetch and rebuild SITE-INDEX.json (119 pages, ~2 min)
python render_index.py    # rebuild SITE-INDEX.md
python audit_structure.py # library vs site diff
python show_page.py /coverage-basics/coverage-levels/gold --list cards
```

For prose that `site_index.py` does not capture, read the page's CMS payload directly — `site_index.py` is the gap-finder, and the payload is the confirmation. Pass multiple URLs to `extract.ps1` to batch-fetch if you must use it for legacy reasons.

---

## 🧭 Where to Look

| If you want to know… | Go to |
| --- | --- |
| I want to know what I'll actually pay | `02-costs-and-financial-help/financial-help.md`, then Shop & Compare |
| When I can enroll | `03-enrollment-and-eligibility/open-enrollment.md` + `07-news-policy-and-updates/key-dates-calendar.md` |
| Whether I qualify | `03-enrollment-and-eligibility/eligibility.md`, `immigrants.md` |
| How to compare plans | `01-coverage-and-plans/coverage-levels.md` then the four tier files |
| What the real plan data and premiums are | `09-external-databases/cms-marketplace-public-use-files.md` + `plan-and-premium-lookup-tools.md` |
| How many plans each carrier offers | `09-external-databases/cms-marketplace-public-use-files.md` — coveredca.com will not tell you |
| What changed and why | `07-news-policy-and-updates/federal-policy-changes-2026-2027.md` |
| I'm being denied something | `04-account-and-managing-coverage/file-an-appeal.md` |
| I'm a broker/agent | `06-partners-agents-and-training/` |
| I'm an employer with 1–100 staff | `03-enrollment-and-eligibility/small-business/` |
| I'm an agent for Medi-Cal | `05-help-support-and-rights/ombuds-office.md` (it will route you to DHCS) |
| I want independent analysis, not agency messaging | `09-external-databases/independent-market-analysis-and-advocacy.md` |
| I want to check whether this library is trustworthy | `10-verification-audit/` |

---

*Every file records its source URL and a 2026-10-13 retrieval date. Figures are reproduced as published — verify against the live site before making a decision, since marketplace rules change annually and this library is a snapshot.*