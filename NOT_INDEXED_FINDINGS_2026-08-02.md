# The 233 not-indexed pages

Pulled after noticing the count on the Search Console overview. It resolves into
three very different things, and only one of them is a problem.


Source: Search Console coverage drilldown export, 2026-08-02.


## The breakdown

| Reason | Pages | Verdict |
|---|---|---|
| Page with redirect | 51 | intentional |
| Alternate page with proper canonical | 26 | intentional |
| Excluded by `noindex` | 12 | intentional |
| **Crawled &mdash; currently not indexed** | **115** | the real one |
| Discovered &mdash; currently not indexed | 21 | not yet fetched |
| Not found (404) | 7 | stale URLs, not in sitemap |
| Duplicate, Google chose different canonical | 1 | &mdash; |

**89 of the 233 are supposed to be there.** Redirects, canonicals and `noindex`
pages are excluded by design.


## 24 of the 115 are ghosts

They are URLs Google still remembers for pages that no longer exist in the repo
and are not in the sitemap &mdash; including an entire `digital-marketing/articles/`
section that has been deleted. Crawled between March and July, now gone.


Nothing to fix; they will age out.


## 4 more are canonicalised duplicates, working correctly

> **CORRECTED 2026-08-03.** This section was missing from the original, and its
> absence made the four most-linked entries look like the worst failures. They
> are not failures at all.

The export lists `/services`, `/blog`, `/vendors` and `/terms-and-conditions`
&mdash; **extensionless**, not the `.html` URLs. Both forms return 200, and the
extensionless one carries a canonical pointing at the `.html` version:


| URL | Status | Canonical |
|---|---|---|
| `/services` | 200 | &rarr; `/services.html` |
| `/services.html` | 200 | self &mdash; **indexed** |


Google crawled the duplicate, read the canonical, and declined to index it
separately. That is exactly the intended outcome. URL inspection confirms
`services.html` and `blog.html` are both **on Google and indexed**.

These four carry the highest inbound-link counts on the site, which is why they
sorted to the top of the priority ranking and were read as "the most-linked
pages, rejected". They should never have been in the queue.

**The real count of live pages Google rejected is 86.**


## The 86 are not thin, orphaned or duplicative

The obvious hypotheses all fail. Against the other 682 indexable pages:


| Measure | Rejected (86) | Everything else (682) |
|---|---|---|
| Median words | **1,586** | 1,304 |
| Median inbound internal links | **7** | 5 |
| Nearest-sibling content overlap | 32.6% | 33.6% |
| Pages with zero inbound links | **0** | &mdash; |

The rejected pages are **longer and better linked** than the pages Google kept,
and no more similar to their siblings. They are spread across every section at
12&ndash;33%, with no bad neighbourhood.


## What actually predicts rejection: publication date

| Published | Rejected | Indexed | Rejected share |
|---|---|---|---|
| 2026-02 and earlier | 7 | 19 | ~27% |
| **2026-03** | **65** | 197 | **25%** |
| 2026-04 | 4 | 49 | 8% |
| 2026-05 | 1 | 86 | **1%** |
| 2026-06 | 4 | 222 | **2%** |
| 2026-07 | 6 | 59 | 9% |

**75% of the rejected pages are a single March 2026 cohort.** Everything published
since May indexes at 98&ndash;99%. The Search Console issue is dated *first detected
3/7/26*, which matches.


So this is not a verdict on the site's current content. It is a verdict passed on
one batch, months ago, that has never been revisited.


## Why it was never revisited

| | |
|---|---|
| Live rejected pages | 86 |
| Present in `sitemap.xml` | 86 |
| Carrying `lastmod` of **2026-04** | **82** |
| Actually modified in the repo since 2026-07-25 | **86** |

Every one of them was rewritten in the last week &mdash; FAQ schema, titles,
headlines, breadcrumbs, answer parity &mdash; while the sitemap told Google they
last changed in April.


Site-wide it was worse: **400 of 764 entries read 2026-04** against 843 HTML files
changed since 25 July. `lastmod` is the main signal Google uses to decide whether a
known URL is worth re-fetching. The sitemap was asking it not to look.


Corroborated directly: URL inspection on `security-guard-company-working-capital`
reports **last crawled 12 June 2026** &mdash; 51 days before this was written.


## A landmine found on the way

`scripts/generate_sitemap.py` does not discover pages. It enumerates a
hand-maintained list that has drifted **188 URLs** behind the site. Running it today
emits 576 URLs against the committed 764, silently deleting all of
`business-debt-relief`, all of `equipment-for-sale`, every `$N-business-loan` page
and more.


It now refuses to write a smaller sitemap than the one on disk unless passed
`--allow-shrink`. The stale page list is left as-is &mdash; fixing it properly means
deciding inclusion rules, which is a separate job.


## What changed

- `lastmod` refreshed from **git history** rather than mtime, so a fresh clone does
  not date the whole site to the checkout. 759 of 764 entries updated.
- URL set asserted byte-identical; the diff is lastmod values and nothing else.
- `generate_sitemap.py` guarded against silent truncation.


**Caveat, stated plainly:** 758 of the 764 now read 2026-08 because this week's
work genuinely touched almost every page. A uniform date is a weaker signal than a
varied one, and Google may discount it. It is still strictly better than 400 pages
claiming April when they were rewritten in August &mdash; that was simply false.


## What to watch

The next crawl is the test. If the March cohort gets re-fetched and a meaningful
share of the 86 moves into the index, the diagnosis was right and the remedy was
recrawl rather than rewrite. If they are re-crawled and still rejected, then it *is*
a content judgement &mdash; and that is worth knowing, because it would mean 86
pages of 1,586 median words are not earning their place.

