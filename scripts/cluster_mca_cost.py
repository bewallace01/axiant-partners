# -*- coding: utf-8 -*-
"""MCA cost page (rewrite) and MCA alternatives (new), daily batch 2026-11-13.

Search Console, Oct 14 - Nov 11 2026: "how to calculate merchant cash advance cost"
47 impressions at 35, "how much does a $100,000 merchant cash advance cost" 43 at 22,
"how much does a merchant cash advance cost" 25 at 55, "mca calculator" 40 at 83 and
"mca factor rate" 10 at 28 all land on how-much-can-you-qualify-for-merchant-cash-advance,
which answers a different question (the size of the advance). The existing rates page
(typical-merchant-cash-advance-rates-2026, published 2026-06-05) is the page for cost, so it
is rewritten here to own those searches (same URL, original publish date kept) and the
qualify page links to it.

Fact fix: the old rates table and FAQ understated the APR (1.30 over 6 months shown as ~88%
and ~90%; over 12 months ~48% and ~45%). Every APR on this page is computed by script with
one stated method: equal payments every business day (21 a month, 252 a year), annual rate
= daily IRR x 252, nominal, on the amount actually received.

"mca alternative" 30 impressions at 29, landing on revenue-based-financing-vs-merchant-cash-
advance, which compares one product. No page listed the alternatives side by side, so
merchant-cash-advance-alternatives is new. The rates page's own "cheaper alternatives" list
now points to it instead of competing with it.

Ranges reuse what the site publishes: factor 1.15-1.50 and holdback 10-20% (this page),
line of credit 8-13% APR at banks and 14-30%+ online (LOC rates page), online term loans
14-30% (working capital rates page), factoring 1-5% per invoice with 80-95% advances
(factoring rates page), equipment 7-22% APR (equipment rates page), RBF 1.10-1.50x
(RBF rates page), SBA 7(a) base + 6.0% cap on $50,001-$250,000 ($100K page). SBA cannot
refinance an active MCA (SOP 50 10 8.1 Appendix 14, as on can-you-refinance-mca-with-sba-
loan). Florida's Commercial Financing Disclosure Law (Fla. Stat. 559.9613) read from the
statute: total funded, disbursed, total repaid, total dollar cost, payment terms and
prepayment costs; no APR. No named lenders.
"""
from cluster_table import table

FTC = ("https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic",
       "FTC: Protecting Small Businesses Seeking Financing",
       "The FTC's guidance to lenders, brokers and merchant cash advance providers on misrepresented costs.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research on small business credit, including how costs are disclosed to borrowers.")
FL_DISC = ("http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0559/Sections/0559.9613.html",
           "Florida Statutes 559.9613: Commercial financing disclosures",
           "What a provider must disclose in Florida: amount funded, amount disbursed, total repaid, total dollar cost and payment terms.")
SBA_7A = ("https://www.sba.gov/funding-programs/loans/7a-loans", "SBA 7(a) Loans",
          "Uses of 7(a) proceeds and the program's maximum rates.")

CLUSTER = {
    "pillar": "merchant-cash-advance.html",
    "hub": "merchant-cash-advance/articles",
    "hub_by_hand": True,
    "crumb": "Merchant Cash Advance",
    "cta_inline": "See whether something cheaper can fund the same need",
    "cta_button": "Compare My Options",
}

COST = {
    "slug": "typical-merchant-cash-advance-rates-2026",
    "date_published": "2026-06-05",
    "crumb": "MCA Cost and Factor Rates",
    "title": "Merchant Cash Advance Cost: Factor Rate to APR (2026)",
    "og_title": "How Much a Merchant Cash Advance Costs: Factor Rate to APR",
    "h1": "How Much a Merchant Cash Advance Costs: Factor Rate to APR (2026)",
    "headline": "How Much a Merchant Cash Advance Costs: Factor Rate to APR (2026)",
    "lede": "The four-step calculation, what a $100,000 advance costs at each factor rate, and "
            "why the same factor is twice as expensive repaid in six months",
    "meta_desc": "How to calculate merchant cash advance cost: a $100,000 MCA at a 1.25-1.45 "
                 "factor costs $25,000-$45,000, or about 46-158% APR. Tables and method.",
    "article_desc": "How to calculate the cost of a merchant cash advance: payback, dollar cost, "
                    "term from the holdback, and APR, with a $100,000 cost table computed by script.",
    "keywords": "merchant cash advance cost, how to calculate merchant cash advance cost, mca factor "
                "rate, mca apr, $100,000 merchant cash advance cost, merchant cash advance rates 2026",
    "quick_answer": "As of November 2026, a merchant cash advance costs the advance times the factor "
                    "rate, minus the advance. A $100,000 MCA at a typical 1.25-1.45 factor costs "
                    "<strong>$25,000-$45,000</strong>. Repaid by daily debits over 6-12 months, that "
                    "is roughly <strong>46-158% APR</strong>, because the cost is fixed and the term "
                    "is short. Factors commonly run 1.15-1.50. Axiant Partners, a business-loan "
                    "broker in Boca Raton, compares MCAs with cheaper options. These are typical "
                    "ranges, not a quote.",
    "sections": [
        ("How to Calculate the Cost of a Merchant Cash Advance",
         "<p>An MCA is priced with a factor rate instead of an interest rate, so the cost is a "
         "fixed dollar amount agreed on day one. Four numbers turn it into something you can "
         "compare with a loan:</p>"
         "<ol>"
         "<li><strong>Payback.</strong> Advance &times; factor rate. $100,000 &times; 1.35 = "
         "$135,000.</li>"
         "<li><strong>Dollar cost.</strong> Payback minus the cash you actually receive. If a fee "
         "is deducted from the funding, subtract the net amount, not the headline advance.</li>"
         "<li><strong>Term.</strong> Payback divided by the daily (or weekly) debit. $135,000 at "
         "$750 a business day is 180 business days, about 8.6 months.</li>"
         "<li><strong>APR.</strong> The annual rate at which the cash received equals the stream of "
         "debits. A spreadsheet&rsquo;s RATE function does it: RATE(180, -750, 100000) &times; 252 "
         "= about 88%.</li>"
         "</ol>"
         "<p>Step 4 is the one providers skip. It matters because a cost of 35% looks like a 35% "
         "rate, but you never have the full $100,000 for the whole term: the debits start the next "
         "business day, so on average you hold about half of it.</p>"),
        ("What a $100,000 Merchant Cash Advance Costs",
         "<p>Computed for equal debits every business day (21 a month). Factor rates are the "
         "typical range; your offer depends on your file.</p>"
         + table(["Factor", "Payback", "Dollar cost", "Daily debit, 6 mo / 12 mo", "APR at 6 / 9 / 12 mo"], [
             ["1.15", "$115,000", "$15,000", "$913 / $456", "57% / 38% / 28%"],
             ["1.25", "$125,000", "$25,000", "$992 / $496", "92% / 62% / 46%"],
             ["1.35", "$135,000", "$35,000", "$1,071 / $536", "126% / 84% / 63%"],
             ["1.45", "$145,000", "$45,000", "$1,151 / $575", "158% / 106% / 79%"],
         ])
         + "<p>In monthly terms, the 1.35 advance over 9 months takes about $15,000 a month out "
         "of the account. Check that against your slowest month, not your average one.</p>"),
        ("Factor Rate to APR on a $50,000 Advance",
         "<p>The same method on a smaller advance. The dollar cost scales with the advance; the "
         "APR depends only on the factor and the term.</p>"
         + table(["Factor", "Payback on $50,000", "Dollar cost", "APR at 6 / 9 / 12 mo"], [
             ["1.15", "$57,500", "$7,500", "57% / 38% / 28%"],
             ["1.25", "$62,500", "$12,500", "92% / 62% / 46%"],
             ["1.30", "$65,000", "$15,000", "109% / 73% / 55%"],
             ["1.40", "$70,000", "$20,000", "142% / 95% / 71%"],
             ["1.50", "$75,000", "$25,000", "174% / 116% / 87%"],
         ])
         + "<p><strong>Correction:</strong> an earlier version of this page showed lower APRs (for "
         "example about 88% for 1.30 over 6 months), from a rougher approximation. The figures "
         "above are recomputed with the method stated on this page.</p>"),
        ("How the Holdback Sets the Term, and the Cost",
         "<p>You rarely choose the term. On a true split, the provider takes a fixed share of card "
         "sales, commonly 10-20%, so busy weeks repay faster. On a fixed ACH debit, the term is set "
         "when you sign. Either way, a faster payback means a higher APR for the same dollar "
         "cost.</p>"
         "<p>Example: $5,000 of daily card sales at a 15% holdback is $750 a day, which repays a "
         "$135,000 payback in about 180 business days. If sales rise to $6,000, the debit is $900 "
         "and the same advance is repaid in 150 days, at a higher APR. If sales fall, a "
         "reconciliation clause should lower the debit; ask whether the agreement has one and how "
         "you request it.</p>"),
        ("Fees and Clauses That Change the Real Cost",
         "<ul>"
         "<li><strong>Fees deducted from funding.</strong> An origination or underwriting fee taken "
         "out of the advance raises the APR. A $100,000 advance at 1.35 over 9 months is about 84%; "
         "with $3,000 deducted, you receive $97,000 and it is about 93%.</li>"
         "<li><strong>Early payoff.</strong> Many agreements owe the full payback even if you repay "
         "early. A written prepayment discount is the exception; get it in the contract.</li>"
         "<li><strong>Stacking.</strong> A second advance on top of the first adds a second daily "
         "debit and is often priced higher. See <a href=\"/merchant-cash-advance/articles/get-out-of-stacked-mcas-without-bankruptcy/\">"
         "stacked MCAs</a>.</li>"
         "<li><strong>Renewals.</strong> Rolling the unpaid balance into a new advance charges the "
         "factor again on money you already owed.</li>"
         "</ul>"
         "<p>Florida&rsquo;s commercial financing disclosure law (<a href=\"http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&amp;URL=0500-0599/0559/Sections/0559.9613.html\" "
         "rel=\"noopener nofollow\" target=\"_blank\">Fla. Stat. 559.9613</a>) requires the provider "
         "to show the amount funded, the amount actually disbursed, the total repaid, the total "
         "dollar cost, the payment terms and any prepayment cost. It does not require an APR, which "
         "is why the calculation above is yours to do.</p>"),
        ("What Drives Your Factor Rate",
         "<p>MCA pricing has little to do with the prime rate. Providers price on their own models:</p>"
         "<ul>"
         "<li><strong>Deposit and card volume</strong>: higher and steadier earns a lower factor.</li>"
         "<li><strong>Negative days and overdrafts</strong> push it up.</li>"
         "<li><strong>Time in business</strong>: a longer track record lowers it.</li>"
         "<li><strong>Industry</strong>: some carry a premium or are excluded.</li>"
         "<li><strong>Open advances</strong>: existing positions raise the factor or cause a decline.</li>"
         "</ul>"
         "<p>How large an advance those same numbers support is a separate question, covered in "
         "<a href=\"/merchant-cash-advance/articles/how-much-can-you-qualify-for-merchant-cash-advance/\">how "
         "much you can qualify for</a>.</p>"),
        ("Before You Sign",
         "<p>Run the four steps on the offer in front of you, then price the same amount as a line "
         "of credit or term loan. A line at a typical 8-13% APR at a bank, or 14-30%+ online, costs "
         "a fraction of an MCA for the same months. The options, side by side, are in "
         "<a href=\"/merchant-cash-advance/articles/merchant-cash-advance-alternatives/\">merchant cash "
         "advance alternatives</a>; the cross-product view is the "
         "<a href=\"/business-loan-rates-2026/\">2026 business loan rates</a> hub. When you have the "
         "numbers, <a href=\"/match.html\">get matched with lenders</a>.</p>"),
    ],
    "faqs": [
        ("How do you calculate the cost of a merchant cash advance?",
         "Multiply the advance by the factor rate to get the payback, then subtract the cash you "
         "actually received. Divide the payback by the daily debit to get the term, and annualize "
         "with a rate function to get the APR. $100,000 at 1.35 repaid at $750 a business day is "
         "$35,000 over about 180 days, or about 88% APR."),
        ("How much does a $100,000 merchant cash advance cost?",
         "At a typical factor of 1.25-1.45, $25,000-$45,000 on top of the $100,000. Repaid over 6-12 "
         "months by daily debits, that is roughly 46-158% APR. These are typical ranges, not a quote."),
        ("What are typical merchant cash advance factor rates in 2026?",
         "Commonly 1.15 to 1.50. Stronger, steadier deposits and fewer open advances earn the lower "
         "end; weaker files and stacking push toward the top."),
        ("How do you convert a factor rate to an APR?",
         "Find the payback and the number of payments, then solve for the rate at which the cash "
         "received equals the payments. With 21 business-day debits a month, a 1.30 factor is about "
         "109% APR over 6 months and about 55% over 12."),
        ("Why does a shorter MCA cost more as an APR?",
         "The dollar cost is fixed when you sign. Repaying it faster means the same cost is spread "
         "over less time and a smaller average balance, so the annual rate rises."),
        ("Do fees change the cost of an MCA?",
         "Yes. A fee deducted from the funding means you receive less but repay the same. On $100,000 "
         "at 1.35 over 9 months, a $3,000 deduction moves the APR from about 84% to about 93%."),
        ("Does a merchant cash advance have to disclose an APR in Florida?",
         "No. Florida's commercial financing disclosure law requires the total funded, amount "
         "disbursed, total repaid, total dollar cost and payment terms, but not an APR. You can "
         "compute it from those figures."),
    ],
    "related": [
        ("/merchant-cash-advance/articles/merchant-cash-advance-alternatives/", "Merchant cash advance alternatives"),
        ("/merchant-cash-advance/articles/how-much-can-you-qualify-for-merchant-cash-advance/", "How much MCA you can qualify for"),
        ("/merchant-cash-advance/articles/red-flags-mca-agreements/", "Red flags in MCA agreements"),
        ("/working-capital-loans/articles/mca-vs-working-capital-loan/", "MCA vs working capital loan"),
        ("/business-loan-rates-2026/", "2026 business loan rates"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [FL_DISC, FTC, CFPB],
}

ALT = {
    "slug": "merchant-cash-advance-alternatives",
    "crumb": "MCA Alternatives",
    "title": "Merchant Cash Advance Alternatives: 7 Options Compared",
    "og_title": "Merchant Cash Advance Alternatives: 7 Cheaper Options Compared",
    "h1": "Merchant Cash Advance Alternatives: 7 Options Compared",
    "headline": "Merchant Cash Advance Alternatives: 7 Options Compared",
    "lede": "What to use instead of an MCA, what each typically costs, how fast it funds, and which "
            "one fits the problem you are actually trying to solve",
    "meta_desc": "MCA alternatives compared: lines of credit at about 8-13% APR at banks, term "
                 "loans, factoring, equipment and SBA loans, with costs, speed and who qualifies.",
    "article_desc": "Seven alternatives to a merchant cash advance compared on typical cost, speed "
                    "and fit, with a $50,000 cost comparison computed by script.",
    "keywords": "mca alternative, merchant cash advance alternatives, alternatives to merchant cash "
                "advance, instead of an mca, cheaper than a merchant cash advance",
    "quick_answer": "As of November 2026, the most common MCA alternatives are a business line of "
                    "credit (typically <strong>8-13% APR</strong> at banks, 14-30%+ online), an online "
                    "term loan, invoice factoring (about <strong>1-5% per invoice</strong>), equipment "
                    "financing, revenue-based financing and SBA 7(a). Each usually costs far less than "
                    "an MCA's 1.15-1.50 factor, but takes longer or asks more. Axiant Partners, a "
                    "business-loan broker in Boca Raton, compares them for you. Typical ranges, not "
                    "a quote.",
    "sections": [
        ("MCA Alternatives Compared",
         "<p>The ranges below are the ones published on each product&rsquo;s own page, typical "
         "across lenders and not quotes.</p>"
         + table(["Alternative", "Typical cost", "Speed", "Best when"], [
             ["Business line of credit", "8-13% APR at banks; 14-30%+ online", "Days online; weeks at a bank",
              "The need repeats: seasons, payroll gaps"],
             ["Online term loan", "About 14-30%", "Days", "A one-time need with a clear payback"],
             ["Invoice factoring", "About 1-5% per invoice; 80-95% advanced", "Days after setup",
              "Customers pay you on 30-90 day terms"],
             ["Equipment financing", "About 7-22% APR by credit tier", "Days", "The money is for a machine or vehicle"],
             ["Revenue-based financing", "Factor about 1.10-1.50, longer terms", "Days to weeks",
              "Recurring or online revenue, $50K+ a month"],
             ["SBA 7(a)", "Capped, e.g. base + 6.0% on $50,001-$250,000", "Weeks", "A planned, larger need"],
             ["Asset-secured loan", "Priced on the collateral", "Days to weeks",
              "You own a truck, equipment or real estate"],
         ])),
        ("Match the Alternative to the Problem",
         "<p>An MCA gets used for every kind of shortfall because it is fast. The cheaper options "
         "are narrower, so start from what is actually short:</p>"
         "<ul>"
         "<li><strong>Customers pay late.</strong> That is a receivables problem: "
         "<a href=\"/working-capital-loans/articles/invoice-factoring-vs-merchant-cash-advance/\">factoring</a> "
         "advances against the invoices instead of your future sales.</li>"
         "<li><strong>Sales are seasonal.</strong> A <a href=\"/business-line-of-credit.html\">line of "
         "credit</a> drawn in the slow months and repaid in the busy ones.</li>"
         "<li><strong>A machine or vehicle.</strong> <a href=\"/equipment-financing.html\">Equipment "
         "financing</a>, secured by the asset, over its working life.</li>"
         "<li><strong>A growth project with a payback.</strong> A term loan, or SBA 7(a) if it can "
         "wait a few weeks.</li>"
         "<li><strong>Equity you already own.</strong> A loan against a "
         "<a href=\"/commercial-truck-title-loan.html\">truck</a>, equipment or "
         "<a href=\"/real-estate-secured-business-loan.html\">real estate</a>.</li>"
         "</ul>"),
        ("Worked Example: $50,000, Four Ways",
         "<p><strong>Illustrative assumptions, not quotes.</strong> The same $50,000, priced at "
         "points inside the typical ranges above, with payments computed by script.</p>"
         + table(["Option", "Assumed terms", "Payment", "Total cost"], [
             ["Merchant cash advance", "1.30 factor, 6 months of daily debits", "About $516 a business day", "$15,000 (about 109% APR)"],
             ["Online term loan", "22% APR, 12 months", "About $4,680 a month", "About $6,157"],
             ["Equipment loan", "11% APR, 36 months", "About $1,637 a month", "About $8,930"],
             ["Bank line of credit", "12% APR, repaid evenly over 6 months", "About $8,627 a month", "About $1,765"],
         ])
         + "<p>The equipment loan costs more in dollars than the term loan only because it runs three "
         "times as long; per year it is the cheaper money. The MCA costs the most and takes the "
         "biggest monthly bite: about $10,800 a month at 21 business days.</p>"),
        ("Why Businesses End Up With an MCA Anyway",
         "<ul>"
         "<li><strong>Speed.</strong> Funding in a day or two. The fix is to apply for a line while "
         "you don&rsquo;t need it, so it is there when you do.</li>"
         "<li><strong>Credit.</strong> Lower scores get fewer bank offers. Secured options, "
         "factoring and equipment financing weigh the asset or the invoice more than the score.</li>"
         "<li><strong>Documents.</strong> An MCA asks for bank statements; a term loan may want tax "
         "returns. Having them ready removes most of the gap.</li>"
         "<li><strong>An existing MCA.</strong> Open positions put off banks. See "
         "<a href=\"/merchant-cash-advance/articles/refinance-mca-to-term-loan-30-day-playbook/\">refinancing "
         "an MCA into a term loan</a>.</li>"
         "</ul>"),
        ("If You Already Have an MCA",
         "<p>An alternative can also replace an advance you already have, but check the rules "
         "first. SBA 7(a) cannot refinance an active MCA under SOP 50 10 8.1; the narrow exception "
         "is explained in <a href=\"/sba-loans/articles/can-you-refinance-mca-with-sba-loan/\">can you "
         "refinance an MCA with an SBA loan</a>. A non-SBA term loan, a consolidation loan or a loan "
         "against an asset you own are the usual routes. If the debits are already more than the "
         "account can carry, read <a href=\"/business-debt-relief/articles/cant-make-mca-payments-options/\">options "
         "when you can&rsquo;t make MCA payments</a> before taking anything new.</p>"),
        ("How to Compare an MCA Offer With an Alternative",
         "<ol>"
         "<li><strong>Put both in dollars:</strong> total repaid minus cash received.</li>"
         "<li><strong>Put both in APR</strong>, using the method in "
         "<a href=\"/merchant-cash-advance/articles/typical-merchant-cash-advance-rates-2026/\">how much a "
         "merchant cash advance costs</a>.</li>"
         "<li><strong>Compare the monthly bite</strong> against your slowest month.</li>"
         "<li><strong>Read prepayment terms</strong>: an MCA often owes the full payback even if "
         "repaid early; most term loans don&rsquo;t.</li>"
         "<li><strong>Apply once</strong> and let a broker return several offers. "
         "<a href=\"/match.html\">Get matched</a>.</li>"
         "</ol>"),
    ],
    "faqs": [
        ("What is the best alternative to a merchant cash advance?",
         "It depends on the problem. A business line of credit fits repeated, seasonal gaps; invoice "
         "factoring fits slow-paying customers; equipment financing fits a machine or vehicle; a "
         "term loan fits a one-time need. Each typically costs far less than an MCA."),
        ("Is a business line of credit cheaper than an MCA?",
         "Usually by a wide margin. Lines commonly run about 8-13% APR at banks and 14-30%+ online, "
         "while an MCA at a 1.30 factor over 6 months is about 109% APR. These are typical ranges, "
         "not a quote."),
        ("Can I get an MCA alternative with bad credit?",
         "Often. Invoice factoring leans on your customers' credit, and equipment financing and "
         "asset-secured loans lean on the collateral, so a lower score matters less than it does at "
         "a bank."),
        ("How fast can an MCA alternative fund?",
         "Online lines of credit and term loans often fund in days, factoring within days of setup, "
         "and equipment financing in days to weeks. SBA 7(a) takes weeks."),
        ("Can an SBA loan pay off a merchant cash advance?",
         "Not an active one, under SOP 50 10 8.1, apart from a narrow conversion path. A non-SBA term "
         "loan, consolidation loan or asset-secured loan is the usual route."),
        ("Is revenue-based financing an MCA alternative?",
         "Yes, for businesses with recurring or online revenue. It is also priced with a factor, "
         "about 1.10-1.50, but usually over longer terms, which lowers the annual cost."),
    ],
    "related": [
        ("/merchant-cash-advance/articles/typical-merchant-cash-advance-rates-2026/", "How much a merchant cash advance costs"),
        ("/revenue-based-financing/articles/revenue-based-financing-vs-merchant-cash-advance/", "Revenue-based financing vs MCA"),
        ("/working-capital-loans/articles/mca-vs-working-capital-loan/", "MCA vs working capital loan"),
        ("/working-capital-loans/articles/invoice-factoring-vs-merchant-cash-advance/", "Invoice factoring vs MCA"),
        ("/business-line-of-credit.html", "Business line of credit"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SBA_7A, FTC, CFPB, FL_DISC],
}

ARTICLES = [COST, ALT]
