# -*- coding: utf-8 -*-
"""/10-million-business-loan.html - new root page, daily batch 2026-11-12.

Search Console, Oct 13 - Nov 9 2026: "how to get a $10 million business loan" 33
impressions (positions 55-82), "10 million business loan" 29 (60-82), "loans from
$500k to $10m" 19 and "requirements for a 10 million business loan" 2, landing on the
$500K page and the term loans pillar. The site's loan-amount pages stop at $5 million,
the SBA 7(a) maximum, so nothing answered what a $10 million loan actually is.

Rules read 2026-11-12: 13 CFR 120.931 (504 loan limits: $5,000,000; $5,500,000 for
small manufacturers and energy projects), 13 CFR 120.910 (borrower contribution 10%,
15% for a business two years old or less or a special-purpose building, 20% for
both), 13 CFR 120.920 (third-party loan at least 50% of project cost in those cases,
otherwise at least equal to the 504 loan), 12 CFR 32.3 (national bank lending limit
15% of capital and surplus, plus 10% fully secured by readily marketable collateral),
7 CFR 5001.406(c) (B&I loans up to $25 million per borrower). Payments and DSCR
figures computed by script. Rates are scenarios, not quotes; the site's CRE rate
pages disagree (see the plan), so no rate range is published here. No named lenders.
"""
from cluster_table import table

SBA_7A = ("https://www.sba.gov/funding-programs/loans/7a-loans", "SBA 7(a) Loans",
          "Program overview and the $5 million maximum loan amount.")
CFR_931 = ("https://www.law.cornell.edu/cfr/text/13/120.931", "13 CFR 120.931: 504 lending limits",
           "The $5,000,000 limit per borrower and the $5,500,000 limit for small manufacturers and energy projects.")
CFR_910 = ("https://www.law.cornell.edu/cfr/text/13/120.910", "13 CFR 120.910: Borrower contribution",
           "The 10%, 15% and 20% minimum contributions to a 504 project.")
CFR_920 = ("https://www.law.cornell.edu/cfr/text/13/120.920", "13 CFR 120.920: Third Party Lender participation",
           "How large the bank's first-lien loan must be relative to the 504 loan.")
OCC_32 = ("https://www.law.cornell.edu/cfr/text/12/32.3", "12 CFR 32.3: Lending limits",
          "The national bank limit of 15% of capital and surplus to one borrower, plus 10% with readily marketable collateral.")
USDA = ("https://www.law.cornell.edu/cfr/text/7/5001.406", "7 CFR 5001.406: Loan limits",
        "USDA Business and Industry guaranteed loans of up to $25 million per borrower.")
OCC_ABL = ("https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/index-asset-based-lending.html",
           "OCC Comptroller's Handbook: Asset-Based Lending",
           "How banks lend against receivables and inventory through a borrowing base.")

_A = lambda href, text: f'<a href="{href}" rel="noopener nofollow" target="_blank">{text}</a>'

CLUSTER = {
    "pillar": "how-much-can-i-borrow-business-loan.html",
    "hub": "business-loan-amounts",
    "no_hub": True,
    "back_href": "/how-much-can-i-borrow-business-loan.html",
    "crumb": "Business Loan Amounts",
    "cta_inline": "Tell us the project and the collateral",
    "cta_button": "Talk to a Large-Loan Specialist",
}

ARTICLES = [{
    "slug": "10-million-business-loan",
    "root_file": "10-million-business-loan.html",
    "crumb": "$10 Million Business Loan",
    "title": "How to Get a $10 Million Business Loan | Axiant",
    "og_title": "How to Get a $10 Million Business Loan: What It Takes",
    "h1": "How to Get a $10 Million Business Loan: What It Takes",
    "headline": "How to Get a $10 Million Business Loan: What It Takes",
    "lede": "Above the SBA 7(a) limit, a $10 million loan is a project loan: real estate, "
            "a 504 structure, an asset-based line or a bank loan shared with other banks",
    "meta_desc": "A $10 million business loan is above the SBA 7(a) limit. See which structures "
                 "reach it, the SBA 504 and bank lending limits, and the cash flow it needs.",
    "article_desc": "What a $10 million business loan really is: commercial real estate, SBA 504 "
                    "projects, asset-based lending, bank participations and USDA B&I, with "
                    "the rules and the cash flow each needs.",
    "keywords": "10 million business loan, how to get a $10 million business loan, $10m business "
                "loan requirements, large business loan, sba 504 10 million project",
    "quick_answer": "As of November 2026, a $10 million business loan is almost always secured and "
                    "tied to a project: commercial real estate, an SBA 504 project, an asset-based "
                    "line against receivables and inventory, or a bank loan shared among banks. It "
                    "is above the SBA 7(a) maximum of <strong>$5 million</strong>, and a 504 "
                    "project caps the SBA part at <strong>$5 million</strong> ($5.5 million for "
                    "small manufacturers). Lenders typically want cash flow of about "
                    "<strong>1.25x</strong> the payment. Axiant Partners, a business-loan broker in "
                    "Boca Raton, places large loans. These are typical figures, not a quote.",
    "sections": [
        ("Who Lends $10 Million, and Against What",
         "<p>At this size the question is not which lender is easiest but which collateral and "
         "which program can carry the amount. Five structures reach $10 million; an SBA 7(a) "
         "loan on its own does not, because its maximum is $5 million.</p>"
         + table(["Structure", "Secured by", "Size rule", "Usually fits"], [
             ["Commercial real estate loan", "The building", "Lender&rsquo;s LTV and DSCR tests",
              "Buying or refinancing property"],
             ["SBA 504 project", "Bank first lien plus a CDC second",
              "504 part up to $5M, or $5.5M for manufacturers", "Owner-occupied buildings, heavy equipment"],
             ["Asset-based line", "Receivables and inventory", "A borrowing base, recalculated often",
              "Distributors, manufacturers"],
             ["Bank term loan or participation", "Cash flow and all business assets",
              "One bank&rsquo;s legal lending limit", "Acquisitions, recapitalizations"],
             ["USDA B&amp;I guaranteed loan", "Real estate, equipment, a USDA guarantee",
              "Up to $25M per borrower", "Businesses in eligible rural areas"],
         ])
         + "<p>Sources: " + _A("https://www.law.cornell.edu/cfr/text/13/120.931", "13 CFR 120.931")
         + " for the 504 limits, " + _A("https://www.law.cornell.edu/cfr/text/7/5001.406", "7 CFR 5001.406")
         + " for USDA B&amp;I. Most real deals combine two of these, for example a 504 loan for the "
         "building and an asset-based line for working capital. If the project is property, start "
         "with <a href=\"/commercial-real-estate-loans.html\">commercial real estate loans</a>; for a "
         "purchase of a company, see <a href=\"/business-acquisition-financing.html\">business "
         "acquisition financing</a>.</p>"),
        ("Why $10 Million Is Different From $5 Million",
         "<p>Three things change once a request passes $5 million.</p>"
         "<p><strong>The SBA 7(a) door closes.</strong> The "
         + _A("https://www.sba.gov/funding-programs/loans/7a-loans", "SBA&rsquo;s 7(a) program")
         + " tops out at $5 million, so a $10 million need is either split across structures or "
         "financed outside the SBA. Our <a href=\"/5-million-business-loan.html\">$5 million business "
         "loan</a> guide covers the 7(a) end of the market.</p>"
         "<p><strong>One bank may not be allowed to lend it all.</strong> Under "
         + _A("https://www.law.cornell.edu/cfr/text/12/32.3", "12 CFR 32.3")
         + ", a national bank&rsquo;s loans to one borrower generally can&rsquo;t exceed 15% of its "
         "capital and surplus, plus another 10% if the excess is fully secured by readily marketable "
         "collateral. A bank with $50 million of capital and surplus can lend one borrower about "
         "$7.5 million under the general limit. A $10 million loan from that bank means it sells "
         "part of the loan to other banks (a participation) or brings in a co-lender. State banks "
         "follow their state&rsquo;s limits, which are often similar.</p>"
         "<p><strong>Underwriting becomes covenant lending.</strong> Expect reviewed or audited "
         "financial statements, a debt service coverage test and often a leverage test that are "
         "checked every quarter or year, and reporting duties for as long as the loan is "
         "outstanding.</p>"),
        ("Worked Example: An $11 Million Building Through SBA 504",
         "<p><strong>Illustrative, not a quote.</strong> An established manufacturer buys and "
         "renovates its own building for $11,000,000. A standard 504 split puts about $9.9 million "
         "of debt on the project:</p>"
         + table(["Piece", "Share", "Amount", "Rule"], [
             ["Bank first-lien loan", "50%", "$5,500,000", "At least equal to the 504 loan (13 CFR 120.920)"],
             ["CDC 504 loan", "40%", "$4,400,000", "Under the $5M, or $5.5M manufacturer, limit"],
             ["Borrower contribution", "10%", "$1,100,000", "Minimum for an established business (120.910)"],
         ])
         + "<p>Two things move the borrower&rsquo;s share. A business that has operated two years or "
         "less, or a special-purpose building, needs at least 15%, and both together need 20% "
         "(" + _A("https://www.law.cornell.edu/cfr/text/13/120.910", "13 CFR 120.910") + "). At 15% "
         "on the same project the contribution is $1,650,000 and the 504 loan falls to $3,850,000. "
         "And because the 504 part is capped, a larger project puts more on the bank loan, which "
         "then runs into the lending limit above. Our "
         "<a href=\"/sba-loans/articles/what-is-an-sba-504-loan/\">SBA 504 guide</a> and "
         "<a href=\"/sba-loans/articles/sba-504-loan-fees/\">504 fees</a> page cover the rest.</p>"),
        ("What Cash Flow Supports $10 Million",
         "<p>Most lenders size a loan this large on debt service coverage: the cash flow available "
         "for debt payments divided by the payments. At a common 1.25x test, here is what a fully "
         "amortizing $10 million loan needs at two rate scenarios (computed; not quotes):</p>"
         + table(["Rate and amortization", "Monthly payment", "Annual payments", "Cash flow at 1.25x"], [
             ["7%, 10 years", "About $116,100", "About $1.39M", "About $1.74M a year"],
             ["7%, 25 years", "About $70,700", "About $848,000", "About $1.06M a year"],
             ["9%, 10 years", "About $126,700", "About $1.52M", "About $1.90M a year"],
             ["9%, 25 years", "About $83,900", "About $1.01M", "About $1.26M a year"],
         ])
         + "<p>The spread between rows is why structure matters more than rate. The same $10 million "
         "on a 25-year real estate schedule needs roughly $640,000 to $680,000 less cash flow a year "
         "than on a 10-year equipment or acquisition schedule. Lenders also look at global cash flow, "
         "meaning the owners&rsquo; other debts and income. Use the "
         "<a href=\"/dscr-loans/articles/how-dscr-is-calculated/\">DSCR formula</a> to test your own "
         "numbers.</p>"),
        ("What Lenders Typically Ask For at This Size",
         "<ul>"
         "<li><strong>Three years of financial statements</strong>, reviewed or audited by a CPA, plus "
         "interim statements and tax returns.</li>"
         "<li><strong>Projections</strong> that show the loan&rsquo;s purpose paying for itself, with "
         "the assumptions written down.</li>"
         "<li><strong>A debt schedule</strong> for the business and its owners.</li>"
         "<li><strong>Third-party reports:</strong> an appraisal, and for real estate usually a Phase I "
         "environmental assessment, ordered early because they set the timeline.</li>"
         "<li><strong>Personal guarantees</strong> from the larger owners on most bank and SBA "
         "structures.</li>"
         "<li><strong>A clear use of funds</strong>, priced out: purchase contract, construction budget "
         "or acquisition model.</li>"
         "</ul>"
         "<p>For an asset-based line, add receivable agings and inventory reports, since the "
         + _A(OCC_ABL[0], "borrowing base")
         + " is recalculated from them, commonly monthly or more often.</p>"),
        ("How to Get a $10 Million Business Loan, Step by Step",
         "<ol>"
         "<li><strong>Name the project and the collateral.</strong> A building, a company, equipment "
         "or receivables each point to a different structure in the table above.</li>"
         "<li><strong>Run the coverage test yourself</strong> at a conservative rate before you talk "
         "to a lender.</li>"
         "<li><strong>Get the statements reviewed</strong> if they are only compiled. It is the most "
         "common gap at this size.</li>"
         "<li><strong>Decide on the equity</strong>: 10% to 20% on a 504 project, often more on a "
         "conventional or acquisition loan.</li>"
         "<li><strong>Approach lenders that hold loans this size</strong>, or a broker who knows which "
         "banks can lend $10 million without a participation.</li>"
         "<li><strong>Order the third-party reports</strong> as soon as a term sheet is signed.</li>"
         "</ol>"
         "<p>When you have the project and the numbers, <a href=\"/match.html\">get matched with lenders "
         "that do large loans</a>.</p>"),
    ],
    "faqs": [
        ("Can you get a $10 million SBA loan?",
         "Not as a single 7(a) loan, which tops out at $5 million. An SBA 504 project can reach $10 "
         "million or more in total, because a bank lends at least as much as the 504 loan, but the 504 "
         "part itself is capped at $5 million, or $5.5 million for small manufacturers and energy "
         "projects."),
        ("What do you need to qualify for a $10 million business loan?",
         "Typically several years of reviewed or audited financials, cash flow of about 1.25 times the "
         "payments, real collateral such as property or receivables, equity in the project and personal "
         "guarantees from the larger owners. These are typical requirements, not a lender's rules."),
        ("What is the monthly payment on a $10 million business loan?",
         "It depends mostly on the term. At 7% it is about $116,100 a month over 10 years or about "
         "$70,700 over 25 years; at 9% about $126,700 or $83,900. These are computed examples, not "
         "quotes."),
        ("Can a startup get a $10 million business loan?",
         "Rarely, and only with substantial equity and collateral. A business two years old or less "
         "needs at least a 15% contribution on an SBA 504 project, and most conventional lenders want "
         "an operating history before lending this much."),
        ("Why would a bank split a $10 million loan with other banks?",
         "Because of lending limits. A national bank generally can't lend one borrower more than 15% "
         "of its capital and surplus, plus 10% with readily marketable collateral, so a smaller bank "
         "sells part of a large loan to other banks as a participation."),
        ("Are there government loans above $5 million?",
         "Yes. USDA Business and Industry guaranteed loans go up to $25 million per borrower for "
         "eligible rural businesses, and an SBA 504 project can exceed $5 million in total because the "
         "bank's first-lien loan sits alongside the 504 loan."),
    ],
    "related": [
        ("/5-million-business-loan.html", "$5 million business loan"),
        ("/2-million-business-loan.html", "$2 million business loan"),
        ("/how-much-can-i-borrow-business-loan.html", "How much can I borrow?"),
        ("/sba-loans/articles/what-is-an-sba-504-loan/", "What is an SBA 504 loan?"),
        ("/commercial-real-estate-loans.html", "Commercial real estate loans"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SBA_7A, CFR_931, CFR_910, CFR_920, OCC_32, USDA, OCC_ABL],
}]
