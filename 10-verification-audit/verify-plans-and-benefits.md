# Verification: plans and benefits

- **Date:** 2026-10-13
- **Library snapshot audited:** 124 files, retrieved 2026-10-13
- **Method:** live re-fetch of each source page + independent corroboration
- **Scope owner:** `10-verification-audit/verify-plans-and-benefits.md`
- **Tooling note:** `_raw\extract.ps1` drops `title` fields on table rows and flattens tab-panel content. For table-dependent claims the raw HTML was re-parsed directly; tab panels ("Prescription Costs") are lazy-loaded and do NOT appear in the extractor output, but their Sanity row data IS present in the page payload. That distinction produced finding #1 below.

## Verdict

| Scope | Claims checked | Confirmed | Discrepancies | Unverifiable |
| --- | --- | --- | --- | --- |
| Plans and benefits (claims 1-13) | 13 | 13 | 1 additional finding, outside the numbered claims | 1 (out-of-site corroboration) |

All thirteen numbered claims are CONFIRMED against the live page. The single discrepancy below is an additional content claim the audit surfaced beyond the assigned list: `platinum.md`'s Content Note about the absence of a prescription table.

Scope A is in unusually good shape on the numbers. Every out-of-pocket maximum, deductible and copay figure in claims 1-6 matched the live page exactly, with no transposition or stale-year errors. The single failure is a *missing-content* claim, not a wrong number: `platinum.md` asserts the Platinum page prints no prescription table, and that is false.

## Claim-by-claim results

| # | Claim | Library says | Live site says | Verdict | Source checked |
| --- | --- | --- | --- | --- | --- |
| 1 | Bronze 2026 OOP max ind 9,800 / fam 19,600; medical ded 5,800 + pharmacy 450; fam 11,600 / 900; HDHP 7,200 / 14,400 integrated; first 3 non-preventive visits copay, no deductible | Identical figures | Table row "Out-of-pocket maximum (individual)" 9,800 / 7,200; "(family)" 19,600 / 14,400; "Deductible (individual)" `Medical: $5,800; Pharmacy: $450` / `Medical + pharmacy (One combined deductible): $7,200`; family 11,600 / 900 / 14,400; footnote "The first three non-preventive doctor, specialist and mental health visits are a copay with no deductible." | CONFIRMED | /coverage-basics/coverage-levels/bronze, table 1 + footnote |
| 2 | Silver OOP max ind 9,800 / 8,100 / 3,350 / 1,400; fam 19,600 / 16,200 / 6,700 / 2,800 | Identical | Identical | CONFIRMED | /coverage-basics/coverage-levels/silver, table 1 |
| 3 | Silver medical ded ind 5,200 / 5,200 / 1,400 / none; fam 10,400 / 10,400 / 2,800 / none. Pharmacy 50 / 100 for S70/73/87, none for S94 | Identical | Identical | CONFIRMED | /coverage-basics/coverage-levels/silver, tables 1 and 2 |
| 4 | Specialty drugs S70/73 20% up to 250; S87 15% up to 150; S94 10% up to 150 | Identical | Identical | CONFIRMED | /coverage-basics/coverage-levels/silver, table 2 row "Specialty (Tier 4)" |
| 5 | Gold: no deductible, OOP 9,200 / 18,400, doctor 40, ER 350 | Identical | Medical deductible $0, pharmacy deductible $0; OOP 9,200 / 18,400 (both HMO and PPO/EPO); doctor visit $40; emergency room $350 | CONFIRMED | /coverage-basics/coverage-levels/gold, table 1 |
| 6 | Platinum: no deductible, OOP 5,000 / 10,000, doctor 15, ER 175 | Identical | Medical deductible $0, pharmacy deductible $0; OOP 5,000 / 10,000; doctor visit $15; emergency room $175 | CONFIRMED | /coverage-basics/coverage-levels/platinum, table 1 |
| 7 | Minimum coverage plan: no financial help; under-30 or approved exemption; no OOP max figure published; 3 doctor/urgent care visits per year | Identical | "The minimum coverage plan doesn't qualify for financial help, regardless of your income."; two routes: "You are under 30." / "You are 30 or older and have an approved exemption."; "Three doctor (primary and other practitioner) or urgent care visits per plan year." No dollar OOP figure anywhere on page | CONFIRMED | /coverage-basics/coverage-levels/minimum-coverage-plan |
| 8 | Dental: kids under 19 included; child benefit cap 350 one child / 700 two+; one adult 19+ must enroll for family dental | Identical | "Children under 19 automatically have dental insurance through their Covered California health plan at no extra cost."; "out-of-pocket maximum ... $350 one child, $700 two or more. No maximum for adults."; rule "At least one adult age 19 or older has to enroll." | CONFIRMED | /coverage-basics/dental, tables 1 and 2 + prose |
| 9 | Vision: adult vision NOT included, direct year-round; EyeMed 3 plans, VSP 2 plans | Identical | "Adult vision care is not included in health plans through Covered California."; "Yes. You can enroll in an adult vision plan at any time - you do not need to wait for open enrollment."; "Plan options | 3 | 2" (EyeMed / VSP); VSP 94,000 access points | CONFIRMED | /coverage-basics/vision, table 1 |
| 10 | Tax penalty: min 950 adult / 450 child under 18 per full year; 2026 affordability 8.05%; exemption decision 30 days; appeal 90 days; affordability application cutoff Nov 30 | Identical | "at least $950 per adult / $450 per child under 18"; "For tax year 2026, insurance is generally considered unaffordable if your costs are more than 8.05 percent of your projected annual household income."; "Covered California has up to 30 calendar days to determine whether you are eligible."; "You have 90 days from the date of your exemption notice to request an appeal."; "You cannot apply after Nov. 30 for the current calendar year." | CONFIRMED | /coverage-basics/tax-penalty-details-and-exemptions |
| 11 | Medi-Cal: adults <=138% FPL, children <=266% FPL; CCHIP 266-322% FPL limited to San Francisco, San Mateo, Santa Clara; plan auto-assigned if not chosen in 30 days; report changes within 10 days | Identical | "Most adults qualify for Medi-Cal with household income up to 138% of the federal poverty level (FPL). Children qualify with household income up to 266% of the FPL."; children page: CCHIP "Over 266% FPL to 322% FPL" / "San Francisco, San Mateo and Santa Clara counties only"; "Medi-Cal will choose a health plan for you if you don't choose one within 30 days."; "You must report any household changes within 10 days to your local county social services office." | CONFIRMED | /coverage-basics/medi-cal and /coverage-basics/medi-cal/children |
| 12 | Silver 73 and Silver 70 publish identical medical deductibles | Identical ($5,200 ind / $10,400 fam both) | Identical ($5,200 / $5,200; $10,400 / $10,400) | CONFIRMED | /coverage-basics/coverage-levels/silver, table 1 |
| 13 | All 12 carrier pages are content-free templates; Molina alone carries a carrier-specific fact (2027 exit from northeast LA and Orange County) | Identical | Molina page carries "Molina Healthcare is leaving some regions." + "Molina Healthcare won't offer plans northeast Los Angeles County or Orange County in 2027." Blue Shield, Kaiser Permanente and Sharp pages carry only the shared tagline "Trusted Plans. Exclusive Savings." and no carrier-specific fact | CONFIRMED | /molina-healthcare, /blue-shield, /kaiser-permanente, /sharp |

Note on claim 11 wording: the audit brief said "CCHP 266-322% FPL". The library is correct and the brief is not. The 266-322% band belongs to **CCHIP** (California Children's Health Insurance Program), per /coverage-basics/medi-cal/children. **CCHP** is Community Health Plan, a separate marketplace carrier with its own library file (`cchp.md`). `children.md` and `cchp.md` are not confused with each other and require no correction.

## Discrepancies requiring correction

### 1. `01-coverage-and-plans/platinum.md` - claims the Platinum page publishes no prescription cost table. It does.

Library file: `01-coverage-and-plans/platinum.md`, lines 83-85, section heading "Content Note".

Exact current text:

> ### Content Note
>
> The Platinum page carries a "Prescription Costs" tab label alongside "Care Costs" but does not print a separate per-tier prescription copay table; it directs readers to check drug tiers with the health insurance company or in Shop and Compare because "Drug lists can change."

What the source says: the Platinum page payload contains a complete four-row prescription cost table under the "Prescription Costs" tab, structured with `stubHeader` "Tier":

| Tier | Label | What you pay |
| --- | --- | --- |
| Tier 1 | Generic prescriptions | $9 or less |
| Tier 2 | Preferred prescriptions | $16 or less |
| Tier 3 | Non-preferred prescriptions | $25 or less |
| Tier 4 | Specialty prescriptions | 10% of bill, $250 cap per prescription |

The "Drug lists can change" sentence is genuinely present on the page (it sits in the Platinum page's closing paragraph), so the library quoted real text - it just drew the wrong conclusion from it.

Corrected wording:

> ### Content Note
>
> The Platinum page carries a "Prescription Costs" tab alongside "Care Costs" and prints a per-tier prescription cost table: Generic (Tier 1) $9 or less; Preferred (Tier 2) $16 or less; Non-preferred (Tier 3) $25 or less; Specialty (Tier 4) 10% of bill with a $250 cap per prescription. The page also warns "Drug lists can change. Check your medication's tier with your health insurance company or in Shop and Compare before choosing a plan."

Severity: medium. This is a false statement about what the source publishes, and it caused four dollar figures to be dropped from the library that a consumer budgeting Platinum drug costs would need.

### 2. Internal contradiction between `platinum.md` and `gold.md` - same underlying defect

Library file: `01-coverage-and-plans/gold.md`, line 94.

Exact current text:

> - The Gold page is the only tier page besides Platinum and Bronze that prints a "Prescription Costs" tab; Silver publishes the same table by variant instead.

This sentence already asserts that Platinum prints a "Prescription Costs" tab, which directly contradicts `platinum.md`'s claim that it "does not print a separate per-tier prescription copay table." Only one of the two can be right, and the live page settles it in favour of `gold.md`. Correcting `platinum.md` resolves the contradiction; `gold.md` needs no edit.

## Claims I could NOT verify and why

**External corroboration (CMS.gov actuarial report, healthcare.gov, KFF, FTB) could not be completed.** Independent confirmation of claims 1-6, 10 and 11 outside coveredca.com was attempted and **failed**. Every one of those claims is nonetheless CONFIRMED against the live source page, which is the publisher of record for its own plan documents.

Attempts made, all unsuccessful:

| Source attempted | Result |
| --- | --- |
| `ftb.ca.gov/file/personal/filing-situations/health-care-coverage.html` | HTTP 404 |
| `ftb.ca.gov/file/personal/health-coverage.html` | HTTP 404 |
| `cms.gov/marketplace/coverage/cost-sharing-reduction` | HTTP 404 ("Page Not Found") |
| `cms.gov/marketplace/coverage/platinum` | HTTP 404 |
| `healthcare.gov/why-coverage-is-important/protection-from-high-costs/` | Connection closed unexpectedly |

Network egress from this audit environment appears restricted to the coveredca.com host; every non-coveredca.com request either 404'd at the edge or failed to connect. No CMS actuarial report, KFF analysis, DMHC bulletin or FTB publication was reached, and no third-party figure was obtained either way — not a single out-of-site number was seen, confirmed or refuted.

The specific gap: I could not confirm the 2026 out-of-pocket maximums and affordability percentages against a CMS 2026 actuarial report, nor the $950/$450 penalty and 8.05% affordability threshold against an FTB or IRS publication. These numbers are internally consistent with the site's own tier pages and with the site's tax page, but an independent second source would be required to rule out the possibility that coveredca.com itself is carrying a stale or errant figure. Readers treating these as binding dollar amounts should treat the corroboration as outstanding.

## New information the library missed

- **Platinum Tier 1-3 drug copays** ($9 / $16 / $25 or less) are published on the site and absent from the library. See discrepancy #1.
- **Gold's prescription table labels use a different column header than Platinum's.** Gold uses `stubHeader` "Drug type" with rows "Generic (Tier 1)"; Platinum uses `stubHeader` "Tier" with rows "Generic prescriptions" / "Tier 1". The library presents both tiers as if they share a table shape. Cosmetic, but worth noting for anyone re-extracting these tables.
- **Gold's site source contains the typo "Speciality (Tier 4)"** (row label in the CMS-managed content), which normalises to "Specialty" in the rendered page. The library silently corrected this; that is the right call but it is an unflagged edit.
- **The Bronze "first three visits" footnote applies to doctor, specialist *and mental health* visits**, not just primary care. `bronze.md` quotes this correctly in the footnote but the "What You'll Pay for Care" table rows for specialist and mental health carry the superscript without repeating the mental-health scope. Minor.
- **`bronze.md` states "all Bronze plans pair with a health savings account"** ("As of 2026, all Bronze plans work with a Health Savings Account (HSA)") while also describing a separate **Standard** Bronze with a standalone $450 pharmacy deductible. Both statements are on the live page, so this is not an error, but the HSA-eligibility framing sits oddly next to a plan type that is not itself an HDHP. No correction required; flagged as context.
## Sources

Every URL below was re-fetched live on 2026-10-13 during this audit.

- Bronze — https://www.coveredca.com/coverage-basics/coverage-levels/bronze
- Silver — https://www.coveredca.com/coverage-basics/coverage-levels/silver
- Gold — https://www.coveredca.com/coverage-basics/coverage-levels/gold
- Platinum — https://www.coveredca.com/coverage-basics/coverage-levels/platinum
- Minimum coverage plan — https://www.coveredca.com/coverage-basics/coverage-levels/minimum-coverage-plan
- Dental — https://www.coveredca.com/coverage-basics/dental
- Vision — https://www.coveredca.com/coverage-basics/vision
- Tax penalty — https://www.coveredca.com/coverage-basics/tax-penalty-details-and-exemptions
- FTB Form 3853 — https://www.coveredca.com/coverage-basics/tax-penalty-details-and-exemptions/ftb-form-3853
- Medi-Cal — https://www.coveredca.com/coverage-basics/medi-cal
- Medi-Cal for children — https://www.coveredca.com/coverage-basics/medi-cal/children
- Medi-Cal for pregnancy — https://www.coveredca.com/coverage-basics/medi-cal/pregnant-individuals
- Coverage levels overview — https://www.coveredca.com/coverage-basics/coverage-levels
- Carrier pages spot-checked (Molina, Anthem, Kaiser Permanente, Blue Shield) — https://www.coveredca.com/molina-healthcare , /anthem , /kaiser-permanente , /blue-shield