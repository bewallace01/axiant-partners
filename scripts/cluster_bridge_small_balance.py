# -*- coding: utf-8 -*-
"""Small balance commercial bridge loans - new spoke, from the 2026-11-10 daily batch.

Search Console, Oct 12 to Nov 8 2026: "small balance commercial bridge loans" 44 impressions at
position 20, landing on the value-add spoke, which doesn't cover loan size. No bridge page treats
small loans as a segment (the pillar has one sentence). Rates, points, terms and LTV reuse the
ranges the pillar and the 2026 rates spoke already publish (9-14%, 1-4 points, 6-36 months,
60-75% LTV). The worked example is computed, labelled illustrative, with an assumed $8,000 of
third-party reports. Agency small-loan program limits are deliberately not quoted: sources
disagree on whether Freddie Mac's SBL product still exists in 2026. Never names a lender.
no_hub: the articles index is edited by hand.
"""
from cluster_table import table
from sba_sources import SBA_504, SBA_7A, OCC

INTERAGENCY = ("https://www.ecfr.gov/current/title-12/chapter-I/part-34/subpart-D",
               "12 CFR Part 34, Subpart D: Real Estate Lending Standards",
               "The interagency real estate lending standards, including supervisory loan-to-value limits for banks.")

CLUSTER = {
    "pillar": "commercial-bridge-loans.html",
    "hub": "commercial-bridge-loans/articles",
    "no_hub": True,
    "back_href": "/commercial-bridge-loans.html",
    "crumb": "Commercial Bridge Loans",
    "cta_inline": "Compare small balance bridge lenders",
    "cta_button": "Get Matched for a Bridge Loan",
}

ARTICLES = [{
    "slug": "small-balance-commercial-bridge-loans",
    "crumb": "Small Balance Bridge Loans",
    "title": "Small Balance Commercial Bridge Loans: Who Lends | Axiant",
    "og_title": "Small Balance Commercial Bridge Loans: Who Lends and What It Costs",
    "h1": "Small Balance Commercial Bridge Loans: Who Lends and What It Costs",
    "headline": "Small Balance Commercial Bridge Loans: Who Lends and What It Costs",
    "lede": "Which lenders do bridge loans of a few million dollars or less, why small loans cost a little more, "
            "and how to line up the exit before you close",
    "meta_desc": "Small balance commercial bridge loans: which lenders take loans of a few million or less, typical 9-14% rates with 1-4 points, recourse, and exits.",
    "article_desc": "Who makes small balance commercial bridge loans, how pricing, recourse and minimum loan sizes differ "
                    "from larger bridge deals, the exits that fit small properties, and a worked example.",
    "keywords": "small balance commercial bridge loans, small balance bridge loan, small commercial bridge loan, "
                "bridge loan under 5 million, small balance commercial real estate loans",
    "quick_answer": "Small balance commercial bridge loans, commonly loans of a few million dollars or less, come mostly "
                    "from local and regional banks, private lenders and smaller debt funds, since many large funds set "
                    "minimum loan sizes above that. Pricing typically sits in the same <strong>9-14%</strong> range with "
                    "<strong>1-4 points</strong>, often at the higher end because fixed costs weigh more on a small loan, "
                    "and recourse is more common. Typical ranges, not a quote; Axiant Partners, a business-loan broker "
                    "in Boca Raton, compares bridge lenders.",
    "sections": [
        ("What Counts as Small Balance",
         "<p>There's no official cutoff. Lenders commonly use \"small balance\" for commercial real estate loans of a few "
         "million dollars or less, and some programs draw the line at $5 million or another round number. What matters "
         "for you is that the lender pool changes as the loan gets smaller: some of the bigger bridge lenders don't "
         "quote below their minimum, and the ones that do often price and structure the loan differently.</p>"
         "<p>The general mechanics don't change. A bridge loan is short-term, usually interest-only, and repaid by a "
         'sale or a permanent loan. For the basics, see <a href="/commercial-bridge-loans.html">commercial bridge loans</a>.</p>'),
        ("Who Makes Small Balance Bridge Loans",
         table(["Lender type", "Usually fits", "Watch for"], [
             ["Local or regional bank", "Borrowers with a banking relationship and a clear exit", "Full recourse, slower approval, deposit requests"],
             ["Private or hard money lender", "Speed, a property that needs work, thinner files", "Higher rates and points, short terms, extension fees"],
             ["Smaller debt fund", "Value-add business plans with a lease-up story", "Minimum loan sizes, reserves, exit fees"],
             ["Credit union", "Members with owner-occupied or local investment property", "Lending caps and membership rules"],
         ])
         + "<p>Banks follow the interagency real estate lending standards, which set supervisory loan-to-value limits by "
         'property type (<a href="https://www.ecfr.gov/current/title-12/chapter-I/part-34/subpart-D" rel="noopener nofollow" target="_blank">12 CFR Part 34, Subpart D</a>). '
         "In practice most bridge lenders lend below those limits, commonly 60-75% of value.</p>"),
        ("Why Small Bridge Loans Can Cost More",
         "<p>Rates and points on small loans typically fall in the same ranges published on our "
         '<a href="/commercial-bridge-loans/articles/typical-commercial-bridge-loan-rates-2026/">2026 bridge rates</a> page, '
         "but often toward the top, for two reasons:</p>"
         "<ul>"
         "<li><strong>Fixed costs.</strong> Appraisal, environmental report, title and legal cost about the same on a small "
         "loan as on a larger one, so they're a bigger share of the loan. If $8,000 of reports is about 0.53% of a "
         "$1,500,000 loan, the same reports are 0.1% of $8,000,000.</li>"
         "<li><strong>Minimum fees.</strong> Some lenders charge a minimum origination or exit fee in dollars, which "
         "works out to more points on a small loan.</li>"
         "</ul>"
         "<p>Compare offers on total cost for the months you'll actually hold the loan, not on the rate alone.</p>"),
        ("Worked Example: A $1.5 Million Bridge Loan",
         "<p><strong>Illustrative, not a quote.</strong> An investor buys a $2,000,000 small retail building that is half "
         "vacant and borrows 75%, or <strong>$1,500,000</strong>, interest-only for 12 months at 11% with 2 points. Assume "
         "$8,000 of third-party reports.</p>"
         + table(["Cost", "About"], [
             ["Monthly interest", "$13,750"],
             ["Interest for 12 months", "$165,000"],
             ["Points (2%)", "$30,000"],
             ["Third-party reports (assumed)", "$8,000"],
             ["Total for 12 months", "$203,000"],
         ])
         + "<p>That's about 13.5% of the loan for one year, before any extension fee. The rate, points and LTV sit inside "
         "the typical ranges above. If lease-up takes longer and the loan needs a six-month extension, add another "
         "$82,500 of interest plus whatever extension fee the lender charges, which is why the exit plan matters more "
         "than a quarter point of rate.</p>"),
        ("Recourse and Guarantees",
         "<p>On larger institutional bridge loans, non-recourse terms with carve-outs are common. On small balance loans, "
         "a full or partial personal guarantee is more common, especially from banks. Ask whether the guarantee "
         "burns off when the property hits an occupancy or income target, and what triggers recourse. Our "
         '<a href="/commercial-bridge-loans/articles/bridge-loan-pitfalls-what-can-go-wrong/">bridge loan pitfalls</a> '
         "guide covers the terms that cause trouble at maturity.</p>"),
        ("Exits That Fit Small Properties",
         "<ul>"
         "<li><strong>Bank permanent loan</strong> once the property is leased and the income supports the payment.</li>"
         '<li><strong>SBA 504 or 7(a)</strong> if your business will occupy the building: SBA requires owner occupancy of at least 51% of an existing building. See the <a href="/sba-loans/articles/sba-504-loan-amortization-schedule/">SBA 504 amortization schedule</a> for how that loan pays down.</li>'
         "<li><strong>Agency small-loan programs</strong> for apartment buildings with five or more units. Their size limits and "
         "terms change, so confirm the current program with a lender before you count on it.</li>"
         "<li><strong>Sale</strong> after the value-add work is done.</li>"
         "</ul>"
         "<p>Get a soft read on the exit loan before you close the bridge. If the takeout lender won't lend enough at "
         "the stabilized value, the bridge will have to be paid down or extended. See "
         '<a href="/commercial-bridge-loans/articles/refinance-hard-money-loan-to-permanent-financing/">refinancing into permanent financing</a>.</p>'),
        ("How to Shop a Small Balance Bridge Loan",
         "<ol>"
         "<li><strong>Ask the minimum loan size first.</strong> It saves a week with a lender that won't quote.</li>"
         "<li><strong>Get total cost in writing.</strong> Rate, points, minimum fees, exit fee, extension terms and third-party costs.</li>"
         "<li><strong>Clarify the guarantee.</strong> Full, partial or carve-out only, and whether it burns off.</li>"
         "<li><strong>Match the term to the plan.</strong> Lease-up or renovation time plus the time to close the exit loan.</li>"
         "<li><strong>Line up the exit.</strong> A soft quote from the bank, SBA lender or agency lender you plan to refinance with.</li>"
         "</ol>"
         '<p><a href="/match.html">Get matched with bridge lenders</a> that take loans your size, or call '
         '<a href="tel:+15612680465">(561) 268-0465</a>. Approval and terms are up to the lender.</p>'),
    ],
    "faqs": [
        ("What is a small balance commercial bridge loan?",
         "A short-term, usually interest-only commercial real estate loan of a few million dollars or less, used to buy, "
         "reposition or refinance a property until it can be sold or moved to permanent financing. There's no official "
         "cutoff for small balance."),
        ("Who makes small balance bridge loans?",
         "Mostly local and regional banks, private and hard money lenders, smaller debt funds and some credit unions. "
         "Many large bridge lenders set minimum loan sizes above that range."),
        ("What are typical rates on a small balance bridge loan?",
         "Typically within the general 9-14% range with 1-4 points, often toward the higher end because fixed costs and "
         "minimum fees weigh more on a small loan. Terms commonly run 6-36 months."),
        ("Are small balance bridge loans recourse?",
         "Often, yes. A full or partial personal guarantee is more common on small loans than on larger institutional "
         "bridge loans, especially from banks."),
        ("How much can I borrow on a small bridge loan?",
         "Commonly 60-75% of the property's value, depending on the property, the business plan and the lender."),
    ],
    "related": [
        ("/commercial-bridge-loans/articles/typical-commercial-bridge-loan-rates-2026/", "Commercial bridge loan rates 2026"),
        ("/commercial-bridge-loans/articles/bridge-loan-value-add-commercial-property/", "Bridge loans for value-add property"),
        ("/commercial-bridge-loans/articles/what-do-lenders-look-for-commercial-bridge-loan/", "What bridge lenders look for"),
        ("/commercial-bridge-loans/articles/bridge-loan-pitfalls-what-can-go-wrong/", "Bridge loan pitfalls"),
        ("/sba-loans/articles/sba-504-loan-amortization-schedule/", "SBA 504 amortization schedule"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [INTERAGENCY, OCC, SBA_504, SBA_7A],
}]
