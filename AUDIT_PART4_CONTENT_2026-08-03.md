# Site audit part 4 — content quality and human voice

Part 4 of 5. Measured against the rendered body with navigation, script and
footer stripped, so shared chrome is never counted as duplicated content.


## The voice is genuinely good

This is the part I expected to find problems in and did not.


| Check | Result |
|---|---|
| Pages containing any AI-tell phrasing | **4 of 768** |
| Total AI-tell instances site-wide | **4** |
| Worst repeated sentence opener | 17.8%, and it is `Best for:` in a comparison list |
| Thin pages / filler (site audit) | **0 / 0** |

The tell list covered *it's important to note*, *in today's fast-paced
landscape*, *delve into*, *unlock the potential*, *plays a crucial role*, *in
conclusion*, *at the end of the day*, *game-changer*, *navigating the waters* and
six more. Four hits across 768 pages, one each. For a site of this size that is
a very low rate, and it reads as written rather than generated.


## The real defect: templating

**207 page pairs share 10 or more non-boilerplate sentences of 8+ words.**
85 of 753 content pages &mdash; **11%** &mdash; are involved.


Boilerplate was excluded first. Any sentence appearing on more than 12 pages is
treated as intentional site furniture and ignored:


| Repeated site-wide | Pages |
|---|---|
| "Get matched with lenders who fit your business." | 278 |
| "Tell us about your business and compare real options." | 126 |
| "Free, no obligation, and checking won't affect your credit." | 126 |

What remains is body copy that repeats between a handful of pages, which is a
different thing entirely.


### Worst cluster: three construction articles at ~62%

| Page | Words | Duplicated |
|---|---|---|
| `signs-contractor-overleveraged` | 1,532 | **62%** |
| `avoid-payment-delays-change-orders-contractor-checklist` | 1,550 | **62%** |
| `reasons-contractor-line-of-credit-reduced-or-frozen` | 1,559 | **61%** |

These three share **62 identical sentences with each other**, and their titles
and H1s are completely different. Sampled shared lines are substantive body copy,
not calls to action:


> "Lenders understand this pattern, but they still need evidence that your
> business manages timing risk..."

> "When the story is clear, underwriters can defend the approval internally."

> "Week one: organize documentation and reconcile reporting gaps."


Three different promises, one body. Google will pick one and discount the rest.


### By section

| Section | Pages involved |
|---|---|
| `equipment/` category pages | 42 |
| root-level pages | 27 |
| `business-growth/articles/` | 6 |
| `equipment-financing/articles/` | 5 |
| `construction-business-financing/` | 3 |

The `equipment/` family is the largest group: category pages built from a shared
skeleton, e.g. `mini-excavators` and `skid-steers` sharing 41 sentences,
`bulldozers` and `excavators` 41, `backhoes` and `wheel-loaders` 39. Individually
each reads fine; collectively they give Google 42 pages saying much the same
thing about different machines.


## Not fixed here, and why

Rewriting 85 pages of templated body copy is a writing project, not a script.
Roughly 2,900 words of genuinely new content would be needed for the construction
cluster alone, and every word of it makes claims about lending. Given how many
figures on this site turned out to disagree with each other earlier today, I am
not generating that volume unprompted.


Recommended order if you want it done:


1. **The construction triangle** &mdash; 3 pages, 62% duplicated, the clearest
   defect and the smallest fix.
2. **`equipment/` category pages** &mdash; 42 pages. The highest-value change is
   probably not rewriting all of them but making each carry something only that
   machine has: real spec ranges, real price bands, the financing wrinkle specific
   to that asset class.
3. **`business-growth/articles/`** &mdash; 4 pages at 34&ndash;38%. Note that 17
   pages in this section are already `noindex`, so the section is half-retired
   already; consider whether these four earn their place at all.


## Method note

The first pass reported the ten worst pages for repeated sentence openers, and
all ten were article hubs where every card ends "Read more". That is link text,
not prose. Excluding card links and hub pages moved the worst genuine result from
65% to 17.8%, which is normal writing. The finding would have been entirely
spurious.

