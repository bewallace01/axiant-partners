# GSC Performance Analysis — June 17, 2026

**Source:** GSC export `https___axiantpartners.com_-Performance-on-Search-2026-06-17` (Web, Last 28 days = May 19 – June 15, 2026)
**Totals:** ~24,700 impressions · **~82 clicks** · site-wide CTR ≈ **0.33%** · avg position ~21
**Context:** First full GSC pull since the May 18 indexing-dilution event (see [SEO_CLEANUP_TRIAGE_2026-05-27.md](SEO_CLEANUP_TRIAGE_2026-05-27.md)).

---

## Headline diagnosis: site-wide CTR collapse, not a ranking problem

The site has plenty of impressions and is ranking on page 1 for many queries — but almost nobody clicks. The dominant cause is **AI Overviews / Google AI Mode answering informational queries in-SERP**, so the user never visits the site.

Evidence:

| Page | Impressions | Clicks | Position |
|---|---:|---:|---:|
| `construction-business-financing/why-contractors-need-working-capital` | **3,774** | **0** | **3.94** |
| `commercial-real-estate-loans/.../how-much-down-payment-required-commercial-property-loan` | 1,436 | 1 | 16.97 |
| `business-line-of-credit/.../what-are-typical-business-line-of-credit-rates` | 613 | 2 | 39.87 |
| `equipment-financing/.../carecredit-vs-patientfi-imaging-radiology` | 614 | **7** | 18.42 |

- Position 4 with 3,774 impressions and **zero** clicks is a textbook AI-answer-cannibalization signal, not a rank issue.
- The **Queries** report is saturated with natural-language and full-paragraph persona/LLM-style prompts (e.g. "what funds construction draw gaps?", "what's the fastest closing time possible for bridge loan financing?", and multi-line ICP persona prompts) — these surface in AI/answer contexts that rarely pass a click.
- **Bright spot / the pattern to copy:** `carecredit-vs-patientfi` is the top non-branded page at **7 clicks** — comparison / "X vs Y" intent still earns a click after the AI summary. "vs", "rates", and concrete-data pages survive AI cannibalization best.

## Recovery from the May drop is real but early

From `Chart.csv` (daily):
- May 19–28: ~350–520 impressions/day, avg position ~24–29, ~1 click/day (post-dilution trough).
- May 29 – Jun 1: impression spike (up to 3,355/day), position briefly 9.8–13.
- Jun 8–15: stabilized ~720–1,150 impressions/day, position recovered to ~17–21, clicks up to **4–10/day**.

**Conclusion:** the cleanup-before-publishing strategy is working. Hold the line — no new programmatic pages until index count and position fully stabilize.

---

## Bridge loan cluster — detail (the "more agency on bridge" question)

The full bridge cluster pulled **~260 impressions and 2 clicks in 28 days.** The cluster is **over-built relative to its search demand**, and the hub has a visibility problem, not a content gap.

| Bridge page | Impr | Clicks | Position |
|---|---:|---:|---:|
| `…/articles/typical-commercial-bridge-loan-rates-2026` | 69 | 1 | **5.43** ✅ only bridge winner |
| `…/articles/how-fast-can-you-close-commercial-bridge-loan` | 36 | 0 | **27.72** ⚠️ was 10.1 in May — fell off page 1 |
| `…/articles/when-should-you-use-commercial-bridge-loan` | 33 | 0 | 10.30 |
| `…/articles/5m-bridge-loan-multifamily-structure-closing-timeline` | 31 | 0 | 6.68 |
| `…/articles/what-do-lenders-look-for-commercial-bridge-loan` | 25 | 0 | 18.88 |
| `…/articles/bridge-loan-pitfalls-what-can-go-wrong` | 24 | 0 | 9.54 |
| `…/articles/bridge-loan-vs-heloc` | 11 | 0 | 50.64 (buried) |
| `…/articles/bridge-loan-value-add-commercial-property` | 11 | 1 | 7.45 |
| `…/articles/construction-loan-vs-bridge-loan` | 6 | 0 | 25.67 |
| `…/articles/bridge-loan-pay-off-construction-debt` | 5 | 0 | 4.80 |
| `…/articles/bridge-loan-buy-before-you-sell` | 5 | 0 | 52.80 |
| **`commercial-bridge-loans.html` (HUB)** | **5** | 0 | 5.80 |

**Key finding: the bridge hub got 5 impressions in 28 days** while its own child articles pull 30–70. A hub at position 5.8 being out-competed by its children is the classic signature of **keyword cannibalization** — authority for "commercial bridge loan" terms is split across child URLs instead of concentrating on the hub.

### What "more agency on bridge" should mean (NOT more pages)
1. **Fix hub cannibalization (diagnose first, ~1 hr).** Identify which bridge URL Google ranks for core "commercial bridge loan" terms and consolidate intent onto the hub. Zero new URLs.
2. **Win AI-citation on existing bridge demand (~half day).** Port the `rates-2026` page's data-first approach to the hub: a real comparison **table** (bridge vs hard money vs construction vs SBA — term/speed/LTV/rate) + dated 2026 rate ranges. Tables + dated numbers get extracted and cited.
3. **Recover `how-fast-can-you-close` (~30 min).** Dropped position 10 → 28. Rewrite title/meta per `.cursor/rules/seo-geo-aeo-meta.mdc` and refresh content.
4. **No net-new bridge URLs** until recovery gates clear.

### Bigger-picture priority
Bridge is high-ticket but low-volume (~260 impr/28d). The recoverable traffic is in construction working capital, CRE down-payment, equipment (semi-truck, medical imaging), and "vs/comparison" queries — pages already pulling 600–3,700 impressions at near-zero CTR. **Fixing CTR / AI-citation on those is ~10× the prize of bridge.** Fix bridge because deals are large; spend the most effort on the high-impression CTR leak.

---

## Recommended next actions (ranked)
1. **Site-wide CTR/AEO pass** on the top ~15 high-impression / zero-click pages — rewrite titles+metas to comparison/data/answer framing that survives AI Overviews. Highest ROI.
2. **Bridge hub cannibalization fix** + hub comparison table (items 1–2 above).
3. **Continue May cleanup** — confirm index count is dropping; keep the publishing freeze.
4. **Re-pull GSC in ~2 weeks** to confirm CTR pass and recovery trajectory.
</content>
</invoke>
