# Article Template (SEO + AEO + GEO)

Canonical structure for every new article on axiantpartners.com. Built around the **Helpful Content Update** (March 2024) — answer-first, dense, no padding.

---

## Core principles

1. **Answer the question in the first 100 words.** The Quick Answer card is the AI-citation hook (Google AI Overviews, Perplexity, ChatGPT search) and the human-CTR hook in one block.
2. **Target 1000-1500 words.** Sweet spot for SEO. Below 800 = thin. Above 2000 = padding risk.
3. **No cross-article duplicate paragraphs.** Site-wide content fingerprinting will catch and remove templated bloat. Write something unique to this article.
4. **One topic per article.** If you find yourself writing two H2s that could each be their own article, split it.
5. **No filler phrases.** "In today's competitive business landscape," "It's important to note," "playing a crucial role" — all banned. They signal SEO-stuffing to the Helpful Content algorithm.

---

## File path

```
/<cluster>/articles/<slug>/index.html
```

Examples: `/equipment-financing/articles/equipment-financing-bad-credit/index.html`, `/working-capital-loans/articles/what-is-working-capital-loan-how-does-it-work/index.html`.

Top-level `/articles/<slug>/index.html` for cross-cluster general posts.

---

## Required schema blocks (in `<head>`, in this order)

### 1. BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://axiantpartners.com/" },
    { "@type": "ListItem", "position": 2, "name": "Equipment Financing", "item": "https://axiantpartners.com/equipment-financing.html" },
    { "@type": "ListItem", "position": 3, "name": "Articles", "item": "https://axiantpartners.com/equipment-financing/articles/" },
    { "@type": "ListItem", "position": 4, "name": "<Article Title>", "item": "<canonical URL>" }
  ]
}
```

### 2. Article

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "<Article Title>",
  "description": "<155-char meta description>",
  "image": { "@type": "ImageObject", "url": "<hero image URL>", "width": 1200, "height": 630 },
  "url": "<canonical URL>",
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "author": { "@type": "Organization", "name": "Axiant Partners", "url": "https://axiantpartners.com" },
  "publisher": { "@id": "https://axiantpartners.com/#organization" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "<canonical URL>" },
  "articleSection": "<Cluster name>",
  "keywords": "<3-5 comma-separated keywords>"
}
```

### 3. FAQPage (if article has FAQs)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "<Q>", "acceptedAnswer": { "@type": "Answer", "text": "<A, 1-3 sentences>" } }
  ]
}
```

### 4. WebPage with Speakable (REQUIRED for AEO)

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": "<canonical URL>#webpage",
  "url": "<canonical URL>",
  "name": "<Article Title>",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".quick-answer"]
  }
}
```

This is the **AI-citation hook**. The `.quick-answer` selector points AI search engines at the Quick Answer block as the canonical citation source for this article.

### 5. HowTo (if article has procedural steps — optional but recommended)

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to <do thing>",
  "description": "<1 sentence>",
  "totalTime": "PT2H",
  "step": [
    { "@type": "HowToStep", "position": 1, "name": "<Step name>", "text": "<2-3 sentences>" }
  ]
}
```

5 steps is the sweet spot. Each step `text` is 2-3 sentences. Don't add HowTo if the article isn't actually procedural.

---

## Required body structure

```html
<main class="blog-post-main">

  <!-- 1. Quick Answer card — REQUIRED. AI-citation hook + above-the-fold CTR. -->
  <div class="quick-answer" style="background:var(--bg-card);border-left:4px solid var(--accent-color);padding:16px 18px;margin:0 0 28px;border-radius:10px;">
    <strong style="display:block;font-size:0.75rem;letter-spacing:0.08em;text-transform:uppercase;color:var(--accent-color);margin-bottom:6px;">Quick answer</strong>
    <p style="margin:0;font-size:1rem;line-height:1.55;color:var(--text-primary);">
      <!-- 50-100 words. Answer the headline question directly. Include 2-3 specific numbers (rates, percentages, time ranges). Bold the most important phrases with <strong>. -->
    </p>
    <p style="margin:12px 0 0;font-size:0.92rem;color:var(--text-secondary);">
      <a href="/match.html" style="color:var(--accent-color);font-weight:600;">Get matched with the right lender for your business &rarr;</a>
    </p>
  </div>

  <!-- 2. First H2 — answers the headline question more deeply. -->
  <h2 id="first-h2">...</h2>
  <p>Lead paragraph (2-3 sentences) that expands the Quick Answer.</p>

  <!-- 3. Subsequent H2s — each addresses a related sub-question. -->
  <h2 id="second-h2">...</h2>

  <!-- 4. Optional table, list, callout, stat-row (use the new aesthetic CSS components). -->

  <!-- 5. Final H2 — summary or "what to do next." -->

</main>
```

The `.quick-answer` selector is the Speakable target. Don't change the class name.

---

## SEO rules

- **Title (`<title>`):** 45-65 chars including " | Axiant Partners" suffix
- **Meta description:** 120-160 chars. Lead with the answer.
- **og:title and twitter:title:** can be slightly different from `<title>` (more punchy, no brand suffix)
- **og:description and twitter:description:** can be the meta description verbatim
- **Canonical URL:** absolute, with trailing slash, matches the file path
- **One H1 only** (in `<header>`, not in `<main>`)
- **Target keyword** appears in: H1, first paragraph (after Quick Answer), one H2, and meta title/description
- **No keyword stuffing** — natural usage only

---

## AEO rules (AI-citation optimization)

- **Quick Answer must be 50-100 words** — too long = AI engines won't extract it; too short = won't satisfy the query
- **Lead with a direct yes/no/specific-answer.** "Yes — X is possible when..." or "Most lenders require..."
- **Include numbers** (rates, ranges, time periods) — these are what AI engines pull as citations
- **Bold key facts** with `<strong>` — this signals salience to extraction algorithms
- **End with a contextual CTA** — "Get matched for X" linking to /match.html, or for calculator topics, link to /equipment-financing-calculator.html

---

## GEO rules (geographic SEO)

For pages targeting US business owners (default):
- Use US-specific terminology ("FICO score" not "credit rating", "EIN" not "company number")
- Reference US lender categories (banks, asset-based lenders, marketplaces, brokers)
- Include US-specific compliance signals where relevant (UCC filings, state-by-state variations)
- For state-specific pSEO pages: include real state data (Secretary of State filing offices, state-specific rate ranges, state economic context)

---

## Internal linking (every article)

Add 3-5 internal links inline in body text (not in a "Related Resources" block — those signal less E-E-A-T to Google than contextual links):

1. **One link to the cluster service page** (`/equipment-financing.html`, `/sba-loans.html`, etc.)
2. **One link to a related article in the same cluster**
3. **One link to a related article in a DIFFERENT cluster** (cross-cluster authority signal)
4. **(optional) One link to the cluster's articles hub** (`/equipment-financing/articles/`)
5. **(optional) One link to /match.html or /equipment-financing-calculator.html** as a contextual conversion

Link anchor text should be the article's actual title or a natural phrase — never "click here" or "learn more."

---

## What NOT to do

- ❌ Copy-paste paragraphs across articles (cross-article duplicate fingerprints will be detected and removed)
- ❌ Write 2500+ words for a topic that only needs 1200
- ❌ Use generic AI filler ("In today's", "It's important to note", "navigating the complexities of")
- ❌ End with "In conclusion..." or "As we've seen..."
- ❌ Stuff keywords — natural usage is enough
- ❌ Use `<title>` content in `og:title` and `twitter:title` if it has pipe `|` characters in regex-replacement scripts (escape them or use string replace)

---

## Quick example (complete article skeleton)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Equipment Financing for Restaurants | Axiant Partners</title>
  <meta name="description" content="Restaurant equipment financing approves at 600-650 FICO with 6 months operating history. Rates 8-15%, 0-20% down. How to qualify and what to bring.">
  <link rel="canonical" href="https://axiantpartners.com/equipment-financing/articles/equipment-financing-restaurants/">

  <!-- og: + twitter: tags -->

  <!-- Schema blocks: BreadcrumbList, Article, FAQPage, WebPage(Speakable), HowTo -->
</head>
<body>
  <header><h1>Equipment Financing for Restaurants</h1></header>
  <main class="blog-post-main">
    <div class="quick-answer">
      <strong>Quick answer</strong>
      <p>Restaurant equipment financing approves at <strong>600-650 FICO</strong> with 6+ months of operating history. Rates run <strong>8-15% APR</strong>, with <strong>0-20% down</strong> depending on credit and equipment type. Most lenders fund 100% of equipment cost on used; specialty restaurant lenders include installation and soft costs in the financed amount.</p>
      <p><a href="/match.html">Get matched for restaurant equipment financing &rarr;</a></p>
    </div>
    <h2>What credit score do restaurants need?</h2>
    <p>...</p>
    <h2>How much down payment is required?</h2>
    <p>...</p>
    <h2>What documents do lenders need?</h2>
    <p>...</p>
    <h2>How fast does it close?</h2>
    <p>...</p>
  </main>
</body>
</html>
```
