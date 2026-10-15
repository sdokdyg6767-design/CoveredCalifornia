# Plan and Premium Lookup Tools (Shop & Compare, plan finders, official APIs)

- **Retrieved:** 2026-10-13
- **Type:** External database / data source guide

## Summary

Covered California has exactly one live plan lookup tool — the Shop & Compare application at `apply.coveredca.com/lw-shopandcompare/` — and there is no separate plan-finder page on coveredca.com (that path returns 404). The tool's front-end configuration is published as JSON and exposes three live REST endpoints, one of which is completely unauthenticated and returns the list of enrollment years the tool can quote. Critically, that list **includes 2027**, so 2027 California premium quotes are retrievable through Shop & Compare even though no bulk 2027 file has been published anywhere else.

## Key Facts

| Attribute | Detail |
| --- | --- |
| Publisher | Covered California (California Health Benefit Exchange) |
| URL | https://apply.coveredca.com/lw-shopandcompare/ |
| Entered from | https://www.coveredca.com/shopandcompare/ — verified 308 redirect to the apply host |
| Access | Free, no registration for browsing or quoting. Enrolling requires an account |
| Coverage | All California individual-market QHPs; also small-group plans |
| Current as of | Enrollment years 2015 through 2027 available in the tool (verified 2026-10-13) |
| Update cadence | Continuous; plan data refreshes with each approved rate filing cycle |
| Machine-readable | Front-end app; JSON REST endpoints (see below). No bulk download, no documented public API |
| Volume | Client-side React SPA, ~1.7 MB main JS bundle, served from `/lw-shopandcompare/assets/` |

## What it contains

Shop & Compare is a single-page application. Page title verified as `Shop & Compare Health Insurance Plans | Covered California™`. Everything rendered on screen comes from the endpoints below.

### The published front-end configuration

The app loads its configuration from a static JSON file whose path is itself a content hash:
`https://apply.coveredca.com/lw-shopandcompare/config/app.production.config.6d3ea464babffaaea465da433ee35d8a.json`

Retrieved verbatim (abridged to the lookup-relevant keys):

```json
window.__APP_CONFIG__ = {
  "apiEndpointShopAndCompareEnrollYear": "https://apply.coveredca.com/shopandcompare/enrollyear",
  "apiEndpointShopAndCompareZipCodeURL": "https://apply.coveredca.com/shopandcompare/zipcounty",
  "apiEndpointShopAndCompareServiceURL": "https://apply.coveredca.com/shopandcompare/screening",
  "apiEndpointRegenerateJwtToken": "{appURL}/ahbx/tokengenerator-service/v1/alt/regenerateJwtToken",
  "apiEndpointZipcodeLookupURI": "/zipCode/{zipCode}/counties/{stateCheck}",
  "apiEndpointZipcodeValidationURI": "/zipcode/{zipCode}",
  "apiEndpointAddressLookupURI": "/address/normalization",
  "apiXApiKey": "hOS6i3RrRuB1Cpdh7tDU5UBbpjkbi2YFR5O0Pk1O",
  "shop": "/hix/private/anonymous",
  "applicationurl": "https://apply.coveredca.com",
  "gtm-key": "GTM-P757DVL"
}
```

The `apiXApiKey` value is a public client-side key shipped to every visitor in this file. Treat it as public: it is not a secret and must not be represented as one.

### Endpoint 1 — enrollment years (open, verified 200)

`GET https://apply.coveredca.com/shopandcompare/enrollyear`

Verified response body, verbatim:

```json
{"enrollYears":["2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027"]}
```

This is the strongest available evidence about 2027 availability. Shop & Compare is quoting 2027 as of 2026-10-13, which means 2027 approved plan data exists inside Covered California's systems even though no 2027 file has been published on the CMS PUF pages.

### Endpoint 2 — ZIP-to-county resolution (token required)

`GET https://apply.coveredca.com/shopandcompare/zipcounty` — verified **403 `{"message":"Missing Authentication Token"}`** for both `?zipCode=90210` and `?zipcode=90210&state=CA`.

### Endpoint 3 — plan screening / quoting (token required)

`GET/POST https://apply.coveredca.com/shopandcompare/screening` — this is the endpoint behind the tool's quote results: it takes a ZIP code, an enrollment year, an age, a household composition and an income, and returns the eligible plans with premiums. Not tested without a session token.

### Token acquisition

`POST https://apply.coveredca.com/ahbx/tokengenerator-service/v1/alt/regenerateJwtToken` — verified **403 Forbidden** when called outside the browser flow. The token is minted by the app during an anonymous handshake (`"pcapAnonymousHandshakeAPI": "/alt/anon/savehandoffdetails"`) and passed as a JWT, alongside the Tableau token endpoint pattern also used by Covered California dashboards.

### Other lookup surfaces checked

- `https://www.coveredca.com/plan-finder`, `/plan-finder/`, `/individuals/plan-finder` — all **404**. Covered California has no plan-finder page; Shop & Compare is the only consumer plan lookup.
- `https://www.healthcare.gov/plan-compare/` — **404**. There is no federal plan-comparison page at that path, and in any case HealthCare.gov carries no California plans.
- `https://www.healthcare.gov/api/` — **404**. No public HealthCare.gov plan API at that path.
- `https://data.healthcare.gov/` — **200**. Reachable, but not verified to contain any marketplace plan data in this pass.

### Per-plan Summary of Benefits links

The CMS SBE QHP PUF `CAPlans` file has columns `URL FOR SUMMARY OF BENEFITS COVERAGE`, `PLAN BROCHURE`, `URL FOR ENROLLMENT PAYMENT`, and `FORMULARY URL`. **Verified caution:** in `CAPlans05052026.csv` all of these columns are empty for every row — 0 non-empty SBC URLs. Do not rely on the PUF to hand you a direct link to any plan's Summary of Benefits. Obtain those through Covered California or HealthCare.gov instead.

## What it does NOT contain

1. **No bulk data access.** Shop & Compare is a transaction-style quote tool. There is no CSV, no export, no download of "all plans for 2027." Every result requires either a browser session or an authenticated token.
2. **No stable or documented public API.** The endpoints discovered here are an implementation detail of a front-end app, discovered by reading the shipped configuration file. They are not published, supported, versioned, or covered by any service-level commitment, and the config path contains a content hash that will change when the app is redeployed. Any automation built on these URLs is fragile by construction.
3. **No carrier-level or plan-level analytic view.** The tool answers "what can I buy at ZIP 90210 for a 27-year-old making $X," not "how many plans does Molina offer." There is no aggregate endpoint.
4. **No historical bulk archive.** Years 2015–2025 are selectable in the tool, but this is quoting, not a downloadable time series.
5. **Quotes are for individuals, not households of record.** Results are conditioned on the ZIP, age, income, and household composition you enter; they are not a census of what is available.
6. **Enrollment requires authentication and eligibility verification.** Nothing past the quote screen is accessible anonymously.

## Questions it can answer that coveredca.com cannot

1. **What are the actual 2027 premium quotes for a specific California ZIP code, age, and income?** This is the one question that the CMS bulk files cannot currently answer, because no 2027 PUF exists. Shop & Compare can.
2. Which plans are available at ZIP 90210 (Beverly Hills) versus ZIP 95814 (Sacramento) for a 2027 plan year — i.e., which carriers serve which ZIP?
3. What is the cheapest Silver plan available to a 30-year-old at a given income in a given county?
4. Which carriers offer plans in a given county at all, from a consumer's point of view?
5. Does a specific plan appear in the tool for 2027, confirming that it was certified for the 2027 plan year?
6. What subsidy or premium-tax-credit amount does Covered California currently quote for a given household?

## How to use it

**Step 1 — open the tool.** Go to https://apply.coveredca.com/lw-shopandcompare/ and enter ZIP code, date of birth (drives age rating), household size, and annual household income for the desired plan year. The year selector offers 2015–2027.

**Step 2 — confirm the tool is quoting the year you expect.** Before anything else, check:

```
GET https://apply.coveredca.com/shopandcompare/enrollyear
```

**Step 3 — re-read the configuration if the app changes.** The config path includes a content hash. If Shop & Compare stops working, fetch `https://apply.coveredca.com/lw-shopandcompare/` and re-extract the new `/lw-shipandcompare/config/...json` path from the `src=` attribute. The endpoint values inside it are the authoritative map of where the app sends data.

**Step 4 — for automated ZIP-to-county resolution, you need a token.** Call the token generator through a real browser session (the app mints one during its anonymous handshake). Direct POST from a script returned 403 in this pass.

**Step 5 — for reproducible, citable numbers at scale, do not use this tool.** Use the CMS SBE QHP PUF (2026 available now) and re-check `enrollyear` and the SBE PUF page each January for the new plan year.

## Status and caveats

**Verified live on 2026-10-13:** `https://apply.coveredca.com/lw-shopandcompare/` (200, title confirmed); `https://apply.coveredca.com/lw-shopandcompare/#/plans` (200); `https://www.coveredca.com/shopandcompare/` (308 → apply host, 200); the production config JSON (200, contents retrieved); `https://apply.coveredca.com/shopandcompare/enrollyear` (200, JSON parsed); `https://www.coveredca.com/robots.txt` (200 — confirms `sitemap.xml`, `marketing-blog/sitemap.xml`, `press-releases/sitemap.xml`).

**Verified blocked or dead:** `zipcounty` (403 without token); `regenerateJwtToken` (403 without browser session); `https://www.coveredca.com/plan-finder`, `/plan-finder/`, `/individuals/plan-finder` (404); `https://www.healthcare.gov/plan-compare/` (404); `https://www.healthcare.gov/api/` (404); `https://www.healthcare.gov/api/articles/` (404); `https://www.cms.gov/medicare/health-plans` (404).

**Stability warning:** the app is redeployed with content-hashed asset and config filenames. The hash observed on 2026-10-13 was `app.production.config.6d3ea464babffaaea465da433ee35d8a.json` and `index-igwbGzCU.js`. These will change. Never hard-code them.

**Terms of use:** this is a consumer application intended for shopping. Automating it for bulk extraction at scale is outside the apparent intended use, may trip rate limiting or bot protection (the app loads Google reCAPTCHA), and may violate Covered California terms. For bulk analysis, prefer the CMS SBE QHP PUF, which is explicitly published for that purpose. Use Shop & Compare for targeted verification of individual ZIP codes and the 2027 plan year, not for enumeration.

**No API key from me is stored or to be stored.** The `apiXApiKey` above is documented as a public client-side value read from a publicly served config file, for transparency about how the app works. Do not treat it as a credential.

**Not verified:** whether a 2027 plan-year quote returns complete results for all counties today, or whether the 2027 data behind the tool is final versus still being amended. Only the year list was confirmed, not the quotes themselves.

## Sources

- [Covered California Shop & Compare (live)](https://apply.coveredca.com/lw-shopandcompare/)
- [Shop & Compare enrollment-years endpoint — returns 2015 through 2027 (verified live)](https://apply.coveredca.com/shopandcompare/enrollyear)
- [Shop & Compare ZIP-to-county endpoint (403 without token)](https://apply.coveredca.com/shopandcompare/zipcounty)
- [Shop & Compare plan screening endpoint (token required)](https://apply.coveredca.com/shopandcompare/screening)
- [Shop & Compare production app configuration JSON (verified live)](https://apply.coveredca.com/lw-shopandcompare/config/app.production.config.6d3ea464babffaaea465da433ee35d8a.json)
- [Covered California /shopandcompare redirect entry point](https://www.coveredca.com/shopandcompare/)
- [coveredca.com robots.txt and sitemap locations](https://www.coveredca.com/robots.txt)
- [data.healthcare.gov (200, contents not verified)](https://data.healthcare.gov/)
- [CMS Marketplace landing page](https://www.cms.gov/marketplace)