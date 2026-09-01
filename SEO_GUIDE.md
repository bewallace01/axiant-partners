# SEO Guide – Axiant Partners

This guide summarizes the SEO work done on the site and what you should do next. The site is **live on Netlify** and pulls from **GitHub**; all URLs use `https://axiantpartners.com`. If your Netlify domain differs, do a find-and-replace (see below).

## What’s in place

### 1. Meta tags (all HTML pages)
- **Meta description** – Unique, ~150–160 character description per page for search snippets.
- **Canonical URL** – `rel="canonical"` on every page to avoid duplicate content.
- **Open Graph** – `og:title`, `og:description`, `og:type`, `og:url`, `og:image`, `og:site_name`, `og:locale` for social sharing (Facebook, LinkedIn, etc.).
- **Twitter Card** – `twitter:card`, `twitter:title`, `twitter:description` for Twitter previews.

### 2. Structured data (JSON-LD)
- **index.html** – `Organization` and `WebSite` schema so Google can show your brand and site in search.
- **faq.html** – `FAQPage` schema so FAQs can appear as rich results (expandable Q&A in search).
- **blog.html** – `Blog` schema; each blog post has `Article` schema for rich results.

### 3. Sitemap and robots
- **sitemap.xml** – All 10 pages with `lastmod`, `changefreq`, and `priority` for crawlers.
- **robots.txt** – Allows all crawlers and points to the sitemap.

### 4. Netlify
- **_headers** – Security headers (X-Frame-Options, X-Content-Type-Options, Referrer-Policy) and cache rules for CSS, JS, images, sitemap, and robots.txt so the site is fast and secure.

### 5. Titles and structure
- Each page has a unique `<title>`; meta descriptions and OG titles are aligned. Headings use a clear hierarchy (one `h1` per page). Key images have `alt` text.

---

## What you need to do

### 1. Confirm your live domain
All canonical URLs, OG URLs, and the sitemap use:

- **Base URL:** `https://axiantpartners.com`

If your Netlify site uses a different URL (e.g. `https://axiantpartners.netlify.app` or a custom domain):

1. **Find and replace** in the whole project: `https://axiantpartners.com` → your real base URL (with `https://`, no trailing slash).
2. Update **sitemap.xml** (every `<loc>`) and **robots.txt** (`Sitemap:` line).

### 2. Submit to search engines
- **Google:** [Google Search Console](https://search.google.com/search-console) – add your property (your live URL), then submit **Sitemap** = `https://axiantpartners.com/sitemap.xml` (or your domain + `/sitemap.xml`).
- **Bing:** [Bing Webmaster Tools](https://www.bing.com/webmasters) – add site and submit the same sitemap URL.

### 3. Social image (optional)
- OG/Twitter use `logo.jpg`. For best results, use an image at least **1200×630 px**. If you add a dedicated `og-image.jpg`, update `og:image` (and optionally `twitter:image`) on the main pages.

### 4. Optional next steps
- **sameAs** – If you have social profiles (LinkedIn, Twitter, etc.), add their URLs to the `sameAs` array in the Organization JSON-LD on `index.html`.
- **Page speed** – Use [PageSpeed Insights](https://pagespeed.web.dev/) and optimize images (e.g. WebP, sizing) if needed.
- **New pages** – When you add pages, add meta description + canonical + OG/Twitter to the `<head>`, and add the URL to `sitemap.xml`.
- **More blog posts** – Add new posts in `blog/` with unique titles, meta, and Article schema; link them from `blog.html` and add URLs to `sitemap.xml`.

---

## File reference

| File / area           | Purpose |
|-----------------------|--------|
| All `.html` `<head>`  | Meta description, canonical, OG, Twitter |
| `index.html`          | Organization + WebSite JSON-LD |
| `faq.html`            | FAQPage JSON-LD |
| `blog.html`           | Blog index + Blog schema |
| `blog/*.html`         | Article schema, internal links to match/services/calculator |
| `glossary.html`       | DefinedTermSet schema, definition list for featured snippets |
| `sba-loans.html`, `equipment-financing.html`, `working-capital-loans.html` | Loan-type landing pages (keywords + internal links) |
| `sitemap.xml`         | All URLs including blog, loan pages |
| `robots.txt`          | Crawl rules + sitemap URL |
| `_headers`            | Netlify headers (security + caching) |
| This guide            | `SEO_GUIDE.md` |

If you change the domain or add new pages, update the HTML meta, `sitemap.xml`, and (if needed) `robots.txt` so everything stays consistent.
