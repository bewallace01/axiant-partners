# Cannibalization screen — re-run against Search Console

Audit finding #3 reported **1,374 title/H1 pairs at or above 0.45** and warned in the
same breath that the raw count overstates the problem. It does. Re-screened against
current `main` and joined to the 2026-08-01 Search Console export, the number collapses
and two of the named conclusions turn out to be wrong.


## Why the number was inflated

Almost every title on this site contains *financing*, *business*, *loan*, *loans*,
*equipment*, *SBA*, *partners*, *Axiant*. Scoring raw token overlap makes unrelated pages
look like duplicates because they share the vocabulary of the whole site.


This screen drops any token appearing in more than 15% of titles before scoring, leaving
only the words that distinguish one page from another.


| | audit | re-screened |
|---|---|---|
| pairs ≥0.45 | 1,374 | **235** |
| 0.70–1.00 | 132 | **25** |
| 0.55–0.69 | 862 | 65 |
| 0.45–0.54 | 380 | 145 |

768 indexable pages screened. `noindex` pages are excluded — a page Google is told to
ignore cannot compete with anything.


### The same tokenizer bug, twice

The audit reported a 1.00 between the $1M, $2M and $5M loan pages and correctly identified
the cause: tokens under four characters were dropped, so "1", "2" and "5" vanished and all
three reduced to `{million, business}`.


The first version of this screen dropped single characters and reproduced it exactly —
`1-million-business-loan` against `5-million-business-loan` at **1.00**. Fixed, and recorded
here because it is evidently an easy mistake to make twice.


## What survives, split by whether anyone sees the pages

Title similarity alone says nothing about whether two pages actually compete. Every pair at
≥0.70 is below, grouped by what Search Console shows.


### A. Both pages earn impressions — 11

Eight are the site's deliberate structure: the same question asked once per product cluster,
or two genuinely different pieces of equipment. They share a pattern, not an intent.


**Worth a look — 3:**


| Score | Page | Impressions | Position |
|---|---|---|---|
| 0.833 | `equipment-financing-calculator` | 42 | 14.9 |
| 0.833 | `excavator-financing-calculator` | 355 | 5.4 |
| 0.833 | `equipment-financing-calculator` | 42 | 14.9 |
| 0.833 | `heavy-equipment-financing-calculator` | 22 | 7.9 |
| 0.8 | `electric-material-handlers` | 3 | 26.7 |
| 0.8 | `material-handlers` | 3 | 2.0 |
| 0.75 | `landscape-trailers` | 22 | 9.3 |
| 0.75 | `trailers` | 12 | 11.0 |
| 0.714 | `excavator-financing-calculator` | 355 | 5.4 |
| 0.714 | `heavy-equipment-financing-calculator` | 22 | 7.9 |

The three calculators share one title formula — *Equipment / Excavator / Heavy Equipment
Financing Calculator: Monthly Payments*. Note that **no calculator query appears in the GSC
export at all**, so this is a titling overlap, not a demonstrated query fight.


**Deliberate, leave alone — 8:** `what-credit-score-needed` across three clusters,
`contractor` vs `restaurant` debt relief, `diagnostic-devices-medical` vs
`diagnostic-equipment-auto`, `dry-` vs `wet-batch-plants`, and the BLOC vs equipment
"how fast" pair, which earns 1,275 and 630 impressions respectively — both working.


### B. One page earns, the other is silent — 9

**This is the bucket that matters.** A page at zero impressions beside a near-identical page
that ranks is the actual signature of cannibalization, and none of these were called out by
the original screen.


| Score | Earning | Impr | Pos | Silent (0 impressions) |
|---|---|---|---|---|
| 0.75 | `mini-excavators` | 776 | 17.0 | `excavators` |
| 0.75 | `contractor-financing` | 106 | 20.0 | `painting-contractor-working-capital` |
| 0.75 | `used-excavator-financing` | 34 | 6.8 | `used-mini-excavator-financing` |
| 0.75 | `unsecured-business-loan-rates-2026` | 10 | 24.4 | `unsecured-business-loans` |
| 0.75 | `used-box-truck-financing` | 5 | 10.0 | `used-dump-truck-financing` |
| 0.75 | `contractor-debt-relief` | 2 | 4.0 | `landscaping-debt-relief` |
| 0.75 | `contractor-debt-relief` | 2 | 4.0 | `trucking-debt-relief` |
| 0.75 | `restaurant-debt-relief` | 1 | 10.0 | `landscaping-debt-relief` |
| 0.75 | `restaurant-debt-relief` | 1 | 10.0 | `trucking-debt-relief` |

Two stand out:


- **`mini-excavators` earns 776 impressions; `excavators` earns nothing.** The audit flagged
  this pair at 0.86 and asked whether it was a deliberate split. Whatever the intent, only
  one of the two is visible.
- **`unsecured-business-loans.html` is silent while an article about its rates earns.** A
  money page outranked by its own supporting article is worth understanding before anything
  is merged.


### C. Neither page earns — 5

Nothing to split. These are not cannibalization; they are pages with no traction.


## Two conclusions from the original audit that do not hold


### `business-debt-consolidation.html` vs `consolidate.html`

Called "the clearest genuine duplicate" at 0.83. **`consolidate.html` is already `noindex`
and has zero Search Console data.** It cannot cannibalize anything. Already handled, and it
does not appear in this screen because `noindex` pages are excluded.


### The patient-financing trio

The audit read real query volume — `patientfi vs carecredit` at 139 impressions,
`cherry vs carecredit` at 86 — as three pages splitting demand.


They are not splitting it. **All three earn zero impressions.**
`carecredit-vs-patientfi-imaging-radiology` takes **1,952 impressions and all 9 clicks** in
the cluster. The problem is not duplication to merge; it is three pages that never gained
traction beside a sibling holding the entire category.


## What this data cannot prove

`Pages.csv` and `Queries.csv` are separate dimensions. There is no query×page cross-tab in
this export, so **no pair here can be shown to compete for a specific query**. Title
similarity is a proxy and impressions are corroboration; neither is proof.


To settle bucket B, export Search Console → Performance → filter by query → Pages, for the
queries the silent pages target. If both URLs appear for one query it is cannibalization and
one should be consolidated. If only one appears, the other is simply weak and needs content
or links, not a redirect.


## Recommended order


1. Pull the per-query page export for bucket B — nine pairs, a few minutes of work.
2. Decide `excavators` vs `mini-excavators` first; it carries 776 impressions.
3. Understand why `unsecured-business-loans.html` is beaten by its own article before
   touching either.
4. Leave bucket A's eight deliberate pairs alone.
5. Treat bucket C and the patient-financing trio as a content problem, not a consolidation
   one.


No merges or redirects were performed. Choosing a survivor changes which URL earns and
needs the query data above.

