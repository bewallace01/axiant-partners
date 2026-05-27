# SEO Cleanup Triage — May 2026 Drop Recovery

**Generated:** 2026-05-27 from GSC export `2026-05-27`
**Diagnosis:** May 18 indexing-dilution event. Index count jumped 378 → 506 in one day. Impressions fell 65%. Average position slid from ~11 to ~27. Brand and high-intent commercial pages still rank fine — the problem is volume of thin pages pulling the domain-wide quality signal down.
**Strategy:** Cleanup BEFORE new pages. Kill / consolidate dead weight, fix title-meta on existing rankers, watch index count drop, then publish selectively.

---

## Section 1 — Never-shown pages (156 URLs)

These are in the sitemap but Google **has not shown them in any search result** over the last 28 days. They cost crawl budget, dilute quality signal, and contribute nothing.

### 1A. /equipment-financing/states/* (state pSEO) — 33 URLs
**Default action:** **KILL or CONSOLIDATE** — these 33 state pages are the prime suspects for the May 18 quality demotion. Either 410-Gone them or 301 to /equipment-financing.html.

- `/equipment-financing/states/alabama/`
- `/equipment-financing/states/alaska/`
- `/equipment-financing/states/arizona/`
- `/equipment-financing/states/arkansas/`
- `/equipment-financing/states/california/`
- `/equipment-financing/states/colorado/`
- `/equipment-financing/states/delaware/`
- `/equipment-financing/states/florida/`
- `/equipment-financing/states/georgia/`
- `/equipment-financing/states/hawaii/`
- `/equipment-financing/states/idaho/`
- `/equipment-financing/states/illinois/`
- `/equipment-financing/states/iowa/`
- `/equipment-financing/states/kansas/`
- `/equipment-financing/states/kentucky/`
- `/equipment-financing/states/louisiana/`
- `/equipment-financing/states/maryland/`
- `/equipment-financing/states/michigan/`
- `/equipment-financing/states/minnesota/`
- `/equipment-financing/states/mississippi/`
- `/equipment-financing/states/nevada/`
- `/equipment-financing/states/new-mexico/`
- `/equipment-financing/states/new-york/`
- `/equipment-financing/states/north-carolina/`
- `/equipment-financing/states/north-dakota/`
- `/equipment-financing/states/ohio/`
- `/equipment-financing/states/oklahoma/`
- `/equipment-financing/states/oregon/`
- `/equipment-financing/states/south-carolina/`
- `/equipment-financing/states/south-dakota/`
- `/equipment-financing/states/utah/`
- `/equipment-financing/states/virginia/`
- `/equipment-financing/states/wisconsin/`

### 1B. /equipment-financing/articles/* — 22 URLs
**Default action:** AUDIT first. Some have geo-specific intent (Arkansas trucking, FL hurricane); others read like generic AI long-tail.

- `/equipment-financing/articles/`
- `/equipment-financing/articles/arkansas-trucking-owner-operator-financing/`
- `/equipment-financing/articles/colorado-craft-brewery-financing/`
- `/equipment-financing/articles/contractor-equipment-financing/`
- `/equipment-financing/articles/do-you-need-down-payment-for-equipment-financing/`
- `/equipment-financing/articles/documents-needed-equipment-financing/`
- `/equipment-financing/articles/equipment-financing-denied-reasons-fixes/`
- `/equipment-financing/articles/equipment-financing-vs-vendor-financing/`
- `/equipment-financing/articles/equipment-lease-vs-loan-vs-cash/`
- `/equipment-financing/articles/equipment-loan-vs-sba-7a/`
- `/equipment-financing/articles/florida-hurricane-contractor-financing/`
- `/equipment-financing/articles/heavy-equipment-financing/`
- `/equipment-financing/articles/how-to-apply-equipment-financing/`
- `/equipment-financing/articles/michigan-auto-tier-1-supplier-financing/`
- `/equipment-financing/articles/north-dakota-bakken-oilfield-financing/`
- `/equipment-financing/articles/reasons-equipment-financing-approval-drags-on/`
- `/equipment-financing/articles/red-flags-equipment-finance-agreements/`
- `/equipment-financing/articles/restaurant-equipment-financing/`
- `/equipment-financing/articles/warehouse-equipment-financing-guide/`
- `/equipment-financing/articles/washington-apple-orchard-financing/`
- `/equipment-financing/articles/what-are-typical-equipment-financing-rates/`
- `/equipment-financing/articles/why-equipment-financing-application-stuck/`

### 1C. /construction-business-financing/* (industry child) — 14 URLs
**Default action:** **CONSOLIDATE** into the /construction-business-financing.html hub. These are sub-topic articles with weak standalone search demand.

- `/construction-business-financing/avoid-payroll-to-draw-timing-mistakes/`
- `/construction-business-financing/avoid-supplier-cod-traps-material-prices-spike/`
- `/construction-business-financing/contractor-cash-flow-red-flags-before-applying-financing/`
- `/construction-business-financing/contractor-financing-mistakes-kill-approvals/`
- `/construction-business-financing/defense-contracts-equipment-financing-bid-axiant/`
- `/construction-business-financing/documentation-mistakes-delay-contractor-funding/`
- `/construction-business-financing/how-contractor-equipment-financing-helps-you-take-on-bigger-jobs/`
- `/construction-business-financing/how-to-cover-materials-and-payroll-before-the-first-draw/`
- `/construction-business-financing/how-to-finance-used-equipment-without-overpaying/`
- `/construction-business-financing/mistakes-financing-used-equipment-contractors/`
- `/construction-business-financing/steel-lumber-prices-finance-job/`
- `/construction-business-financing/why-contractors-get-stuck-in-underwriting/`
- `/construction-business-financing/win-more-bids-by-financing-equipment-instead-of-draining-working-capital/`
- `/construction-business-financing/working-capital-vs-equipment-financing-contractors/`

### 1D. /working-capital-loans/articles/* — 7 URLs
**Default action:** AUDIT first.

- `/working-capital-loans/articles/`
- `/working-capital-loans/articles/ach-loan-vs-mca/`
- `/working-capital-loans/articles/reasons-working-capital-loan-keeps-denied/`
- `/working-capital-loans/articles/war-fuel-material-costs-cash-flow-squeezed-options/`
- `/working-capital-loans/articles/what-is-working-capital-loan-how-does-it-work/`
- `/working-capital-loans/articles/whats-keeping-you-from-refinancing-business-debt/`
- `/working-capital-loans/articles/working-capital-loan-wholesalers-distributors/`

### 1E. /merchant-cash-advance/articles/* — 7 URLs
**Default action:** AUDIT first.

- `/merchant-cash-advance/articles/`
- `/merchant-cash-advance/articles/how-fast-can-you-get-merchant-cash-advance/`
- `/merchant-cash-advance/articles/mca-mistakes-keep-you-in-cycle/`
- `/merchant-cash-advance/articles/merchant-cash-advance-requirements/`
- `/merchant-cash-advance/articles/what-credit-score-needed-merchant-cash-advance/`
- `/merchant-cash-advance/articles/what-is-merchant-cash-advance-how-does-it-work/`
- `/merchant-cash-advance/articles/why-mca-daily-payment-higher-than-expected/`

### 1F. /sba-loans/articles/* — 6 URLs
**Default action:** AUDIT first.

- `/sba-loans/articles/can-you-use-sba-loan-to-buy-a-business/`
- `/sba-loans/articles/sba-7a-vs-conventional-bank-loan/`
- `/sba-loans/articles/sba-7a-vs-sba-express/`
- `/sba-loans/articles/sba-loan-manufacturing-lost-supplier-overseas-conflict-pivot/`
- `/sba-loans/articles/sba-pre-approval-how-long-valid/`
- `/sba-loans/articles/veterinary-practice-loan-vs-small-business-loan/`

### 1G. /business-line-of-credit/articles/* — 5 URLs
**Default action:** AUDIT first.

- `/business-line-of-credit/articles/`
- `/business-line-of-credit/articles/business-line-of-credit-vs-term-loan/`
- `/business-line-of-credit/articles/line-of-credit-for-law-firms/`
- `/business-line-of-credit/articles/open-line-of-credit-now-before-wartime-inflation-rates-higher/`
- `/business-line-of-credit/articles/secured-vs-unsecured-business-line-of-credit/`

### 1H. /business-term-loans/articles/* — 5 URLs
**Default action:** AUDIT first.

- `/business-term-loans/articles/`
- `/business-term-loans/articles/term-loan-for-business-acquisition/`
- `/business-term-loans/articles/term-loan-vs-bridge-loan/`
- `/business-term-loans/articles/term-loan-vs-line-of-credit/`
- `/business-term-loans/articles/why-term-loan-funding-keeps-getting-pushed-back/`

### 1I. /commercial-real-estate-loans/articles/* — 4 URLs
**Default action:** AUDIT first.

- `/commercial-real-estate-loans/articles/`
- `/commercial-real-estate-loans/articles/hard-money-vs-conventional-cre/`
- `/commercial-real-estate-loans/articles/reasons-cre-loan-approval-taking-forever/`
- `/commercial-real-estate-loans/articles/why-cre-loan-keeps-coming-back-for-more-documents/`

### 1J. /trucking-business-financing/* (industry child) — 4 URLs
**Default action:** **CONSOLIDATE** into the /trucking-business-financing.html hub.

- `/trucking-business-financing/bridge-net-30-net-45-gap-without-missing-fuel-and-payroll/`
- `/trucking-business-financing/detention-layover-pay-cash-crunch/`
- `/trucking-business-financing/pre-peak-freight-capacity-financing-plan/`
- `/trucking-business-financing/truck-note-lease-payment-slow-freight-weeks/`

### 1K. /fix-and-flip/articles/* — 4 URLs
**Default action:** AUDIT first.

- `/fix-and-flip/articles/fix-and-flip-loan-requirements/`
- `/fix-and-flip/articles/reasons-fix-and-flip-lenders-back-out/`
- `/fix-and-flip/articles/typical-fix-and-flip-loan-rates/`
- `/fix-and-flip/articles/what-credit-score-needed-fix-and-flip-loan/`

### 1X. Other / misc — 34 URLs
**Default action:** Audit individually.

- `/articles/`
- `/articles/business-financing-options-bad-credit/`
- `/articles/why-lender-keeps-asking-for-more-documents/`
- `/business-financing-glossary/`
- `/business-loan-calculator-guide/`
- `/business-loan-eligibility/`
- `/business-loan-rates-2026/`
- `/buying-a-business-financing-guide/`
- `/commercial-bridge-loans/articles/commercial-bridge-loan-vs-hard-money-loan/`
- `/commercial-bridge-loans/articles/why-bridge-loan-keeps-coming-back-for-more-documents/`
- `/equipment/brake-rotor-equipment/`
- `/equipment/bulldozers/bulldozer-financing-leasing/`
- `/equipment/grain-equipment/`
- `/equipment/pos-systems-restaurant/`
- `/equipment/refrigerated-trucks/`
- `/equipment/semi-trucks/semi-truck-financing-requirements/`
- `/equipment/shop-tools-storage/auto-shop-equipment-package-financing/`
- `/equipment/skid-steers/skid-steer-financing-landscaping/`
- `/equipment/sprayers/`
- `/equipment/sprinter-vans/`
- `/equipment/sprinter-vans/sprinter-van-financing-delivery/`
- `/equipment/ventilation-hood-systems/`
- `/healthcare-practice-financing-guide/`
- `/manufacturing-financing-guide/`
- `/refinancing-business-debt-guide/`
- `/restaurant-financing-guide/`
- `/revenue-based-financing/articles/`
- `/revenue-based-financing/articles/revenue-based-financing-professional-services/`
- `/revenue-based-financing/articles/what-do-lenders-look-for-revenue-based-financing/`
- `/securities-based-lending/articles/securities-based-lending-business-acquisition/`
- `/startup-financing/articles/`
- `/startup-financing/articles/finance-inventory-new-ecommerce-startup/`
- `/startup-financing/articles/startup-financing-use-of-funds-guide/`
- `/trucking-company-financing-guide/`

### 1Y. /get-matched/* (KEEP — lead capture) — 4 URLs
**Default action:** **KEEP** — conversion pages, not meant to rank organically.

- `/get-matched/equipment/`
- `/get-matched/line-of-credit/`
- `/get-matched/merchant-cash-advance/`
- `/get-matched/working-capital/`

### 1Z. Root .html pages (KEEP — review individually) — 7 URLs
**Default action:** **KEEP** — these are likely load-bearing nav pages. Verify each.

- `/agriculture-business-financing.html`
- `/blog.html`
- `/business-line-of-credit.html`
- `/construction-business-financing.html`
- `/industries.html`
- `/match.html`
- `/referral.html`

---

## Section 2 — Title/meta fix candidates (47 URLs)

These pages ARE ranking but getting **zero clicks** despite >=100 impressions each. The title or meta isn't compelling the click. **Highest ROI work in the whole cleanup** — no content rewrite needed, just rewrite the `<title>` and `<meta name="description">` per `.cursor/rules/seo-geo-aeo-meta.mdc`.

| Impr | Pos | URL | Priority |
|-----:|----:|-----|----------|
| 3117 | 11.2 | `/commercial-real-estate-loans/articles/how-much-down-payment-required-commercial-property-loan/` | MED (just below fold) |
| 1283 | 10.1 | `/sba-loans/articles/how-long-sba-loan-approval/` | MED (just below fold) |
| 630 | 4.9 | `/securities-based-lending/articles/how-much-can-you-borrow-with-securities-based-lending/` | **TOP** (page 1, just bad CTR) |
| 583 | 5.7 | `/securities-based-lending/articles/securities-based-lending-traps-margin-calls-cross-collateral-concentration/` | HIGH (page 1, position 6–10) |
| 564 | 8.3 | `/equipment/semi-trucks/semi-truck-financing-down-payment/` | HIGH (page 1, position 6–10) |
| 489 | 58.1 | `/sba-loans/articles/sba-7a-vs-504-loan/` | LOW (rewrite unlikely to lift to page 1) |
| 452 | 24.3 | `/equipment/semi-trucks/semi-truck-lease-vs-loan/` | LOW (rewrite unlikely to lift to page 1) |
| 396 | 8.7 | `/equipment/semi-trucks/how-to-finance-a-semi-truck/` | HIGH (page 1, position 6–10) |
| 363 | 3.4 | `/revenue-based-financing/articles/revenue-based-financing-requirements/` | **TOP** (page 1, just bad CTR) |
| 362 | 6.0 | `/equipment-financing/articles/equipment-financing-vs-sba-loan/` | HIGH (page 1, position 6–10) |
| 353 | 6.5 | `/sba-loans/articles/sba-loan-vs-business-line-of-credit/` | HIGH (page 1, position 6–10) |
| 351 | 31.5 | `/equipment/medical-imaging/` | LOW (rewrite unlikely to lift to page 1) |
| 345 | 4.8 | `/merchant-cash-advance/articles/merchant-cash-advance-vs-working-capital-loan/` | **TOP** (page 1, just bad CTR) |
| 288 | 11.5 | `/construction-business-financing/progress-payment-cash-flow-gaps/` | MED (just below fold) |
| 273 | 10.2 | `/sba-loans/articles/how-much-down-payment-required-sba-loan/` | MED (just below fold) |
| 269 | 6.1 | `/sba-loans/articles/sba-loan-restaurant-acquisition/` | HIGH (page 1, position 6–10) |
| 247 | 9.6 | `/commercial-real-estate-loans/articles/owner-occupied-vs-investment-commercial-property-loan/` | HIGH (page 1, position 6–10) |
| 240 | 4.3 | `/merchant-cash-advance/articles/how-much-can-you-qualify-for-merchant-cash-advance/` | **TOP** (page 1, just bad CTR) |
| 239 | 14.0 | `/working-capital-loans/articles/working-capital-loan-staffing-agencies/` | MED (just below fold) |
| 223 | 7.1 | `/articles/business-loan-guarantee-traps/` | HIGH (page 1, position 6–10) |
| 200 | 9.3 | `/sba-loans/articles/sba-loan-veterinary-practice/` | HIGH (page 1, position 6–10) |
| 185 | 6.5 | `/revenue-based-financing/articles/revenue-based-financing-vs-merchant-cash-advance/` | HIGH (page 1, position 6–10) |
| 162 | 8.2 | `/articles/why-applying-multiple-banks-blindly-hurts-approval-odds/` | HIGH (page 1, position 6–10) |
| 156 | 5.2 | `/equipment-financing/articles/can-equipment-financing-help-build-business-credit/` | HIGH (page 1, position 6–10) |
| 152 | 6.3 | `/equipment-financing/articles/equipment-financing-ucc-lien-approval/` | HIGH (page 1, position 6–10) |
| 149 | 9.3 | `/commercial-real-estate-loans/articles/what-credit-score-needed-commercial-real-estate-loan/` | HIGH (page 1, position 6–10) |
| 144 | 20.1 | `/working-capital-loans/articles/working-capital-loan-seasonal-businesses/` | LOW (rewrite unlikely to lift to page 1) |
| 140 | 7.2 | `/trucking-business-financing.html` | HIGH (page 1, position 6–10) |
| 135 | 9.5 | `/equipment-financing/articles/what-do-lenders-look-at-equipment-financing-approval/` | HIGH (page 1, position 6–10) |
| 133 | 10.9 | `/working-capital-loans/articles/business-loans-for-bad-credit/` | MED (just below fold) |
| 132 | 10.1 | `/commercial-bridge-loans/articles/how-fast-can-you-close-commercial-bridge-loan/` | MED (just below fold) |
| 132 | 12.5 | `/equipment-financing/articles/what-credit-score-needed-equipment-financing/` | MED (just below fold) |
| 128 | 11.0 | `/securities-based-lending.html` | MED (just below fold) |
| 125 | 9.8 | `/sba-loans/articles/what-documents-needed-sba-loan/` | HIGH (page 1, position 6–10) |
| 121 | 6.8 | `/sba-loans/articles/sba-loan-alternatives-when-you-dont-qualify/` | HIGH (page 1, position 6–10) |
| 117 | 19.6 | `/equipment/industrial-robots/robotics-automation-financing/` | MED (just below fold) |
| 114 | 9.2 | `/commercial-real-estate-loans/articles/how-long-close-commercial-real-estate-loan/` | HIGH (page 1, position 6–10) |
| 111 | 11.3 | `/equipment/flatbed-trucks/flatbed-truck-financing-haulers/` | MED (just below fold) |
| 109 | 33.8 | `/equipment/semi-trucks/semi-truck-financing-bad-credit/` | LOW (rewrite unlikely to lift to page 1) |
| 108 | 2.7 | `/business-line-of-credit/articles/red-flags-line-of-credit-offers/` | **TOP** (page 1, just bad CTR) |
| 108 | 7.7 | `/revenue-based-financing/articles/when-is-revenue-based-financing-not-right-option/` | HIGH (page 1, position 6–10) |
| 105 | 6.1 | `/sba-loans/articles/why-sba-loan-approval-taking-forever/` | HIGH (page 1, position 6–10) |
| 105 | 8.7 | `/sba-loans/articles/what-do-lenders-look-for-sba-loan-approval/` | HIGH (page 1, position 6–10) |
| 103 | 11.2 | `/working-capital-loans/articles/what-credit-score-needed-working-capital-loan/` | MED (just below fold) |
| 102 | 4.3 | `/revenue-based-financing/articles/how-fast-can-you-get-revenue-based-financing/` | **TOP** (page 1, just bad CTR) |
| 101 | 7.5 | `/equipment/mini-excavators/mini-excavator-financing-contractors/` | HIGH (page 1, position 6–10) |
| 101 | 14.9 | `/sba-loans/articles/sba-loan-owner-occupied-commercial-property/` | MED (just below fold) |

---

## Section 3 — Recommended order of operations

1. **Week 1 — Quick wins.** Rewrite titles + metas on the top 10–15 entries from Section 2. No content edits required. Watch CTR climb week-over-week.
2. **Week 1 — Kill dead weight.** Drop the 33 state pSEO pages and 14 construction child pages. Either delete the files + add `410` redirects, or `301` each to the closest hub. Remove from `sitemap.xml`. This signals to Google we're pruning and should drop the indexed count from 506 toward ~420.
3. **Week 2 — Audit article batches.** For each Section-1 article group (1D–1K), sample 3 pages per template. If duplicate ratio >40% OR reads as generic AI long-tail with no real query intent, consolidate into hub. Otherwise rewrite for human intent.
4. **Week 3+ — Resubmit cleaned sitemap.** Use GSC URL Inspection to request reindexing of the rewritten pages. Rank recovery typically begins within 1–2 weeks of index count stabilizing at a lower number.
5. **NO new programmatic pages** until index count drops below ~420 AND average position recovers above 15. When we do publish: one batch of ~10 at a time, never 128 in a day.

---

## Section 4 — Data still needed from user

Coverage.xlsx only has counts. To finish triage we need per-URL exports from GSC. Open **Search Console → Pages**, click each issue category, then **Export** to CSV:

- **Crawled — currently not indexed** (17 URLs). Google crawled these and *explicitly rejected* them. Highest-priority audit — these are the worst-quality pages on the site by Google's own judgment.
- **Discovered — currently not indexed** (82 URLs). Google saw them but won't crawl yet. Often signals low link equity from the rest of the site.
- **Excluded by `noindex` tag** (6 URLs). Verify intentional vs accidental.
- **Alternate page with proper canonical** (6 URLs). Usually fine; spot-check canonical targets.
- **Not found (404)** (5 URLs). 301 to the closest relevant page or resurrect.

---

## Appendix — Pattern summary

- Sitemap URLs: 560
- URLs with any impressions in last 28d: 430
- Never-shown URLs: 156
- Title-fix candidates (≥100 imp, 0 clicks): 47
