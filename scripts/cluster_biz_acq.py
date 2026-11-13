# -*- coding: utf-8 -*-
"""Buying a business with 5% down - SBA plan Cluster 4 spoke. New folder under
business-acquisition-financing/ with no Articles index, so no_hub, and the back link goes to
the pillar. Every rule is from SOP 50 10 8.1, Appendix 15, read on 2026-11-05. The pillar is
not edited. Never names the program lender, its loan officer or domain.
"""
from cluster_table import table
from sba_sources import SOP, FEES, SBA_7A, EQ

CLUSTER = {
    "pillar": "business-acquisition-financing.html",
    "hub": "business-acquisition-financing/articles",
    "no_hub": True,
    "back_href": "/business-acquisition-financing.html",
    "crumb": "Business Acquisition Financing",
    "cta_inline": "See if your purchase can be structured this way",
    "cta_button": "Talk to an SBA Specialist",
}

ARTICLES = [{
    "slug": "buy-a-business-with-5-percent-down",
    "crumb": "Buy a Business With 5% Down",
    "title": "Buy a Business With 5% Down: SBA Rules for 2026 | Axiant",
    "og_title": "How to Buy a Business With 5% Down Using an SBA Loan and a Seller Note",
    "h1": "How to Buy a Business With 5% Down Using an SBA Loan and a Seller Note",
    "headline": "How to Buy a Business With 5% Down Using an SBA Loan and a Seller Note",
    "lede": "The structure is real, but the 5% is half of a 10% rule. Here is how it works under "
            "SOP 50 10 8.1, and why the seller has to agree to wait",
    "meta_desc": "How to buy a business with 5% down: SBA's 10% equity rule, a seller note on full standby for the other 5%, the 1.25 cash flow test and a worked example.",
    "article_desc": "How an SBA 7(a) acquisition can work with 5% cash and a seller note on full "
                    "standby under SOP 50 10 8.1, including who qualifies and what it costs.",
    "keywords": "buy a business with 5% down, sba 5 percent down business acquisition, seller "
                "note equity injection, sba equity injection change of ownership, full standby seller note",
    "quick_answer": "It can be done on an SBA 7(a) loan, but 5% is half of a rule. A first-time "
                    "buyer needs <strong>10% equity</strong> of total project cost, and a seller note on "
                    "<strong>full standby</strong> can supply up to half, leaving about <strong>5% in "
                    "cash</strong>. The seller gets no payments for the loan's term. Axiant Partners, a "
                    "business-loan broker in Boca Raton, can find lenders who allow it. Lender "
                    "requirements commonly go beyond these minimums.",
    "sections": [
        ("How the 5% Down Structure Works",
         '<p><a href="https://www.sba.gov/document/sop-50-10-lender-development-company-loan-programs" '
         'rel="noopener nofollow" target="_blank">SBA SOP 50 10 8.1</a>, effective October 1, 2026, sets '
         "the rules in its Appendix 15. A buyer who doesn't already own the business usually falls "
         "under an <strong>Initial Acquisition</strong>, the default category, with a 10% minimum "
         "equity injection that can't be reduced or eliminated.</p>"
         + table(["Part of the 10%", "Source", "SBA rule"], [
             ["At least half", "Cash not borrowed, including a gift; certain verified prepaid expenses and grants", "Unlimited sources, no cap"],
             ["No more than half", "Seller note on full standby", "No principal or interest payments for the term of the 7(a) loan"],
             ["No more than half, combined", "Other standby debt; non-controlling minority investors with under 20%", "Counted together with the seller note"],
         ])
         + "<p>So on a $1,000,000 project, the minimum is $100,000, and at most $50,000 of that can "
         "come from limited sources. The base is total project cost, not just the price, so closing "
         "costs and any working capital raise it. The standby debt may accrue interest and may start "
         "being paid only after the 7(a) loan is paid off.</p>"),
        ("The Catch: The Seller Has to Agree",
         "<p>Full standby asks a lot. On a 10-year loan, the seller could wait a decade to see a "
         "dollar of that note, behind the lender. Many won't accept it, and you'll need a price or "
         "other terms that make it worthwhile. Seller debt that does have payments can still be part "
         "of a deal, but it doesn't count as equity, and the payments have to fit inside your cash "
         "flow test.</p>"
         "<ul>"
         "<li><strong>Interest-only seller debt.</strong> When it isn't on standby, the lender must "
         "underwrite it on an amortization of no more than 10 years.</li>"
         "<li><strong>Refinancing later.</strong> Seller debt from a change of ownership becomes "
         "eligible for refinancing after 36 months in place and current.</li>"
         "<li><strong>Seller transition.</strong> In this kind of deal the seller can't stay on as an "
         "officer, director, owner or employee. A consulting contract is allowed, up to 24 months in "
         "total.</li>"
         "</ul>"),
        ("Who Can Get This, and What Lenders Add",
         "<p>SBA rules are a floor. Lenders add their own, and that is why one says no where another "
         "says yes. These are common practices, not promises:</p>"
         "<ul>"
         "<li><strong>Relevant experience.</strong> Time in the industry, or as a manager at a similar "
         "company, carries the most weight. The lender has to document it.</li>"
         "<li><strong>Credit.</strong> Many SBA lenders look for roughly 650-680 or higher.</li>"
         "<li><strong>Reserves.</strong> 5% down doesn't mean 5% is all you need. Expect to show cash "
         "left over after closing.</li>"
         "<li><strong>Bigger deals.</strong> On roughly $1M-$5M purchases, lenders often want more "
         "collateral or a larger seller note. The SOP requires a Quality of Earnings report at a "
         "$3 million purchase price.</li>"
         "<li><strong>Citizenship.</strong> All direct and indirect owners and required guarantors must "
         "be U.S. citizens or nationals living in the U.S. or its territories.</li>"
         "</ul>"
         "<p>Many SBA lenders also decline certain businesses, such as gas stations and anything with "
         "underground tanks, restaurants and bars, vape shops, delivery routes such as FedEx, and "
         "fleet-heavy companies. If yours is on that list, a different lender or a "
         '<a href="/business-term-loans.html">conventional term loan</a> may fit.</p>'),
        ("The Cash Flow Test and the Valuation",
         "<p>The business has to carry the deal. Appendix 15 requires debt service coverage of at least "
         "<strong>1.25 to 1</strong> for an Initial Acquisition, based on the last fiscal year-end or a "
         "two-year average. Total eligible debt supporting the purchase, including seller debt that "
         "isn't on full standby, is limited to the business valuation. If the price is higher than the "
         "valuation supports, the difference has to come from extra equity or full-standby funds. The "
         "full rule table by deal type is in <a href=\"/business-acquisition-financing/articles/sba-seller-note-equity-injection-rules/\">"
         "full equity and seller note rules</a>.</p>"
         "<p>A business valuation is required, though the lender may do its own at $350,000 or less "
         "unless buyer and seller have a close relationship. Term is also tighter than people assume: "
         "acquisition loans amortize over 10 years at most. Real estate bought in the deal can run up "
         "to 25 years, either as a separate loan or blended, and the same equity rules apply to it.</p>"),
        ("Worked Example: A $1,000,000 Purchase",
         "<p><strong>Illustrative numbers, not a quote.</strong> A manager in the industry buys a service "
         "company for $1,000,000, with no real estate, plus about $15,000 in closing costs. The "
         "estimated guaranty fee, at 3.5% of the 75% guaranteed share under the "
         '<a href="https://www.naggl.org/sba-issues-notices-announcing-fy-2027-7a-and-504-loan-program-fees/" '
         'rel="noopener nofollow" target="_blank">FY2027 fee notice</a>, adds about $24,560.</p>'
         + table(["Item", "Amount"], [
             ["Total project cost", "About $1,039,560"],
             ["Buyer's cash (5%)", "About $51,980"],
             ["Seller note on full standby (5%)", "About $51,980"],
             ["SBA 7(a) loan (90%)", "About $935,600"],
             ["Assumed rate and term", "10.5%, 10 years"],
             ["Monthly payment", "About $12,625 ($151,500 a year)"],
             ["Cash flow needed at 1.25 to 1", "About $189,400 a year"],
         ])
         + "<p>If the company produces less than about $189,400 a year after any adjustments, the lender "
         "will likely ask for a lower price or more equity. You also still need to pay yourself.</p>"),
        ("Already Own a Business? You May Need Less",
         "<p>A different category applies if you already own a company in the same four-digit NAICS "
         "industry group, which is how <a href=\"/business-acquisition-financing/articles/buy-a-competitor-sba-loan/\">"
         "buying a competitor with an SBA loan</a> works. A <strong>Business Expansion</strong> needs two full fiscal years of operation "
         "under current ownership and the purchase of 100% of the target. The minimum is still 10%, but "
         "the lender may reduce or eliminate it if you have enough liquidity and working capital and "
         "your balance sheet doesn't show negative net worth. The coverage test is 1.15 to 1. If "
         "the lender waives equity, it can't add dedicated permanent working capital to this or another "
         "7(a) term loan within 90 days.</p>"
         "<p>Next steps: review the broader "
         '<a href="/business-acquisition-financing.html">business acquisition financing</a> guide, read '
         'about <a href="/sba-loans/articles/where-sba-loan-down-payment-can-come-from/">where an SBA '
         'down payment can come from</a>, and <a href="/match.html">get matched</a>, or talk to an SBA '
         'specialist at (561) 268-0465. Buying your building too? See '
         '<a href="/sba-100-percent-financing.html">100% SBA financing</a>, though in a change of '
         "ownership the real estate is subject to the same equity rules.</p>"),
    ],
    "faqs": [
        ("Can you really buy a business with 5% down?",
         "Yes, in some SBA 7(a) deals. The rule is 10% equity, and a seller note on full standby can "
         "cover up to half of that, leaving about 5% in cash. The seller must agree and the lender must "
         "allow it."),
        ("What does full standby mean for a seller note?",
         "No payments of principal or interest for the term of the 7(a) loan. Interest may accrue and be "
         "paid after the SBA loan is repaid. The seller also subordinates to the lender."),
        ("Can I borrow my 5% down payment?",
         "Cash for the unlimited portion must not be borrowed, with a narrow exception for a personal "
         "loan to a guarantor if repayment can be shown to come from outside the business's cash flow. A "
         "gift can count if it's documented."),
        ("Does the 10% apply to the price or to total costs?",
         "It applies to total project cost, meaning all costs required to become operational, except "
         "lines of credit and 504 loans. That's usually more than the purchase price."),
        ("Can the SBA equity requirement be waived?",
         "Not on an Initial Acquisition. A lender may reduce or eliminate it on a Business Expansion or "
         "Owner Buyout, if the borrower has enough liquidity and working capital and no negative net "
         "worth at the last fiscal year-end."),
        ("What credit score do I need?",
         "SBA sets no single public score for this. Many lenders look for roughly 650-680 or higher, and "
         "strong experience and cash flow can matter as much. Treat that as a typical range, not a rule."),
    ],
    "related": [
        ("/business-acquisition-financing.html", "Business acquisition financing"),
        ("/sba-loans/articles/where-sba-loan-down-payment-can-come-from/", "Where an SBA down payment can come from"),
        ("/sba-loans/articles/sba-loan-buy-out-business-partner/", "SBA loans to buy out a partner"),
        ("/sba-loans/articles/sba-loan-franchise-acquisition/", "SBA franchise acquisition"),
        ("/buying-a-business-financing-guide/", "Buying a business financing guide"),
        ("/sba-100-percent-financing.html", "100% SBA financing for your building"),
        ("/business-acquisition-financing/articles/sba-seller-note-equity-injection-rules/", "SBA seller note and equity rules"),
    ],
    "sources": [SOP, FEES, SBA_7A, EQ],
}]
