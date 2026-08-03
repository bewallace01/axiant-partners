# FAQ answer parity — content dropped from schema

Companion to the answer-parity change. The page is now the source of truth for
every `FAQPage` answer, so wording that existed **only** in the JSON-LD is gone.
Nothing visible was removed. This is the list of what disappeared, so you can
decide whether any of it deserves to be written onto the page as real content.


## CLOSED 2026-08-03

Two entries below were escalated as judgement calls because they were factual
claims about Axiant's products rather than editorial choices. Both were resolved
from what the pages themselves already said, and **both figures were confirmed
correct by the site owner on 2026-08-03**. No further action.

**`revenue-based-financing/.../how-fast-can-you-get-revenue-based-financing/`**
The FAQ claimed funding "sometimes as little as 24–48 hours" while the body of
the same page stated 3–10 business days four times, including a comparison
saying RBF is *slower* than a merchant cash advance at 24–72 hours. The claim
made RBF faster than the product the page says beats it. Reconciled to the
page's own timeline in PR #189. Now reads *3–10 business days: 24–72 hours
initial review, 1–3 days to conditional approval, 2–5 days underwriting*.
Zero 24–48 hour claims remain; "3–10 business days" appears 3× consistently.

**`fix-and-flip/articles/how-much-down-payment-fix-and-flip-loan/`**
The FAQ referred to "the ARV cap" without ever stating it, while the body gave
70–75% twice. Named in the answer in PR #189. 70–75% now appears 3×
consistently across body, FAQ and schema.

Nothing was invented in either case — both figures were already published
elsewhere on the same page. The rest of this document is unreviewed and remains
open.


## Answers that lost a figure — 35

These matter most: the schema stated a number the page never showed, so the
number was never reviewed on-page. Each is now gone from the markup.


| Page | Question | Figures dropped |
|---|---|---|
| `business-acquisition-financing.html` | How much down payment do you need to buy a business? | 20% |
| `business-acquisition-financing.html` | What are typical business acquisition loan rates? | 2026 |
| `business-debt-relief/articles/mca-froze-my-bank-account/index.html` | How do I get my frozen business bank account released? | 1, 2, 3 |
| `business-debt-relief/articles/release-ucc-lien-business/index.html` | How do I get a UCC lien released? | 1, 2, 4 |
| `business-line-of-credit/articles/what-are-typical-business-line-of-credit-rates/index.html` | Does frequent line usage help reduce rates over time? | 2, 2026,, 24, 250,000, 48, 50,000 |
| `commercial-bridge-loans/articles/why-bridge-loan-timeline-keeps-slipping/index.html` | Why does my bridge loan timeline keep slipping? | 24, 48 |
| `dental-practice-financing.html` | What financing options are available for dental practices? | 5,000,000 |
| `equipment-financing/articles/3d-printer-financing/index.html` | Should I lease or buy a 3D printer? | 1 |
| `equipment-financing/articles/commercial-printing-press-financing/index.html` | Should I lease or buy a printing press? | 1 |
| `equipment-financing/articles/construction-equipment-financing-excavators-dozers/index.html` | Can I finance used construction equipment? | 12, 20, 25%, 8 |
| `equipment-financing/articles/restaurant-equipment-financing/index.html` | Can I finance used restaurant equipment? | 10, 7 |
| `equipment-for-sale/drilling-rigs/index.html` | How deep can these mobile drilling rigs drill? | 3.5 |
| `equipment/bulldozers/used-bulldozer-financing/index.html` | Can you finance a used bulldozer? | 36, 60 |
| `equipment/bulldozers/used-bulldozer-financing/index.html` | Do used bulldozers require a larger down payment? | 680 |
| `equipment/excavators/used-excavator-financing/index.html` | Can you finance a used excavator? | 36, 60 |
| `equipment/excavators/used-excavator-financing/index.html` | Do used excavators require a larger down payment? | 680 |
| `equipment/forklifts/used-forklift-financing/index.html` | Can you finance a used forklift? | 36, 60 |
| `equipment/forklifts/used-forklift-financing/index.html` | What credit score is needed for used forklift financing? | 680 |
| `equipment/injection-molding/injection-molding-equipment-financing/index.html` | How much does an injection molding machine cost? | 100, 200, 500 |
| `equipment/injection-molding/injection-molding-equipment-financing/index.html` | What credit score do I need for injection molding financing? | 680 |
| `equipment/zero-turn-mowers/zero-turn-vs-standard-mower-financing/index.html` | Can I finance both zero-turn and standard mowers? | 24, 48, 600 |
| `equipment/zero-turn-mowers/zero-turn-vs-standard-mower-financing/index.html` | What credit score do I need for commercial mower financing? | 680 |
| `fix-and-flip/articles/fix-and-flip-vs-hard-money-loan/index.html` | What is the difference between a fix-and-flip loan and a har | 12, 18, 6, 70, 75% |
| `fix-and-flip/articles/how-much-down-payment-fix-and-flip-loan/index.html` | How much down payment do you need for a fix-and-flip loan? | 100%, 20%, 70, 75% |
| `hvac-business-financing.html` | What financing options are available for HVAC contractors? | 5,000,000 |
| `manufacturing-business-financing/manufacturing-equipment-financing-expand-capacity-without-cash-crunch/index.html` | What KPI should determine next equipment investment? | 12, 8 |
| `plumbing-business-financing.html` | What financing options are available for plumbing contractor | 5,000,000 |
| `revenue-based-financing/articles/how-fast-can-you-get-revenue-based-financing/index.html` | How fast can you get revenue-based financing? | 10, 3 |
| `roofing-business-financing.html` | What financing options are available for roofing contractors | 5,000,000 |
| `sba-loans/articles/how-long-sba-loan-approval/index.html` | Is there a faster SBA loan option? | 500,000. |
| `sba-loans/articles/how-long-sba-loan-approval/index.html` | Why do SBA loans take longer than other loans? | 2, 3 |
| `small-business-lending-statistics.html` | What is the average SBA 7(a) loan size? | 2025,, 477,571, |
| `small-business-lending-statistics.html` | What percentage of small businesses apply for financing? | 2021. |
| `working-capital-loans.html` | What is the minimum loan amount? | 10,000. |
| `working-capital-loans/articles/invoice-factoring-vs-merchant-cash-advance/index.html` | Is invoice factoring cheaper than a merchant cash advance? | 1, 1.15, 1.50, 100%, 15, 2 |

## Answers that lost substantive wording — 90 of 196

The schema answer was written to stand alone; the page answer leans on its
heading. Same ground, fewer words. Listed where six or more content words went.


**`automotive-business-loans.html`** — How do automotive businesses qualify for a loan?

- dropped words: additional, around, based, businesses, dealers, face, qualification, score, seeking
- old schema answer: Qualification is based on the business: revenue, time in business, credit, and cash flow. Most lenders look for roughly 6+ months in business, consistent monthly deposits, and a cr

**`automotive-business-loans.html`** — What are automotive business loans?

- dropped words: business, carry, cash-flow, instead, need, plus, product, vehicle
- old schema answer: Automotive business loans are financing for companies in the automotive sector—car dealerships, repair shops, body shops, tire and parts stores, and car washes. There is no single 

**`automotive-business-loans.html`** — What can automotive businesses use financing for?

- dropped words: assets, common, credit, include, loans, long-lived, needs, recurring, revolving, term, uses
- old schema answer: Common uses include vehicle inventory (floor plan), shop equipment, real estate or build-outs, hiring and payroll, parts inventory, marketing, and bridging seasonal slow periods. M

**`best-small-business-loans.html`** — How do I choose the right business loan?

- dropped words: advance, applying, axiant, financing, lets, multiple, need, points, questions, start, three, through
- old schema answer: Start with three questions: how fast do you need it, how much, and what is it for. Speed points to working capital or an advance; lowest cost points to SBA; flexibility points to a

**`best-small-business-loans.html`** — What is the best small business loan?

- dropped words: answer, chasing, leads, loan, longest, match, need, one-size-fits-all, option, product, rather, short-term
- old schema answer: There is no single best loan—the best option depends on your goal. For the lowest rates and longest terms, an SBA 7(a) loan leads. For speed, short-term working capital wins. For f

**`business-acquisition-financing.html`** — Can you buy a business with an SBA loan?

- dropped words: acquiring, because, close, included, repayment, stretches, thorough, without
- old schema answer: Yes. The SBA 7(a) program is the most common way to finance a business acquisition in the U.S. It funds up to $5 million, stretches repayment to 10 years for a business without rea

**`business-acquisition-financing.html`** — How do I choose a business acquisition lender?

- dropped words: across, bank, cash-flow, closing, first, injection, knows, look, offer, rather, sell, side
- old schema answer: Match the lender to the deal rather than taking the first offer. Compare across structures: an SBA lender for a cash-flow business with a modest down payment, a conventional bank f

**`business-acquisition-financing.html`** — How much down payment do you need to buy a business?

- dropped words: against, allow, borrowing, instead, lenders, portfolio, portion, targets, term
- old schema answer: For an SBA 7(a) acquisition, the SBA requires a minimum 10% equity injection, and a portion of that can sometimes come from a seller note that is on full standby for the loan's ter

**`business-acquisition-financing.html`** — What are typical business acquisition loan rates?

- dropped words: 2026, commonly, deal, depend, digits, double, illustration, low-double, low-to-mid, mid-single, often, page
- old schema answer: Rates depend on the structure and the deal. As an illustration, SBA 7(a) acquisition loans are commonly priced as a variable rate tied to the prime rate (often in the low-to-mid do

**`business-acquisition-financing.html`** — What do lenders look for in a business acquisition loan?

- dropped words: both, business, businesss, deal, debt, debt-service-coverage, discretionary, earnings, financials, focus, help, lenders
- old schema answer: Lenders focus on the target's cash flow first: they want the business's seller's discretionary earnings (SDE) or EBITDA to cover the new debt payment with a debt-service-coverage r

**`business-acquisition-financing.html`** — What is business acquisition financing?

- dropped words: about, acquisition, against, bank, buyer, carry, investment, much, portfolio, purchase, several, structures
- old schema answer: Business acquisition financing is funding used to buy an existing business or franchise. It is an umbrella for several structures: SBA 7(a) acquisition loans, conventional bank ter

**`business-debt-relief/articles/mca-froze-my-bank-account/index.html`** — How do I get my frozen business bank account released?

- dropped words: attorney, improperly, matters, obtained, releases, resolution, speed, through
- old schema answer: There are three common routes: (1) negotiate a payoff or settlement with the funder so it releases the restraint, (2) move the underlying debt into a structured resolution through 

**`business-growth/articles/cold-email-deliverability-domains-warmup-inbox/index.html`** — How long does domain warmup take?

- dropped words: domain, fastest, inbox, increase, number, plan, sends
- old schema answer: Plan on roughly two to four weeks. Start with a small number of sends per inbox per day and increase gradually while engagement stays healthy. Rushing warmup is the fastest way to 

**`business-growth/articles/cold-email-deliverability-domains-warmup-inbox/index.html`** — Should I send cold email from my main domain?

- dropped words: deliverability, keep, look-alike, often, per-domain, safe, suffers, variations, volume
- old schema answer: No. Use separate sending domains (often look-alike variations) so that if deliverability suffers, your primary domain's reputation and normal business email stay protected. Many te

**`business-growth/articles/cold-email-deliverability-domains-warmup-inbox/index.html`** — What are SPF, DKIM, and DMARC?

- dropped words: allowed, checks, cold, cryptographically, domain, fails, lists, message, receiving, send, servers, should
- old schema answer: They are DNS records that prove your email is legitimate. SPF lists the servers allowed to send for your domain, DKIM cryptographically signs your messages, and DMARC tells receivi

**`business-growth/articles/fresh-leads-vs-bought-lists-pipeline-quality/index.html`** — Are bought lead lists worth it?

- dropped words: bounce, change, companies, freshly, high, lists, many, non-compliant, often, people, purchased, quickly
- old schema answer: Usually not. Purchased lists are typically resold many times, go stale quickly as people change roles and companies, and often contain inaccurate or non-compliant contacts. The res

**`business-growth/articles/fresh-leads-vs-bought-lists-pipeline-quality/index.html`** — How do I get fresh leads instead of buying lists?

- dropped words: customer, decays, ideal, lists, match, one-time, opposed, profile, purchased
- old schema answer: Define a tight ideal customer profile, then source contacts that match it from current data rather than recycled lists. Tools that discover and verify prospects on an ongoing basis

**`business-growth/articles/fresh-leads-vs-bought-lists-pipeline-quality/index.html`** — What makes a lead high quality?

- dropped words: company, customer, dozens, hammered, high-quality, holds, ideal, lead, other, person, profile, role
- old schema answer: Relevance and freshness. A high-quality lead matches your ideal customer profile, is current (the person still holds the role at the company), is accurately contactable, and has no

**`business-growth/articles/fresh-leads-vs-bought-lists-pipeline-quality/index.html`** — Why do purchased lists hurt deliverability?

- dropped words: bounce, cause, contain, rates, sending, signals
- old schema answer: Old lists contain invalid addresses and spam traps, which cause high bounce rates and complaints. Mailbox providers read those signals as spammer behavior and damage your sending r

**`business-line-of-credit/articles/what-are-typical-business-line-of-credit-rates/index.html`** — Does frequent line usage help reduce rates over time?

- dropped words: $250,000, $50,000, 2026, above, accepting, access, accordingly, across, actual, actually, additional, adjusted
- old schema answer: It can. Strong repayment behavior and healthy deposit trends may improve renewal terms with some lenders. Most borrowers compare line offers on APR only, but total cost often shift

**`business-loans-california.html`** — Are there business loans for California agriculture?

- dropped words: calendar, cold, crop, especially, harvesters, line, makes, revolving, storage, valuable
- old schema answer: Yes. Central Valley farms use equipment financing for tractors, harvesters, and irrigation, seasonal lines of credit to bridge planting and harvest, and term loans for facilities a

**`commercial-bridge-loans/articles/why-bridge-loan-timeline-keeps-slipping/index.html`** — Why does my bridge loan timeline keep slipping?

- dropped words: causes, common, complete, delays, docs, early, hours, ordering, packaging, response, within
- old schema answer: Common causes: appraisal or valuation delays, title or survey issues, incomplete documentation, slow response to lender conditions, or lender backlog. Fix by ordering appraisal and

**`commercial-real-estate-loans/articles/cash-out-refinance-commercial-property/index.html`** — Can I do a cash-out refinance on an investment property?

- dropped words: allow, cash-out, deals, lenders, limits, many, refinance, stricter, though
- old schema answer: Yes. Many lenders allow cash-out refinance on investment commercial properties, though leverage limits and DSCR requirements are often stricter than owner-occupied deals.

**`construction-business-financing/working-capital-subcontractors-invoices/index.html`** — How fast can subcontractors get working capital financing?

- dropped words: approval, bank, contracts, proof, statements, subcontractor, support, work
- old schema answer: Lines of credit and working capital loans can fund in days to a few weeks depending on lender and documentation. Bank statements, contracts, and proof of subcontractor work support

**`construction-business-financing/working-capital-subcontractors-invoices/index.html`** — What credit score do subcontractors need for working capital

- dropped words: capital, credit, lender, line, odds, requirements, vary, working
- old schema answer: Requirements vary by lender. Many working capital and line of credit programs look for 600+ FICO. Strong revenue, clean bank statements, and solid contracts improve approval odds.

**`corporate-and-asset-finance.html`** — Is corporate and asset finance the same as equipment financi

- dropped words: across, assets, broader, machine, need, options, start, vehicle, weighing
- old schema answer: Equipment financing is one part of it. Corporate and asset finance is the broader category that also includes asset-based lending, working capital, and commercial real estate. If y

**`corporate-and-asset-finance.html`** — What are typical asset finance rates and terms?

- dropped words: 24-84, borrower, calculator, commercial, depend, estate, estimate, matched, month, options, page, payment
- old schema answer: Rates depend on the structure, the asset, and the borrower. Equipment finance commonly runs 24-84 month terms, asset-based lines price off the collateral, and SBA and commercial re

**`corporate-and-asset-finance.html`** — What is corporate and asset finance?

- dropped words: against, already, asset, borrowing, corporate, inventory, leases, loans, machinery, receivables, technology, vehicles
- old schema answer: Corporate and asset finance is business funding that is used to acquire assets or secured by assets the business owns. It is the umbrella for equipment finance (loans and leases fo

**`corporate-and-asset-finance.html`** — What is the difference between asset finance and asset-based

- dropped words: accounts, acquire, borrow, financing, lease, receivable, reverse, short, vehicle
- old schema answer: Asset finance funds the purchase of a new asset: you borrow or lease to acquire equipment or a vehicle, and that asset secures the financing. Asset-based lending (ABL) is the rever

**`corporate-and-asset-finance.html`** — What types of assets can a business finance?

- dropped words: asset-based, categories, common, financed, lending, software
- old schema answer: Common categories are equipment and machinery, commercial vehicles and trucks, technology and software, commercial real estate, and current assets like receivables and inventory th

**`corporate-and-asset-finance.html`** — Who qualifies for corporate and asset finance?

- dropped words: 24-48, 650-680, fund, hours, itself, longer, programs, qualify, sba-backed, start, take
- old schema answer: Most established U.S. businesses qualify. Equipment finance programs often start around 550+ FICO and can fund in 24-48 hours; SBA-backed options favor 650-680+ and take longer; as

**`equipment-appraisal.html`** — Can I use an equipment appraisal to get a loan?

- dropped words: back, borrow, cash, keep, lease, lessor, sell
- old schema answer: Yes. An appraisal is often the first step in raising capital against equipment you own. Once the value is established you can access it through a sale-leaseback (sell the equipment

**`equipment-financing/articles/3d-printer-financing/index.html`** — Should I lease or buy a 3D printer?

- dropped words: $1-buyout, because, case, depreciate, iterates, leasing, popular, production, stable
- old schema answer: FMV leasing is popular in additive because the technology iterates quickly and you may want to upgrade in a few years. Buy (loan or $1-buyout) when you have a stable production use

**`equipment-financing/articles/commercial-printing-press-financing/index.html`** — Should I lease or buy a printing press?

- dropped words: $1-buyout, decades, depreciate, finishing, presses, youll
- old schema answer: Lease (FMV) digital presses tied to cost-per-click contracts and fast technology cycles for lower payments and easy upgrades. Buy (loan or $1-buyout) offset presses and finishing y

**`equipment-financing/articles/construction-equipment-financing-excavators-dozers/index.html`** — Can I finance used construction equipment?

- dropped words: 12-month, approval, auction, bros, carefully, check, construction, dealer, down, drive, equipment, equipments
- old schema answer: Yes — most lenders finance used construction equipment up to 8–12 years old at similar rates to new with a 12-month dealer warranty. Auction purchases (Ritchie Bros, IronPlanet) fi

**`equipment-financing/articles/equipment-financing-requirements/index.html`** — Can new businesses qualify for equipment financing?

- dropped words: additional, businesses, documentation, finance, lenders, many, newer, payments, require
- old schema answer: Yes. Many lenders finance newer businesses, but they may require stronger owner credit, additional documentation, or higher down payments than established companies.

**`equipment-financing/articles/equipment-financing-requirements/index.html`** — Do lenders verify the equipment vendor before approval?

- dropped words: collateral, fraud, reduce, risk, typically, verify
- old schema answer: Yes. Lenders typically verify the vendor, invoice details, and equipment value before funding to reduce fraud and collateral risk.

**`equipment-financing/articles/equipment-sale-leaseback-financing/index.html`** — What equipment qualifies for a sale-leaseback?

- dropped words: advance, advances, appraise, best, clean, condition, construction, existing, financing, free-and-clear, good, lenders
- old schema answer: Lenders want titled or serialized, long-lived equipment with clear resale value that you own free-and-clear or with minimal existing financing — heavy construction equipment, truck

**`equipment-financing/articles/restaurant-equipment-financing/index.html`** — Can I finance used restaurant equipment?

- dropped words: 7-10, finances, hobart, inspection, major, needs, often, older, pitco, report, shorter, standard
- old schema answer: Yes for major equipment up to 7-10 years old. Cooking equipment with strong-brand resale (Vulcan, Wolf, Hobart, Pitco) finances at standard terms. Older equipment often needs an in

**`equipment-financing/articles/woodworking-cabinet-shop-equipment-financing/index.html`** — Can I finance used woodworking machinery?

- dropped words: clean, competitive, control, edgebanders, feed, generation, keep, makers, records, reputable, spindle, terms
- old schema answer: Yes. CNC routers, edgebanders, and saws from reputable makers hold value and finance well. Lenders weigh spindle/feed hours and the control generation; clean records keep terms com

**`equipment-for-sale/vacuum-trucks/index.html`** — Can I finance a septic or vacuum truck, new or used?

- dropped words: axiant, guide, read, septic, terms, through, used
- old schema answer: Yes — both new and used. Truck financing is asset-based, so the equipment carries much of the deal. Apply once through Axiant to get matched with terms, or read our guide on financ

**`equipment-for-sale/vacuum-trucks/index.html`** — What is a vacuum truck used for?

- dropped words: away, blower, different, pump, sanitation, slurry, using, work
- old schema answer: A vacuum truck pumps liquids, slurry and waste into an onboard tank using a vacuum pump or blower, then hauls it away. In septic and portable sanitation work it pumps septic tanks,

**`equipment/bulldozers/used-bulldozer-financing/index.html`** — Do used bulldozers require a larger down payment?

- dropped words: increase, lender, resale, risk, uncertainty, undercarriage, wear
- old schema answer: Yes. Used equipment typically requires 10-20% down versus 0-10% for new. Undercarriage wear and resale uncertainty increase lender risk. Strong credit (680+) may qualify for 10% do

**`equipment/bulldozers/used-bulldozer-financing/index.html`** — What credit score is needed for used bulldozer financing?

- dropped words: asset-backed, bulldozers, equipment, financing, terms, used
- old schema answer: Most lenders look for 600+ FICO. Scores of 680+ qualify for the best rates and terms on used bulldozers. Equipment financing is asset-backed, so some programs work with 580+ when r

**`equipment/bulldozers/used-bulldozer-financing/index.html`** — What do lenders look at when financing a used bulldozer?

- dropped words: best, caterpillar, deere, hold, john, komatsu, value
- old schema answer: Lenders evaluate brand, model, age, hours, undercarriage condition, and maintenance history. Caterpillar, Komatsu, and John Deere hold value best. A pre-purchase inspection and doc

**`equipment/bulldozers/used-bulldozer-financing/index.html`** — What is the maximum age for used bulldozer financing?

- dropped words: caterpillar, down, equipment, komatsu, larger, like, older, payments, programs, require, specialty
- old schema answer: Most lenders finance bulldozers up to 5-7 years old. Some programs extend to 10 years for low-hour, well-maintained machines from strong brands like Caterpillar or Komatsu. Older e

**`equipment/commercial-kitchen/commercial-kitchen-lease-vs-buy/index.html`** — Is it better to lease or buy commercial kitchen equipment?

- dropped words: answer, cash, claim, deductibility, depreciation, easier, equipment, flow, follows, full, horizon, keep
- old schema answer: Buy if you will keep the equipment long-term and want to build equity and claim depreciation; lease if you want lower payments, easier upgrades, and full deductibility of the payme

**`equipment/excavators/excavator-lease-vs-loan/index.html`** — Are excavator lease payments tax deductible?

- dropped words: asset, deduct, depreciate, differs, interest, loans, where
- old schema answer: Yes. Operating lease payments are typically fully deductible as a business expense in the year paid. This differs from loans, where you deduct interest and depreciate the asset. Co

**`equipment/excavators/excavator-lease-vs-loan/index.html`** — What is the typical term for an excavator lease?

- dropped words: align, business, equipments, life, needs, useful
- old schema answer: Excavator leases typically run 36-60 months. Terms align with the equipment's useful life and your business needs. Shorter terms (36 months) may have higher payments but faster upg

**`equipment/excavators/used-excavator-financing/index.html`** — Do used excavators require a larger down payment?

- dropped words: depreciation, increase, lender, resale, risk, uncertainty
- old schema answer: Yes. Used equipment typically requires 10-20% down versus 0-10% for new. Depreciation and resale uncertainty increase lender risk. Strong credit (680+) may qualify for 10% down on 

**`equipment/excavators/used-excavator-financing/index.html`** — Should I get a pre-purchase inspection before financing a us

- dropped words: dealers, hours, issues, many, potential, provide, reports
- old schema answer: Yes. A third-party inspection documents condition, hours, and potential issues. It protects you and can help lenders structure financing. Many dealers provide inspection reports; i

**`equipment/excavators/used-excavator-financing/index.html`** — What credit score is needed for used excavator financing?

- dropped words: asset-backed, equipment, excavators, financing, terms, used
- old schema answer: Most lenders look for 600+ FICO. Scores of 680+ qualify for the best rates and terms on used excavators. Equipment financing is asset-backed, so some programs work with 580+ when r

**`equipment/flatbed-trucks/flatbed-truck-financing-haulers/index.html`** — Flatbed vs step-deck: which is easier to finance?

- dropped words: common, flatbeds, resale, similar, step-decks, value
- old schema answer: Both are routinely financed. Flatbeds are more common; step-decks have similar resale value. Include specs (length, axles, load capacity) in your quote.

**`equipment/forklifts/used-forklift-financing/index.html`** — Can you finance a used forklift?

- dropped words: 36-60, affect, approval, brand, capacity, condition, hours, lift, months, rates, trucks, typically
- old schema answer: Yes. Most equipment lenders finance used forklifts typically 5-7 years old or newer. Used lift trucks may require 10-20% down and shorter terms (36-60 months). Brand, hours, condit

**`equipment/forklifts/used-forklift-financing/index.html`** — Do used forklifts require a larger down payment?

- dropped words: affect, battery, condition, electric, overall, terms
- old schema answer: Yes. Used equipment typically requires 10-20% down versus 0-10% for new. Battery age (for electric) and overall condition affect terms.

**`equipment/forklifts/used-forklift-financing/index.html`** — Electric or propane: which used forklifts are easier to fina

- dropped words: crown, engine, forklifts, hours, hyster, propane, toyota, yale
- old schema answer: Both are routinely financed. Electric forklifts may have battery condition considerations; propane units have engine hours. Strong brands (Toyota, Crown, Hyster, Yale) hold value f

**`equipment/forklifts/used-forklift-financing/index.html`** — What credit score is needed for used forklift financing?

- dropped words: asset-backed, best, equipment, financing, qualify, rates, scores
- old schema answer: Most lenders look for 600+ FICO. Scores of 680+ qualify for the best rates. Equipment financing is asset-backed; some programs work with 580+ when revenue and down payment are stro

**`equipment/forklifts/used-forklift-financing/index.html`** — What is the maximum age for used forklift financing?

- dropped words: crown, different, electric, hyster, like, limits, programs, toyota
- old schema answer: Most lenders finance forklifts up to 5-7 years old. Some programs extend to 10 years for low-hour, well-maintained units from strong brands like Toyota, Crown, or Hyster. Electric 

**`equipment/injection-molding/injection-molding-equipment-financing/index.html`** — How much does an injection molding machine cost?

- dropped words: $150k-$400k, 200-500, 50-100, injection, mid-size, molding, shot, size
- old schema answer: Injection molding machines run $50,000-$1,000,000+ depending on clamp tonnage and shot size. Small machines (50-100 ton) $50K-$150K; mid-size (200-500 ton) $150K-$400K; large (500+

**`equipment/injection-molding/injection-molding-equipment-financing/index.html`** — Lease or buy injection molding equipment?

- dropped words: build, cash, cycle, equipment, equity, flexibility, flow, loans, manage, upgrade
- old schema answer: Leasing is popular—lower payments, preserve capital, upgrade flexibility. Loans build equity. Molders often lease to manage cash flow and cycle equipment.
