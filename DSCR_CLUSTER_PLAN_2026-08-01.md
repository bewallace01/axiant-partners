# DSCR Cluster Plan — 2026-08-01

**Scope correction that produced this plan.** Earlier work in this cycle read "commercial
mortgage / back deals with real estate" as SBA 504. That was wrong — SBA is
government-guaranteed lending, the opposite of the private-credit, business-purpose lane
Axiant actually places. This plan covers that lane.

**Method:** DataForSEO Labs (US, en) — 215 unique DSCR keywords at ≥100/mo; live SERP pulls
on the three head terms; cross-referenced against all site pages and the fresh GSC export
(`_analysis/gsc-2026-08-01`, 28 days to 2026-07-30).

---

## Why this is the largest opportunity on the site

| Cluster | Head term | Volume | KD |
|---|---|---|---|
| **DSCR** | `dscr loan` | **60,500** | **8** (`dscr loans` = **1**) |
| Commercial mortgage | `commercial property loan calculator` | 14,800 | 10 |
| SBA 504 | `sba 504 lender` | 8,100 | 19 |

`dscr loan` is **7× the entire SBA 504 cluster** and **4× the calculator cluster**, at lower
difficulty than either. Total addressable across the cluster is roughly **125,000/mo**.

**Current coverage is close to nothing:**

| Existing page | Words | Problem |
|---|---|---|
| `dscr-calculator.html` | **606** | Thinnest page in the cluster, against 7,200/mo of KD-0 calculator terms |
| `dscr-loan-vs-conventional-mortgage/` | 1,277 | Fine — distinct intent, leave alone |
| `dscr-rental-loans-real-estate-investors/` | 1,462 | Fine — distinct intent, leave alone |
| `real-estate-investor-financing-guide/` | 1,401 | Mentions DSCR, doesn't target it |

There is **no DSCR hub or service page**. GSC confirms the absence: one DSCR page appears in
the top 673 at **17 impressions**. The homepage does not link to the DSCR calculator at all.

---

## SERP reality check

KD 8 on a 60,500/mo commercial term is suspicious, so I pulled the live SERPs.

**`dscr loan` — only 7 organic results.** AI Overview and SERP features consume the rest.
Rankers: figure.com, **reddit.com at #2**, angeloakms, newfi, farmbureau.bank, nasb,
crosscountrymortgage. Reddit ranking second on a commercial-intent money term means Google
is not satisfied with the commercial pages available. That is the opening.

**`dscr loan calculator` — 9 organic**, all lender-built calculators plus omnicalculator and
nerdwallet. Same shape as the commercial mortgage calculator SERP, which is a play already
run successfully on this site.

**`dscr loan lenders`** — note **txpremiermortgage.com at #5** with "Top DSCR Lenders in
Texas". A competitor is already winning with the exact geo play proposed in Phase 3.

**Read:** the field is lenders and brokers, not Forbes/NerdWallet-class publishers. Axiant is
the same class of entity. This is beatable — unlike the commercial mortgage calculator SERP,
where every slot was a bank or a dedicated calculator property.

---

## Phase 1 — Foundation (do these two first)

### 1.1 Expand `dscr-calculator.html` — 606 → ~1,500 words
**Targets:** `dscr loan calculator` 3,600/**KD 0** · `dscr calculator` 3,600/**KD 0** ·
`calculate dscr` 3,600/KD 16 · `dscr formula` 3,600/KD 23 · `dscr ratio formula` 3,600/KD 24

Roughly **7,200/mo at KD 0** plus ~10,800/mo of formula-intent terms the page can absorb with
a worked-math section. This is the single cheapest win in the plan: the tool already exists,
it is simply too thin to rank and too buried to be found.

- Keep one calculator URL. Do **not** split `dscr calculator` and `dscr loan calculator` —
  same SERP, same intent (this is the rule the commercial mortgage calculator merge established).
- Add: the formula written out, a worked example with dollars, what lenders accept
  (1.20–1.35x typical), what happens below 1.0, and an FAQ mirrored in `FAQPage` JSON-LD.
- Link it from the homepage and the CRE hub. It currently has no homepage link.
- `dscr-calculator-embed.html` (102 words) must stay `noindex`.

### 1.2 New hub: `/dscr-loans.html` — the missing money page
**Targets:** `dscr loan` / `dscr loans` **60,500/mo, KD 1–8** · `what is a dscr loan`
6,600/KD 13 · `what is dscr loan` 1,900/KD 18

A root-level service page, structured like `commercial-real-estate-loans.html`. This is the
cluster's hub and every other page in the plan links up to it.

Because only 7 organic slots exist and an AI Overview sits above them, the page must be
built to be **cited**, not only clicked: front-load a 40–60 word answer carrying the
citable numbers (no personal income verification, 20–25% down, 1.0–1.25x minimum DSCR,
close in 21–30 days), then go deep.

---

## Phase 2 — Supporting cluster

| # | Page | Primary target | Vol | KD | CPC |
|---|---|---|---|---|---|
| 2.1 | DSCR loan requirements | `dscr loan requirements` | 2,900 | 10 | $11.76 |
| 2.2 | DSCR loan rates | `dscr loan rates` | 3,600 | 6 | $13.26 |
| 2.3 | **DSCR loan lenders** | `dscr loan lenders` | 590 | **0** | **$44.74** |
| 2.4 | What is a DSCR loan | `dscr loan meaning` | 8,100 | 27 | $4.25 |

**2.3 is the conversion page.** `dscr loan lenders` at **$44.74 CPC** and `best dscr loan` at
**$53.39** are the highest-value keywords found anywhere in this account — higher than the
SBA 504 refinance term that was the previous record. KD 0. No page exists.

2.4 is definitional and low-CPC; build it for citation and internal linking, not conversion.
It can be folded into 1.2 if hub length allows — decide at build time, do not split
`what is a dscr loan` from the hub if the hub already answers it well.

---

## Phase 3 — Geo pages (27 terms, ~12,000/mo, every one KD 0)

| State | Volume | CPC | | State | Volume | CPC |
|---|---|---|---|---|---|---|
| Texas | 1,300 | $20.03 | | Illinois | 170 | $19.19 |
| Florida | 1,300 | $19.48 | | **Pennsylvania** | 170 | **$41.74** |
| Ohio | 480 | $22.38 | | Alabama | 170 | $16.99 |
| Michigan | 480 | $16.90 | | Maryland | 170 | $14.18 |
| North Carolina | 390 | $20.05 | | Colorado | 140 | $17.20 |
| Georgia | 320 | $23.69 | | Virginia | 140 | $21.72 |
| California | 320 | $25.03 | | | | |

**Validated by a competitor:** txpremiermortgage.com ranks #5 for `dscr loan lenders` on a
Texas-specific page.

**Two conditions before building any of these:**

1. **Confirm Axiant can actually place DSCR in the state.** These are lender-intent queries;
   ranking in a state you cannot fund wastes the click and the reputation. This is a business
   question, not an SEO one, and it gates the whole phase.
2. **Each page must carry genuinely state-specific substance** — local lender behaviour,
   state-level LLC and transfer-tax treatment, typical rents and DSCR maths for that market.
   Spun templates with the state name swapped are what Google's 2024–25 updates target, and
   this site has already paid for duplicate content three times this cycle.

Start with Texas and Florida only. Measure for 6 weeks. Expand only if they rank.

---

## Cannibalization guardrails

The site has produced **three duplicate pairs** in this cycle, each splitting authority and
suppressing a cluster. Rules for this build:

- **One calculator page.** `dscr calculator` and `dscr loan calculator` share a SERP.
- **Do not retarget the two existing DSCR articles.** `dscr-loan-vs-conventional-mortgage`
  and `dscr-rental-loans-real-estate-investors` hold distinct intents and should link *up*
  to the new hub, not compete with it.
- **Hub owns the head term.** No supporting page may take `dscr loan` / `dscr loans` in its
  title or H1.
- **Geo pages target `dscr loan [state]` only** — never the unqualified head term.
- Run the existing overlap check (title/H1 token Jaccard ≥ 0.45) before publishing each page.

---

## Sequence and expected effort

| Order | Item | Type | Why first |
|---|---|---|---|
| 1 | Expand DSCR calculator | Optimize | 7,200/mo KD 0, tool already exists, cheapest win |
| 2 | `/dscr-loans.html` hub | **New** | Anchors the cluster; 60,500/mo head term |
| 3 | DSCR loan lenders | **New** | KD 0 at $44.74 CPC — highest-value term in the account |
| 4 | DSCR loan requirements | **New** | 2,900/mo, KD 10 |
| 5 | DSCR loan rates | **New** | 3,600/mo, KD 6 |
| 6 | Texas + Florida geo | **New** | 2,600/mo combined, KD 0 — pilot only |
| 7 | Remaining 10 states | **New** | Only if 6 ranks |

Items 1–5 are the core. Item 1 is an edit; 2–5 are four new pages.

---

## What this plan does not solve

**Links.** Nothing here builds any, and the head term almost certainly needs them. The
supporting terms (KD 0–10) are winnable on content alone; `dscr loan` at 60,500 probably is
not, even at KD 8. Treat the hub as a 6–12 month asset, not a quick win.

**The site-wide pattern.** Across 328 equipment queries and 7,322 impressions the site earned
**2 clicks**; the CRE cluster earned 0 on 1,280. Broad eligibility, narrow winning. This plan
adds a cluster where coverage is genuinely absent — but it does not fix the pages already
ranking 10–13 and converting nothing. Those are a separate, cheaper workstream
(`vending machine financing` 1,300/mo KD 0 at position 10.5; `security guard payroll
financing` 880/mo KD 0 at position 10.5).

**Verify before building.** Several GSC-visible queries in this account turned out to be AI
Overview fan-out with zero human volume. Every keyword in this plan was checked against
DataForSEO and has real volume — but re-check anything added to it later.
