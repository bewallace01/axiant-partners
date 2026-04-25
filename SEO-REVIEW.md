# Full SEO Review: Axiant Partners Site

**Review date:** March 16, 2026  
**Scope:** Site-wide technical, on-page, and content/linking SEO.

---

## 1. Executive Summary

The site has a solid SEO foundation: consistent canonicals, meta descriptions, and titles across sampled pages; Organization and Article/Breadcrumb/FAQ schema; a single sitemap and clear robots.txt; and strong internal linking from hub pages and related articles. The main gaps addressed in this review are **sitemap coverage** (missing article URLs added) and **recommendations** for ongoing improvements (meta length, duplicate-like content, and optional enhancements).

---

## 2. Technical SEO

### 2.1 Crawlability & indexing

| Item | Status | Notes |
|------|--------|------|
| **robots.txt** | ✅ Good | Allows all user-agents, references sitemap, allows common AI crawlers (GPTBot, PerplexityBot, etc.). |
| **Sitemap** | ✅ Fixed | Single `sitemap.xml` with 50k limit. **Update:** Missing article URLs were added (e.g. MCA mistakes, CRE red flags, fix-and-flip red flags, SBL traps, RBF not right option, CRE mistakes, fix-and-flip mistakes, RBF traps, red flags MCA). |
| **Canonicals** | ✅ Good | Sampled pages use `rel="canonical"` with absolute URLs. Pattern: `https://axiantpartners.com/...` with trailing slash for directory-style URLs (e.g. `/merchant-cash-advance/articles/mca-mistakes-keep-you-in-cycle/`). |
| **Meta robots** | ✅ Good | Articles use `index, follow, max-snippet:-1, max-image-preview:large` where checked. |
| **Google site verification** | ✅ Present | On homepage and blog. |

**Recommendation:** Keep sitemap in sync when adding or retiring pages. Consider splitting into multiple sitemaps (e.g. by section) if the URL count grows significantly (e.g. 1,000+).

### 2.2 URL structure

- **Pattern:** Consistent. Service hubs use `.html` (e.g. `/merchant-cash-advance.html`). Articles use directory + `index.html` with trailing slash in canonicals (e.g. `/merchant-cash-advance/articles/mca-mistakes-keep-you-in-cycle/`).
- **Canonical consistency:** Canonicals match this pattern (trailing slash for directories). No mixed http/https or www/non-www observed in sampled canonicals.

**Recommendation:** Ensure server/hosting serves trailing-slash URLs consistently (301 from non-canonical if needed) so canonicals and sitemap match live URLs.

### 2.3 Security & performance (headers)

- **`_headers` (Netlify):** X-Frame-Options, X-Content-Type-Options, Referrer-Policy set. Cache rules for HTML (revalidate), static assets (long cache). Calculator embed has `frame-ancestors *` for iframe use.
- **HTTPS:** Canonicals and sitemap use `https://axiantpartners.com`. Ensure SSL and redirects are configured on the host.

---

## 3. On-Page SEO

### 3.1 Title tags

- **Homepage:** “Axiant Partners: Business Financing for U.S. Companies” — clear and branded.
- **Articles:** Descriptive, include topic and “| Axiant Partners” (e.g. “MCA Mistakes That Keep You in a Cycle | Axiant Partners”).
- **Length:** Most within 50–60 characters; some longer. Google typically displays ~50–60 characters; consider trimming only if truncation is an issue in SERPs.

**Recommendation:** Keep primary keyword near the start where it reads naturally; keep “Axiant Partners” for brand.

### 3.2 Meta descriptions

- **Presence:** Meta description present on all sampled pages.
- **Length:** Many in the 150–160 character range; a few may be short or long. Aim for ~155 for best display.
- **Content:** Descriptive and relevant to the page topic; often include a CTA or outcome (e.g. “avoid MCA mistakes that trap you and how to break the cycle”).

**Recommendation:** Audit any pages with very short (&lt;120) or very long (&gt;160) descriptions and adjust for clarity and SERP display.

### 3.3 Headings & content structure

- **H1:** One main H1 per page (e.g. article title). No duplicate H1s in sampled files.
- **Structure:** Articles use H2 for main sections; some use H3 for subsections. Logical hierarchy.
- **Content depth:** Article pages have substantial copy (e.g. 2,500+ words on key guides) and internal links to hub and related articles.

**Recommendation:** Keep a single H1 per page; use H2/H3 for scannable structure. Continue internal links in body and “Related resources” sections.

### 3.4 Structured data (Schema.org)

| Type | Status | Notes |
|------|--------|------|
| **Organization** | ✅ | On homepage (`@id`: `https://axiantpartners.com/#organization`). Name, url, logo, contactPoint, sameAs. |
| **Article** | ✅ | On article pages: headline, description, url, image, datePublished/Modified, author, publisher (`@id` to organization). |
| **BreadcrumbList** | ✅ | On article and hub pages; 3–4 levels (Home → Service → Articles → Article). |
| **FAQPage** | ✅ | On many articles; questions/answers match content. |
| **ItemList / CollectionPage** | ✅ | On hub article index pages (e.g. MCA articles, CRE articles) for listing pages. |

**Recommendation:** Ensure every article that should appear as an article in Search has Article (and BreadcrumbList where applicable). Keep FAQPage Q&A accurate and non-spammy.

---

## 4. Internal Linking

### 4.1 Hub structure

- **Blog hub:** `blog.html` links to all topic hubs (SBA, equipment, LOC, working capital, term loans, CRE, bridge, RBF, MCA, SBL, fix-and-flip).
- **Topic hubs:** Each service has an `articles/` index with a grid of article cards and intro copy that now links to key articles (e.g. “MCA mistakes that keep you in a cycle”, “red flags in MCA agreements”).
- **Article pages:** “Back to [Service] Articles” and “| All Articles” (where present); lead paragraph links to the service page; “Related resources” and in-body links to sibling and cross-hub articles.

### 4.2 Cross-linking

- **Sibling links:** Related articles link to each other (e.g. Red Flags MCA ↔ MCA Mistakes; CRE Mistakes ↔ CRE Red Flags; Fix and Flip Mistakes ↔ Fix and Flip Loan Red Flags; SBL Risks ↔ SBL Traps; RBF Traps ↔ When Is RBF NOT the Right Option).
- **Cross-hub:** Working capital, MCA, RBF, and general articles link across hubs (e.g. “how to get out of bad business debt”, “revenue-based financing vs MCA”).
- **Conversion:** Match/apply and key service pages linked from CTAs and nav.

**Recommendation:** Continue adding 1–2 contextual in-body links per new article to relevant existing pieces; keep “Related resources” lists to 4–7 high-value links.

---

## 5. Content & Duplication

### 5.1 Duplicate / near-duplicate content

- **URLs:** Single canonical per URL; no obvious duplicate content from multiple URLs in sampled set.
- **Thin content:** Not observed on main service or article pages; article content is substantive.
- **Equipment/industry pages:** Many equipment and industry pages exist; ensure each has distinct, useful content and unique meta description/title to avoid template-like duplication in search.

**Recommendation:** If you add more equipment or industry landing pages, keep titles and descriptions unique and content meaningfully differentiated.

### 5.2 Blog / article indexes

- **blog.html:** Lists topic hubs only (no full article list). Good for clarity and crawl budget.
- **Topic article indexes:** Each hub’s `articles/index.html` lists that hub’s articles with ItemList/CollectionPage schema. `numberOfItems` and item list are updated when new articles are added.

---

## 6. Sitemap Fix Applied

The following URLs were **added** to `sitemap.xml` so all important articles are included for discovery:

- `merchant-cash-advance/articles/mca-mistakes-keep-you-in-cycle/`
- `merchant-cash-advance/articles/red-flags-mca-agreements/`
- `commercial-real-estate-loans/articles/cre-loan-mistakes-delay-deny-closing/`
- `commercial-real-estate-loans/articles/cre-loan-red-flags-recourse-prepayment-balloon-closing-costs/`
- `fix-and-flip/articles/fix-and-flip-mistakes-to-avoid/`
- `fix-and-flip/articles/fix-and-flip-loan-red-flags-points-fees-draw-schedule-prepayment/`
- `revenue-based-financing/articles/revenue-based-financing-traps/`
- `revenue-based-financing/articles/when-is-revenue-based-financing-not-right-option/`
- `securities-based-lending/articles/securities-based-lending-traps-margin-calls-cross-collateral-concentration/`

Ensure any future new articles are also added to the sitemap (and to the hub’s ItemList where applicable).

---

## 7. Optional Enhancements

1. **Meta description length:** Run a crawl (e.g. Screaming Frog, Sitebulb) and flag pages with meta description &lt;120 or &gt;160 characters; tweak for clarity and SERP fit.
2. **Image SEO:** Ensure important images have descriptive `alt` text and that Article/og:image URLs resolve and are relevant.
3. **Core Web Vitals / performance:** Use PageSpeed Insights or CrUX; optimize LCP/INP/CLS if needed (e.g. hero images, fonts, layout shifts).
4. **Local / multi-region:** If you target specific regions, consider LocalBusiness or regional landing pages and/or hreflang only if you add non-English or multi-URL versions.
5. **Redirects:** If you ever change URLs (e.g. rename an article slug), add 301 redirects and update internal links and sitemap.

---

## 8. Checklist Summary

| Area | Status |
|------|--------|
| robots.txt + Sitemap | ✅ |
| Canonicals (sampled) | ✅ |
| Meta title & description (sampled) | ✅ |
| H1 usage | ✅ |
| Organization + Article/Breadcrumb/FAQ schema | ✅ |
| Internal linking (hubs + articles) | ✅ |
| Sitemap includes key articles | ✅ (updated) |
| Security headers | ✅ |
| No critical duplicate content observed | ✅ |

---

## 9. Conclusion

The site is in good shape for SEO: technical setup is correct, on-page elements and schema are consistent, and internal linking is strong. The sitemap has been updated to include previously missing article URLs. Remaining work is mostly ongoing hygiene (keeping sitemap and ItemList in sync, auditing meta length and image alt, and monitoring performance). No critical blockers were found.
