# SEO Review: Services Dropdown Pages

**Date:** March 7, 2026  
**Scope:** All pages linked from the Services dropdown (sba-loans, equipment-financing, equipment, business-line-of-credit, working-capital-loans, business-term-loans, commercial-real-estate-loans, commercial-bridge-loans, revenue-based-financing, securities-based-lending, fix-and-flip)

---

## Executive Summary

The service pages have a strong SEO foundation: canonicals, BreadcrumbList and FAQPage schema, Open Graph, and sitemap inclusion. Main issues: **inconsistent Services navigation** (some pages omit CRE, RBF, SBL, Revenue-Based, Securities-Based), **equipment.html** thin content and generic og:image, **commercial-bridge-loans** slightly under 2.5k words, and **BLOC/BTL** missing twitter:image on some pages. Most pages meet or exceed 2.5k words and have high-intent apply-focused copy.

---

## 1. Services Dropdown Pages Inventory

| Page | File | Word Count | Target 2.5k+ |
|------|------|------------|--------------|
| SBA Loans | sba-loans.html | 2,593 | Yes |
| Equipment Financing | equipment-financing.html | 2,867 | Yes |
| Equipment by Type | equipment.html | 650 | **No** |
| Business Line of Credit | business-line-of-credit.html | 2,972 | Yes |
| Working Capital Loans | working-capital-loans.html | 2,657 | Yes |
| Business Term Loans | business-term-loans.html | 2,930 | Yes |
| Commercial Real Estate Loans | commercial-real-estate-loans.html | 2,805 | Yes |
| Commercial Bridge Loans | commercial-bridge-loans.html | 2,405 | **Slightly under** |
| Revenue-Based Financing | revenue-based-financing.html | 2,514 | Yes |
| Securities-Based Lending | securities-based-lending.html | 2,600 | Yes |
| Fix and Flip | fix-and-flip.html | 2,516 | Yes |

---

## 2. Meta Tags & Titles

### Meta Descriptions (Target: 150–160 chars)

| Page | Chars | Status |
|------|-------|--------|
| SBA Loans | 116 | OK, could add keywords |
| Equipment Financing | 116 | OK |
| Equipment by Type | 156 | OK |
| Business Line of Credit | 124 | OK |
| Working Capital Loans | 148 | OK |
| Business Term Loans | 129 | OK |
| Commercial Real Estate | 144 | OK |
| Commercial Bridge Loans | 120 | OK |
| Revenue-Based Financing | 112 | OK |
| Securities-Based Lending | 115 | OK |
| Fix and Flip | 107 | OK |

All descriptions include primary keywords and a clear CTA or value prop. Some could be extended to 150–160 chars for more SERP real estate.

### Page Titles (Target: 50–60 chars, max ~70)

| Page | Chars | Status |
|------|-------|--------|
| SBA Loans | 52 | OK |
| Equipment Financing | 54 | OK |
| Equipment by Type | 42 | OK, could add location/benefit |
| Business Line of Credit | 54 | OK |
| Working Capital Loans | 53 | OK |
| Business Term Loans | 64 | OK |
| Commercial Real Estate | 62 | OK |
| Commercial Bridge Loans | 52 | OK |
| Revenue-Based Financing | 55 | OK |
| Securities-Based Lending | 72 | **Slightly long** |
| Fix and Flip | 66 | OK |

Securities-Based Lending title ("Securities-Based Lending: Unlock Liquidity Without Selling Your Portfolio | $10K-$10M+ | Axiant Partners") may be truncated on some SERPs. Consider shortening to ~60 chars.

---

## 3. Technical SEO

### Canonical URLs
All service pages have correct `rel="canonical"` pointing to `https://www.axiantpartners.com/{page}.html`.

### Schema Markup
All pages include:
- **BreadcrumbList** (Home → [Service])
- **FinancialService**
- **WebPage**
- **FAQPage** (5–6 questions each)

BLOC and WCL also include **HowTo** schema for the apply process. Good for rich results.

### Open Graph & Twitter
- All pages have `og:title`, `og:description`, `og:url`, `og:image`, `og:image:width`, `og:image:height`
- **equipment.html** uses `logo.jpg` for og:image instead of a service-specific 1200×630 image
- Most use page-specific hero images (sba-hero.png, rbf-hero.png, sbl-hero.png, etc.)
- **twitter:image** – Present on WCL, BTL, CRE, CBL; missing on SBA, EF, BLOC, RBF, SBL, FAF, equipment

**Recommendation:** Add `twitter:image` to all service pages for consistent social sharing.

---

## 4. Navigation Inconsistency (High Priority)

The Services dropdown differs across pages. Users on some pages cannot see or reach all services.

| Page | Missing from Nav |
|------|------------------|
| sba-loans.html | Commercial Real Estate, Commercial Bridge, Revenue-Based, Securities-Based |
| equipment-financing.html | Commercial Real Estate, Commercial Bridge, Revenue-Based, Securities-Based (has Equipment by Type) |
| business-line-of-credit.html | CRE, CBL, RBF, SBL (has Equipment by Type) |
| working-capital-loans.html | CRE, CBL, RBF, SBL (has Equipment by Type) |
| business-term-loans.html | CRE, CBL, RBF, SBL (has Equipment by Type) |
| commercial-real-estate-loans.html | Equipment by Type, RBF, SBL |
| commercial-bridge-loans.html | Equipment by Type, RBF, SBL |
| revenue-based-financing.html | Equipment by Type (has CRE, CBL, RBF, SBL) |
| securities-based-lending.html | Equipment by Type (has full list: CRE, CBL, RBF, SBL) |
| fix-and-flip.html | Equipment by Type, RBF, SBL |

**Recommendation:** Standardize the Services dropdown across all pages to the full list used on securities-based-lending.html:

1. SBA Loans  
2. Equipment Financing  
3. Business Line of Credit  
4. Working Capital Loans  
5. Business Term Loans  
6. Commercial Real Estate Loans  
7. Commercial Bridge Loans  
8. Revenue-Based Financing  
9. Securities-Based Lending  
10. Fix and Flip  

Optionally include "Equipment by Type" where it adds value (e.g., under or after Equipment Financing).

---

## 5. Content & Structure

### H1 Usage
- All pages have a single, descriptive H1
- H1s align with primary keywords and value proposition

### Heading Hierarchy
- Consistent H2 → H3 structure
- Use-case cards, amounts, why-choose, process, FAQs follow Equipment Financing pattern on rebuilt pages

### Internal Linking
- Service pages cross-link to related services (e.g., SBA → CRE, RBF → working capital)
- Article sections link to `/topic/articles/` canonical URLs
- Match.html (Apply) and contact/phone CTAs present throughout

---

## 6. Page-Specific Issues

### equipment.html (Equipment by Type)
- **Word count:** 650 words – thin for a hub page
- **og:image:** Uses `logo.jpg` – create a 1200×630 equipment hub image
- **meta robots:** No explicit `index, follow` (relies on default)
- **Schema:** No BreadcrumbList, FinancialService, or FAQPage
- **Recommendation:** Add schema, consider expanding intro copy or adding short descriptions per equipment type to reach 1,200+ words

### commercial-bridge-loans.html
- **Word count:** 2,405 – slightly under 2.5k target
- **Recommendation:** Add a "States We Serve" or "What You'll Need" section (as on RBF/SBL) to reach 2,500+

### equipment-financing.html
- **og:image:** Uses `construction-industry-overview.png` – not page-specific hero; consider `ef-hero.png` or similar if available for consistency

---

## 7. Sitemap
All 11 service pages are in sitemap.xml with priority 0.8 (equipment.html and equipment-financing.html). Article hubs and individual articles use canonical `/topic/articles/` URLs. No issues found.

---

## 8. Image Alt Text
Service pages use descriptive alt text on hero and card images (e.g., "Securities-based lending and portfolio-backed liquidity", "Business working capital and liquidity"). No obvious missing or generic alts on main service pages.

---

## 9. Competitor & Intent Alignment
- Apply-focused CTAs throughout
- Trust stats, use cases, amounts, process steps, FAQs
- Phone and Apply buttons in hero and CTA sections
- High word counts support topical authority

---

## Action Checklist

| Priority | Task |
|----------|------|
| High | Standardize Services dropdown to full 10-item list on all service pages |
| Medium | Add twitter:image to SBA, EF, BLOC, RBF, SBL, FAF, equipment |
| Medium | Create 1200×630 og:image for equipment.html; replace logo.jpg |
| Medium | Expand commercial-bridge-loans to 2,500+ words |
| Low | Shorten Securities-Based Lending title to ~60 chars |
| Low | Expand equipment.html content and add schema (BreadcrumbList, FinancialService) |
| Low | Add meta robots="index, follow" to equipment.html if not inheriting |

---

## Summary Scores (Per Page)

| Page | Meta | Schema | Nav | Content | Images | Overall |
|------|------|--------|-----|---------|--------|---------|
| SBA Loans | 9 | 9 | 6 | 9 | 9 | 8.4 |
| Equipment Financing | 9 | 9 | 6 | 9 | 8 | 8.2 |
| Equipment by Type | 7 | 5 | 6 | 4 | 4 | 5.2 |
| Business Line of Credit | 9 | 9 | 6 | 9 | 8 | 8.2 |
| Working Capital Loans | 9 | 9 | 6 | 9 | 9 | 8.4 |
| Business Term Loans | 9 | 9 | 6 | 9 | 9 | 8.4 |
| Commercial Real Estate | 9 | 9 | 6 | 9 | 9 | 8.4 |
| Commercial Bridge Loans | 9 | 9 | 6 | 9 | 9 | 8.4 |
| Revenue-Based Financing | 9 | 9 | 8 | 9 | 9 | 8.8 |
| Securities-Based Lending | 9 | 9 | 9 | 9 | 9 | 9.0 |
| Fix and Flip | 9 | 9 | 6 | 9 | 9 | 8.4 |

*Nav score reflects whether the page includes the full Services list. Content score reflects word count and structure.*
