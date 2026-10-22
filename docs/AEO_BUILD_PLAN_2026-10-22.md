# Axiant AEO build plan — for Claude Code (2026-10-22)

Goal: more AI-assistant leads. Two page types do two jobs:
- **Money pages** (narrow, underserved need, buyer ready to act) convert ChatGPT traffic. Proven: `/commercial-truck-title-loan.html` (16 leads, 6 apps), `/commercial-marine-financing.html` (6 leads, 4 apps).
- **Citation pages** ("best X 2026", "typical X rates 2026", "X vs Y") get quoted by Bing Copilot (~3,000/day) and Google AI Overviews, which builds brand searches. They rarely convert directly.

Full context: `axiant/Breakdown.md` and `axiant/Plan.md` in the AEO project.

---

## STATUS — read this first (last updated 2026-10-22, session 2)

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

### Next up (in order; one per session)
1. [ ] **Fix unstyled tables on older money pages.** `ba-table` / `ba-table-wrap` have no CSS anywhere (truck title, real-estate secured, marine, MCA consolidation, etc. show plain unbordered tables). Swap to the v2 `.table-wrap` component; on phones its first-column cells do not wrap, so keep first-column text under ~26 characters. Check each page at 390px for horizontal overflow (Playwright, `document.documentElement.scrollWidth` must equal 390). Money pages are cited: one push for all, then the 7-day watch.
2. [ ] **2b. Dump truck title loan spoke** under `commercial-truck-title-loan/articles/` (validated: Bing cites consumer title lenders at $100–$25K). Then box truck and tow truck spokes (tow truck spoke must link `/towing-business-financing.html`).
3. [ ] **2a. `/vending-machine-financing.html`** pillar (validated: no finance specialist cited). The existing spoke earns non-brand clicks: keep it as a spoke unless a check shows it is uncited, and link it in.
4. [ ] **2a. Car wash:** merge `articles/how-to-finance-buy-a-car-wash/` + `sba-loans/articles/car-wash-financing/` into `/car-wash-financing.html`, 301 both (check neither is Bing-cited first).
5. [ ] **2a. NEMT:** do NOT move or 301 the spoke (Bing cites it). Strengthen it in place: typical rates/terms, a vs page, link from towing/ambulance pages.
6. [ ] **2e. Companion pages:** "Typical truck title loan rates and terms 2026", "Truck title loan vs refinance vs equipment loan"; marine: "Typical commercial boat loan rates 2026", "Commercial vessel loan vs marine lease" (also lifts marine's link count); real-estate: "2nd-position business loan vs HELOC vs cash-out refi", "Typical rates on 2nd-lien business loans 2026".
7. [ ] **Batch 3** items, top of table first.
8. [ ] **Batch 5** llms.txt lines for each money page shipped so far.
9. [ ] Lower priority (specialists/Crestmont own the answer): fishing vessel (strengthen inside marine cluster, no new root), ambulance, marina.
10. [ ] **Skip:** ITIN pillar, funeral home pillar (specialists own them).

### Dated tasks
- **2026-10-29:** Bing Webmaster → AI Performance. Compare Copilot citations/day with the pre-push baseline (~3,000–4,500/day; 3-month total 252.9K). If they held, editing already-cited pages is safe again. Log the numbers here.
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
| Security guard payroll funding (1,762 impr, pos 10.9) | `security-guard-business-financing/articles/guard-payroll-between-invoices/` + pillar | Retitle/H1/Quick Answer to "payroll funding" wording; add rates/terms numbers; link from pillar first screen |
| Imaging/radiology patient financing (500–770 impr each, pos 28–32) | `carecredit-vs-patientfi-imaging-radiology/`, `patient-financing-imaging-centers/`, `radiology-practice-financing-complete-guide/` | **Overlapping**: merge the two patient-financing pages, keep the vs page (it's cited), cross-link |
| Electrical contractor funding (747 impr, pos 25.5) | `construction-business-financing/electrical-contractor-financing/` | Rewrite to the full page template; add numbers and FAQ |
| Owner-occupied vs investment CRE by state (Copilot grounding; ID, AZ, UT cited) | `commercial-real-estate-loans/articles/owner-occupied-vs-investment-commercial-property-loan/` | Add 3 state spokes (Idaho, Arizona, Utah) **only with real state-specific content** (state SBA district, typical LTV/DSCR, property-tax and title differences). No find-and-replace state pages |
| Construction-to-permanent (Copilot grounding) | `commercial-real-estate-loans/articles/construction-to-permanent-financing/` | Audit against template; add typical rates/timeline numbers |
| 5 Cs of lending (Copilot grounding) | none found | **New** spoke under `/how-lenders-decide/` |
| Unsecured LOC for startups/new businesses (Copilot grounding) | only vs-pages under `startup-financing/articles/` | **New** spoke: "Unsecured business line of credit for a new business (under 2 years)" |

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
