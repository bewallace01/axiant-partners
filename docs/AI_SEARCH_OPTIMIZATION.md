# AI Search Optimization Summary

The site has been optimized for AI search engines and assistants (ChatGPT, Perplexity, Google AI Overviews, etc.) using the same rigor applied to traditional SEO.

## Canonical host and URLs

- **Preferred origin:** `https://axiantpartners.com` (non-www) for `rel="canonical"`, `og:url`, JSON-LD URLs, and `sitemap.xml` `<loc>` values.
- **Organization `@id`:** `https://axiantpartners.com/#organization`. Pages that reference this id in `publisher` or `provider` get a matching `Organization` JSON-LD node injected at runtime when `language-switcher.js` runs (deduplicated if a full Organization block is already present).

## Article JSON-LD conventions (for new/edited pages)

Use a single Article script block where possible:

| Field | Convention |
|--------|-------------|
| **image** | Prefer `ImageObject` with `url`, `width` 1200, `height` 630 (or hero dimensions). Plain string URL is acceptable for legacy pages. |
| **author** | `{ "@type": "Organization", "name": "Axiant Partners LLC", "url": "https://axiantpartners.com/" }` |
| **publisher** | `{ "@id": "https://axiantpartners.com/#organization" }` (Organization node supplied sitewide as above). |
| **datePublished** | ISO date `YYYY-MM-DD` when the article first shipped. |
| **dateModified** | ISO date; set on substantive updates. If never updated, match `datePublished` or omit only when mirroring an existing legacy pattern. |

## Changes Implemented

### 1. robots.txt – AI crawler access
Explicit `Allow` rules added for major AI crawlers:
- **GPTBot** (OpenAI/ChatGPT)
- **ChatGPT-User** (ChatGPT browsing)
- **CCBot** (Common Crawl – used by many AI systems)
- **PerplexityBot** (Perplexity AI)
- **anthropic-ai** (Anthropic/Claude)
- **Cohere-AI** (Cohere)

This signals that content is intended for AI indexing and citation.

### 2. Meta tags – AI extraction
- **index.html, match.html, faq.html, contact.html**: Added `robots` meta with `max-snippet:-1, max-image-preview:large` to allow full snippet and image use in AI answers.
- **232 pages** updated via `scripts/optimize_ai_search.py`: Added the same robots meta to all pages with a description meta.

### 3. Organization & WebSite schema (index.html)
- **WebSite.mainEntity**: Linked to Organization.
- Existing Organization schema (ContactPoint, logo, description) kept intact.

### 4. Article schema
Across article pages:
- **image**: Uses `og:image` when present so AI systems can surface images.
- **mainEntityOfPage**: WebPage reference to the canonical URL for clearer page identification.

### 5. Script: `scripts/optimize_ai_search.py`
Python script that:
- Adds robots meta (`max-snippet`, `max-image-preview`) where missing
- Ensures Article schema includes `image` when `og:image` exists
- Adds `mainEntityOfPage` to Article schema when missing

Re-run anytime:
```bash
python scripts/optimize_ai_search.py
```

## Optional Enhancements

| Enhancement | Where | Notes |
|-------------|-------|-------|
| **Organization.sameAs** | index.html | Add LinkedIn, Twitter/X URLs when available. Replace `"sameAs": []` with real URLs. |
| **Organization.address** | index.html | Add `PostalAddress` if you want a physical address in schema. |
| **FAQPage on more articles** | Article pages | Equipment guides already have FAQPage + HowTo. Topic articles (SBA, working capital, etc.) can get FAQPage where FAQ sections exist. |

## Existing AI-Friendly Features

- **FAQPage schema** – Homepage, faq.html, many service and equipment pages
- **HowTo schema** – Equipment financing guides (e.g., “How to Finance a Forklift”)
- **BreadcrumbList** – Site-wide
- **FinancialService schema** – Service and industry pages
- **Clear meta descriptions** – All main pages and articles

## AI Search Best Practices

1. **Structured data** – Schema helps AI understand content structure.
2. **Clear, direct answers** – FAQs and HowTo content align with how AI summarizes.
3. **Canonical URLs** – Reduce duplicate or conflicting signals.
4. **Semantic HTML** – Proper H1/H2 hierarchy supports understanding.
