# Site Hygiene Sweep — June 18, 2026

**Scope:** Full-site observation of all 846 published HTML pages on axiantpartners.com, via a deterministic scanner (`_analysis/observe-site.mjs`), followed by remediation. Broken internal links stayed at **0** throughout.

---

## Fixed this session

### 1. 35 dead-end article cards removed (18 pages)
Hub and `/articles/` index pages rendered "Relevant Articles" cards with a heading + description but **no link** — dead ends advertising pages that were never built or were deleted (e.g. `contractor-cash-flow-red-flags-before-applying-financing`, and "wartime inflation" LOC pieces already 301'd in `_redirects`). The hrefs had been stripped to avoid broken-link flags. Auto-relinking was attempted but **rejected**: fuzzy title matching produced wrong-section mismatches (a "CRE loan documents" card matching an SBA page), so removal was the correct fix. Every affected section retains its real, linked cards (minimum 4).

### 2. Rate-page cannibalization — BLoC + equipment
A "2026 rate pages" batch created duplicate rate articles competing with established ones:
- `business-line-of-credit/articles/typical-business-line-of-credit-rates-2026` → canonicaled to `what-are-typical-business-line-of-credit-rates` (178 impr @ pos 37).
- `equipment-financing/articles/typical-equipment-financing-rates-2026` → canonicaled to `what-are-typical-equipment-financing-rates`.

Both dups removed from the sitemap; hub→rates internal links added on the BLoC hub.

### 3. Duplicate contractor hub consolidated
`contractor-financing.html` is a noun-swapped template clone of `construction-business-financing.html` (identical section skeleton). Construction is the clear winner — **15 impressions vs 0, 79 inbound internal links vs 11**, and it owns the `/construction-business-financing/articles/` cluster. Canonicaled the contractor page to construction and removed it from the sitemap.

### 4. 25 indexable pages added to the sitemap
Self-canonical industry sub-pages with no crawl path: clusters under `business-growth-financing/`, `landscaping-business-financing/`, `logistics-warehousing-business-financing/`, `manufacturing-business-financing/`, `medical-practices-business-financing/`, and `restaurants-business-financing/`. Canonical-elsewhere dupes and bare-dir stubs were excluded.

### 5. 894 "·"-as-em-dash typos corrected (54 pages)
A past find/replace turned em-dashes into `&middot;` glued mid-sentence ("revenue is project-based·you incur costs", "</strong>·$25,000"). Replaced `&middot;` with `&mdash;` everywhere it was **not** a space-padded separator, leaving the 281 legitimate ` &middot; ` list/inline separators untouched.

---

## Checked and intentionally left alone

- **Construction working-capital cluster** (~18 pages: retainage, mobilization, subcontractor invoices, draw gaps, material deposits): genuinely distinct long-tail intents, **not** duplicates. A merge would destroy real coverage.
- **Other rate pages** (WC, MCA, SBA, CRE, SBL): each has a *single* rates page — no counterpart, no cannibalization. (`typical-sbl-rates-2026` is a winner at 136 impr, pos 7.)
- **"1 inbound link" pages (~170):** a thin-internal-linking opportunity, not breakage. True zero-inbound orphans ≈ 1.
- **`digital-marketing/fragments/` and `tools/article_supplements/`** have no `<title>`/meta because they are HTML *includes*, not standalone pages. Low risk (unlinked, not in sitemap) — but worth a `noindex`/robots guard if they ever become directly linkable.

---

## Clean (no action needed)
0 broken internal links · 0 exact-duplicate titles · 0 sitemap URLs without a backing file · 0 noindex pages in the sitemap. The 22 "canonical points elsewhere" entries are all intentional (`*-blog.html` and bare-dir pages consolidating to their `/articles/` hub, plus the dedups above).

*Scanner: `_analysis/observe-site.mjs` (re-runnable). This write-up is surfaced in the audit dashboard's "Fixes & Opportunities" tab.*
