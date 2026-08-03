# Site audit part 2 — hub architecture and internal linking

Part 2 of 5. Scope: can a crawler walk to every page, and does the hub
structure hold. Built the real internal link graph, resolving relative hrefs,
directory indexes and the 539-rule redirect table, then breadth-first from the
homepage.


## The finding: three isolated islands

**24 indexable pages were unreachable from the homepage by any internal link.**
They were not orphans &mdash; they linked each other heavily. They were islands
with no bridge from the main site, discoverable only via `sitemap.xml` and
receiving no internal link equity at all.


| Island | Pages | Inbound links | From outside the island |
|---|---|---|---|
| State pages (CA, TX, FL, NY, IL, PA, GA, NC, Atlanta) | 9 | 5&ndash;7 each | **0** |
| Loan-amount pages ($25K, $150K, $2M, $5M) | 4 | 3 each | **0** |
| `business-growth` hub + articles | 9 | 24 to the hub | **0** |

`business-growth/articles/index.html` had **24 inbound links and was still
unreachable** &mdash; every one of them came from inside its own island.


## Why each was stranded

- **Amount pages.** `how-much-can-i-borrow-business-loan.html` is the hub for
  this family and links 5 of the 9. The other 4 were never added.
- **State pages.** Nine pages, and not one link into them from anywhere else on
  the site.
- **business-growth.** A 14th topic hub that `blog.html` never listed. The whole
  section hung off a page nothing linked to.


## Fixed &mdash; four link additions, 22 pages recovered

Each completes an existing pattern rather than inventing a new one:


| Change | Effect |
|---|---|
| `services.html` &rarr; 4 missing amount pages added to *By loan amount* | bridges the amount island |
| `services.html` &rarr; new *By state* group, 9 links | bridges the state island |
| `how-much-can-i-borrow` &rarr; the same 4 amounts | completes the family hub |
| `blog.html` &rarr; business-growth hub card (14th) | bridges the growth island |

## Hub coverage: 14 of 15 hubs were already perfect

Every article hub was checked against the children on disk, excluding `noindex`
pages and children that canonicalise elsewhere:


| Hub | Children | Gap |
|---|---|---|
| `equipment-financing/articles/` | 97 | 0 |
| `sba-loans/articles/` | 48 | 0 |
| `working-capital-loans/articles/` | 45 | 0 |
| `commercial-real-estate-loans/articles/` | 33 | 0 |
| &hellip;11 more | | 0 |
| **`articles/`** | 47 | **6** |

The root `articles/` hub listed 40 of 47. Six real children were missing and
have been added; the seventh canonicalises to another article and is correctly
left unlinked.


## Result


| | Before | After |
|---|---|---|
| Unreachable indexable pages | **24** | **1** |
| True orphans (0 inbound) | 2 | 0 |
| Near-orphans (1 inbound) | 5 | 3 |
| Deepest page | depth 5 | depth 4 |

The single remaining unreachable page is
`articles/business-loan-denied-what-to-do/`, which canonicalises to
`/articles/what-to-do-if-business-loan-denied/` and is excluded from the
sitemap. Unlinked is the correct state for it.


## Context worth carrying to part 3

74 pages in total are unreachable; 50 of them are deliberately `noindex`,
mostly the `business-growth` article set. They cost crawl budget but not
indexing. Median inbound links across indexable pages is 6; the maximum is
5,621, which is the site-wide navigation.

