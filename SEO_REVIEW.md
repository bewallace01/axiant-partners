# SEO Review: Axiant Partners Website

**Date:** March 2, 2026  
**Scope:** Full site audit—technical SEO, content, schema, sitemap, and internal linking.

---

## Executive Summary

The site has a solid foundation: meta tags, Open Graph, schema markup, and redirects are in place. The main improvements are in **URL consistency** (sitemap and canonicals), **technical hygiene** (duplicate H1, mixed verification codes), and **content/social enhancements** (breadcrumbs, og:image size, Organization sameAs).

---

## 1. Sitemap Issues (High Priority)

**File:** `sitemap.xml`

| Issue | Detail |
|-------|--------|
| **Lists redirect sources, not destinations** | Sitemap includes URLs like `blog/what-do-lenders-look-for-sba-loan-approval.html`, `equipment-financing-blog.html`, `sba-loans-blog.html`—these 301 to `/topic/articles/` URLs. Search engines should discover final URLs, not redirects. |
| **Broken/redirect-only URLs** | `working-capital.html` is in sitemap but `working-capital-loans.html` is the actual page; `working-capital.html` may 404. |
| **Missing service pages** | `commercial-real-estate-loans.html`, `commercial-bridge-loans.html`, `fix-and-flip.html` are not in sitemap. |
| **Missing referral page** | `referral.html` is not in sitemap. |
| **Inconsistent article coverage** | Fix-and-flip articles use canonical `/fix-and-flip/articles/slug/` URLs; most other topics still list `blog/slug.html`. Articles in SBA, equipment, working capital, CRE, bridge, revenue-based, securities-based should use `/topic/articles/slug/` URLs in sitemap. |
| **Missing article hubs** | Sitemap has `fix-and-flip/articles/` but not `sba-loans/articles/`, `equipment-financing/articles/`, `business-line-of-credit/articles/`, etc. |
| **URL format** | Homepage uses `index.html`; canonical uses `https://www.axiantpartners.com/` (trailing slash). Consider standardizing. |
| **Dated lastmod** | Many entries show `2025-02-21`; update for accuracy. |

**Recommendation:** Rebuild sitemap to include only final crawlable URLs:
- All service/topic pages (e.g. `fix-and-flip.html`, `sba-loans.html`, …)
- All article hubs (`/sba-loans/articles/`, `/equipment-financing/articles/`, …)
- All individual articles at `/topic/articles/slug/`
- Core pages: `match.html`, `services.html`, `faq.html`, `contact.html`, `calculator.html`, `blog.html`, `glossary.html`, `referral.html`
- Equipment landing pages
- Legal: `privacy-policy.html`, `terms-and-conditions.html`, `vendors.html`
- Remove: `*-blog.html`, `blog/*.html`, any redirect-only URLs

---

## 2. Canonical & Schema URL Inconsistencies (High Priority)

**Problem:** Many blog files that 301 redirect still have canonicals and Article schema pointing to the old `blog/*.html` URL instead of the final `/topic/articles/slug/` URL.

**Examples:**
- `blog/sba-504-vs-conventional-commercial-real-estate-loan.html` — canonical and schema `url` point to `blog/...` but page redirects to `/commercial-real-estate-loans/articles/sba-504-vs-conventional-commercial-real-estate-loan/`
- Similar pattern across SBA, equipment, working capital, CRE, bridge, and other topics

**Fix-and-flip articles** are correctly set (canonical and schema point to `/fix-and-flip/articles/slug/`).

**Recommendation:** For every blog file that redirects:
1. Set `rel="canonical"` to the final destination (e.g. `/commercial-real-estate-loans/articles/sba-504-vs-conventional-commercial-real-estate-loan/`)
2. Update Article schema `url` to the same final URL
3. Update `og:url` to match

---

## 3. Google Site Verification Mismatch (Medium Priority)

| File | Verification code |
|------|-------------------|
| `index.html` | `465625784297c409` |
| `faq.html`, `match.html`, `services.html`, `blog.html` | `r6yyqb6FxWxmJGmr4GBVwPzRZ9flVFuz8Vt6CUkbarc` |

**Recommendation:** Use a single verification code site-wide. Confirm which code is active in Google Search Console and remove the other from all pages.

---

## 4. Duplicate H1 on Homepage (Medium Priority)

**File:** `index.html` (lines ~741, 749)

- First H1: `AXIANT PARTNERS` (in `<header>`)
- Second H1: `Business Financing Made Simple` (in hero)

**Recommendation:** Use one primary H1. Options:
- Make "AXIANT PARTNERS" an H2 or styled text
- Or make "Business Financing Made Simple" the single H1 and style the brand name differently (e.g. `<p>`, `<span>` with class)

---

## 5. Open Graph Image (Medium Priority)

**Current:** All pages use `https://www.axiantpartners.com/logo.jpg` for `og:image`.

**Issue:** Social platforms recommend 1200×630 px for `summary_large_image`. A logo may be smaller and may not display well on Facebook, LinkedIn, Twitter, etc.

**Recommendation:** Create a dedicated social image (1200×630) with logo + tagline or key message. Use it for `og:image` and `twitter:image` on key pages (home, services, main articles).

---

## 6. Organization Schema (Low–Medium Priority)

**File:** `index.html` (line 690)

```json
"sameAs": []
```

**Recommendation:** Add social profile URLs (LinkedIn, Twitter/X, Facebook, etc.) if they exist. Helps with entity recognition and Knowledge Panel.

---

## 7. Breadcrumbs (Low Priority)

**Current:** No BreadcrumbList schema or visible breadcrumbs on article/topic pages.

**Recommendation:** Add BreadcrumbList schema and optional visible breadcrumbs on:
- Article pages: Home → [Topic] → Articles → [Article title]
- Article hub pages: Home → [Topic] → Articles

---

## 8. Internal Linking Consistency (Low–Medium Priority)

**Current state:**
- Fix-and-flip service page uses canonical `/fix-and-flip/articles/slug/` links
- Other service pages and blog hub pages may still use `*-blog.html` or `blog/slug.html`

**Recommendation:** Prefer direct links to canonical URLs:
- Use `/topic/articles/` and `/topic/articles/slug/` instead of `*-blog.html` and `blog/slug.html`
- Reduces redirect hops and reinforces canonical structure

---

## 9. Image Alt Text (Low Priority)

**Current:** Logos and most images have alt text. Spot-check remaining images (especially on equipment landing and vendor pages) for descriptive alt attributes.

---

## 10. Content & Structure (Informational)

- **H1→H2→H3:** Generally consistent across pages
- **Meta descriptions:** Present and unique; typically 130–160 characters
- **Article length:** Typically 800–2000+ words
- **Redirects:** `_redirects` and `.htaccess` correctly map old blog/hub URLs to new structure

---

## Action Checklist

| Priority | Task |
|----------|------|
| High | Rebuild sitemap with only final URLs; add missing pages; remove redirect sources |
| High | Update canonicals, Article schema `url`, and `og:url` in all blog files to point to final `/topic/articles/slug/` URLs |
| Medium | Resolve Google verification code mismatch |
| Medium | Fix duplicate H1 on homepage |
| Medium | Create and use 1200×630 og:image for social sharing |
| Medium | Audit internal links on service pages and hubs; switch to canonical article URLs |
| Low | Add social URLs to Organization schema `sameAs` |
| Low | Add BreadcrumbList schema to articles and hubs |
| Low | Verify image alt text on all pages |

---

## File Reference Summary

| Item | Location |
|------|----------|
| Sitemap | `sitemap.xml` |
| Redirects | `_redirects`, `.htaccess` |
| Organization schema | `index.html` ~lines 683–690 |
| Homepage H1s | `index.html` ~lines 741, 749 |
| Blog canonicals | `blog/*.html` (multiple files) |
| Topic article structure | `{topic}/articles/{slug}/index.html` |
