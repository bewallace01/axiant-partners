# Overnight Build Plan — 2026-08-01

Written to be executed autonomously. Every item below is fully specified: target keywords with
volume and difficulty, cannibalization check, required page furniture, and the audit that must
pass before the work is committed.

---

## Standing rules — apply to every task, no exceptions

**Boundary: build and open PRs. Do not merge anything.** Merging deploys to the live site.
Everything waits for review in the morning.

**Per-page requirements.** A page is not done until all of these hold:

| Requirement | Standard |
|---|---|
| Title | 45–65 chars, exact-match primary keyword |
| Meta description | 120–155 chars, and `og:`/`twitter:` synced to title + description |
| H1 | Exactly one, carrying the target phrasing |
| AEO lead | First 40–60 words answer the query and carry a citable number |
| Word count | ≥1,200, with real substance — numbers, mechanisms, worked examples |
| FAQ | Visible FAQ, mirrored 1:1 in `FAQPage` JSON-LD. **Count must match exactly.** |
| Breadcrumb | Visible `nav.crumbs` **and** `BreadcrumbList` schema, leaf names identical |
| Internal links | Links up to the hub, sideways to 2+ siblings, and to one money page |
| Related Resources | Block present, 5–6 links |
| Freshness | `dateModified` and any visible "Updated" date set to build date |
| Sitemap | Entry added with correct priority |
| Voice | Zero banned phrases, zero AI-tell structures, sentence stdev ≥ 6 |

**Cannibalization gate — run before writing, not after.** For each new page, compute title/H1
token Jaccard against every existing page. **≥0.45 means stop and resolve** — either retarget
the new page or move the competing section onto it, as was done with the "Top DSCR Lenders"
section. Three duplicate pairs have already suppressed clusters on this site; a fourth is not
acceptable.

**Verification per page, in this order:**
1. `python qa.py` — 0 hard fails. *Known false positive on root pages: "links to a sibling
   article" checks for `../` paths, which root pages do not use. Ignore that one only.*
2. `python voice_audit.py` — no banned phrases, no AI-tell structures
3. FAQ visible count == schema count; every visible question present in schema
4. All JSON-LD parses
5. Serve locally and verify every internal link returns 200
6. `npm run audit` — broken:0 thin:0 filler:0
7. **Confirm the file ends with `</html>` and nothing follows it.** An insertion anchor has
   misfired three times on this site, once dumping 2,051 characters after `</html>`.

**Accuracy rules.** Every number published must be verifiable. Worked examples must reproduce
in the on-page calculator if one exists. Do not publish competitor pricing or loan ranges that
go stale — describe qualitatively and tell the reader to confirm. Hedge where lender practice
varies.

**Keyword rule.** Verify every target against DataForSEO before building. Several GSC-visible
queries in this account are AI Overview fan-out with zero human volume — impressions alone do
not justify a page.

---

## Status at handoff

| PR | Item | State |
|---|---|---|
| #154 | DSCR cluster plan | open |
| #155 | Phase 1.1 — calculator expanded 606 → 1,679 words | open |
| #156 | Phase 1.2 — `/dscr-loans.html` hub | open |
| #157 | Phase 2.3 — `/dscr-lenders.html` (stacked on #156) | open |

Branch to continue from: `seo/dscr-lenders`. Each new task branches from the previous one and
stacks, so links between new pages resolve during verification.

---

## Task 1 — DSCR loan requirements page

**Branch:** `seo/dscr-requirements` from `seo/dscr-lenders` · **File:** `/dscr-loan-requirements.html`

**Targets (verified):** `dscr loan requirements` 2,900/mo KD 10 · `dscr loan requirement`
2,900 KD 10 · `dscr loans requirements` 2,900 KD 10 · CPC $11.76

**Cannibalization:** the hub has a requirements *table*; this page goes deep on each item. Before
building, check overlap against `/dscr-loans.html`. If ≥0.45, retitle toward
"DSCR Loan Requirements: Credit, Down Payment and Reserves" and trim the hub's table to a
summary that links here.

**Substance to cover:** credit score tiers and what each unlocks; down payment by scenario;
reserve requirements including why cash-out needs more; the appraisal and Form 1007 rent
schedule; entity and guarantor requirements; seasoning; property-type limits including
non-warrantable condos and rural acreage; what documentation is actually collected given no
income docs. Include one worked qualification walkthrough.

---

## Task 2 — DSCR loan rates page

**Branch:** `seo/dscr-rates` from Task 1 · **File:** `/dscr-loan-rates.html`

**Targets (verified):** `dscr loan rates` 3,600/mo KD 6 · `dscr loan rate` 3,600 KD 0 ·
`dscr loans rates` 3,600 KD 3 · CPC $13.26

**Cannibalization:** check against `/dscr-loans.html` (has a costs section) and
`commercial-refinance-rates-2026`. The hub covers cost *structure*; this page covers *pricing
and what moves it*.

**Substance:** what drives DSCR pricing — ratio tier, LTV, credit, property type, STR vs
long-term, prepay election; the spread over conventional and why it exists; points vs rate
trade-off; rate buydowns; prepayment buy-down pricing; a worked comparison of the same deal at
1.05x vs 1.30x. **Do not publish a specific rate table** — it dates immediately and this site
should not be quoting live pricing. Use relationships and spreads.

---

## Task 3 — "What is a DSCR loan" — decision, not automatic build

**Targets:** `dscr loan mean` / `means` / `meaning` / `dscr loans meaning` 8,100/mo KD 27 ·
`what is a dscr loan` 6,600 KD 13 (already targeted by the hub)

**Do this first:** the hub already answers "what is a DSCR loan" in its quick answer and opening
section. Compute overlap. **If the hub covers it well, do not build a separate page** — instead
strengthen the hub's definitional section and add the `meaning`/`means` phrasings to its FAQ.
Record the decision either way in the playbook fix log.

If a separate page is genuinely warranted, it is definitional and low-CPC ($4.25) — build it for
citation and internal linking, not conversion, and link it up to the hub.

---

## Task 4 — Geo pilot: Texas and Florida only

**Branch:** `seo/dscr-geo-pilot` · **Files:** `/dscr-loan-texas.html`, `/dscr-loan-florida.html`

**Targets:** `dscr loan texas` 1,300/mo KD 0 CPC $20.03 · `dscr loan florida` 1,300 KD 0
CPC $19.48 (plus `dscr loans texas` / `dscr loans florida`, same volume)

**Build only these two. Do not build additional states overnight.** The full set is 43 states,
and 43 near-identical pages would likely not index at all — the thin ones become a
site-wide quality signal. Texas and Florida are a pilot to be measured over 6 weeks.

**Each page must clear this bar or it does not ship:**
- State LLC treatment and whether title can be held in an entity without due-on-sale friction
- Transfer/recordation tax and typical closing costs in that state
- Rent-to-price ratios for 2–3 named metros (TX: Houston, San Antonio, DFW · FL: Tampa,
  Jacksonville, Orlando) and the DSCR those produce at current rates
- Judicial vs non-judicial foreclosure and why DSCR lenders price for it
  (**TX non-judicial and fast; FL judicial and slow — this is a real pricing difference**)
- The local condition that actually moves the maths: **FL wind/hurricane insurance**, which can
  swing NOI by thousands and is the single most important DSCR factor in that state;
  **TX property tax**, among the highest in the country and equally decisive

If a page cannot say something specific and true under each heading, do not ship it. A templated
page with the state name swapped is worse than no page.

---

## Task 5 — Equipment cluster: the position-10 pages

**Branch:** `seo/equipment-ctr` · Edits to existing pages, no new pages.

These already rank on page 1–2 with real demand and earn almost nothing. All KD 0.

| Page | Target | Vol | Position |
|---|---|---|---|
| `equipment-financing/articles/vending-machine-financing/` | `vending machine financing` / `finance vending machine` | **1,300** | 10.5–11.4 |
| `working-capital-loans/articles/security-guard-company-working-capital/` | `security guard payroll financing` | **880** | 10.5–11.2 |
| `equipment-financing/articles/carecredit-vs-patientfi-imaging-radiology/` | `patientfi vs carecredit` | 170 | 8.6 |
| `equipment/stump-grinders/` | `stump grinder financing` | 50 | 13.3 |

**This is a CTR and vocabulary job, not a rewrite.** For each: confirm the exact-match keyword is
in the title, tighten the title to earn the click, verify the AEO lead answers the query with a
number, sync `og:`/`twitter:`, add breadcrumbs if missing, and confirm FAQ/schema parity.

The security guard page is the standout — **1,181 impressions at position 11 with zero clicks**.

**Do not** target `electrical contractor funding`, `imaging patient financing`, or
`radiology patient financing`. Despite 358/261/188 impressions they have **no real search
volume** — AI Overview fan-out.

---

## Task 6 — Site-wide audit sweep and report

**Branch:** `seo/audit-sweep-2026-08-01`

Run across all pages and fix what is mechanical and safe:

1. **FAQ schema violations.** The DSCR calculator had six schema entries of which three were not
   FAQs — a CTA heading, a body fragment, and an H2. Scan every page with `FAQPage` schema and
   report any where schema entries do not correspond to visible questions. Fix where
   unambiguous; report where judgement is needed.
2. **Duplicate FAQ sections.** Both `dscr-rental-loans-real-estate-investors` and
   `dscr-loan-vs-conventional-mortgage` have **two** "Frequently Asked Questions" H2 blocks.
   Find all instances site-wide and merge.
3. **Cannibalization scan.** Run the title/H1 Jaccard check across all pages at ≥0.45 and report
   every pair. Do not merge anything autonomously — three merges have already been done and each
   needed a judgement call on which page survives. **Report only.**
4. **Breadcrumb coverage.** Report which pages have `BreadcrumbList` schema but no visible
   breadcrumb, and any where the schema leaf does not match the visible leaf.
5. **Orphan check.** Report pages in the sitemap with fewer than two inbound internal links.

Write findings to `SITE_AUDIT_FINDINGS_2026-08-01.md` and open a PR.

---

## Morning review order

1. **#155** calculator — smallest diff, fixes a real structured-data violation
2. **#156** hub — the cluster anchor
3. **#157** lenders — stacked on #156
4. Then whatever overnight tasks completed, in the order above

Each PR body states what was built, what was verified, and any judgement calls made. Anything
that could not be completed safely will say so explicitly rather than being silently skipped.

---

## What will not be done autonomously

- **No merging.** Every change waits for review.
- **No merging of duplicate pages found in Task 6.** Choosing which page survives needs GSC
  impressions, inbound link counts, and a judgement call. Reported, not actioned.
- **No additional geo pages beyond Texas and Florida.**
- **No global nav changes.** Adding DSCR to the nav would touch all 836 pages and is a design
  decision.
- **No link building or outreach.**
- **Nothing requiring a business answer** — lender relationships, pricing, funding capability.
  If a task needs one, it stops and reports.
