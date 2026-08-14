# Keyword research — overhaul/engine financing and RPO financing

Requested: are there pages worth building for (a) overhaul / engine replacement
financing and (b) rental purchase option (RPO) financing, and what terms should
they target.

**Both gaps are real and both are worth building — but not for the reason or in
the order the first pass of this document claimed.** Volume, difficulty and CPC
now come from DataForSEO. Two conclusions from the pre-volume draft were wrong
and are corrected below.

Reproduce with:

```
node scripts/kw-volume-overhaul-rpo.mjs      # Google Ads volume + CPC + competition
node scripts/kw-difficulty-overhaul-rpo.mjs  # Labs expansions + keyword difficulty
```

Both read `DATAFORSEO_LOGIN`/`DATAFORSEO_PASSWORD` the same way
`Axiant-Partners-CRM/scripts/kw_volume.mjs` does. Total API cost for this
research: **$0.17**.


## Sources

| Source | What it gave |
|---|---|
| DataForSEO Google Ads `search_volume/live` | Volume, CPC, competition — 93 keywords |
| DataForSEO Labs `keyword_suggestions/live` | Phrase expansions + keyword difficulty — 5 seeds |
| Search Console, `https://axiantpartners.com/`, 2026-05-12 → 2026-08-11, live `query=*contains` filters | Existing footprint (proved the gap) |
| `commercialvehicleguide.com` GSC export, 3 months to 2026-05-16 | Audience confirmation |
| Live SERPs | Intent disambiguation on the three ambiguous head terms |


## The number that decides this: difficulty is ~0

`AUDIT_PART5_DEMAND_2026-08-03.md` concluded that every commercial query on this
site sits at position 10+ and that this is a link-authority constraint no on-page
work can reach. That is the reason to care about KD here, and KD is **0 across
almost the entire space**:

| Keyword | Vol/mo | KD | CPC |
|---|---|---|---|
| truck repair financing | 70 | **0** | $26.04 |
| semi truck repair financing | 70 | **0** | $14.53 |
| commercial truck repair financing | 10 | **0** | $29.24 |
| truck repair financing no credit check | 30 | **0** | $10.89 |
| engine overhaul financing | 30 | **0** | **$34.24** |
| rental purchase option | 50 | **0** | $1.05 |
| rent to own heavy equipment | 50 | **0** | $15.38 |
| lease to own heavy equipment | 50 | **0** | $15.38 |
| rent to own restaurant equipment | 110 | **0** | $19.21 |
| equipment lease to own | 30 | **0** | **$52.87** |

Compare the terms this site already fights for: `business line of credit` 14,800
at $233 CPC, `equipment financing` 4,400 at $59. Those are the fights it loses at
position 16.8.

**This is a low-volume, zero-difficulty, high-CPC pocket.** That combination is
the argument for building. It is not a traffic play and should not be sold as
one.


## Correction 1 — I was wrong that "RPO" has no demand

The pre-volume draft said the literal term was "close to dead as a query" and
told you not to name a page after it. That was inferred from Google autocomplete
returning zero suggestions for `rpo financing` variants. **Autocomplete
suppression is not zero volume, and I over-read it.**

| Keyword | Vol/mo | KD | CPC |
|---|---|---|---|
| rpo financing | **260** | – | – |
| rental purchase option | 50 | 0 | $1.05 |
| rpo equipment | 40 | – | $22.32 |
| rental purchase option equipment | 20 | – | – |
| rental agreement with option to purchase | 140 | 9 | $4.29 |
| rental with option to purchase agreement | 140 | 8 | $4.29 |
| rpo rental purchase option | 20 | 40 | – |

`rpo financing` at 260/mo is **higher than every single term in the overhaul
cluster**, including the head term I had ranked Priority 1.

One caveat that survives: the SERP for `rpo financing` is split between Rental
Purchase Option (RDO Equipment ranks #1, ALL Crane, Commercial Credit Group) and
Remaining Performance Obligation, the SaaS accounting metric (Motley Fool,
Hubifi). So some of that 260 is not your buyer. But the equipment meaning holds
the #1 result, so Google reads the term as leaning your way.

**Revised guidance:** use RPO in the title, not just the body. Something that
carries both vocabularies — the RPO term has the volume, the rent-to-own terms
have the breadth.

The parts of the original claim that *did* hold: `rental purchase option
financing`, `rpo buyout financing`, `rental conversion financing` and `convert
rental to purchase equipment` all return **no data** on volume as well as no
autocomplete. Those specific phrasings really are empty. Don't build for them.


## Correction 2 — the consumer branch is 10× the commercial one

The pre-volume draft told you to stay off the consumer repair branch as "wrong
ICP." That advice stands for a B2B broker, but you should see what you are
walking away from:

| Keyword | Vol/mo | KD | CPC |
|---|---|---|---|
| **auto repair financing** | **4,400** | – | $10.39 |
| financing for transmission repair | 390 | – | $7.96 |
| engine replacement financing | 140 | – | $8.09 |
| engine repair financing | 40 | – | $7.63 |
| transmission replacement financing | 20 | – | $8.32 |

`auto repair financing` alone is **more than ten times the entire commercial
truck repair cluster**. Note that `engine replacement financing` — the exact
phrase you asked about — sits here at 140/mo, not in the commercial cluster.

This is consumer-lender territory (Acorn Finance, credit-repair blogs) and
fulfilling it means point-of-sale patient-style financing, not commercial
lending. Skipping it is defensible. Skipping it *without knowing it is 4,400/mo*
is not, which is why it is in the table.


## Cluster 1 — overhaul / engine, commercial truck

Real but small. The whole commercial cluster is roughly **350/mo** summed across
overlapping variants.

| Keyword | Vol/mo | KD | CPC | Comp |
|---|---|---|---|---|
| truck repair financing | 70 | 0 | $26.04 | MEDIUM |
| semi truck repair financing | 70 | 0 | $14.53 | MEDIUM |
| semi truck repair loan | 50 | – | $18.48 | HIGH |
| engine rebuild financing | 40 | – | $6.55 | HIGH |
| engine overhaul financing | 30 | 0 | **$34.24** | HIGH |
| truck repair financing no credit check | 30 | 0 | $10.89 | – |
| semi truck engine overhaul financing | 20 | – | – | LOW |
| semi truck repair financing no credit check | 20 | – | $9.53 | HIGH |
| commercial truck repair financing | 10 | 0 | **$29.24** | HIGH |
| commercial truck repair loan | 10 | – | $29.86 | HIGH |
| truck engine overhaul financing | 10 | 40 | – | LOW |
| diesel engine overhaul financing | 10 | – | $21.20 | – |
| engine overhaul financing truckers | 10 | 23 | – | – |

`truck repair financing` is the head, not `truck engine overhaul financing`
(10/mo, KD 40 — the hardest term in the cluster and nearly the smallest). The
first draft had that backwards.

**The cost layer is bigger than the financing layer**, which confirms the buyer
researches price before money:

| Keyword | Vol/mo | KD | CPC |
|---|---|---|---|
| semi truck engine overhaul cost | 210 | – | – |
| truck engine overhaul cost | 110 | – | – |
| semi truck engine rebuild cost | 70 | – | – |
| truck engine rebuild cost | 30 | – | $1.39 |
| in frame overhaul cost | 30 | – | – |
| cummins isx overhaul cost | 30 | – | $1.24 |
| cummins x15 overhaul cost | 30 | – | $0.48 |
| n14 cummins overhaul cost | 10 | – | – |
| volvo truck engine rebuild cost | 10 | – | $9.58 |

~510/mo, near-zero CPC — research traffic, not buyers. It is the top of the
funnel for the $26–34 CPC financing terms, and that is how the page should be
built: lead with cost, convert to financing.

Aircraft is real but tiny — `aircraft engine overhaul cost` 40, `aircraft engine
overhaul financing` 10 at $9.02. A section on `aircraft-financing.html`, not a
page.


## Cluster 2 — rent-to-own / lease-to-own / RPO

Broader, higher volume, same zero difficulty, and it spans equipment categories
you already have pages for.

| Keyword | Vol/mo | KD | CPC |
|---|---|---|---|
| rent to own lawn equipment | **6,600** | 3 | $2.84 |
| lease to own lawn equipment | **6,600** | 7 | $2.84 |
| rpo financing | 260 | – | – |
| rent to own equipment | 210 | 0 | $8.04 |
| rent to own gym / fitness / exercise equipment | 210 each | 0 | $5.93 |
| rent to own restaurant equipment | 110 | 0 | **$19.21** |
| lease to own restaurant equipment | 110 | 0 | **$19.21** |
| lease to own equipment | 70 | 0 | $15.85 |
| rent to own equipment no credit check | 70 | 0 | $7.25 |
| rent to own heavy equipment | 50 | 0 | $15.38 |
| lease to own heavy equipment | 50 | 0 | $15.38 |
| rental purchase option | 50 | 0 | $1.05 |
| rent to own equipment near me | 50 | 6 | $7.10 |
| equipment lease to own | 30 | 0 | **$52.87** |
| lease to own equipment financing | 30 | 23 | $25.43 |
| lease to own commercial kitchen equipment | 20 | – | $9.62 |

The lawn-equipment pair at 6,600/mo, KD 3–7, is the largest thing in this
research by an order of magnitude. Treat with caution — at $2.84 CPC it is
probably homeowners renting a mower, not landscaping contractors. But you have
`commercial-mower-financing` and `landscaping-business-financing` already, and
nobody has checked whether the commercial slice is reachable. Worth its own look.

By machine, where the intent is unambiguously commercial:

| Keyword | Vol/mo | CPC |
|---|---|---|
| rent to own skid steer / lease to own skid steer | 390 each | $10.62 |
| rent to own mini excavator | 140 | $5.83 |
| rent to own skid steer no credit check | 110 | $13.37 |
| rent to own excavator | 90 | $7.45 |
| rent to own dump truck | 90 | $3.92 |
| lease to own dump truck | 90 | $5.45 |
| rent to own forklift | 70 | $14.46 |
| rent to own excavator no credit check | 40 | $8.69 |
| lease to own excavator | 40 | $6.48 |
| rent to own backhoe | 20 | $7.66 |

Search Console corroborates: `rent to own` already pulls 12 impressions at
position 22.5 across 8 queries (`rent to own mini excavator`, `rent to own skid
steer no credit check near me`, `rent to own vending machines`) landing on
equipment pages that do not answer the question.

**The SERP hole is still the best part.** Every RPO result is a dealer or rental
yard explaining its own program — RDO, United Rentals, ALL Crane, Luby, Carolina
Cat. The only finance-side page is Commercial Credit Group's. Nobody answers
*my rental term is ending, the buyout is due, I need financing for it.*


## Cluster 3 — trucking lease-purchase (do not build as written)

| Keyword | Vol/mo | CPC |
|---|---|---|
| lease to own semi trucks | 2,900 | $7.94 |
| lease purchase trucking companies | 2,400 | $8.98 |
| lease purchase semi truck(s) / a semi truck | 390 each | $8.90 |
| rent to own semi trucks | 170 | $4.43 |
| rent to own trailers | 2,900 | $5.07 |

Big numbers, wrong intent. The SERP for `lease to own semi trucks` is carriers
and dealers running lease-purchase programs — Prime, Melton, Ryder, Lone
Mountain, SFI, Freedomway. These are **drivers looking for a carrier to lease
from**, not businesses seeking third-party financing. You cannot fulfill it.

`rent to own trailers` at 2,900 is likely mobile homes — autocomplete surfaces
`rent to own trailer homes` and `rent to own trailer parks near me` alongside it.

There is one legitimate angle: a comparison page arguing what lease-purchase
actually costs a driver versus financing their own truck. Every page in that SERP
is selling lease-purchase, so nobody occupies the sceptical position, and it
converts lease-purchase-curious drivers into equipment-finance leads. That is a
different page from the one the raw volume suggests.


## Recommended build, revised order

### Priority 1 — `/equipment-financing/articles/rent-to-own-equipment-financing/`

Bigger cluster, broader internal-link surface, and the only genuinely open SERP.

**Title:** Rent-to-Own & Lease-to-Own Equipment Financing | RPO Buyouts | Axiant

Primary: `rent to own equipment` (210), `rpo financing` (260), `lease to own
equipment` (70), `rent to own heavy equipment` / `lease to own heavy equipment`
(50 each, $15.38). Secondary: `rental purchase option`, `equipment lease to own`
($52.87 CPC), `rent to own equipment no credit check`.

Differentiated section, the one nobody has: **financing the RPO buyout** —
rental credits applied, residual owed, how a lender underwrites a machine you
have already been running, why converting beats re-renting. Links to
`trac-lease-benefits-saves-money`, `equipment-lease-vs-loan-vs-cash`,
`equipment-sale-leaseback-financing`.

Because KD is 0 on the by-machine terms, the skid steer (390), mini excavator
(140), excavator (90), dump truck (90) and forklift (70) variants are worth
sections on this page pointing at the existing `equipment/` pages, or eventually
their own children.

### Priority 2 — `/equipment-financing/articles/truck-repair-financing/`

Note the URL: `truck-repair-financing`, not `truck-engine-overhaul-financing`.
The head term is `truck repair financing` (70, KD 0, $26.04), not
`truck engine overhaul financing` (10, KD 40).

**Title:** Truck Repair & Engine Overhaul Financing | Semi Truck Repair Loans | Axiant

Primary: `truck repair financing`, `semi truck repair financing`, `engine
overhaul financing` ($34.24 CPC — highest-value term in the research).
Secondary: `semi truck repair loan`, `commercial truck repair financing`,
`truck repair financing no credit check`, `engine rebuild financing`.

Open with the cost layer — in-frame vs out-of-frame, ISX/X15/N14 figures — since
that is 510/mo of the entry traffic, then move to what a lender funds against a
truck that is already down.

### Priority 3 — two candidates, both needing a check first

- **Restaurant/commercial-kitchen rent-to-own** — 110/mo at $19.21 CPC, KD 0, and
  you already have four restaurant equipment pages to link from. Cheapest real win.
- **The lease-purchase-vs-financing comparison** for trucking, per Cluster 3.
- **Lawn/landscaping rent-to-own** at 6,600/mo needs an intent check before
  anyone commits to it.


## Still true from the first pass

**`no credit check` is a real modifier, not a fantasy** — `truck repair financing
no credit check` 30/mo KD 0, `rent to own equipment no credit check` 70/mo KD 0,
`rent to own skid steer no credit check` 110/mo. It is also not accurate;
equipment lenders check credit. Rank for it by answering it honestly. Link
`no-credit-check-business-loans.html`.

**`breakdown-repair-cash-crunch` needs pointing** at the new repair page and
should cede the repair-financing terms to it, or this repeats the imaging-cluster
cannibalization from `AUDIT_PART5_DEMAND`.

**The authority ceiling still applies** — but KD 0 across this space is the
concrete reason these two pages are a better bet than anything else currently
queued.


Sources: [CAG Truck Capital](https://cagtruckcapital.com/engine-overhaul-financing/),
[National Truck Loans](https://www.nationaltruckloans.com/engine-financing),
[First Capital Business Finance](https://firstcapitalbusinessfinance.com/commercial-truck-financing/repair-loans-for-semi-trucks-trailers/),
[RDO Equipment](https://www.rdoequipment.com/resources/blogs/rental-purchase-options-rdo-guide),
[Commercial Credit Group](https://www.commercialcreditgroup.com/blog/rental-conversions),
[ALL Crane](https://www.allcrane.com/rent/rental-purchase-options),
[Prime Inc](https://www.primeinc.com/success-leasing/lease-lease-purchase/),
[Lone Mountain Truck Leasing](https://lonemountaintruck.com/lease-to-own-new-used-semi-trucks-what-you-need-to-know/)


---

# Round 2 — three follow-up questions, and what was built

## Is "auto repair financing" consumer or commercial? Consumer. Settled.

Pulled the live SERP rather than inferring. Top 10 for **`auto repair financing`**
(4,400/mo):

Oportun, AAA, AAMCO, Upstart, Synchrony, OneMain Financial, Credit Karma,
Reddit, Sunbit.

Every result is a consumer personal-loan or point-of-sale consumer lender. Not
one commercial lender ranks. **Skip it** — fulfilling that intent means
consumer POS lending, which is a different business.

**But `engine replacement financing` (140/mo) is genuinely mixed**, and that
changes the earlier advice. Its SERP:

Patriot Engines, American First Finance, Fraser Engines, **National Truck Loans
(#5)**, Reddit, Gearhead Engines, **CAG Truck Capital (#12)**, 800LoanMart,
**Capital Reman Exchange — PACCAR MX engines (#14)**.

Two commercial truck lenders and a Class 8 engine remanufacturer rank on page
one. Google will accept a commercial page for this term, so it is a legitimate
secondary target on the truck repair page rather than something to avoid.

## Sleeper engine replacement — the instinct is right, the query is not

Correct that a sleeper engine replacement is exactly when an operator needs
financing. But almost nobody searches it that way:

| Keyword | Vol/mo |
|---|---|
| semi truck engine replacement cost | 50 |
| truck engine replacement cost | 50 |
| semi truck engine for sale | 70 |
| sleeper truck financing | 10 |
| sleeper truck engine replacement | **no data** |
| semi truck engine replacement financing | **no data** |
| truck engine replacement financing | **no data** |

So: no separate sleeper page — there is no query to rank for. Instead the
replacement decision became a major section of the truck repair page
(*Overhaul, Replace, or Trade*), targeting the cost terms that do exist plus
`engine replacement financing` at 140. That adds roughly 240/mo to the page and
makes it better, so the instinct earned its place — just not as its own URL.

## ITIN — real, wide open, and small in the business slice

| Keyword | Vol/mo | KD | CPC |
|---|---|---|---|
| itin loans / loans with itin | 1,300 | **0** | $6.62 |
| itin mortgage / itin home loans | 880 | **0** | – |
| itin number loans | 590 | **0** | $7.83 |
| itin personal loans | 320&ndash;390 | **0** | $5.68&ndash;$10.60 |
| itin auto / car loans | 210 | **0** | $9.14 |
| itin financing | 90 | 0 | – |
| **business loans with itin number** | **30** | **0** | $15.03 |
| **itin business loans** | **10** | **0** | **$30.41** |

KD **0 across the entire family** — including the 1,300/mo head. The catch: the
volume concentrates in mortgage, personal and auto, which are consumer. The
*business* slice is only ~40/mo exact-match.

What makes it worth building anyway is the SERP. Top 10 for `itin business
loans`: RRCU, Embold CU, Excite CU, Nebo CU, Marine CU, Fibre CU, Cultiva
Financial, Acra Lending, Morty. **Eight credit unions and no national commercial
broker.** Credit unions are membership-restricted by geography or employer, so
a national commercial lender has an open lane — and the trucking overlap is
substantial, since a large share of owner-operators file with an ITIN.

Small volume, $15&ndash;30 CPC, zero difficulty, no direct competitor. Built.

## What was built

| URL | Primary targets | Vol/mo | KD |
|---|---|---|---|
| `/equipment-financing/articles/rent-to-own-equipment-financing/` | rent to own equipment, rpo financing, lease to own equipment, rent/lease to own heavy equipment | 210 / 260 / 70 / 50 | 0 |
| `/equipment-financing/articles/truck-repair-financing/` | truck repair financing, semi truck repair financing, engine overhaul financing, engine replacement financing | 70 / 70 / 30 / 140 | 0 |
| `/equipment-financing/articles/itin-business-loans/` | itin business loans, business loans with itin number, itin equipment/truck financing | 10 / 30 | 0 |

Each built from the existing article template (`tow-truck-wrecker-financing`),
so head, nav, critical CSS, rails, footer and scripts are identical to the rest
of `/equipment-financing/articles/`. Each carries BreadcrumbList, Article,
FAQPage and WebPage JSON-LD, a `.quick-answer` speakable block, a 10-question
FAQ with full schema/visible parity, and a working TOC.

**Wired in** (checked, not assumed):

- `sitemap.xml` — 3 `<url>` entries, file re-parsed to confirm valid XML
- `equipment-financing/articles/index.html` — 3 article cards
- `equipment-financing.html` — 2 links in *More Equipment &amp; Asset Financing*
- `trucking-business-financing.html` — a `relevant-post-card` for truck repair
- `trucking-business-financing/breakdown-repair-cash-crunch/` — a pointer ceding
  the repair-financing terms, per the cannibalization note above

**Not built, deliberately:** `auto repair financing` (consumer, SERP-confirmed),
a standalone sleeper page (no query), `lease to own semi trucks` / `lease
purchase trucking companies` (carrier-program intent you cannot fulfil), and
`rent to own lawn equipment` at 6,600/mo, which still needs an intent check
before anyone commits to it.

**Next:** these are new URLs with no inbound authority. Add them to
`REINDEX_QUEUE` and request indexing; `npm run indexnow` submits to IndexNow.


---

# QA pass — audited against docs/CONTENT_QUALITY_PLAYBOOK.md

Audited the three pages against the site's own standard rather than a generic
checklist. Seven defect classes found and fixed; two findings came back clean.

## Fixed

1. **British spellings** — `labour` ×4, `tyres`, `favour`, `licence` ×2. A US
   commercial-finance site should not read as British. Now US throughout.
2. **Exact-match target phrases were largely absent.** The pages used hyphenated
   and paraphrased forms, so coverage was 3/13, 5/12 and 2/7 against the terms
   the research says to target. Playbook step 1 is explicit about matching
   Google's exact vocabulary. Now **13/13, 12/12, 7/7**.
3. **Primary phrase missing from title/H1** on the truck page — it read *Truck
   Repair & Engine Overhaul Financing*, which never contains the contiguous head
   term `truck repair financing` (70/mo, KD 0). Retitled to **Truck Repair
   Financing & Engine Overhaul Loans**.
4. **Schema/title desync** created by that retitle — `og:title`, `twitter:title`,
   `Article.headline`, `WebPage.name`, the BreadcrumbList leaf and the visible
   crumb all still carried the old wording. This is the exact failure
   `SCHEMA_TITLE_CONFLICT_2026-08-02.md` documents. All six aligned, plus the
   inbound anchor text on two pages.
5. **`author` violated the documented convention** — `AI_SEARCH_OPTIMIZATION.md`
   requires `Axiant Partners LLC` / `https://axiantpartners.com/`. The template
   these were generated from carries the legacy value, so all three inherited it.
   Corrected.
6. **No `HowTo` block** — the playbook lists HowTo on equipment guides and the
   source template has one. Added a 5-step HowTo to each page.
7. **17 AI-voice tells** not on the playbook's banned list: `genuinely` ×4,
   `considerably` ×4, `the honest summary`, `the good news is`, `this is where`,
   `it is worth`, `materially`, `effectively`, `in practice`. All rewritten to
   direct phrasing.

**A regression I introduced and caught:** retitling the truck page removed
`engine overhaul financing` — at $34.24 CPC the highest-value term in the whole
research — from the document entirely. Restored to the body.

## Clean

- **Banned phrases:** zero across all three, against the playbook's 30-item list.
- **Cannibalization:** checked all 18 target phrases against the title and H1 of
  every HTML file in the repo. **No other page claims any of them.** The one real
  adjacency, `breakdown-repair-cash-crunch`, is framed as cash-flow and now links
  in rather than competing.

## Calibration note

Measured em-dash density and contraction use against `tow-truck-wrecker-financing`
before "fixing" either. The existing page runs 8.9 em-dashes per 1,000 words and
3 contractions; the new pages run 6.7&ndash;9.4 and 4&ndash;7. Already house voice, so
both were left alone.

## One deliberate deviation

`rent to own equipment` is not contiguous in the rent-to-own page's title or H1,
which keep the correctly-hyphenated *Rent-to-Own*. Google normalizes hyphens, and
unhyphenating a title to chase an exact string reads wrong to a human. The exact
unhyphenated phrase carries in an H2 (*How Rent to Own Equipment Financing
Works*) and throughout the body instead.

## Final state

| | Words | Schema blocks | FAQ parity | TOC | Links |
|---|---|---|---|---|---|
| rent-to-own-equipment-financing | 2,072 | 5 | 10/10 | 8/8 | 36/36 |
| truck-repair-financing | 2,060 | 5 | 10/10 | 8/8 | 32/32 |
| itin-business-loans | 1,740 | 5 | 10/10 | 7/7 | 28/28 |

Schema on each: BreadcrumbList, Article, FAQPage, WebPage, HowTo. Quick-answer
blocks run 109&ndash;130 words, each carrying a number, each marked `speakable`.
Sitemap re-parsed as valid XML after the edits. Every new page has 2&ndash;3
inbound internal links.
