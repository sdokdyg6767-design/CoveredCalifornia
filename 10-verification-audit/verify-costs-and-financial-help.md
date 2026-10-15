# Verification: Costs and Financial Help

- **Date:** 2026-10-13
- **Library snapshot audited:** 124 files, retrieved 2026-10-13
- **Method:** live re-fetch of each source page + independent corroboration

## Verdict

| Scope | Claims checked | Confirmed | Discrepancies | Unverifiable |
| --- | --- | --- | --- | --- |
| Costs and financial help | 9 claims + 3 library-text checks | 9 | 1 material (plus 2 minor) | 0 |

## Claim-by-claim results

| # | Claim | Library says | Live site says | Verdict | Source checked |
| --- | --- | --- | --- | --- | --- |
| 1 | APTC income band 100%–400% FPL, any coverage level | `financial-help.md`: "between 100% FPL to 400% FPL"; "Available to use with any plan coverage level" | Identical: "Available if your income is between 100% FPL to 400% FPL." / "Available to use with any plan coverage level." | CONFIRMED | https://www.coveredca.com/costs/financial-help |
| 2 | CSR at 250% FPL or less, Enhanced Silver only | `financial-help.md`: "250% FPL or less"; "Included with Enhanced Silver plans" | Identical | CONFIRMED | https://www.coveredca.com/costs/financial-help |
| 3 | 2027 state credit $300M; cap 200% FPL = $31,920 ind / $66,000 fam4; 500,000+ recipients; 200,000 newly eligible; nearly 200,000 choose two Silver plans at $0 | All five figures present | "$300 million … up from $190 million"; "up to 200 percent of the federal poverty level in 2027 ($31,920 for an individual or $66,000 for a family of four)"; "more than 500,000 Californians are projected to receive a state subsidy in 2027"; "open financial help to an additional 200,000 Californians who weren't eligible in 2026"; "nearly 200,000 can choose from two Silver-tier plans with a $0 premium" | CONFIRMED | https://www.coveredca.com/press-releases/2026/07/21/covered-california-rates-and-plans-for-2027-california-continues-fight-for-health-insurance-affordability-and-access |
| 4 | 2026 state credit $190M; income cap 150% vs 165% FPL — library records both | Library records both and flags the discrepancy | Oct. 30, 2025 release: "$190 million … earning up to 150 percent of the federal poverty level". Dec. 22, 2025 release: "$190 million … earning up to 165 percent of the federal poverty level" | CONFIRMED (the conflict is real and correctly characterized) | Both 2025 press releases, fetched live |
| 5 | 2027 average rate change +9.9%; 60% no increase; 26% keep $0 premium | All three | "preliminary weighted average rate increase of 9.9 percent"; "60 percent of enrollees will see no increase in their monthly premium, 26 percent will remain eligible for $0 premiums without changing plans" | CONFIRMED | July 21, 2026 press release |
| 6 | Enhanced APTC ended Dec. 31, 2025; premiums +97% for 1.7M+; 160,000 lose eligibility; ~$2.5B/year | All four | "that help ended on Dec. 31, 2025"; "premiums are projected to rise by 97 percent on average for more than 1.7 million Californians"; "more than 160,000 middle-income consumers … would lose eligibility in 2026"; "cannot replace the nearly $2.5 billion in enhanced premium tax credits that Californians receive from the federal government annually" | CONFIRMED | https://www.coveredca.com/important-changes and Oct. 30, 2025 press release |
| 11 | Employer affordability 9.96%; minimum value 60% | `employer-coverage.md`: 9.96% or less; at least 60 percent | "The lowest-cost, employee-only option costs 9.96% or less of your household income"; "The plan pays at least 60 percent of the total cost of medical services" | CONFIRMED | https://www.coveredca.com/costs/financial-help/employer-coverage |
| 14 | Covered California itself publishes conflicting 2026 state-credit income caps | `press-releases.md` records 150% (Oct 30, 2025) and 165% (Dec 22, 2025) | Both figures verified verbatim in the two live releases | CONFIRMED | Both 2025 press releases |
| 13 | `billing.md` publishes no 60-day non-payment termination notice and no grace period | `billing.md` and `INDEX.md` lines 146 and 242 assert the page "could" cancel coverage for non-payment and publishes no day count or grace period | The live billing page says only that a missed payment "could" cancel your plan, with no day count and no grace-period length. I searched the full sitemap for any grace/non-payment/lapse page and found none | CONFIRMED | https://www.coveredca.com/account/billing plus full `_raw/sitemap.xml` scan |

## Discrepancies requiring correction

### 1. `02-costs-and-financial-help/financial-help.md` — SSI and Child Tax Credit are on the WRONG SIDE of the income table (material, consumer-harmful)

Current text in the file, under "Income items the page says to include vs. exclude":

> - Include: self-employment income; retirement or pension income; investment income; **Supplemental Security Income (SSI)**; **Child Tax Credit**.
> - Do not include: child support.

What the source actually says. The live page renders two side-by-side columns. The "Doesn't Count" column is prefaced "Do **not** include when you report your income." and contains, in order:

> Child support, Gifts, Veteran disability payments, **Supplemental Security Income (SSI)**, Workers' compensation, Money from loans, like student or home equity loans, **Child Tax Credit**

The "Counts" column is prefaced "Include these when you report your income." and contains only:

> Wages and salary, Tips, Self-employment income, Unemployment, Social Security benefits, Social Security Disability (SSDI), Retirement or pension income, Investment income

So the library has moved two items that the page explicitly tells consumers **not** to report from the "Doesn't Count" column to the "Include" column. This is the single most consequential error in the scope A files: a reader following the library would report SSI and the Child Tax Credit as household income, overstating their income by potentially thousands of dollars and reducing their APTC.

Corrected wording — replace the two bullets with:

> - Include: wages and salary; tips; self-employment income; unemployment; Social Security benefits; Social Security Disability (SSDI); retirement or pension income; investment income.
> - Do not include: child support; gifts; veteran disability payments; Supplemental Security Income (SSI); workers' compensation; money from loans such as student or home equity loans; Child Tax Credit.

Verified against raw HTML at the `Doesn’t Count` heading, not just the flattened extractor output. Note this error also means the library **omits** wages, tips, unemployment, Social Security and SSDI, which the page does list under "Counts".

### 2. `07-news-policy-and-updates/press-releases.md` — HCARF full name is wrong

Current text: "**$300 million** appropriated through the Health Care Affordability and Responsiveness Fund (HCARF) for the state subsidy in 2027".

Live release text: "appropriating $300 million in **Health Care Affordability Reserve Fund** (HCARF)". The acronym HCARF is correct; the expansion is not.

Corrected wording: "**$300 million** appropriated through the Health Care Affordability Reserve Fund (HCARF) for the state subsidy in 2027 — up from **$190 million** for 2026."

### 3. `02-costs-and-financial-help/costs.md` — copay definition is quoted from the wrong page

Current text quotes the copay as "A set amount you pay for a covered visit or service." That is the wording from `/costs/financial-help`. The `/costs` page itself says:

> A fixed amount you pay for a covered service, like a doctor visit or prescription.

Minor, but the file presents these as page-published definitions, and the `/costs` page wording additionally names prescription as an example.

## Claims I could NOT verify and why

No claim in this scope was unverifiable against the Covered California source itself.

**Independent corroboration was only partly completed, and I am not claiming more than I did.** From this environment every attempt at CMS.gov, KFF, Medicaid.gov, DHCS and the HealthCare.gov deep links failed — 404s on the CMS and HealthCare.gov deep links, a 403 from Medicaid.gov, an empty response body from DHCS, and aborted connections from KFF and HealthCare.gov. The one success was the HealthCare.gov CSR glossary, which independently corroborates the **Silver-only** element of claim 2:

> "If you qualify, you must enroll in a plan in the Silver category to get the extra savings… if you qualify for extra savings too, you'll get those savings only if you pick a Silver plan."

That page does **not** state the 250% FPL threshold, so the numeric half of claim 2 remains corroborated by the Covered California page alone. Claims 1, 3, 5, 6 and 9 are confirmed against coveredca.com but were **not** corroborated against a second authoritative source. For claims 3 and 5 I regard this as low risk: both are figures Covered California publishes in a dated press release quoting its own regulator and its own actuarial exhibit, and an independent source would only be re-reporting them.

The reason this matters beyond bookkeeping: claim 6's 160,000 and claim 3's 500,000-plus are Covered California **projections** about its own enrollees. A library that restates them as fact without the "projected" qualifier inherits an estimate as a measurement.

## Possible fabrication: none found

No library number in this scope was absent from the source pages. Every figure I tested — 100–400%, 250%, $300M, $31,920, $66,000, 500,000+, 200,000, $190M, 150%, 165%, 9.9%, 60%, 26%, 97%, 1.7M, 160,000, $2.5B, 9.96%, 60% — appears verbatim in a live page. That is a notably clean result and the opposite of what the adversarial framing anticipated, so I am reporting it plainly rather than manufacturing a finding.

The one failure mode that *did* appear is not invention but **mis-assignment**: the SSI and Child Tax Credit error above is a real page-to-library corruption, and it points at a specific weakness in how the library was built. The extractor flattens `/costs/financial-help` into two adjacent lists whose column boundaries are not marked in the output. A side-by-side "Counts / Doesn't Count" table is exactly the layout where an automated summarizer can silently merge the wrong column, and that is what happened. Any other two-column page in the library deserves the same skeptical re-read.

## New information the library missed

- The full "Counts" list on `/costs/financial-help`: wages and salary, tips, self-employment income, unemployment, Social Security benefits, SSDI, retirement or pension income, investment income. The library recorded only three of the eight.
- The full "Doesn't Count" list: gifts, veteran disability payments, workers' compensation, and money from loans (student or home equity) — none recorded.
- The July 21, 2026 release publishes region-level and carrier-level rate detail the library does not capture: Statewide Total enrollees 1,785,900 with a **-0.2%** "shop and switch" figure; 19 rating regions (lowest Inland Empire Health Plan's Region 4 San Francisco 9.7%, highest Region 13 Mono/Inyo/Imperial 14.9%); and by-carrier overall changes ranging from Inland Empire Health Plan 5.6% to Valley Health Plan 20.4%.
- Molina's departing ~1,600 enrollees in Regions 15 and 18 will be allowed to "move to the carrier with the lowest-cost plan **in the same metal tier**" — a guaranteed-shopping protection not mentioned anywhere in the library.
- The Dec. 22, 2025 release reports "more than 364,000 people have enrolled with state subsidies" and gives shopping savings by metal tier: Platinum and Gold plans 23% lower premiums, Silver 70 and 73 plans 39% lower, with the current issuer. Not in the library.
- The Dec. 22, 2025 release publishes the California Shared Responsibility Penalty amounts (at least $900 per adult, $450 per dependent child, $2,700 for a family of four). Not in the library.