# SBA program clusters: build plan for Claude Code (2026-10-29)

**Why:** an SBA lender partner (the "program lender" below) sent Jerry its appetite on 2026-10-28. Its strengths are narrow, high-ticket needs with few credible answers online, the same pattern as `/commercial-truck-title-loan.html`:
- 100% financing on owner-occupied commercial real estate
- hotels, including PIP and flag-conversion work
- USDA loans in towns under 50,000 people
- business acquisitions with 5% cash down
- refinancing real estate, term debt and lines of credit (not MCAs)

The site already has ~50 SBA guides, but they are generic ("SBA loan requirements") or by industry. None leads with these programs.

Follow the STATUS rules and section 0 of `docs/AEO_BUILD_PLAN_2026-10-22.md` (generators, page template, one commit per push, IndexNow, no editing cited pages without the 7-day watch). Add this plan to STATUS "Next up" as its own block.

---

## Content rules for this program (read before writing anything)

1. **Never name the program lender, its loan officer or its email domain**, and never present its terms as a quote or an offer. Write "some SBA lenders…" / "lenders in our network…" / "a typical structure is…". The appetite below shapes *what we write about*; public numbers come from SBA/USDA sources or are framed as typical ranges.
2. **Check every SBA rule against the current SBA SOP 50 10** (sba.gov) and every USDA rule against USDA Rural Development's Business & Industry program pages. Link both in Sources. Topics where the rules changed recently and lenders differ:
   - equity injection for changes of ownership
   - whether a seller note can count toward the injection, and its standby terms
   - whether an existing business buying a competitor needs any injection
   - guarantee fees for the current fiscal year
   - which debts are eligible to refinance

   If the SOP and the lender appetite disagree, the SOP wins on the page, and the page says lenders vary.
3. **Don't publish:**
   - the referral fee or compensation
   - "no points"
   - the program lender's minimum credit score or rate floors as a fixed rule

   Use ranges: e.g. "many SBA lenders look for roughly 650–680+; some go to the mid-660s with strong cash flow". Rates are framed as "Prime + a spread, adjustable quarterly on many 7(a) loans; owner-occupied real estate usually prices at the low end".
4. **What these lenders won't do is content too.** Say plainly that many SBA lenders exclude gas stations and anything with underground tanks, restaurants and bars, vape shops, FedEx routes and fleet-heavy businesses, standalone working capital, and projections-only deals. Point those readers to the Axiant page that fits (MCA consolidation, working capital, equipment). "Why one SBA lender says no and another says yes" is the broker's value and a strong citation angle.
5. **All deals:** cash flow last year and this year, no projections. Prior bankruptcy considered after ~7 years with a reasonable explanation. Express both as common lender practice, not as a promise.

### Worked example (use on the 100% CRE pages, anonymised)
From a real lender proposal (remove address, date and lender). Numbers verified (P&I recomputes to $23,444.46):

| Item | Amount |
|---|---|
| Purchase price (owner-occupied building) | $3,000,000 |
| SBA guarantee fee (estimate) | $81,875 |
| 7(a) packaging fee (estimate) | $2,500 |
| Appraisal, environmental, escrow, etc. (estimate) | $19,500 |
| **Total project cost** | **$3,103,875** |
| Cash down | **$0 (0%)** |
| SBA 7(a) loan | $3,103,875 |
| Rate (estimate) / term | 7.75% / 25 years |
| Monthly P&I | **$23,444** |

Recompute the guarantee fee from the current SBA fee notice before publishing. Label it "illustrative; rates and fees change; subject to approval". Keep the two real-world conditions from the proposal: the business must support the payment from existing cash flow, and excess land must be used by the business (e.g. paved for parking).

---

## Validate first
Ask Bing Copilot (and ChatGPT/Perplexity if signed in) each pillar's buyer question below. Log who gets cited in `_analysis/aeo-validation.md`. Build where specialists are thin; if a specialist owns the answer, make it a spoke, not a pillar.

---

## Cluster 1: SBA 100% financing for owner-occupied commercial real estate (highest priority)
**New root money page:** `/sba-100-percent-financing.html`
Buyer question: "can I buy my business's building with no money down?"

Quick Answer:
- some SBA 7(a) lenders finance up to 100% of an owner-occupied purchase for an established, cash-flowing business
- roughly $350K–$5M
- 25-year term
- fees can be rolled in
- the worked example above

Spokes (`/sba-100-percent-financing/articles/<slug>/`), each different in substance:
1. Buying the building your auto repair shop rents (lifts, environmental, zoning)
2. 100% financing for a daycare building (licensing capacity, outdoor space)
3. Financing a contractor's yard or land the business uses (land must be used by the business; agriculture excluded)
4. Office, retail and industrial for your own business (51%+ occupancy rule from the SOP, sourced)
5. Adding small tenant improvements to an SBA building purchase (TI must fund within a few months)
6. Assisted living and memory care facilities (mostly private-pay; Medicaid-heavy is harder)
7. Owner-occupied vs investment property: why only owner-occupied gets 100%
8. 100% SBA 7(a) vs SBA 504 (10% down) vs conventional (20–25% down): a comparison table (citation shape)

**Existing pages:**
- `commercial-real-estate-loans/articles/100-percent-financing-owner-occupied-commercial-real-estate/` and `sba-loans/articles/sba-loan-owner-occupied-commercial-property/` overlap the new pillar. Check Bing citations first. If cited, keep both and link them to the pillar in the first screen; if not cited, merge into the pillar and 301.
- `sba-loans/articles/how-much-down-payment-required-sba-loan/` says "10–20%" in its title, which conflicts with this program. After the 7-day watch, add "as low as 0% for owner-occupied real estate with some lenders" to its Quick Answer and link the pillar.

## Cluster 2: Hotel and hospitality financing
**New root money page:** `/hotel-financing.html`
Buyer question: "how do I get an SBA loan to buy a hotel?"

Quick Answer:
- SBA 7(a)/504 and USDA for flagged or strong independent hotels
- buyer hotel experience expected
- up to ~85% LTV typical for SBA hotel deals
- PIP and flag conversions financeable
- no ground-up construction

Spokes:
1. SBA loans for flagged hotels vs independents
2. Financing a PIP (property improvement plan) with the purchase
3. Flag conversion financing
4. How much hotel experience lenders want (and how to show it)
5. USDA B&I hotel loans in towns under 50,000 people (link Cluster 3)
6. Typical hotel loan rates and terms 2026 (rates companion, citation shape)
7. Hotel financing: SBA vs CMBS vs bank. The existing `commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/` already covers this, so link it as a spoke; don't duplicate it.

## Cluster 3: USDA Business & Industry (B&I) loans
**New root money page:** `/usda-business-loans.html`
Buyer question: "USDA business loan for a hotel in a small town". There are no USDA pages on the site today.

Quick Answer (from the USDA RD program page):
- rural areas, generally towns under 50,000 population
- real estate, buildings, equipment, inventory, working capital
- lenders commonly go to ~80% LTV
- loan size per USDA, with the note that lender appetite varies (some cap around $10M)

Spokes:
1. Is my town eligible? (link the USDA eligibility map)
2. USDA B&I vs SBA 7(a)
3. USDA hotel loans
4. Typical USDA B&I rates, fees and terms 2026

## Cluster 4: Buying a business with 5% down
**Strengthen the existing pillar** `/business-acquisition-financing.html` (check whether it's cited; if so, edit after the watch) and add spokes under `business-acquisition-financing/articles/`:
1. Buy a business with 5% down and a seller note (who qualifies: industry experience or current manager; reserves; the standby rule from the current SOP)
2. Buying a competitor: when 100% financing is possible (verify against the SOP)
3. SBA equity injection rules for business acquisitions, 2026 (sourced, citation shape)
4. Bigger acquisitions: why lenders ask for more collateral or a bigger seller note ($1M–$5M)

Link the existing `sba-loans/articles/sba-loan-buy-out-business-partner/`, `buying-a-business-financing-guide/` and franchise acquisition pages.

## Cluster 5: Refinancing debt with an SBA loan
Spokes under `sba-loans/articles/`:
1. What debts an SBA loan can refinance (real estate, equipment and working-capital term loans, lines of credit), from the SOP's debt-refinance rules
2. **Can you refinance an MCA with an SBA loan? (Generally no.)** Strong AEO question. Point to the MCA consolidation and debt relief money pages, and fix any page that implies otherwise.
3. Refinancing a balloon or hard-money building loan into SBA 7(a)

## Cluster 6: Who SBA lenders turn down, and where to go instead (citation page)
One page: "Businesses SBA lenders often decline: gas stations, restaurants and bars, vape shops, delivery routes, projections-only startups, standalone working capital". For each, the realistic alternative on Axiant, plus a line that lenders differ and a broker can find the one that says yes. Link from `sba-loan-denied-reasons-fix-before-reapplying` and `sba-loan-alternatives-when-you-dont-qualify` after the watch.

Also one spoke: **SBA loan after bankruptcy** (time since discharge, the explanation lenders want, examples like job loss, family illness or a partner dispute).

---

## Calls, not just pageviews
- Every page in these clusters ends with: "Talk to an SBA specialist: (561) 268-0465" plus the get-matched form. When per-channel numbers ship, these pages use them.
- The form's loan-type options must include "SBA: buy my building", "SBA: buy a business", "Hotel" and "USDA" so these leads arrive tagged. Check `match.html` and the CRM intake mapping.

## llms.txt
Add one factual key-facts line per new pillar (100% owner-occupied SBA, hotels, USDA B&I, 5% down acquisitions, SBA debt refinance), with no lender names.

## Order (new pages first; edits to cited pages after the watch)
1. Cluster 1 pillar + spokes 1–4 + the 7(a) vs 504 vs conventional comparison
2. Cluster 2 pillar + PIP + flag conversion + experience
3. Cluster 3 pillar + eligibility + USDA vs SBA
4. Cluster 5 "Can you refinance an MCA with SBA?" + Cluster 6 page
5. Cluster 4 spokes
6. Remaining spokes and rates companions; then the edits to existing cited pages
