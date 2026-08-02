# Site Audit Findings — 2026-08-02

Task 6 of the overnight plan. **843 pages scanned.** Reporting only — nothing in this document
was auto-fixed, because every item needs a judgement call the plan reserved for you.

---

## 1. FAQ schema declaring questions that are not on the page — **102 pages, 193 phantom questions**

**This is the highest-priority finding.** Google requires `FAQPage` structured data to
correspond to content **visible on the page**. Where it does not, the markup is non-compliant
and can cost the rich result — or, at scale, trust in the site's markup generally.

Verified by hand, not just by script. On `1-million-business-loan.html` the schema declares
*"How long does a $1 million business loan take to fund?"* and that question appears **nowhere
in the visible text**. Same pattern across the `$25,000` through `$5 million` loan-amount pages,
typically 1–3 phantom questions each.

This is the same class of defect found on `dscr-calculator.html` during the DSCR work, where
three of six schema entries were a CTA heading, a body-copy fragment, and an H2. That one was
fixed. These 102 were not — the fix requires deciding per page whether to **add the question to
the page** or **remove it from the schema**, and those are different editorial choices.

**Recommendation:** rebuild each page's `FAQPage` block from its visible FAQ markup, the way
`dscr-calculator.html` was repaired. Mechanical once the decision rule is set; the decision rule
is yours.

---

## 2. Duplicate FAQ sections — **100 pages**

100 pages carry **two separate** `<h2>Frequently Asked Questions</h2>` blocks with different
questions covering overlapping ground.

Example — `business-term-loans/articles/term-loan-vs-bridge-loan/`:

- Block 1 (`id="frequently-asked-questions"`): *"What is the difference between a term loan and a bridge loan?"*
- Block 2 (`id="faq"`, `.article-faq`): *"What's the difference?"*

Both answer the same question with different wording and different detail. Spread across 11
top-level sections including business-term-loans, commercial-real-estate-loans,
equipment-financing, fix-and-flip and merchant-cash-advance.

**The plan said to merge these. On inspection, I did not** — the two blocks contain genuinely
different content, so merging means choosing which answers survive on 100 pages. That is
editorial judgement, not a mechanical pass, and auto-merging risked losing the better answer.

**Recommendation:** keep the block with fuller questions (usually block 1), fold any unique
answers from block 2 into it, delete block 2, then rebuild the schema from what remains — which
also resolves a large share of finding #1.

---

## 3. Cannibalization screen — **1,374 pairs at ≥0.45, but treat the number sceptically**

| Band | Pairs |
|---|---|
| 0.70–0.89 | **132** |
| 0.55–0.69 | 862 |
| 0.45–0.54 | 380 |

**The raw count overstates the problem.** This site uses a systematic naming convention, so
title-token overlap flags many pairs that are intentionally distinct — `equipment/excavators/`
versus `equipment/mini-excavators/` scores 0.86 but may be a deliberate split.

My first run was worse: it reported pairs at **1.00** between `1-million-business-loan.html`,
`2-million-business-loan.html` and `5-million-business-loan.html`, which was a **tokenizer
artifact** — the filter dropped tokens under four characters, so "1", "2" and "5" vanished and
all three reduced to `{million, business}`. Fixed before reporting. Mentioning it because it is
exactly the kind of number that would otherwise have been quoted as fact.

**Genuine candidates worth reviewing first (≥0.78):**

| Score | Pair |
|---|---|
| 0.88 | `equipment-financing/articles/equipment-financing-…` vs `heavy-equipment-financing` |
| 0.86 | `equipment/landscape-trailers/` vs `equipment/trailers/` |
| 0.86 | `equipment/excavators/` vs `equipment/mini-excavators/` |
| 0.86 | `equipment/diagnostic-devices-medical/` vs `equipment/diagnostic-equipment-auto/` |
| 0.83 | `business-debt-consolidation.html` vs `consolidate.html` |
| 0.80 | `equipment-for-sale/electric-material-handlers/` vs `material-handlers/` |
| 0.78 | three-way overlap among `affirm-vs-cherry`, `carecredit-vs-affirm`, `cherry-vs-carecredit` |

`business-debt-consolidation.html` vs `consolidate.html` at 0.83 looks like the clearest genuine
duplicate — two root pages on the same intent.

The patient-financing trio is interesting: three pages permuting the same three brands. GSC shows
`patientfi vs carecredit` at 170/mo and `cherry vs carecredit` at 86 impressions, so there is
real demand — but three pages splitting it is the same pattern that suppressed the SBA 504
cluster.

**No merges performed.** Choosing a survivor needs GSC impressions and inbound-link counts per
pair, exactly as the three completed merges did.

---

## 4. Breadcrumbs — **710 pages have schema but no visible breadcrumb**

Every one of those pages emits `BreadcrumbList` structured data while showing the user nothing.
Google's guidance is that breadcrumb markup should reflect a real on-page navigational element.

Only 34 pages had visible `nav.crumbs` before this cycle; the DSCR and equipment work added a
further 14. The remaining 710 are unchanged.

**Not fixed** because adding a visible breadcrumb to 710 pages is a design decision with layout
implications across several templates, not a mechanical edit. The pattern used on the pages I
did fix is available to copy.

**No leaf-name mismatches remain** — the four found earlier in this cycle were corrected.

---

## 5. Orphan pages — **130 in the sitemap with fewer than two inbound links**

- **51 pages with zero inbound internal links**
- 79 pages with exactly one

These are in the sitemap, so Google is invited to crawl them, but the site itself signals almost
no importance. Several are cluster index pages that ought to be well-linked —
`business-line-of-credit/index.html` and `business-term-loans/index.html` among them.

**Recommendation:** internal linking is the cheapest ranking lever available and requires no new
content. Prioritise the zero-inbound set, and check the cluster hubs first since those should be
structurally well-connected.

---

## What this adds up to

Findings 1, 2 and 4 are all the same underlying issue: **markup emitted programmatically without
verifying it matches the page**. FAQ schema without visible FAQs, duplicate FAQ blocks, and
breadcrumb schema without breadcrumbs are three symptoms of one habit.

That matters more than any single page fix. Whatever generates these pages should validate
against rendered output — the check added to the DSCR work (`visible FAQ count == schema count`,
`file ends with </html>`) would have caught all three classes.

Finding 5 is the cheapest win on the list and the one I would do first.
