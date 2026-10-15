# Covered California — Structural Site Index

Generated 2026-10-13 by `_raw/site_index.py` from the live site.  
- **Source:** all 119 English pages of `https://www.coveredca.com/`, enumerated from `https://www.coveredca.com/sitemap.xml`
- **Retrieved:** 2026-10-13
- **Renderer:** `_raw/render_index.py` from `_raw/SITE-INDEX.json`  
This is a **structure map**, not a content summary: for every page it records the real `<table>` grids (with each cell kept aligned to its own row), the card groups, the heading outline, and the FAQ items.

It exists because the first extractor used to build the library **flattened tables and discarded row labels**, which silently merged a row away. Anything on this site expressed as a table or card must be transcribed row-by-row, not as a bag of text.

- Pages indexed: **119/119**
- Pages containing real `<table>` elements: **38** (41 tables)
- Pages containing card groups: **29** (30 groups)
- Total FAQ items captured: **866**

## Read this before you use this file

This index is a **gap-finder. It is not proof of absence.** Four limits, in order of how much damage they can do:

1. **It records structure, not prose.** Paragraph text is not captured at all. A page can publish any number of facts in prose and appear here to publish nothing. You cannot conclude "the page does not say X" from this file.
2. **It cannot see tab-hidden content.** Bronze, Gold and Platinum each carry a **Prescription Costs** table that exists in the site's Sanity CMS payload but is **not server-rendered** into the initial DOM — it renders only when a reader selects the tab. Each of those three pages therefore shows **1 table** here. Silver's drug table *is* server-rendered, which is why Silver shows **2**. This is the most likely way to reach a wrong conclusion from this index, and it has already caused one: a remediation pass flagged the Bronze, Gold and Platinum prescription tables as unsupported and tried to withdraw them. All three were re-verified as correct on 2026-10-13.
3. **It captures FAQ question headings, not answers.**
4. **English only.** 119 of 234 sitemap URLs. The 115 Spanish mirrors were deliberately skipped.

**Use it to find gaps, then open the live page to confirm before adding anything. Never use it as the sole basis for removing content.**

## Risk ranking

Pages are ordered by how likely a flattening extractor would corrupt them (tables weighted heaviest, since that is where row-to-rule mis-assignment happens).

| # | Page | Tables | Cards | FAQ | KB |
|---:|---|---:|---:|---:|---:|
| 1 | `/` | 0 | 1 | 16 | 520 |
| 2 | `/small-business/health-plans/blue-shield` | 1 | 0 | 3 | 507 |
| 3 | `/small-business/health-plans/kaiser` | 1 | 0 | 3 | 496 |
| 4 | `/enrollment/documents/immigration-status` | 0 | 0 | 6 | 496 |
| 5 | `/enrollment` | 0 | 1 | 9 | 466 |
| 6 | `/coverage-basics/coverage-levels/silver` | 2 | 1 | 14 | 451 |
| 7 | `/coverage-basics/coverage-levels` | 1 | 1 | 14 | 452 |
| 8 | `/small-business/health-plans/sharp` | 1 | 0 | 3 | 448 |
| 9 | `/coverage-basics/coverage-levels/bronze` | 1 | 1 | 15 | 436 |
| 10 | `/account` | 0 | 0 | 13 | 434 |
| 11 | `/costs/financial-help` | 0 | 2 | 10 | 426 |
| 12 | `/coverage-basics/dental` | 2 | 0 | 9 | 418 |
| 13 | `/insurance-company-contacts` | 0 | 0 | 21 | 421 |
| 14 | `/coverage-basics/tax-penalty-details-and-exemptions` | 1 | 0 | 10 | 414 |
| 15 | `/coverage-basics/coverage-levels/platinum` | 1 | 1 | 10 | 411 |
| 16 | `/coverage-basics/coverage-levels/gold` | 1 | 1 | 10 | 408 |
| 17 | `/enrollment/eligibility/immigrants` | 1 | 0 | 10 | 408 |
| 18 | `/enrollment/major-life-changes` | 1 | 1 | 11 | 404 |
| 19 | `/get-help/events` | 0 | 0 | 6 | 406 |
| 20 | `/small-business/health-plans` | 1 | 1 | 3 | 400 |
| 21 | `/accessibility-and-language-support` | 1 | 0 | 6 | 401 |
| 22 | `/get-help` | 1 | 0 | 6 | 395 |
| 23 | `/account/renew` | 1 | 1 | 9 | 391 |
| 24 | `/account/guide-to-your-account` | 0 | 1 | 8 | 393 |
| 25 | `/small-business/mandate/1095-forms` | 2 | 0 | 9 | 388 |
| 26 | `/enrollment/eligibility` | 1 | 1 | 6 | 389 |
| 27 | `/account/using-your-plan` | 0 | 1 | 7 | 388 |
| 28 | `/account/file-an-appeal` | 0 | 0 | 14 | 384 |
| 29 | `/enrollment/documents/citizenship` | 0 | 0 | 6 | 384 |
| 30 | `/important-changes` | 0 | 0 | 6 | 384 |
| 31 | `/small-business/mandate/resources` | 1 | 0 | 4 | 380 |
| 32 | `/small-business` | 0 | 1 | 9 | 380 |
| 33 | `/ombuds-office` | 0 | 0 | 14 | 378 |
| 34 | `/enrollment/documents/income` | 0 | 0 | 6 | 378 |
| 35 | `/coverage-basics/tax-penalty-details-and-exemptions/ftb-form-3853` | 0 | 0 | 9 | 377 |
| 36 | `/glossary` | 0 | 0 | 6 | 375 |
| 37 | `/coverage-basics/medi-cal` | 1 | 0 | 11 | 372 |
| 38 | `/small-business/eligibility` | 1 | 0 | 5 | 371 |
| 39 | `/privacy/terms` | 0 | 0 | 6 | 370 |
| 40 | `/coverage-basics/coverage-levels/minimum-coverage-plan` | 1 | 0 | 7 | 365 |
| 41 | `/coverage-basics` | 1 | 0 | 8 | 364 |
| 42 | `/enrollment/eligibility/american-indians-alaska-natives` | 0 | 0 | 11 | 366 |
| 43 | `/small-business/apply` | 0 | 0 | 6 | 366 |
| 44 | `/small-business/mandate` | 1 | 0 | 9 | 363 |
| 45 | `/small-business/costs-and-financial-help` | 0 | 0 | 7 | 366 |
| 46 | `/account/tax-forms` | 0 | 0 | 6 | 364 |
| 47 | `/account/using-your-plan/free-preventive-care-for-children` | 1 | 0 | 8 | 360 |
| 48 | `/enrollment/losing-medi-cal-coverage` | 1 | 0 | 11 | 359 |
| 49 | `/account/using-your-plan/free-preventive-care-for-adults` | 1 | 0 | 9 | 358 |
| 50 | `/coverage-basics/medi-cal/children` | 0 | 0 | 10 | 359 |
| 51 | `/coverage-basics/vision` | 1 | 0 | 9 | 356 |
| 52 | `/costs/financial-help/employer-coverage` | 1 | 0 | 6 | 355 |
| 53 | `/enrollment/documents/identity` | 0 | 0 | 6 | 357 |
| 54 | `/enrollment/open-enrollment` | 0 | 0 | 6 | 353 |
| 55 | `/small-business/employer-forms` | 0 | 0 | 3 | 353 |
| 56 | `/enrollment-partners-small-business/ccsb-certification` | 0 | 1 | 7 | 350 |
| 57 | `/enrollment-partners-small-business/ccsb-certification/code-of-conduct` | 0 | 0 | 5 | 352 |
| 58 | `/account/cancel` | 0 | 0 | 10 | 352 |
| 59 | `/costs/financial-help/health-reimbursement-arrangements` | 1 | 0 | 7 | 348 |
| 60 | `/enrollment/documents` | 1 | 0 | 6 | 348 |
| 61 | `/account/using-your-plan/enrollee-programs` | 1 | 0 | 10 | 348 |
| 62 | `/costs` | 1 | 0 | 6 | 348 |
| 63 | `/small-business/dental-plans` | 0 | 1 | 6 | 348 |
| 64 | `/enrollment/eligibility/people-with-chronic-conditions` | 0 | 0 | 6 | 350 |
| 65 | `/consumer-protection` | 1 | 0 | 6 | 347 |
| 66 | `/enrollment/documents/notification-of-a-deceased-member` | 0 | 0 | 6 | 348 |
| 67 | `/small-business/health-plans/western-health-advantage` | 0 | 0 | 3 | 348 |
| 68 | `/account/using-your-plan/free-preventive-care-for-women` | 1 | 0 | 9 | 345 |
| 69 | `/account/renew/moving-to-medicare` | 0 | 0 | 9 | 347 |
| 70 | `/account/using-your-plan/mental-health` | 0 | 0 | 7 | 346 |
| 71 | `/coverage-basics/medi-cal/pregnant-individuals` | 1 | 0 | 11 | 343 |
| 72 | `/privacy` | 0 | 0 | 15 | 346 |
| 73 | `/enrollment-partners-small-business/training-and-education` | 0 | 0 | 5 | 345 |
| 74 | `/enrollment/major-life-changes/domestic-abuse` | 0 | 0 | 10 | 343 |
| 75 | `/enrollment/documents/minimum-essential-coverage` | 0 | 0 | 6 | 341 |
| 76 | `/molina-healthcare` | 0 | 1 | 6 | 338 |
| 77 | `/enrollment/documents/not-incarcerated` | 0 | 0 | 6 | 339 |
| 78 | `/small-business/dental-plans/delta-dental` | 0 | 0 | 3 | 339 |
| 79 | `/enrollment-partners-individuals/training-and-education` | 0 | 0 | 6 | 339 |
| 80 | `/coverage-basics/medi-cal/mixed-program-families` | 1 | 0 | 6 | 335 |
| 81 | `/enrollment/documents/social-security-number` | 1 | 0 | 6 | 335 |
| 82 | `/small-business/employee-forms` | 0 | 0 | 3 | 336 |
| 83 | `/account/billing` | 0 | 0 | 9 | 336 |
| 84 | `/about-covered-california` | 0 | 0 | 7 | 336 |
| 85 | `/health-net` | 0 | 1 | 6 | 332 |
| 86 | `/western-health-advantage` | 0 | 1 | 6 | 332 |
| 87 | `/kaiser-permanente` | 0 | 1 | 6 | 332 |
| 88 | `/valley-health` | 0 | 1 | 6 | 332 |
| 89 | `/anthem` | 0 | 1 | 6 | 332 |
| 90 | `/blue-shield` | 0 | 1 | 6 | 331 |
| 91 | `/la-care` | 0 | 1 | 6 | 331 |
| 92 | `/enrollment-partners-small-business/client-support` | 0 | 0 | 5 | 333 |
| 93 | `/caloptima` | 0 | 1 | 6 | 331 |
| 94 | `/enrollment/documents/american-indian-or-alaskan-native` | 0 | 0 | 6 | 333 |
| 95 | `/cchp` | 0 | 1 | 6 | 331 |
| 96 | `/iehp` | 0 | 1 | 6 | 331 |
| 97 | `/sharp` | 0 | 1 | 6 | 331 |
| 98 | `/marketing-blog` | 0 | 0 | 6 | 332 |
| 99 | `/costs/financial-help/health-reimbursement-arrangements/hra-affordability-calculator` | 0 | 0 | 6 | 327 |
| 100 | `/enrollment-partners-individuals/become-an-agent/code-of-conduct` | 0 | 0 | 6 | 327 |
| 101 | `/enrollment-partners-small-business/contact` | 0 | 0 | 5 | 325 |
| 102 | `/enrollment-partners-individuals/marketing-branding-policies` | 0 | 0 | 6 | 324 |
| 103 | `/social-media-commenting-disclaimer` | 0 | 0 | 6 | 319 |
| 104 | `/small-business/contact` | 0 | 0 | 3 | 318 |
| 105 | `/press-releases` | 0 | 0 | 6 | 318 |
| 106 | `/enrollment-partners-individuals/become-a-certified-enroller` | 0 | 0 | 6 | 317 |
| 107 | `/enrollment-partners-individuals/contact` | 0 | 0 | 6 | 317 |
| 108 | `/enrollment-partners-individuals` | 0 | 0 | 6 | 310 |
| 109 | `/enrollment-partners-small-business` | 0 | 0 | 5 | 310 |
| 110 | `/enrollment-partners-individuals/become-an-agent` | 0 | 0 | 6 | 309 |
| 111 | `/enrollment-partners-individuals/client-support` | 0 | 0 | 6 | 304 |
| 112 | `/get-help/find-an-enroller` | 0 | 0 | 7 | 285 |
| 113 | `/enrollment-partners-individuals/privacy-policy` | 0 | 0 | 6 | 262 |
| 114 | `/get-help/help-on-demand` | 0 | 0 | 6 | 292 |
| 115 | `/get-help/live-chat` | 0 | 0 | 6 | 270 |
| 116 | `/legal-notices` | 0 | 0 | 6 | 279 |
| 117 | `/media-inquiries` | 0 | 0 | 6 | 275 |
| 118 | `/small-business/enrollment-support` | 0 | 0 | 3 | 263 |
| 119 | `/small-business/get-a-quote` | 0 | 0 | 3 | 270 |

## Per-page structure

### coverage-basics

#### `/coverage-basics`

*Coverage Basics | Covered California* — 19 headings, 1 table(s), 0 card group(s), 8 FAQ item(s), 373,235 bytes

**Table 1** — 3 rows x 3 cols

|   | Covered California | Medi-Cal |
|---|---|---|
| What It Is | Private plans you buy through the state marketplace, with or without financial help | Insurance for people with lower incomes |
| Who Is Eligible | Californians without job-based or other government insurance | Californians who qualify based on income and household size |
| What You Pay | A monthly premium, often lowered by financial help | Little to no cost |

**FAQ / accordions (8)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Coverage Levels
- Benefits Covered by All Plans

#### `/coverage-basics/coverage-levels`

*Health Plan Coverage Levels | Covered California* — 37 headings, 1 table(s), 1 card group(s), 14 FAQ item(s), 463,554 bytes

**Table 1** — 4 rows x 5 cols

| Plan Tier | Monthly Payment | Plan Covers of average annual cost | You Pay | Preventive Care |
|---|---|---|---|---|
| Bronze Bronze | Low | 60% | 40% | Free |
| Silver Silver | Medium | * 70-94% | * 6-30% | Free |
| Gold Gold | High | 80% | 20% | Free |
| Platinum Platinum | Highest | 90% | 10% | Free |

**Card group 1**

- **HMO Plans**
  - Only covers in-network care, except for emergencies
  - Need a referral to see a specialist
  - Usually the lowest monthly premium
- **PPO Plans**
  - See doctors in or out of the network
  - No referral needed to see a specialist
  - Higher monthly premium than HMO or EPO
- **EPO Plans**
  - Only covers in-network care, except for emergencies
  - No referral needed to see a specialist
  - Costs usually fall between HMO and PPO

**FAQ / accordions (14)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Once or twice
- Monthly or more
- Paying less each month
- Somewhere in between
- Paying less when I get care
- What if I pick a lower-level plan and then something happens?
- How do I know if I qualify for extra savings on a Silver plan?
- Can I change my plan later?

#### `/coverage-basics/coverage-levels/bronze`

*Bronze Plans | Covered California* — 27 headings, 1 table(s), 1 card group(s), 15 FAQ item(s), 447,053 bytes

**Table 1** — 6 rows x 3 cols

|   | Standard Bronze | HDHP Bronze |
|---|---|---|
| Best fit | A few doctor visits a year; no ongoing needs | Rarely see the doctor; want protection from big bills |
| Monthly premium | Lowest of all coverage levels | Lowest of all coverage levels |
| Out-of-pocket maximum (individual) | $9,800 | $7,200 |
| Out-of-pocket maximum (family) | $19,600 | $14,400 |
| Deductible (individual) | $5,800; $450 Medical: Pharmacy: | :$7,200 Medical + pharmacy (One combined deductible) |
| Deductible (family) | $11,600; $900 Medical: Pharmacy: | :$14,400 Medical + pharmacy (One combined deductible) |

**Card group 1**

- **HMO Plans**
  - Only covers in-network care, except for emergencies
  - Need a referral to see a specialist
  - Usually the lowest monthly premium
- **PPO Plans**
  - See doctors in or out of the network
  - No referral needed to see a specialist
  - Higher monthly premium than HMO or EPO
- **EPO Plans**
  - Only covers in-network care, except for emergencies
  - No referral needed to see a specialist
  - Costs usually land between HMO and PPO

**FAQ / accordions (15)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- coverage levels
- out-of-pocket costs
- free preventive care
- Enhanced Silver
- What You Pay for Care
- Prescription Costs
- When does my Bronze plan start helping with costs?
- Are my prescriptions covered before I meet the deductible?
- What's the HSA-eligible Bronze plan?

#### `/coverage-basics/coverage-levels/gold`

*Gold Plans | Covered California* — 21 headings, 1 table(s), 1 card group(s), 10 FAQ item(s), 418,481 bytes

**Table 1** — 17 rows x 3 cols

| Service | What You Pay - HMO | What You Pay - PPO and EPO |
|---|---|---|
| Out-of-pocket maximum (individual) | $9,200 | $9,200 |
| Out-of-pocket maximum (family) | $18,400 | $18,400 |
| Medical deductible | $0 | $0 |
| Pharmacy deductible | $0 | $0 |
| Doctor visit | $40 | $40 |
| Specialist visit | $70 | $70 |
| Mental health outpatient visit | $40 | $40 |
| Urgent care | $40 | $40 |
| Emergency room | $350 | $350 |
| Ambulance | $250 | $250 |
| Lab visit / lab tests | $40 | $40 |
| X-rays and diagnostic imaging | $75 | $75 |
| CT/PET scans, MRIs | $75 | 25% of bill |
| Home health | $30 per visit | 20% of bill |
| Durable medical equipment | 20% of bill | 20% of bill |
| Skilled nursing care | $150 per day, up to 5 days | 30% of bill |
| Hospital facility fee | $375 per day, up to 5 days | 30% of bill |

**Card group 1**

- **HMO Plans**
  - Only covers in-network care, except for emergencies
  - Need a referral to see a specialist
  - Usually the lowest monthly premium
- **PPO Plans**
  - See doctors in or out of the network
  - No referral needed to see a specialist
  - Higher monthly premium than HMO or EPO
- **EPO Plans**
  - Only covers in-network care, except for emergencies
  - No referral needed to see a specialist
  - Costs usually land between HMO and PPO

**FAQ / accordions (10)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- coverage levels
- covered services
- Enhanced Silver
- Prescription Costs

#### `/coverage-basics/coverage-levels/minimum-coverage-plan`

*Minimum Coverage Plan | Covered California* — 20 headings, 1 table(s), 0 card group(s), 7 FAQ item(s), 374,455 bytes

**Table 1** — 5 rows x 3 cols

|   | Minimum Coverage Plan | Bronze Plan |
|---|---|---|
| Who can buy it? | Usually people under 30, or people 30 or older with an approved hardship or affordability exemption | People of any age who are eligible for Covered California |
| Monthly premium | Usually lower, but not always the lowest total cost | Often similar to minimum coverage plans |
| Financial help available | No | Yes, if you qualify |
| Deductible and costs when you use care | Usually higher out-of-pocket costs before the plan pays for most care | May have a lower deductible and different cost-sharing |
| Exemption required | Yes, if you are 30 or older | No exemption needed |

**FAQ / accordions (7)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- out-of-pocket maximum

#### `/coverage-basics/coverage-levels/platinum`

*Platinum Plans | Covered California* — 21 headings, 1 table(s), 1 card group(s), 10 FAQ item(s), 421,260 bytes

**Table 1** — 17 rows x 3 cols

| Service | What You Pay - HMO | What You Pay - PPO and EPO |
|---|---|---|
| Out-of-pocket maximum (individual) | $5,000 | $5,000 |
| Out-of-pocket maximum (family) | $10,000 | $10,000 |
| Medical deductible | $0 | $0 |
| Pharmacy deductible | $0 | $0 |
| Doctor visit | $15 | $15 |
| Specialist visit | $30 | $30 |
| Mental health outpatient visit | $15 | $15 |
| Urgent care | $15 | $15 |
| Emergency room | $175 | $175 |
| Ambulance | $150 | $150 |
| Lab visit / lab tests | $15 | $15 |
| X-rays and diagnostic imaging | $30 | $30 |
| CT/PET scans, MRIs | $75 | 10% of bill |
| Home health | $20 per visit | 10% of bill |
| Durable medical equipment | 10% of bill | 10% of bill |
| Skilled nursing care | $125 per day, up to 5 days | 10% of bill |
| Hospital facility fee | $225 per day, up to 5 days | 10% of bill |

**Card group 1**

- **HMO Plans**
  - Only covers in-network care, except for emergencies
  - Need a referral to see a specialist
  - Usually the lowest monthly premium
- **PPO Plans**
  - See doctors in or out of the network
  - No referral needed to see a specialist
  - Higher monthly premium than HMO or EPO
- **EPO Plans**
  - Only covers in-network care, except for emergencies
  - No referral needed to see a specialist
  - Costs usually land between HMO and PPO

**FAQ / accordions (10)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- monthly premium
- covered services
- Enhanced Silver
- Prescription Costs

#### `/coverage-basics/coverage-levels/silver`

*Silver Plans | Covered California* — 28 headings, 2 table(s), 1 card group(s), 14 FAQ item(s), 462,530 bytes

**Table 1** — 11 rows x 5 cols

| Service | Silver 70 | Silver 73 | Silver 87 | Silver 94 |
|---|---|---|---|---|
| Out-of-pocket max individual | $9,800 | $8,100 | $3,350 | $1,400 |
| Out-of-pocket max family | $19,600 | $16,200 | $6,700 | $2,800 |
| Medical deductible individual | $5,200 | $5,200 | $1,400 | None |
| Medical deductible family | $10,400 | $10,400 | $2,800 | None |
| Doctor visit | $50 | $50 | $15 | $5 |
| Specialist visit | $90 | $90 | $25 | $8 |
| Urgent care | $50 | $50 | $15 | $5 |
| Emergency room | $400 | $400 | $200 | $50 |
| Lab tests | $50 | $50 | $30 | $10 |
| X-rays & diagnostic imaging | $95 | $95 | $50 | $10 |
| CT/PET scans, MRIs | $325 | $325 | $100 | $50 |

**Table 2** — 6 rows x 5 cols

|   | Silver 70 | Silver 73 | Silver 87 | Silver 94 |
|---|---|---|---|---|
| Pharmacy deductible individual | $50 | $50 | $50 | None |
| Pharmacy deductible family | $100 | $100 | $100 | None |
| Generic (Tier 1) | $19 | $19 | $8 | $3 |
| Preferred (Tier 2) | $60 | $55 | $25 | $10 |
| Non-preferred (Tier 3) | $90 | $85 | $45 | $15 |
| Specialty (Tier 4) | 20% up to $250 | 20% up to $250 | 15% up to $150 | 10% up to $150 |

**Card group 1**

- **HMO Plans**
  - Only covers in-network care, except for emergencies
  - Need a referral to see a specialist
  - Usually the lowest monthly premium
- **PPO Plans**
  - See doctors in or out of the network
  - No referral needed to see a specialist
  - Higher monthly premium than HMO or EPO
- **EPO Plans**
  - Only covers in-network care, except for emergencies
  - No referral needed to see a specialist
  - Costs usually land between HMO and PPO

**FAQ / accordions (14)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- coverage level
- monthly premium
- Enhanced Silver
- out-of-pocket costs
- out-of-pocket maximums
- How do I get an Enhanced Silver plan, and which level?
- If I qualify for Enhanced Silver, do I have to choose it?
- What happens to my plan if my income changes during the year?

#### `/coverage-basics/dental`

*Dental Insurance | Covered California* — 27 headings, 2 table(s), 0 card group(s), 9 FAQ item(s), 428,729 bytes

**Table 1** — 11 rows x 4 cols

| Health Insurance Company | Children's Dental Company | Plan Types | Contact |
|---|---|---|---|
| Anthem | Anthem Blue Cross | DHMO, DPPO | (877) 567-1804 |
| Balance by CCHP | Delta Dental of California | DHMO | (800) 471-9925 |
| Blue Shield | Dental Benefit Providers | DHMO, DPPO | DPPO: (888) 271-4880 / DHMO: (800) 286-7401 |
| Health Net | Dental Benefit Providers | DHMO, DPPO | (866) 249-2382 |
| Inland Empire Health Plan | Liberty Dental Plan | DHMO | (866) 544-2981 |
| Kaiser Permanente | Delta Dental of California | DHMO | (888) 282-8528 |
| L.A. Care | Liberty Dental Plan | DHMO | (800) 700-5243 |
| Molina | DentaQuest | DHMO | (855) 425-4164 |
| Sharp | Delta Dental | DHMO | (855) 370-4215 |
| Valley Health Plan | Liberty Dental Plan | DHMO | (888) 902-0403 |
| Western Health Advantage | Delta Dental of California | DHMO | (800) 422-4234 |

**Table 2** — 15 rows x 3 cols

| Feature | Dental HMO (DHMO) | Dental PPO (DPPO) |
|---|---|---|
| Whom it covers | Adults, plus any children you add | Adults, plus any children you add |
| Monthly premium payments | Usually lower than DPPO plans | Generally higher than DHMO plans |
| Provider network | In-network only, except emergencies | In-network and out-of-network |
| Seeing a specialist | You need a referral | No referral needed |
| Deductible | $0 | $50 per adult, $75 per child |
| Annual benefit limit | No limit | $1,500 for adults, no limit for children |
| Out-of-pocket maximum | $350 one child, $700 two or more. No maximum for adults. | $350 one child, $700 two or more. No maximum for adults. |
| Waiting period | None | Adults wait six months. May be shorter or waived with proof of past coverage. |
| Checkups, cleanings, X-rays | Free in network | Free in network |
| Amalgam filling (one surface) | $25 | You pay 20% |
| Root canal (molar) | $300 | You pay 50% |
| Gingivectomy (per tooth) | $50 | You pay 50% |
| Extraction: single tooth, exposed root or erupted | $65 | You pay 50% |
| Crown (porcelain with metal) | $300 | You pay 50% |
| Medically necessary braces | Children only: $350 | Children only: you pay 50% |

**FAQ / accordions (9)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Why isn't adult dental insurance included with my health insurance plan?
- Can my child have both the included dental plan and a family dental plan?
- Where can I find the complete list of covered services, exclusions and limitations?

#### `/coverage-basics/medi-cal`

*Medi-Cal | Covered California* — 24 headings, 1 table(s), 0 card group(s), 11 FAQ item(s), 381,432 bytes

**Table 1** — 3 rows x 3 cols

|   | Medi-Cal | Covered California |
|---|---|---|
| What It Is | A state program that gives free or low-cost coverage to people with limited income | Private health insurance marketplace where people can get income-based financial help to reduce monthly premiums |
| Who Is Eligible | Californians with incomes at or below 138% of the federal poverty level | Californians who need insurance and aren't eligible for Medi-Cal |
| When You Can Apply | Any time of year | During open enrollment — or special enrollment if you experience a major life change |

**FAQ / accordions (11)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Programs You Already Use
- Other Factors
- Can I decline Medi-Cal?
- I applied for Medi-Cal but haven’t received any information from the county. What should I do?
- What if my income or situation changes?

#### `/coverage-basics/medi-cal/children`

*Medi-Cal for Children | Covered California* — 22 headings, 0 table(s), 0 card group(s), 10 FAQ item(s), 368,470 bytes

**FAQ / accordions (10)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Does my child qualify?
- Compare Medi-Cal and CCHIP
- Covered Benefits for Children
- Families with Mixed Program Eligibility

#### `/coverage-basics/medi-cal/mixed-program-families`

*Medi-Cal for Mixed Program Families | Covered California* — 18 headings, 1 table(s), 0 card group(s), 6 FAQ item(s), 343,711 bytes

**Table 1** — 2 rows x 3 cols

| If a family member qualifies for… | Cost and Coverage | What to Do Next |
|---|---|---|
| A Covered California plan | They can choose a health plan and may qualify for financial help that lowers monthly premiums and out-of-pocket costs. | Compare plans, total costs and doctor networks before enrolling. |
| Medi-Cal | They can get low-cost or no-cost health insurance through Medi-Cal. | Watch for next steps or notices from your county or Medi-Cal. |

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/coverage-basics/medi-cal/pregnant-individuals`

*Medi-Cal for Pregnancy | Covered California* — 18 headings, 1 table(s), 0 card group(s), 11 FAQ item(s), 351,479 bytes

**Table 1** — 4 rows x 4 cols

| Program | Whom It Helps | What It Covers | How Long Insurance Lasts |
|---|---|---|---|
| Full-Scope Medi-Cal | Pregnant people who meet standard Medi-Cal eligibility requirements | Prenatal care, labor and delivery, postpartum care, dental, mental health and other medically necessary services | Pregnancy, plus 12 months after pregnancy ends |
| Medi-Cal for Pregnant Individuals | Pregnant people living in California who aren’t legal residents, and who don’t qualify for full-scope Medi-Cal | All medically necessary services, plus dental and mental health services | Pregnancy, plus 12 months after pregnancy ends |
| Medi-Cal Access Program (MCAP) | Pregnant people whose income is too high for other Medi-Cal programs | Comprehensive insurance at no cost, with no copays or deductibles for covered services | Pregnancy, plus 12 months after pregnancy ends |
| Presumptive Eligibility for Pregnant Individuals | Pregnant people — or those who think they may be pregnant — who need insurance right away while they wait for their Medi-Cal application to be processed | Prenatal care, care related to pregnancy loss and prescription drugs related to pregnancy. It does not cover labor and delivery or other hospitalization. | Up to 60 days |

**FAQ / accordions (11)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- How does pregnancy affect my Medi-Cal eligibility?
- Can I apply if I’m already pregnant?
- What if I need care right away?
- Does pregnancy qualify me for Covered California special enrollment?
- What happens to my insurance after my baby is born?

#### `/coverage-basics/tax-penalty-details-and-exemptions`

*Penalty Details and Exemptions | Covered California* — 29 headings, 1 table(s), 0 card group(s), 10 FAQ item(s), 424,095 bytes

**Table 1** — 5 rows x 3 cols

|   | Franchise Tax Board (FTB) | Covered California |
|---|---|---|
| When | After the year ends when you file your state taxes | During the year, for current or future months only |
| Based On | Your actual income and situation for the prior year | Your projected household income or current circumstances |
| Who Processes It | Franchise Tax Board (FTB); no Covered California involvement | Covered California reviews and approves; issues an exemption certificate (ECN) |
| How to Claim | Complete Form FTB 3853 with your state tax return | Submit an application with supporting proof |
| Note on Affordability | If insurance was unaffordable based on your actual income, claim this exemption at tax time | If insurance is unaffordable based on your projected income, apply through Covered California during the year |

**FAQ / accordions (10)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Do I need to apply for an exemption if I don’t file state taxes?
- How long does a Covered California exemption decision take?
- What if some people in my household are eligible and others aren’t?
- What if I disagree with the decision?

#### `/coverage-basics/tax-penalty-details-and-exemptions/ftb-form-3853`

*Form FTB 3853 | Covered California* — 27 headings, 0 table(s), 0 card group(s), 9 FAQ item(s), 386,791 bytes

**FAQ / accordions (9)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- What exemptions can I claim directly on Form FTB 3853?
- What is the Marketplace Coverage Affordability Worksheet?
- What if my tax software doesn't ask me about Form FTB 3853?

#### `/coverage-basics/vision`

*Vision Insurance | Covered California* — 24 headings, 1 table(s), 0 card group(s), 9 FAQ item(s), 364,924 bytes

**Table 1** — 4 rows x 3 cols

|   | EyeMed | VSP |
|---|---|---|
| Network | Independent eye care professionals + national/regional retail chains: LensCrafters, Pearle Vision, Target Optical | Largest national network of independent doctors + retail chains: Costco Optical, Walmart, Sam's Club — 94,000 access points |
| Plan options | 3 | 2 |
| Enrollment | Year-round, direct through EyeMed | Year-round, direct through VSP |
| Phone | (844) 225-3107 | (800) 410-1857 |

**FAQ / accordions (9)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Can I enroll in adult vision insurance at any time?
- When does my child's vision plan start?
- Whom do I contact with questions about a vision plan?


### costs

#### `/costs`

*Costs and Financial Help | Covered California* — 17 headings, 1 table(s), 0 card group(s), 6 FAQ item(s), 356,608 bytes

**Table 1** — 6 rows x 2 cols

| Type of Cost | What It Means |
|---|---|
| Premium | The amount you pay each month to have a health plan. |
| Deductible | The amount you pay for covered services before your plan starts paying. |
| Copay | A fixed amount you pay for a covered service, like a doctor visit or prescription. |
| Coinsurance | Your share of the cost for a covered service, usually a percentage, after you meet your deductible. |
| Out-of-pocket costs | What you pay yourself for care. This includes deductibles, copays and coinsurance. |
| Out-of-pocket maximum | The most you'll pay in a year for covered services. After that, your plan pays 100% of covered costs. |

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/costs/financial-help`

*Financial Help | Covered California* — 37 headings, 0 table(s), 2 card group(s), 10 FAQ item(s), 436,249 bytes

**Card group 1**

- **Advance Premium Tax Credit (APTC)**
  - A federal tax credit created to help people afford health insurance.
  - Use it to lower your monthly bill, or claim it when you file your federal taxes.
  - Available if your income is between 100% FPL to 400% FPL.
  - Available to use with any plan coverage level.
- **Cost-sharing reductions**
  - Lower out-of-pocket costs, like your deductible, copays and coinsurance.
  - Available if your income is 250% FPL or less.
  - Included with Enhanced Silver plans.
- **California Premium Subsidy (state subsidy)**
  - Some households get extra money to lower their premium.
  - Available for households that qualify based on income, agreement to file taxes and enrollment in a Covered California health plan.
  - Must apply for free or low-cost health insurance and meet all eligibility requirements for APTC.

**Card group 2**

- **Counts**
  - Wages and salary
  - Tips
  - Self-employment income
  - Unemployment
  - Social Security benefits
  - Social Security Disability (SSDI)
  - Retirement or pension income
  - Investment income
- **Doesn’t Count**
  - Child support
  - Gifts
  - Veteran disability payments
  - Supplemental Security Income (SSI)
  - Workers' compensation
  - Money from loans, like student or home equity loans
  - Child Tax Credit

**FAQ / accordions (10)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- What if I don’t qualify for financial help?
- What if I need to prove my income?
- What if my income changes?
- What if I drive for a rideshare or delivery company?

#### `/costs/financial-help/employer-coverage`

*Employer Coverage and Financial Help | Covered California* — 18 headings, 1 table(s), 0 card group(s), 6 FAQ item(s), 364,404 bytes

**Table 1** — 3 rows x 3 cols

| If your cost is | And your family's cost is | Who can get financial help? |
|---|---|---|
| 9.96% or less | 9.96% or less | No one |
| 9.96% or less | More than 9.96% | Your family, not you |
| More than 9.96% | More than 9.96% | You and family |

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/costs/financial-help/health-reimbursement-arrangements`

*Health Reimbursement Arrangements (HRA) | Covered California* — 16 headings, 1 table(s), 0 card group(s), 7 FAQ item(s), 357,331 bytes

**Table 1** — 2 rows x 4 cols

| HRA Type | Eligibility | Advantages | Column 3 |
|---|---|---|---|
| ICHRA | Employers set eligibility rules | Reimbursements are tax-free Employees can shop for plans that work for them | Can affect ability to receive premium subsidies |
| QSEHRA | Must include all full-time employees | Works with other group plans Can use funds for premiums and qualified medical expenses | Caps on reimbursement amount Must maintain minimum essential coverage to get premium subsidies |

**FAQ / accordions (7)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Monthly premiums

#### `/costs/financial-help/health-reimbursement-arrangements/hra-affordability-calculator`

*HRA Affordability Calculator | Covered California* — 12 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 335,352 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### enrollment

#### `/enrollment`

*Eligibility and Enrollment | Covered California* — 33 headings, 0 table(s), 1 card group(s), 9 FAQ item(s), 477,638 bytes

**Card group 1**

- **Open Enrollment**
  - Nov. 1 to Jan. 31
  - The time every year where eligible Californians can enroll, renew or change their plan.
- **Special Enrollment**
  - Available Year-Round
  - Open to Californians who recently experienced a , like lost health insurance, got married, had a baby, moved or changed their immigration status. major life change

**FAQ / accordions (9)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- What if I have a pre-existing condition?
- Do I qualify if I'm not a citizen or don't have lawful immigration status?
- What if I'm not sure which program I qualify for?

#### `/enrollment/documents`

*Documents to Confirm Eligibility | Covered California* — 19 headings, 1 table(s), 0 card group(s), 6 FAQ item(s), 357,258 bytes

**Table 1** — 4 rows x 2 cols

| Method | What to Know |
|---|---|
| Online | and upload documents through your Household Summary, Eligibility Results, or Documents and Correspondence sections. Sign in to your account |
| By Fax | Fax copies of your documents, including the , to (888) 329-3700. document cover page (PDF) |
| By Mail | Mail copies, including the , to: Covered CaliforniaP.O. Box 989725West Sacramento, CA 95798-9725 document cover page (PDF) |
| In Person | from certified enrollers, insurance agents and county eligibility workers. Find free local help |

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/documents/american-indian-or-alaskan-native`

*American Indian or Alaska Native Documentation | Covered California* — 18 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 341,162 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/documents/citizenship`

*Proof of Citizenship | Covered California* — 29 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 394,002 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/documents/identity`

*Proof of Identity | Covered California* — 23 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 366,556 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/documents/immigration-status`

*Proof of Immigration Status or Lawful Presence | Covered California* — 25 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 508,673 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/documents/income`

*Proof of Income | Covered California* — 29 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 387,808 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/documents/minimum-essential-coverage`

*Minimum Essential Coverage | Covered California* — 17 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 349,556 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/documents/not-incarcerated`

*Proof of Non-Incarcerated Status | Covered California* — 19 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 348,058 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/documents/notification-of-a-deceased-member`

*Notification of Deceased Status | Covered California* — 18 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 357,281 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/documents/social-security-number`

*Proof of Social Security Number | Covered California* — 17 headings, 1 table(s), 0 card group(s), 6 FAQ item(s), 343,082 bytes

**Table 1** — 3 rows x 2 cols

| If this applies to you: | Submit one of these documents: |
|---|---|
| You have a document with your SSN. | Social Security card Tax form Benefit or income statement from Social Security that shows the Social Security number |
| Your SSN is pending or unavailable. | Tax form Benefit or income statement from Social Security that shows the Social Security number |
| You have an established religious objection. | Letter stating that the applicant refuses to obtain an SSN for established religious objections (also called an SSN Waiver) |

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/eligibility`

*Eligibility Guidelines | Covered California* — 35 headings, 1 table(s), 1 card group(s), 6 FAQ item(s), 399,094 bytes

**Table 1** — 3 rows x 2 cols

| Program | Who It’s For |
|---|---|
| Covered California | California residents who are lawfully present. Depending on income, you may also qualify for financial help to lower your cost. |
| Medi-Cal | People with lower incomes, children, pregnant individuals and others who meet Medi-Cal eligibility criteria. |
| Mixed-Program Family | Families where some members qualify for Medi-Cal and others qualify for Covered California. |

**Card group 1**

- **Your Household**
  - You
  - Anyone you claim as a tax dependent
- **Your Income**
  - We look at your household’s estimated yearly income and household size to determine what programs and financial help you may qualify for.
  - Good to know
  - Income is measured against the federal poverty level for your household size.
- **Where You Live**
  - You must be a California resident.
  - Good to know
  - Moving to California from out of state is a major life change that may let you enroll outside open enrollment.
- **Citizenship or Immigration Status**
  - For people who are applying for health insurance.
  - Good to know
  - Only the people applying need to share Social Security numbers or immigration information. The rest of your household can still be listed.
- **Current Health Insurance**
  - Including insurance through your job, Medicare or other insurance.
  - Good to know
  - Having other health insurance doesn't disqualify you from applying, but it may affect whether you qualify for financial help.
- **Other Factors**
  - Some eligibility rules depend on your age, disability status and other specific situations.
  - Good to know
  - These factors may affect which health insurance options are available to you.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/eligibility/american-indians-alaska-natives`

*Coverage for American Indians and Alaska Natives | Covered California* — 27 headings, 0 table(s), 0 card group(s), 11 FAQ item(s), 375,410 bytes

**FAQ / accordions (11)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- major life change
- I am AI/AN, but not a member of a federally recognized tribe. Do I have options?
- What happens if some people in my household are AI/AN and others are not?
- Can I still use the Indian Health Service (IHS), tribal programs or urban Indian health programs if I enroll in Covered California?
- What if I want to see a doctor outside the tribal or Indian health system?

#### `/enrollment/eligibility/immigrants`

*Information for Immigrants | Covered California* — 29 headings, 1 table(s), 0 card group(s), 10 FAQ item(s), 418,328 bytes

**Table 1** — 4 rows x 3 cols

| Status | Covered California | Medi-Cal |
|---|---|---|
| Lawfully present | Eligible | Varies: see below |
| Not lawfully present | Not eligible | Limited: see below |
| DACA recipient | Not eligible | Limited: see below |
| Mixed-status family | Eligibility varies by person | Eligibility varies by person |

**FAQ / accordions (10)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- What documents do I need?
- Do I need a Social Security number to apply?
- Can I get help applying in my language?
- Will my information be kept confidential?

#### `/enrollment/eligibility/people-with-chronic-conditions`

*People with Chronic Conditions | Covered California* — 19 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 358,512 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/enrollment/losing-medi-cal-coverage`

*Losing Medi-Cal Coverage | Covered California* — 23 headings, 1 table(s), 0 card group(s), 11 FAQ item(s), 368,022 bytes

**Table 1** — 3 rows x 3 cols

| Your Situation | What Happened | What to Do |
|---|---|---|
| A plan was selected for you. | California law requires Covered California to enroll you in a plan so you don’t have a gap in coverage. We picked the one with the most financial help. | You don’t have to keep the plan chosen for you. to keep, change or cancel it. Sign in to your account |
| A plan was not selected for you. | You may not qualify for financial help through Covered California. | Double check the information on your application and see if you qualify for financial help. If you still don’t qualify, you can compare plans and costs, then select a plan and make your first payment. |
| You think your Medi-Cal ended by mistake. | Your county may need to review or correct your information. | . Contact your local Medi-Cal county office |

**FAQ / accordions (11)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- out-of-pocket costs
- What will my new plan cost?
- Can I keep my doctor?
- Will my benefits stay the same?
- What if my employer offers health insurance?

#### `/enrollment/major-life-changes`

*Major Life Changes | Covered California* — 33 headings, 1 table(s), 1 card group(s), 11 FAQ item(s), 414,204 bytes

**Table 1** — 6 rows x 3 cols

| Situation | When to Act | What to Consider |
|---|---|---|
| Marriage, divorce, domestic partnership or a death in your household | Within 60 days of the event | Coverage typically starts the first of the month after you choose a plan |
| Lost job-based insurance | 60 days before or after your coverage ends to apply | Apply before insurance ends to avoid a gap |
| Lost Medi-Cal coverage | Within 90 days of your Medi-Cal ending | Covered California may automatically select a plan for you |
| Moved to or within California | Within 60 days of moving. You may be able to report your move before it happens. | Coverage start date may depend on your move date |
| Released from jail or prison | Within 60 days of your release | Coverage typically starts the first of the month after your release date or plan selection, whichever is later |
| Birth, adoption or foster placement | Within 60 days of the event | Coverage start options may vary; Covered California will show your date after you apply |

**Card group 1**

- **Lost or Will Lose Health Insurance**
  - Lost health insurance through your job
  - Lost Medi-Cal coverage
  - Lost student health coverage
  - COBRA coverage ended
  - Aged off a parent’s or child-only plan
- **Family or Household Changes**
  - Got married or entered a domestic partnership
  - Had a baby, adopted a child or began foster care
  - Got divorced or legally separated
  - Had a death in the household that affects coverage
- **Moved to or Within California**
  - Moved to California from another state
  - Moved within California and plan options changed
- **Status Changes**
  - Gained citizenship, national status or lawful presence
  - Lost insurance after military service
  - Lost insurance tied to military service
- **Special Situations**
  - Experienced domestic abuse or spousal abandonment
  - Were released from jail or prison
  - Are a federally recognized American Indian or Alaska Native member
- **Changes to Existing Enrollment**
  - Lost financial help after an income change
  - Lost financial help after a household change
  - Lost insurance after a household member died

**FAQ / accordions (11)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- financial help
- Can I apply before my current health plan ends?
- Does pregnancy count as a major life change?
- What counts as losing COBRA coverage for special-enrollment purposes?
- What documents will I need?

#### `/enrollment/major-life-changes/domestic-abuse`

*Domestic Abuse or Spousal Abandonment | Covered California* — 20 headings, 0 table(s), 0 card group(s), 10 FAQ item(s), 351,314 bytes

**FAQ / accordions (10)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Do I need to show proof of domestic abuse or spousal abandonment?
- What if I’m still legally married?
- What if I’m already enrolled with my spouse or partner?
- What if I get financial help?

#### `/enrollment/open-enrollment`

*Open Enrollment | Covered California* — 26 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 361,734 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### account

#### `/account`

*Managing Your Account | Covered California* — 24 headings, 0 table(s), 0 card group(s), 13 FAQ item(s), 445,059 bytes

**FAQ / accordions (13)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- I lost my health insurance
- My family or household changed
- My immigration status changed
- I am an American Indian or Alaska Native
- My income, job or benefits changed
- I want to re-enroll
- None of these apply to me

#### `/account/billing`

*Guide to Your Bill and Payments | Covered California* — 22 headings, 0 table(s), 0 card group(s), 9 FAQ item(s), 344,194 bytes

**FAQ / accordions (9)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- What if I haven't gotten my bill yet?
- Will I get a separate bill for dental or vision insurance?
- What if my bill amount changes?

#### `/account/cancel`

*Cancel Your Plan | Covered California* — 25 headings, 0 table(s), 0 card group(s), 10 FAQ item(s), 360,528 bytes

**FAQ / accordions (10)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- What if I was moved from Medi-Cal to a Covered California plan?
- Will canceling my health plan also cancel my dental plan?
- What if I already paid my premium for next month?
- Are there penalties for canceling my plan?

#### `/account/file-an-appeal`

*File an Appeal or a Complaint | Covered California* — 36 headings, 0 table(s), 0 card group(s), 14 FAQ item(s), 393,969 bytes

**FAQ / accordions (14)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- financial help
- cost-sharing reductions
- major life change
- Can I file an appeal for someone in my household?
- What if I need help in another language or an accessible format?
- What if I have an active appeal?
- How do I fix a problem with my Medi-Cal eligibility?
- Where can I get legal advice?

#### `/account/guide-to-your-account`

*Guide to Your Account | Covered California* — 30 headings, 0 table(s), 1 card group(s), 8 FAQ item(s), 402,452 bytes

**Card group 1**

- **Forgot your password**
  - 1. Select on the sign-in page. Forgot password?
  - 2. Enter your username and date of birth — we'll send a one-time passcode.
  - 3. Enter the passcode, then create a new password.
- **Forgot your username**
  - 1. On the sign-in page, select Forgot username?
  - 2. Enter your email address and date of birth.
  - 3. We'll send your username to your email.
- **Account is locked**
  - Call us at to unlock your account. We’ll just need to confirm it’s you first. (800) 300-1506

**FAQ / accordions (8)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- I haven’t applied yet.
- I have an access code.

#### `/account/renew`

*How to Renew Your Plan | Covered California* — 28 headings, 1 table(s), 1 card group(s), 9 FAQ item(s), 400,545 bytes

**Table 1** — 3 rows x 3 cols

| Renewal Topic | Covered California | Medi-Cal |
|---|---|---|
| When it happens | Each October during the renewal period | Happens throughout the year based on your Medi-Cal anniversary date |
| Who contacts you | Covered California sends renewal information or account notices | Your county may contact you if information is needed |
| What to do | Review your application, compare options, keep or change your plan | Follow the instructions in your renewal notice; some renewals are automatic |

**Card group 1**

- **Household and Contact Information**
  - Confirm that your address, phone number and email are up to date.
  - Add anyone who joined your household.
  - Remove anyone who moved out or is no longer a dependent.
- **Income and Financial Help**
  - Financial help changed
  - Program eligibility changed
- **Plan Options**
  - Your doctors and hospitals are in network
  - Your prescriptions are covered
  - The costs fit your budget

**FAQ / accordions (9)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Can I change plans outside of renewal?
- Can my financial help change when I renew?
- What if I didn’t apply for financial help before?

#### `/account/renew/moving-to-medicare`

*Moving to Medicare | Covered California* — 19 headings, 0 table(s), 0 card group(s), 9 FAQ item(s), 355,565 bytes

**FAQ / accordions (9)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- I got a notice saying I'm eligible for Medicare. What should I do?
- Will Covered California automatically cancel my health plan when I enroll in Medicare?
- What happens if I have to pay a premium for Medicare Part A?

#### `/account/tax-forms`

*Understanding Your Tax Forms | Covered California* — 22 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 372,766 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/account/using-your-plan`

*Guide to Using Your Plan | Covered California* — 30 headings, 0 table(s), 1 card group(s), 7 FAQ item(s), 397,903 bytes

**Card group 1**

- **Make Your First Payment**
  - Your plan starts once you pay your first bill.
  - If you didn't pay when you enrolled, be sure to make your first payment to your health insurance company (not Covered California) to start using your plan.
- **Check Your Providers**
  - Make sure your doctors, specialists and pharmacies are in your plan's network.
  - Seeing an out-of-network provider can mean paying the full cost yourself. Check your plan's directory first.
- **Get Care**
  - You can get care as soon as your plan starts — no need to wait for your ID card.
  - Just make sure your first payment is processed. If your plan is canceled for non-payment, you'll owe the full cost of any care you received.
- **Watch for Mail**
  - Covered California will send a welcome letter and brochure.
  - Your insurance company will send your ID card and enrollment packet.

**FAQ / accordions (7)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- essential health benefits

#### `/account/using-your-plan/enrollee-programs`

*Enrollee Programs | Covered California* — 24 headings, 1 table(s), 0 card group(s), 10 FAQ item(s), 356,965 bytes

**Table 1** — 4 rows x 3 cols

|   | Grocery Support Program | Child Scholarship Account Program |
|---|---|---|
| What it offers | A reloadable debit card for groceries | Up to $1,000 in your child's CalKIDS scholarship account |
| Who may be invited | Enrollees with a chronic health condition and household income at or below 250% of the federal poverty level | Enrollees with California-born children under 18 months old |
| What you may need to do | Reply to FORWARD's invitation and complete enrollment | Complete well-child visits and vaccines; claim your child's CalKIDS account |
| Availability | Limited — first come, first served | Limited — first come, first served |

**FAQ / accordions (10)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- How long will Beyond Covered last?
- I have more questions. Where can I get help?
- Are Beyond Covered benefits taxable? Will they affect CalFresh or TANF?
- I think I qualify. Why hasn't FORWARD contacted me yet?

#### `/account/using-your-plan/free-preventive-care-for-adults`

*Free Preventive Care for Adults | Covered California* — 15 headings, 1 table(s), 0 card group(s), 9 FAQ item(s), 367,101 bytes

**Table 1** — 11 rows x 3 cols

| Service | What It Is | When It's Covered |
|---|---|---|
| Annual wellness exam | A yearly checkup to review your overall health, catch issues early and stay up to date on vaccines | Every year |
| Blood pressure screening | A check of your blood pressure to catch high blood pressure early | Every year |
| Cholesterol screening | A blood test to check cholesterol levels and help prevent heart disease based on age and risk | Usually every 4-6 years |
| Abdominal aortic aneurysm screening | An ultrasound to check for an aortic aneurysm in men aged 65-75 who have smoked | Once per lifetime |
| Obesity screening and counseling | Weight checks and support to reach or maintain a healthy weight | Ongoing |
| Type 2 diabetes screening | A blood sugar test to catch diabetes early in adults with high blood pressure | Every year |
| Diet counseling | Nutrition advice for adults at higher risk for chronic disease | As needed |
| Skin cancer counseling | Guidance on protecting your skin and lowering skin cancer risk | Adults at high risk |
| Fall-prevention counseling | Advice on preventing falls, including exercise and home safety tips for adults 65+ | Every year |
| Colorectal cancer screening | A test for colon cancer for adults 45+ | Every 1–10 years depending on the test |
| Lung cancer screening | People at high risk, like long-time smokers | Every year |

**FAQ / accordions (9)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Wellness and Screenings
- Mental Health and Substance Use
- Sexual and Reproductive Health

#### `/account/using-your-plan/free-preventive-care-for-children`

*Free Preventive Care for Children | Covered California* — 15 headings, 1 table(s), 0 card group(s), 8 FAQ item(s), 369,583 bytes

**Table 1** — 11 rows x 3 cols

| Service | What It Is | When It’s Covered |
|---|---|---|
| Wellness exams | Regular checkups to track your child's growth, development and overall health | Throughout childhood |
| Medical history | A review of your child's health history at each visit to catch concerns early | Through age 17 |
| Height, weight and BMI measurements | Tracking height, weight and BMI to watch growth and prevent obesity | Through age 17 |
| Behavioral assessments | Check-ins to spot emotional or behavioral concerns early | Through age 17 |
| Developmental screening | Screenings to make sure babies and toddlers are developing on track | Through age 3 |
| Autism screening | A check to look for early signs of autism | At 18 and 24 months |
| Vision screening | Routine vision tests to catch problems early | Throughout childhood |
| Newborn hearing screening | A hearing test to detect hearing loss early | At birth |
| Depression screening | Screenings to check for signs of depression, with referrals to support as needed | Children and teens |
| Tobacco use prevention | Counseling to help prevent tobacco use | Through age 17 |
| Alcohol, tobacco and drug use assessments | Discussions to help prevent misuse of alcohol, tobacco and drugs | Through age 17 |

**FAQ / accordions (8)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Wellness and Development
- Screenings and Supplements

#### `/account/using-your-plan/free-preventive-care-for-women`

*Free Preventive Care for Women | Covered California* — 15 headings, 1 table(s), 0 card group(s), 9 FAQ item(s), 353,282 bytes

**Table 1** — 7 rows x 3 cols

| Service | What It Is | When It's Covered |
|---|---|---|
| Well-woman visit | An annual checkup to review your overall reproductive and general health, screenings and preventive care needs | Every year |
| Cervical cancer screening | A Pap test to find early signs of cervical cancer | Every 3 years for most women starting at age 21 |
| HPV DNA test | A test to find high-risk HPV types that cause cervical cancer | Every 3 years for women 30+ with normal results |
| Osteoporosis screening | A bone density test to check for osteoporosis and help prevent fractures for women over 60 | As needed, depending on risk |
| Urinary incontinence screening | A yearly check and help managing incontinence, if needed | Every year |
| Tobacco screening and cessation support | Screening for tobacco use, with help to quit if needed, plus extra counseling during pregnancy | As needed |
| Domestic and interpersonal violence screening and counseling | Private counseling and support if you may be experiencing domestic or interpersonal violence | As needed |

**FAQ / accordions (9)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Well-Woman Care
- Breast and Reproductive Health
- Pregnancy and Maternal Health

#### `/account/using-your-plan/mental-health`

*Mental Health and Therapy Coverage | Covered California* — 19 headings, 0 table(s), 0 card group(s), 7 FAQ item(s), 355,150 bytes

**FAQ / accordions (7)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- out-of-pocket costs


### get-help

#### `/get-help`

*Get Help | Covered California* — 26 headings, 1 table(s), 0 card group(s), 6 FAQ item(s), 405,039 bytes

**Table 1** — 15 rows x 2 cols

| Language | Phone Number |
|---|---|
| English | (800) 300-1506 |
| Español (Spanish) | (800) 300-0213 |
| العربية (Arabic) | (800) 826-6317 |
| հայերեն (Armenian) | (800) 996-1009 |
| 粵語 (Cantonese) | (800) 339-8938 |
| فارسی (Farsi) | (800) 921-8879 |
| Tagalog (Filipino) | (800) 983-8816 |
| Hmoob (Hmong) | (800) 771-2156 |
| ខ្មែរ (Khmer) | (800) 906-8528 |
| 한국어 (Korean) | (800) 738-9116 |
| ລາວ (Lao) | (800) 357-7976 |
| 國語 (Mandarin) | (800) 300-1533 |
| русский (Russian) | (800) 778-7695 |
| Tiếng Việt (Vietnamese) | (800) 652-9528 |
| TTY | (888) 889-4500 |

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/get-help/events`

*Events | Covered California* — 16 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 416,290 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/get-help/find-an-enroller`

*Find an Enroller | Covered California* — 9 headings, 0 table(s), 0 card group(s), 7 FAQ item(s), 292,720 bytes

**FAQ / accordions (7)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Search Filters

#### `/get-help/help-on-demand`

*Help on Demand | Covered California* — 9 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 299,276 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

#### `/get-help/live-chat`

*Chat with a member of our support team | Covered California* — 9 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 277,468 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### consumer-protection

#### `/consumer-protection`

*Consumer Protection | Covered California* — 19 headings, 1 table(s), 0 card group(s), 6 FAQ item(s), 355,401 bytes

**Table 1** — 7 rows x 2 cols

| Fact | Scam |
|---|---|
| CoveredCA.com is the official website and the only place online to enroll in a Covered California health plan. | A website asks you to enter personal information to enroll, but it isn't the official Covered California site. |
| Monthly premiums are paid directly to your health insurance company or to Covered California Licensed Insurance Agent. | A website asks you to enter your confidential information to make a payment but isn’t an official site. |
| Enrollment help from Covered California is always free. | A representative charges a fee to help you enroll. |
| Covered California certified representatives never ask for cash payments. | A representative asks to be paid in cash. |
| You don’t need to share your personal information in order to learn about your health insurance options through Covered California. | Representatives requesting your personal information over the phone or door-to-door without a clear reason. |
| There are no criminal penalties for not having health insurance. There is a financial penalty in California. Covered California and its partners will never pressure you to buy a plan. | A salesperson says you will go to jail if you don’t buy insurance, or they offer a one-time-only special discount. |
| Medicare recipients do not need to take action to keep their insurance because of the Affordable Care Act. | A caller requests your Social Security number and personal information to continue Medicare eligibility. |

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### insurance-company-contacts

#### `/insurance-company-contacts`

*Insurance Company Contacts | Covered California* — 37 headings, 0 table(s), 0 card group(s), 21 FAQ item(s), 431,270 bytes

**FAQ / accordions (21)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Anthem Blue Cross of California
- Balance by CCHP
- Blue Shield of California
- CalOptima Health
- Health Net (Ambetter)
- Inland Empire Health Plan
- Kaiser Permanente
- L.A. Care Health Plan
- Molina Healthcare
- Sharp Health Plan
- Valley Health Plan
- Western Health Advantage
- Anthem Blue Cross Dental
- Blue Shield of California Dental
- California Dental Network (DentaQuest)


### ombuds-office

#### `/ombuds-office`

*Ombuds Office | Covered California* — 26 headings, 0 table(s), 0 card group(s), 14 FAQ item(s), 388,019 bytes

**FAQ / accordions (14)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- What if I need legal advice?
- What if my issue is with Medi-Cal eligibility?
- What can the Covered California service center help with?
- What if I have a complaint about my health insurance company?
- What if I have a complaint about my insurance agent or broker?
- What if my issue involves a state prison or correctional facility?
- What if I or someone I know needs protection from abuse or neglect?
- What if I or someone I know needs support services for older adults?


### small-business

#### `/small-business`

*Covered California for Small Business | Covered California for Small Business* — 25 headings, 0 table(s), 1 card group(s), 9 FAQ item(s), 389,329 bytes

**Card group 1**

- **Choose What to Offer**
  - Select the coverage levels — Bronze, Silver, Gold or Platinum — that you want to make available to your employees. You can offer anywhere from one tier to all four, and add dental insurance as an option.
- **Control Your Costs**
  - You decide how much to contribute toward employee premiums. Receive one monthly bill for all your coverage, making it easier to manage and budget for health benefits.
- **Let Employees Choose Their Plans**
  - Employees pick the plans that work best for their needs and budget from the options you offer. Enrollment is year-round, so adding or removing employees is easy.

**FAQ / accordions (9)**

- For Enrollment Partners
- For Small Business
- Applications & Forms
- Tax Credits for Employers
- Is CCSB right for you?
- What types of plans are available?
- What kinds of businesses qualify for Covered California for Small Business?
- What does small business insurance cost? Are tax credits available?
- How and when can I enroll my business?

#### `/small-business/apply`

*How to Apply | Covered California for Small Business* — 30 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 375,273 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Small Business
- Applications & Forms
- Can I get help before I choose a plan?
- Can I enroll at any time of year?
- What happens after I submit my application?

#### `/small-business/contact`

*Contact Us | Covered California for Small Business* — 28 headings, 0 table(s), 0 card group(s), 3 FAQ item(s), 326,584 bytes

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/costs-and-financial-help`

*Financial Help for Employers | Covered California for Small Business* — 26 headings, 0 table(s), 0 card group(s), 7 FAQ item(s), 375,080 bytes

**FAQ / accordions (7)**

- For Enrollment Partners
- For Small Business
- Applications & Forms
- What is a full-time-equivalent employee?
- Do all small businesses qualify for the tax credit?
- Is this the same as financial help for individuals and families?
- How can I get help understanding my costs?

#### `/small-business/dental-plans`

*Dental Plans | Covered California for Small Business* — 24 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 356,522 bytes

**Card group 1**

- **Employee and Dependent Choice**
  - Employees can pick a dental insurance plan for themselves and their dependents through the CCSB application.
- **Plan Types – HMO and PPO**
  - Dental plans are available in HMO and PPO formats, with options for children only or the full family. HMO plans typically have lower premiums with a network of assigned dentists, while PPO plans offer more provider flexibility.
- **Benefits, Limitations and Exclusions**
  - Review plan documents to understand what dental services are covered, what restrictions apply and what services are not included. This helps employers and employees understand what to expect from their dental coverage.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Small Business
- Applications & Forms
- Can employees get dental insurance for their dependents?
- Does my business have to contribute to dental premiums?
- When can dental insurance be added?

#### `/small-business/dental-plans/delta-dental`

*Delta Dental of California | Covered California for Small Business | Covered California for Small Business* — 19 headings, 0 table(s), 0 card group(s), 3 FAQ item(s), 347,548 bytes

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/eligibility`

*Eligibility Guidelines | Covered California for Small Business* — 20 headings, 1 table(s), 0 card group(s), 5 FAQ item(s), 380,418 bytes

**Table 1** — 5 rows x 3 cols

| Employee Category | Eligibility Criteria | Insurance Eligibility |
|---|---|---|
| Full-time employees | 30 or more hours per week | Eligible for health insurance |
| Part-time employees | 20-29 hours per week | May be offered health insurance at the employer's discretion |
| Part-time employees | Fewer than 20 hours per week | Not eligible through CCSB |
| Seasonal or temporary employees | Employment type | Not eligible through CCSB |
| Form 1099 workers | Employment type | Not eligible through CCSB |

**FAQ / accordions (5)**

- For Enrollment Partners
- For Small Business
- Applications & Forms
- What if I’m a sole proprietor?
- What if my business has more than 100 full-time-equivalent employees?

#### `/small-business/employee-forms`

*Applications and Forms for Employees | Covered California for Small Business* — 20 headings, 0 table(s), 0 card group(s), 3 FAQ item(s), 344,565 bytes

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/employer-forms`

*Applications and Forms for Employers | Covered California for Small Business* — 21 headings, 0 table(s), 0 card group(s), 3 FAQ item(s), 361,638 bytes

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/enrollment-support`

*Enrollment support | Covered California for Small Business* — 8 headings, 0 table(s), 0 card group(s), 3 FAQ item(s), 270,303 bytes

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/get-a-quote`

*Get a Quote | Covered California for Small Business* — 8 headings, 0 table(s), 0 card group(s), 3 FAQ item(s), 276,536 bytes

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/health-plans`

*Health Plans | Covered California for Small Business* — 35 headings, 1 table(s), 1 card group(s), 3 FAQ item(s), 409,899 bytes

**Table 1** — 4 rows x 3 cols

| Tiers Offered | What Employees Can Choose From | What You Can Offer |
|---|---|---|
| 4 metal tiers | All four metal tiers | Bronze, Silver, Gold and Platinum |
| 3 metal tiers | Three touching tiers | Bronze, Silver and Gold Silver, Gold and Platinum or |
| 2 metal tiers | Two touching tiers | Bronze and Silver Silver and Gold Gold and Platinum or or |
| 1 metal tier | One tier of your choice | Bronze Silver Gold Platinum or or or |

**Card group 1**

- **Coverage Levels**
  - The coverage levels — Platinum, Gold, Silver and Bronze — organize plans by how costs are shared between the plan and the employee. Higher tiers generally mean lower out-of-pocket costs for employees and higher monthly premiums.
- **Networks**
  - Each carrier has its own network of doctors, hospitals and service areas. Review network summaries to understand which providers may be available to your employees.
- **Plan and Benefit Summaries**
  - CCSB provides standard benefit summaries for each plan tier. Review these documents to compare what each plan covers and how benefits may have changed from the prior year.
- **Creditable Coverage**
  - If your business has Medicare-eligible employees, you may be required to provide an annual written notice about whether your prescription drug coverage is creditable, meaning it meets Medicare Part D standards.

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/health-plans/blue-shield`

*Blue Shield | Covered California for Small Business* — 64 headings, 1 table(s), 0 card group(s), 3 FAQ item(s), 519,195 bytes

**Table 1** — 4 rows x 3 cols

| Rating Category | HMO | PPO |
|---|---|---|
| Overall rating | 3 out of 5 stars | 3 out of 5 stars |
| Getting the right care | 3 out of 5 stars | 3 out of 5 stars |
| Members' care experience | 4 out of 5 stars | 4 out of 5 stars |
| Members' care experience | 4 out of 5 stars | 3 out of 5 stars |

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/health-plans/kaiser`

*Kaiser Permanente | Covered California for Small Business* — 37 headings, 1 table(s), 0 card group(s), 3 FAQ item(s), 508,041 bytes

**Table 1** — 4 rows x 2 cols

| Rating Category | HMO |
|---|---|
| Overall rating | 5 out of 5 stars |
| Getting the right care | 5 out of 5 stars |
| Members' care experience | 4 out of 5 stars |
| Plan services for members | 5 out of 5 stars |

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/health-plans/sharp`

*Sharp Health Plan | Covered California for Small Business* — 49 headings, 1 table(s), 0 card group(s), 3 FAQ item(s), 459,574 bytes

**Table 1** — 4 rows x 2 cols

| Rating Category | HMO |
|---|---|
| Overall rating | 4 out of 5 stars |
| Getting the right care | 4 out of 5 stars |
| Members' care experience | 5 out of 5 stars |
| Plan services for members | 5 out of 5 stars |

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/health-plans/western-health-advantage`

*Western Health Advantage | Covered California for Small Business* — 24 headings, 0 table(s), 0 card group(s), 3 FAQ item(s), 357,243 bytes

**FAQ / accordions (3)**

- For Enrollment Partners
- For Small Business
- Applications & Forms

#### `/small-business/mandate`

*Employer Mandate | Covered California for Small Business* — 28 headings, 1 table(s), 0 card group(s), 9 FAQ item(s), 372,225 bytes

**Table 1** — 3 rows x 2 cols

|   | Column 1 |
|---|---|
| Your Business Size | Does the mandate apply? |
| Fewer than 50 full-time-equivalent employees | Generally no — you are not subject to employer shared responsibility provisions. If you choose to offer insurance, it must still meet Affordable Care Act requirements. |
| 50 or more full-time-equivalent employees | Likely yes — you may be an applicable large employer and required to offer qualifying health insurance or face IRS fees. |

**FAQ / accordions (9)**

- For Enrollment Partners
- For Small Business
- Applications & Forms
- employer shared responsibility payment
- Does every small business have to offer health insurance?
- What is a full-time equivalent employee?
- Does Covered California decide whether my business owes a penalty?
- Where can I find information on employer reporting forms?
- Can I get help choosing insurance for my employees?

#### `/small-business/mandate/1095-forms`

*1095 Forms and Reporting | Covered California for Small Business* — 34 headings, 2 table(s), 0 card group(s), 9 FAQ item(s), 398,178 bytes

**Table 1** — 3 rows x 4 cols

| Form | Usually Issued By | Who May Get It | What It Reports |
|---|---|---|---|
| Form 1095-B | The health insurance company (for employers with fewer than 50 full-time-equivalent employees) or a government agency (for Medi-Cal and other government-sponsored insurance) | Employees enrolled in a Covered California for Small Business health insurance plan, or recipients of government-sponsored insurance | Months of minimum essential coverage |
| Form 1095-C | The employer (for applicable large employers with 50 or more full-time equivalent employees) | Full-time employees of applicable large employers | Months of employer-sponsored insurance offered and employee premium share |
| W-2 (Box 12, Code DD) | The employer | All employees receiving applicable employer-sponsored insurance | Cost of employer-sponsored health insurance (informational only; not taxable income) |

**Table 2** — 5 rows x 2 cols

| Form 1095-C | Form 1094-C |
|---|---|
| Whether a health insurance plan was offered each month, and which plan | Whether insurance was offered to at least 95% of full-time employees and their dependents |
| Employee's share of the monthly premium for the lowest-cost self-only minimum value coverage | Information about any aggregated applicable large employer group members |
| Number of months the employee was enrolled in insurance | Full-time and total employee counts by month |
| If self-insured: information about covered individuals enrolled by month | Total number of Forms 1095-C issued |
| Whether an affordability safe harbor or other relief applies for any month | Whether you are eligible for certain transition relief |

**FAQ / accordions (9)**

- For Enrollment Partners
- For Small Business
- Applications & Forms
- Whom should an employee contact if their Form 1095-B has an error?
- Whom should an employee contact if their Form 1095-C has an error?
- What if my business sponsors a self-insured health insurance plan?
- What if my business is part of a common ownership group?
- Where can I find a qualified tax professional?
- Where can I find more IRS guidance on Affordable Care Act reporting requirements?

#### `/small-business/mandate/resources`

*Mandate Resources | Covered California for Small Business* — 29 headings, 1 table(s), 0 card group(s), 4 FAQ item(s), 389,536 bytes

**Table 1** — 9 rows x 3 cols

| If you need to… | Resource | What It Helps With |
|---|---|---|
| Understand employer shared responsibility rules | IRS Employer Shared Responsibility Provisions | Guidance, examples and FAQs on the employer mandate and related payments |
| Determine whether your business may be an applicable large employer | IRS Determining If an Employer Is an Applicable Large Employer | Step-by-step guidance on applicable large employer status |
| Estimate your full-time-equivalent employee count | Employer Shared Responsibility Provision Estimator | Full-time-equivalent calculator and applicable large employer determination tool |
| Estimate potential shared responsibility payments | IRS ACA Estimator Tools for Individuals and Employers | Additional calculators and decision support |
| Review ACA tax provisions for smaller businesses | IRS ACA Tax Provisions for Small Employers | Information tailored to employers with fewer than 50 full-time employees |
| Access a central hub for applicable large employer resources | IRS ACA Information Center for Applicable Large Employers | Central hub for applicable large employer-specific Affordable Care Act information and tools |
| Watch a guided walkthrough of employer shared responsibility rules | IRS ACA Employer Shared Responsibility Webinars | On-demand webinars covering employer shared responsibility rules and reporting steps |
| Find a qualified federal tax preparer | IRS Directory of Federal Tax Return Preparers | Search for credentialed preparers with a PTIN |
| Find a California-registered tax preparer | California Tax Education Council Directory of Registered Tax Preparers | Find preparers registered with the California Tax Education Council (CTEC) |

**FAQ / accordions (4)**

- For Enrollment Partners
- For Small Business
- Applications & Forms
- employer shared responsibility payment


### enrollment-partners-individuals

#### `/enrollment-partners-individuals`

*Enrollment Partners for Individuals & Families | Covered California* — 17 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 317,993 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- Individuals & Families
- Certifications
- Training & Education
- Marketing & Branding
- Client Support

#### `/enrollment-partners-individuals/become-a-certified-enroller`

*Become a Certified Enroller | Covered California* — 12 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 324,651 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- Individuals & Families
- Certifications
- Training & Education
- Marketing & Branding
- Client Support

#### `/enrollment-partners-individuals/become-an-agent`

*Become an Agent | Covered California* — 14 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 317,344 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- Individuals & Families
- Certifications
- Training & Education
- Marketing & Branding
- Client Support

#### `/enrollment-partners-individuals/become-an-agent/code-of-conduct`

*Agent Code of Conduct | Covered California* — 11 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 335,056 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- Individuals & Families
- Certifications
- Training & Education
- Marketing & Branding
- Client Support

#### `/enrollment-partners-individuals/client-support`

*Client Support Resources | Covered California* — 10 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 311,867 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- Individuals & Families
- Certifications
- Training & Education
- Marketing & Branding
- Client Support

#### `/enrollment-partners-individuals/contact`

*Contact Us | Covered California* — 16 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 324,644 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- Individuals & Families
- Certifications
- Training & Education
- Marketing & Branding
- Client Support

#### `/enrollment-partners-individuals/marketing-branding-policies`

*Marketing and Branding | Covered California* — 15 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 332,459 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- Individuals & Families
- Certifications
- Training & Education
- Marketing & Branding
- Client Support

#### `/enrollment-partners-individuals/privacy-policy`

*Privacy Policy | Covered California* — 8 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 268,688 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- Individuals & Families
- Certifications
- Training & Education
- Marketing & Branding
- Client Support

#### `/enrollment-partners-individuals/training-and-education`

*Training and Education for Enrollment Partners Serving Individuals and Families | Covered California | Covered California* — 19 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 347,206 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- Individuals & Families
- Certifications
- Training & Education
- Marketing & Branding
- Client Support


### enrollment-partners-small-business

#### `/enrollment-partners-small-business`

*Helping Employers and Their Employees (CCSB) | Covered California for Small Business | Covered California for Small Business* — 15 headings, 0 table(s), 0 card group(s), 5 FAQ item(s), 317,851 bytes

**FAQ / accordions (5)**

- For Enrollment Partners
- Small Business
- CCSB Certification
- Training & Education
- Client Support

#### `/enrollment-partners-small-business/ccsb-certification`

*CCSB Certification | Covered California for Small Business | Covered California for Small Business* — 28 headings, 0 table(s), 1 card group(s), 7 FAQ item(s), 359,127 bytes

**Card group 1**

- **Agency Certification**
  - A new agency must appoint an Authorized Signer or Agency Manager to initiate the contracting process. The agency manager is responsible for all business submitted to CCSB and the management of all agents using that agency's Tax ID.
- **Downline Agent Certification**
  - Downline agents, or agents who are employed by an agency, certify under an existing certified agency to manage small-business enrollments. Before a downline can enroll, the agency must either be in the process of becoming certified or already certified.

**FAQ / accordions (7)**

- For Enrollment Partners
- Small Business
- CCSB Certification
- Training & Education
- Client Support
- What if I’m already certified for the individual market?
- Whom do I contact for help?

#### `/enrollment-partners-small-business/ccsb-certification/code-of-conduct`

*CCSB Agent Code of Conduct | Covered California for Small Business | Covered California for Small Business* — 28 headings, 0 table(s), 0 card group(s), 5 FAQ item(s), 360,743 bytes

**FAQ / accordions (5)**

- For Enrollment Partners
- Small Business
- CCSB Certification
- Training & Education
- Client Support

#### `/enrollment-partners-small-business/client-support`

*Client Support Resources for CCSB Agents | Covered California for Small Business | Covered California for Small Business* — 16 headings, 0 table(s), 0 card group(s), 5 FAQ item(s), 341,370 bytes

**FAQ / accordions (5)**

- For Enrollment Partners
- Small Business
- CCSB Certification
- Training & Education
- Client Support

#### `/enrollment-partners-small-business/contact`

*Contact and Support for CCSB Agents | Covered California for Small Business | Covered California for Small Business* — 12 headings, 0 table(s), 0 card group(s), 5 FAQ item(s), 332,814 bytes

**FAQ / accordions (5)**

- For Enrollment Partners
- Small Business
- CCSB Certification
- Training & Education
- Client Support

#### `/enrollment-partners-small-business/training-and-education`

*Training and Education for CCSB Agents | Covered California for Small Business | Covered California for Small Business* — 17 headings, 0 table(s), 0 card group(s), 5 FAQ item(s), 354,097 bytes

**FAQ / accordions (5)**

- For Enrollment Partners
- Small Business
- CCSB Certification
- Training & Education
- Client Support


### important-changes

#### `/important-changes`

*Important Changes | Covered California* — 26 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 393,744 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### glossary

#### `/glossary`

*Glossary | Covered California* — 80 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 384,592 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### privacy

#### `/privacy`

*Privacy Policy | Covered California* — 20 headings, 0 table(s), 0 card group(s), 15 FAQ item(s), 354,424 bytes

**FAQ / accordions (15)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Access Your Records
- Update Your Records
- Preferred Communication
- Request a Disclosure Report
- Authorize a Representative
- File a Complaint
- Notify Covered California About the Death of an Enrollee
- Opt out of the Covered California Healthcare Evidence Initiative
- Contact the Covered California Privacy Office

#### `/privacy/terms`

*Terms and Conditions | Covered California* — 38 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 379,123 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### about-covered-california

#### `/about-covered-california`

*About Covered California | Covered California* — 17 headings, 0 table(s), 0 card group(s), 7 FAQ item(s), 344,116 bytes

**FAQ / accordions (7)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- financial help


### accessibility-and-language-support

#### `/accessibility-and-language-support`

*Accessibility and Language Support | Covered California* — 26 headings, 1 table(s), 0 card group(s), 6 FAQ item(s), 410,909 bytes

**Table 1** — 14 rows x 2 cols

| Language | Phone Number |
|---|---|
| العربية (Arabic) | (800) 826-6317 |
| 粵語 (Cantonese) | (800) 339-8938 |
| 國語 (Mandarin) | (800) 300-1533 |
| Hmoob (Hmong) | (800) 771-2156 |
| 한국어 (Korean) | (800) 738-9116 |
| русский (Russian) | (800) 778-7695 |
| Tagalog (Filipino) | (800) 983-8816 |
| հայերեն (Armenian) | (800) 996-1009 |
| فارسی (Farsi) | (800) 921-8879 |
| ខ្មែរ (Khmer) | (800) 906-8528 |
| ລາວ (Lao) | (800) 357-7976 |
| Español (Spanish) | (800) 300-0213 |
| Tiếng Việt (Vietnamese) | (800) 652-9528 |
| TTY | (888) 889-4500 |

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### legal-notices

#### `/legal-notices`

*Serving a Legal Notice | Covered California* — 12 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 285,813 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### media-inquiries

#### `/media-inquiries`

*For Media Inquiries, Covered California is the state’s health insurance marketplace, where Californians can find affordable, high-quality insurance from top insurance companies. | Covered California* — 11 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 282,601 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### marketing-blog

#### `/marketing-blog`

*Covered Blog | Covered California* — 10 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 340,566 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### social-media-commenting-disclaimer

#### `/social-media-commenting-disclaimer`

*Social Media Commenting Disclaimer | Covered California* — 12 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 327,313 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### (home)

#### `/`

*The Official Site of California's Health Insurance Marketplace | Covered California* — 26 headings, 0 table(s), 1 card group(s), 16 FAQ item(s), 532,718 bytes

**Card group 1**

- **Marisol**
- **Gary**
- **James**
- **Dana & Eli**

**FAQ / accordions (16)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account
- Included in Every Plan
- What is Covered California?
- Medi-Cal vs. Covered California
- I lost my health insurance
- My family or household changed
- My immigration status changed
- I am an American Indian or Alaska Native
- My income, job or benefits changed
- I want to re-enroll
- None of these apply to me


### anthem

#### `/anthem`

*Anthem | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 340,367 bytes

**Card group 1**

- **If you already have a Anthem plan:**
  - Cancel your current plan after enrolling through Covered California.
  - In most cases, your accumulated deductible and out-of-pocket maximum will carry over, but you should confirm with Anthem before you switch.
  - It helps to have your current plan details ready when shopping for a similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### blue-shield

#### `/blue-shield`

*Blue Shield of California | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 339,833 bytes

**Card group 1**

- **If you already have a Blue Shield of California plan:**
  - Cancel your current plan after enrolling through Covered California.
  - In most cases, your accumulated deductible and out-of-pocket maximum will carry over, but you should confirm with Blue Shield of California before you switch.
  - It helps to have your current plan details ready when shopping for a similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### caloptima

#### `/caloptima`

*CalOptima Health | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 339,349 bytes

**Card group 1**

- **If you already have CalOptima Health:**
  - Cancel your current plan after enrolling through Covered California.
  - In most cases, your accumulated deductible and out-of-pocket maximum will carry over, but you should confirm with CalOptima before you switch.
  - It helps to have your current plan details ready when shopping fora similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### cchp

#### `/cchp`

*CCHP | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 339,159 bytes

**Card group 1**

- **If you already have a CCHP plan:**
  - Cancel your current plan after enrolling through Covered California.
  - In most cases, your accumulated deductible and out-of-pocket maximum will carry over, but you should confirm with CCHP before you switch.
  - It helps to have your current plan details ready when shopping for a similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### health-net

#### `/health-net`

*Health-Net | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 340,775 bytes

**Card group 1**

- **If you already have a Health-Net Plan**
  - Cancel your current plan after enrolling through CoveredCalifornia.
  - In most cases, your accumulated deductible and out-of-pocketmaximum will carry over, but you should confirm withHealth-Net before you switch.
  - It helps to have your current plan details ready when shopping fora similar plan here.
- **What Youll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### iehp

#### `/iehp`

*IEHP | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 339,159 bytes

**Card group 1**

- **If you already have an IEHP plan**
  - Cancel your current plan after enrolling through Covered California.
  - In most cases, your accumulated deductible and out-of-pocket maximum will carry over, but you should confirm with IEHP before you switch.
  - It helps to have your current plan details ready when shopping for a similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### kaiser-permanente

#### `/kaiser-permanente`

*Kaiser-Permanente | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 340,668 bytes

**Card group 1**

- **If you already have a Kaiser-Permanente Plan**
  - Cancel your current plan after enrolling through CoveredCalifornia.
  - In most cases, your accumulated deductible and out-of-pocketmaximum will carry over, but you should confirm withKaiser-Permanente before you switch.
  - It helps to have your current plan details ready when shopping fora similar plan here.
- **What Youll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### la-care

#### `/la-care`

*LA Care | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 339,483 bytes

**Card group 1**

- **If you already have a LA Care Plan**
  - Cancel your current plan after enrolling through CoveredCalifornia.
  - In most cases, your accumulated deductible and out-of-pocketmaximum will carry over, but you should confirm withHealth-Net before you switch.
  - It helps to have your current plan details ready when shopping fora similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### molina-healthcare

#### `/molina-healthcare`

*Molina Healthcare | Covered California* — 18 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 346,771 bytes

**Card group 1**

- **If you already have a Molina Healthcare Plan**
  - Cancel your current plan after enrolling through CoveredCalifornia.
  - In most cases, your accumulated deductible and out-of-pocketmaximum will carry over, but you should confirm withMolina Healthcare before you switch.
  - It helps to have your current plan details ready when shopping fora similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### press-releases

#### `/press-releases`

*Agency Press Releases | Covered California* — 9 headings, 0 table(s), 0 card group(s), 6 FAQ item(s), 326,238 bytes

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### sharp

#### `/sharp`

*Sharp Health Plan | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 339,045 bytes

**Card group 1**

- **If you're already insured through Sharp:**
  - Cancel your current plan after enrolling through Covered California.
  - In most cases, your accumulated deductible and out-of-pocket maximum will carry over, but you should confirm with Sharp before you switch.
  - It helps to have your current plan details ready when shopping for a similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### valley-health

#### `/valley-health`

*Valley Health | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 340,503 bytes

**Card group 1**

- **If you already have a Anthem Plan**
  - Cancel your current plan after enrolling through CoveredCalifornia.
  - In most cases, your accumulated deductible and out-of-pocketmaximum will carry over, but you should confirm withAnthem before you switch.
  - It helps to have your current plan details ready when shopping fora similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account


### western-health-advantage

#### `/western-health-advantage`

*Western Health Advantage | Covered California* — 17 headings, 0 table(s), 1 card group(s), 6 FAQ item(s), 340,747 bytes

**Card group 1**

- **If you already have a Anthem Plan**
  - Cancel your current plan after enrolling through CoveredCalifornia.
  - In most cases, your accumulated deductible and out-of-pocketmaximum will carry over, but you should confirm withAnthem before you switch.
  - It helps to have your current plan details ready when shopping fora similar plan here.
- **What You'll Need to Apply**
  - Employer and income information for applicants who earn money.
  - Social Security Numbers for applicants who have them.
  - Federal tax information for applicants who file taxes.
  - Immigration documents for non-citizens.

**FAQ / accordions (6)**

- For Enrollment Partners
- For Individuals & Families
- Coverage Basics
- Eligibility & Enrollment
- Costs & Financial Help
- Managing Your Account

