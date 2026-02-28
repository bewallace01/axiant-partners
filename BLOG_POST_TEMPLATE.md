# Blog Post Template (SEO + Internal Linking)

Use this exact template when sending a new post draft. Fill what you can; leave unknown fields as `TBD`.

---

## 1) Post Input Block (fill this first)

```txt
SLUG: 
DATE: YYYY-MM-DD
PRIMARY_TOPIC: (sba | equipment | linecredit | termloan | workingcapital | bridge | cre | fixflip | revenue | securities | general)
POST_TITLE_H1:
POST_TAGLINE:
TARGET_KEYWORD:
SEARCH_INTENT: (informational | comparison | transactional)

META_TITLE_DRAFT: 
META_DESCRIPTION_DRAFT: 

CTA_BUTTON_TEXT:
CTA_BUTTON_URL: ../match.html

BACK_LINK_LABEL: (example: Back to SBA Loans Blog)
BACK_LINK_URL: (example: ../sba-loans-blog.html)

SERVICE_PAGE_URL: (example: ../sba-loans.html)
SERVICE_LINK_LABEL: (example: Explore SBA loan options)

RELATED_BLOG_HUB_URL: (example: ../sba-loans-blog.html)
RELATED_BLOG_HUB_LABEL: (example: Read more in the SBA Loans Blog)

RELATED_ARTICLE_URL: (example: ./how-long-sba-loan-approval.html)
RELATED_ARTICLE_LABEL: (example: Related article: SBA Loan Approval Timeline)
```

---

## 2) Body Structure (use this order)

```txt
H1
Tagline
Lead paragraph (2-4 sentences)

H2 section
Paragraph(s)

H2 section
Paragraph(s)

H2 section
Paragraph(s) + bullets/table if useful

H2 Final Thoughts
Short close + service link mention
```

Keep sections scannable. Use plain language and examples.

---

## 3) SEO Rules (always)

- Title length target: 45-65 chars
- Meta description target: 120-155 chars
- Include target keyword naturally in:
  - H1
  - first paragraph
  - one H2
  - meta title or description
- Use only one H1
- Avoid keyword stuffing

---

## 4) Internal Linking Rules (always)

Include these links on every post:

1. In-body link to primary service page
2. In-body link to one related article
3. In-body link to blog hub
4. Related Resources block before CTA:
   - service page
   - blog hub
   - related article
   - ../match.html

---

## 5) Output Request to Assistant (copy/paste this)

```txt
Use this template to create/update:
1) /blog/<SLUG>.html
2) SEO tags in <head>:
   - <title>
   - meta description
   - og:title, og:description
   - twitter:card, twitter:title, twitter:description
3) Add/update Related Resources block above services CTA
4) Ensure back-link text and byline formatting are clean
5) Keep encoding ASCII-safe (no mojibake)
6) Keep all links relative for local + hosted compatibility
7) Run: powershell -ExecutionPolicy Bypass -File "scripts/auto_blog_seo.ps1" -PostPath "blog/<SLUG>"
```

---

## 6) Quick Example

```txt
SLUG: sba-loan-collateral-requirements.html
DATE: 2026-03-01
PRIMARY_TOPIC: sba
POST_TITLE_H1: SBA Loan Collateral Requirements Explained
POST_TAGLINE: What lenders require and how collateral affects approval
TARGET_KEYWORD: SBA loan collateral requirements
SEARCH_INTENT: informational

META_TITLE_DRAFT: SBA Loan Collateral Requirements | Axiant Partners
META_DESCRIPTION_DRAFT: Learn SBA collateral requirements, when collateral is required, and how lenders evaluate business assets for SBA loan approvals.

CTA_BUTTON_TEXT: Get Matched for SBA Financing
CTA_BUTTON_URL: ../match.html

BACK_LINK_LABEL: Back to SBA Loans Blog
BACK_LINK_URL: ../sba-loans-blog.html

SERVICE_PAGE_URL: ../sba-loans.html
SERVICE_LINK_LABEL: Explore SBA loan options

RELATED_BLOG_HUB_URL: ../sba-loans-blog.html
RELATED_BLOG_HUB_LABEL: Read more in the SBA Loans Blog

RELATED_ARTICLE_URL: ./what-credit-score-needed-sba-loan.html
RELATED_ARTICLE_LABEL: Related article: Credit Score for SBA Loans
```
