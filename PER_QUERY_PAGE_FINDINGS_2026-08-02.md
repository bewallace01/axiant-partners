# Per-query page export — the nine pairs, settled

The cannibalization screen ended by saying no merge should happen until someone
pulled the query×page cross-tab, because title similarity cannot distinguish a
page that splits a query from a page that is simply weak. That data is now in.


**None of the nine pairs is cannibalization. No merges, no redirects.**


Source: Search Console UI, property `https://axiantpartners.com/`, filtered
per query and per page. Window **2026-05-01 to 2026-07-31** (3 months) rather than
the 28 days the CSV exports covered, for enough volume to be worth reading.


## The test

For each pair: take the query the silent page was built for, and look at which
URLs the site actually surfaces. Cannibalization means both URLs appear and split
the query. Weakness means only one appears.


## Pair 1 — `excavators` vs `mini-excavators` (the one that mattered)

Exact query **"excavator financing"** — 94 impressions, 0 clicks, average position **46.1**:


| Page | Impressions |
|---|---|
| `/equipment/mini-excavators/` | **88** |
| `/equipment/excavators/excavator-lease-vs-loan/` | 5 |
| `/equipment-financing/articles/excavator-financing-calculator/` | 4 |
| `/equipment-financing/articles/mini-excavator-financing/` | 4 |
| `/equipment/excavators/` | **0 — does not appear** |

The hub built to own this term is absent. Across **all** excavator queries (412
impressions, 12 pages, 0 clicks) it never appears either. Filtered to the page
itself: **2 impressions in three months**.


This is not two pages splitting a query. Google picked one page as the site's
answer for "excavator financing" and never shows the other. Redirecting the silent
page into the earner would change nothing, because the earner already holds the
query — at position 46.


## Pair 2 — `unsecured-business-loans.html`

The screen flagged a money page apparently beaten by its own supporting article.
Filtered to the page: **0 impressions, 0 clicks, no query data at all** in three
months. It is not being beaten. It is not in the auction.


Unsecured queries site-wide earn 731 impressions at position 8.6 and **0 clicks**,
and every one of them goes to business-line-of-credit articles.


## Pair 3 — `used-mini-excavator-financing`

Exact query **"used mini excavator financing"** — 55 impressions:


| Page | Impressions |
|---|---|
| `/equipment/mini-excavators/` | **50** |
| `/equipment-financing/articles/mini-excavator-financing/` | 4 |
| `/equipment-financing/articles/excavator-financing-calculator/` | 1 |
| `/equipment/mini-excavators/used-mini-excavator-financing/` | **0** |

The exact-match URL does not appear for its own exact-match query. The hub takes it.


## Pair 4 — `painting-contractor-working-capital`

**0 impressions in three months.** Same verdict.


## Pairs 5–9

The earning side carries 1–5 impressions over 28 days — box trucks vs dump trucks,
and four debt-relief pairs. There is no signal to interpret at that volume and no
action worth taking on it.


## The pattern, which matters more than the nine verdicts

Every pair behaves the same way: **Google selects one page per topic cluster and
never surfaces the siblings.** The silent pages are not losing a split. They are
not entering the auction at all.


That inverts the remedy. Consolidation helps when two pages divide one query's
authority. Here the authority is already concentrated on one URL per cluster — and
that URL ranks 46th. Merging pages into it would move nothing.


## A correction I owe on the headline number

Every report since the search-performance analysis has repeated **"42 clicks in 28
days, 37 of them branded"** — about five non-branded clicks a month. That was drawn
from `Queries.csv`, and it is wrong.


The export is **capped at 1,000 rows**. It captured the branded head and truncated
a long non-branded tail. Queried directly, over 2026-05-01 to 2026-07-31:


| | Clicks | Impressions | CTR |
|---|---|---|---|
| **Total** | **424** | 109,000 | 0.4% |
| Branded (contains "axiant") | 79 | 779 | 10.1% |
| **Non-branded** | **345** | ~108,000 | 0.3% |

**Branded is 19% of clicks, not 88%.** Non-branded search earns roughly 115 clicks
a month, not five. The site is not invisible to people who have never heard of it;
it converts them badly.


The caveat stated in the original analysis — that `Pages.csv` reported 218 clicks
where `Queries.csv` reported 42, so the query export did not account for every
click — was the visible edge of this. It should have been chased then rather than
footnoted.


## What the numbers actually say to do


1. **Do not merge or redirect anything.** Nine pairs examined, zero are
   cannibalization. Every silent page is silent because it never appears, not
   because a sibling outranks it.
2. **CTR is the constraint, not impressions.** 109,000 impressions at position 16.6
   produce 424 clicks. `how-much-down-payment-required-commercial-property-loan`
   alone takes **10,951 impressions for 11 clicks** — 0.1%. That is a title and
   snippet problem on a page already ranking, which is far cheaper to fix than
   moving a page-5 ranking.
3. **The head terms are still where the ceiling is.** "excavator financing" sits at
   position 46 with one page holding it. That is an authority problem and no amount
   of on-page work inside the cluster changes it.
4. **Stop quoting the 42/37 figure**, including in
   `SEARCH_PERFORMANCE_FINDINGS_2026-08-02.md`, which is corrected in place.

