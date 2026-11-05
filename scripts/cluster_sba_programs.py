# -*- coding: utf-8 -*-
"""Two root money pages from the SBA plan: /sba-100-percent-financing.html and
/hotel-financing.html. Rendered with the v2 article template via root_file.

SOP rules read from SOP 50 10 8.1 on 2026-11-05 (the SOP wins over any lender appetite).
Fees: FY2027 notice as reported by NAGGL. Never names the program lender, its loan officer
or domain, and doesn't publish its terms as a quote. The existing 100% CRE article and the
SBA vs CMBS hotel page aren't edited, so a link from them to these pillars waits for the watch.
"""
from cluster_table import table
from sba_sources import SOP, FEES, OCC, SBA_7A, SBA_504, EQ

CLUSTER = {
    "pillar": "sba-loans.html",
    "hub": "sba-loans",
    "no_hub": True,
    "back_href": "/sba-loans.html",
    "crumb": "SBA Loans",
    "cta_inline": "Talk to an SBA specialist",
    "cta_button": "Talk to an SBA Specialist",
}

_SOP_A = ('<a href="https://www.sba.gov/document/sop-50-10-lender-development-company-loan-programs" '
          'rel="noopener nofollow" target="_blank">SBA SOP 50 10 8.1</a>')
_FEE_A = ('<a href="https://www.naggl.org/sba-issues-notices-announcing-fy-2027-7a-and-504-loan-program-fees/" '
          'rel="noopener nofollow" target="_blank">FY2027 fee notice</a>')

ARTICLES = [{
    "slug": "sba-100-percent-financing",
    "root_file": "sba-100-percent-financing.html",
    "crumb": "100% SBA Financing",
    "title": "100% SBA Financing for Owner-Occupied Buildings | Axiant",
    "og_title": "100% SBA Financing: Buying Your Business's Building With No Money Down",
    "h1": "100% SBA Financing: Buying Your Business's Building With No Money Down",
    "headline": "100% SBA Financing: Buying Your Business's Building With No Money Down",
    "lede": "Some 7(a) lenders will finance the entire purchase for an established, cash-flowing "
            "business. Who qualifies, what it costs, and why most lenders still want money down",
    "meta_desc": "100% SBA financing on owner-occupied buildings: who qualifies, the 51% occupancy rule, a $3M worked example, and how 7(a) compares with 504 and bank loans.",
    "article_desc": "How some SBA 7(a) lenders finance up to 100% of an owner-occupied building "
                    "for established businesses, with a worked example and comparison.",
    "keywords": "100% sba financing, sba 100 percent financing owner occupied, buy commercial building "
                "no money down, sba 7a no down payment, owner occupied commercial real estate",
    "quick_answer": "Some SBA 7(a) lenders finance up to <strong>100%</strong> of an owner-occupied "
                    "building for an established, cash-flowing business, commonly on loans of about "
                    "$350,000 to <strong>$5 million</strong> over <strong>25 years</strong>, with fees "
                    "rolled in. Your business must occupy at least <strong>51%</strong>. Start-ups and "
                    "purchases of a business don't qualify for zero down. Axiant Partners, a broker in "
                    "Boca Raton, can find these lenders. Terms are typical ranges, not a quote.",
    "sections": [
        ("Why 100% Is Possible on This Kind of Loan",
         f"<p>{_SOP_A} sets minimum equity for start-ups (one year or less in operation) and for changes "
         "of ownership, at 10%. For an existing business buying its own building, with no change of "
         "ownership, the SOP has no such fixed percentage. Instead, the lender or the SBA has to decide "
         "that the equity position and resulting debt-to-worth are acceptable. That leaves room for some "
         "lenders to go to 100%.</p>"
         "<p>It's lender appetite, not an SBA entitlement. Many 7(a) lenders still ask for 10% or more "
         "as their own policy. A \"no\" from your bank doesn't mean the SBA forbids it, which is "
         "where a broker can help.</p>"),
        ("Compare 100% 7(a), SBA 504 and a Bank Loan",
         table(["", "100% SBA 7(a)", "SBA 504", "Conventional bank"], [
             ["Typical money down", "$0 with some lenders", "At least 10%; 15-20% in special cases", "Commonly 20-25%"],
             ["Maximum term", "Up to 25 years on real estate", "10, 20 or 25 years", "Often 5-10 years, longer amortization"],
             ["Rate type", "Often Prime + a spread, adjusting quarterly", "Fixed on the SBA portion", "Varies, often resets"],
             ["Loan limit", "$5 million", "$5.5 million per the SBA's 504 page", "Lender limit"],
             ["Rolls in closing costs", "Often", "Limited", "Rarely"],
             ["Occupancy", "51% for existing buildings", "51% for existing buildings", "Lender policy"],
         ])
         + "<p>The 504 can win on a fixed rate and lower overall cost, and more cash down lowers your "
         "payment. Zero down wins when keeping cash in the business matters more. Use "
         '<a href="/sba-loans/articles/sba-loan-owner-occupied-commercial-property/">7(a) vs 504 for '
         "owner-occupied property</a> for more on that choice. Figures in this table are SBA rules or "
         "typical ranges, not quotes.</p>"),
        ("Who Usually Qualifies",
         "<p>These are common among lenders offering this structure, not SBA requirements:</p>"
         "<ul>"
         "<li><strong>Established operations.</strong> Two or more years, with cash flow last year and "
         "this year that supports the new payment. Projections alone rarely work.</li>"
         "<li><strong>Credit.</strong> Many SBA lenders look for roughly 650-680 or higher, and some go "
         "to the mid-660s with strong cash flow.</li>"
         "<li><strong>Clean history.</strong> A prior bankruptcy is often considered after about seven "
         "years, with a reasonable explanation.</li>"
         "<li><strong>Personal guarantees.</strong> Owners generally guarantee SBA loans, and lenders "
         "will usually take the building as collateral.</li>"
         "<li><strong>Citizenship.</strong> All direct and indirect owners and required guarantors must be U.S. "
         "citizens or nationals who live in the U.S. or its territories, under the SOP.</li>"
         "</ul>"
         "<p>Many SBA lenders exclude gas stations and anything with underground tanks, restaurants and "
         "bars, vape shops, FedEx routes and fleet-heavy companies, along with standalone working capital "
         "and projections-only deals. If that's you, look at "
         '<a href="/real-estate-secured-business-loan.html">a real estate secured loan</a> or '
         '<a href="/working-capital-loans.html">working capital</a> instead.</p>'),
        ("The Occupancy Rule and What Owner-Occupied Means",
         '<p>Under <a href="https://www.law.cornell.edu/cfr/text/13/120.131" rel="noopener nofollow" '
         'target="_blank">13 CFR 120.131</a> and the SOP, you must permanently occupy and use at least '
         "<strong>51%</strong> of the rentable property in an existing building, and may lease out up to "
         "49%. For new construction it's <strong>60%</strong>, with stricter rules on the rest. An "
         "investor buying a building to rent doesn't qualify, so the owner-occupied test is what makes "
         "this possible.</p>"
         "<ul>"
         "<li><strong>Holding companies.</strong> A related real estate company can own the building and "
         "lease all of it to your operating company, which must then meet the same occupancy test.</li>"
         "<li><strong>Extra land.</strong> Land in the purchase should be used by the business, for "
         "example paved for parking or used as a yard. Lenders question excess land.</li>"
         "<li><strong>Improvements.</strong> Small tenant improvements can often be included, but "
         "lenders commonly want them funded within a few months.</li>"
         "</ul>"),
        ("Worked Example: Buying a $3,000,000 Building",
         "<p><strong>Illustrative numbers, not a quote or an offer; rates and fees change, and every "
         "loan is subject to approval.</strong> A company that has rented for years buys its building. "
         f"The guaranty fee below is recomputed from the {_FEE_A}: 3.5% on the first $1 million of the "
         "75% guaranteed share, plus 3.75% above that, with the fee itself financed.</p>"
         + table(["Item", "Amount"], [
             ["Purchase price", "$3,000,000"],
             ["SBA guaranty fee (estimate)", "About $84,880"],
             ["7(a) packaging fee (estimate)", "$2,500"],
             ["Appraisal, environmental, escrow, etc. (estimate)", "$19,500"],
             ["<strong>Total project cost</strong>", "<strong>About $3,106,880</strong>"],
             ["Cash down", "$0 (0%)"],
             ["SBA 7(a) loan", "About $3,106,880"],
             ["Assumed rate and term", "7.75%, 25 years"],
             ["Monthly principal and interest", "About $23,467"],
         ])
         + "<p>Two real-world conditions usually come with this. The business must support the payment "
         "from existing cash flow, and any excess land must actually be used by the business. Compare "
         "$23,467 a month, or about $281,600 a year, with the rent you'd stop paying. Remember that as "
         "owner you also take on taxes, insurance and repairs.</p>"),
        ("What to Expect After You Apply",
         "<ol>"
         "<li><strong>Gather three years of business and personal returns,</strong> plus year-to-date "
         "statements and your debt schedule.</li>"
         "<li><strong>Get the contract and property details.</strong> Lenders want the address, price and "
         "how much of the building you'll occupy.</li>"
         "<li><strong>Prequalify across lenders.</strong> Appetite for zero down varies widely.</li>"
         "<li><strong>Order third-party reports.</strong> Expect an appraisal and environmental review, "
         "which is important for shops with lifts, tanks or chemicals.</li>"
         "<li><strong>Close.</strong> SBA real estate deals usually take longer than a bank's. Plan for "
         "it in your purchase contract.</li>"
         "</ol>"
         '<p><a href="/match.html">Get matched with lenders</a>, or talk to an SBA specialist at (561) '
         "268-0465. Our related guides include "
         '<a href="/commercial-real-estate-loans/articles/100-percent-financing-owner-occupied-commercial-real-estate/">'
         "100% financing on owner-occupied real estate</a>, and "
         '<a href="/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/">buying a '
         "business with 5% down</a> if the business comes with it.</p>"),
    ],
    "faqs": [
        ("Can I buy my business's building with no money down?",
         "Sometimes. Some SBA 7(a) lenders finance up to 100% for an established business that occupies "
         "at least 51% of an existing building and has the cash flow to support the payment. Not every "
         "lender offers this."),
        ("Does the SBA require a down payment on commercial real estate?",
         "The SOP sets a 10% minimum for start-ups and changes of ownership. For an existing business "
         "buying its own building, the lender or SBA instead decides whether the equity position is "
         "acceptable, and many lenders set their own minimum."),
        ("Why does a start-up not qualify for 100%?",
         "A business that has operated for one year or less needs at least 10% equity on a 7(a) loan, "
         "based on total project cost. The same 10% minimum applies to a change of ownership, including "
         "real estate bought in that deal."),
        ("Can I rent out part of the building?",
         "Yes, up to 49% of an existing building, as long as your business permanently occupies and uses "
         "at least 51% of the rentable property."),
        ("How is 100% 7(a) different from an SBA 504 loan?",
         "A 504 generally needs at least 10% from you, and 15-20% in some cases, in exchange for a fixed "
         "rate on the SBA portion. A 7(a) can reach 100% with some lenders, usually on an adjustable rate."),
        ("Are there businesses that can't get this?",
         "Investors buying rental property aren't eligible. Many lenders also exclude gas stations, "
         "restaurants and bars, vape shops, delivery routes and fleet-heavy companies, though lenders differ."),
    ],
    "related": [
        ("/sba-loans.html", "SBA loans"),
        ("/sba-loans/articles/sba-loan-owner-occupied-commercial-property/", "SBA 7(a) vs 504 for your building"),
        ("/commercial-real-estate-loans/articles/100-percent-financing-owner-occupied-commercial-real-estate/", "100% owner-occupied financing"),
        ("/hotel-financing.html", "Hotel financing"),
        ("/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/", "Buying a business with 5% down"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, OCC, FEES, SBA_7A, SBA_504, EQ],
}, {
    "slug": "hotel-financing",
    "root_file": "hotel-financing.html",
    "crumb": "Hotel Financing",
    "title": "Hotel Financing: SBA Loans, PIPs and Flags | Axiant",
    "og_title": "Hotel Financing: SBA Loans for Buying a Hotel and Paying for a PIP",
    "h1": "Hotel Financing: SBA Loans for Buying a Hotel and Paying for a PIP",
    "headline": "Hotel Financing: SBA Loans for Buying a Hotel and Paying for a PIP",
    "lede": "How SBA 7(a) and 504 work for flagged and strong independent hotels, how a property "
            "improvement plan gets financed, and what lenders want from a buyer",
    "meta_desc": "Hotel financing with SBA 7(a) or 504: the 50% transient revenue rule, 10-20% equity, PIP and flag conversion funding, buyer experience, and a worked example.",
    "article_desc": "How buyers finance flagged and independent hotels using SBA loans, "
                    "including PIP costs, flag conversions and SBA eligibility rules.",
    "keywords": "hotel financing, sba loan to buy a hotel, hotel pip financing, property improvement "
                "plan loan, flag conversion financing, motel financing",
    "quick_answer": "Hotels can qualify for SBA 7(a) or 504 loans if over <strong>50%</strong> of revenue "
                    "comes from guests staying 30 days or less. Buyers commonly put in about "
                    "<strong>15%</strong>, though SBA minimums run from <strong>10%</strong> on a 7(a) "
                    "acquisition to 15-20% on a 504. Lenders typically want hotel experience and can "
                    "often include PIP costs. Axiant Partners, a broker in Boca Raton, can find lenders "
                    "for hotels. These are typical ranges, not a quote.",
    "sections": [
        ("Is a Hotel Eligible for an SBA Loan?",
         f"<p>{_SOP_A} treats hotels and motels as eligible if more than 50% of the prior year's revenue "
         "comes from transients who stay 30 days or less at a time, and the business complies with zoning "
         "and other legal requirements. A start-up's projections must show the same. That test catches "
         "extended-stay properties and buildings that have drifted into monthly rentals, so check your "
         "numbers early.</p>"
         "<p>A hotel run by an outside management company adds a question: lenders must make sure a "
         "management agreement doesn't make the applicant an ineligible passive business, unless the "
         "agreement is part of the franchise documents for a brand on the SBA's Franchise Directory.</p>"),
        ("SBA 7(a), SBA 504 and Other Options Compared",
         table(["", "SBA 7(a)", "SBA 504", "CMBS or bank"], [
             ["Minimum equity", "10% on a change of ownership", "15%, or 20% with a new business", "Commonly 25-30%"],
             ["Maximum term", "Up to 25 years if 85%+ of costs are real estate", "10, 20 or 25 years", "Often 5-10 years"],
             ["Loan limit", "$5 million", "Depends on project and debenture limits", "Lender limit"],
             ["Covers goodwill or PIP", "Often both", "Fixed assets, not working capital", "Case by case"],
             ["Best for", "Smaller flagged or strong independent deals", "Fixed-rate real estate with more equity", "Larger stabilized hotels"],
         ])
         + "<p>The SBA lists hotels and other lodging as limited or special purpose property, which is why "
         "the 504 needs at least 15%, rising to 20% if the project also involves a new business. On a "
         "7(a), lenders may allow up to about 85% loan to value and often set their own higher equity "
         "for hotels. For a deeper comparison of larger structures, see "
         '<a href="/commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/">SBA vs '
         "CMBS vs conventional hotel loans</a>. Figures are SBA rules or typical ranges, not a quote.</p>"),
        ("Financing a PIP or a Flag Conversion",
         "<p>A <strong>property improvement plan</strong> is the brand's list of required upgrades, usually "
         "triggered by a sale, a new franchise agreement or a change of flag. It can cover rooms, "
         "lobbies, signs and systems, and it has a deadline. Lenders read it closely because it changes "
         "both the cost and the time before the hotel stabilizes.</p>"
         "<ul>"
         "<li><strong>Get the PIP before pricing the deal.</strong> The brand generally issues it after an "
         "inspection. The buyer's budget should use real contractor quotes.</li>"
         "<li><strong>Include it in the project.</strong> SBA renovation proceeds can be part of the "
         "total. That raises the project cost, so your equity requirement rises with it.</li>"
         "<li><strong>Watch the timing.</strong> The SOP allows an additional period for construction or "
         "renovation on a real estate loan, but brands set their own completion dates.</li>"
         "<li><strong>Flag conversions.</strong> Moving to a new brand can support a higher room rate, but "
         "lenders want to see the franchise approval, conversion PIP and fees. A conversion is "
         "underwritten as a renovation of an existing hotel, and it's different from a new build.</li>"
         "</ul>"
         "<p>Many lenders won't finance ground-up hotel construction through these programs, so a new "
         'build is usually a different conversation. See <a href="/commercial-bridge-loans.html">bridge '
         "loans</a> if a property needs repositioning before it can qualify.</p>"),
        ("What Lenders Want From a Buyer",
         "<p>Hotels are a management business. Appendix 15 requires the lender to describe your industry "
         "experience and management team, including how daily operations will be run. Beyond that, these "
         "are common lender practices:</p>"
         "<ul>"
         "<li><strong>Hotel experience.</strong> Prior ownership or general manager time is often expected. "
         "If you lack it, a strong GM or a brand-approved manager can help.</li>"
         "<li><strong>Brand strength.</strong> Flagged hotels and strong independents are easier to place "
         "than properties with weak history.</li>"
         "<li><strong>Historical numbers.</strong> Lenders review recent financials, occupancy, room rate "
         "and revenue per available room, often with STR reports.</li>"
         "<li><strong>Coverage.</strong> The SOP's test is 1.25 to 1 for a first acquisition, and lenders "
         "may want more. A business valuation is required for a change of ownership.</li>"
         "<li><strong>Credit and reserves.</strong> Many SBA lenders look for roughly 650-680 or higher, "
         "plus cash beyond the down payment.</li>"
         "</ul>"
         "<p>Two rules help hotel buyers. On an owner-occupied special purpose purchase, the lender may rely "
         "on projections rather than history if the appraised value fully collateralizes the loan, and "
         "no Quality of Earnings report is required. Lenders may still be stricter than that.</p>"),
        ("Worked Example: Buying a Flagged Hotel With a PIP",
         "<p><strong>Illustrative numbers, not a quote.</strong> An experienced operator buys a 70-room "
         "limited-service hotel for $3,400,000, with a $500,000 PIP and about $60,000 in closing costs. "
         f"The estimated guaranty fee, from the {_FEE_A}, adds about $94,430.</p>"
         + table(["Item", "Amount"], [
             ["Total project cost", "About $4,054,430"],
             ["Buyer's equity (15%, above the 10% SBA minimum)", "About $608,160"],
             ["SBA 7(a) loan (85%)", "About $3,446,260"],
             ["Assumed rate and term", "8.25%, 25 years"],
             ["Monthly principal and interest", "About $27,170"],
             ["Annual debt service", "About $326,070"],
             ["Cash flow needed at 1.25 to 1", "About $407,580 a year"],
         ])
         + "<p>That $407,580 needs to come from the hotel's actual performance after management fees and "
         "reserves, so don't count on the post-PIP room rate. The 25-year term applies only if the "
         "lender treats it as a special purpose purchase with at least 85% of total project costs in real "
         "estate; goodwill-heavy deals can have a shorter blended term and a higher payment.</p>"),
        ("Steps to Get a Hotel Deal Funded",
         "<ol>"
         "<li><strong>Test the transient rule.</strong> Pull the revenue split for last year.</li>"
         "<li><strong>Collect the data.</strong> Three years of financials, STR reports, franchise "
         "agreement and any existing PIP.</li>"
         "<li><strong>Ask the brand early.</strong> Learn what a sale triggers before you make an offer.</li>"
         "<li><strong>Write a management plan.</strong> Name who runs the property day to day.</li>"
         "<li><strong>Talk to several lenders.</strong> Hotel appetite varies a lot, and many banks don't "
         "lend on them at all.</li>"
         "</ol>"
         '<p><a href="/match.html">Get matched with hotel lenders</a>, or talk to an SBA specialist at (561) '
         "268-0465. If you already run a hotel and want to buy a second, read "
         '<a href="/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/">how SBA equity '
         'rules work on a purchase</a>. For the wider SBA picture, see <a href="/sba-loans.html">SBA loans</a> '
         'and <a href="/sba-100-percent-financing.html">100% financing for other owner-occupied buildings</a>.</p>'),
    ],
    "faqs": [
        ("Can you use an SBA loan to buy a hotel?",
         "Yes, if more than 50% of the hotel's prior-year revenue comes from guests staying 30 days or "
         "less and it meets zoning and other legal requirements. 7(a) and 504 are both used, and lender "
         "appetite varies."),
        ("How much down do I need to buy a hotel with an SBA loan?",
         "A 7(a) change of ownership has a 10% SBA minimum, and lenders commonly want about 15% or more "
         "on hotels. A 504 needs at least 15% for this property type, or 20% if the project includes a new "
         "business."),
        ("Can an SBA loan pay for a PIP?",
         "Often. Renovation costs can be part of the project, including a PIP tied to a purchase, as long "
         "as the lender is comfortable with the budget and schedule. The extra cost also raises required equity."),
        ("Do I need hotel experience to get a loan?",
         "It isn't a stated percentage in SBA rules, but lenders must document your industry experience "
         "and management, and many expect prior hotel ownership or a strong general manager."),
        ("Can I use an SBA loan to build a new hotel?",
         "SBA rules address new construction, but many lenders avoid ground-up hotels because there's no "
         "operating history. Expect a harder search and much more equity."),
        ("What is a flag conversion?",
         "It's a change from one hotel brand to another, or from independent to branded. It usually comes "
         "with a new franchise agreement and a PIP, both of which lenders will review."),
    ],
    "related": [
        ("/sba-loans.html", "SBA loans"),
        ("/commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/", "SBA vs CMBS vs conventional"),
        ("/sba-100-percent-financing.html", "100% SBA financing"),
        ("/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/", "Buying a business with 5% down"),
        ("/commercial-bridge-loans.html", "Commercial bridge loans"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, FEES, SBA_7A, SBA_504, EQ],
}]
