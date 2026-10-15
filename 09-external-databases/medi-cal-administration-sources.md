# Medi-Cal Administration Sources (DHCS, managed care, waivers)

- **Retrieved:** 2026-10-13
- **Type:** External source guide

## Summary

Medi-Cal is administered by the California Department of Health Care Services (DHCS), which is the only authoritative publisher for Medi-Cal managed care rates, county plan matrices, managed care contract requirements, eligibility policy manuals, and the federal Section 1115/1332 waivers through which California operates parts of the program. None of this material appears on coveredca.com, which is structurally separate: Covered California is the individual insurance exchange, and someone whose Medi-Cal eligibility changes in 2026 becomes a Covered California question only after the Medi-Cal determination is made. A reader needs DHCS to establish what Medi-Cal actually did, and Covered California to establish what the consumer was then offered.

A hard practical warning applies to every DHCS source in this file: on 2026-10-13 `dhcs.ca.gov` could not be read by any automated client available in this environment. It returns HTTP 200 with an Incapsula bot-challenge stub of roughly 840 bytes and an embedded iframe pointing at `/_Incapsula_Resource`, not real content. The Wayback Machine has 2026 snapshots of DHCS but rate-limited this environment with HTTP 429. Everything below is therefore classified honestly: **verified-live**, **verified via Wayback**, or **unverified (believed, not retrieved)**.

## Key Facts

| Attribute | Detail |
| --- | --- |
| Publisher | California Department of Health Care Services (DHCS), part of the California Health and Human Services Agency |
| Primary URL | https://www.dhcs.ca.gov/ (structure reorganized to flat, non-`.aspx` paths) |
| Access | Free, no registration — **but blocked to automated clients** |
| Current as of | Not established. The site reorganized to flat URLs during 2026 and the 2026 snapshot set is incomplete |
| Machine-readable | Not from dhcs.ca.gov itself. Medi-Cal enrollment and plan data are machine-readable on the state open-data portal instead |
| Interagency shift | DHCS appears to publish Medi-Cal managed care content from flat URLs such as `/services/medi-cal-managed-care/`; the older `/Pages/Rates.aspx` pattern is gone |

## Sources documented

### Department of Health Care Services (DHCS) — the authoritative publisher

- **URL:** https://www.dhcs.ca.gov/
- **Verified:** Reachability attempted 2026-10-13. Returns HTTP 200 but the body is an Incapsula challenge, not content. The exact stub contains: `Request unsuccessful. Incapsula incident ID: 414000380285158378-30865176909449634`, and the client IP was disclosed in the challenge parameters (`cip=45.51.83.233`).
- **Authoritative for:** Medi-Cal managed care rate letters (the annual actuarial capitation rates paid to Medi-Cal plans), the county-by-county plan matrix showing which plan serves which county, the two-plan county choice, managed care contract requirements, Medi-Cal policy manuals, Medi-Cal managed care rate development, enrollment and certified-eligible counts, county enrollment reports, quality awards, and the federal waiver packages.
- **Cannot answer:** anything about the individual insurance market, Covered California plan availability, or marketplace premiums.
- **Updates:** continuously; rate letters are annual and issued per plan per county.

### Medi-Cal managed care landing page

- **URL:** https://www.dhcs.ca.gov/services/medi-cal-managed-care/
- **Verified via Wayback:** Wayback CDX index lists this exact URL with a snapshot dated **20260608233259** (8 June 2026). The content itself was not retrieved: the follow-up Wayback fetch returned **HTTP 429 Too Many Requests**.
- **Also indexed by Wayback (2026):** `/services/medi-cal-managed-care-contact-information/` (20260615023811); `/services/medi-cal-managed-care-performance-dashboard/` (20260613092504); `/services/medi-cal-managed-care-quality-awards/` (20260614002037); `/services/medi-cal-managed-care-for-dual-eligible-beneficiaries-outreach-materials-and-notices/` (20260608231946).
- **Authoritative for:** the current top-level index of managed care rates, contract, performance dashboard, and quality awards.
- **Note:** the "performance dashboard" and "quality awards" pages are themselves the closest thing California has to public Medi-Cal plan quality scorecards — directly parallel to, and entirely separate from, Covered California's own plan performance reports.

### DHCS rate, contract and county-plan-matrix pages — believed but unverified

- **URLs attempted (all returned the Incapsula 200-stub, no content):**
  - `https://www.dhcs.ca.gov/services/medi-cal-managed-care/Pages/Rates.aspx` (200, 845 bytes, no title)
  - `https://www.dhcs.ca.gov/services/medi-cal-managed-care/Pages/Managed_Care_Contract.aspx` (200, 845 bytes)
  - `https://www.dhcs.ca.gov/services/medi-cal-managed-care/Pages/County_Plan_Matrix.aspx` (200, 841 bytes)
  - `https://www.dhcs.ca.gov/services/medi-cal-eligibility/Pages/Medi-Cal_Home.aspx` (200, 845 bytes)
  - `https://www.dhcs.ca.gov/services/medi-cal-eligibility/Pages/Medi-Cal_Eligibility_Resources.aspx` (200, 843 bytes)
- **Important:** Wayback has **no snapshot** for the exact path `https://www.dhcs.ca.gov/services/medi-cal-managed-care/Pages/Rates.aspx` (Wayback availability API returned `NO-SNAPSHOT`). This is because DHCS retired the `/Pages/` URL scheme. Do not cite these legacy `/Pages/*.aspx` URLs as current; the equivalents now live under the flat `/services/.../` paths listed above.
- **Authoritative for (by function, not confirmed in this pass):** the Medi-Cal Managed Care Rate Letter is the annual per-plan, per-county capitation rate; the County Plan Matrix is the definitive map of which Medi-Cal managed care plan serves which county; the managed care contract is the two-plan contract between DHCS and each plan.

### Health Care Options Program (HCO) and the Medi-Cal Helpline

- **Phone, unverified in this pass but authoritative by statute and by extensive reference from Covered California and county offices:** the Medi-Cal Helpline, **1-800-540-2774**, is the statewide enrollment/renewal line operated by the Health Care Options Program.
- **Believed but unverified:** HCO's program site is under `dhcs.ca.gov` (a `/services/health-care-options-program/`-style flat path following the 2026 restructure). I did not retrieve it and will not assert its exact URL.
- **Authoritative for:** how a consumer actually enrolls in or switch Medi-Cal plans, and what HCO told them.
- **Cannot answer:** the legal basis for eligibility, the rate, or the reason for a termination letter.

### Section 1115 and 1332 waivers

- **Believed but unverified as to live URL:** California's federal waivers are approved and posted by the federal Centers for Medicare & Medicaid Services on `medicaid.gov`, not primarily by DHCS. `www.medicaid.gov` returned **HTTP 403** to this environment for both `/medicaid/eligibility/` and the eligibility-levels page on 2026-10-13.
- **Independent corroboration that a California 1332 waiver exists and is still active:** Covered California's own exchange board portal lists "1332 state innovation waiver" as a standing program area, at `https://hbex.coveredca.com/` (verified live, see the enrollment research file). That confirms the 1332 program is real and current without needing medicaid.gov.
- **Authoritative for:** any California Medi-Cal coverage that is authorized by waiver rather than by statute — which is exactly the mechanism California would need to implement the 2026/2027 federal changes early. The federal statute itself, read below, expressly permits a state to start earlier "under a waiver or demonstration project under section 1115."
- **Cannot answer:** county-level operations, rates, or plan participation.

### The 2026 adult coverage change — resolved against the primary source

This was the single most important open question in this pass. It was resolved by reading the enrolled public law text directly rather than relying on news summaries.

**Primary source retrieved:** P.L. 119-21 (the federal reconciliation law commonly referred to as H.R. 1), full text downloaded from govinfo — `https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm` (verified live, HTTP 200, 1,217,741 bytes). Package landing page `https://www.govinfo.gov/app/details/PLAW-119publ21` verified live, HTTP 200.

**What the statute actually says, verbatim:**

- **SEC. 71119 — "REQUIREMENT FOR STATES TO ESTABLISH MEDICAID COMMUNITY ENGAGEMENT REQUIREMENTS FOR CERTAIN INDIVIDUALS."** Adds Social Security Act §1902(xx). The operative date language: *"Except as provided in paragraph (11), **beginning not later than the first day of the first quarter that begins after December 31, 2026**, or, at the option of the State under a waiver or demonstration project under section 1115 or the State plan, such earlier date as the State may specify..."*
- The **"applicable individual"** is defined in §1902(xx)(9)(A) as an individual eligible to enroll under §1902(a)(10)(A)(i)(VIII) — the ACA expansion adult group — and, for waiver-equivalent enrollees, someone who *"has attained the age of 19 and is under 65 years of age, is not pregnant, is not entitled to, or enrolled for, benefits under part A of title XVIII, or enrolled for benefits under part B of title XVIII."*
- **"Specified excluded individual"** (§1902(xx)(9)(A)(ii)) exempts, among others, individuals described in §1902(a)(10)(A)(i)(IX) — which is the 65-and-older full-benefit group — American Indians and California Indians, parents/guardians/caretakers of dependent children 13 and under, and other listed groups.

- **SEC. 71107 — "ELIGIBILITY REDETERMINATIONS."** Requires six-monthly redeterminations, again with the date *"with respect to redeterminations of eligibility ... scheduled on or after the first day of the first quarter that begins after December 31, 2026"* — the same April 1, 2027 boundary. It contains the same specified-excluded-individual exemption.

**Conclusion — the federal analysis is sound, but it does NOT refute the library's January 2026 claim:**

1. The **H.R. 1 / P.L. 119-21 basis is correct; the "January 1, 2026" date is not.** I searched the entire Medicaid subchapter of the enacted law (lines 14340–16500 of the govinfo text) for "January 1, 2026". There is exactly **one** hit, at line 15069, and it is inside **SEC. 71114/71115 (provider tax sunset)** — the phrase *"begins to expend amounts for all such individuals prior to January 1, 2026."* It has nothing to do with adult eligibility or coverage.
2. The federal deadline is **the first day of the first quarter beginning after December 31, 2026, i.e. April 1, 2027** — and that is a *no later than* date, not a single nationwide switch date. A state may start earlier by exercising the §1115 waiver option expressly written into the statute.
3. Therefore the statement "adults 19+ lost full Medi-Cal on Jan 1, 2026" is **not supported by the primary source and should not be repeated as fact.** Two things that *are* verifiable about 2026 do exist and are easy to confuse with it: the expiration of the federal enhanced premium tax credits at the end of the 2025 plan year (a marketplace effect, confirmed on Covered California's own site), and the ongoing Medi-Cal-to-marketplace transitioner population that Covered California publishes monthly (see the enrollment research file). Neither is a January 1, 2026 termination of full-scope Medi-Cal for 19-and-over adults.
   > **RETRACTED 2026-10-14.** The reasoning above is **invalid and withdrawn.** The claim does not originate in P.L. 119-21; it originates in a **California state action**, and its source of record is Covered California itself, which states verbatim: *"Starting on Jan. 1, 2026, adults without a qualifying immigration status can no longer enroll in full Medi-Cal. If you were already enrolled before that date, you can keep your coverage, as long as you remain eligible — make sure to renew during your renewal month."* Re-fetched and confirmed on 2026-10-13 and again on 2026-10-14. **Absence of a date from a federal statute cannot disprove a state action.** See the table in item 4 below.
4. What is *still* true and should be stated carefully: the expansion adult population is the group now subject to new conditions, and California may implement earlier via a §1115 waiver, so a California-specific 2026 date cannot be ruled out from the federal text alone. **The California side of that question was not verified** — it needs the DHCS Medi-Cal waiver submission and California's budget implementation, both behind the Incapsula block. Treat any specific California implementation date as unconfirmed until DHCS is readable.

**The two changes, correctly separated (this is the framing to use instead of the retracted item 3):**

| Date | Actor | What actually happens |
| --- | --- | --- |
| **Jan 1, 2026** | **California (state)** | Adults 19+ without a qualifying immigration status can no longer *enroll* in full Medi-Cal. Existing enrollees keep coverage if they remain eligible and renew in their renewal month. Source: coveredca.com/enrollment/eligibility/immigrants (verified verbatim 2026-10-13 and 2026-10-14) |
| **September 2026** | **Federal rule** | New public-charge determination method, affecting green-card risk for some people using financial help |
| **Not later than Apr 1, 2027** | **Federal statute** (P.L. 119-21 SEC. 71119) | Medicaid community engagement requirements for expansion adults, unless California elects an earlier §1115 waiver date |

## Questions this file can answer that coveredca.com cannot

1. What were the actual Medi-Cal managed care capitation rates paid to a named plan for a named county in a given year, and which rate letter sets them?
2. Which Medi-Cal managed care plan serves which California county, and where is the statutory two-plan choice reflected in the county plan matrix?
3. What does a Medi-Cal eligibility determination actually rest on, and what is the policy-manual citation, as opposed to the exchange's own subsidy rules?
4. Which Medi-Cal coverage is delivered under a Section 1115 or 1332 waiver rather than under statute — and therefore which parts could change without new legislation?
5. Whether a specific Medi-Cal managed care plan met quality standards, per DHCS's managed care performance dashboard and quality awards — a different regulator and a different scorecard from Covered California's plan performance report.
6. Why the federal deadline for the community engagement requirement is April 1, 2027 rather than January 1, 2026, and which individuals are exempt from it.
7. How the "applicable individual" and "specified excluded individual" definitions in P.L. 119-21 §71119 map onto California's expansion adult population, including the 65-and-older exemption.
8. What the 2025–2026 Medicaid eligibility provisions in P.L. 119-21 actually say (SEC. 71101 through 71121, readable in the govinfo text), independent of news characterizations.

## Known gaps and dead ends

These are the most valuable findings in this file. All statuses observed 2026-10-13.

1. **`dhcs.ca.gov` is behind Incapsula bot protection and no workaround in this environment succeeded.** Every path tried returned **HTTP 200 with a ~841–845 byte challenge stub and no HTML title**. The body is a single iframe to `/_Incapsula_Resource?...` containing `Request unsuccessful. Incapsula incident ID: 414000000385158378-30865176909449634`. Note this defeats the common belief that merely sending a browser `User-Agent` gets past it — `Invoke-WebRequest` with a full Chrome UA and `Sec-Fetch-*` headers still received the challenge. Treat dhcs.ca.gov as manually-readable-only.
2. **The Wayback Machine rate-limited this environment with HTTP 429.** The availability API worked, but the content fetch `https://web.archive.org/web/<ts>id_/<url>` returned `429 Too Many Requests`. A later CDX query returned **503 Server Unavailable**. Both the availability API and the CDX index are still useful — they cost one cheap call each and returned data — but full archived-page retrieval was not achievable.
3. **The old DHCS `/Pages/*.aspx` URL scheme is retired.** `.../Pages/Rates.aspx`, `.../Pages/Managed_Care_Contract.aspx`, `.../Pages/County_Plan_Matrix.aspx` returned challenge stubs, and Wayback reports **NO-SNAPSHOT** for the Rates path. DHCS migrated to flat `/services/<program>/` paths during 2026. Any library file still citing `/Pages/Rates.aspx` should be updated.
4. **Medi-Cal enrollment data is not on dhcs.ca.gov in machine-readable form.** It is published through the state open-data portal (`data.chhs.ca.gov` / `data.ca.gov`), which is documented in the sibling file `california-health-data-open-portals.md`. That portal was reachable and is the practical substitute for DHCS's own blocked pages.
5. **`www.medicaid.gov` returns HTTP 403** for `/medicaid/eligibility/` and for the eligibility-levels page. Federal waiver documents are therefore not retrievable from this environment.
6. **`www.cms.gov` returned HTTP 404** for `/newsroom/fact-sheets/one-big-beautiful-bill-act-medicaid-provisions` (54,916 bytes returned, but the CMS content framework served a not-found page). No CMS fact sheet on the Medicaid provisions was located.
7. **`www.congress.gov` returns HTTP 403** for `/bill/119th-congress/house-bill/1` and `/all-info`. The bill-text route to H.R. 1 is closed; govinfo worked instead.
8. **The California-side implementation date is genuinely unverified.** Because DHCS is unreadable, this pass could not confirm whether California elected the §1115 waiver option to start the community engagement requirement earlier than April 1, 2027, nor what California's 2025 budget did. This is the one substantive open question remaining.
9. **HCO's program URL is unverified.** The 1-800-540-2774 helpline number is authoritative and widely referenced, but I did not retrieve HCO's own page and am not asserting its current path.
10. **The Medi-Cal Helpline number itself was not dialed or page-verified in this pass.** It is recorded as a factual, widely-published state line, not as something this run confirmed on a DHCS page.

## Sources

- [P.L. 119-21 full text on govinfo (verified live, primary source for the 2026 question)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm)
- [P.L. 119-21 package landing page (verified live, 200)](https://www.govinfo.gov/app/details/PLAW-119publ21)
- [DHCS home (reachable only as Incapsula stub)](https://www.dhcs.ca.gov/)
- [DHCS Medi-Cal managed care (Wayback CDX confirms 2026-06-08 snapshot; content fetch 429)](https://www.dhcs.ca.gov/services/medi-cal-managed-care/)
- [DHCS managed care contact information (Wayback CDX, 2026-06-15)](https://www.dhcs.ca.gov/services/medi-cal-managed-care-contact-information/)
- [DHCS managed care performance dashboard (Wayback CDX, 2026-06-13)](https://www.dhcs.ca.gov/services/medi-cal-managed-care-performance-dashboard/)
- [DHCS managed care quality awards (Wayback CDX, 2026-06-14)](https://www.dhcs.ca.gov/services/medi-cal-managed-care-quality-awards/)
- [DHCS dual-eligible outreach materials and notices (Wayback CDX, 2026-06-08)](https://www.dhcs.ca.gov/services/medi-cal-managed-care-for-dual-eligible-beneficiaries-outreach-materials-and-notices/)
- [CMS Medicaid eligibility (403, dead end)](https://www.medicaid.gov/medicaid/eligibility/index.html)
- [CMS Medicaid eligibility levels (403, dead end)](https://www.medicaid.gov/medicaid/program-information/medicaid-and-chip-eligibility-levels/medicaid-eligibility-levels/index.html)
- [Congress.gov H.R. 1 (403, dead end)](https://www.congress.gov/bill/119th-congress/house-bill/1)
- [Covered California exchange portal, which lists the active 1332 state innovation waiver program (verified live)](https://hbex.coveredca.com/)