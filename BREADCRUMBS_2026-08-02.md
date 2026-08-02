# Breadcrumbs — what was rendered, and what was found on the way

Audit finding #4: 710 pages emitting `BreadcrumbList` structured data while showing
the reader nothing. Measured on the current branch it was **688** — the DSCR and
equipment work had already covered the rest.


## What changed

| | pages |
|---|---|
| Visible breadcrumb rendered (trail of 3+) | 598 |
| Two-level schema removed instead of rendered | 90 |
| Breadcrumbs moved out of the site header | 8 |
| Trails repaired before rendering | 9 |
| Pre-existing name mismatches synced | 5 |

One self-contained inline-styled `nav.crumbs` is used everywhere, so no page
depends on CSS it may not carry. `--text-secondary` is defined in the critical CSS
inlined on every page. Placement is per template, always after the site navigation:


- `main.blog-post-main` → immediately inside the opening tag (524 pages)
- `div.ef-page-wrap` → immediately before it, matching the existing `ef-breadcrumb` pages
- otherwise `<main>`, else after `</header>`


## Two-level trails were dropped, not drawn

90 pages had a trail of exactly `Home > This Page`. Google returns no rich result
for a single-level breadcrumb, and 65 of the 90 are root money pages where the line
would sit directly above the hero CTA. Removing the schema makes them compliant
with no visual change.


## Defects found while doing it


### 1. Eight breadcrumbs were rendering above the site navigation

The markup had been inserted inside the header container, so it drew above the nav
bar rather than below it. Six are the DSCR pages built overnight, plus
`equipment/stump-grinders/` and `real-estate-secured-business-loan.html`. All eight
are in PRs that have not merged yet, and all eight are now moved.


### 2. `startup-financing/articles/` does not exist

Six breadcrumbs linked to that hub. The directory holds 8 articles and **no
`index.html`**, so the link 404s — it is the only cluster on the site missing its
articles index. Those crumbs now point at `/startup-financing.html`. **The hub
itself still needs building**; every other cluster has one.


### 3. Three trails read `Home > Articles > Articles`

`business-loan-approval-timeline-by-lender-type`, `business-loan-denied-what-to-do`
and `how-to-compare-business-loan-offers` each repeated the same crumb. Rendering
them verbatim would have put the duplicate on the page. Deduped in both the visible
trail and the schema.


### 4. Five trails where the schema never matched the visible breadcrumb

On pages that already showed a breadcrumb, the schema leaf and the visible leaf
differed — schema `Business Loan to Pay the IRS or Back Taxes`, page `Business loan
to pay back taxes`. The page wins, same rule as the FAQ answer work.


## Verification

- 652 pages carry `BreadcrumbList`; **652** show a matching visible trail
- 0 breadcrumbs above the site nav, 0 schema without a visible trail, 0 visible
  trails whose names differ from the markup
- 0 breadcrumb links pointing at a page that does not exist
- All JSON-LD parses; nothing after `</html>`; tag balance unchanged from HEAD on
  all 700 changed files
- FAQ parity from the earlier PRs still holds
- `npm run audit`: 840 pages, `broken:0 thin:0 filler:0`

