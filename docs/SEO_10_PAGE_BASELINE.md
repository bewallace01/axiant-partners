# 10-Page SEO/GEO/AEO Baseline (Implementation Order)

This document captures the exact optimization sequence used for the current 10-page batch so future batches can follow the same process consistently.

## Scope (Current 10 Pages)

- `equipment/semi-trucks/how-to-finance-a-semi-truck/index.html`
- `equipment-financing/articles/equipment-financing-requirements/index.html`
- `commercial-real-estate-loans/articles/cash-out-refinance-commercial-property/index.html`
- `business-line-of-credit/articles/what-are-typical-business-line-of-credit-rates/index.html`
- `commercial-bridge-loans.html`
- `equipment/diagnostic-equipment-auto/scan-tool-financing/index.html`
- `trucking-business-financing.html`
- `construction-business-financing/progress-payment-cash-flow-gaps/index.html`
- `revenue-based-financing/articles/revenue-based-financing-traps/index.html`
- `sba-loans/articles/sba-loan-restaurant-acquisition/index.html`

## Implementation Order (Repeat This Per Batch)

1. **SERP snippet optimization**
   - Rewrite `title`, `meta description`, `og:title`, `og:description`, `twitter:title`, `twitter:description`.
   - Keep one clear intent per page (no mixed-intent titles).

2. **Answer-first content insertion**
   - Add a concise in-body `Quick Answer` near top of main content.
   - Make this summary intent-specific and snippet-friendly.

3. **FAQ enrichment (visible content)**
   - Add targeted `FAQ Quick Hits` in visible body content.
   - Add 2 intent-specific Q&As that answer likely high-impression query variants.

4. **FAQ schema synchronization**
   - Add matching `FAQPage` JSON-LD entries for newly added questions.
   - Keep schema wording aligned with visible page content.

5. **Internal link and conversion path pass**
   - Tighten contextual internal links to relevant adjacent pages.
   - Add one high-context conversion link to `/match.html` in top answer area.
   - Avoid repetitive anchor stuffing.

6. **Depth expansion for sub-2k pages**
   - Add a unique long-form section per page (playbook/framework/checklist).
   - Expand with non-overlapping intent so pages do not cannibalize one another.

7. **Quality checks**
   - Lint pass on all edited files.
   - Confirm changed files and ensure no unrelated modifications are reverted.

8. **Word-count compliance and reinforcement**
   - Measure visible page words (exclude `script/style/noscript`) to validate content depth.
   - If below target, add high-signal reinforcement blocks (not filler), such as:
     - mini case studies
     - scenario comparisons
     - implementation checklists
     - decision frameworks
   - Re-count and iterate until threshold is met.

## Anti-Cannibalization Rules Used

- Keep each page tied to one primary search intent.
- Add page-specific expansion themes:
  - underwriting playbook
  - documentation pathways
  - proceeds strategy
  - pricing framework
  - operational ROI policy
  - draw-cycle execution
  - exit strategy playbook
  - acquisition diligence/transition
- Link to related pages for adjacent intents instead of repeating full sections.
- Keep headings and FAQ language distinct across sibling topics.
- Add reinforcement content that is page-native (no cross-page copy blocks).
- Case study sections must be unique by context, metrics, and operational lesson.

## Batch QA Checklist

- [x] Titles/descriptions updated and unique
- [x] In-body Quick Answer exists
- [x] FAQ Quick Hits section exists
- [x] FAQ schema added/updated
- [x] Contextual internal links improved
- [x] Conversion link to `/match.html` included contextually
- [x] Sub-2k pages expanded with unique topical depth
- [x] Lint clean
- [x] Visible word-count audit completed
- [x] Reinforcement blocks added where needed

## Word Count Baseline (Visible Content)

Word counts were measured from visible HTML text (excluding script/style/noscript blocks) after this implementation pass:

- `equipment/semi-trucks/how-to-finance-a-semi-truck/index.html`: 2019
- `equipment-financing/articles/equipment-financing-requirements/index.html`: 2014
- `commercial-real-estate-loans/articles/cash-out-refinance-commercial-property/index.html`: 2020
- `business-line-of-credit/articles/what-are-typical-business-line-of-credit-rates/index.html`: 2010
- `commercial-bridge-loans.html`: 2493
- `equipment/diagnostic-equipment-auto/scan-tool-financing/index.html`: 2017
- `trucking-business-financing.html`: 3235
- `construction-business-financing/progress-payment-cash-flow-gaps/index.html`: 2565
- `revenue-based-financing/articles/revenue-based-financing-traps/index.html`: 2011
- `sba-loans/articles/sba-loan-restaurant-acquisition/index.html`: 2024

## What Was Implemented On This Batch

This batch included all of the following end-to-end steps:

1. **SERP layer**
   - Rewrote title/meta/OG/Twitter snippets for CTR and query-intent alignment.

2. **Answer-engine layer**
   - Added in-body quick-answer content near top of main content.
   - Added FAQ Quick Hits in visible body content.
   - Added matching FAQ JSON-LD entries for new Q&As.

3. **Internal link layer**
   - Strengthened contextual internal links to adjacent intent pages.
   - Added conversion path links to `/match.html` in high-intent contexts.

4. **Depth layer**
   - Expanded page-specific sections with non-overlapping operational content.
   - Used unique frameworks/checklists/playbooks per page to avoid cannibalization.

5. **Compliance layer**
   - Ran visible word-count audit and iterated until threshold targets were met.
   - Ran lint verification after edits.

## Reinforcement Content Guidelines (For Future Batches)

When a page needs additional depth, use one or two of these section types:

- **Mini case study:** short scenario with starting condition, decision, and result.
- **Decision framework:** how to choose between 2-3 financing structures.
- **Execution checklist:** practical first 30/60/90-day steps.
- **Risk controls:** specific mistakes and preventive controls.

Rules:

- Keep every reinforcement section tied to the page's primary intent.
- Do not duplicate examples from sibling pages.
- Avoid generic statements without operational detail.

## Notes for Next 10-Page Batch

- Prioritize pages by: high impressions, position 4-20, low CTR.
- Apply this same order end-to-end before moving to the next set.
- Re-check Search Console after 10-14 days, then iterate titles/FAQs based on actual query movement.
