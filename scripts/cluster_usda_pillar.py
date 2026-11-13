# -*- coding: utf-8 -*-
"""USDA Business & Industry loans - SBA plan Cluster 3 root money page /usda-business-loans.html.

A separate module from cluster_usda.py only because article_v2 takes the crumb trail from the
cluster: this page sits under Home > SBA Loans (like /hotel-financing.html and
/sba-100-percent-financing.html), while its spokes sit under it. Sources, fee rates and helpers
are shared with cluster_usda.py; see its docstring for where each rule was read.

    python scripts/build-cluster.py usda_pillar --apply
"""
from cluster_table import table
from cluster_usda import (RURAL, PROJ, INEL, BORR, APPR, FEAS, TERM, LIMIT, FEE, NOTICE, MAP,
                          PROGRAM, USES, _a, pmt, g_fee, guar_pct, d, FEE_STD, RET_STD)

CLUSTER = {
    "pillar": "sba-loans.html",
    "hub": "usda-business-loans",
    "no_hub": True,
    "back_href": "/sba-loans.html",
    "crumb": "SBA Loans",
    "cta_inline": "Check whether your project fits USDA",
    "cta_button": "Talk to a Specialist",
}

_ELIG = '<a href="/usda-business-loans/articles/usda-eligible-areas/">USDA eligible areas</a>'
_VS = '<a href="/usda-business-loans/articles/usda-b-and-i-vs-sba-7a/">USDA B&amp;I vs SBA 7(a)</a>'
_HOTEL = '<a href="/usda-business-loans/articles/usda-hotel-loans/">USDA hotel loans</a>'
_FEES = '<a href="/usda-business-loans/articles/usda-b-and-i-loan-rates-fees/">USDA B&amp;I rates, fees and terms</a>'

# worked example: an existing food processor expands in a town of about 9,000
P_BLDG, P_EQUIP, P_WC = 3_800_000, 1_900_000, 500_000
P_TOTAL = P_BLDG + P_EQUIP + P_WC
P_EQ = P_TOTAL * 0.10
P_LOAN = P_TOTAL - P_EQ
P_RATE, P_YRS = 8.0, 20
P_PAY = pmt(P_LOAN, P_RATE, P_YRS)

ARTICLES = [{
    "slug": "usda-business-loans",
    "root_file": "usda-business-loans.html",
    "crumb": "USDA Business Loans",
    "title": "USDA Business Loans: B&I Guaranteed Loans | Axiant",
    "og_title": "USDA Business Loans: How B&I Guaranteed Loans Work for Rural Businesses",
    "h1": "USDA Business Loans: How B&amp;I Guaranteed Loans Work for Rural Businesses",
    "headline": "USDA Business Loans: How B&I Guaranteed Loans Work for Rural Businesses",
    "lede": "Up to $25 million, terms to 40 years, for buildings, equipment, acquisitions, hotels and "
            "working capital outside the big cities. What qualifies and what lenders ask for",
    "meta_desc": "USDA Business & Industry loans: up to $25M for rural businesses, the 50,000 population "
                 "rule, eligible uses including hotels, equity rules, fees and a worked example.",
    "article_desc": "How USDA Business & Industry guaranteed loans work: rural eligibility, loan limits, "
                    "uses, equity, fees and the application path.",
    "keywords": "usda business loans, usda b&i loan, usda business and industry loan, rural business "
                "loan, usda loan for business in small town, usda b&i guaranteed loan",
    "quick_answer": "A USDA Business &amp; Industry (B&amp;I) loan is a bank loan with a USDA guarantee "
                    "for businesses in rural areas, generally outside towns of more than "
                    "<strong>50,000</strong> people. It can pay for real estate, buildings, equipment, "
                    "inventory, acquisitions and working capital, up to <strong>$25 million</strong> per "
                    "borrower. Lenders commonly lend up to about <strong>80%</strong> of collateral value, "
                    "and their appetite for size varies. Axiant Partners, a broker in Boca Raton, matches "
                    "rural projects with B&amp;I lenders. These are program rules and typical ranges, not a quote.",
    "sections": [
        ("How a B&amp;I Loan Works".replace("&amp;", "&"),
         "<p>USDA doesn't lend the money. A bank, credit union or other approved lender makes the loan, "
         "and USDA Rural Development guarantees part of it against loss. Under the FY2026 annual notice "
         f"the guarantee is <strong>85%</strong> on loans under $5 million and <strong>80%</strong> from "
         f"$5 million to $25 million. The cap is {_a(LIMIT, '$25 million per borrower')}, counting any "
         "B&amp;I balance you already have.</p>"
         "<p>The guarantee is what lets a lender go bigger and longer than it would on its own. Terms can "
         f"run to the useful life of what you're financing, up to {_a(TERM, '40 years')}, and the loan must "
         "fully amortize with no balloon. The rate is negotiated with the lender, with no USDA rate sheet. "
         f"For the numbers, see {_FEES}.</p>"),
        ("Where It Works: The Rural Test",
         f"<p>The project has to be in a {_a(RURAL, 'rural area')}: not in a city or town of more than "
         "50,000 people and not in the urbanized area attached to one, by the latest census. That rules "
         "out most suburbs but leaves in thousands of county seats, highway towns and resort areas, "
         "including some fairly large towns that stand alone.</p>"
         f"<p>Check the exact address on the {_a(MAP, 'USDA eligibility map')} before anything else. "
         f"{_ELIG} walks through the map and the narrow exceptions.</p>"),
        ("What It Can Pay For",
         table(["Eligible", "Not eligible"], [
             ["Buy, build or expand property", "Golf courses, racetracks and for-profit zoos"],
             ["Machinery and equipment", "Lines of credit"],
             ["Working capital (term loan)", "Apartments, timeshares and other residential housing"],
             ["Whole business, saving jobs", "Commercial rental where you don't control tenants or services"],
             ["Hotels, motels, B&amp;Bs, camps", "Speculative real estate investment"],
             ["Nursing, assisted living", "Independent living facilities"],
             ["Refinancing, within limits", "Loan finder or broker fees"],
         ])
         + f"<p>Sources: {_a(PROJ, '7 CFR 5001.105')}, {_a(INEL, '5001.115')}, {_a(USES, '5001.122')}. "
         "A buyout between existing owners also qualifies when the remaining owners have held their stake "
         "and worked in the business for at least 24 months and the seller keeps no interest. Hotels "
         f"have their own catches, covered in {_HOTEL}. For a business acquisition outside a rural area, "
         'see <a href="/business-acquisition-financing.html">business acquisition financing</a>.</p>'),
        ("Equity, Collateral and Who Can Borrow",
         "<p>The rule sets minimum equity at loan closing. A borrower meets one test in its row:</p>"
         + table(["Borrower", "Balance sheet equity", "Or cash into the project"], [
             ["Existing business", "10% (or 9:1 debt to equity)", "10% of eligible project cost"],
             ["New business, sales contracts", "10%", "10%"],
             ["New business, pre-completion", "25% (or 3:1)", "25%"],
             ["Any other new business", "20% (or 4:1)", "25%"],
         ])
         + "<p>USDA can raise these for riskier loans. Beyond the rule, these are common lender practice:</p>"
         "<ul>"
         "<li><strong>Collateral.</strong> Lenders discount appraised values and commonly lend up to about "
         "80% of collateral value; personal guarantees are standard. Going-concern value comes out of the "
         f"appraisal before discounting ({_a(APPR, '5001.203')}).</li>"
         "<li><strong>Cash flow.</strong> Lenders want history that covers the new payment, often at 1.25 "
         "times or better.</li>"
         f"<li><strong>Feasibility study.</strong> Required for a new business borrowing over $1 million "
         f"({_a(FEAS, '5001.306')}), and possible on other loans.</li>"
         f"<li><strong>Who can borrow.</strong> Companies, cooperatives, tribes, public bodies and "
         f"individuals. An individual must be a U.S. citizen or a green-card holder ({_a(BORR, '5001.126')}), "
         "and the collateral must be fixed assets in the U.S.</li>"
         "</ul>"),
        ("Worked Example: A Rural Plant Expansion",
         "<p><strong>Illustrative, not a quote or an offer.</strong> A food processor that has run for "
         f"years in a town of about 9,000 adds a building ({d(P_BLDG)}), equipment ({d(P_EQUIP)}) and "
         f"permanent working capital ({d(P_WC)}). It meets the existing-business test by putting in 10% "
         "of project cost. Fees use the FY2026 B&amp;I rates.</p>"
         + table(["Item", "Amount"], [
             ["Total project cost", d(P_TOTAL)],
             ["Owner's cash (10%)", d(P_EQ)],
             ["B&amp;I loan", d(P_LOAN)],
             ["USDA guarantee", f"{guar_pct(P_LOAN)}%"],
             [f"Guarantee fee ({FEE_STD:.1f}%)", d(g_fee(P_LOAN))],
             [f"Retention fee, year 1 ({RET_STD:.2f}%)", d(P_LOAN * guar_pct(P_LOAN) / 100 * RET_STD / 100)],
             ["Assumed rate and blended term", f"{P_RATE:.2f}%, {P_YRS} years"],
             ["Monthly principal and interest", d(P_PAY)],
         ])
         + f"<p>At {d(P_LOAN)}, this is already past the SBA 7(a) limit of $5 million, which is the most "
         "common reason a rural company ends up on B&amp;I. A real lender would likely set a longer term on "
         "the building and shorter ones on the equipment and working capital, so the payment above is a "
         f"blend. {_VS} shows when SBA is the better fit.</p>"),
        ("How to Apply",
         "<ol>"
         "<li><strong>Confirm the address is rural</strong> on USDA's map.</li>"
         "<li><strong>Find a lender that does B&amp;I.</strong> Fewer banks use it than SBA, and appetite "
         "for size, industry and hotels varies.</li>"
         "<li><strong>Build the file:</strong> three years of financials, interim statements, a debt "
         "schedule, the project budget, and a pro forma balance sheet as of closing.</li>"
         "<li><strong>The lender applies to USDA.</strong> Expect appraisals, an environmental review and, "
         "if needed, a feasibility study.</li>"
         "<li><strong>Conditional commitment, then closing.</strong> USDA issues a conditional commitment, "
         "the loan closes, and the loan note guarantee follows once the conditions are met.</li>"
         "</ol>"
         "<p>Related guides: <a href=\"/hotel-financing.html\">hotel financing</a> for SBA hotel rules, "
         '<a href="/sba-100-percent-financing.html">100% SBA financing</a> for buying your own building, '
         'and <a href="/sba-loans.html">SBA loans</a> if your site is in a city.</p>'
         '<p><a href="/match.html">Get matched with USDA and SBA lenders</a>, or talk to a specialist: '
         "(561) 268-0465.</p>"),
    ],
    "faqs": [
        ("What is a USDA business loan?",
         "Usually it means a Business &amp; Industry guaranteed loan: a loan from a bank or other lender, "
         "partly guaranteed by USDA Rural Development, for a business in a rural area."),
        ("What is the maximum USDA B&amp;I loan?",
         "$25 million per borrower, including existing B&amp;I balances. Cooperatives doing value-added "
         "agricultural processing can go higher with the Secretary's approval."),
        ("Does my town have to be under 50,000 people?",
         "The project must be outside any city or town of more than 50,000 people and outside the urbanized "
         "area attached to it. Check the address on USDA's eligibility map."),
        ("Can a USDA B&amp;I loan buy a business?",
         "Yes, if it's an entire business, not a partial stock purchase, and jobs are created or saved. Buyouts "
         "between existing owners qualify under conditions in the rule."),
        ("How much do I need to put down?",
         "The rule's minimum is 10% for an existing business and 20-25% for most new ones, by the tests in "
         "7 CFR 5001.105(d). Lenders may ask more."),
        ("Can USDA B&amp;I fund working capital?",
         "Yes, as a permanent working capital term loan. Lines of credit are not eligible."),
    ],
    "related": [
        ("/usda-business-loans/articles/", "USDA business loan articles"),
        ("/usda-business-loans/articles/usda-eligible-areas/", "USDA eligible areas"),
        ("/usda-business-loans/articles/usda-hotel-loans/", "USDA hotel loans"),
        ("/usda-business-loans/articles/usda-b-and-i-vs-sba-7a/", "USDA B&I vs SBA 7(a)"),
        ("/usda-business-loans/articles/usda-b-and-i-loan-rates-fees/", "USDA B&I rates and fees"),
        ("/10-million-business-loan.html", "$10 million business loans"),
    ],
    "sources": [PROJ, RURAL, LIMIT, TERM, INEL, BORR, FEAS, FEE, NOTICE, PROGRAM],
}]
