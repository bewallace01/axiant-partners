# SEO Cleanup Actions — Per-URL Decisions

**Generated:** 2026-05-27 from GSC Coverage drill-down exports
**Inputs:** 17 "Crawled — currently not indexed" + 82 "Discovered — currently not indexed" = 99 URLs total
**Companion doc:** `_analysis/SEO_CLEANUP_TRIAGE_2026-05-27.md` (overall strategy + Section 2 title fixes)

---

## Issue type cheat sheet

- **Crawled — currently not indexed (17 URLs):** Google crawled the page and *explicitly chose* not to add it to the index. This is a direct quality verdict — the worst signal a page can have. Highest priority.
- **Discovered — currently not indexed (82 URLs):** Google saw the URL (via sitemap or links) but hasn't bothered crawling it. "Last crawled: 1969-12-31" means never. Signals low priority for Google.

---

## Summary by URL pattern

| Bucket | Crawled-rejected | Discovered-never-crawled | Default action |
|---|---:|---:|---|
| 1A. /equipment-financing/states/* (state pSEO) | 1 | 15 | **KILL (410)** or **301 → /equipment-financing.html** |
| 1B. /equipment-financing/articles/* | 0 | 15 | **REVIEW** |
| 1C. /construction-business-financing/* | 2 | 5 | **CONSOLIDATE → parent industry hub** |
| 1D. /working-capital-loans/articles/* | 1 | 5 | **AUDIT + rewrite or kill** |
| 1E. /merchant-cash-advance/articles/* | 1 | 6 | **AUDIT + rewrite or kill** |
| 1F. /sba-loans/articles/* | 0 | 3 | **REVIEW** |
| 1G. /business-line-of-credit/articles/* | 1 | 2 | **AUDIT + rewrite or kill** |
| 1H. /business-term-loans/articles/* | 0 | 2 | **REVIEW** |
| 1I. /commercial-real-estate-loans/articles/* | 0 | 2 | **REVIEW** |
| 1J. /trucking-business-financing/* | 0 | 2 | **CONSOLIDATE → parent industry hub** |
| 1K. /fix-and-flip/articles/* | 0 | 3 | **REVIEW** |
| 1L. /medical-practices-business-financing/* | 1 | 0 | **CONSOLIDATE → parent industry hub** |
| 1M. /restaurants-business-financing/* | 1 | 0 | **CONSOLIDATE → parent industry hub** |
| 1Q. /articles/* | 3 | 8 | **AUDIT + rewrite or kill** |
| 1X. Other / misc | 5 | 11 | **AUDIT + rewrite or kill** |
| 1Z. Root .html pages (KEEP — review individually) | 1 | 3 | **KEEP + audit** |

---

## 1A. /equipment-financing/states/* (state pSEO) — 16 URLs

### Crawled — currently not indexed (1)

**Action:** **KILL (410)** or **301 → /equipment-financing.html** — Google explicitly rejected after crawl

- `/equipment-financing/states/pennsylvania/`

### Discovered — currently not indexed (15)

**Action:** **KILL (410)** — never even crawled; no search demand for state-specific equipment financing

- `/equipment-financing/states/arkansas/`
- `/equipment-financing/states/colorado/`
- `/equipment-financing/states/delaware/`
- `/equipment-financing/states/georgia/`
- `/equipment-financing/states/illinois/`
- `/equipment-financing/states/iowa/`
- `/equipment-financing/states/minnesota/`
- `/equipment-financing/states/nebraska/`
- `/equipment-financing/states/new-york/`
- `/equipment-financing/states/ohio/`
- `/equipment-financing/states/oklahoma/`
- `/equipment-financing/states/oregon/`
- `/equipment-financing/states/south-dakota/`
- `/equipment-financing/states/utah/`
- `/equipment-financing/states/virginia/`

---

## 1B. /equipment-financing/articles/* — 15 URLs

### Discovered — currently not indexed (15)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/equipment-financing/articles/arkansas-trucking-owner-operator-financing/`
- `/equipment-financing/articles/colorado-craft-brewery-financing/`
- `/equipment-financing/articles/do-you-need-down-payment-for-equipment-financing/`
- `/equipment-financing/articles/documents-needed-equipment-financing/`
- `/equipment-financing/articles/equipment-financing-denied-reasons-fixes/`
- `/equipment-financing/articles/equipment-financing-vs-vendor-financing/`
- `/equipment-financing/articles/equipment-lease-vs-loan-vs-cash/`
- `/equipment-financing/articles/equipment-loan-vs-sba-7a/`
- `/equipment-financing/articles/michigan-auto-tier-1-supplier-financing/`
- `/equipment-financing/articles/north-dakota-bakken-oilfield-financing/`
- `/equipment-financing/articles/reasons-equipment-financing-approval-drags-on/`
- `/equipment-financing/articles/red-flags-equipment-finance-agreements/`
- `/equipment-financing/articles/washington-apple-orchard-financing/`
- `/equipment-financing/articles/what-are-typical-equipment-financing-rates/`
- `/equipment-financing/articles/why-equipment-financing-application-stuck/`

---

## 1C. /construction-business-financing/* — 7 URLs

### Crawled — currently not indexed (2)

**Action:** **CONSOLIDATE → parent industry hub** — Google rejected after crawl

- `/construction-business-financing/how-contractor-equipment-financing-helps-you-take-on-bigger-jobs/`
- `/construction-business-financing/how-contractors-cover-payroll-materials-before-project-draws/`

### Discovered — currently not indexed (5)

**Action:** **CONSOLIDATE → parent industry hub** — no organic demand

- `/construction-business-financing/contractor-financing-mistakes-kill-approvals/`
- `/construction-business-financing/documentation-mistakes-delay-contractor-funding/`
- `/construction-business-financing/why-contractors-get-stuck-in-underwriting/`
- `/construction-business-financing/win-more-bids-by-financing-equipment-instead-of-draining-working-capital/`
- `/construction-business-financing/working-capital-vs-equipment-financing-contractors/`

---

## 1D. /working-capital-loans/articles/* — 6 URLs

### Crawled — currently not indexed (1)

**Action:** **AUDIT + rewrite or kill** — Google crawled and explicitly chose not to index. Worst-quality verdict.

- `/working-capital-loans/articles/how-fast-can-you-get-working-capital-loan/`

### Discovered — currently not indexed (5)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/working-capital-loans/articles/ach-loan-vs-mca/`
- `/working-capital-loans/articles/reasons-working-capital-loan-keeps-denied/`
- `/working-capital-loans/articles/what-is-working-capital-loan-how-does-it-work/`
- `/working-capital-loans/articles/whats-keeping-you-from-refinancing-business-debt/`
- `/working-capital-loans/articles/working-capital-loan-wholesalers-distributors/`

---

## 1E. /merchant-cash-advance/articles/* — 7 URLs

### Crawled — currently not indexed (1)

**Action:** **AUDIT + rewrite or kill** — Google crawled and explicitly chose not to index. Worst-quality verdict.

- `/merchant-cash-advance/articles/whats-preventing-merchant-cash-advance/`

### Discovered — currently not indexed (6)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/merchant-cash-advance/articles/how-fast-can-you-get-merchant-cash-advance/`
- `/merchant-cash-advance/articles/mca-mistakes-keep-you-in-cycle/`
- `/merchant-cash-advance/articles/merchant-cash-advance-requirements/`
- `/merchant-cash-advance/articles/what-credit-score-needed-merchant-cash-advance/`
- `/merchant-cash-advance/articles/what-is-merchant-cash-advance-how-does-it-work/`
- `/merchant-cash-advance/articles/why-mca-daily-payment-higher-than-expected/`

---

## 1F. /sba-loans/articles/* — 3 URLs

### Discovered — currently not indexed (3)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/sba-loans/articles/can-you-use-sba-loan-to-buy-a-business/`
- `/sba-loans/articles/sba-7a-vs-sba-express/`
- `/sba-loans/articles/sba-pre-approval-how-long-valid/`

---

## 1G. /business-line-of-credit/articles/* — 3 URLs

### Crawled — currently not indexed (1)

**Action:** **AUDIT + rewrite or kill** — Google crawled and explicitly chose not to index. Worst-quality verdict.

- `/business-line-of-credit/articles/line-of-credit-for-law-firms/`

### Discovered — currently not indexed (2)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/business-line-of-credit/articles/business-line-of-credit-vs-term-loan/`
- `/business-line-of-credit/articles/secured-vs-unsecured-business-line-of-credit/`

---

## 1H. /business-term-loans/articles/* — 2 URLs

### Discovered — currently not indexed (2)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/business-term-loans/articles/term-loan-for-business-acquisition/`
- `/business-term-loans/articles/term-loan-vs-line-of-credit/`

---

## 1I. /commercial-real-estate-loans/articles/* — 2 URLs

### Discovered — currently not indexed (2)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/commercial-real-estate-loans/articles/hard-money-vs-conventional-cre/`
- `/commercial-real-estate-loans/articles/why-cre-loan-keeps-coming-back-for-more-documents/`

---

## 1J. /trucking-business-financing/* — 2 URLs

### Discovered — currently not indexed (2)

**Action:** **CONSOLIDATE → parent industry hub** — no organic demand

- `/trucking-business-financing/bridge-net-30-net-45-gap-without-missing-fuel-and-payroll/`
- `/trucking-business-financing/owner-operator-add-second-truck-double-capacity/`

---

## 1K. /fix-and-flip/articles/* — 3 URLs

### Discovered — currently not indexed (3)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/fix-and-flip/articles/fix-and-flip-loan-requirements/`
- `/fix-and-flip/articles/typical-fix-and-flip-loan-rates/`
- `/fix-and-flip/articles/what-credit-score-needed-fix-and-flip-loan/`

---

## 1L. /medical-practices-business-financing/* — 1 URLs

### Crawled — currently not indexed (1)

**Action:** **CONSOLIDATE → parent industry hub** — Google rejected after crawl

- `/medical-practices-business-financing/finance-medical-equipment-upgrades-without-disrupting-patient-flow/`

---

## 1M. /restaurants-business-financing/* — 1 URLs

### Crawled — currently not indexed (1)

**Action:** **CONSOLIDATE → parent industry hub** — Google rejected after crawl

- `/restaurants-business-financing/restaurant-working-capital-payroll-inventory-slow-weeks/`

---

## 1Q. /articles/* — 11 URLs

### Crawled — currently not indexed (3)

**Action:** **AUDIT + rewrite or kill** — Google crawled and explicitly chose not to index. Worst-quality verdict.

- `/business-growth/articles/scale-paid-ads-tight-margins-framework/`
- `/commercial-bridge-loans/articles/commercial-bridge-loan-vs-sba-loan/`
- `/startup-financing/articles/`

### Discovered — currently not indexed (8)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/articles/business-financing-options-bad-credit/`
- `/commercial-bridge-loans/articles/commercial-bridge-loan-vs-hard-money-loan/`
- `/commercial-bridge-loans/articles/why-bridge-loan-keeps-coming-back-for-more-documents/`
- `/revenue-based-financing/articles/revenue-based-financing-professional-services/`
- `/revenue-based-financing/articles/what-do-lenders-look-for-revenue-based-financing/`
- `/securities-based-lending/articles/securities-based-lending-business-acquisition/`
- `/startup-financing/articles/finance-inventory-new-ecommerce-startup/`
- `/startup-financing/articles/startup-financing-use-of-funds-guide/`

---

## 1X. Other / misc — 16 URLs

### Crawled — currently not indexed (5)

**Action:** **AUDIT + rewrite or kill** — Google crawled and explicitly chose not to index. Worst-quality verdict.

- `/blog`
- `/equipment/commercial-mowers/how-to-finance-a-commercial-mower/`
- `/equipment/excavators/how-to-finance-an-excavator/`
- `/equipment/tractors/tractor-financing-new-farmers/`
- `/services`

### Discovered — currently not indexed (11)

**Action:** **REVIEW** — low priority for Google; either improve and link internally, or kill

- `/business-loan-approval-timeline/`
- `/business-loan-calculator-guide/`
- `/business-loan-eligibility/`
- `/business-loan-rates-2026/`
- `/buying-a-business-financing-guide/`
- `/equipment/grain-equipment/`
- `/equipment/pos-systems-restaurant/`
- `/equipment/refrigerated-trucks/`
- `/equipment/semi-trucks/semi-truck-financing-requirements/`
- `/equipment/skid-steers/skid-steer-financing-landscaping/`
- `/equipment/sprayers/`

---

## 1Z. Root .html pages (KEEP — review individually) — 4 URLs

### Crawled — currently not indexed (1)

**Action:** **KEEP + audit** — likely load-bearing nav page; verify

- `/trucking-business-financing.html`

### Discovered — currently not indexed (3)

**Action:** **KEEP + audit** — likely load-bearing nav page; verify

- `/agriculture-business-financing.html`
- `/business-line-of-credit.html`
- `/construction-business-financing.html`

---
