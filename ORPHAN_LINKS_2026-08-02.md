# Orphan pages — what the finding actually was

The audit reported **130 sitemap pages with fewer than two inbound internal links,
51 of them with zero**, and called it the cheapest win available. Rebuilt from the
current site, that is not what the link graph shows.


## The number did not reproduce

| Counting rule | zero inbound | exactly one | under two |
|---|---|---|---|
| Any body link, relative and absolute (correct) | 1 | 13 | 14 |
| Only links inside `<main class="blog-post-main">` | 84 | 64 | 148 |
| Ignoring relative `../` links | 2 | 56 | 58 |

Nav, header and footer are excluded throughout - they appear on every page, so
counting them would mean no page is ever an orphan. That matches
`scripts/audit_internal_links.py`.


The audit's figure sits between the two narrow rules and cannot be reproduced by
the correct one. This site cross-links heavily with relative `../` hrefs and with
Related Resources blocks that sit outside `blog-post-main`; a rule that misses
either produces a large phantom orphan list.


## What was actually weak, and what changed

| Page | inbound before | after |
|---|---|---|
| `aircraft-financing.html` | 1 | 3 |
| `business-acquisition-financing.html` | 1 | 3 |
| `business-loans-atlanta.html` | 1 | 1 |
| `commercial-marine-financing.html` | 1 | 2 |
| `data-center-financing.html` | 1 | 2 |
| `down-payment-assistance.html` | 1 | 2 |
| `drone-financing.html` | 1 | 1 |
| `equipment-for-sale/electric-material-handlers/index.html` | 1 | 2 |
| `equipment-for-sale/index.html` | 1 | 2 |
| `faq.html` | 1 | 2 |
| `medical-equipment-financing.html` | 1 | 3 |
| `referral.html` | 0 | 1 |
| `small-business-financing-report/index.html` | 1 | 1 |
| `vendors.html` | 1 | 1 |

12 contextual links were added across 12 source pages. Zero-inbound pages: **1 to 0**.
Under two inbound: **14 to 5**.

Every anchor was chosen by reading the sentence it lands in. One candidate was
rejected on that basis: `equipment/wheel-loaders/` lists "general contractors,
quarry operators, site development companies, and material handlers" - operator
businesses, not the machine, so the anchor would not have described the page.


## Still under two inbound — 5

Not forced. An invented link is worse than a thin one.


**`business-loans-atlanta.html`** — 1 inbound

- Only its own state page mentions Atlanta. A second link would have to be invented rather than found.

**`drone-financing.html`** — 1 inbound

- No page on the site mentions drones except equipment-financing.html, which already links it.

**`referral.html`** — 1 inbound

- Now linked from contact.html. A second link really wants a nav entry, which is a site-wide template decision.

**`small-business-financing-report/index.html`** — 1 inbound

- No page mentions the report by name outside the one that already links it.

**`vendors.html`** — 1 inbound

- A portal login page with 97 characters of body text. Inbound links will not help it; it needs content or noindex.

## Zero-inbound pages that are not in the sitemap — 36

The audit described orphans as pages Google is invited to crawl. These are the
opposite: no inbound links and no sitemap entry. Nearly all are intentional -
`noindex` redirect stubs of 9-15 words, calculator embeds, and internal docs.
Two are worth knowing about:


- `articles/business-loan-denied-what-to-do/` — 1,464 words and indexable, but its
  canonical points at `articles/what-to-do-if-business-loan-denied/`, so it is a
  deliberate duplicate rather than an orphan.
- `index.html` — the homepage. Reached through nav on every page; it shows here
  only because nav links are excluded from the graph.

