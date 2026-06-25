# Build Scope — Commercial Real Estate Loan Calculator

A new, high-quality calculator page targeting a winnable high-volume gap. Built per the
Content Quality Playbook. This doc is the record so we can reuse the pattern for other
calculator/build pages.

## Why this page (the data)
- **Primary keyword:** "commercial real estate loan calculator" — **14,800/mo, difficulty 8–10** (very low).
- Cross-refs (same intent, same page should own them): "commercial real estate loans calculator," "commercial loan calculator" (14,800, diff 13), "commercial mortgage calculator," "commercial property loan calculator," "commercial property mortgage calculator."
- **Cannibalization check (done):** no existing CRE calculator page; Axiant ranks for **none** of these queries today. `calculator.html` is a generic loan/equipment calc, `dscr-calculator.html` owns DSCR, `business-loan-calculator-guide/` owns "business loan calculator." So this page is greenfield and must stay a **payment/down-payment** calc (not a DSCR clone).

## URL
`/commercial-real-estate-loans/commercial-real-estate-loan-calculator/` — **cluster-level**, not top-level.
Rationale: Axiant's bottleneck is domain authority, so we maximize every topical signal by nesting the tool inside the 34-page CRE cluster (vs. the top-level calculator convention). It inherits and feeds cluster authority.

## The tool (the AIO-resistant asset — the whole point)
A CRE loan **payment + down-payment** calculator. Google can't reproduce an interactive calculator in the SERP, so this is what wins the click an AI Overview would otherwise eat.
- **Inputs:** purchase price, loan program (SBA 504 / SBA 7(a) / conventional owner-occupied / investment / multifamily → auto-fills a typical down-payment %), down-payment % (editable), interest rate, amortization term (years), optional balloon (yrs) — CRE loans commonly balloon.
- **Outputs:** loan amount, down-payment $, estimated monthly payment, total interest, balloon balance (if set).
- Reuse the existing calculator JS pattern from `calculator.html` / the down-payment article's `#cre-dp-calc`. Label all figures "illustrative, not a quote."

## Supporting content (so it's substantive, not thin)
1. **Front-loaded answer (40–60 words):** what a CRE loan calculator estimates + the key drivers (price, down payment by program, rate, amortization, balloon).
2. **How the math works:** amortization vs. balloon (most CRE loans amortize over 20–25 yrs but balloon in 5–10), why payment ≠ payoff.
3. **Down payment by program** (mini-table) — link to the existing [down-payment article](/commercial-real-estate-loans/articles/how-much-down-payment-required-commercial-property-loan/) (don't duplicate it; summarize + link).
4. **What the calculator doesn't show — DSCR** (lenders size the loan to DSCR ≥ ~1.25) → link to `dscr-calculator.html`.
5. **FAQ** (commercial mortgage calculator questions) + **FAQPage JSON-LD** (server-rendered).
6. **CTA:** get matched.

## Internal linking (route cluster authority, no cannibalization)
- **Link TO this page from:** the CRE hub `commercial-real-estate-loans.html`, the down-payment article, the requirements article, the refinance articles (contextual "estimate your payment" links).
- **Link FROM this page to:** down-payment article, CRE requirements, `dscr-calculator.html`, the CRE hub, `/match.html`.

## Schema
BreadcrumbList, WebPage/SoftwareApplication (or Article), FAQPage. Visible "Updated" date + 2026 figures.

## Why it should win
Diff 8–10, 14,800/mo, zero existing Axiant competition, backed by a 34-page CRE cluster + a real interactive tool that's also **link bait** for the authority push.

## Revised Build list (after the cannibalization check)
1. **CRE loan calculator** — NEW (this page).
2. **Construction financing** pillar (22k/mo, diff 15) — NEW.
3. **Business loan calculator** — DO NOT build new; **optimize the existing** `business-loan-calculator-guide/` (it already targets 18k/mo "business loan calculator").
