# Commercial Mortgage Keyword Strategy — 2026-08-01

**Method:** DataForSEO Labs keyword_suggestions (US, en), 18 seeds, 728 unique keywords
collected → 229 after variant dedupe. Cross-referenced against all 834 site pages
(title + H1 + URL token coverage) to score existing coverage. GSC export
`_analysis/gsc-2026-06-03` used for current-position evidence. API spend: $0.31.

---

## Headline: the cross-sell thesis has no search demand

The premise was that equipment applicants with real estate should be routed to a
property-secured facility, and that we should build pages attacking that framing.

**Those searches do not exist.** Seeds returning zero keywords at ≥40 monthly volume:

| Seed | Results |
|---|---|
| `business loan secured by real estate` | 0 |
| `real estate secured business loan` | 0 |
| `business loan using property as collateral` | 0 |
| `borrow against commercial property` | 0 |

Nobody searches for the collateral-swap concept. They search for the *product* —
`commercial mortgage rates`, `commercial property loan`, `sba 504` — because by the
time they search, they already know they want property financing.

**Implication:** the cross-sell is a sales motion, not a search motion. Capture the
large existing commercial-mortgage demand, then run the equipment→CRE conversion
through on-page CTAs, internal links, and the intake form. Do not build a content
cluster around the framing itself.

The one exception — a thin but extremely high-intent seam worth 2–3 pages:

| Keyword | Vol | KD | CPC |
|---|---|---|---|
| `business loan for property purchase` | 320 | 24 | **$43.48** |
| `loan against property` | 390 | 3 | **$41.12** |
| `commercial equity loan` | 260 | 0 | **$47.11** |
| `business loan rental property` | 260 | 0 | $19.38 |

Low volume, but CPC above $40 means advertisers are paying heavily for this exact
buyer. `real-estate-secured-business-loan.html` (2,914 words) already exists and is
the natural home — it needs re-optimizing toward these phrasings, not replacing.

---

## Priority 1 — The calculator cluster (~40,000/mo, KD 9–13)

The single biggest winnable opportunity on the site.

| Keyword | Vol | KD | Coverage |
|---|---|---|---|
| `commercial real estate loan calculator` | 14,800 | 13 | 0.89 — strong |
| `commercial property loan calculator` | 14,800 | 10 | 0.64 — partial |
| `commercial mortgage calculator` | 9,900 | **9** | 0.55 — weak |
| `commercial mortgage loan calculator` | 9,900 | 9 | 0.64 — partial |
| `mortgage calculator commercial property` | 1,300 | 10 | 0.42 — none |

Difficulty of 9–13 against ~40k combined volume is extraordinarily soft for this
vertical. We have exactly one calculator page
(`commercial-real-estate-loans/articles/commercial-real-estate-loan-calculator/`),
optimized for one phrasing, and GSC shows **zero clicks** on it.

**Do:** expand the existing page to own all phrasings — H2s and FAQ entries using
"commercial mortgage calculator" and "commercial property loan calculator" verbatim,
plus schema. **Do not** build separate pages per phrasing; that is textbook
cannibalization and these variants share a SERP.

Also: `commercial-real-estate-loan-calculator/embed.html` (113 words) needs
`noindex` — it currently canonicals to the parent but should not be crawlable at all.

---

## Priority 2 — SBA 504 (8,100/mo, ranking position 52–67)

GSC shows ~400 impressions across a dozen `504 vs 7a` variants at **positions 52–67**.
Page six. Proven eligibility, zero capture.

| Keyword | Vol | KD | CPC |
|---|---|---|---|
| `sba 504 lender` / `lending` / `lenders` | 8,100 | 19–37 | $19.36 |
| `sba 504 loan interest rate` | 2,400 | **0** | $12.69 |
| `sba 504 interest rate` | 2,400 | **2** | $12.69 |
| `sba 504 rate` | 2,400 | 6 | $12.69 |
| `sba 504 program` | 880 | 26 | $17.74 |
| `sba 504 refinance` / `refinancing` / `refi` | 140 | **0** | **$55.29** |
| `sba 504 prepayment penalty` | 110 | 0 | — |

Three pages currently chase this cluster and none wins:
`sba-loans/articles/sba-504-vs-7a-decision-tree/`,
`sba-loans/articles/sba-504-vs-conventional-cre/`,
`commercial-real-estate-loans/articles/sba-504-vs-conventional-commercial-real-estate-loan/`.

The last two are near-duplicates of each other.

**Do:**
1. Merge `sba-504-vs-conventional-cre` and
   `sba-504-vs-conventional-commercial-real-estate-loan` → one page, 301 the loser.
2. New page: **SBA 504 lenders** — 8,100/mo, KD 19, and the closest thing we have is
   `sba-loans-blog.html`, a thin index. Genuine gap.
3. New page: **SBA 504 refinance** — KD 0 at $55.29 CPC, the highest-intent keyword
   in the entire dataset.
4. Fold `sba 504 interest rate` phrasings into the existing
   `sba-loans/articles/sba-504-loan-rates/` page. KD 0–6 means this is nearly free.

---

## Priority 3 — Broker / lender intent (KD 0–14, CPC $37–39)

| Keyword | Vol | KD | CPC |
|---|---|---|---|
| `commercial mortgage broker` / `brokers` / `brokerage` | 1,600 | **0** | $37.27 |
| `commercial mortgage agent` | 1,600 | 8 | $37.27 |
| `commercial mortgage lender` / `lenders` | 1,300 | 10 | $39.47 |
| `commercial mortgage lending` | 1,300 | 14 | $39.47 |

Difficulty zero. CPC near $40. **This is what Axiant actually is**, and there is no
page for it. Highest ratio of commercial value to effort in the analysis.

**Do:** one page targeting commercial mortgage broker/lender intent — who we are,
what we place, lender network, process. Positions the brokerage directly rather than
educating about a product.

---

## Priority 4 — Rate pages (2,900/mo, KD 19–21)

| Keyword | Vol | KD |
|---|---|---|
| `commercial mortgage rates` / `rate` / `interest rate(s)` | 2,900 | 19–20 |
| `current commercial mortgage rates` | 1,000 | 21 |
| `30 year commercial mortgage rates` | 880 | 14 |
| `commercial building loan rate` | 720 | 19 |
| `commercial mortgage rates today` | 590 | 20–21 |
| `interest rate on loan for commercial property` | 1,900 | 22 |

`commercial-real-estate-loans/articles/typical-commercial-real-estate-loan-rates-2026/`
exists but scores only 0.42 against the "commercial mortgage rate" phrasings — it uses
"commercial real estate loan," not "commercial mortgage." Same vocabulary problem as
the calculator.

**Do:** re-optimize the existing rates page for "commercial mortgage rate(s)" wording
and add a `current` / `today` freshness section. Term-length variants (30-year,
15-year, 10-year) belong as H2s on that page, not separate URLs.

---

## Cannibalization findings

Canonicals are clean — the stub `index.html` files and `-blog.html` variants all
canonical correctly to their `/articles/` hubs. Three real problems:

**1. True duplicate — fix first.**
`fix-and-flip/articles/fix-and-flip-first-time-investors/` vs
`fix-and-flip/articles/fix-and-flip-loan-first-time-flippers/` — 71% title/H1 token
overlap, both self-canonical, both ~1,600–2,000 words, same intent, same query.
Merge, 301 the loser.

**2. SBA 504 vs conventional — two pages, one query.** Covered in Priority 2.

**3. `commercial-real-estate-loan-requirements` vs
`how-much-down-payment-required-commercial-property-loan`** — both ~2,160 words,
overlapping on down payment. Pick one to own the query; the other links to it.

**Template repetition to monitor:** "what do lenders look for" runs three times
(bridge / CRE / fix-and-flip). Defensible since collateral differs, but check GSC
before adding a fourth.

---

## Do NOT build

- **CMBS** (`commercial mortgage backed securities`, 4,400/mo, KD 7). Volume is real
  but intent is analyst/student, not borrower. The existing
  `cmbs-vs-life-company-vs-agency-debt` article is sufficient.
- **Brand and TV-ad noise** surfaced by the tool: `rocket mortgage super bowl`,
  `tom selleck reverse mortgage commercial`, `berkadia commercial mortgage`,
  `arbor commercial mortgage llc`, `redfin rocket mortgage`. Irrelevant.
- **Separate pages per calculator or rate phrasing.** Consolidate instead.

---

## Sequence

| # | Action | Type | Why |
|---|---|---|---|
| 1 | Merge the two fix-and-flip first-timer pages | Fix | Active cannibalization |
| 2 | Expand calculator page to all phrasings | Optimize | ~40k/mo, KD 9–13 |
| 3 | New: commercial mortgage broker/lender page | New | KD 0, CPC $37–39 |
| 4 | Consolidate SBA 504 vs conventional duplicates | Fix | 3 pages, none ranking |
| 5 | New: SBA 504 lenders | New | 8,100/mo, KD 19, no page |
| 6 | New: SBA 504 refinance | New | KD 0, CPC $55.29 |
| 7 | Re-optimize rates page for "mortgage" vocabulary | Optimize | 2,900/mo, KD 19 |
| 8 | Re-optimize `real-estate-secured-business-loan.html` | Optimize | CPC $41–47 seam |
| 9 | `noindex` the calculator embed page | Fix | Thin duplicate |

Items 1, 2, 4, 7, 8, 9 are edits to existing pages. Only 3, 5, 6 are new pages —
three, not a cluster. The site already has 58 CRE pages; the constraint is
consolidation and vocabulary, not volume.

---

## Note on vocabulary

The recurring failure across the calculator, rates, and SBA clusters is that pages say
**"commercial real estate loan"** where searchers say **"commercial mortgage."** The
content is right; the words are wrong. That single substitution, applied across the
existing CRE cluster, is worth more than any new page in this document.
