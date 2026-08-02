# Content Quality Playbook — Best-Possible Articles & Landing Pages

The repeatable standard for turning any Axiant article (or landing-site page) into the
best version of itself: **sharply keyword-targeted, genuinely substantive, zero AI-sound,
AEO/GEO-ready, and built to convert.** Reuse this for every page and every landing site.

---

## The 7-step process (per page)

1. **Find the one target query.** Pull it from the report's 🔑 Keywords tab (striking-distance
   + DataForSEO volume/difficulty) and GSC. One page = one primary intent. Match Google's
   *exact vocabulary* — e.g. it ranks you for "construction **companies** need working capital,"
   not "**contractors**," so use that phrasing.
2. **Align the shell to the query.** Title (exact-match phrase + a curiosity hook the AI answer
   can't satisfy), one H1, a crisp meta, and at least one H2 phrased as the literal query.
3. **Front-load the answer (AEO/GEO).** First 40–60 words directly answer the query, with one
   citable fact or number. This is what gets quoted in answer boxes / AI Overviews.
4. **Make every section earn its place.** Each section carries a concrete number, a named
   mechanism, or a worked example. Delete any sentence that's "true but empty" or restates its
   heading.
5. **De-cliché (kill the AI-sound).** Remove every banned phrase below; replace with direct,
   specific wording. This is usually what makes good content *read* like a content mill.
6. **Structure for retrieval + conversion.** Real-question H2/H3s, short paragraphs, a comparison
   table where it helps, a visible FAQ mirrored in `FAQPage` JSON-LD, internal links to siblings
   and one money page, a clear CTA.
7. **Verify.** Target phrase present in title/H1/an H2/body; zero banned phrases; schema valid in
   raw HTML; links resolve; "Updated" date current.

---

## Banned phrases (the AI tells) → what to write instead

| Don't write | Write instead |
|---|---|
| unlock / unleash | name the real outcome ("gets a lender to yes", "frees up cash") |
| "whether you're a X or a Y" | address the reader directly; drop the scaffold |
| seamless / seamlessly | "without [the specific friction]" |
| "in today's fast-paced world / landscape" | cut it, or name the actual condition |
| "not only X but also Y" | two direct sentences |
| leverage / utilize | use |
| navigate / navigating the | handle / get through |
| delve into / dive into | look at / break down |
| robust / streamline / facilitate / empower / elevate / embark | a concrete verb |
| "it's important to note" / "worth noting" | just say the thing |
| "the key to" / cornerstone / game-changer / peace of mind / rest assured | cut or specify |
| "a wide range of" / "a variety of" / myriad / plethora | give the actual number or list |
| in order to | to |
| ever-evolving / ever-changing | cut |
| "look no further" / "you're not alone" / "rest assured" | cut |

(Run `scripts/fluff-detector.mjs`-style scan to find these; the report's Content Quality
section flags them per page.)

## Substance standards (what "no fluff" actually means)

- **Real numbers:** advance rates 80–90%, retainage 5–10%, net 30–90, mobilization 2–5% of
  contract value, decisions 24–72h. Use ranges, label them illustrative where needed.
- **Named mechanisms:** UCC-1, notice of assignment (NOA), subordination, acceleration, schedule
  of values, ACV/RCV — name them and explain in one plain sentence.
- **One worked example** with dollars where it fits.
- **No filler:** cut sentences that hedge without informing or restate the heading.

## Voice

Direct, specific, second-person where natural. Sound like an operator who's placed the deals,
not a content mill. Vary sentence length. Lead with the point. Hedging ("may/typically") is fine
in financing writing *when it's accurate* — just don't use it as filler.

---

## Fix log (record every page so we can reuse the patterns)

| Date | Page | Target query | Keyword | Substance | De-cliché | Notes |
|---|---|---|---|---|---|---|
| 2026-06-25 | /articles/business-loans-with-a-tax-lien | "business loan with a tax lien" | already aligned (title/H1/H2 match) | already strong (table, release/withdrawal/subordination, NOA priority) | removed "unlock(s)"×3 | content was solid; only needed de-cliché — example of "don't over-rewrite good pages" |
| 2026-06-25 | /working-capital-loans/articles/how-to-choose-factoring-company | "how to choose / switch a factoring company" | aligned (title/H1) | already strong (NOA, UCC-1, buyout, recourse, all-in cost, red flags) | removed "the key to", "seamless", "whether you're", "more than just"×2 | de-cliché only; content excellent |

| 2026-06-25 | /equipment-financing/articles/...revenue-dropped-war-inflation | "equipment financing revenue dropped" | aligned | strong (HowTo steps, YoY margin) | "unlock approval"→"earn approval" | left "leverage"/"utilization" — legit finance terms |
| 2026-06-25 | /business-debt-relief/articles/release-ucc-lien-business | "release a UCC lien" | aligned | strong (UCC-1/UCC-3, partial release, subordination) | "the key to"×2 → "what reopens" | — |
| 2026-06-25 | /articles/defaulted-on-business-loan-what-happens | — | — | strong | **none — false flag** ("not only missing payments" is correct) | no change |
| 2026-06-25 | /construction-business-financing/can-contractors-finance-used-equipment | — | — | strong | **none — false flag** ("utilization" is a legit equipment term) | no change |

| 2026-06-25 | /commercial-real-estate-loans/articles/how-much-down-payment-required-commercial-property-loan | **SEO/Win-the-click** — "commercial RE / multifamily loan down payment" (6,916 impr, pos 11.6, ~0 clicks) | title → curiosity-gap ("how to put down less") to beat the AI Overview; added a **multifamily table row** to target the biggest query (294 impr, pos 9.4); freshness dates → today | already strong (by-type table, calculator, FAQ) | clean | first SEO-pass page; leak was CTR/position, not content — so improve the *click + the near-page-1 query*, don't rewrite |

| 2026-06-25 | /construction-business-financing/why-contractors-need-working-capital | **SEO** — page pos 4.0, 3,789 impr, 1 click; ranks pos 3 for "reasons construction companies need working capital" (235 impr, 0 clk) | renamed H2 → exact query "The Top Reasons Construction Companies Need Working Capital"; added "construction companies" vocabulary (was 0 mentions — pure "contractors") + concrete reasons list (mobilization 2–5%, retainage 5–10%) | added reasons list w/ numbers | removed "growth tool vs crisis tool" cliché | title already had a calculator hook; fix was the contractor→construction-company vocabulary mismatch + winning the click |

| 2026-06-25 | /construction-business-financing/progress-payment-cash-flow-gaps | "construction company cash flow between jobs payment timing" (225 impr, pos 8.2) | added "construction-company cash-flow between jobs / payment timing" vocabulary to the Quick Answer (page was all "contractor / between draws") | — | punctuation fixed in the site-wide pass | vocab align for the 225-impr query |
| 2026-06-25 | /equipment-financing/articles/how-fast-can-equipment-financing-be-approved | (well-titled — "24–72 Hours", pos 9) | title already strong | — | "streamline"×5 → faster/direct/speed/express | de-fluff only; content + title were already good |
| 2026-06-25 | **SITE-WIDE** | — | — | — | repaired garbled &mdash; punctuation across 29 pages (595 apostrophes + 264 quote pairs); still-live corruption the deepening didn't touch | safe in-place script pass |

| 2026-06-25 | /commercial-real-estate-loans/articles/commercial-real-estate-loan-calculator/ **(NEW)** | **Build** — "commercial real estate loan calculator" (14,800/mo, **diff 8–10**) | greenfield (cannibalization-checked: no existing CRE calc page, Axiant ranked for zero of these); built a full **payment + balloon calculator** (AIO-resistant tool) + amortization/DSCR/rates content + FAQ + 4 schema blocks; placed in the CRE cluster (`articles/` depth so relative paths hold), interlinked from the high-traffic down-payment page + sitemap | net-new substantive page | clean | first Build-phase page; "business loan calculator" was DROPPED from the build list (existing `business-loan-calculator-guide/` already owns it — optimize, don't duplicate) |

| 2026-06-25 | /construction-business-financing.html | **Build→Optimize** — "construction financing" (22,200/mo, diff 15) | cannibalization check found an existing hub (pos 19, 58 impr, 0 clicks) → **optimize, don't build**; retargeted title/H1/meta/og/subhead to "Construction Financing **for Contractors**" — captures the bigger term, disambiguates from construction *loans*, keeps "construction business financing"; freshness | hub already strong (739 lines, **17 cluster links**) | clean | 2nd Build item became an optimize — same lesson as the business-loan calculator |

| 2026-06-25 | /business-loan-calculator-guide/ | **Build→Optimize** — "business loan calculator" (18,100/mo) | already strong & on page 1 (pos 5.28, 697 impr, **0 clicks**) → **win the click**: title/meta now lead with the factor-rate-to-APR + total-cost angle an AI Overview can't reproduce; freshness | already strong (working calc, amortization/factor-rate/total-cost math) | clean | 3rd Build item = optimize; CTR fix on a page that already ranks |

| 2026-06-25 | /corporate-and-asset-finance.html **(NEW)** | **Build** — "corporate and asset finance" (33,100/mo, **difficulty 0 / refDomains 10**) — the #1 Growth-tab rec | verified before building: US-relevant (Swoop's *US* page ranks #18), greenfield (no asset-finance hub; equipment-financing is equipment-only, ABL is a buried article). Built an **umbrella pillar** — hub→spoke to equipment / ABL / working-capital / CRE — with a front-loaded citable answer to win the AI Overview, and funnels to the commercial spokes since the term is informational/low-CPC. FAQ + 4 schema blocks; inbound link from the equipment hub; sitemap | focused pillar, **426 lines** (not bloated — the construction template was 739) | clean | quality-not-quantity: verify intent/geo + cannibalization first; handle informational intent by being the AIO source + routing to money pages |

| 2026-08-01 | /fix-and-flip/articles/fix-and-flip-loan-first-time-flippers/ **(MERGE)** | **Consolidate + retarget** — two pages split one intent: `fix-and-flip-first-time-investors` (2,008 words) and this one (1,606), both self-canonical, 71% title/H1 token overlap. GSC 2026-06-03: pos 5.5 and 6.1 on the same query space, 49 combined impr, **0 clicks**. Survivor chosen on data — more impr (35 v 14), more inbound links (8 v 5), still in the 06-18 export | **DataForSEO killed both existing targets**: neither "first-time investors" nor "first-time flippers" has measurable volume; `fix and flip loans for beginners` = **320/mo, KD 0, CPC $23.61** → retargeted title/H1/meta/og/tw/schema to "beginners", kept investor/flipper wording as secondary in FAQ + schema keywords | folded 4 unique sections from the retired page (project selection, rates/costs, track record, alternatives); 1,606 → 1,979 words | clean | 301s + rationale in `_redirects`; hub card removed, ItemList renumbered 11→10, contextual link repointed, sitemap entry dropped, dir deleted |
| 2026-08-01 | /commercial-real-estate-loans/articles/commercial-real-estate-loan-calculator/ | **Optimize (vocabulary)** — page existed and earned **0 clicks**. Cluster is ~40k/mo at **KD 9–13**: `commercial real estate loan calculator` 14,800/KD13 (owned, 0.89), `commercial property loan calculator` 14,800/KD10 (0.64), `commercial mortgage calculator` 9,900/**KD9** (0.55) | **SERP-verified one page, not four**: live top-10 overlap 8/10, 8/10, 9/10 across the three phrasings, same top 3 in the same order → single intent. Title now leads with the unowned KD-9 "commercial mortgage calculator"; H1 keeps exact-match CRE phrasing; new H2 + 3 FAQs carry property/mortgage-loan variants and `calculate commercial mortgage payment` (210/KD9), `25-year commercial mortgage calculator` (170/KD9) | +terminology H2, +3 FAQs mirrored in FAQPage JSON-LD (8 visible = 8 schema) | clean | **rule: split on distinct calculation or distinct SERP, never on distinct phrasing.** Lendio ranks one `commercial-mortgage-calculator` URL top-5 for all three — proof the single-page play works |

| 2026-08-01 | /commercial-real-estate-loans/articles/sba-504-vs-conventional-commercial-real-estate-loan/ **(MERGE)** | **Consolidate** — duplicate of `/sba-loans/articles/sba-504-vs-conventional-cre` (1,329 words). GSC 2026-06-03: **42 impressions v 3**, and 28 inbound internal links v 12 → CRE-cluster page survives despite both being similar length | already aligned | folded in the retired page's **two worked dollar examples** ($2M 50/40/10 structure split; $1.5M cost comparison showing conventional is ~$455/mo cheaper but costs $225K more equity, ≈$22.5K/yr at a 10% return). Survivor had **no worked example** — playbook asks for one | removed "prefer a streamlined process" → "prefer a faster close with fewer parties"; synced og/twitter title+desc (all four were mismatched pre-existing) | retired page repeated itself: "When SBA 504 Wins" / "When Conventional Wins" / "When Each Option Wins". 11 files repointed across **three** link encodings — plain `href="…"`, JSON-LD `href=\"…\"`, and HTML-entity `&lt;a href=&quot;…&quot;&gt;`. Careful: survivor's own TOC anchor `#quick-comparison-sba-504-vs-conventional-**cre**-loan` contains the dead slug — must not be caught by a blind find/replace |
| 2026-08-01 | /sba-loans/articles/sba-504-lenders/ **(NEW)** | **Build** — `sba 504 lender` **8,100/mo, KD 19, CPC $19.36**; closest existing page was `sba-loans-blog.html`, a thin index (0.57 match) → genuine greenfield gap. Cluster context: 504 pages rank **position 52–67** on ~400 monthly impressions | title/H1/meta/schema all lead with "SBA 504 lenders"; secondary `sba 504 lenders/lending`, `sba 504 loan lender` (260/mo) | 1,792 words. Differentiator competitors miss: **a 504 has two lenders, not one** (bank ~50% first + CDC ~40% second + ~10% injection; 15% if startup *or* special-use, 20% if both). Structure table, 51%/60% occupancy gate, 1.20–1.35x DSCR, ~200+ CDCs by territory, job-creation benchmark ($75K/job, $120K small mfr), $5M/$5.5M caps, ~1.5% CDC processing fee, 60–90 day close, decline reasons | clean | key insight for the cluster: CDC pricing is standardized off the debenture, so **all shopping leverage is on the bank half** — that framing is the page's reason to exist |
| 2026-08-01 | /commercial-real-estate-loans/articles/commercial-mortgage-broker/ **(NEW)** | **Build** — `commercial mortgage broker` **1,600/mo, KD 0, CPC $37.27**; also `brokers`/`brokerage`/`agent` (same volume), `commercial mortgage lender(s)` 1,300/KD 10/**CPC $39.47**, `broker near me` 90/KD 1. Difficulty zero at ~$38 CPC — best value-to-effort ratio in the whole analysis, and no page existed | exact-match title/H1; variants in H2s + FAQ | 1,317 words. Leads with the **honest** answer (broker fees 0.5–2%, scaling down with loan size; go direct when the bank already wants the deal) — a go-direct table, the six lender types with what each is actually good at, vetting questions, and red flags | clean | commercial-intent page that argues *against itself* where true; that's the credibility play on a query where every competitor is selling |

> **Consolidation pattern:** when two pages split one intent, pick the survivor on GSC impressions + inbound links (not word count), then re-check the target query with DataForSEO before keeping either page's original wording — both may be aimed at phrasings nobody searches.

> **Build-phase pattern:** before building any "pillar," check for an existing hub. Two of three Build targets (business-loan calculator, construction financing) already had pages → optimize, don't duplicate. Only build truly greenfield gaps (the CRE calculator).

> **Key learning:** the worst-*scored* articles are actually substantive — the "AI sound" is a thin layer of stock phrases over good content, so the dominant fix is **surgical de-cliché**, not rewriting. And the detector **over-flags legitimate financial vocabulary** — "leverage" (financial leverage), "utilization" (equipment utilization), and natural "not only X" comparisons are NOT clichés. Across the 6 worst-scored articles the *real* fluff was ~8 phrase swaps total. Recalibrate the detector to exclude finance terms before trusting the count, and always verify by reading. Reserve full rebuilds for pages genuinely thin/off-target.
