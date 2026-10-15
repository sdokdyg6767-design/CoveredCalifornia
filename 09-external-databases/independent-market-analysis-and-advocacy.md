# Independent Market Analysis and Advocacy (KFF, California Health Report, Health Consumer Alliance, Public Advocates, CBO/GAO/Urban)

- **Retrieved:** 2026-10-13
- **Type:** External source guide

## Summary

Covered California is a state-run marketing agency as well as a regulator of itself, so everything on coveredca.com is written by an interested party about its own product. This file documents the independent and adversarial sources that exist precisely to evaluate the California individual market from outside: **KFF** for comparative health policy data across states, the **California Health Report** as the state's dedicated health journalism outlet, the **Health Consumer Alliance** as the independent consumer-assistance network, advocacy organizations such as **Public Advocates**, and the federal analytic bodies **CBO**, **GAO** and **Urban Institute**.

Access from this environment was the worst of any of the four files. Three of the most authoritative publishers — KFF, CBO and GAO — were unreachable by the methods available, and the California Health Report's domain did not resolve at all. The Health Consumer Alliance, Urban Institute and CHCF did respond normally, so those are the sources a reader should actually start from.

## Key Facts

| Attribute | Detail |
| --- | --- |
| Reachable publishers | Health Consumer Alliance (200), Urban Institute (200), CHCF (200), Public Advocates (200 via curl) |
| Blocked publishers | CBO (403), GAO (403), KFF (404 on state-facts path; connection aborted on other paths) |
| DNS failures | californiahealthreport.org and www.californiahealthreport.org (no resolution) |
| Access | All nominally free; none requires registration |
| Bias profile | KFF and CBO/GAO are nonpartisan; CHR is journalistic; HCA and Public Advocates are advocacy — all are interested in different ways than the state is |
| Machine-readable | None of these publish APIs. Urban and KFF publish downloadable data files; the rest are HTML/PDF |

## Sources documented

### Health Consumer Alliance (HCA) — the consumer assistance network

- **URL:** https://www.healthconsumer.org/
- **Verified live:** HTTP 200, 114,206 bytes, title `Welcome to the Health Consumer Alliance - Health Consumer Alliance (HCA)`.
- **What it is:** the statewide network of nonprofit consumer health counselors across California — the organizations that do one-on-one enrollment assistance, counseling, and appeals help, as distinct from the state's own call centers.
- **Authoritative for:** what an independent counselor actually tells consumers, which coverage issues are recurring and hard, where the state's own scripts diverge from real-world cases, and the existence of local, in-person help outside Covered California.
- **Cannot answer:** official eligibility rules, rates, or plan data.
- **Why it matters here:** Covered California's own Ombudsman/CBA materials describe a state-defined process. HCA describes that same process from the advocate's side, which is where complaints that never surface in official statistics become visible.
- **Does not answer:** whether a specific counselor organization covers a specific county.

### California Health Report — believed to be the current outlet, URL unresolved

- **Status: DNS failure, and I could not confirm the URL.** Four attempts on 2026-10-13 all failed: `https://californiahealthreport.org/` (curl 000, exit 6), `https://www.californiahealthreport.org/` (curl 000, exit 6), and the same two via `Invoke-WebRequest` ("The remote name could not be resolved"). A Wayback CDX query for `californiahealthreport.org*` over 2024–2026 returned **EMPTY** — no captures at all in the index for that domain pattern.
- **Believed but unverified:** a previous run of this project reported that "California Health Report" is the current name of California's health policy journalism outlet with 2026 coverage. **I was unable to confirm this.** The total absence of both live DNS and any Wayback captures is itself notable and suggests either that the domain was never archived under that exact host, or that the outlet's domain is different from the obvious one.
- **Do not cite a URL for this outlet from this file.** If the parent project needs it, resolve it from an independent index or a current hyperlink rather than from the bare domain name.

### Public Advocates

- **URL:** `https://www.publicadvocates.org/` — via PowerShell this failed with *"Could not create SSL/TLS secure channel"*; via `curl` the same host **returned HTTP 200, 175,795 bytes**, redirecting to the non-`www` origin `https://publicadvocates.org/`. So the site is alive; PowerShell's TLS stack was the problem, not the server.
- **Authoritative for:** California's legal advocacy nonprofit, publishing litigation, analysis and commentary on health care affordability, Medi-Cal, and insurance regulation — including critical work on the individual market and on the legality of Covered California policy choices.
- **Cannot answer:** neutral data; everything here is an advocacy position, valuable as a record of what is contested and by whom.

### KFF — the primary comparative health policy source

- **URL:** `https://www.kff.org/state-health-facts/` — **verified live, HTTP 200, 131,389 bytes.**
- **Blocked paths found:** `https://www.kff.org/health-state-facts/` returns **HTTP 404** (94,691 bytes — a KFF not-found page, so the server responds but the legacy path is gone); `https://www.kff.org/medicaid/medicaid-expansion-tracker/` and `https://www.kff.org/report-section/medicaid-expansion-tracker/` both return **HTTP 404**; `https://www.kff.org/tag/covered-california/` returns **HTTP 404**. `https://www.kff.org/health-costs/` **redirects** to `https://www.kff.org/topic/health-costs/` (HTTP 200, 354,053 bytes).
- Also observed: `Invoke-WebRequest` to `https://www.kff.org/health-state-facts/` produced *"The request was aborted: The connection was closed unexpectedly"* — KFF's edge behaves inconsistently across clients. `curl` works reliably.
- **Authoritative for:** state-to-state comparison of health coverage, uninsurance rates, Medicaid expansion status, marketplace premium growth, and subsidy take-up. KFF is the standard reference for "how does California's individual market compare with other states," which no California government source will frame that way.
- **Practical note:** the legacy `health-state-facts/` path is retired; the live one is `state-health-facts/`. Older citations and the Medicaid Expansion Tracker deep links are dead and will need re-finding.

### Urban Institute

- **URL:** https://www.urban.org/ — **verified live, HTTP 200, 414,265 bytes.**
- **Authoritative for:** research on ACA marketplace enrollment dynamics, subsidy take-up and unwinding, health insurance markets, and state health policy — including California-specific analyses.
- **Cannot answer:** California's official figures. Urban is a DC-based research institution; its California work is often produced in partnership with California organizations.

### Congressional Budget Office (CBO)

- **Status: blocked.** `https://www.cbo.gov/` returns **HTTP 403**; `https://www.cbo.gov/publication/61032` also returns **HTTP 403**.
- **Authoritative for:** budget scoring of federal legislation affecting the ACA — most importantly, the coverage and federal-cost estimates of the 2025 reconciliation law (P.L. 119-21) whose Medicaid provisions are documented in the Medi-Cal file.
- **Note:** the exchange portal itself hosts CBO-related material, including `Covered California to CBO - National CSR Funding and Reinsurance - 04-14-2017 Final.pdf` and `Federal Budget Impact of Not Funding CSRs-04-14-17 Final_.pdf`, both confirmed as live links on hbex. Those are useful secondary access points to CBO-style federal-impact analysis without needing cbo.gov.

### Government Accountability Office (GAO)

- **Status: blocked.** `https://www.gao.gov/` returns **HTTP 403**.
- **Authoritative for:** federal oversight of ACA implementation, marketplace federalism, and federal payments to state exchanges — the closest federal analogue to the state auditor question raised in the oversight file.

### Center for Health Care Market Analysis

- **Status: not verified. I found no such organization and did not confirm any source for it.** No URL was attempted and none can be recommended. Listed here as a dead end so that the next pass does not spend budget chasing it: either it does not exist, it has been renamed or folded into another organization, or it was a confusion with an academic program. **Treat as unconfirmed and possibly nonexistent.**

### Consumers' Alliance

- **Status: not verified.** No live source was retrieved and no specific organization by this name could be pinned down. Ambiguous name — there are multiple health-advocacy organizations using similar branding. Do not cite without disambiguation.

## Questions this file can answer that coveredca.com cannot

1. How does California compare with other states on uninsurance, Medicaid expansion durability, and marketplace premium growth — on a consistent cross-state definition rather than the state's own.
2. What did independent nonpartisan analysts conclude about the cost and coverage effects of the federal 2025 Medicaid law, as distinct from the state's characterization of it.
3. Where independent nonprofits and legal advocates are actually contesting California health policy, and on what grounds — the litigation and comment record that a state press release will never contain.
4. What real consumers are being told by independent counselors, including which problems recur and which official answers fail in practice.
5. How the Exchange performs against the claims advocates make about it, using researchers who are not employed by the state.
6. Whether California's marketplace dynamics differ structurally from the general ACA state-marketplace case, which federal and DC-based research treats as the default.

## Known gaps and dead ends

All statuses observed 2026-10-13.

1. **`www.cbo.gov` — HTTP 403** on both `/` and a publication page. CBO analysis could not be retrieved. Workaround for some documents: hbex.coveredca.com hosts CBO-related federal-impact PDFs.
2. **`www.gao.gov` — HTTP 403** at the root.
3. **KFF is partially blocked and partially moved.** `curl` reaches it; PowerShell's request was aborted ("connection was closed unexpectedly"). Dead paths returning 404: `/health-state-facts/` (the old state facts entry point), `/medicaid/medicaid-expansion-tracker/`, `/report-section/medicaid-expansion-tracker/`, `/tag/covered-california/`. Use `https://www.kff.org/state-health-facts/`, which returned 200.
4. **`californiahealthreport.org` — DNS failure**, both apex and `www`, via two different clients. Wayback CDX for `californiahealthreport.org*` returned EMPTY for 2024–2026. **The California Health Report outlet URL is unresolved.** A prior run asserted this name; this run could not confirm it and the file does not supply a URL for it.
5. **`www.publicadvocates.org` fails in PowerShell with a TLS error but returns HTTP 200 via curl** (redirecting to the apex domain). Use `curl`, and expect a redirect.
6. **`https://www.dmhc.ca.gov/`-class state enforcement sites are also Akamai-blocked** — see the oversight file. The pattern of state insurance/health sites being blocked is systematic, not incidental.
7. **No source at all was retrieved for the "Center for Health Care Market Analysis."** Existence unconfirmed.
8. **No source was resolved for "Consumers' Alliance."** The name is too ambiguous to cite.
9. **No paywalled sources were encountered.** Everything attempted here is nominally free; the barrier in this environment was blocking and DNS, not licensing.
10. **GAO and CBO 403s mean this file under-represents the federal analytic view.** That view is important for the ACA question and is a known weakness of this document.

## Sources

- [Health Consumer Alliance (verified live, 200)](https://www.healthconsumer.org/)
- [KFF State Health Facts (verified live, 200)](https://www.kff.org/state-health-facts/)
- [KFF Health Costs topic (verified live, 200, reached by redirect from /health-costs/)](https://www.kff.org/topic/health-costs/)
- [Urban Institute (verified live, 200)](https://www.urban.org/)
- [Public Advocates (verified live, 200 via curl; TLS failure via PowerShell)](https://www.publicadvocates.org/)
- [California Health Care Foundation (verified live, 200)](https://www.chcf.org/)
- [CBO root (403, blocked)](https://www.cbo.gov/)
- [GAO root (403, blocked)](https://www.gao.gov/)
- [California Health Report (DNS failure, unresolved)](https://californiahealthreport.org/)