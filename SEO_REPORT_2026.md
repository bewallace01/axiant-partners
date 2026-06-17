# Axiant Partners – Full SEO Report

**Date:** March 2026 · **Last updated:** June 17, 2026 (live GSC data)
**Overall Grade:** **84/100 (B+)** *(code/technical fundamentals — see live-data caveat below)*

---

## ⚠️ June 17, 2026 Update — Live GSC Data Changes the Picture

The B+ grade below reflects **technical fundamentals from a code audit.** The first full Search Console pull since the **May 18 indexing-dilution event** tells a harder story on real performance. Full detail: [`_analysis/GSC_ANALYSIS_2026-06-17.md`](_analysis/GSC_ANALYSIS_2026-06-17.md).

**28-day totals (May 19 – Jun 15):** ~24,700 impressions · **~82 clicks** · CTR ≈ **0.33%** · avg position ~21.

1. **Site-wide CTR collapse — the #1 issue.** Strong fundamentals are not converting to clicks. `construction-business-financing/why-contractors-need-working-capital` pulled **3,774 impressions, 0 clicks, at position 3.94.** The cause is **AI Overviews / Google AI Mode answering queries in-SERP** — confirmed by a query report saturated with natural-language/persona prompts. Comparison ("vs"), "rates", and concrete-data pages survive best (the `carecredit-vs-patientfi` page is the top non-branded earner at 7 clicks).
2. **May-drop recovery is real but early** — position recovered ~27 → ~17–21 and daily clicks rose from ~1 to 4–10 over June. **Hold the publishing freeze** until index count and position fully stabilize.
3. **Bridge cluster is over-built vs demand** — ~260 impressions / 2 clicks in 28 days; the **hub itself got 5 impressions**, out-competed by its own child articles (keyword cannibalization). The fix is consolidation + an AEO/GEO comparison table, **not more pages.**

**Revised priority order:** (1) site-wide CTR/AEO rewrite of top high-impression / zero-click pages → (2) bridge hub cannibalization fix + comparison table → (3) continue May cleanup / hold freeze → (4) re-pull GSC in ~2 weeks. Tables and dated data, not new URLs, are the lever.

---

## Executive Summary

| Category | Score | Status |
|----------|-------|--------|
| Technical SEO | 90/100 | ✅ Strong |
| On-Page SEO | 85/100 | ✅ Good |
| Structured Data | 92/100 | ✅ Strong |
| Content & UX | 78/100 | ✅ Good |
| Crawlability | 88/100 | ✅ Strong |

The site has solid fundamentals: valid sitemap, clean robots.txt, strong meta tags, rich schema, and good internal linking. The main opportunities are title length optimization, a few missing/weak meta elements, Core Web Vitals preparation, and minor technical cleanups.

---

## 1. What’s Working Well

- **robots.txt** – Sitemap declared; AI crawlers (GPTBot, PerplexityBot, etc.) allowed
- **Canonicals** – All pages point to https://axiantpartners.com
- **301 Redirects** – Blog migration and hub redirects configured in `_redirects` + `.htaccess`
- **Schema** – Organization (with sameAs), WebSite, BreadcrumbList, Article, FAQPage, HowTo, FinancialService
- **Meta tags** – Titles, descriptions, OG, Twitter on main pages
- **H1s** – Single primary H1 per page
- **Image alts** – No empty alt attributes
- **Mobile** – viewport meta present
- **Performance hints** – Preconnect, preload, critical CSS, lazy-loaded styles

---

## 2. Issues to Fix (Prioritized)

### High Priority

| Issue | Location | Fix |
|-------|----------|-----|
| **Long titles (60+ chars)** | Equipment Financing No Money Down, Business Term Loans, What Documents Do I Need SBA | Shorten to ~50–60 chars so they don’t get truncated in SERPs |
| **fix-and-flip-blog.html missing meta description** | `fix-and-flip-blog.html` | Add meta description (even though it redirects, some crawlers may index it briefly) |
| **Duplicate dns-prefetch** | `index.html` lines 27–28 | Remove duplicate `dns-prefetch` for images.unsplash.com |
| **Blog hub pages** | fix-and-flip-blog, sba-loans-blog, etc. | Ensure consistent meta descriptions and canonical tags where they exist as redirect pages |

### Medium Priority

| Issue | Location | Fix |
|-------|----------|-----|
| **Image dimensions** | Hero images, card images | Add explicit `width` and `height` to reduce CLS (Core Web Vitals) |
| **Title variety** | Equipment pages | Many use the same suffix `| Costs & Rates | Axiant Partners` – acceptable but consider slight variation for differentiation |
| **industry pages** | e.g. `landscaping-business-financing.html` | Confirm all 10 industry pages have unique meta descriptions |
| **Duplicate content path** | `equipment\` vs `equipment/` | On Windows, both can exist; ensure canonicals and internal links use a single URL format consistently |

### Lower Priority

| Issue | Location | Fix |
|-------|----------|-----|
| **rightmfgsystems.html** | Vendor/partner page | Confirm it has appropriate noindex or canonical if it’s thin/duplicate |
| **Sitemap coverage** | sitemap.xml | Confirm all important indexable pages are included (~100 URLs vs 200+ HTML files; many may be redirects) |
| **Article dateModified** | Some article pages | Add dateModified where missing for Article schema completeness |
| **Learn more links** | Article content | Most are contextual (“Learn more in…”); a few could use more descriptive anchor text |

---

## 3. Title Length Audit (Sample)

| Page | Title Length | Status |
|------|--------------|--------|
| Equipment Financing No Money Down: 100% Financing Guide (2026) \| Axiant Partners | 64 chars | ⚠️ Long |
| Business Term Loans \| $10K-$5M+ Lump-Sum Capital for Expansion & Growth \| Axiant Partners | 73 chars | ⚠️ Long |
| What Documents Do I Need for an SBA Loan? \| Axiant Partners | 47 chars | ✅ |
| Equipment Financing Guides \| Axiant Partners | 38 chars | ✅ |
| Axiant Partners: Business Financing for U.S. Companies | 45 chars | ✅ |

**Guideline:** Aim for 50–60 characters. Google often truncates around 60.

---

## 4. Technical Checklist

| Item | Status |
|------|--------|
| Sitemap valid XML | ✅ |
| Sitemap in robots.txt | ✅ |
| Canonicals on all pages | ✅ |
| No duplicate robots meta | ✅ |
| OG image 1200×630 | ✅ |
| Favicon present | ✅ |
| lang attribute | ✅ en |
| viewport meta | ✅ |

---

## 5. Structured Data Checklist

| Schema Type | Homepage | Service Pages | Equipment | Articles |
|-------------|----------|---------------|-----------|----------|
| Organization | ✅ | — | — | — |
| WebSite | ✅ | — | — | — |
| BreadcrumbList | — | ✅ | ✅ | ✅ |
| FAQPage | ✅ | — | ✅ | — |
| Article | — | — | ✅ | ✅ |
| HowTo | — | — | ✅ | — |
| FinancialService | — | — | ✅ | — |

---

## 6. Content & Internal Linking

- Industry pages link to equipment guides and service pages.
- Equipment pages link to articles and service hubs.
- Equipment Guides nav works from equipment category pages.
- Footer links to privacy, terms, vendors.

**Suggestion:** Add more cross-links between related articles (e.g., SBA vs equipment financing) where relevant.

---

## 7. Recommended Action Plan

1. ~~**Shorten long titles**~~ – DONE: Equipment Financing No Money Down, Business Term Loans, TRAC Lease, Red Flags.
2. ~~**Add meta description to fix-and-flip-blog.html**~~ – DONE.
3. ~~**Remove duplicate dns-prefetch**~~ – DONE.
4. ~~**Add image width/height**~~ – DONE: index hero, CRE intro.
5. **Spot-check industry pages** – Ensure unique meta descriptions and strong H1s.
6. **Run live Core Web Vitals test** – Use PageSpeed Insights or Chrome DevTools.
7. **Monitor Search Console** – For crawl errors, indexing, and mobile usability.

---

## 8. Fixes Applied (Session)

- Removed duplicate `dns-prefetch` in index.html.
- Added meta description and viewport to fix-and-flip-blog.html.
- Shortened titles: equipment-financing-no-money-down, business-term-loans, trac-lease, red-flags.
- Added `width` and `height` to index hero image and commercial-real-estate cre-intro image.

---

*Report generated from codebase audit. Run live tools (PageSpeed Insights, Search Console, Screaming Frog) for production validation.*
