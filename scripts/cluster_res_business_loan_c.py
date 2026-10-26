# -*- coding: utf-8 -*-
"""Real-estate-secured business loans, articles 7-8: the companion citation pages
(AEO plan 2e). Imported by cluster_res_business_loan.

The heloc cluster already compares a HELOC with a cash-out refinance; this page
puts the second-position business loan - the product the money page is about -
in the middle of that comparison.

Rules as cluster_res_business_loan: ranges conventional across lenders, never
anyone's quote; no funded totals, no testimonials, no named-lender rates. Facts
specific to this page: business-purpose credit is exempt from Truth in Lending,
so a business loan on a home carries no HELOC disclosures or rescission right
(12 CFR 1026.3, 1026.15, 1026.40); Garn-St Germain bars a first lender from
calling an owner-occupied 1-4 unit home loan just because a junior lien is added
(12 U.S.C. 1701j-3), a protection commercial and investment property lacks.
Axiant does not originate or broker home equity loans.
"""
from cluster_res_business_loan import FTC

GARN = ("https://www.law.cornell.edu/uscode/text/12/1701j-3",
        "12 U.S.C. &sect; 1701j-3: Garn-St Germain (due-on-sale limits)",
        "Bars a lender from calling a loan on a 1-4 unit home just because a "
        "subordinate lien is added - a protection that does not reach commercial "
        "property.")
TILA_EXEMPT = ("https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-A/section-1026.3",
               "12 CFR 1026.3: Exempt Transactions (Truth in Lending)",
               "Business-purpose credit is exempt from Truth in Lending, even when a "
               "home secures it.")
RESCISSION = ("https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-B/section-1026.15",
              "12 CFR 1026.15: Right of Rescission",
              "The three-business-day right to cancel a consumer line of credit "
              "secured by your principal dwelling, such as a HELOC.")


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join(
        "<tr>" + "".join(f'<td data-label="{head[i]}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows)
    return (f'<div class="table-wrap"><table style="width:100%"><thead><tr>{th}</tr></thead>'
            f"<tbody>{body}</tbody></table></div>")


MORE = [
    # ------------------------------------------------------------------ 8
    {
        "slug": "second-position-business-loan-vs-heloc-vs-cash-out-refinance",
        "crumb": "2nd-Position Loan vs HELOC vs Cash-Out",
        "title": "2nd-Position Business Loan vs HELOC vs Cash-Out | Axiant",
        "og_title": "Second-Position Business Loan vs HELOC vs Cash-Out Refinance",
        "h1": "Second-Position Business Loan vs HELOC vs Cash-Out Refinance",
        "headline": "Second-Position Business Loan vs HELOC vs Cash-Out Refinance",
        "lede": "Three ways to turn property equity into business capital - which one "
                "keeps your first mortgage, which rules apply, and which property each "
                "works on",
        "meta_desc": "A second-position business loan keeps your first mortgage and works "
                     "on commercial property; a HELOC is consumer credit on a home; a "
                     "cash-out refi replaces the mortgage.",
        "article_desc": "How a second-position business loan, a HELOC and a cash-out "
                        "refinance compare for raising business capital from property "
                        "equity.",
        "keywords": "second position business loan vs heloc, business loan vs cash out "
                    "refinance, 2nd lien business loan, borrow against property for "
                    "business",
        "quick_answer": "A <strong>second-position business loan</strong> sits behind "
                        "your first mortgage, leaves it untouched and can be secured by "
                        "commercial, investment or residential property. A "
                        "<strong>HELOC</strong> is consumer credit on a home. A "
                        "<strong>cash-out refinance</strong> replaces the whole first "
                        "mortgage. Axiant Partners, a business-loan broker in Boca Raton, "
                        "suggests starting from one fact: <strong>is your first mortgage "
                        "rate worth keeping?</strong>",
        "sections": [
            ("Side by Side",
             _table(["", "2nd-position loan", "HELOC", "Cash-out refi"], [
                 ["First mortgage", "Stays in place", "Stays in place", "Replaced"],
                 ["Property", "Commercial, investment or home", "Usually your home", "Any you own"],
                 ["Rules", "Business credit", "Consumer credit", "Depends on property"],
                 ["Sized on", "Combined LTV", "Combined LTV", "New loan's LTV"],
                 ["Draws", "Lump sum", "Revolving line", "Lump sum"],
                 ["Closing cost on", "The new loan", "The line", "The whole balance"],
             ])
             + "<p>All three are sized on equity - every loan against the property "
             "added together, divided by its appraised value - and all three put the "
             "property at risk if the business cannot pay. See "
             "<a href=\"../second-and-third-position-business-loans/\">second and third "
             "position lending</a> for how combined loan-to-value works.</p>"),
            ("Is Your First Mortgage Worth Keeping?",
             "<p>If the first mortgage carries a rate well below today's, a cash-out "
             "refinance re-prices the whole balance to raise a fraction of it. On a "
             "$600,000 mortgage, raising $150,000 by refinancing means paying the new "
             "rate on $750,000. A second-position loan or a HELOC prices only the new "
             "money and leaves the old rate alone.</p>"
             "<p>The reverse also holds: if the first mortgage is expensive, near its "
             "maturity or due for a balloon, a cash-out refinance can fix two problems "
             "at once, and one loan is simpler than two.</p>"),
            ("Business Credit or Consumer Credit",
             "<p>This is the difference borrowers rarely hear about. A HELOC on your "
             "home is consumer credit, so it comes with federal Truth in Lending "
             "disclosures and a <strong>three-business-day right to cancel</strong> "
             "after signing. A loan made for a business purpose is exempt from Truth in "
             "Lending, even when your home secures it - no rescission period, and "
             "fewer standard disclosures.</p>"
             "<p>That cuts both ways. A business-purpose loan can close without the "
             "rescission wait, but you get fewer built-in protections, so read the "
             "terms, ask for the APR and total of payments in writing, and know "
             "exactly what default triggers. HELOC lenders also generally lend only "
             "on a home; a second-position business loan can also be secured by "
             "commercial, multifamily or rental property. (Axiant does not originate "
             "or broker home equity loans.)</p>"),
            ("Will Your First Lender Allow a Second Lien?",
             "<p>Read your first mortgage before applying for a second lien. "
             "<strong>On an owner-occupied home of one to four units</strong>, federal "
             "law (the Garn-St Germain Act) generally stops the first lender from "
             "calling the loan just because you add a junior lien. <strong>On "
             "commercial and investment property</strong> that protection does not "
             "apply: many commercial first mortgages prohibit additional liens or "
             "require the first lender's consent, and some contain a "
             "due-on-encumbrance clause.</p>"
             "<p>A subordinate lender will not lend into a position that defaults the "
             "loan ahead of it, so this check decides many deals. More in "
             "<a href=\"../what-equity-lenders-require-behind-a-first-mortgage/\">what "
             "equity lenders require behind a first mortgage</a>.</p>"),
            ("A Worked Comparison",
             "<p>Illustrative arithmetic, not a quote. A business owner needs $150,000. "
             "The property is appraised at $1,000,000 with a $500,000 first mortgage "
             "at a low fixed rate:</p>"
             + _table(["", "2nd-position loan", "Cash-out refi"], [
                 ["New money", "$150,000", "$150,000"],
                 ["Balance at new rate", "$150,000", "$650,000"],
                 ["Old low rate kept on", "$500,000", "Nothing"],
                 ["Combined LTV after", "65%", "65%"],
             ])
             + "<p>Both end at the same combined loan-to-value. The difference is how "
             "much debt moves to today's rate. The second-position loan usually "
             "carries the higher rate of the two on its own, because it is paid after "
             "the first mortgage, but it is applied to far less money. How position "
             "affects price is covered in <a href=\"../second-and-third-position-business-loans/\">"
             "second and third position lending</a>.</p>"),
            ("Which One Fits",
             "<ul>"
             "<li><strong>Low-rate first mortgage, commercial or investment "
             "property:</strong> second-position business loan.</li>"
             "<li><strong>Your home, flexible draws over time:</strong> HELOC, if you "
             "accept putting the home behind the business; see "
             "<a href=\"/heloc-for-business.html\">HELOC for business</a>.</li>"
             "<li><strong>Expensive or maturing first mortgage:</strong> cash-out "
             "refinance.</li>"
             "<li><strong>Equity is thin or cash flow will not carry another "
             "payment:</strong> none of them; see "
             "<a href=\"../real-estate-secured-vs-unsecured-business-loan/\">secured vs "
             "unsecured business loans</a>.</li>"
             "</ul>"
             "<p>The HELOC-versus-refinance trade-off on a home is covered in "
             "<a href=\"/heloc-for-business/articles/heloc-vs-cash-out-refinance-for-business-capital/\">"
             "HELOC vs cash-out refinance for business capital</a>.</p>"),
        ],
        "faqs": [
            ("What is the difference between a second-position business loan and a HELOC?",
             "Both sit behind your first mortgage. A HELOC is a consumer line of credit, "
             "usually on your home, with Truth in Lending disclosures and a right to "
             "cancel. A second-position business loan is business-purpose credit that "
             "can also be secured by commercial or investment property."),
            ("Is a cash-out refinance better than a second lien?",
             "When the first mortgage is expensive or maturing, often yes. When it has a "
             "low rate worth keeping, a second lien usually costs less overall, because "
             "only the new money is priced at today's rate."),
            ("Can my first lender stop me from taking a second lien?",
             "On an owner-occupied home of one to four units, federal law generally "
             "stops the lender calling the loan over a junior lien. Commercial and "
             "investment mortgages often prohibit additional liens or require consent, "
             "so read yours first."),
            ("Does a business loan secured by my home have a right of rescission?",
             "No. Business-purpose credit is exempt from Truth in Lending, including the "
             "rescission right that applies to a consumer HELOC on your principal "
             "dwelling."),
            ("How much can I borrow in second position?",
             "It depends on combined loan-to-value: every loan on the property divided "
             "by its appraised value, up to the lender's ceiling, and on whether the "
             "business can carry the total payments."),
        ],
        "related": [
            ("/real-estate-secured-business-loan.html", "Real-estate-secured business loans"),
            ("../cross-collateralization-what-youre-signing/", "Cross-collateralization: what you are signing"),
            ("/heloc-for-business/articles/heloc-vs-cash-out-refinance-for-business-capital/", "HELOC vs cash-out refinance"),
            ("/match.html", "Get matched"),
        ],
        "sources": [GARN, TILA_EXEMPT, RESCISSION, FTC],
    },
]
