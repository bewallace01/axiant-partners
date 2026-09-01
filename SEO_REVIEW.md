# Full SEO Review — Axiant Partners

**Date:** March 8, 2026  
**Scope:** Sitemap, structure, on-page SEO, technical SEO by section

---

## Executive Summary

| Category       | Status   | Key Findings |
|----------------|----------|--------------|
| Sitemap        | Issues   | Missing industries.html; structure is sound |
| Services       | Good     | Solid meta, canonicals, schema |
| Industries     | Good     | Good meta; industries hub missing from sitemap |
| Equipment      | Issues   | Relative og:image on all equipment articles (44 pages) |
| Articles       | Good     | Breadcrumbs, Article/FAQ/HowTo schema; some fixes needed |
| Technical SEO  | Good     | Gzip, canonicals, robots.txt; Organization schema needs verification |

---

## 1. Sitemap Structure

### Current State

- **Location:** `sitemap.xml`, referenced in `robots.txt`
- **URLs:** ~100 indexable pages
- **Generator:** `scripts/generate_sitemap.py` (Python)
- **Excludes redirects:** Correctly omits *-blog.html and topic index paths that 301

### Section Breakdown

| Section | In Sitemap | Count | Notes |
|---------|------------|-------|-------|
| **Core** | Yes | 8 | /, match, services, faq, contact, calculator, blog, referral |
| **Services** | Yes | 11 | sba-loans, equipment-financing, equipment, business-line-of-credit, etc. |
| **Industries** | Partial | 10 | Individual industry pages only; **industries.html hub missing** |
| **Equipment** | Yes | 56 | 28 categories + 28 how-to articles |
| **Article hubs** | Yes | 10 | /topic/articles/ |
| **Articles** | Yes | ~55 | Per-topic articles; excludes business-term-loan-vs-line-of-credit (301) |
| **Legal/utility** | Yes | 4 | vendors, rightmfgsystems, privacy, terms |

### Sitemap Issues

1. **Missing `industries.html`** — Hub page for industry-specific financing is not in sitemap.
2. **Priority/changefreq** — Reasonable: home 1.0, match/services 0.9, industries/services 0.8, articles 0.7, legal 0.4.
3. **lastmod** — All use generation date; could use file mtime for articles.
4. **Equipment landing pages** — Script lists legacy pages (e.g. dump-truck-financing.html); many may not exist. Current structure uses `/equipment/[type]/` and `/equipment/[type]/how-to-finance-*/`; legacy paths should be dropped if 404.

### Recommendations

- Add `industries.html` to sitemap (priority 0.85).
- Remove or verify legacy equipment paths in the generator.
- Run sitemap generator after content changes to keep lastmod accurate.

---

## 2. Services Section

**Pages:** services.html, sba-loans.html, equipment-financing.html, equipment.html, business-line-of-credit.html, working-capital-loans.html, business-term-loans.html, commercial-real-estate-loans.html, commercial-bridge-loans.html, fix-and-flip.html, revenue-based-financing.html, securities-based-lending.html

### Strengths

| Element | Status |
|---------|--------|
| Canonical URLs | All absolute, correct |
| Meta description | Present, ~150–160 chars |
| Title tags | Unique, include "Axiant Partners" |
| OG/Twitter | Present; og:image absolute |
| Schema | FinancialService or WebPage where appropriate |
| H1 | One per page, keyword-aligned |

### Gaps

- **Organization schema** — Many pages reference `publisher: {"@id": "https://axiantpartners.com/#organization"}` but the Organization with `@id` must exist somewhere (e.g. index.html). Needs verification.
- **Internal links** — Services should cross-link where relevant (e.g. equipment ↔ equipment-financing).

---

## 3. Industries Section

**Pages:** industries.html (hub), construction-business-financing.html, trucking-business-financing.html, agriculture-business-financing.html, forestry-business-financing.html, landscaping-business-financing.html, manufacturing-business-financing.html, medical-practices-business-financing.html, restaurants-business-financing.html, auto-repair-business-financing.html, logistics-warehousing-business-financing.html

### Strengths

| Element | Status |
|---------|--------|
| Meta description | Present, industry-specific |
| Canonical | Correct absolute URLs |
| OG/Twitter | Complete |
| H1 | Unique per industry |
| robots | index, follow on sample (construction) |

### Issues

- **industries.html missing from sitemap** — Fix in `generate_sitemap.py`.
- **Internal linking** — Industries hub should link to all 10 industry pages; industry pages should link back to hub and relevant services.

---

## 4. Equipment Section

**Structure:**  
`/equipment.html` → `/equipment/[category]/` → `/equipment/[category]/how-to-finance-[item]/`

**Examples:** forklifts, excavators, semi-trucks, dental-equipment, etc.

### Strengths

| Element | Status |
|---------|--------|
| Breadcrumbs | BreadcrumbList schema on how-to pages |
| Article schema | Headline, description, datePublished, dateModified |
| FAQPage / HowTo | Used where relevant (e.g. forklift) |
| CollectionPage | On category hubs |
| H1 hierarchy | Category: "X Financing"; How-to: "How to Finance X" |

### ~~Critical Issue: Relative og:image~~ (Fixed)

All equipment pages now use **absolute** og:image URLs (e.g. `https://axiantpartners.com/assets/...`).

### Other Notes

- Equipment category pages use absolute og:image (e.g. forklifts index).
- Internal links: category → how-to; how-to → category and equipment hub.

---

## 5. Articles Section

**Topics:** SBA loans, equipment financing, business line of credit, working capital, business term loans, commercial real estate, commercial bridge, fix-and-flip, revenue-based financing, securities-based lending

### Strengths

| Element | Status |
|---------|--------|
| BreadcrumbList | On all sampled articles |
| Article schema | headline, description, url, datePublished, dateModified, author, publisher |
| OG type | article |
| article:published_time / article:modified_time | Present |
| Canonical | Correct, trailing-slash format |
| H1 | Unique, matches headline |

### Gaps

- **og:image** — Some use generic logo.jpg; topic-specific images would improve CTR.
- **Internal linking** — Add "Related articles" or "More from [Topic]" blocks.
- **Character encoding** — One article had `` in schema description; fix encoding.
- **Keywords** — Inconsistent; add where it supports topical relevance.

---

## 6. Core Pages (Home, Match, Blog, FAQ, Contact, Calculator)

### Home (index.html)

| Element | Status |
|---------|--------|
| Title | "Commercial Lending & Business Financing \| Get Matched \| Axiant Partners" |
| Meta description | 155 chars, keyword-rich |
| Canonical | https://axiantpartners.com/ |
| OG/Twitter | Complete |
| Google verification | Present |
| Preconnect/dns-prefetch | Fonts, Unsplash |
| Preload | Hero images |

**Organization schema:** Ensure `{"@type":"Organization","@id":"https://axiantpartners.com/#organization"}` is defined on the homepage (or a shared template) so publisher references resolve.

### Match, FAQ, Contact, Calculator

- Canonical, meta, and titles present.
- Match as primary CTA deserves strong internal links and optional CTA schema.

### Blog (blog.html)

- In sitemap with changefreq weekly.
- Hub for topic-specific article sections.
- Consider adding ItemList schema for article listings.

---

## 7. Technical SEO

| Item | Status |
|------|--------|
| robots.txt | Allow /, Sitemap URL correct |
| Canonicals | Consistently absolute |
| Redirects | 301 for legacy URLs; no redirect chains in sitemap |
| Mobile | viewport meta present |
| Gzip | Enabled in .htaccess |
| HTTPS | Canonicals use https |
| Trailing slashes | Consistent for directory URLs |

### Recommendations

1. Add `width` and `height` to images to reduce CLS.
2. Confirm Organization schema with `@id` on homepage.
3. Add optional `image` object to Article schema for rich results.

---

## 8. Action Items (Prioritized)

### High priority (Done)

1. ~~Add `industries.html` to sitemap~~ ✓
2. ~~Change equipment how-to articles from relative to absolute `og:image` URLs~~ ✓

### Medium priority

3. Verify and add Organization schema on homepage if missing.
4. Clean legacy equipment paths from sitemap generator or add 404 handling.
5. Use article-specific og:images where possible.

### Lower priority

6. Add "Related articles" or "More from [Topic]" blocks.
7. Use file mtime for lastmod in sitemap.
8. Add ItemList schema to blog/article hub pages.
9. Add `image` to Article schema for key pages.

---

## 9. Sitemap Structure Reference (Target)

```
/
├── Core (8)
│   /, match, services, faq, contact, calculator, blog, referral
├── Services (11)
│   sba-loans, equipment-financing, equipment, business-line-of-credit, ...
├── Industries (11) ← add industries.html
│   industries, construction-*, trucking-*, agriculture-*, ...
├── Equipment (56)
│   equipment/[category]/ + equipment/[category]/how-to-finance-*/
├── Article hubs (10)
│   /topic/articles/
├── Articles (~55)
│   /topic/articles/[slug]/
└── Legal (4)
    vendors, rightmfgsystems, privacy, terms
```

---

*Report generated from codebase analysis. Re-run sitemap generator and validate in GSC after fixes.*
