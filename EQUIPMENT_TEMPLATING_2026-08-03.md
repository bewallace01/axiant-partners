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


## What was done instead (2026-08-03)

The recommendation above was overruled and the pages were fixed. Re-measuring
first changed the shape of the job twice.


**The cluster is 18 pages, not 21.** Counting pages that share 20+ verbatim
sentences with at least one sibling gives 25, but eight of those are hangers-on
with one to four connections. Eighteen pages share copy with 17 siblings each.


**Verbatim matching undercounted the template badly.** The template substitutes
the machine name inline &mdash; *&ldquo;Requirements to Finance a Backhoe&rdquo;*,
*&ldquo;when financing backhoes&rdquo;* &mdash; so sentences that are otherwise
identical do not match across the cluster. Normalising the machine name to a
placeholder raises the worst pair from 90 identical sentences to **116**, and
the median pair from 33 to **59**.


Attributed by section, the shared prose per pair sat at: FAQ 121 words,
Requirements 99, What to Have Ready 81, Process 77, Options 69, Tips 59,
Rates 52, When to Apply 52, Common Mistakes 50.


### Four sections rewritten per machine

| | |
|---|---|
| What to Have Ready Before You Apply | 18 machine-specific document lists |
| When to Apply | 18 machine-specific timing arguments |
| Tips to Get Approved | 18 machine-specific tip sets |
| Common Mistakes to Avoid | 18 machine-specific mistake lists |


These are the four where a different answer genuinely exists. A bucket truck
needs a current dielectric test certificate; a tanker needs its DOT
specification and its position in the test cycle; an excavator needs a measured
undercarriage percentage; a reefer has an hour meter independent of the truck's
odometer; a log truck needs the haul agreement and the seasonality stated
plainly. The shared copy said none of that on any of the eighteen pages.


Result: worst pair **116 &rarr; 87** normalised shared sentences, median
**59 &rarr; 43**. Pages grew 2,157&ndash;3,260 words to 2,250&ndash;3,425.


### What was deliberately left alone, and why

Requirements, Financing Options, Rates, the four process steps, Related
Resources and the FAQ still share copy. That copy is identical on the **other
75 equipment pages too** &mdash; *Rather Than Pay Cash* appears on 36 pages
across the family, the approval-time FAQ answer on every page checked. Removing
it from 18 pages would make the cluster the odd one out in its own family, which
is the failure this document originally warned about.


If that boilerplate is worth fixing it is a 93-page family-wide job, not a
cluster job, and it should be decided as one.


### Correction: the family is not verbose, only the cluster is

The paragraph above &mdash; and what I told the user &mdash; said the remaining
boilerplate was *&ldquo;identical on the other 75 equipment pages too&rdquo;*, so
removing it from 18 would make the cluster the odd one out. That was measured on
**headings**, not on the sections underneath them. Measuring the sections
reverses the conclusion:


| Section | Cluster median | Rest of family median |
|---|---|---|
| Requirements to Finance | 193 words | **39** |
| Financing Options | 214 | **120** |
| Rates and Monthly Payments | 112 | **36** |
| Rather Than Pay Cash | 119 | **51** |


`dental-equipment` and `pos-systems-restaurant` carry *Requirements* as a table
plus one line of links. `tractors` carries it as a single paragraph. Only the
cluster carries three paragraphs saying the same thing on all eighteen pages.


So bringing the cluster down to the family length makes it **consistent** with
its family, not different from it. That is the opposite of the risk this
document originally identified, and the original recommendation rested on it.


Applied to all 18: requirement tables kept with their own values, payment
examples kept with their own figures, term ranges and the TRAC-lease and SBA
*best for* clauses kept. What was removed is prose measured as identical across
the cluster. Worst pair **87 &rarr; 66** normalised shared sentences, median
**43 &rarr; 34**; pages 2,076&ndash;3,142 words.


Still shared, and deliberately: the four process steps (Axiant's own process,
identical everywhere because it is), the FAQ answers (universal facts &mdash;
rewriting them eighteen ways would be paraphrase-spinning, which is worse than
duplication), and the Related Resources link list.


### Separately: four pages with unclosed `<p>` tags

Found by the integrity sweep, present in HEAD, not caused by any of this work:
`used-box-truck-financing`, `used-dump-truck-financing`,
`used-mini-excavator-financing` and `used-skid-steer-financing` each had four or
five paragraphs never closed. Browsers auto-close at the next block tag so
nothing rendered wrong, but the markup was invalid. Closed.


### One defect introduced and caught before shipping

The first draft of the new copy used British spellings &mdash; *tyres*,
*aluminium*, *labour*, *mobilisation*, *authorised*, *favour*, *autumn*
&mdash; on pages addressed to U.S. contractors. 41 instances across the
equipment copy, plus 15 that had already shipped in the construction rewrite
(#214). All corrected; the equipment pages were reverted and regenerated rather
than patched in place.


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

