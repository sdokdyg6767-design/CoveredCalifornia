# Verification: account and support

- **Date:** 2026-10-13
- **Library snapshot audited:** 124 files, retrieved 2026-10-13
- **Method:** live re-fetch of each source page + independent corroboration
- **Scope owner:** `10-verification-audit/verify-account-and-support.md`

## Verdict

| Scope | Claims checked | Confirmed | Discrepancies | Unverifiable |
| --- | --- | --- | --- | --- |
| Account and support (claims 14-22) | 9 | 8 | 1 (minor) | 0 |

Scope B holds up under adversarial checking. Every deadline in the assigned list — the 90-day appeal window, the 14-day cancellation notice, the 30-day auto-reenrolment, the 30-day reporting window, the Jan 31 1095-A date, the 10-business-day behavioral health appointment — was checked against the live page and is correct. No transposed digits, no stale years. The single discrepancy is a terminology conflation in `ombuds-office.md`, and it does not change any actionable number.

A supplementary pass over the 47 phone numbers and 15 phone numbers in Scope B's high-risk tables (`insurance-company-contacts.md`, `get-help.md`, `consumer-protection.md`) found no transcription errors.

## Claim-by-claim results

| # | Claim | Library says | Live site says | Verdict | Source checked |
| --- | --- | --- | --- | --- | --- |
| 14 | Appeal filed 90 days after the decision is mailed; hearing + decision up to 90 days; complaint response 30 business days | Identical | "You generally must file your appeal within 90 days of the date Covered California mailed your eligibility decision."; "For most appeals, the hearing process and decision take up to 90 days from the date we get a valid appeal request."; "Covered California will review your complaint and respond within 30 business days." | CONFIRMED | /account/file-an-appeal |
| 15 | Cancellation: 14 days notice, ends last day of the month (June 30 -> submit June 16), no retroactive cancellation | Identical | "Submit your cancellation request at least 14 days in advance. To end insurance on June 30, for example, you would need to submit by June 16."; "End your plan on the last day of the month."; "Generally, you can't cancel insurance for months that have already passed." | CONFIRMED | /account/cancel |
| 16 | Renewal opens October; no action = auto-reenrolled within 30 days of the deadline | Identical | "Renewal opens in October."; "If you don't do anything, you'll be re-enrolled into your current plan within 30 days of the renewal deadline, using the most recent household and income information on file." | CONFIRMED | /account/renew |
| 17 | Report changes: 30 days Covered California vs 10 days Medi-Cal | Identical | /account: "Update your information within 30 days of the income change." / "Update your information within 30 days of the job or income change." /covered California enrollees "update your information within 30 days". /coverage-basics/medi-cal: "You must report any household changes within 10 days to your local county social services office." | CONFIRMED | /account and /coverage-basics/medi-cal |
| 18 | Medicare transition: report eligibility within 30 days, cancel at least 14 days before, 7-month initial window, Part B penalty 10% | Identical | "Report your Medicare eligibility to Covered California within 30 days."; "You must cancel your plan at least 14 days before you want it to end"; "seven-month initial enrollment period ... starts three months before your birthday month and ends three months after"; "a lifetime penalty that increases your monthly premium by 10 percent or more" | CONFIRMED | /account/renew/moving-to-medicare |
| 19 | 1095-A issued by Jan 31; not issued for Medi-Cal, catastrophic, or CCSB | Identical | "Covered California will send you IRS Form 1095-A by Jan. 31."; "You will not receive an IRS Form 1095-A if you had: Medi-Cal / A minimum coverage plan, also known as a catastrophic plan / Employer health insurance through Covered California for Small Business (CCSB)" | CONFIRMED | /account/tax-forms |
| 20 | Preventive care free in-network pre-deductible; behavioral health appointment within 10 business days | Identical | "They're free when you see an in-network care provider and schedule the visit as preventive care, even if you haven't met your deductible for the year."; "Health plans must also offer members a return behavioral health appointment within 10 business days after referral or initial visit." | CONFIRMED | /account/using-your-plan/free-preventive-care-for-adults and /account/using-your-plan/mental-health |
| 21 | Service Center (800) 300-1506, Mon-Fri 8 a.m.-6 p.m., weekends closed, TTY (888) 889-4500, 14 language lines | Identical | Footer: "SERVICE CENTER HOURS Monday to Friday: 8 a.m. to 6 p.m. Saturday and Sunday: Closed"; "TTY (888) 889-4500"; phone list contains 14 non-TTY numbers plus the TTY line | CONFIRMED | /get-help |
| 22 | Ombuds: complaint filed more than 30 days ago and unresolved; case ID 10 digits starting 5 or 1; Health Consumer Alliance a network of 10 programs; HCA hours Mon-Fri 9 a.m.-5 p.m. | Identical | "you filed a Covered California complaint more than 30 days ago and haven't received an update."; "Your case ID number: a 10-digit number associated with your account, starting with a 5 or 1."; "The HCA is a network of 10 consumer-assistance programs operated by community-based legal services."; "(888) 804-3536 Monday through Friday, 9 a.m. to 5 p.m." | CONFIRMED (numbers) / see discrepancy 1 for one label | /ombuds-office |

## Discrepancies requiring correction

### 1. `05-help-support-and-rights/ombuds-office.md` - conflates two distinct identifiers

Library file: `05-help-support-and-rights/ombuds-office.md`, lines 20-22 (Key Facts) and lines 41-42 (The Contact Form).

Exact current text:

> **Required before submitting the Ombuds Contact Form:**
> - A 10-digit number associated with your account, starting with a 5 or 1.
> - The case number provided by the service center when they assisted with your case.

What the source says: the page lists **two separately named** items:

> Your **case ID number**: a 10-digit number associated with your account, starting with a 5 or 1.
> Your **reference number**: provided by the service center when they assisted with your case.

The library relabels the service-center-supplied "reference number" as the "case number". That is the same word the site uses for the 10-digit identifier, so a reader following `ombuds-office.md` would reasonably believe one field satisfies both descriptions. On the live page they are two different values.

Corrected wording:

> **Required before submitting the Ombuds Contact Form:**
> - Your case ID number — a 10-digit number associated with your account, starting with a 5 or 1.
> - Your reference number — provided by the service center when they assisted with your case.

Severity: low. All numeric content is correct and unchanged; only the label on the second item needs to match the source.

### 2. `05-help-support-and-rights/insurance-company-contacts.md` - one note attributed to the wrong page

Library file: `05-help-support-and-rights/insurance-company-contacts.md`, line 58.

Exact current text:

> **Vision plan cancellation note:** to cancel a vision plan you must call the **vision insurance company directly** — Covered California does not process it.

This sentence does not appear on `/insurance-company-contacts`. A direct check of the live page returns no match for "call your vision insurance company". The statement is **true on the site** — it appears verbatim on `/account/cancel` ("To cancel your vision plan, call your vision insurance company directly") — but it is filed inside a record whose header declares `Source URL: https://www.coveredca.com/insurance-company-contacts`, with no cross-reference.

Recommended fix: either move the note to `04-account-and-managing-coverage/cancel.md` (which already carries it correctly) or annotate it inline as sourced from `/account/cancel`.

Severity: low. No factual error, but it misattributes a claim to a page that does not make it. Flagged because the same file handles cross-page sourcing honestly elsewhere — see the note below.

## Claims I could NOT verify and why

**None within scope.** All nine assigned claims were checked directly against the live source page and all nine resolved.

Two false leads I chased and rejected, recorded so they are not re-litigated:

- **Four "missing" phone numbers on `/insurance-company-contacts`** — (844) 332-8384 "New Customers", (855) 777-6782 "Existing Customers / CCSB Service Center", (877) 453-9198 "Agent Service Center", (855) 324-3147 "CEC/PBE Helpline" appear in the page payload but are absent from `insurance-company-contacts.md`. I tested each against the unrelated `/glossary` page: **all four are present there too**, so they are site-wide footer content, not insurance-company-contacts content. The library correctly excluded them. Not a discrepancy.
- **"01 Health Insurance Companies / 02 Dental Insurance Companies / 03 Vision Insurance Companies"** reads at first like a company count that would contradict the library's "2 vision companies". It is the "On this page" jump-nav list with ordinal numbering. The rendered Vision section lists exactly EyeMed and VSP. Library correct. Not a discrepancy.
- **Two library phone numbers absent from the contacts page** — (800) 927-4357 (CDI) and (888) 466-2219 (DMHC). Both are real and both are sourced from `/ombuds-office`. The library states this explicitly ("The escalation path published elsewhere on the site is"), which is correct practice, not an error.

## New information the library missed

- **`/ombuds-office` publishes a large amount of regulator contact detail that `ombuds-office.md` does not record.** The live page names and numbers: **DMHC Help Center (888) 466-2219** (file a complaint after 30 days in your carrier's grievance system), **California Department of Insurance (800) 927-4357** plus its remit (IMR, licensing, insurance fraud), **DHCS Ombudsman Office (888) 452-8609, Monday through Friday, 8 a.m. to 5 p.m.**, email **mmcdombudsmanoffice@dhcs.ca.gov**, **CDCR** prison visitation/facility contacts, **Adult Protective Services (833) 401-0832** (7 days, 24 hours, enter your five-digit ZIP), and the **California Department of Aging Long-Term Care Ombudsman / Statewide CRISISline (800) 231-4024** (24 hours, 7 days). `ombuds-office.md` lists only two of these. This is the single largest content gap in Scope B.
- **DHCS Ombudsman Office hours (Mon-Fri 8 a.m.-5 p.m.) are distinct from HCA hours (Mon-Fri 9 a.m.-5 p.m.).** The library records only the HCA hours. Both are on the same page and are easy to conflate.
- **`/insurance-company-contacts` carries the Molina 2027 regional-withdrawal notice in its own right**, not only on the Molina carrier page. `insurance-company-contacts.md` records this correctly — worth noting because it means the notice has two independent live sources, so the library's Molina claim is doubly supported.
- **DHCS can assist with "Access-to-care issues."** Listed on `/ombuds-office` as a Medi-Cal concern DHCS handles; not recorded in the library's DHCS bullet list.
- **`/consumer-protection` fraud contacts verified clean.** (888) 217-9309, TTY (888) 889-4500, fax (916) 228-8915, StopFraud@covered.ca.gov, 1601 Exposition Blvd. Sacramento CA 95815, $25,000 ACA fine, (800) 927-HELP, (800) 822-6222, stopmedicalfraud@dhcs.ca.gov, (800) MEDICARE / (800) 633-4227, (877) FTC-HELP, (877) ID-THEFT — every one present on the live page, zero errors.
- **`/account/using-your-plan/enrollee-programs` verified clean.** Beyond Covered: two programs, up to $1,000 CalKIDS, grocery eligibility at or below 250% FPL with a chronic health condition, California-born children under 18 months, FORWARD contacts you by email/text/phone, you cannot apply yourself, spots limited first-come-first-served, voluntary, launched 2025 "as long as funding is available". All present; zero errors.
- **Library files for billing, cancel, renew, appeal, tax forms, Medicare transition, get-help, find-an-enroller and enrollee-programs are all clean** against their declared source URLs. `find-an-enroller.md` is appropriately explicit that the locator is client-side and that listings are not captured offline — good practice worth preserving elsewhere.