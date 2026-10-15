# Verification: Enrollment and Eligibility

- **Date:** 2026-10-13
- **Library snapshot audited:** 124 files, retrieved 2026-10-13
- **Method:** live re-fetch of each source page + independent corroboration

## Verdict

| Scope | Claims checked | Confirmed | Discrepancies | Unverifiable |
| --- | --- | --- | --- | --- |
| Enrollment and eligibility | 6 claims | 5 | 1 | 0 |

Scope B is the strongest part of the library. Every enrollment window, every SEP deadline, every immigration date and every SHOP figure in the assigned file list matched the live source. The single defect is an over-broad sentence in `INDEX.md`, not in any of the audited source files.

## Claim-by-claim results

| # | Claim | Library says | Live site says | Verdict | Source checked |
| --- | --- | --- | --- | --- | --- |
| 7 | Open enrollment 2027 Nov 1 2026 – Jan 31 2027; Dec 31 2026 for a Jan 1 start; January signups start Feb 1 | `open-enrollment.md` | "Open enrollment for 2027 coverage runs Nov. 1, 2026, to Jan. 31, 2027." / "Enroll by Dec. 31 for a health plan that starts Jan. 1. Enroll in January for a plan starting Feb. 1." | CONFIRMED | https://www.coveredca.com/enrollment/open-enrollment |
| 8 | SEP: standard 60 days; loss of coverage 60 days before or after; Medi-Cal loss 90 days; incarceration release 60 days | `major-life-changes.md` | "Within 60 days of the event"; "60 days before or after your coverage ends to apply"; "Within 90 days of your Medi-Cal ending"; "Within 60 days of your release". COBRA exhaustion: "You have 60 days before and 60 days after your coverage ends." | CONFIRMED | https://www.coveredca.com/enrollment/major-life-changes |
| 9 | Immigration: adults 19+ lost full Medi-Cal Jan 1 2026; DACA excluded Aug 2025; 2027 restriction to green card / Cuban-Haitian entrants / COFA migrants effective Jan 1 2027 | `immigrants.md` | All three present: "Starting Jan. 1, 2026", "as of August 2025", and the H.R. 1 2027 groups. Library also correctly captures that 2026 costs do not change | CONFIRMED | https://www.coveredca.com/enrollment/eligibility/immigrants |
| 10 | Documents: one document per request; copies only; income statements within 45 days; non-incarceration proof not currently requested | `documents.md` is accurate on three of four | "In most cases, you only need to submit one document."; "Always send copies" and "Do not send originals"; "We're not asking for this document." for non-incarceration. BUT the 45-day rule applies to the **EMPLOYER STATEMENT** only: "Dated within 45 days of submission" — not to income statements generally | PARTIALLY WRONG | /enrollment/documents, /enrollment/documents/income, /enrollment/documents/not-incarcerated |
| 11 | SHOP: 1–100 FTEs; employer contributes ≥50%; adjacent metal tiers; affordability 9.96%; minimum value 60% | `small-business/eligibility.md`, `costs-and-financial-help.md`, `health-plans.md` | "You have 100 or fewer full-time-equivalent employees" plus "at least one employee who receives a W-2"; "Pay at least 50 percent of … premiums"; "**Adjacent metal tiers**"; "9.96% or less of your household income"; "at least 60 percent of the total cost of medical services" | CONFIRMED | /small-business/eligibility, /small-business/costs-and-financial-help, /small-business/health-plans, /costs/financial-help/employer-coverage |
| 12 | 1095-C: all full-time employees; W-2 Box 12 Code DD; Additional Medicare Tax 0.9% above $200,000 | `small-business/1095-forms.md` | "you are required to issue Form 1095-C to each full-time employee"; "**Form W-2 in Box 12, Code DD**"; "an additional **0.9 percent** of Medicare Tax on employee wages or compensation that exceed **$200,000**" | CONFIRMED | https://www.coveredca.com/small-business/mandate/1095-forms |

## Discrepancies requiring correction

### 1. `INDEX.md` — the 45-day document rule is stated against the wrong document type

Current text at line 130:

> one document per request; **income statements must be dated within 45 days**; copies only

What the source actually says. The 45-day dating requirement is attached to exactly one document type on the live income page. Under **Employer statement** the requirements read:

> - Be dated within 45 days of submission
> - Include employer information, such as company name and address
> - Show the employee's eligibility for employer-sponsored insurance, including coverage dates

The other income evidence the page accepts — pay stubs, unemployment benefits, Social Security benefits, retirement or pension statements, investment income — carries **no 45-day dating rule**. The live page states a 45-day window only for employer statements.

This matters because the over-broad wording implies a stale pay stub will be rejected and forces a consumer to request a fresh document unnecessarily. Note that `03-enrollment-and-eligibility/documents/doc-income.md` itself is correct and does not over-generalize; the defect is confined to the `INDEX.md` summary line.

Corrected wording:

> one document per request; **employer statements must be dated within 45 days of submission**; copies only, never originals; proof of non-incarceration is not currently requested

### 2. `INDEX.md` — SHOP employee threshold described imprecisely

Current text compresses SHOP eligibility to "1–100 full-time employees". The live `/small-business/eligibility` page states two separate conditions:

> - You have 100 or fewer full-time-equivalent employees
> - You have at least one employee who receives a W-2

Two corrections matter. The threshold is expressed in **full-time-equivalent** employees, not headcount — the page explicitly distinguishes the two elsewhere ("A full-time-equivalent employee is not simply a headcount. It is a calculation that combines the hours of part-time and full-time employees"). And the floor is defined by W-2 receipt, not by "1 employee".

Corrected wording:

> **100 or fewer full-time-equivalent employees**, with **at least one employee who receives a W-2**

### 3. `03-enrollment-and-eligibility/major-life-changes.md` — the summary table understates the list of qualifying events

The library's table has five rows, collapsing "Common events" into a parenthetical. The live page publishes **thirteen** distinct qualifying events in a three-column table (event / how long you have to act / coverage start). The library's body text does cover most of them, but the table — the part a consumer would scan — is materially narrower than the source.

Current table rows in the file: `Qualifying event` / `Common events (marriage, birth, adoption, divorce, death in household, status changes)` / `Lost health insurance through your job` / `Lost Medi-Cal coverage` / `Moved to California from another state, or moved within California and plan options changed` / `Were released from jail or prison`.

The live page's thirteen events are: Got married or entered a domestic partnership; Had a baby, adopted a child or began foster care; Got divorced or legally separated; Had a death in the household that affects coverage; Moved to California from another state; Moved within California and plan options changed; Gained citizenship, national status or lawful presence; Lost insurance after military service; Lost insurance tied to military service; Experienced domestic abuse or spousal abandonment; Were released from jail or prison; Are a federally recognized American Indian or Alaska Native member; Lost financial help after an income change; Lost financial help after a household change.

The two most consequential additions, because a reader would not think to look for them:

- **Lost financial help after an income change** and **lost financial help after a household change** — these open an SEP on their own, not only a change in the underlying job-based coverage.
- **Are a federally recognized American Indian or Alaska Native member** — an eligibility category, not a change event, that the source nonetheless lists as qualifying.

Recommended corrected table: expand to the full thirteen rows. If the five-row summary is kept for readability, retitle it "Selected qualifying events (full list on the live page)" so it does not read as exhaustive.

## Claims I could NOT verify and why

**External corroboration for claim 9 could not be completed from this environment.** I attempted DHCS (`dhcs.ca.gov/medicaid-eligibility` and `/immigration-status`), HealthCare.gov, CMS.gov, Medicaid.gov and KFF. Every attempt failed — 404s on the CMS and HealthCare.gov deep links, a 403 from Medicaid.gov, an empty body from DHCS, and aborted connections from KFF and HealthCare.gov. The claim is therefore CONFIRMED against the Covered California source page only. The figures are consistent with the well-known Budget Act 2025 schedule (adults 19+ restricted from Jan. 1, 2026) and the DACA Aug. 2025 federal action, but I did not verify them against a second source and am not asserting that I did.

No claim in this scope was unverifiable against the primary source.

## New information the library missed

- **Per-event coverage start rules.** The live SEP table's third column is event-specific and the library does not reproduce it. Incarceration release, for example: "Coverage typically starts the first of the month after your release date or plan selection, **whichever is later**" and "Coverage start options may vary; Covered California will show your date after you apply." The move row says "You may be able to report your move **before it happens**."
- **Pre-event application.** The page states: "For some major life changes — like losing job-based coverage or moving — you may be able to apply before the event happens. This can help you avoid a gap in coverage. The application will ask for the date of your life change." This materially changes what a consumer should do after a job loss.
- **COBRA non-qualification, stated explicitly.** "Stopping your COBRA payments does not count as losing coverage and does not open a special-enrollment period." The library covers COBRA exhaustion but should state the inverse too.
- **Pregnancy is not by itself a qualifying event.** "Pregnancy alone may not qualify you for a Covered California health insurance plan outside open enrollment." Worth stating plainly, since consumers commonly assume otherwise.
- **Applying anyway.** "Apply anyway. Covered California will review your application for Covered California plans, Medi-Cal, and other programs." The library does not convey that submitting outside an SEP is non-punitive.
- **Molina's 2027 market exit is narrower than "some regions".** The live page specifies **northeast Los Angeles County** and **Orange County**. The library records the same detail, but the headline and the July 21, 2026 press release both generalise it to "some regions" — worth reconciling so the two do not disagree.