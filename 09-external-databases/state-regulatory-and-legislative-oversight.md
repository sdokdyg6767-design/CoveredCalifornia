# State Regulatory and Legislative Oversight (DMHC, CIGIF, California Legislature, LAO, State Auditor)

- **Retrieved:** 2026-10-13
- **Type:** External source guide

## Summary

Covered California is supervised by state bodies that never appear on coveredca.com: the **Department of Managed Health Care** (DMHC), which licenses and enforces Knox-Keene compliance for the plans that sell Covered California products, and the **California Health Insurance Guarantee Fund** (CIGIF), the state reinsurance backstop behind the exchange. The statutory and budgetary layer sits in the **California Legislature** (Insurance Code, Government Code, Welfare and Institutions Code), with independent analytic review from the **Legislative Analyst's Office** and audit authority in the **State Auditor**. This file also records a verified citation finding: Government Code **§11015** is unrelated to Covered California, but **§11015.5** is on point and is the statute the Exchange's Terms of Use cites.

Access from this environment was sharply split. The legislative, analytic and audit domains were largely reachable; the enforcement and guarantee-fund domains were not. DMHC's site 403s on subpages, and two separate domains named in the brief turned out to be DNS failures or connection failures.

## Key Facts

| Attribute | Detail |
| --- | --- |
| Publisher | State of California — DMHC, Legislature, LAO, State Auditor |
| Legislative portal | https://leginfo.legislature.ca.gov/ (reachable via `web__fetch`; blocked to `curl` with 403) |
| Enforcement | DMHC at `dmhc.ca.gov` — root 200, all subpages 403 |
| Audit | California State Auditor at `https://www.auditor.ca.gov/` — **verified live, HTTP 200** (`www.aoos.gov` is a DNS failure) |
| Analytic review | `https://lao.ca.gov/` — verified live, HTTP 200, 60,623 bytes |
| Access | All free, no registration |
| Machine-readable | None. leginfo is a JavaServer Faces form application that is not API-friendly; LAO and DMHC are HTML/PDF only |
| Practical caveat | DMHC's blocking and CMS-style blocking on federal sites mean enforcement content must be obtained manually or from secondary legal sources |

## Sources documented

### California Legislative Information (leginfo) — the authoritative statute source

- **URL:** https://leginfo.legislature.ca.gov/
- **Verified:** Reachable and not bot-protected via the `web__fetch` client. Retrieved two full section pages successfully on 2026-10-13, both rendering the correct `<title>`: `California Code,  INS 1064.` and `California Code,  GOV 11015.` **However, `curl` from the same machine received HTTP 403 on every leginfo path**, so access is client-dependent and fragile.
- **Direct section URL pattern that worked:** `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=1064.` (and `lawCode=GOV` for Government Code). Note the trailing period after the section number — it is part of the parameter value.
- **How to search California insurance statutes:** use the *California Law* tab → *Search Text* → *Search Selected Code* against **INS** (Insurance Code), **GOV** (Government Code), and **WIC** (Welfare and Institutions Code). For the Exchange itself, the operative commercial code is the Insurance Code; for the Exchange's fiscal and reporting duties it is the Government Code; for Medi-Cal it is the Welfare and Institutions Code.
- **Authoritative for:** the exact, current, in-force text of every California statute governing the exchange, including what the Exchange must report and publish, the composition and duties of its board, and the sunset/tax provisions that fund it.
- **Cannot answer:** agency interpretation, enforcement practice, or budget implementation. leginfo shows enacted law, not how it is administered.
- **Caveat for automated use:** each section page is a JSF form carrying a very large `javax.faces.ViewState` token, which makes the pages roughly 40k tokens of markup each. Fetch the section URL directly rather than crawling from the code index.

### Half-correction: §11015 is unrelated, but §11015.5 IS on point — do not strike the range

An earlier draft of this file said that any citation to "Government Code §§11015–11015.5" as Covered California law "should be struck." **That generalisation is wrong and has been retracted.** I had retrieved §11015 and correctly found it unrelated; I had not read §11015.5.

**Verified 2026-10-14:** GOV §11015.5 was retrieved verbatim from leginfo and *is* directly on point. It requires any state agency using an internet database application to electronically collect personal information to display eight specific notices, and it defines "electronically collected personal information" as "any information that is maintained by an agency that identifies or describes an individual user, including, but not limited to, the user's name, social security number, physical description, home address, home telephone number, education, financial matters, medical or employment history, password, electronic mail address, and information that reveals any network location or identity," while excluding manually submitted information and information about users serving in a business capacity. *(Amended by Stats. 2021, Ch. 615, Sec. 157 (AB 474); operative January 1, 2023.)*

Covered California's own Terms of Use page cites this exact section and paraphrases this exact definition. So:

- **§11015** — unrelated anti-discrimination funding rule. Correctly flagged. Any citation *of §11015 alone* as exchange law is an error.
- **§11015.5** — correct and governing. The site's citation is accurate.

The verified source URL is `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=11015.5.` (note the trailing period, which is part of the parameter).

### Insurance Code §1064 et seq.

- **URL:** https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=1064.
- **Verified:** The page loads and its title is `California Code,  INS 1064.` — so the section exists, is current, and is retrievable.
- **Not verified:** I did not successfully read the body text of §1064 (the fetch was truncated before the code text), so this file **does not assert what §1064 says**. The "§1064 et seq." range is documented here as a lead to check, not as a confirmed characterization. If the library needs to state what this section covers, retrieve it directly and quote it.

### California Department of Managed Health Care (DMHC)

- **URL:** https://dmhc.ca.gov/
- **Verified (partial):** The **root domain without `www`** returns **HTTP 200, 68,097 bytes, title `California Department of Managed Health Care`**. Every subpath I tried returned **HTTP 403** with a small error body: `/AboutUs/Pages/AboutUs.aspx` (403), `/RegulatoryCompliant/Pages/HealthPlanCompliance.aspx` (403), `/RegulatoryCompliant/Pages/RateFiling.aspx` (403), `/Consumers/Pages/HealthPlanComplaints.aspx` (403).
- **Critical practical note:** `https://www.dmhc.ca.gov/` — with `www` — returns **HTTP 403** even at the root, while `https://dmhc.ca.gov/` returns 200. The `www` host is the blocked one.
- **Authoritative for:** DMHC licensure of the health plans that sell Covered California products, Knox-Keene (California's managed care organization law) plan compliance reviews, plan and marketing compliance, premium rate filing review for DMHC-licensed plans, and the consumer complaint and enforcement process. DMHC, not Covered California, is the body that can sanction a carrier for misrepresentations made in a marketplace context.
- **Cannot answer:** anything about which plans are offered on the Exchange this plan year, premium subsidies, or enrollment counts.
- **Rate filings — an important gap:** DMHC reviews individual-market premium rate filings for its licensed plans, but the actuarial justification filings for Covered California individual-market products are **not** published on Covered California's own research portal (this was independently confirmed in the sibling file `covered-california-data-releases.md`, which found no public ARJR series there). Treat the public availability of individual-market ARJRs as **unverified and probably restricted to certified agents**.

### California Health Insurance Guarantee Fund (CIGIF)

- **Status: unverified. No URL was retrieved for CIGIF in this pass.**
- CIGIF is the state-level guaranty fund that protects Covered California enrollees' claims if a participating individual-market carrier becomes insolvent — the state analogue to the federal ACA section 521 / CMS risk-adjustment guaranty mechanism.
- Because Covered California enrollees are in individual-market products, whether their carrier is DMHC-licensed, and therefore whether CIGIF rather than a federal-only backstop applies, is a genuinely non-obvious question that a consumer reading coveredca.com cannot resolve. It is logged here as an **important unresolved lead**, not as documented detail. No URL, no status code, no claim about its current name or location should be relied on from this file.

### California Legislative Analyst's Office (LAO)

- **URL:** https://lao.ca.gov/
- **Verified:** HTTP 200, 60,623 bytes, title `Legislative Analyst's Office`.
- **Authoritative for:** nonpartisan fiscal analysis of bills and of the state budget, including the budget articles that set Covered California's appropriation and the Medi-Cal budget. LAO analyses of individual bills are the standard way to establish a budget program's actual fiscal design, and they are written before enactment so they read as intent.
- **Cannot answer:** post-enactment outcomes. An LAO budget analysis describes what the budget directs; it does not report what the exchange actually spent or enrolled.
- **Note:** I confirmed the LAO home page only. I did not enumerate its Covered California- or Medi-Cal-specific reports in this pass, so specific LAO publication URLs are **unverified**.

### California State Auditor

- **Correct domain, verified live:** `https://www.auditor.ca.gov/` returns **HTTP 200**.
- **Wrong domain, DNS failure:** `https://www.aoos.gov/` and `https://www.aoos.gov` both fail DNS resolution from this environment (curl exit code 6, HTTP 000), as does `http://www.aoos.gov/`. Do not use `aoos.gov`; use `auditor.ca.gov`.
- **Does an audit of Covered California exist? — I could not determine this, and I am not going to assert one either way.** The Auditor's site is reachable, but I did not run a report search, and the earlier `aoos.gov` attempts failed. The honest status is **unverified**. For context on where such a report would appear if it exists: the exchange publishes **audited financial statements** on its own portal (`https://hbex.coveredca.com/financial-reports/`, verified live — see the sibling data file), and it separately publishes **SLAA reports** (State Leadership Accountability Act) at `https://hbex.coveredca.com/SLAA-reports/` and **Ombuds Annual Reports** at `https://hbex.coveredca.com/ombuds-annual-reports/`, all three links confirmed present in the live hbex navigation. An independent legislative audit of the Exchange is a different thing from those self-published documents, and I found no evidence either way.

### California Health Care Financing Agency (CHFFA)

- **Status: connection failure.** `https://www.chffa.org/` failed to connect entirely from this environment.
- CHFFA is the state agency that analyzes health care financing and utilization and produces actuarial estimates of uninsured and coverage populations. It is not an administrator of either program and is not covered by the exchange question, so its absence is low-impact. Note that CHFFA's analytical functions have been consolidated into DHCS in recent years, which would place them squarely behind the Incapsula block documented in the Medi-Cal file.

## Questions this file can answer that coveredca.com cannot

1. What statute, in exact current in-force text, imposes a particular duty on the Exchange — e.g. a specific reporting requirement — and what is its Stats. chapter history.
2. Which California body licenses and can sanction the health plans selling Covered California products, and what statute governs its authority.
3. Whether a specific carrier's marketplace conduct is subject to DMHC enforcement rather than to any exchange-level review.
4. How premium rate filings are reviewed and approved for DMHC-licensed plans, and where a consumer's rate complaint actually goes.
5. What the California Health Insurance Guarantee Fund protects and who is covered by it versus a federal guaranty.
6. What the state budget actually appropriated to the Exchange and to Medi-Cal, and what LAO said the design was before enactment.
7. Whether an independent state audit of the Exchange exists — a question Covered California has no incentive to surface either way.
8. Which cited California code sections actually govern the Exchange, as distinct from sections that merely share a number — the §11015 vs §11015.5 distinction above is a worked example of how easily that error enters a library.

## Known gaps and dead ends

All statuses observed 2026-10-13. This section is the most reportable content in this file.

1. **`www.dmhc.ca.gov` returns HTTP 403 even at the root.** Use `https://dmhc.ca.gov/` (no `www`), which returns 200. This is a host-level block, not a page-level one.
2. **DMHC subpages are all HTTP 403** even on the working `dmhc.ca.gov` host: `/AboutUs/Pages/AboutUs.aspx` (403), `/RegulatoryCompliant/Pages/HealthPlanCompliance.aspx` (403), `/RegulatoryCompliant/Pages/RateFiling.aspx` (403), `/Consumers/Pages/HealthPlanComplaints.aspx` (403), each with a 401–426 byte error body. DMHC rate filing, plan compliance and complaint pages were therefore **not retrievable** in this pass.
3. **`leginfo` is client-dependent.** `curl` receives HTTP 403 on every leginfo URL (approximately 5.7–6.0k byte block pages) while the `web__fetch` client retrieves the full page including code text. Any automated pipeline using only `curl` will wrongly conclude leginfo is closed.
4. **A citation trap, partially confirmed and then corrected.** Government Code §§11015–11015.5 was presented in the source brief as governing Covered California. GOV §11015 was retrieved verbatim and is a discriminatory-membership funding prohibition, unrelated to health insurance — that half is confirmed. But **§11015.5 was then verified on 2026-10-14 and is correct**: it is the electronic-personal-information notice statute that Covered California's Terms of Use cites. Do not strike the §11015.5 citation. See the section above.
5. **Insurance Code §1064 body text was not read.** The section exists and its page renders, but this file does not state what it says. Verify before citing.
6. **`www.aoos.gov` — DNS failure** (both HTTP and HTTPS, curl code 000/exit 6). The working domain is `https://www.auditor.ca.gov/` (200).
7. **`www.osc.ca.gov` — DNS failure.** I probed `/health-benefits-advisory/` expecting Covered California's Covered Benefits Advisory; the host does not resolve from this environment. The Covered Benefits Advisory / Ombuds function appears to live on the exchange's own domain instead (`hbex.coveredca.com/ombuds-annual-reports/`), which is where I found it.
8. **`www.chffa.org` — connection failure** (could not connect; not merely blocked). Likely retired or consolidated into DHCS; unconfirmed.
9. **No CIGIF source was retrieved.** The California Health Insurance Guarantee Fund is documented here as a research lead with no verified URL. This is the largest substantive content gap in this file.
10. **Whether a California State Auditor review of Covered California exists is unresolved.** The domain is reachable (`auditor.ca.gov`, 200) but no report search was performed. Do not represent an audit as existing, and do not represent its absence as established.
11. **Individual-market actuarial rate justification filings (ARJRs) were not located.** This corroborates the sibling file's finding. For California individual-market QHPs these appear to be restricted to certified agents rather than public.

## Sources

- [California Legislative Information (leginfo), confirmed reachable](https://leginfo.legislature.ca.gov/)
- [Insurance Code §1064 — page confirmed live, title `California Code, INS 1064.`](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=1064.)
- [Government Code §11015 — page confirmed live, full text retrieved; proves it is unrelated to Covered California](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=GOV&sectionNum=11015.)
- [Department of Managed Health Care, working host (verified live, 200)](https://dmhc.ca.gov/)
- [DMHC About Us — blocked, 403](https://dmhc.ca.gov/AboutUs/Pages/AboutUs.aspx)
- [DMHC Rate Filing — blocked, 403](https://dmhc.ca.gov/RegulatoryCompliant/Pages/RateFiling.aspx)
- [DMHC Health Plan Compliance — blocked, 403](https://dmhc.ca.gov/RegulatoryCompliant/Pages/HealthPlanCompliance.aspx)
- [DMHC Health Plan Complaints — blocked, 403](https://dmhc.ca.gov/Consumers/Pages/HealthPlanComplaints.aspx)
- [California Legislative Analyst's Office (verified live, 200)](https://lao.ca.gov/)
- [California State Auditor, correct domain (verified live, 200)](https://www.auditor.ca.gov/)
- [California Health Care Financing Agency (connection failure, dead end)](https://www.chffa.org/)
- [Covered California financial reports, audited statements (verified live via hbex navigation)](https://hbex.coveredca.com/financial-reports/)
- [Covered California SLAA reports (verified live via hbex navigation)](https://hbex.coveredca.com/SLAA-reports/)
- [Covered California Ombuds Annual Reports (verified live via hbex navigation)](https://hbex.coveredca.com/ombuds-annual-reports/)