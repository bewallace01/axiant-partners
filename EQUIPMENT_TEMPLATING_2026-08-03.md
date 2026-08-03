# Equipment category templating — what it actually is

Follow-up to part 4, which reported 42 templated `equipment/` pages and
recommended rewriting them. Measuring properly before writing anything changed
the number, the diagnosis and the recommendation.


## It is 21 pages, not 42

Pages sharing 20+ identical sentences with each other:


| | Pages | Median length |
|---|---|---|
| Templated cluster | **21** | 2,252&ndash;3,382 words |
| Everything else in `equipment/` | 35 | ~1,334 words |

The cluster is the construction and truck categories &mdash; excavators,
bulldozers, skid-steers, backhoes, semi-trucks, dump-trucks and so on. Each shares
20+ sentences with 16 or 17 siblings.


The part-4 figure of 42 counted every page that appeared in any heavy pair,
including single links into the cluster. 21 is the set that genuinely shares copy.


## What is shared is process copy, not machine copy

`mini-excavators` and `skid-steers`, measured directly: **90 identical sentences,
1,171 shared words, 44% of each page**. All of it generic:


> "Typical requirements: 3-6 months of business bank statements, tax returns..."

> "The best time to apply is before you need the equipment..."

> "Equipment quote or proposal - Written quote from your dealer with make, model..."


The machine-specific halves are genuinely distinct. `bulldozers` explains crawler
versus wheel dozers and prices them $80,000&ndash;$500,000+ tiered by size;
`mini-excavators` does its own thing. Nobody templated the part that matters.


## Why the obvious fix is wrong

The instinct is to strip the shared process sections and link to the canonical
`equipment-financing-requirements` article. **The 35 non-templated pages have the
same 17 sections.** `tractors` and `combines` carry *Requirements to Finance*,
*What to Have Ready*, *Tips to Get Approved* and the rest &mdash; they are simply
written more concisely, at ~1,500 words rather than ~2,700.


So removing those sections from 21 pages would make them structurally different
from the other 35, which is a worse kind of inconsistency than the one it fixes.
Matching the concise style instead means rewriting roughly **24,600 words** of
lending copy.


## And the evidence that templating is the constraint is weak

| Page | Templated | Impressions | Position |
|---|---|---|---|
| `equipment/mini-excavators/` | yes | 776 | **17** |
| `tractor financing` (non-templated page) | no | 238 | **76** |

The templated page outperforms the non-templated one by a wide margin. Part 5
established the binding constraint on this section: every genuinely commercial
query on the site sits at position 10 or worse, and the site converts at
3&ndash;20% when it reaches the top ten. That is link authority. Rewriting 24,600
words of process copy does not touch it.


**Recommendation: do not do the bulk rewrite.** If any of these pages is worth
individual attention, pick it from Search Console demand rather than from a
duplication score.


## One real defect found on the way

`scripts/equipment_specific_content.json` is **stale, and dangerous to regenerate
from**. Every cost range checked disagrees with the published page, and the page
is the better of the two:


| Machine | Data file | Live page |
|---|---|---|
| bulldozers | $100K&ndash;$600K+ | **$80,000&ndash;$500,000+**, tiered $80&ndash;150K compact, $150&ndash;300K mid |
| backhoes | $40K&ndash;$120K | **$50,000&ndash;$180,000+**, tiered |
| mini-excavators | $30K&ndash;$80K | $25,000&ndash;$100,000+ |
| skid-steers | $25K&ndash;$70K | $25,000&ndash;$75,000+ |
| semi-trucks | $100K&ndash;$200K+ | $100,000&ndash;$270,000+ |

The pages were edited after the file was written. Anyone regenerating from it
would replace current tiered figures with older flat ones across 53 machines. The
file now carries a `_WARNING` key recording this; it is still valid JSON and still
useful for the machine list and related-equipment mapping.


## Method note

Three measurements in this pass were wrong before they were right:


- A check for whether machine-specific content had been "applied" compared the
  first nine words of a JSON field against the page. It reported 39 of 53 pages
  missing their content. The content is there &mdash; adapted, not pasted.
- A per-section duplication table normalised section names by deleting the machine
  name, which produced two different keys for the same section and unusable
  percentages.
- A family-wide boilerplate scan found exactly one shared sentence across 56 pages
  and concluded there was no templating, because the templated set is 21 pages and
  a 50% threshold across 56 hid it.


The number that survived all three is the direct one: 90 identical sentences
between two named pages, counted by hand.

