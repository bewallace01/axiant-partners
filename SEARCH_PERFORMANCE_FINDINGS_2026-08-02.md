# Why the category pages "underperform" the articles — and what the data actually says

Written after checking a specific claim I had made myself: that the
`/equipment/{category}/` pages were being beaten by `/equipment-financing/articles/`
and the category template was the problem. The gap is real but small, every
structural explanation for it fails, and looking for the cause turned up something
that matters considerably more.


Source: the 2026-08-01 Search Console export, covering **2026-07-03 to 2026-07-30**
(28 days).


## The gap is small, and the category pages win where it counts

| | category `/equipment/` | articles `/equipment-financing/articles/` |
|---|---|---|
| indexable pages | 93 | 98 |
| zero impressions | 20 (22%) | 27 (28%) |
| total impressions | 6,115 | 8,430 |
| total clicks | **39** | 37 |
| median position | 11.0 | **8.4** |
| median words | 1,109 | 1,261 |
| median inbound links | **6** | 5 |
| median schema types | 11 | 12 |
| **CTR** | **0.64%** | 0.44% |

Articles rank about 2.6 positions better on median. Category pages earn more clicks
from fewer impressions, have more inbound links, and have a marginally lower share of
pages that never surface.


### Explanations that do not hold

- **Templating.** Mean pairwise body similarity within each tree, sampled at 18 pages
  each: **0.08** for category pages, **0.05** for articles. Both are low. The category
  pages are not near-duplicates of one another, which is what I had assumed after
  seeing two of them share an H2 skeleton.
- **Depth.** 1,109 median words against 1,261. A 14% difference does not move a page
  three positions.
- **Internal links.** Category pages have more, not fewer.
- **Schema.** Effectively identical coverage.


## What does explain it: query difficulty

| Query length | Queries | Median position | Impressions | Clicks |
|---|---|---|---|---|
| 2–3 words (head) | 281 | 35.7 | 5,401 | **39** |
| 4–6 words (mid) | 410 | 36.5 | 5,901 | 3 |
| 7+ words (long tail) | 309 | **9.2** | 4,592 | **0** |

70% of head terms rank past position 20; only 37% of long-tail do. Articles match
long-tail phrasing and rank accordingly. Category pages target head commercial terms
— "excavator financing" — which are simply harder. The position gap is the queries,
not the pages.


## The finding that matters more than the question

**The long tail ranks well and converts nothing. 4,592 impressions at a median
position of 9.2, and zero clicks.**


The queries explain themselves:


| Position | Impressions | Clicks | Query |
|---|---|---|---|
| 4.1 | 605 | **0** | i have a $10m+ investment portfolio and need liquidity without selling assets |
| 3.5 | 138 | **0** | construction company cash flow between jobs payment timing |
| 8.6 | 168 | **0** | financing vendors for small fleets fewer than 10 trucks |
| 5.4 | 131 | **0** | commercial multifamily loan typical down payment 20% 30% |

These are not people typing into a search box. They are AI Overview fan-out — the
exact pattern `OVERNIGHT_PLAN_2026-08-01.md` warned about: *"impressions alone do not
justify a page."* Ranking fourth for a sentence no human types is worth nothing.


Site-wide, in the query export:


- **254 queries rank in the top 10** → 4,834 impressions → **41 clicks**
- **591 queries rank past position 20** → 7,489 impressions → **0 clicks**
- **992 of 1,000 queries (99%) earn zero clicks**, carrying 15,521 impressions


## The number to sit with

The query export covers 1,000 queries: **15,894 impressions, 42 clicks, CTR 0.26%**.


**37 of those 42 clicks are branded** — *axiant partners*, *axiantpartners.com*,
*axiant*. Five clicks in 28 days came from anything else.


One caveat, stated rather than glossed: `Pages.csv` reports 218 clicks across 672
pages for the same window, so the 1,000-query export does not account for every
click. The branded share above is exact within the query export and should not be
read as the whole site. The direction is not in doubt; the precise ratio is.


## What this means for the excavator consolidation

Ten excavator pages exist. `/equipment/excavators/` earns zero impressions despite
being in the sitemap, indexable, self-canonical, 2,748 words, and carrying **21
inbound internal links — more than the sibling that earns 776**.


It is tempting to read that as cannibalization and merge. Two things argue against
acting on it yet:


1. Body similarity between `/equipment/excavators/` and `/equipment/mini-excavators/`
   is **0.66**, and between the two mini-excavator pages **0.05**. These are not
   duplicate pages competing for one slot; they are distinct pages.
2. "excavator financing" carries 77 impressions at **position 46**. Merging two
   distinct pages does not move a page-5 ranking. That is an authority problem.


The whole excavator cluster produces **0 clicks on 295 impressions**.


## What would actually move the number


1. **Stop treating impressions as progress.** Two thirds of this account's
   impressions come from queries that convert at zero. A page built to serve them is
   a page built for nobody.
2. **Head terms are where the clicks are** — all 39 non-long-tail clicks. They sit at
   a median position of 35.7. Moving "excavator financing" from 46 to the first page
   is worth more than any consolidation in this report.
3. **Pull the per-query page export** before merging anything. It is the one piece of
   data that separates cannibalization from ordinary weakness, and it is a few
   minutes of work in Search Console.
4. **Non-branded search is close to zero.** Whatever the exact ratio, the site earns
   its clicks on its own name. That is the headline, and no amount of FAQ schema,
   breadcrumb markup or page consolidation changes it.

