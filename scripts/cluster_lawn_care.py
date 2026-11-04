# -*- coding: utf-8 -*-
"""Lawn care business loans - new spoke under landscaping-business-financing/.

Search Console (Aug 5 - Nov 2, 2026): 89 lawn care queries, 2,427 impressions at
about position 29, 0 attributed clicks. Top: "lawn care business loans" (210).

The landscaping pillar's title already names lawn care, and it stays untouched.
This page is deliberately distinct: the owner-operator or small mowing crew
borrowing small amounts, not a landscaping firm taking on crews and commercial
contracts. The spokes in this folder cover those larger moves.

The folder has no Articles index, so no_hub. Mower, rate and down payment ranges
match equipment/zero-turn-mowers and equipment-financing/articles/
commercial-mower-financing; line of credit ranges match the electrical contractor
page. Microloan facts read from sba.gov on 2026-11-04. No funded totals, no
testimonials, no named-lender rates. One entity: Axiant Partners, (561) 268-0465,
Boca Raton.
"""
from cluster_security_guard import IRS_946, SBA_7A, FTC, SBCS

CLUSTER = {
    "pillar": "landscaping-business-financing.html",
    "hub": "landscaping-business-financing",
    "no_hub": True,
    "crumb": "Landscaping Business Financing",
    "cta_inline": "See what your routes support",
    "cta_button": "Get Matched for a Lawn Care Loan",
}

SBA_MICRO = ("https://www.sba.gov/funding-programs/loans/microloans",
             "SBA Microloans",
             "Loans up to $50,000 for working capital, supplies, machinery and "
             "equipment, averaging about $13,000, with a maximum term of seven years.")

ARTICLES = [
    {
        "slug": "lawn-care-business-loans",
        "crumb": "Lawn Care Business Loans",
        "title": "Lawn Care Business Loans: Options and Rates | Axiant",
        "og_title": "Lawn Care Business Loans: Options, Rates and What You Qualify For",
        "h1": "Lawn Care Business Loans: Options, Rates and What You Qualify For",
        "headline": "Lawn Care Business Loans: Options, Rates and What You Qualify For",
        "lede": "For owner-operators and small mowing crews: how to pay for a mower, "
                "a trailer, or the slow months, and what lenders will want to see",
        "meta_desc": "Lawn care business loans compared: mower financing about 6-15% with 0-20% down, SBA microloans up to $50,000, and lines of credit for slow months.",
        "article_desc": "Financing options for lawn care owner-operators and small "
                        "crews, with typical rates, a worked example and what "
                        "lenders check.",
        "keywords": "lawn care business loans, lawn care company loans, small "
                    "business loans for lawn care, lawn care equipment financing, "
                    "lawn mowing business loan",
        "quick_answer": "Most lawn care businesses need one of two things. "
                        "<strong>Equipment financing</strong> pays for mowers and "
                        "trailers, commonly about <strong>6-15%</strong> over 24-48 "
                        "months with <strong>0-20% down</strong>. A "
                        "<strong>line of credit</strong> or small working capital loan "
                        "covers payroll and fuel in the slow months. New companies can "
                        "also look at "
                        "<strong>SBA microloans up to $50,000</strong>. Axiant "
                        "Partners, a business-loan broker in Boca Raton, matches lawn "
                        "care owners with lenders. These are typical ranges across "
                        "lenders, not a quote.",
        "sections": [
            ("Lawn Care Financing Options at a Glance",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Need</th><th>Usual fit</th><th>Typical range</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Need">Mower or stand-on</td>'
             '<td data-label="Usual fit">Equipment loan or lease</td>'
             '<td data-label="Typical range">About 6-15%; 24-48 months; 0-20% down</td></tr>'
             '<tr><td data-label="Need">Truck and trailer</td>'
             '<td data-label="Usual fit">Equipment or vehicle loan</td>'
             '<td data-label="Typical range">About 6-15%; 36-72 months</td></tr>'
             '<tr><td data-label="Need">Slow-season payroll</td>'
             '<td data-label="Usual fit">Business line of credit</td>'
             '<td data-label="Typical range">About 8-13% APR at banks; 14-30%+ online</td></tr>'
             '<tr><td data-label="Need">Starting out</td>'
             '<td data-label="Usual fit">SBA microloan</td>'
             '<td data-label="Typical range">Up to $50,000; up to 7 years</td></tr>'
             '<tr><td data-label="Need">Buying a route or company</td>'
             '<td data-label="Usual fit">SBA 7(a)</td>'
             '<td data-label="Typical range">Up to $5 million</td></tr>'
             "</tbody></table></div>"
             "<p>These are conventional ranges, not anyone's quote. Credit, time in "
             "business, deposits and the amount decide where you land.</p>"),
            ("Equipment First: Mowers, Trailers and Trucks",
             "<p>Commercial zero-turn mowers commonly run about "
             "<strong>$6,000-$20,000</strong> new depending on deck size and engine, "
             "and stand-on mowers about $7,000-$15,000. Used commercial machines "
             "typically cost 25-40% less. Because the mower secures the loan, this "
             "is usually the easiest financing for a small operator to get.</p>"
             "<ul>"
             "<li><strong>Credit.</strong> Many programs start around 550-600, with "
             "the strongest rates and $0-down offers at about 680 or higher.</li>"
             "<li><strong>Dealer financing.</strong> Often the cheapest route on a "
             "new machine during promotions, but it only covers that brand and "
             "usually nothing else you need.</li>"
             "<li><strong>Bundling.</strong> A single loan covering a mower, trailer "
             "and handheld gear can be simpler than several small accounts.</li>"
             "</ul>"
             "<p>For model-level detail, see "
             '<a href="/equipment/zero-turn-mowers/">zero-turn mower financing</a> '
             "and "
             '<a href="/equipment-financing/articles/commercial-mower-financing/">'
             "commercial mower financing</a>. Equipment you buy may qualify for "
             'Section 179 under <a href="https://www.irs.gov/publications/p946" '
             'rel="noopener nofollow" target="_blank">IRS Publication 946</a>; ask '
             "your accountant about current limits.</p>"),
            ("Worked Example: A Second Mower and Trailer",
             "<p><strong>Illustrative numbers, not a quote.</strong> A two-person "
             "crew finances a $14,000 commercial zero-turn at 8% over 48 months.</p>"
             "<ul>"
             "<li>Monthly payment: about <strong>$342</strong></li>"
             "<li>At an assumed $45 per cut, that is about <strong>8 cuts a "
             "month</strong> to cover the payment</li>"
             "</ul>"
             "<p>Adding a trailer and gear brings the total to $20,000 at an assumed "
             "9% over 48 months, or about <strong>$498 a month</strong>. Before "
             "signing, test the payment against your slowest month rather than July. "
             "If the winter months do not cover it, ask about seasonal payment "
             "structures, which some equipment lenders offer, or set the cash aside "
             "during the season.</p>"),
            ("Covering the Slow Months",
             "<p>Lawn care income can stop for months in northern markets and slow "
             "sharply in southern ones, while the truck note, insurance and spring "
             "startup costs keep coming. A revolving line of credit fits best: draw "
             "it in the off-season, pay it down in the peak, and pay interest only on "
             "what you use. Apply during the season, when your deposits look their "
             "best, not in January when the account is thin.</p>"
             "<p>Be careful with daily-payment cash advances. They are easy to get, "
             "but the payments do not stop when the grass does. See "
             '<a href="/working-capital-loans/articles/working-capital-loan-seasonal-businesses/">'
             "working capital for seasonal businesses</a> for how to plan the "
             "amount and timing.</p>"),
            ("Can a New Lawn Care Company Get a Loan?",
             "<p>Yes, though with fewer choices. Most online working capital lenders "
             "want 6-12 months or more of deposits. For a company with little "
             "history, the realistic routes are:</p>"
             "<ul>"
             "<li><strong>Equipment financing on personal credit</strong>, since the "
             "mower is collateral. Expect a higher rate or larger down payment.</li>"
             "<li><strong>SBA microloans</strong>, which "
             '<a href="https://www.sba.gov/funding-programs/loans/microloans" '
             'rel="noopener nofollow" target="_blank">go up to $50,000</a>, average '
             "about $13,000 and run up to seven years. They can fund working capital "
             "and equipment but cannot pay existing debts or buy real estate, and "
             "they come through nonprofit intermediaries, which may also ask for "
             "training.</li>"
             "<li><strong>Used equipment and dealer offers</strong>, which reduce how "
             "much you have to borrow in the first place.</li>"
             "<li><strong>Buying an existing route</strong>, where the seller's "
             'customers and records can support an <a href="https://www.sba.gov/funding-programs/loans/7a-loans" '
             'rel="noopener nofollow" target="_blank">SBA 7(a)</a> application.</li>'
             "</ul>"
             "<p>For the first-year picture, read our "
             '<a href="/startup-financing.html">startup financing</a> guide.</p>'),
            ("What Lenders Check on a Lawn Care Business",
             "<ul>"
             "<li><strong>Bank statements</strong>, usually 3-6 months. Keep job "
             "income in a business account, because cash and personal-account jobs "
             "do not count toward your revenue.</li>"
             "<li><strong>Customer base.</strong> Recurring route or contract "
             "customers read better than one-off cleanups, and a route list "
             "helps.</li>"
             "<li><strong>Seasonality.</strong> Lenders expect it, so show a full "
             "year if you can, including how you got through the last winter.</li>"
             "<li><strong>Existing debt.</strong> List mower notes, truck loans, "
             "credit cards and any advances.</li>"
             "<li><strong>Licenses and insurance.</strong> General liability, and a "
             "pesticide applicator license if your state requires one and you "
             "apply chemicals.</li>"
             "<li><strong>A quote or use of funds.</strong> \"$14,000 for a second "
             "mower\" reads much better than \"working capital.\"</li>"
             "</ul>"),
            ("Which Option Should You Choose?",
             "<ol>"
             "<li><strong>Buying a machine?</strong> Use equipment financing, not a "
             "general loan or a credit card, so the term matches the mower's working "
             "life.</li>"
             "<li><strong>Same cash gap every winter?</strong> Use a line of "
             "credit.</li>"
             "<li><strong>Under a year in business?</strong> Start with equipment on "
             "personal credit or a microloan.</li>"
             "<li><strong>Ready for commercial accounts or more crews?</strong> See "
             '<a href="/landscaping-business-financing/landscaping-financing-win-commercial-contracts/">'
             "financing to win commercial contracts</a> and "
             '<a href="/landscaping-business-financing/landscaping-equipment-financing-add-more-crews/">'
             "equipment financing to add crews</a>.</li>"
             "<li><strong>Compare total cost</strong>, including fees, guarantees "
             "and prepayment terms, and get them in writing. The "
             '<a href="https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic" '
             'rel="noopener nofollow" target="_blank">FTC</a> has warned small '
             "businesses about misrepresented costs.</li>"
             "</ol>"
             "<p>When you are ready, "
             '<a href="/match.html">get matched with lenders that fund lawn care '
             "companies</a>. One application covers equipment, lines of credit and "
             "working capital. For larger operations, see "
             '<a href="/landscaping-business-financing.html">landscaping business '
             "financing</a>.</p>"),
        ],
        "faqs": [
            ("Can I get a loan for a lawn care business?",
             "Yes. Most lawn care owners use equipment financing for mowers and "
             "trailers, and a line of credit or working capital loan for slow months. "
             "New companies can also look at SBA microloans of up to $50,000."),
            ("What credit score do I need for a lawn care business loan?",
             "Many equipment programs start around 550-600, with the strongest rates "
             "and $0-down offers at about 680 or higher. Bank lines and SBA loans "
             "usually want stronger credit. These are typical ranges across lenders, "
             "not a quote."),
            ("How much does it cost to finance a commercial mower?",
             "As an illustration, $14,000 at 8% over 48 months is about $342 a month. "
             "Rates commonly run about 6-15% with 0-20% down, depending on credit, "
             "time in business and whether the mower is new or used."),
            ("Can I start a lawn care business with no money?",
             "It is difficult to borrow with no cash and no history. Equipment "
             "financing on good personal credit, used equipment, or an SBA microloan "
             "are the most realistic routes, and you should expect to put something "
             "down."),
            ("How do lawn care companies get through winter?",
             "Usually with cash saved in season, a revolving line of credit, and "
             "off-season income such as snow removal or cleanups. Apply for a line "
             "during the season, when your deposits look strongest."),
            ("Are lawn care business loans different from landscaping loans?",
             "The products are the same. Lawn care owners usually borrow smaller "
             "amounts for mowers and slow months, while landscaping firms more often "
             "finance crews, heavier equipment and commercial contract ramps."),
        ],
        "related": [
            ("/landscaping-business-financing.html", "Landscaping business financing"),
            ("/equipment/zero-turn-mowers/", "Zero-turn mower financing"),
            ("/equipment-financing/articles/commercial-mower-financing/",
             "Commercial mower financing"),
            ("/landscaping-business-financing/landscaping-truck-trailer-financing-cash-flow/",
             "Financing a second truck and trailer"),
            ("/working-capital-loans/articles/working-capital-loan-seasonal-businesses/",
             "Working capital for seasonal businesses"),
            ("/startup-financing.html", "Startup financing"),
        ],
        "sources": [SBA_MICRO, SBA_7A, IRS_946, SBCS, FTC],
    },
]
