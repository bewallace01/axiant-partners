# -*- coding: utf-8 -*-
"""Batch 1 of the DSCR cluster - articles 1-3 of 14.

Figures here describe ranges that are conventional across DSCR lenders, stated
as ranges rather than as any lender's quote. No funded totals, no years in
business, no testimonials, no named lender rates. One entity throughout:
Axiant Partners, (561) 268-0465, Boca Raton.
"""

SBA_NOTE = ("https://www.sba.gov/funding-programs/loans/504-loans",
            "SBA 504 Loan Program",
            "The federal program most often compared against a DSCR loan for "
            "owner-occupied property, and the reason DSCR is the investor's "
            "route rather than the occupier's.")
SLOOS = ("https://www.federalreserve.gov/data/sloos.htm",
         "Federal Reserve Senior Loan Officer Opinion Survey",
         "Quarterly survey of bank lending standards, including commercial "
         "real estate. The public record of whether underwriting is tightening.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research and rulemaking on business credit disclosure, including how "
        "cost is presented to borrowers.")
IRS_527 = ("https://www.irs.gov/publications/p527",
           "IRS Publication 527: Residential Rental Property",
           "The federal definition of rental income and deductible expenses - "
           "the same schedule an underwriter reads when your return is on file.")
HUD_MF = ("https://www.hud.gov/program_offices/housing/mfh",
          "HUD Multifamily Housing Programs",
          "Federal multifamily programs and their equity requirements, the "
          "benchmark conventional multifamily terms are quoted against.")
CENSUS_HV = ("https://www.census.gov/housing/hvs/index.html",
             "U.S. Census Bureau Housing Vacancy Survey",
             "Quarterly rental vacancy rates by region - the public check on "
             "whether a market rent assumption is realistic.")

ARTICLES = [
    # ------------------------------------------------------------------ 1 --
    {
        "slug": "how-dscr-is-calculated",
        "crumb": "How DSCR Is Calculated",
        "title": "How DSCR Is Calculated: The Formula, Worked Through | Axiant",
        "og_title": "How DSCR Is Calculated: The Formula, Worked Through",
        "h1": "How DSCR Is Calculated",
        "headline": "How DSCR Is Calculated",
        "lede": "The ratio that decides a DSCR loan, worked end to end - what "
                "goes in the numerator, what goes in the denominator, and where "
                "deals fall apart",
        "meta_desc": "DSCR is net operating income divided by annual debt service. "
                     "See the formula worked end to end, what underwriters put in each "
                     "half, and why taxes and insurance move the ratio most.",
        "article_desc": "The DSCR formula worked end to end, including what "
                        "underwriters count as net operating income and what they "
                        "include in debt service.",
        "keywords": "how is dscr calculated, dscr formula, debt service coverage ratio, "
                    "dscr calculation example, net operating income, piti dscr",
        "quick_answer": "DSCR is <strong>net operating income divided by annual debt "
                        "service</strong>. A property producing $60,000 in net operating "
                        "income against $50,000 of annual mortgage payments has a DSCR of "
                        "<strong>1.20</strong> &mdash; it earns 20% more than it owes. Most "
                        "lenders want at least 1.00, and commonly 1.20 to 1.25, so the "
                        "arithmetic is worth doing before you apply rather than after.",
        "sections": [
            ("The Formula",
             "<p>Every DSCR lender uses the same two-part equation:</p>"
             "<p><strong>DSCR = Net Operating Income &divide; Annual Debt Service</strong></p>"
             "<p>The elegance is also the trap. Both halves look obvious and neither is. "
             "Two underwriters handed the same property routinely produce different "
             "ratios, because they disagree about what belongs in each half &mdash; not "
             "about how to divide.</p>"
             "<p>A ratio of 1.00 means the property exactly covers its debt. Below 1.00 "
             "it does not, and the shortfall comes out of your pocket every month. Above "
             "1.00 there is a cushion, and the size of that cushion is what you are "
             "really negotiating.</p>"),
            ("What Counts as Net Operating Income",
             "<p>Net operating income is gross rental income minus operating expenses, "
             "before any mortgage payment. The mortgage is excluded deliberately: putting "
             "it in both halves would make the ratio meaningless.</p>"
             "<p>What underwriters typically include as expenses:</p>"
             "<ul>"
             "<li><strong>Property taxes</strong> &mdash; at the reassessed figure after "
             "your purchase, not the seller's current bill</li>"
             "<li><strong>Insurance</strong> &mdash; at a bound quote, not last year's premium</li>"
             "<li><strong>HOA dues</strong> where they apply</li>"
             "<li><strong>Property management</strong> &mdash; commonly underwritten at a "
             "percentage of gross rent even when you self-manage</li>"
             "<li><strong>Vacancy allowance</strong> &mdash; a deduction for the weeks the "
             "unit sits empty between tenants</li>"
             "<li><strong>Maintenance and reserves</strong> on many programs</li>"
             "</ul>"
             "<p>What does not belong: your mortgage payment, capital improvements, "
             "depreciation, and your own labour. Depreciation catches people out most "
             "often, because it is the single biggest line on many Schedule Es and it is "
             "a tax concept, not a cash one.</p>"),
            ("What Counts as Debt Service",
             "<p>Debt service is twelve months of payments on the loan being underwritten. "
             "Whether that means principal and interest only, or the full PITI figure, is "
             "the most consequential difference between programs.</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>What the denominator includes</th><th>Effect on the ratio</th>"
             "<th>Where you see it</th></tr></thead><tbody>"
             "<tr><td data-label=\"Includes\">Principal + interest only</td>"
             "<td data-label=\"Effect\">Highest ratio</td>"
             "<td data-label=\"Where\">Some portfolio programs; taxes and insurance are "
             "then usually caught in the expense side instead</td></tr>"
             "<tr><td data-label=\"Includes\">PITI &mdash; principal, interest, taxes, insurance</td>"
             "<td data-label=\"Effect\">Lower ratio</td>"
             "<td data-label=\"Where\">The common convention on single-family rentals</td></tr>"
             "<tr><td data-label=\"Includes\">PITIA &mdash; PITI plus HOA dues</td>"
             "<td data-label=\"Effect\">Lowest ratio</td>"
             "<td data-label=\"Where\">Condos and any property with an association</td></tr>"
             "</tbody></table></div>"
             "<p>Ask which convention a lender uses before comparing two quotes. The same "
             "property can present as 1.25 under one definition and below 1.00 under "
             "another, and neither underwriter has done anything wrong.</p>"),
            ("A Worked Example",
             "<p>Take a single-family rental bought for $300,000, renting at $2,400 a "
             "month, financed with a $225,000 loan.</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Line</th><th>Monthly</th><th>Annual</th></tr></thead><tbody>"
             "<tr><td data-label=\"Line\">Gross rent</td><td data-label=\"Monthly\">$2,400</td>"
             "<td data-label=\"Annual\">$28,800</td></tr>"
             "<tr><td data-label=\"Line\">Less vacancy allowance (5%)</td>"
             "<td data-label=\"Monthly\">&minus;$120</td><td data-label=\"Annual\">&minus;$1,440</td></tr>"
             "<tr><td data-label=\"Line\">Less property management (8%)</td>"
             "<td data-label=\"Monthly\">&minus;$192</td><td data-label=\"Annual\">&minus;$2,304</td></tr>"
             "<tr><td data-label=\"Line\">Less maintenance reserve</td>"
             "<td data-label=\"Monthly\">&minus;$120</td><td data-label=\"Annual\">&minus;$1,440</td></tr>"
             "<tr><td data-label=\"Line\"><strong>Net operating income</strong></td>"
             "<td data-label=\"Monthly\"><strong>$1,968</strong></td>"
             "<td data-label=\"Annual\"><strong>$23,616</strong></td></tr>"
             "<tr><td data-label=\"Line\">Principal &amp; interest</td>"
             "<td data-label=\"Monthly\">$1,480</td><td data-label=\"Annual\">$17,760</td></tr>"
             "<tr><td data-label=\"Line\">Taxes</td><td data-label=\"Monthly\">$310</td>"
             "<td data-label=\"Annual\">$3,720</td></tr>"
             "<tr><td data-label=\"Line\">Insurance</td><td data-label=\"Monthly\">$135</td>"
             "<td data-label=\"Annual\">$1,620</td></tr>"
             "<tr><td data-label=\"Line\"><strong>Annual debt service (PITI)</strong></td>"
             "<td data-label=\"Monthly\"><strong>$1,925</strong></td>"
             "<td data-label=\"Annual\"><strong>$23,100</strong></td></tr>"
             "</tbody></table></div>"
             "<p>$23,616 &divide; $23,100 = <strong>1.02</strong>. The property clears its "
             "debt, but only just. On a program wanting 1.20 this file does not work as "
             "structured &mdash; and the fix is arithmetic, not persuasion: a larger down "
             "payment, a longer amortization, or a different property.</p>"
             "<p>Notice how thin the margin is. A $200-a-month miss on the insurance quote "
             "is enough to push this below 1.00.</p>"),
            ("Where the Ratio Usually Breaks",
             "<p>In practice, four things move a DSCR calculation more than anything else:</p>"
             "<ul>"
             "<li><strong>Reassessed property taxes.</strong> Buyers budget the seller's "
             "tax bill. In states that reassess on sale, the real number can be "
             "substantially higher, and it lands entirely in the denominator.</li>"
             "<li><strong>Insurance quotes.</strong> In coastal and wildfire markets "
             "premiums have moved sharply. A stale estimate is the most common reason a "
             "file that penciled at application fails at underwriting.</li>"
             "<li><strong>Management fees you did not plan to pay.</strong> Many programs "
             "impute a management cost whether or not you use a manager.</li>"
             "<li><strong>Optimistic rent.</strong> Underwriters generally take the lower "
             "of the lease and the appraiser's market rent opinion, so an above-market "
             "lease does not lift the ratio.</li>"
             "</ul>"
             "<p>Run your own numbers with the reassessed tax figure and a bound insurance "
             "quote before you apply. It is the cheapest way to find out whether a deal "
             "works. Our <a href=\"/dscr-calculator.html\">DSCR calculator</a> takes the "
             "same inputs an underwriter uses.</p>"),
            ("How to Improve a Ratio That Falls Short",
             "<p>A DSCR below the program minimum is a structuring problem, and it has a "
             "small number of levers:</p>"
             "<ul>"
             "<li><strong>Increase the down payment.</strong> A smaller loan means smaller "
             "debt service, and this is the most direct lever there is.</li>"
             "<li><strong>Extend the amortization.</strong> A longer schedule lowers the "
             "monthly payment and lifts the ratio, at the cost of more total interest.</li>"
             "<li><strong>Consider an interest-only period</strong> where a program offers "
             "one. It reduces debt service during the interest-only term, which some "
             "lenders will underwrite to.</li>"
             "<li><strong>Buy down the rate.</strong> Points paid at closing lower the "
             "payment and can lift the ratio over a threshold.</li>"
             "<li><strong>Challenge the expense assumptions</strong> with evidence &mdash; "
             "a bound insurance quote below the underwriter's estimate is a legitimate, "
             "documentable correction.</li>"
             "</ul>"
             "<p>What does not help: a strong personal balance sheet. That is the point of "
             "a DSCR loan, and it cuts both ways. See "
             "<a href=\"/dscr-loan-requirements.html\">DSCR loan requirements</a> for the "
             "thresholds each of these has to clear.</p>"),
        ],
        "faqs": [
            ("What is a good DSCR for a rental property?",
             "<strong>1.20 to 1.25</strong> is comfortable on most programs, and "
             "<strong>1.00</strong> is the common floor &mdash; at 1.00 the property "
             "exactly covers its debt with nothing spare. Some lenders will go below 1.00 "
             "with compensating factors such as a larger down payment or reserves, and "
             "price accordingly."),
            ("Does DSCR include taxes and insurance?",
             "It depends on the program, and this is the most consequential difference "
             "between two DSCR quotes. Many single-family rental programs use "
             "<strong>PITI</strong> &mdash; principal, interest, taxes and insurance "
             "&mdash; and condos usually add HOA dues to make <strong>PITIA</strong>. "
             "Others use principal and interest only and account for taxes and insurance "
             "as operating expenses instead. Ask before you compare."),
            ("Is depreciation included in the DSCR calculation?",
             "No. Depreciation is a tax deduction, not a cash expense, so it is excluded "
             "from net operating income. This surprises owners who read their Schedule E "
             "and see depreciation as the largest line on the page."),
            ("Can you get a DSCR loan below 1.0?",
             "Sometimes. Programs exist for ratios under 1.00, and occasionally with no "
             "ratio test at all, but they carry higher rates, larger down payments, or "
             "reserve requirements. The shortfall is real: below 1.00 the property does "
             "not cover its own debt and you fund the difference every month."),
            ("What rent do underwriters use if my lease is above market?",
             "Generally the lower of the two. Underwriters compare the signed lease "
             "against the appraiser's market rent opinion, usually a Form 1007 rent "
             "schedule, and take the conservative figure. An above-market lease does not "
             "lift the ratio, though it does help the property perform in reality."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("/dscr-loan-requirements.html", "DSCR loan requirements"),
            ("/dscr-calculator.html", "DSCR calculator"),
            ("../what-counts-as-rental-income-dscr/", "What counts as rental income on a DSCR loan"),
        ],
        "sources": [IRS_527, SLOOS, CENSUS_HV],
    },

    # ------------------------------------------------------------------ 2 --
    {
        "slug": "what-counts-as-rental-income-dscr",
        "crumb": "What Counts as Rental Income",
        "title": "What Counts as Rental Income on a DSCR Loan | Axiant",
        "og_title": "What Counts as Rental Income on a DSCR Loan",
        "h1": "What Counts as Rental Income on a DSCR Loan",
        "headline": "What Counts as Rental Income on a DSCR Loan",
        "lede": "Which income an underwriter credits toward the ratio, which "
                "gets struck out, and how to document the difference",
        "meta_desc": "DSCR underwriters count the lower of the signed lease and the "
                     "appraiser's market rent. See what income is credited, what is struck "
                     "out, and how vacant, short-term and multi-unit properties are treated.",
        "article_desc": "Which rental income counts toward a DSCR loan, which is "
                        "excluded, and how underwriters document each case.",
        "keywords": "what counts as rental income dscr, dscr rental income, form 1007 "
                    "market rent, dscr vacant property, gross rent dscr",
        "quick_answer": "Underwriters generally credit <strong>the lower of the signed "
                        "lease and the appraiser's market rent opinion</strong>, before "
                        "expenses. Base rent counts; most of what tenants pay on top of it "
                        "&mdash; pet fees, parking, late charges, utility reimbursements "
                        "&mdash; usually does not. A vacant property is not disqualifying: "
                        "it is underwritten on market rent alone.",
        "sections": [
            ("The Rule Underwriters Actually Apply",
             "<p>The income half of a DSCR calculation is not simply what a tenant pays "
             "you. It is the more conservative of two figures:</p>"
             "<ul>"
             "<li><strong>The signed lease</strong> &mdash; the contractual rent on the "
             "property today</li>"
             "<li><strong>The appraiser's market rent opinion</strong> &mdash; usually a "
             "Form 1007 single-family comparable rent schedule, or a Form 1025 for two- "
             "to four-unit property</li>"
             "</ul>"
             "<p>Take the lower. That single rule explains most of the gap between what "
             "an owner expects and what an underwriter produces. If your lease is $2,600 "
             "and the appraiser says the market is $2,300, the ratio is built on $2,300.</p>"
             "<p>It works the other way too. If you have deliberately kept a good tenant "
             "below market, the appraisal can lift the underwritten figure above your "
             "lease &mdash; though many programs cap how far above the lease they will go.</p>"),
            ("What Is Credited",
             "<p>Base rent under an arm's-length lease is the core of it. Beyond that, "
             "treatment varies by program, but the common pattern is:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Income</th><th>Usual treatment</th><th>Why</th></tr></thead><tbody>"
             "<tr><td data-label=\"Income\">Base monthly rent</td>"
             "<td data-label=\"Treatment\">Counted</td>"
             "<td data-label=\"Why\">Contractual and verifiable against the lease</td></tr>"
             "<tr><td data-label=\"Income\">Market rent on a vacant unit</td>"
             "<td data-label=\"Treatment\">Counted</td>"
             "<td data-label=\"Why\">Supported by the appraiser's rent schedule</td></tr>"
             "<tr><td data-label=\"Income\">Rent from each unit of a 2&ndash;4 unit property</td>"
             "<td data-label=\"Treatment\">Counted</td>"
             "<td data-label=\"Why\">Underwritten per unit, then totalled</td></tr>"
             "<tr><td data-label=\"Income\">Pet rent, parking, storage</td>"
             "<td data-label=\"Treatment\">Usually excluded</td>"
             "<td data-label=\"Why\">Treated as ancillary and not durable</td></tr>"
             "<tr><td data-label=\"Income\">Utility reimbursements</td>"
             "<td data-label=\"Treatment\">Usually excluded</td>"
             "<td data-label=\"Why\">Offsets a cost rather than adding income</td></tr>"
             "<tr><td data-label=\"Income\">Late fees, one-off charges</td>"
             "<td data-label=\"Treatment\">Excluded</td>"
             "<td data-label=\"Why\">Not recurring</td></tr>"
             "<tr><td data-label=\"Income\">Rent from a family member below market</td>"
             "<td data-label=\"Treatment\">Scrutinised</td>"
             "<td data-label=\"Why\">Not arm's length; market rent usually governs</td></tr>"
             "</tbody></table></div>"
             "<p>If a meaningful share of your income is ancillary, say so early. It rarely "
             "helps the ratio, and finding out at underwriting is worse than finding out "
             "at application.</p>"),
            ("Vacant Properties Are Not Disqualifying",
             "<p>One of the genuine advantages of DSCR underwriting is that a property "
             "with no tenant can still be financed. There is no lease to read, so the "
             "appraiser's market rent opinion carries the whole income side.</p>"
             "<p>That makes the appraisal unusually important. On a tenanted property a "
             "weak rent opinion is bounded by the lease; on a vacant one it is the only "
             "number in play. It is worth giving the appraiser genuine comparable rentals "
             "rather than leaving the selection entirely to them.</p>"
             "<p>Some programs apply a larger vacancy deduction, a lower maximum "
             "loan-to-value, or both, on a property that is not yet rented. Ask which "
             "applies before you assume a vacant purchase prices the same as a tenanted one.</p>"),
            ("Short-Term and Seasonal Rent",
             "<p>Income from short-term letting is treated differently again, and by no "
             "means every DSCR lender accepts it. Where it is accepted, the usual "
             "evidence is a trailing twelve months of platform statements, sometimes "
             "averaged against a market rent opinion for long-term use as a floor.</p>"
             "<p>Seasonal properties raise the same question in a different form: twelve "
             "months of income arriving in five. Underwriters generally annualise and then "
             "apply a heavier vacancy assumption. We cover this in full in "
             "<a href=\"../dscr-loans-short-term-rentals/\">DSCR loans for short-term "
             "rentals</a>.</p>"),
            ("How to Document It",
             "<p>The paperwork is short, and having it ready is the difference between a "
             "quick file and a slow one:</p>"
             "<ul>"
             "<li><strong>The current lease</strong>, signed and dated, for every occupied unit</li>"
             "<li><strong>Proof the rent is actually paid</strong> &mdash; typically bank "
             "statements showing the deposits, on many programs</li>"
             "<li><strong>The appraisal with a rent schedule</strong> &mdash; Form 1007 for "
             "single-family, Form 1025 for two to four units</li>"
             "<li><strong>Platform statements</strong> where short-term income is being used</li>"
             "<li><strong>A rent roll</strong> where the property has several units</li>"
             "</ul>"
             "<p>What you are not asked for is the point of the product: no tax returns, no "
             "W-2s, no debt-to-income calculation. If a lender starts asking for personal "
             "income documents on a DSCR file, ask why.</p>"),
        ],
        "faqs": [
            ("Do underwriters use my actual rent or market rent?",
             "Generally the lower of the two. The signed lease is compared against the "
             "appraiser's market rent opinion &mdash; a Form 1007 for single-family or "
             "Form 1025 for two to four units &mdash; and the conservative figure is used. "
             "An above-market lease does not lift the ratio."),
            ("Can I get a DSCR loan on a vacant property?",
             "Yes. With no lease to read, the appraiser's market rent opinion carries the "
             "entire income side of the calculation. Some programs apply a larger vacancy "
             "deduction or a lower maximum loan-to-value on an unrented property, so "
             "confirm the terms before assuming they match a tenanted purchase."),
            ("Does pet rent or parking income count toward DSCR?",
             "Usually not. Most programs credit base rent only and treat pet rent, "
             "parking, storage and utility reimbursements as ancillary income that is not "
             "durable enough to underwrite. Late fees and one-off charges are excluded "
             "outright."),
            ("How is rental income counted on a duplex or fourplex?",
             "Per unit, then totalled. Each unit is underwritten against its own lease or "
             "market rent opinion, commonly on a Form 1025, and the sum becomes the gross "
             "income figure the ratio is built from."),
            ("Will renting to a family member cause a problem?",
             "It invites scrutiny. A below-market lease to a relative is not an arm's-length "
             "transaction, so underwriters generally fall back to the appraiser's market "
             "rent opinion. Disclose the relationship rather than let it surface later."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("../how-dscr-is-calculated/", "How DSCR is calculated"),
            ("../dscr-loans-short-term-rentals/", "DSCR loans for short-term rentals"),
            ("/dscr-loan-requirements.html", "DSCR loan requirements"),
        ],
        "sources": [IRS_527, CENSUS_HV, HUD_MF],
    },

    # ------------------------------------------------------------------ 3 --
    {
        "slug": "dscr-loans-short-term-rentals",
        "crumb": "DSCR Loans for Short-Term Rentals",
        "title": "DSCR Loans for Short-Term Rentals: Airbnb & Vrbo Income | Axiant",
        "og_title": "DSCR Loans for Short-Term Rentals: How Airbnb Income Is Treated",
        "h1": "DSCR Loans for Short-Term Rentals",
        "headline": "DSCR Loans for Short-Term Rentals",
        "lede": "How Airbnb and Vrbo income is underwritten, what evidence "
                "lenders accept, and where local regulation decides the deal",
        "meta_desc": "How DSCR lenders underwrite Airbnb and Vrbo income: trailing "
                     "12-month platform statements, market rent as a floor, heavier vacancy "
                     "assumptions, and why local short-term rental rules can end a file.",
        "article_desc": "How short-term rental income is treated on a DSCR loan, "
                        "including documentation, vacancy assumptions and regulatory risk.",
        "keywords": "dscr loan short term rental, airbnb dscr loan, vrbo financing, "
                    "short term rental loan, str dscr, airbnb investment property loan",
        "quick_answer": "Some DSCR lenders accept short-term rental income and some will "
                        "not, so the first question is whether a program allows it at all. "
                        "Where it is accepted, the usual evidence is a <strong>trailing "
                        "twelve months of platform statements</strong>, often floored "
                        "against a long-term market rent opinion, with a "
                        "<strong>heavier vacancy assumption</strong> than a standard "
                        "rental. Local short-term letting rules matter as much as the "
                        "numbers.",
        "sections": [
            ("Not Every Program Allows It",
             "<p>Short-term rental income sits outside the standard DSCR box, and lender "
             "appetite splits three ways. Some programs decline short-term income "
             "outright and will underwrite the property only on long-term market rent. "
             "Some accept it with a documented history. A smaller group actively "
             "specialises in it.</p>"
             "<p>This is the first thing to establish, because it determines everything "
             "downstream. A property that works beautifully on nightly rates may not "
             "clear the ratio at all when underwritten as a long-term rental &mdash; and "
             "if the program does not accept short-term income, that is exactly what "
             "happens.</p>"
             "<p>Ask the question before the appraisal is ordered rather than after.</p>"),
            ("How the Income Is Evidenced",
             "<p>Where short-term income is accepted, underwriters want a history rather "
             "than a projection. The common evidence:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Situation</th><th>What is usually asked for</th>"
             "<th>How it is treated</th></tr></thead><tbody>"
             "<tr><td data-label=\"Situation\">You own it and have been letting it</td>"
             "<td data-label=\"Asked for\">Trailing 12 months of platform statements</td>"
             "<td data-label=\"Treated\">Annualised, then a vacancy factor applied</td></tr>"
             "<tr><td data-label=\"Situation\">Buying a property already let short-term</td>"
             "<td data-label=\"Asked for\">Seller's platform history, where it transfers</td>"
             "<td data-label=\"Treated\">Accepted by some programs, discounted by others</td></tr>"
             "<tr><td data-label=\"Situation\">Buying to convert to short-term</td>"
             "<td data-label=\"Asked for\">No history exists</td>"
             "<td data-label=\"Treated\">Usually underwritten on long-term market rent</td></tr>"
             "<tr><td data-label=\"Situation\">Under 12 months of history</td>"
             "<td data-label=\"Asked for\">What exists, plus a market rent opinion</td>"
             "<td data-label=\"Treated\">Often floored at the long-term figure</td></tr>"
             "</tbody></table></div>"
             "<p>The pattern is consistent: a documented trailing history is credited, and "
             "a forecast is not. Projections from rental-estimate tools are not "
             "underwriting evidence, however plausible they look.</p>"),
            ("Why the Vacancy Assumption Is Heavier",
             "<p>A long-term rental is empty between tenants. A short-term rental is empty "
             "between guests, which is a different shape of risk: more turnover, more "
             "seasonality, and revenue that responds quickly to changes in demand.</p>"
             "<p>Underwriters answer that with a larger deduction from gross income than "
             "they would apply to an annual lease, and often with reserve requirements on "
             "top. The effect is that a property producing more gross revenue than a "
             "comparable long-term rental does not necessarily produce a better ratio.</p>"
             "<p>Operating costs push the same direction. Cleaning, platform fees, "
             "furnishing, utilities and higher management percentages all sit in the "
             "expense half of the calculation, and a short-term let carries more of them "
             "than a long-term one. See <a href=\"../how-dscr-is-calculated/\">how DSCR is "
             "calculated</a> for where each of these lands.</p>"),
            ("Local Rules Can End the File",
             "<p>The regulatory question is the one that most often decides a short-term "
             "rental deal, and it has nothing to do with the property's numbers.</p>"
             "<p>Cities and counties have moved in very different directions: permit "
             "caps, primary-residence requirements, outright prohibitions in some "
             "districts, minimum stay lengths, and registration regimes with real "
             "enforcement. An HOA can prohibit short-term letting even where the "
             "municipality permits it.</p>"
             "<p>Underwriters increasingly ask for evidence that the use is permitted "
             "&mdash; a registration number, a permit, or confirmation that the "
             "jurisdiction has no restriction. Where the use is not permitted, the "
             "income is generally not credited, and the property gets underwritten as a "
             "long-term rental instead.</p>"
             "<p>Check the rule before you check the rate. It is the cheaper enquiry and "
             "the more decisive one.</p>"),
            ("Structuring a File That Works",
             "<p>Practical steps that make a short-term rental file underwritable:</p>"
             "<ul>"
             "<li><strong>Confirm the program accepts short-term income</strong> in "
             "writing before ordering the appraisal.</li>"
             "<li><strong>Pull twelve months of platform statements</strong> rather than "
             "a summary dashboard export &mdash; underwriters want the statement, not the "
             "screenshot.</li>"
             "<li><strong>Get the long-term market rent opinion anyway.</strong> On many "
             "programs it is the floor, and knowing it tells you whether the deal survives "
             "a regulatory change.</li>"
             "<li><strong>Document the permit</strong> or the absence of any restriction.</li>"
             "<li><strong>Budget the real operating cost</strong>, including cleaning and "
             "platform fees, rather than the gross nightly figure.</li>"
             "<li><strong>Test the ratio at long-term rent.</strong> If it only works on "
             "nightly rates, you are carrying regulatory risk in the capital structure.</li>"
             "</ul>"
             "<p>If the deal clears on long-term rent and performs better short-term, you "
             "have a resilient file. If it only clears short-term, price that risk "
             "deliberately. Compare against "
             "<a href=\"/dscr-loan-requirements.html\">standard DSCR requirements</a> "
             "before you commit.</p>"),
        ],
        "faqs": [
            ("Can you get a DSCR loan on an Airbnb?",
             "Often, but not universally. Lender appetite splits: some programs decline "
             "short-term income and underwrite the property on long-term market rent "
             "instead, some accept it with a documented history, and a smaller group "
             "specialises in it. Establish which you are dealing with before the appraisal "
             "is ordered."),
            ("What documentation proves short-term rental income?",
             "A <strong>trailing twelve months of platform statements</strong> is the "
             "standard evidence &mdash; the statements themselves rather than a dashboard "
             "summary. Where less than twelve months exists, underwriters typically use "
             "what there is and floor it against a long-term market rent opinion."),
            ("Do projections from rental estimate tools count?",
             "No. Underwriters credit documented history, not forecasts. Estimates from "
             "third-party rental projection tools are not underwriting evidence, however "
             "reasonable the assumptions behind them."),
            ("Why is my DSCR lower than my Airbnb revenue suggests?",
             "Two reasons, both structural. Underwriters apply a heavier vacancy "
             "assumption to short-term letting than to an annual lease, and the operating "
             "costs specific to short-term rental &mdash; cleaning, platform fees, "
             "utilities, higher management percentages &mdash; all sit in the expense half "
             "of the ratio. Higher gross revenue does not automatically mean a higher DSCR."),
            ("What happens if my city bans short-term rentals?",
             "The income generally stops being credited and the property is underwritten "
             "as a long-term rental. That is why it is worth testing whether the deal "
             "clears at long-term market rent even when you intend to let it nightly "
             "&mdash; if it only works short-term, a rule change becomes a financing "
             "problem as well as an income one."),
        ],
        "related": [
            ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
            ("../what-counts-as-rental-income-dscr/", "What counts as rental income on a DSCR loan"),
            ("../how-dscr-is-calculated/", "How DSCR is calculated"),
            ("/dscr-lenders.html", "How to compare DSCR lenders"),
        ],
        "sources": [CENSUS_HV, IRS_527, CFPB],
    },
]
