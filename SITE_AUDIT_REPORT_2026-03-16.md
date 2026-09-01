# Full Site Audit Report – Axiant Partners

**Date:** March 16, 2026  
**Scope:** SEO, linking, encoding, optimization (post–encoding fixes)

---

## Executive Summary

| Area | Status | Critical fixes applied |
|------|--------|------------------------|
| **SEO** | ✅ Addressed | H1 on match page, meta/canonical on calculator-embed, duplicate titles resolved |
| **Linking** | ✅ Improved | Root pages now use `/match.html` (absolute) for consistency |
| **Encoding** | ✅ Clean | No remaining replacement characters or mojibake in HTML |
| **Structured data** | ✅ OK | Valid JSON-LD on critical pages; no broken schema |
| **Sitemap / robots** | ✅ OK | sitemap.xml present; .htaccess redirects in place |

---

## 1. Critical issues (FIXED)

### SEO
- **match.html** – Had no `<h1>` (only `<h2>Apply for Business Financing</h2>`). **Fixed:** Promoted to `<h1>Apply for Business Financing</h1>`.
- **calculator-embed.html** – Missing `<meta name="description">` and `<link rel="canonical">`. **Fixed:** Added description and canonical to `https://axiantpartners.com/calculator-embed.html`.
- **Duplicate titles** – Two pairs of pages shared identical titles (bad for SEO):
  - `equipment-financing/index.html` (redirect) and `equipment-financing/articles/index.html` both had “Equipment Financing Articles: Loans vs Leases | Axiant Partners”. **Fixed:** Redirect page title set to “Equipment Financing | Axiant Partners”.
  - `revenue-based-financing/index.html` (redirect) and `revenue-based-financing/articles/index.html` both had “Revenue-Based Financing Articles | Axiant Partners”. **Fixed:** Redirect page title set to “Revenue-Based Financing | Axiant Partners”.

### Linking
- **Relative `match.html` on root** – Many root-level pages used `href="match.html"`. From subpages this would resolve incorrectly. **Fixed:** All root-level HTML files now use `href="/match.html"` (38 files updated).

---

## 2. Warnings / recommendations (optional follow-up)

### SEO
- **Redirect index pages** – Topic index pages (e.g. `commercial-real-estate-loans/index.html`, `business-line-of-credit/index.html`) that immediately redirect to `articles/` have minimal content. Canonicals already point to the destination; consider keeping them noindex if you don’t want them ever indexed.
- **Title length** – Some article/guide titles are 60–70 characters. Trimming to under 60 can improve SERP display; not critical.

### Linking
- **Equipment paths** – Links use trailing-slash directory URLs (e.g. `equipment/stump-grinders/`). This matches canonicals and is consistent; no change needed unless you standardize on a different URL style.
- **Internal link audit** – No broken internal links to `/blog/`, `/topic/`, or bare `/equipment` were found. Equipment and article links align with existing structure.

### Duplicate content
- **Path style** – Repo has both backslash and forward-slash paths (e.g. `equipment\stump-grinders\` vs `equipment/stump-grinders/`). These are the same logical page. Ensure production serves only one URL style (e.g. forward-slash) and redirects the other to avoid duplicate content.

---

## 3. What was verified (no issues)

### Critical pages
- **index.html** – One H1, canonical, title, meta description, valid JSON-LD (Organization, WebSite, WebPage, FAQPage).
- **equipment.html** – One H1, canonical, title, meta description, valid JSON-LD.
- **match.html** – Canonical, title, meta description, valid WebPage schema; H1 added (see above).
- **equipment/stump-grinders/index.html** – One H1, canonical, multiple schema types (BreadcrumbList, FinancialService, FAQPage, Article, HowTo), valid.

### Encoding
- No `ï¿½` (mojibake) or Unicode replacement character (U+FFFD) found in HTML. Previous encoding fixes (en-dash → hyphen, bullet checkmarks, trailing “?”) are in place.

### Technical
- **Canonicals** – All audited pages use `https://axiantpartners.com/...`.
- **Meta descriptions** – Present on all critical and sampled pages; none under 50 characters.
- **Sitemap** – `sitemap.xml` exists and includes key URLs (home, match, services, calculator, embed-calculator, blog, equipment, articles).
- **Redirects** – `.htaccess` defines 301s for blog migration and hub redirects (e.g. `sba-loans-blog.html` → `sba-loans/articles/`). No conflicting rules found for the audited flows.

---

## 4. Files changed in this audit

| File | Change |
|------|--------|
| `match.html` | `<h2>` → `<h1>` for main heading; `href="match.html"` → `href="/match.html"` in nav |
| `calculator-embed.html` | Added `<meta name="description">` and `<link rel="canonical">` |
| `equipment-financing/index.html` | Title set to “Equipment Financing \| Axiant Partners” (removes duplicate with articles index) |
| `revenue-based-financing/index.html` | Title set to “Revenue-Based Financing \| Axiant Partners” (removes duplicate with articles index) |
| `index.html` | All `href="match.html"` → `href="/match.html"` |
| `equipment.html` | All `href="match.html"` → `href="/match.html"` |
| 36 other root-level `.html` files | All `href="match.html"` → `href="/match.html"` |

---

## 5. Summary

- **Critical:** Match page H1, calculator-embed SEO tags, and duplicate titles are fixed. Root-level match links are standardized to `/match.html`.
- **SEO:** Canonicals, meta descriptions, and structured data are in good shape on critical and sampled pages.
- **Linking:** No broken internal link patterns found; equipment and article URLs are consistent.
- **Encoding:** Site is clean after the earlier question-mark and range-character fixes.

For ongoing checks: run a crawl (e.g. Screaming Frog or Sitebulb) after deployment to confirm no 404s and that canonicals match live URLs. Re-run encoding checks if new content is added from external sources (e.g. copy-paste from Word or other encodings).
