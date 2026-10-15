# Bronze Plans

- **Source URL:** https://www.coveredca.com/coverage-basics/coverage-levels/bronze
- **Covered California section:** Coverage Basics / Plan Tiers
- **Retrieved:** 2026-10-13

## Summary

Bronze is the most affordable of Covered California's four standard coverage levels, with the lowest monthly premium. On average the plan pays about 60 percent of covered medical expenses and the member pays up to 40 percent. As of 2026 Bronze comes in two types — Standard Bronze and High Deductible Bronze (HDHP) — that cost about the same each month but work very differently when care is used. Free preventive care is covered from day one on both, and as of 2026 all Bronze plans pair with a health savings account.

## Key Facts

- "On average, your health insurance company pays about 60 percent of covered medical expenses, and you pay up to 40 percent."
- The page carries a **plan-type card group (HMO / PPO / EPO)** under the heading "Plan types: HMO, PPO and EPO"; transcribed below under "Plan Types: HMO, PPO and EPO".
- Two Bronze types: **Standard Bronze** and **High Deductible (HDHP) Bronze**. "They cost about the same each month but work differently when you use care."
- Free preventive care "is covered from the first day your plan begins" and there is "no deductible to meet first" for preventive care.
- "As of 2026, all Bronze plans work with a Health Savings Account (HSA)."
- Out-of-pocket maximum: $9,800 individual / $19,600 family (Standard); $7,200 individual / $14,400 family (HDHP).
- Deductible (individual): Standard — Medical: $5,800; Pharmacy: $450. HDHP — Medical + pharmacy (one combined deductible): $7,200.
- Deductible (family): Standard — Medical: $11,600; Pharmacy: $900. HDHP — one combined deductible: $14,400.
- Bronze footnote: "The first three non-preventive doctor, specialist and mental health visits are a copay with no deductible. After three visits, you pay full cost until the deductible is met."
- Pharmacy deductible (individual): Standard $450 (separate from medical); HDHP "None" — "Prescriptions count toward the one integrated deductible ($7,200)".
- Pharmacy deductible (family): Standard $900 (separate from medical); HDHP "None" — prescriptions count toward the one integrated deductible ($14,400).
- HSA rules: "The money you add isn't subject to federal income tax, and what you don't spend rolls over each year." An HSA "can be used for medical and dental costs, like deductibles and copays, but not your monthly premium."

## Details

### Is Bronze Right for You?

A Standard Bronze plan may be a good fit if you:

- Want to keep your monthly costs low.
- Don't expect to use health care services often.
- Are comfortable paying more out of pocket when you do need care.

You may want to consider other coverage levels if you:

- See a doctor several times a year.
- Regularly fill prescriptions.
- Want more protection and lower costs when you get care.
- Qualify for Enhanced Silver benefits.

**High Deductible (HDHP) Bronze plan** fits if you "rarely see the doctor but want to be covered in case of emergency or big medical bills." You pay "the entire bill for your care and prescriptions until you meet your deductible."

### Use an HSA With Your Bronze Plan

"Both Standard and HDHP Bronze plans can be paired with a health savings account (HSA). Your HSA belongs to you, not your insurance company." It pairs well with Bronze: "you keep the lowest monthly premium, and your HSA helps cover the higher costs when you do need care. Anything you don't spend stays yours and rolls over to the next year."

### Plan Costs

| Standard table | Standard Bronze | HDHP Bronze |
| --- | --- | --- |
| Best fit | A few doctor visits a year; no ongoing needs | Rarely see the doctor; want protection from big bills |
| Monthly premium | Lowest of all coverage levels | Lowest of all coverage levels |
| Out-of-pocket maximum (individual) | $9,800 | $7,200 |
| Out-of-pocket maximum (family) | $19,600 | $14,400 |
| Deductible (individual) | Medical: $5,800; Pharmacy: $450 | Medical + pharmacy (one combined deductible): $7,200 |
| Deductible (family) | Medical: $11,600; Pharmacy: $900 | Medical + pharmacy (one combined deductible): $14,400 |

All six rows above are transcribed from the Bronze page's only `<table>`, which the structural site index records as 6 rows by 3 columns with the header "Standard Bronze" / "HDHP Bronze". In the site markup the Standard Bronze deductible cells carry a combined amount plus the inline labels "Medical:" and "Pharmacy:" (individual: $5,800 and $450; family: $11,600 and $900), and the HDHP Bronze cells read "$7,200 Medical + pharmacy (One combined deductible)" and "$14,400 Medical + pharmacy (One combined deductible)".

Footnote ¹: "The first three non-preventive doctor, specialist and mental health visits are a copay with no deductible. After three visits, you pay full cost until the deductible is met."

The page notes: "For exact costs, including premiums, use Shop and Compare to see plan-specific details."

> **Correction (2026-10-13) — why only one of this page's three tables appears in `SITE-INDEX.md`.** The Bronze page renders a tab strip reading **Plan Costs | What You Pay for Care | Prescription Costs**. Only the first tab's table is server-rendered into the initial DOM, so the structural site index records exactly one table — the six-row Plan Costs grid above. The other two tables live in the page's Sanity CMS payload and appear only after a reader selects their tab. Their absence from the index is therefore not evidence of absence from the page.
>
> An intermediate draft of this file wrongly flagged the "What You'll Pay for Care" and "Prescription Costs" tables as "unverified against the current structural index" on that basis. **That flag is retracted.** Both tables have now been re-verified directly against `https://www.coveredca.com/coverage-basics/coverage-levels/bronze` on 2026-10-13 by reading the payload. Every value in both tables matched what is reproduced below: the Standard Bronze pharmacy deductible figures are stored with a **doubled dollar sign** in the payload (`$$450`, `$$900`, `$$20`), a typo in Covered California's content; the HDHP Bronze cells read "None" with the separate line "Prescriptions count toward the one integrated deductible ($7,200)" / "($14,400)"; and the Tier 2, 3 and 4 Standard Bronze cells read "Full cost before deductible; 40% after, capped at $500 per prescription". No figure in either table was changed.

### What You'll Pay for Care

| Service | Standard Bronze | HDHP Bronze |
| --- | --- | --- |
| Doctor visit | $60 (no deductible for first 3 non-preventive visits¹) | Full cost before deductible; free after |
| Specialist visit | $95 (counts toward the first 3 visits¹) | Full cost before deductible; free after |
| Mental health outpatient visit | $60 (no deductible for first 3 non-preventive visits¹) | Full cost before deductible; free after |
| Urgent care | $60 | Full cost before deductible; free after |
| Emergency room | 40% of bill after deductible | Full cost before deductible; free after |
| Ambulance | 40% of bill after deductible | Full cost before deductible; free after |
| Lab visit / tests | $50 | Full cost before deductible; free after |
| X-rays and imaging (incl. CT/PET, MRI) | 40% of bill after deductible | Full cost before deductible; free after |
| Home health, durable medical equipment, skilled nursing | 40% of bill (full cost before deductible) | Full cost before deductible; free after |
| Hospital facility fee | 40% of bill after deductible | Full cost before deductible; free after |

### Prescription Costs

| Drug type | Standard Bronze | HDHP Bronze |
| --- | --- | --- |
| Pharmacy deductible (Individual) | $450 (separate from medical) | None — Prescriptions count toward the one integrated deductible ($7,200) |
| Pharmacy deductible (Family) | $900 (separate from medical) | None — Prescriptions count toward the one integrated deductible ($14,400) |
| Generic (Tier 1) | $20 | Full cost before deductible; free after |
| Preferred (Tier 2) | Full cost before deductible; 40% after, capped at $500 per prescription | Full cost before deductible; free after |
| Non-preferred (Tier 3) | Full cost before deductible; 40% after, capped at $500 per prescription | Full cost before deductible; free after |
| Specialty (Tier 4) | Full cost before deductible; 40% after, capped at $500 per prescription | Full cost before deductible; free after |

"Not sure which tier your medication is in? Each health plan has its own list. Check your plan's drug list (formulary) in Shop and Compare or on the insurance company's site."

### Plan Types: HMO, PPO and EPO

The page presents a plan-type card group with these three cards. Transcribed verbatim:

- **HMO Plans** — "Only covers in-network care, except for emergencies"; "Need a referral to see a specialist"; "Usually the lowest monthly premium"
- **PPO Plans** — "See doctors in or out of the network"; "No referral needed to see a specialist"; "Higher monthly premium than HMO or EPO"
- **EPO Plans** — "Only covers in-network care, except for emergencies"; "No referral needed to see a specialist"; "Costs usually land between HMO and PPO"

Note the site's wording for the EPO cost position on this page: costs "usually **land** between HMO and PPO". (The overview page at `/coverage-basics/coverage-levels` uses "**fall**" instead.)

| Plan type | Full name | Character | Key rules | Best for |
| --- | --- | --- | --- | --- |
| HMO | Health maintenance organization | Lower cost, more structure | Only covers in-network care, except for emergencies; need a referral to see a specialist; usually the lowest monthly premium | Lower costs, with a primary doctor managing your care |
| PPO | Preferred provider organization | More choice, higher cost | See doctors in or out of the network; no referral needed to see a specialist; higher monthly premium than HMO or EPO | Flexibility to choose your own doctors and hospitals |
| EPO | Exclusive provider organization | Part HMO, part PPO | Only covers in-network care, except for emergencies; no referral needed to see a specialist; costs usually land between HMO and PPO | Lower costs without needing referrals |

### Common Questions

- **When does my Bronze plan start helping with costs?** "Free preventive care and your first few non-preventive visits are covered right away. For most other care, you pay the full cost until you meet your deductible – then your plan pays the larger share. Bronze's lower monthly premium is the trade-off for that higher deductible."
- **Are my prescriptions covered before I meet the deductible?** "Generic drugs are usually covered at a set copay right away. Brand-name and specialty drugs apply to your pharmacy deductible first, then drop to a copay or a share of the cost."
- **What's the HSA-eligible Bronze plan?** "As of 2026, all Bronze plans work with a Health Savings Account (HSA). An HSA is a separate savings account you can open to set money aside for health costs and use it, tax-free, to pay for care. It pairs well with Bronze: you keep the lowest monthly premium, and your HSA helps cover the higher costs when you do need care. Anything you don't spend stays yours and rolls over to the next year."