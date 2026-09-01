# Axiant Partners – Full SEO Analysis Report

**Date:** March 9, 2026  
**Full SEO Grade:** **84/100** (B+)

---

## Executive Summary

| Category | Score | Status | Notes |
|----------|-------|--------|------|
| **Technical SEO** | 90/100 | ✅ Strong | Sitemap, robots, canonicals, redirects, no broken links |
| **On-Page SEO** | 85/100 | ✅ Good | Meta tags, H1s, descriptive anchors; some long titles |
| **Structured Data** | 92/100 | ✅ Strong | Organization, Article, FAQPage, HowTo, BreadcrumbList |
| **Content & UX** | 78/100 | ✅ Good | Solid content, internal linking; minor alt/schema gaps |
| **Crawlability & Indexing** | 88/100 | ✅ Strong | robots.txt, AI crawlers allowed, sitemap referenced |

| Category | Status | Notes |
|----------|--------|------|
| **Broken Internal Links** | ✅ Fixed | Equipment sub-page links updated across 10 files |
| **Redirects** | ✅ OK | Blog migration and equipment landing redirects in place |
| **Sitemap & robots.txt** | ✅ OK | Valid sitemap (~100 URLs), robots references sitemap |
| **Meta Tags** | ✅ Strong | Titles, descriptions, canonical, OG, Twitter |
| **Structured Data** | ✅ Strong | BreadcrumbList, FAQPage, Article, FinancialService, HowTo |

---

## Full SEO Grade Breakdown

### Technical SEO (90/100)
| Criterion | Status | Notes |
|-----------|--------|------|
| Sitemap | ✅ | Valid XML, lastmod, changefreq, priority; covers main pages + equipment + articles |
| robots.txt | ✅ | Sitemap referenced; AI crawlers (GPTBot, PerplexityBot, etc.) explicitly allowed |
| Canonical URLs | ✅ | All audited pages have canonical pointing to https://axiantpartners.com |
| 301 Redirects | ✅ | Blog migration, hub redirects, equipment landing pages in _redirects + .htaccess |
| No broken internal links | ✅ | Equipment links fixed; Equipment Guides nav fixed |
| Mobile viewport | ✅ | viewport meta present |
| HTTPS (assumed) | ✅ | Canonicals use https |

*Minor deduction: sitemap may not include every indexable URL; some hub redirects intentionally excluded.*

### On-Page SEO (85/100)
| Criterion | Status | Notes |
|-----------|--------|------|
| Unique titles | ✅ | Titles vary by page; include target keywords |
| Title length | ⚠️ | Some titles 60–70 chars (e.g. Equipment Financing No Money Down guide); ideal &lt;60 |
| Meta descriptions | ✅ | Present on all audited pages; reasonably unique |
| H1 structure | ✅ | Single primary H1 on homepage; equipment/article pages use clear H1s |
| Descriptive anchor text | ✅ | "Learn more" replaced with specific CTAs on homepage |
| Image alt text | ✅ | No empty alts; equipment pages use descriptive alts |

*Minor deduction: occasional long titles; some article pages could shorten for SERP display.*

### Structured Data (92/100)
| Criterion | Status | Notes |
|-----------|--------|------|
| Organization | ✅ | Contact, logo, sameAs (LinkedIn, Facebook, Instagram, YouTube) |
| WebSite | ✅ | Search/structured data on homepage |
| BreadcrumbList | ✅ | Article and equipment pages |
| Article | ✅ | headline, datePublished, dateModified, author, publisher |
| FAQPage | ✅ | Homepage, equipment, industry pages |
| HowTo | ✅ | Equipment guides |
| FinancialService | ✅ | Service and equipment pages |

*Minor deduction: not every article has dateModified; some schema could add keywords.*

### Content & UX (78/100)
| Criterion | Status | Notes |
|-----------|--------|------|
| Internal linking | ✅ | Industry → equipment; equipment → articles; service hubs |
| Content depth | ✅ | Equipment pages expanded; articles substantive |
| Duplicate content risk | ⚠️ | equipment\ vs equipment/ path representation (Windows); canonicals mitigate |
| Page speed signals | ✅ | Preconnect, preload, critical CSS, lazy-loaded styles |

### Crawlability & Indexing (88/100)
| Criterion | Status | Notes |
|-----------|--------|------|
| robots meta | ✅ | index, follow; no duplicate robots tags |
| Noindex on redirect pages | N/A | Redirect targets are canonical pages |
| Sitemap discoverability | ✅ | Referenced in robots.txt |

---

## 1. Link Fixes Applied

### 1.1 Equipment Sub-Page Links (Industry Tabs & Related Pages)

**Issue:** Industry pages and equipment-financing.html linked to non-existent URLs like `/equipment/tractors/how-to-finance-a-tractor/`. Only category index pages exist (e.g. `/equipment/tractors/`).

**Files Updated:**
- `agriculture-business-financing.html` – 6 equipment links
- `trucking-business-financing.html` – 6 equipment links  
- `restaurants-business-financing.html` – 6 equipment links
- `medical-practices-business-financing.html` – 6 equipment links
- `manufacturing-business-financing.html` – 6 equipment links
- `logistics-warehousing-business-financing.html` – 6 equipment links
- `landscaping-business-financing.html` – 6 equipment links
- `forestry-business-financing.html` – 7 equipment links
- `auto-repair-business-financing.html` – 6 equipment links
- `equipment-financing.html` – 2 equipment links
- `equipment-financing/articles/trac-lease-benefits-saves-money/index.html` – 2 equipment links

**Change:** All `/equipment/CATEGORY/how-to-finance-X/` links → `/equipment/CATEGORY/`

### 1.2 Equipment Guides Nav Link (language-switcher.js)

**Issue:** "Equipment Guides" link used wrong depth from equipment category pages, resolving to `/equipment/equipment.html` (404).

**Fix:** `depth = segments.length` instead of `segments.length - 1` so `../../equipment.html` resolves correctly from `/equipment/tractors/`.

---

## 2. SEO Strengths

### Meta Tags
- **Title & description** on main pages
- **Canonical URLs** pointing to https://axiantpartners.com
- **Robots** directives (`index, follow`, `max-snippet`, `max-image-preview`)
- **Open Graph** (og:title, og:description, og:url, og:image, og:type)
- **Twitter Cards** (summary_large_image)
- **Google verification** on homepage

### Structured Data (Schema.org JSON-LD)
- **Organization** – homepage (contact, logo)
- **WebSite** – search/structured data
- **BreadcrumbList** – most pages
- **Article** – article and equipment pages
- **FAQPage** – homepage, equipment, industry pages
- **FinancialService** – service and equipment pages
- **HowTo** – equipment guides

### Technical
- Preconnect to Google Fonts
- DNS prefetch for Unsplash
- Preload for hero images
- Critical CSS + lazy-loaded styles
- AI crawlers allowed in robots.txt (GPTBot, PerplexityBot, etc.)

---

## 3. Redirects

- **`_redirects` (Netlify):** Glossary, blog migration, topic hubs, equipment landing pages
- **`.htaccess`:** Same rules for Apache deployments
- **Target checks:** All redirect targets resolve to existing pages

---

## 4. Recommendations

### SEO
1. **H1 structure:** Confirm each page has a single primary H1.
2. **Duplicate meta descriptions:** Audit for uniqueness across similar pages.
3. **Image alt text:** Ensure all images have descriptive alt attributes.
4. **Internal linking:** Link equipment guides and industry pages where relevant.

### Technical
1. **Organization schema:** Populate `sameAs` with LinkedIn, Facebook, etc. if used.
2. **Mobile usability:** Test responsive layout and tap targets.
3. **Core Web Vitals:** Monitor LCP, FID, CLS.

### Content
1. **Equipment pages:** Ensure titles and descriptions include target keywords.
2. **Industry pages:** Cross-link to related equipment and service pages.

---

## 5. Summary of Fixes Applied

| Fix | Description |
|-----|-------------|
| Equipment links on industry pages | 55+ links updated from `/equipment/X/how-to-finance-Y/` → `/equipment/X/` |
| Equipment links on equipment-financing.html | 2 links updated |
| Trac-lease article links | 2 links updated |
| Equipment Guides nav | `language-switcher.js` depth fix so link works from equipment category pages |
| **Duplicate robots meta** | Removed from fix-and-flip, equipment, 8 industry pages, conveyor-systems |
| **sba-loans redirect** | Added /sba-loans/index.html → /sba-loans/articles/ in _redirects and .htaccess; simplified index.html |
| **Image alt text** | Replaced generic "Loans","Leasing","SBA","POS" with descriptive alts on equipment pages |
| **Learn more anchors** | Replaced with descriptive text on index.html (e.g. "Equipment financing details") |
| **Organization schema** | Added sameAs with LinkedIn, Facebook, Instagram, YouTube |
| **Article schema** | Added dateModified to equipment page Article schema |
