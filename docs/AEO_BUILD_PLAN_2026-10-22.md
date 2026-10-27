# Axiant AEO build plan — for Claude Code (2026-10-22)

Goal: more AI-assistant leads. Two page types do two jobs:
- **Money pages** (narrow, underserved need, buyer ready to act) convert ChatGPT traffic. Proven: `/commercial-truck-title-loan.html` (16 leads, 6 apps), `/commercial-marine-financing.html` (6 leads, 4 apps).
- **Citation pages** ("best X 2026", "typical X rates 2026", "X vs Y") get quoted by Bing Copilot (~3,000/day) and Google AI Overviews, which builds brand searches. They rarely convert directly.

Full context: `axiant/Breakdown.md` and `axiant/Plan.md` in the AEO project.

---

## STATUS — read this first (last updated 2026-10-27, session 8)

**Rule for every session:** do the first unchecked item in "Next up", follow sections 0.2–0.8, ship it, then update this STATUS block (tick it, add a log line, move the next item up) in the same push. Stop after one item and report.

### Done
- [x] **0.** Pending attribution work committed and live (`64f1bd3fb`): homepage form → CRM, `attribution.js` on homepage + equipment-for-sale.
- [x] **1a.** Brand clause in the Quick Answer of the top-25 cited + 5 money pages. List: `scripts/aeo/top25-cited.txt`, `scripts/aeo/money-pages.txt`. Check: `python scripts/check_brand_quick_answers.py` (expect 0).
- [x] **1b.** Get-matched block on the top-10 cited pages. Source: `_components/get-matched.html`; sync: `python scripts/sync-get-matched.py`. Contact details reach `/match.html` via sessionStorage (never the URL: pixels). Test: `PLAYWRIGHT_MODULE=../Axiant-Partners-CRM/node_modules/playwright node scripts/tests/get-matched.test.mjs`.
- [x] **1c.** Contextual links into money pages: `scripts/aeo/add_money_page_links.py` (refuses Quick Answer / FAQ spots). Measure: `python scripts/count_money_page_links.py`. Outside-cluster links: truck title 12, real-estate 10, security guard 10, **towing 3, marine 2** (no other relevant pages yet; Batch 2/3 pages must link to them).
- [x] **1d.** 48 "Editorial Team" Person authors → Organization (`@id https://axiantpartners.com/#organization`). Named reviewer still waits on Alex.
- [x] **1e.** Sources blocks on 311 more pages, matched to claims: `scripts/aeo/add_sources_by_claim.py` (catalog + triggers inside). 70 pages with no matching claim left without one (by design).
- [x] **1f.** Visible "Updated" = `dateModified` on 87 pages: `scripts/aeo/fix_page_dates.py`, content dates via `scripts/aeo/content_dates.py` (ignores sweeps >50 files and AEO commits). Only 17 pages lack `dateModified` (all equipment-for-sale, see "Blocked").
- [x] **Batch 2 validation** (Bing AI Mode only): results in `_analysis/aeo-validation.md`. Changes to the Batch 2 plan below.
- [x] **ITIN fact fix** (`327057750`): SBA now requires 100% owners US citizens/nationals (since 2026-03-01); the ITIN article said "majority, citizens or LPRs".
- [x] All of the above pushed 2026-10-22 as 21 single-commit pushes; every IndexNow run succeeded.

- [x] **2b. `/heavy-equipment-equity-loan.html`** + 5 spokes + hub (2026-10-22). Pillar: `python scripts/build_heavy_equity_pillar.py --apply` (FAQ/FAQPage and HowTo from one list; uses `.table-wrap`). Spokes: `scripts/cluster_heavy_equity.py` via `python scripts/build-cluster.py heavy_equity --apply`. Linked from excavators, bulldozers, wheel loaders, skid steers, backhoes, equipment refinancing, equipment-financing pillar (7 outside links). Key angle: most yellow iron has no title, lenders file a UCC-1. Rebuilding either re-dates the pages: only rebuild for a real content change.
- [x] **Renderer fix** (2026-10-22): `scripts/article_v2.py` now emits UET/Meta/OpenAI tags from `_components/tracking-tags.html` and `script.js` at the live `?v=`. Before this, any fresh render shipped with no ad conversion tracking.
- [x] **FTC source fix** (2026-10-22): `ftc.gov/business-guidance/credit-finance-trade` had become an empty listing; 113 pages + 10 modules repointed to the FTC's small-business-financing guidance (`scripts/aeo/fix_ftc_source.py`).
- [x] **2b. Truck-class title loan spokes** (2026-10-26): dump, box and tow truck spokes under `commercial-truck-title-loan/articles/` from `scripts/cluster_truck_title_d.py`. Built with `python scripts/build-cluster.py truck_title --only dump-truck-title-loan,box-truck-title-loan,tow-truck-title-loan --apply`: the new `--only` flag stops a rebuild from re-dating the 8 cited spokes. Each spoke has its own price table (from the matching equipment page), where that class sits in the site's existing 50–80%-of-FLV range, lender types, a class-specific appraisal table and "wrong tool" cases; worked examples labelled illustrative. Sources: OCC ABL handbook (liquidation value), FHWA bridge formula, DOE weight classes, 49 CFR 383.91 (26,001 lb CDL line). Linked from `/equipment/dump-trucks/`, `/equipment/box-trucks/`, the tow truck & wrecker guide (no tow-truck equipment page exists); tow spoke links `/towing-business-financing.html`. Hub, sitemap, llms.txt updated.
- [x] **2a. `/vending-machine-financing.html`** + 4 spokes + hub (2026-10-26). Pillar: `python scripts/build_vending_pillar.py --apply`; spokes: `scripts/cluster_vending.py` via `python scripts/build-cluster.py vending --apply` (typical rates 2026, lease vs loan vs pay-later checkout, micro-market financing, buying a vending route). The old spoke `equipment-financing/articles/vending-machine-financing/` stays put (earns non-brand clicks), is listed in the pillar's guides and links up to the pillar (`add_money_page_links.py`, `VEND`). Rates reuse the site's 7-22% APR tiers; machine costs come from the old spoke. Specific facts with sources: FDA calorie labeling at 20+ machines (21 CFR 101.8), Smart Snacks in schools (7 CFR 210.11), Randolph-Sheppard priority on federal property, TILA business-purpose exemption (so ask for the APR), SBA 10% equity injection on a change of ownership, Form 8594 allocation. Added to `money-pages.txt`, sitemap, llms.txt. Only 1 outside link so far: add more after the Oct 29 check (candidates: `/equipment-financing.html`, `/startup-financing.html`, `/business-acquisition-financing.html`). Old spoke already overflowed to 408px at 390px before this change: fix it with the table pass.
- [x] **2e. Truck title companions** (2026-10-26, moved ahead of car wash by Alex): `typical-truck-title-loan-rates-2026` and `truck-title-loan-vs-refinance-vs-equipment-loan` under `commercial-truck-title-loan/articles/`, from `scripts/cluster_truck_title_e.py`, built with `--only` (cited spokes not re-dated). The truck cluster had published no APR; the rates page uses ranges the site already publishes (7-22% APR equipment tiers, 50-80% of FLV and 24-72 months from equipment refinancing, 6-15% truck purchase from `/equipment/semi-trucks/`) and contrasts the CFPB 2016 consumer title study (~300% APR, ~1 in 5 sequences repossessed). **Alex: confirm 7-22% matches what lenders quote your truck-title leads.** Linked from the dump/box/tow spokes' Related lists; the money page is not edited (watch). Hub, sitemap, llms.txt (13 guides).
- [x] **2e. Marine and real-estate vs pages** (2026-10-26): `commercial-marine-financing/articles/commercial-vessel-loan-vs-marine-lease/` (`cluster_marine_d.py`: preferred ship mortgage 46 USC 31322, owner-citizenship rules for coastwise/fishery endorsements 46 USC 12113, bareboat charter, vessels as 10-year MACRS class 00.28) and `real-estate-secured-business-loan/articles/second-position-business-loan-vs-heloc-vs-cash-out-refinance/` (`cluster_res_business_loan_c.py`: business-purpose loans on a home have no TILA disclosures or rescission, 12 CFR 1026.3/1026.15; Garn-St Germain protects owner-occupied 1-4 unit homes from due-on-sale over a junior lien, commercial property is not protected). Built with `--only`; hubs, sitemap, llms.txt (marine 6, real-estate 7 guides). Money pages not edited (watch).
- [x] **Batch 3, security guard payroll funding** (2026-10-27): `guard-payroll-between-invoices` retitled to "Security Guard Payroll Funding: Rates, Terms and How It Works" (slug kept). New Quick Answer, a rates-and-terms section comparing payroll funding with a line of credit, an illustrative worked example and a cost FAQ. Every number reuses ranges the site already publishes: factoring 80-95% advance, ~1-5% fee and 24-hour funding after setup (`/invoice-factoring.html`); lines of credit 8-13% APR at banks and 14-30%+ online (the cited LOC rates page, linked to, not edited). Built with `python scripts/build-cluster.py security_guard --only guard-payroll-between-invoices --apply`. Pillar: "Payroll funding" in the first-screen hero checks now links to the spoke, and the guides list was retitled (hand edit; `link-pillars-to-clusters.py` skips pillars that already have the list). Bing showed **0 Copilot citations** for the whole guard cluster and pillar before the edit, so this sits outside the watch. 390px: no overflow on the spoke, pillar or hub.

### Next up (in order; one per session)
1. [ ] **2e. Rates companions, waiting on Alex's ranges:** "Typical commercial boat loan rates 2026" (marine, slug `typical-commercial-boat-loan-rates-2026`) and "Typical rates on 2nd-lien business loans 2026" (real-estate, slug `typical-second-lien-business-loan-rates-2026`). Neither cluster nor the site publishes a boat-loan or 2nd-lien rate, so do not invent one: Alex to send APR range, term, max LTV/CLTV or down payment, fees, typical loan size from real deals. Add to `cluster_marine_d.py` / `cluster_res_business_loan_c.py`, build with `--only`, then link them from the two vs pages.
2. [ ] **Batch 3** items, top of table first. Security guard row done 2026-10-27. **Next: electrical contractor** (0 Copilot citations on 2026-10-27, so safe now). Imaging merge waits: `patient-financing-imaging-centers` has 15 Copilot citations and the vs page is top-25, so it goes behind the 10-29 check. Construction-to-perm and owner-occupied are top-25 cited (same). The 5 Cs and new-business unsecured LOC rows are **not new pages** (already answered, see the table); waiting on Alex whether to strengthen the existing pages instead. Most remaining rows edit existing pages: check each is uncited first, or hold it for after 10-29.
3. [ ] **Batch 5, rest:** key-facts lines for the older money pages (truck title, marine, real-estate secured; MCA consolidation). Lines for everything shipped since Oct 22 went in on 2026-10-27.
5. [ ] Lower priority (specialists/Crestmont own the answer): fishing vessel (strengthen inside marine cluster, no new root), ambulance, marina.
6. [ ] **Skip:** ITIN pillar, funeral home pillar (specialists own them).

### Dated tasks
- **2026-10-29:** Bing Webmaster → AI Performance. Compare Copilot citations/day with the pre-push baseline (~3,000–4,500/day; 3-month total 252.9K). If they held, editing already-cited pages is safe again. Log the numbers here.
  - [ ] **Then, only if citations held (run these two first, moved here by Alex 2026-10-27):**
  - [ ] **1. Fix unstyled tables on older money pages.** `ba-table` / `ba-table-wrap` have no CSS anywhere (truck title, real-estate secured, marine, MCA consolidation, etc. show plain unbordered tables). Swap to the v2 `.table-wrap` component; on phones its first-column cells do not wrap, so keep first-column text under ~26 characters. Check each page at 390px for horizontal overflow (Playwright, `document.documentElement.scrollWidth` must equal 390). Money pages are cited: one push for all, then a fresh 7-day watch. Skip it if citations dropped and log why. (Moved out of Next up on 2026-10-26: it edits cited pages inside the Oct 22 watch.)
  - [ ] **2. 2a. NEMT, right after the table fix:** do NOT move or 301 the spoke (Bing cites it). Strengthen it in place: typical rates/terms, a vs page, link from towing/ambulance pages. It edits a cited page, so it sits behind the same check. Each of these two pushes edits cited pages; Alex wants both straight after 10-29, so ship them back to back and run one 7-day watch covering both.
  - [ ] **Same condition: car wash, strengthen in place (merge cancelled 2026-10-26).** Both `articles/how-to-finance-buy-a-car-wash/` and `sba-loans/articles/car-wash-financing/` are now Bing-cited (sources 1 and 2 of 4 for "how to finance buying a car wash"; see `_analysis/aeo-validation.md`). Do NOT merge or 301. Cross-link them (purchase guide <-> financing options), add a worked example and a sources block to the purchase guide, and give the SBA page the SOP 50 10 8 equity-injection detail. One push, then a fresh 7-day watch.
  - [ ] **Same condition:** link the money page `/commercial-truck-title-loan.html` to the two new companion pages, and add 2-3 outside links into `/vending-machine-financing.html`.
  - [ ] **CRE rate conflict:** `/commercial-real-estate-loans/articles/typical-commercial-real-estate-loan-rates-2026/` says bank CRE 6.5-8%; `/business-loan-rates-2026/` says commercial real estate 8-12%. Both cited. Ask Alex which is right, then align one push.
  - [ ] **Check `/equipment-financing/articles/section-179-tax-strategy-2026/`:** it says a $1.16M limit and 60% bonus depreciation; the 2025 tax law appears to have raised these (about $2.5M, inflation-adjusted for 2026, and 100% bonus). Verify against IRS sources before editing; check whether it is cited first.
- **~2026-12-15:** Batch 4 push 1 (top 3 cited pages to 2027). **~2026-12-26 to 2027-01-02:** remaining "2026" titles, ≤25 per push.

### Blocked / waiting on Alex
- Named reviewer + short factual bio (1d `reviewedBy`).
- Referral-partner terms (2d; Bing compares programs by commission).
- Google Business Profile URL (Batch 5 `sameAs`).
- Perplexity sign-in in Chrome, to add it to validation. ChatGPT side not yet checked.
- 17 equipment-for-sale pages have no `dateModified`: fix inside `scripts/equipment-for-sale/build.py` only after its `_chrome.html` carries the UET/pixel tags (0.3), diff-verified.

### How to ship (learned 2026-10-22)
- No git identity on this machine: commit with `git -c user.name="Alex Solopenkov" -c user.email="alex@axiantpartners.com" commit ...`.
- **One commit per push, ≤25 HTML pages per commit.** `.github/workflows/indexnow.yml` submits only `--since HEAD~1`, so a multi-commit push leaves earlier commits' pages unsubmitted. Push with `git push origin <sha>:main` one commit at a time and confirm `gh run list --limit 1` shows success before the next.
- Verify live with `curl` on one changed page after Netlify deploys (~1 min).
- Validation of new pages: `https://www.bing.com/copilotsearch?q=<buyer question>`; sources show in the "N Sources" pills. Record in `_analysis/aeo-validation.md`.
- Never put PII in URLs; never submit forms on production (it creates real CRM leads); never delete pages (merge + 301 instead).

### Log
- 2026-10-22: Section 0, Batch 1 (1a–1f), Batch 2 validation, ITIN fix. All live.
- 2026-10-22: Heavy equipment equity pillar + 5 spokes + hub; renderer tracking-tags fix; FTC source repointed on 113 pages. Found: `ba-table` money-page tables are unstyled (now Next up #1).
- 2026-10-26: Dump, box and tow truck title loan spokes + hub, sitemap, llms.txt, 3 equipment-page links; `build-cluster.py --only`. Table fix moved under the 2026-10-29 Bing check (cited pages, inside the watch). Next: vending machine pillar.
- 2026-10-26: Vending machine financing pillar + 4 spokes + hub, sitemap, llms.txt; old vending spoke links up. Next: car wash merge.
- 2026-10-26: Truck title companions (typical rates 2026; vs refinance vs equipment loan), hub, sitemap, llms.txt. Next: car wash merge.
- 2026-10-26: Car wash merge **cancelled**: Bing now cites both car wash pages (were uncited on 10-22). Logged in aeo-validation.md; moved to "strengthen in place" under the 10-29 task. Next: marine + real-estate companion pages.
- 2026-10-26: Marine vessel loan vs lease; 2nd-position loan vs HELOC vs cash-out refi. Rates companions held for Alex's real ranges. Next: those two once ranges arrive, else NEMT after 10-29.
- 2026-10-27: Batch 5: llms.txt key-facts lines for heavy equipment equity, vending (with rates and lease-vs-loan), dump/box/tow truck title, truck title rates + vs refinance, vessel loan vs lease, 2nd-position vs HELOC vs cash-out. No .html changed, so IndexNow did not run (workflow only watches .html/sitemap). Batch 3 new pages **not built**: both are duplicates (5 Cs = `/how-lenders-decide/` itself; new-business unsecured LOC = `business-line-of-credit/articles/business-line-of-credit-for-startups/`, titled "Under 2 Years"). NEMT moved behind the 10-29 check, after the table fix. No cited page edited.
- 2026-10-27: Batch 3 security guard payroll funding (spoke retitle + rates/terms, pillar first-screen link, hub, sitemap). Copilot citations checked first in Bing AI Performance (3 months): guard cluster 0, electrical contractor 0, `patient-financing-imaging-centers` 15, NEMT 68. Next: electrical contractor rewrite.

---

## 0. Before you start (read once)

1. `git pull`, then commit the uncommitted attribution work already in the tree (new `attribution.js`, `index.html` homepage form → CRM, 17 `equipment-for-sale/*` pages, `scripts/equipment-for-sale/_chrome.html`). Message: "Homepage form to CRM; first-touch attribution on homepage and equipment-for-sale".
2. **Build with the existing generators, never by hand-editing generated HTML.** Clusters are data modules (`scripts/cluster_*.py`, e.g. `cluster_truck_title.py`, `_b`, `_c`) rendered by `scripts/article_v2.py` / `scripts/build-cluster.py`. Copy the closest existing module as the template.
3. **Do NOT run `scripts/equipment-for-sale/build.py`.** Its `_chrome.html` is missing the Microsoft UET and pixel tags that were added to the generated pages by hand, so a rebuild strips tracking from 17 pages. If you need it, move those tags into `_chrome.html` first and confirm with a diff that a rebuild adds nothing but your change.
4. **Content rules (copy from the header docstring of `cluster_truck_title.py`):** describe ranges as conventional across lenders, never as anyone's quote; no funded totals, no testimonials, no named-lender rates, no invented statistics. One entity: Axiant Partners, (561) 268-0465, Boca Raton. Business-purpose only. Every number needs a source or "typical range" framing.
5. **Page template (every new page):** Quick Answer (50–100 words, 2–3 bold numbers, class `quick-answer`, Speakable target) → At a Glance tiles → comparison table → worked example → visible FAQ matching `FAQPage` JSON-LD → HowTo if procedural → BreadcrumbList + Article/FinancialService → visible "Updated" date equal to `dateModified` → "Sources & Further Reading" block (`id="article-sources-h2"`) with .gov/primary links → apply CTA every two sections.
6. **Links per new spoke:** pillar, one sibling, one other cluster, `/match.html` (3–5 in-body, contextual). Add the new page to its hub, `sitemap.xml` (lastmod from git) and `llms.txt`.
7. **Ship in batches of ≤25 pages per push.** IndexNow fires on push. Bing citations dipped after both earlier big structural changes, so after any batch that edits already-cited pages, wait 7 days and check Bing AI Performance before the next such batch. New pages can ship faster.
8. **Merge before you create.** If two pages target the same question, merge into one and 301 the other in `_redirects`.

---

## Batch 1 — Enhance what already wins (week 1–2, highest leverage)

### 1a. Put the brand inside the Quick Answer
Today **9 of 642** Quick Answers mention Axiant, so when Copilot or AI Overviews quote one, the quote carries no name.
- On the **top 25 Copilot/AI Overview pages** (list below) and **all money pages**, add one natural clause to the Quick Answer: e.g. "Axiant Partners, a business-loan broker in Boca Raton, typically sees …" Keep it to one mention, factual, and keep the numbers unchanged.
- Do not rewrite the rest of the answer. Small edit, same shape, so citations aren't disturbed.
- Top cited pages (Copilot / AIO):
  - `/business-line-of-credit/articles/best-unsecured-business-lines-of-credit-2026/`
  - `/working-capital-loans/articles/best-working-capital-loans-2026/`
  - `/business-line-of-credit/articles/typical-business-line-of-credit-rates-2026/`
  - `/equipment-financing/articles/cherry-vs-carecredit/`
  - `/sba-loans/articles/what-is-an-sba-504-loan/`
  - `/commercial-real-estate-loans/articles/typical-commercial-real-estate-loan-rates-2026/`
  - `/business-loan-rates-2026/`
  - `/business-term-loans/articles/term-loan-vs-line-of-credit/`
  - `/commercial-real-estate-loans/articles/how-much-down-payment-required-commercial-property-loan/`
  - `/equipment-financing/articles/carecredit-vs-patientfi-imaging-radiology/`
  - `/securities-based-lending/articles/typical-sbl-rates-2026/`
  - `/business-line-of-credit/articles/how-fast-can-you-get-approved-business-line-of-credit/`
  - `/equipment-financing/articles/trac-lease-benefits-saves-money/`
  - `/commercial-real-estate-loans/articles/how-long-close-commercial-real-estate-loan/`
  - Fill to 25 from the Bing AI Performance export (see "Inputs").
- Acceptance: a script check that prints every top-25 page and money page whose `.quick-answer` text lacks "Axiant" (should be zero).

### 1b. "Get matched" block on the top 10 cited pages
- Directly after the Quick Answer: a compact block ("Get matched in 24 hours, no hard credit pull") with a **3-field form (name, email, phone)** that POSTs to `/.netlify/functions/apply` exactly like the new homepage form in `index.html` (`form_type: 'front_page'`, `lead_type: 'citation-block'`, `...window.__axAttr()`), plus a Netlify Forms copy. Then redirect to `/match.html` with name/email/phone prefilled so they can finish the full application.
- Put it in a shared component (`_components/`) with a sync script like the footer, not pasted 10 times.
- One line under it linking the **closest money page** (e.g. lines-of-credit pages → `/real-estate-secured-business-loan.html` and `/commercial-truck-title-loan.html` "if you own a truck or property outright").
- Acceptance: headless test that submitting the block from one of these pages sends `lead_channel` and `lead_landing_page` to the mocked endpoint.

### 1c. Internal links into the money pages
Money pages have very few contextual internal links in:

| Money page | Pages linking in today |
|---|---|
| `/commercial-marine-financing.html` | **1** |
| `/towing-business-financing.html` | 2 |
| `/security-guard-business-financing.html` | 4 |
| `/real-estate-secured-business-loan.html` | 6 |
| `/commercial-truck-title-loan.html` | 9 |

- Add contextual in-body links (not footer/sidebar boilerplate) so each has **≥10 relevant linking pages**. Sources: the trucking, equipment-financing, working-capital, MCA, bad-credit and equipment-type pages for truck title; equipment-financing, SBA and the fishing/charter spokes for marine; the HELOC, CRE, cash-out and DSCR pages for real-estate-secured; trucking and equipment/tow pages for towing; payroll and working-capital pages for security guard.
- Anchor text = the buyer's phrase ("borrow against a semi you own", "financing a commercial fishing vessel").

### 1d. Replace "Editorial Team" as a Person
48 pages emit `Person` schema named "Editorial Team". A Person must be a person.
- **Decision for Alex:** who is the named reviewer? Default assumption: **Alex Solopenkov, Founder**, with a `/about/alex-solopenkov/` bio page (role, years brokering, what he reviews). **No invented credentials or licenses.**
- Until decided: change those 48 to `Organization` (Axiant Partners) so the schema is truthful.
- Then add `reviewedBy` (Person) + visible "Reviewed by" line on money pages and the top-25 cited pages.

### 1e. Sources on every article
Sources blocks exist on **131** pages. Use `scripts/add-article-sources.py` to extend to all `/articles/` pages and money pages, with real primary sources per topic (SBA, Fed SBCS, CFPB, FTC, IRS Pub 946, FMCSA, USCG, NOAA). No generic filler lists: each source must relate to a claim on the page.

### 1f. Dates
56 indexable pages have no `dateModified`. Add it from the file's last real content commit (git log), and make the visible "Updated" date match. Never set dates to "today" without an edit.

---

## Batch 2 — Money pages (weeks 2–8, 2–3 per week)

**Validation rule before building each one:** ask ChatGPT, Copilot and Perplexity the buyer's question (given below). Build only if the answers cite no specialist or only thin sources. Record the result in a `_analysis/aeo-validation.md` table (question, date, who was cited, decision).

### 2a. Promote buried winners to root money pages (pillar + 5–8 spoke cluster)
These already exist as single spokes. Promote, then 301 the old spoke to the new pillar (or keep the spoke and link it in, if it targets a distinct question).

| New pillar | Existing page(s) to fold in | Buyer question to validate |
|---|---|---|
| `/nemt-van-financing.html` | `equipment-financing/articles/nemt-wheelchair-van-financing/` | "how do I finance wheelchair vans for my NEMT business" |
| `/itin-business-loans.html` | `equipment-financing/articles/itin-business-loans/` | "can I get a business loan with an ITIN and no SSN" |
| `/car-wash-financing.html` | **merge** `articles/how-to-finance-buy-a-car-wash/` + `sba-loans/articles/car-wash-financing/` (duplicates) | "how to finance buying a car wash" |
| `/commercial-fishing-vessel-financing.html` (or keep under marine and strengthen; decide after validation) | **merge** `commercial-marine-financing/articles/commercial-fishing-vessel-financing/` + `equipment-financing/articles/louisiana-commercial-fishing-financing/` | "loan for a commercial fishing boat" |
| `/vending-machine-financing.html` | `equipment-financing/articles/vending-machine-financing/` (already earns non-brand Google clicks) | "how to finance vending machines" |
| `/funeral-home-financing.html` | `sba-loans/articles/funeral-home-financing/` | "loan to buy a funeral home" |
| `/ambulance-financing.html` | `equipment-financing/articles/ambulance-financing/` | "financing ambulances for a private ambulance company" |

### 2b. Asset-equity family (modelled on truck title). Avoid near-duplicate pages
The truck title page already covers semi, box, dump and tow trucks. **Do not create separate root pages for box/dump/tow truck title loans**: five near-identical pages would compete with the winner. Instead:
- Add spokes under `commercial-truck-title-loan/articles/`: "box truck title loan", "dump truck title loan", "tow truck title loan". Each must differ in substance (typical values and loan-to-value by truck class, who lends, what the appraiser checks for that truck).
- **One new root page:** `/heavy-equipment-equity-loan.html` ("borrow against excavators, loaders and dozers you own" / heavy equipment cash-out refinance). Different asset, different lenders, a distinct page. Cluster: valuation, existing lien, equipment title loan vs sale-leaseback, vs MCA, default.
- Validate: "title loan on my excavator", "cash out equity in my construction equipment".

### 2c. Marine family
- New: `/marina-financing.html` (marina acquisition/expansion: real estate + business, SBA 7(a)/504, CRE). Validate: "how to finance buying a marina".
- Strengthen `commercial-marine-financing/articles/charter-boat-business-financing/` (keep as spoke).

### 2d. Referral-partner pages (ChatGPT has sent 4 partner enquiries)
Off `/referral.html`: `/referral-partners/equipment-dealers/`, `/referral-partners/accountants/`, `/referral-partners/insurance-agents/`. Each covers what the partner's client needs, how a referral works, how the partner is paid (only what is true today, so confirm terms with Alex), and the partner-portal sign-in. Validate: "business loan referral program for accountants".

### 2e. Companion citation pages for each money page
So the money pages get cited, not just the research pages (truck title has 19 Copilot citations):
- Truck title already has vs MCA and vs sale-leaseback. Add: **"Truck title loan vs refinance vs equipment loan"** and **"Typical truck title loan rates and terms 2026"**.
- Marine: **"Typical commercial boat loan rates and terms 2026"**, **"Commercial vessel loan vs marine equipment lease"**.
- Real-estate-secured: **"2nd-position business loan vs HELOC vs cash-out refinance"**, **"Typical rates on 2nd-lien business loans 2026"**.
- Each new money pillar from 2a/2b gets one "typical rates" and one "vs" spoke at launch.

---

## Batch 3 — Fix existing pages that sit on cited or high-impression questions (weeks 4–10)

The plan listed these as new pages; **most already exist**. Improve them instead:

| Query / signal | Existing page | Action |
|---|---|---|
| Security guard payroll funding (1,762 impr, pos 10.9) | `security-guard-business-financing/articles/guard-payroll-between-invoices/` + pillar | **Done 2026-10-27.** Retitle/H1/Quick Answer to "payroll funding" wording; add rates/terms numbers; link from pillar first screen |
| Imaging/radiology patient financing (500–770 impr each, pos 28–32) | `carecredit-vs-patientfi-imaging-radiology/`, `patient-financing-imaging-centers/`, `radiology-practice-financing-complete-guide/` | **Overlapping**: merge the two patient-financing pages, keep the vs page (it's cited), cross-link |
| Electrical contractor funding (747 impr, pos 25.5) | `construction-business-financing/electrical-contractor-financing/` | Rewrite to the full page template; add numbers and FAQ |
| Owner-occupied vs investment CRE by state (Copilot grounding; ID, AZ, UT cited) | `commercial-real-estate-loans/articles/owner-occupied-vs-investment-commercial-property-loan/` | Add 3 state spokes (Idaho, Arizona, Utah) **only with real state-specific content** (state SBA district, typical LTV/DSCR, property-tax and title differences). No find-and-replace state pages |
| Construction-to-permanent (Copilot grounding) | `commercial-real-estate-loans/articles/construction-to-permanent-financing/` | Audit against template; add typical rates/timeline numbers |
| 5 Cs of lending (Copilot grounding) | `/how-lenders-decide/` (title "The 5 C's of Credit"; Quick Answer + one section per C + lender-weighting table) | **Not a new page** (found 2026-10-27). Strengthen in place if anything; Alex to decide |
| Unsecured LOC for startups/new businesses (Copilot grounding) | `business-line-of-credit/articles/business-line-of-credit-for-startups/` ("Startup Business Line of Credit: Under 2 Years", secured vs unsecured section) | **Not a new page** (found 2026-10-27). Strengthen in place if anything; Alex to decide |

---

## Batch 4 — 2027 refresh (December; separate pushes)

- 194 titles contain "2026", including the most-cited Copilot pages.
- Push 1 (≈Dec 15): the **top 3 cited pages only**: update numbers + title year, same URLs, IndexNow. Watch Copilot citations 7 days.
- Push 2 (≈Dec 26–Jan 2): the remaining 191 in batches of ≤25.
- `/business-loan-rates-2026/`: keep the URL, update content, and add `/business-loan-rates-2027/` as a 301 to it, or the reverse. Pick one and never split the page.

---

## Batch 5 — llms.txt and entity signals (alongside batch 1)

- `llms.txt` key-facts block: add one line per money page with what it is for and who qualifies (truck title, marine, real-estate-secured, plus each new pillar as it ships). Keep everything factual; no "recommend us" language.
- Homepage `Organization`/`FinancialService` schema: add the Google Business Profile URL to `sameAs` once Alex supplies it; add `areaServed: US`, `knowsAbout` (product list).
- Make the entity line identical everywhere (name, phone, city).

---

## Inputs Claude Code needs from Alex (put files in `_analysis/aeo-inputs/`)
1. Bing Webmaster Tools → AI Performance: **grounding queries + cited pages export** (CSV). Drives the top-25 list and new cited-but-missing pages.
2. GSC Generative AI report export (AI Overview pages).
3. Named reviewer decision (1d) and a short bio.
4. Referral-partner terms (2d).
5. Google Business Profile URL (batch 5).

## Weekly loop after launch
Read the new Bing grounding queries + GSC machine queries. Any question cited or asked 3+ times with no dedicated page → add to the next batch. Merge duplicates monthly. Track: Copilot citations/day, AI-assistant leads (forms + calls), brand searches.

## Not for Claude Code (Alex / off-site)
AI engines lean on third-party mentions, so the site alone has a ceiling. Off-site work: Google Business Profile + real reviews, listings in broker/lender directories, answering real borrower questions on Reddit/Quora/LinkedIn as the founder (no astroturfing), and a few earned mentions (trade press for trucking, marine and contractors).
