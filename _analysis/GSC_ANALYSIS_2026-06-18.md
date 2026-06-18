# GSC Performance Analysis — June 18, 2026

**Source:** GSC export `https___axiantpartners.com_-Performance-on-Search-2026-06-18` (Web, **Last 7 days = Jun 10 – Jun 16, 2026**)
**Totals:** ~6,631 impressions · **31 clicks** · site-wide CTR ≈ **0.47%** · avg position ~19 (impression-weighted)
**Context:** Short 7-day pull, one day after the 28-day analysis ([GSC_ANALYSIS_2026-06-17.md](GSC_ANALYSIS_2026-06-17.md)). Use that file for the longer-window baseline; this one is the freshness check.

---

## Headline: recovery is holding, the CTR leak is unchanged

Versus the 28-day window (May 19 – Jun 15: 0.33% CTR, position ~21), the last 7 days show **CTR up to ~0.47%** and **position tightening to ~19**. Rankings continue to improve. But the structural problem is the same: the site earns impressions and ranks on page 1 for many queries, and almost nobody clicks — **AI Overviews / Google AI Mode answer the query in-SERP**.

The clearest new signal of this is `/business-loan-calculator-guide`: **321 impressions, position 3.77, zero clicks.** Page-1, near top-of-page, no click — that is AI-answer cannibalization, not a ranking problem.

## Where the clicks leak (high impressions, ~0 clicks, 7d)

| Page | Impr. | Clicks | Position |
|---|---:|---:|---:|
| `commercial-real-estate-loans/.../how-much-down-payment-required-commercial-property-loan` | 491 | 1 | 12.43 |
| `equipment-financing/.../carecredit-vs-patientfi-imaging-radiology` | 332 | **3** | 19.09 |
| `business-loan-calculator-guide` | 321 | **0** | **3.77** |
| `commercial-real-estate-loans/.../multifamily-loan-down-payment` | 203 | 0 | 8.94 |
| `business-line-of-credit/.../what-are-typical-business-line-of-credit-rates` | 178 | **0** | 37.05 |
| `business-line-of-credit/.../how-fast-can-you-get-approved-business-line-of-credit` | 154 | 0 | 9.09 |

**Bright spot (still the pattern to copy):** `carecredit-vs-patientfi` is the top non-branded clicker at **3 clicks**. The Queries report confirms it — `patientfi vs carecredit` (23 impr), `cherry vs carecredit` (17 impr). Comparison / "vs" intent still earns a click after the AI summary.

**The 28-day giant cratered:** `construction-business-financing/why-contractors-need-working-capital` — which pulled 3,774 impressions in the 28-day window — fell to **12 impressions at position 33** in the last 7 days. Worth a glance to confirm it wasn't deindexed or hit by a title/intent change.

## Queries confirm the AI-answer thesis

The Queries report is again saturated with natural-language / LLM-style prompts that surface in AI contexts and rarely pass a click:
- "i have a $10m+ investment portfolio and need liquidity without selling assets — what lending options are available through a private bank?" (18 impr)
- "can i finance a complete automotive diagnostics setup for my shop?" (15 impr)
- `excel pmt(0.1025, 20, -126000000)` (23 impr) — a literal calculator query landing on the calculator guide.
- Multiple "commercial multifamily loan typical down payment 20%/25%/30%" paraphrases (64 + 27 + 20 + 18 + 16 impr) all hitting the CRE down-payment pages.

## Recovery from the May 18 dilution event

From `Chart.csv` (daily, Jun 10–16):
- Clicks: 9, 5, 4, 3, 2, 4, 4 — averaging **~4/day**, stable after the early-June 4–10 spike.
- Impressions: rose **925 → 1,313/day**.
- Position: tightened from **18.3 → 15.6** across the week.

**Conclusion:** the cleanup-before-publishing strategy is working. Hold the line — no new programmatic pages until index count and position fully stabilize.

## Bridge loan cluster — 7-day detail

The full bridge cluster pulled **~41 impressions and 1 click** in 7 days, and the hub (`/commercial-bridge-loans.html`) recorded **0 impressions**. Authority for "commercial bridge loan" is split across child URLs while the hub goes unseen — the textbook cannibalization signature, now even starker than the 28-day view (hub was 5 impr there). Over-built relative to its search demand.

| Bridge page | Impr. | Clicks | Position |
|---|---:|---:|---:|
| `.../5m-bridge-loan-multifamily-structure-closing-timeline` | 15 | 0 | 7.53 |
| `.../typical-commercial-bridge-loan-rates-2026` | 7 | **1** | 6.00 |
| `.../when-should-you-use-commercial-bridge-loan` | 7 | 0 | 5.14 |
| `.../bridge-loan-pay-off-construction-debt` | 4 | 0 | 8.25 |
| `.../what-do-lenders-look-for-commercial-bridge-loan` | 4 | 0 | 20.00 |
| `.../bridge-loan-pitfalls-what-can-go-wrong` | 2 | 0 | 11.00 |
| `.../bridge-loan-value-add-commercial-property` | 1 | 0 | 3.00 |
| `.../construction-loan-vs-bridge-loan` | 1 | 0 | 66.00 |
| **`/commercial-bridge-loans.html` (HUB)** | **0** | 0 | — |

## Priorities (unchanged in shape, refreshed in target)

1. **NOW — fix the hub cannibalization.** The hub got 0 impressions; consolidate "commercial bridge loan" intent onto it. Zero new URLs.
2. **NOW — recover the BLoC rates page.** `what-are-typical-business-line-of-credit-rates` is 178 impr at position 37 with 0 clicks — a high-demand "rates" query buried on page 4. Rewrite title/meta to the SEO/GEO/AEO bar, add a dated 2026 rate table.
3. **SOON — win AI-citation with data + tables.** Comparison and dated-rate pages survive AI cannibalization best; port that format to the high-impression hubs.
4. **HOLD — no net-new bridge URLs** until the recovery gates clear.

**Bigger-picture:** bridge is high-ticket but low-volume (~41 impr/7d). The recoverable traffic is in CRE down-payment, the calculator guide, equipment, and "vs/comparison" queries — pages already pulling 150–500 impressions at near-zero CTR. Fix bridge because deals are large; spend the most effort on the high-impression CTR leak.
