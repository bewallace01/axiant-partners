# -*- coding: utf-8 -*-
"""Vending machine financing - 4 articles. Money-page cluster (AEO plan 2a).

Validated 2026-10-22 against Bing AI Mode: "how to finance vending machines" cited a
machine supplier and consumer pay-later checkouts, no business-finance specialist.

The older spoke at equipment-financing/articles/vending-machine-financing/ earns
non-brand Google clicks, so it stays where it is (machine costs and route expansion)
and the pillar links to it. These four answer the questions it does not: what the
financing costs, lease vs loan vs a pay-later checkout, micro-markets, and buying an
existing route.

Ranges are described as conventional across lenders, never quoted as anyone's terms,
and match what the site already publishes: equipment financing at 7-22% APR by
credit tier, used equipment +1-3 points, sub-$50K tickets a little dearer than large
ones (typical-equipment-financing-rates-2026); machine costs, 24-60 month terms and
10-20% down for newer operators (the vending spoke). Every payment figure is
arithmetic on a stated illustrative rate. No funded totals, no testimonials, no
named-lender rates. One entity: Axiant Partners, (561) 268-0465, Boca Raton.
Business-purpose only.
"""

CLUSTER = {
    "pillar": "vending-machine-financing.html",
    "hub": "vending-machine-financing/articles",
    "crumb": "Vending Machine Financing",
    "cta_inline": "Get matched for vending machine financing",
    "cta_button": "Get Matched for Vending Financing",
    "hub_title": "Vending Machine Financing Guides | Axiant Partners",
    "hub_h1": "Vending Machine Financing Articles",
    "hub_lede": "What vending financing costs, how to structure it, and how operators "
                "fund micro-markets and buy existing routes",
    "hub_desc": "Guides for vending operators: typical financing rates and terms, lease "
                "vs loan vs pay-later checkout, micro-market financing, and financing "
                "the purchase of an existing vending route.",
    "hub_intro": "Vending is financed one placement at a time, and the placement - not "
                 "the machine - is what most lenders are really underwriting. Start "
                 "with <a href=\"/vending-machine-financing.html\">vending machine "
                 "financing</a>, or see <a href=\"/equipment-financing/articles/vending-machine-financing/\">"
                 "machine costs and route expansion</a>.",
    "hub_cta_h2": "Adding machines or buying a route?",
    "hub_cta_p": "Send the machines, the placements and the cost. We will bring back "
                 "real terms, and checking won't affect your credit.",
}

FTC = ("https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic",
       "FTC: Protecting Small Businesses Seeking Financing",
       "The FTC's guidance on misrepresented financing costs and terms aimed at small "
       "businesses - the reason to compare total of payments, not the advertised payment.")
TILA_EXEMPT = ("https://www.ecfr.gov/current/title-12/chapter-X/part-1026/subpart-A/section-1026.3",
               "12 CFR 1026.3: Exempt Transactions (Truth in Lending)",
               "Credit for a business purpose is exempt from federal Truth in Lending "
               "disclosures, so a business financing offer may not show an APR unless "
               "you ask.")
IRS_946 = ("https://www.irs.gov/publications/p946",
           "IRS Publication 946: How To Depreciate Property",
           "Section 179 and depreciation rules for business equipment, including "
           "financed machines and how leases are treated.")
IRS_8594 = ("https://www.irs.gov/forms-pubs/about-form-8594",
            "IRS Form 8594: Asset Acquisition Statement",
            "How buyer and seller of a business allocate the price between equipment, "
            "goodwill and other assets - which decides what can be depreciated.")
UCC_9310 = ("https://www.law.cornell.edu/ucc/9/9-310",
            "UCC &sect; 9-310: When Filing Is Required to Perfect a Security Interest",
            "Vending machines carry no title; a lender records its lien by filing a "
            "UCC-1, which is what a lien search on a route turns up.")
SBA_SOP = ("https://www.sba.gov/document/sop-50-10-lender-development-company-loan-programs",
           "SBA SOP 50 10: Lender and Development Company Loan Programs",
           "SBA's operating rules for 7(a) loans, including the equity injection required "
           "when buying a business and when a seller note can count toward it.")
FDA_VEND = ("https://www.ecfr.gov/current/title-21/chapter-I/subchapter-B/part-101/subpart-A/section-101.8",
            "21 CFR 101.8: Vending Machines (FDA calorie labeling)",
            "Calorie disclosure required of operators who own or operate 20 or more "
            "food vending machines.")
PCI = ("https://www.pcisecuritystandards.org/",
       "PCI Security Standards Council",
       "The card-data security standard that applies to cashless readers and "
       "self-checkout kiosks.")


def _table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join(
        "<tr>" + "".join(f'<td data-label="{head[i]}">{c}</td>' for i, c in enumerate(r)) + "</tr>"
        for r in rows)
    return (f'<div class="table-wrap"><table style="width:100%"><thead><tr>{th}</tr></thead>'
            f"<tbody>{body}</tbody></table></div>")


ARTICLES = [
    # ------------------------------------------------------------------ 1
    {
        "slug": "typical-vending-machine-financing-rates-2026",
        "crumb": "Typical Rates and Terms 2026",
        "title": "Vending Machine Financing Rates and Terms 2026 | Axiant",
        "og_title": "Typical Vending Machine Financing Rates and Terms (2026)",
        "h1": "Typical Vending Machine Financing Rates and Terms (2026)",
        "headline": "Typical Vending Machine Financing Rates and Terms in 2026",
        "lede": "What vending machine loans and leases commonly cost by credit tier, what "
                "moves the price for a vending operator, and what the payments look like",
        "meta_desc": "Vending machine financing commonly runs 7-22% APR by credit tier, "
                     "over 24-60 months. What moves the price for vending operators, and "
                     "payments on $10K-$50K.",
        "article_desc": "Typical rates, terms and down payments for vending machine "
                        "financing in 2026, and the vending-specific factors behind them.",
        "keywords": "vending machine financing rates, vending machine loan interest rate, "
                    "vending machine lease rates, vending financing terms 2026",
        "quick_answer": "Vending machines are financed as small-ticket equipment, so "
                        "rates follow the same credit tiers: roughly <strong>7-9% APR</strong> "
                        "for strong credit and two-plus years in business, "
                        "<strong>10-16%</strong> in the middle, and up to "
                        "<strong>22%</strong> with specialty lenders. Terms commonly run "
                        "<strong>24-60 months</strong>. Axiant Partners, a business-loan "
                        "broker in Boca Raton, sees signed placements and refurbished-unit "
                        "age move vending pricing more than the machine brand does.",
        "sections": [
            ("Rates by Credit Tier",
             "<p>There is no separate rate sheet for vending. Lenders price a vending "
             "machine the way they price any small-ticket equipment, and the biggest "
             "lever is the borrower's credit tier. These are the ranges commonly seen "
             "across lenders, the same ones on our "
             "<a href=\"/equipment-financing/articles/typical-equipment-financing-rates-2026/\">"
             "typical equipment financing rates</a> page:</p>"
             + _table(["Credit tier", "Typical APR", "Typical term", "Down payment"], [
                 ["720+, 2+ yrs in business", "7-9%", "Up to 60 mo", "0-10%"],
                 ["680-719", "10-13%", "36-60 mo", "0-10%"],
                 ["640-679", "13-16%", "36-60 mo", "10-20%"],
                 ["580-639", "16-22%", "24-48 mo", "15-25%"],
                 ["Below 580", "Limited programs", "24-36 mo", "20%+"],
             ])
             + "<p>Typical ranges, not a quote. Vending terms usually stop around 60 "
             "months because that is roughly the working life lenders give a machine "
             "in a public placement; a longer term on a used unit is rare.</p>"),
            ("What Moves the Price for a Vending Operator",
             "<p>Within a tier, these are the things that push a vending deal up or "
             "down:</p>"
             "<ul>"
             "<li><strong>Ticket size.</strong> Most vending deals are under $50,000, "
             "and small tickets tend to price about half a point to a point above large "
             "ones, because the cost of underwriting does not shrink with the loan.</li>"
             "<li><strong>New or refurbished.</strong> Refurbished machines are normal in "
             "vending and finance fine, but older or used units commonly add one to three "
             "points. See <a href=\"/equipment-financing/articles/can-you-finance-used-equipment/\">"
             "financing used equipment</a>.</li>"
             "<li><strong>Signed placements.</strong> A location agreement with an "
             "office, gym, school or plant shows where the machine will earn. Lenders "
             "treat it as evidence the payment will be covered, and it matters most for "
             "newer operators.</li>"
             "<li><strong>Sales data.</strong> Operators with telemetry or card-reader "
             "reports can show sales per machine per location. That is the closest thing "
             "vending has to an income statement for a single asset.</li>"
             "<li><strong>Time in business.</strong> Under two years usually means a "
             "larger down payment rather than a decline, especially with placements in "
             "hand.</li>"
             "</ul>"),
            ("What the Payments Look Like",
             "<p>Monthly payments on a 48-month loan at three illustrative rates, one "
             "from each part of the range - $10,000 is one or two machines, $30,000 a "
             "small batch, $50,000 a large micro-market. Arithmetic, not a quote; fees are not "
             "included:</p>"
             + _table(["Amount financed", "At 9%", "At 13%", "At 18%"], [
                 ["$10,000", "$249", "$268", "$294"],
                 ["$30,000", "$747", "$805", "$881"],
                 ["$50,000", "$1,244", "$1,341", "$1,469"],
             ])
             + "<p>The useful way to read the table is per machine. Eight machines on "
             "$30,000 at 13% cost about $100 a month each. If a placement cannot clear "
             "that after product cost and the location's commission, the problem is the "
             "placement, not the rate.</p>"),
            ("Ask for the APR and the Total of Payments",
             "<p>Federal Truth in Lending disclosures do not apply to business-purpose "
             "credit, so a vending financing offer can arrive with a monthly payment and "
             "a term but no APR. Ask for three numbers on every offer:</p>"
             "<ol>"
             "<li><strong>The APR</strong>, or the rate and every fee, so you can work "
             "it out.</li>"
             "<li><strong>The total of payments</strong> over the full term, plus any "
             "buyout at the end.</li>"
             "<li><strong>What happens if you pay early</strong> - whether the interest "
             "is reduced or the full amount is still owed.</li>"
             "</ol>"
             "<p>That is especially important with the pay-later and lease-to-own offers "
             "that appear at checkout on machine suppliers' sites. They can be quick and "
             "convenient, but a small monthly figure over a long term can cost more in "
             "total than an equipment loan. Our guide on "
             "<a href=\"/articles/how-to-compare-business-loan-offers/\">comparing "
             "business loan offers</a> shows the method.</p>"),
            ("How to Get Into a Better Tier",
             "<ul>"
             "<li><strong>Bring placements, not just a quote for machines.</strong> A "
             "signed site agreement does more for a newer operator than a larger order.</li>"
             "<li><strong>Show your sales.</strong> Telemetry exports, card-processor "
             "statements and bank deposits that match them.</li>"
             "<li><strong>Batch purchases.</strong> One package for several machines "
             "can price better than several single-machine deals.</li>"
             "<li><strong>Put more down on older units.</strong> It narrows the gap "
             "between price and resale value that lenders charge for.</li>"
             "</ul>"
             "<p>Whether to lease or borrow is a separate decision with its own costs: "
             "see <a href=\"../vending-machine-lease-vs-loan/\">vending machine lease vs "
             "loan</a>.</p>"),
        ],
        "faqs": [
            ("What interest rate can I get on a vending machine loan?",
             "It follows your credit tier. Ranges commonly seen across lenders run "
             "roughly 7-9% APR for strong credit and two-plus years in business, 10-16% "
             "for mid-tier credit, and up to about 22% with specialty lenders for weaker "
             "files. These are typical ranges, not a quote."),
            ("How long can I finance vending machines for?",
             "Commonly 24 to 60 months, matched to the working life of the machines. "
             "Used and refurbished units usually get the shorter end."),
            ("Do I need a down payment?",
             "Strong-credit operators with established placements can sometimes finance "
             "with little or nothing down. Newer operators and refurbished machines "
             "commonly need 10-20% down."),
            ("Are refurbished vending machines more expensive to finance?",
             "Usually somewhat. Used and refurbished equipment commonly prices one to "
             "three points above new, reflecting the shorter remaining life. The lower "
             "purchase price often more than makes up for it."),
            ("Why doesn't my financing offer show an APR?",
             "Federal Truth in Lending disclosures do not apply to business-purpose "
             "credit, so an offer may show only a payment and a term. Ask for the APR "
             "and the total of payments before you sign."),
        ],
        "related": [
            ("/vending-machine-financing.html", "Vending machine financing"),
            ("../vending-machine-lease-vs-loan/", "Vending machine lease vs loan vs pay-later"),
            ("/equipment-financing/articles/typical-equipment-financing-rates-2026/", "Typical equipment financing rates 2026"),
            ("/equipment-financing/articles/vending-machine-financing/", "Vending machine costs and route expansion"),
        ],
        "sources": [TILA_EXEMPT, FTC, IRS_946],
    },
    # ------------------------------------------------------------------ 2
    {
        "slug": "vending-machine-lease-vs-loan",
        "crumb": "Lease vs Loan vs Pay-Later",
        "title": "Vending Machine Lease vs Loan vs Pay-Later | Axiant",
        "og_title": "Vending Machine Lease vs Loan vs Pay-Later Checkout",
        "h1": "Vending Machine Lease vs Loan vs Pay-Later Checkout",
        "headline": "Vending Machine Lease vs Loan vs Pay-Later Checkout",
        "lede": "Four ways to pay for vending machines over time, what each one really "
                "costs, and which fits a route that moves machines between locations",
        "meta_desc": "Equipment loan, $1-buyout lease, FMV lease or a pay-later offer at "
                     "checkout: how each works for vending machines, what to compare, "
                     "and when each fits.",
        "article_desc": "A comparison of loans, leases and pay-later checkout offers for "
                        "vending machines, with the vending-specific reasons to pick each.",
        "keywords": "vending machine lease vs buy, lease vending machines, vending "
                    "machine lease to own, vending machine pay later financing",
        "quick_answer": "Buy with an <strong>equipment loan or $1-buyout lease</strong> "
                        "for machines you will keep in stable placements; use an "
                        "<strong>FMV lease</strong> when you want to return or upgrade "
                        "units that underperform. <strong>Pay-later and lease-to-own "
                        "offers at checkout</strong> are fast but often cost the most in "
                        "total. Axiant Partners, a business-loan broker in Boca Raton, "
                        "suggests comparing every option on total of payments plus "
                        "buyout, not the monthly figure.",
        "sections": [
            ("The Four Options Side by Side",
             _table(["Option", "Who owns it", "End of term", "Fits best"], [
                 ["Equipment loan", "You, from day one (lender holds a lien)", "Lien released", "Machines you will keep"],
                 ["$1-buyout lease", "Lessor until the $1 buyout", "You own it", "Buying, with lease paperwork"],
                 ["FMV lease", "Lessor", "Return, renew or buy at market value", "Units you may swap"],
                 ["Pay-later at checkout", "Depends on the contract", "Read the contract", "Small, urgent purchases"],
             ])
             + "<p>The first two are both, in substance, ways of buying the machine. The "
             "third is renting it. The fourth can be either, and the paperwork - not the "
             "checkout button - decides which.</p>"),
            ("Why Vending Is Different From Most Equipment",
             "<p>Most equipment stays where it is installed. Vending machines move. A "
             "machine that underperforms in one break room gets pulled and placed "
             "somewhere else, and a lost contract can leave several units in your "
             "warehouse at once. That changes the lease-or-buy decision in two ways:</p>"
             "<ul>"
             "<li><strong>Owning gives you freedom to redeploy</strong> without asking "
             "anyone. With a loan, you can move a machine anywhere, sell it or "
             "cannibalise it for parts once paid off.</li>"
             "<li><strong>An FMV lease gives you a way out</strong> of a model you no "
             "longer want - an older cash-only unit when your locations want card "
             "readers, for example - without having to sell it yourself.</li>"
             "</ul>"
             "<p>Check the location clause in any lease. Some restrict where the "
             "equipment can be kept or require notice before it moves, which can be a "
             "problem for a route operator.</p>"),
            ("Pay-Later and Lease-to-Own at Checkout",
             "<p>Machine suppliers' websites increasingly offer instant pay-later or "
             "lease-to-own approval at checkout. For a single machine needed this week, "
             "the speed is real. The things to check before you click:</p>"
             "<ul>"
             "<li><strong>Is it a loan or a lease?</strong> A lease-to-own contract "
             "usually means you do not own the machine until the final payment or a "
             "buyout.</li>"
             "<li><strong>Total of payments.</strong> Multiply the payment by the number "
             "of payments and add any buyout. Compare that with the cash price.</li>"
             "<li><strong>Personal or business?</strong> Some checkout products are "
             "consumer credit. Business equipment belongs on business credit.</li>"
             "<li><strong>Early payoff.</strong> Whether paying it off early saves "
             "anything.</li>"
             "</ul>"
             "<p>None of this makes checkout financing wrong. It makes it something to "
             "price against an equipment loan rather than accept by default.</p>"),
            ("A Worked Comparison",
             "<p>Illustrative arithmetic for an $8,000 smart machine with a card "
             "reader:</p>"
             + _table(["", "Equipment loan", "Any lease or pay-later offer"], [
                 ["Monthly payment", "$210.67 at 12% over 48 months", "From the offer"],
                 ["Number of payments", "48", "From the offer"],
                 ["Total of payments", "$10,112", "Payment &times; number of payments"],
                 ["End-of-term cost", "$0, you own it", "Buyout, if any"],
                 ["Total cost of the machine", "$10,112", "Total of payments + buyout"],
             ])
             + "<p>Lay every offer out this way. The cheapest option is the one with the "
             "lowest bottom line for the outcome you want - ownership or flexibility - "
             "not the lowest monthly figure.</p>"),
            ("Taxes: Who Gets the Deduction",
             "<p>With a loan or a $1-buyout lease, you are generally treated as the "
             "owner, so you depreciate the machine and may be able to use Section 179 in "
             "the year it is placed in service; financed equipment qualifies the same as "
             "equipment bought with cash. With a true FMV lease, the lessor owns it and "
             "your lease payments are generally deductible as a business expense "
             "instead.</p>"
             "<p>Which treatment is better depends on your tax position that year. IRS "
             "Publication 946 sets out the rules; confirm with your accountant before "
             "you choose a structure for tax reasons.</p>"),
            ("Which One to Pick",
             "<ul>"
             "<li><strong>Stable placements, long life ahead:</strong> equipment loan.</li>"
             "<li><strong>Want to own, lessor offers better terms:</strong> $1-buyout lease.</li>"
             "<li><strong>Testing new locations or new machine types:</strong> FMV lease.</li>"
             "<li><strong>One machine, needed now, small amount:</strong> checkout offer, "
             "after comparing total cost.</li>"
             "</ul>"
             "<p>For what each structure typically costs, see "
             "<a href=\"../typical-vending-machine-financing-rates-2026/\">typical "
             "vending machine financing rates</a>. The general comparison for all "
             "equipment is in <a href=\"/equipment-financing/articles/equipment-leasing-vs-loan-which-is-better/\">"
             "equipment leasing vs loan</a>.</p>"),
        ],
        "faqs": [
            ("Is it better to lease or buy vending machines?",
             "Buy, with a loan or a $1-buyout lease, for machines you will keep in "
             "stable locations. Use an FMV lease when you want the option to return or "
             "upgrade machines that underperform. Compare every option on total of "
             "payments plus buyout."),
            ("What is lease-to-own for vending machines?",
             "A lease where you make payments over a term and own the machine after the "
             "final payment or a buyout. Until then the lessor owns it. Check the total "
             "of payments and the buyout before signing."),
            ("Are pay-later offers at checkout a good way to buy vending machines?",
             "They are fast and can suit a single, urgent purchase. They can also cost "
             "more in total than an equipment loan, so compare the total of payments "
             "with the cash price and with a loan offer first."),
            ("Can I move a leased vending machine to a new location?",
             "Usually, but check the lease. Some leases restrict where equipment can be "
             "kept or require notice before it is moved."),
            ("Can I take Section 179 on financed vending machines?",
             "Generally yes, if you are treated as the owner - a loan or $1-buyout lease "
             "- and the machine is placed in service that year. With a true FMV lease the "
             "lessor owns the machine. Confirm with your accountant."),
        ],
        "related": [
            ("/vending-machine-financing.html", "Vending machine financing"),
            ("../typical-vending-machine-financing-rates-2026/", "Typical vending machine financing rates 2026"),
            ("/equipment-financing/articles/equipment-leasing-vs-loan-which-is-better/", "Equipment leasing vs loan"),
            ("/match.html", "Get matched"),
        ],
        "sources": [FTC, IRS_946, TILA_EXEMPT],
    },
    # ------------------------------------------------------------------ 3
    {
        "slug": "micro-market-financing",
        "crumb": "Micro-Market Financing",
        "title": "Micro-Market Financing for Vending Operators | Axiant",
        "og_title": "How to Finance a Micro-Market",
        "h1": "How to Finance a Micro-Market",
        "headline": "How Vending Operators Finance a Micro-Market",
        "lede": "What goes into a micro-market, why it is financed as one package, and "
                "what lenders want to see about the host location",
        "meta_desc": "A micro-market setup commonly runs $15K-$50K. How operators finance "
                     "kiosks, coolers and shelving as one package, and why the host "
                     "agreement matters most.",
        "article_desc": "How vending operators finance micro-markets, and the host-site "
                        "factors lenders weigh.",
        "keywords": "micro market financing, finance micro market kiosk, micro market "
                    "equipment loan, unattended retail financing",
        "quick_answer": "A micro-market - open shelving, coolers and a self-checkout "
                        "kiosk in a workplace - commonly costs <strong>$15,000-$50,000</strong> "
                        "to set up and is financed as one equipment package over "
                        "<strong>36-60 months</strong>. Axiant Partners, a business-loan "
                        "broker in Boca Raton, finds the <strong>host agreement</strong> "
                        "weighs as much as credit: lenders want its term to cover the "
                        "loan's.",
        "sections": [
            ("What You Are Financing",
             "<p>A micro-market is a small, unattended store inside a workplace: "
             "customers pick products off open shelves and out of coolers and pay at a "
             "kiosk. The setup is a package of equipment, and lenders finance it as "
             "one:</p>"
             + _table(["Component", "What drives the cost"], [
                 ["Self-checkout kiosk", "Number of kiosks, card and mobile pay, software"],
                 ["Coolers and freezers", "Count and size; fresh food needs more"],
                 ["Shelving and fixtures", "Store size and finish"],
                 ["Security cameras", "Coverage the platform or host requires"],
                 ["Installation", "Electrical and network work at the site"],
             ])
             + "<p>The software subscription is usually a running cost, not part of the "
             "financed package. Ask the platform provider which parts of their quote are "
             "equipment and which are service.</p>"),
            ("The Host Agreement Is the Collateral That Matters",
             "<p>A cooler or kiosk has some resale value, but a lender knows that much "
             "of a micro-market's cost - installation, fixtures, custom shelving - "
             "recovers little if the market is pulled. What actually pays the loan is "
             "the location. So lenders look hard at the agreement with the host:</p>"
             "<ul>"
             "<li><strong>Term.</strong> A host agreement that runs at least as long as "
             "the financing is the strongest position. A month-to-month arrangement "
             "means the location can end before the loan does.</li>"
             "<li><strong>Exclusivity.</strong> Whether you are the only food provider "
             "in the space.</li>"
             "<li><strong>Termination and removal.</strong> How much notice the host "
             "must give, and whether you can recover the equipment.</li>"
             "<li><strong>Commission.</strong> What share of sales goes to the host, "
             "which comes straight out of the margin that covers the payment.</li>"
             "</ul>"),
            ("Which Sites Support a Micro-Market",
             "<p>Operators generally look for a closed, secure workplace with a large, "
             "steady employee population and long shifts: plants, warehouses, "
             "hospitals, large offices. Platform providers usually publish their own "
             "minimums. The site question matters to a lender for one reason - shrink. "
             "An open honor-system store in a location with public access loses more "
             "product, and the loss comes out of the margin that pays the loan.</p>"
             "<p>Kiosks take card and mobile payments, so they fall under the card "
             "industry's PCI data-security standard. Reputable platforms handle that "
             "for you; it is worth confirming before you sign.</p>"),
            ("A Worked Example",
             "<p>Illustrative arithmetic, not a quote. An operator with an existing "
             "vending route adds a micro-market - kiosk, coolers, shelving and cameras - "
             "at a 300-person distribution center under a five-year host agreement:</p>"
             + _table(["Item", "Figure"], [
                 ["Equipment package", "$36,000"],
                 ["Term", "60 months"],
                 ["Illustrative rate", "13% APR"],
                 ["Monthly payment", "About $819"],
                 ["Total of payments", "About $49,147"],
             ])
             + "<p>The test is whether the market's monthly gross margin, after product "
             "cost, the host's commission, the software fee and shrink, clears $819 with "
             "room to spare. The five-year host agreement is what lets a lender offer "
             "the full 60 months.</p>"),
            ("When Financing a Micro-Market Is the Wrong Move",
             "<ul>"
             "<li><strong>The host will not sign a term.</strong> Without one, you are "
             "carrying five years of payments on a location that can end next month.</li>"
             "<li><strong>The site is open to the public.</strong> Shrink can erase the "
             "margin; traditional machines may fit better.</li>"
             "<li><strong>The headcount is marginal.</strong> A few well-placed machines "
             "may earn more per dollar of equipment.</li>"
             "</ul>"
             "<p>For machine-by-machine costs, see <a href=\"/equipment-financing/articles/vending-machine-financing/\">"
             "vending machine costs and route expansion</a>. For what the financing "
             "costs, see <a href=\"../typical-vending-machine-financing-rates-2026/\">"
             "typical vending machine financing rates</a>.</p>"),
            ("What to Bring to the Lender",
             "<ul>"
             "<li><strong>The platform quote</strong>, split into equipment, installation "
             "and monthly service.</li>"
             "<li><strong>The signed host agreement</strong>, or a draft with the term, "
             "exclusivity, removal and commission spelled out.</li>"
             "<li><strong>The site's headcount and shifts</strong>, and whether the space "
             "is closed to the public.</li>"
             "<li><strong>Sales from your current machines</strong>, if you run a route "
             "now - telemetry or card-processor reports and matching bank deposits.</li>"
             "<li><strong>Recent business bank statements</strong>, typically three to "
             "six months.</li>"
             "</ul>"
             "<p>Operators adding a micro-market to an established route usually have "
             "the easiest time, because their existing placements show how they run a "
             "location. If you are buying a route that already includes micro-markets, "
             "see <a href=\"../buying-a-vending-route/\">financing a route purchase</a>.</p>"),
        ],
        "faqs": [
            ("How much does a micro-market cost?",
             "Setups commonly run about $15,000 to $50,000, depending on the number of "
             "kiosks and coolers, fresh food, fixtures and installation. These are "
             "typical ranges, not a quote."),
            ("Can you finance a micro-market?",
             "Yes. The kiosk, coolers, shelving and cameras are usually financed together "
             "as one equipment package, often over 36 to 60 months."),
            ("What do lenders want to see for micro-market financing?",
             "The host agreement above all: its term, exclusivity, termination notice "
             "and commission. Then the usual items - credit, time in business and, for "
             "existing operators, sales from current locations."),
            ("Is the software subscription included in the financing?",
             "Usually not. The platform's monthly fee is normally a running cost. Ask "
             "the provider to separate equipment from service in its quote."),
            ("Can a new vending operator finance a micro-market?",
             "It is harder than financing a few machines, because the package is larger. "
             "A signed multi-year host agreement and a larger down payment help most."),
        ],
        "related": [
            ("/vending-machine-financing.html", "Vending machine financing"),
            ("../buying-a-vending-route/", "Financing the purchase of a vending route"),
            ("/equipment-financing/articles/vending-machine-financing/", "Vending machine costs and route expansion"),
            ("/match.html", "Get matched"),
        ],
        "sources": [PCI, UCC_9310, IRS_946],
    },
    # ------------------------------------------------------------------ 4
    {
        "slug": "buying-a-vending-route",
        "crumb": "Buying a Vending Route",
        "title": "How to Finance Buying a Vending Route | Axiant",
        "og_title": "How to Finance Buying a Vending Route",
        "h1": "How to Finance Buying a Vending Route",
        "headline": "How to Finance the Purchase of an Existing Vending Route",
        "lede": "What you are really buying, what to verify before you borrow, and how "
                "route purchases are structured",
        "meta_desc": "Buying a vending route means buying machines plus location "
                     "contracts. How SBA 7(a), equipment loans and seller notes finance "
                     "it, and what to check first.",
        "article_desc": "How buyers finance an existing vending route: structures, the "
                        "SBA equity injection, and the due diligence lenders expect.",
        "keywords": "finance vending route, buy vending route loan, vending business "
                    "acquisition financing, SBA loan vending route",
        "quick_answer": "A vending route is machines plus the location contracts and "
                        "cash flow that come with them, so it is financed as a "
                        "<strong>business acquisition</strong>, not just equipment. "
                        "Common structures are an <strong>SBA 7(a) loan</strong> (with "
                        "at least <strong>10% equity injection</strong> for a change of "
                        "ownership), an equipment loan on the machines plus a seller "
                        "note, or both. Axiant Partners, a business-loan broker in Boca "
                        "Raton, sees the location contracts decide these deals.",
        "sections": [
            ("What You Are Actually Buying",
             "<p>The asking price for a route is usually well above what the machines "
             "would sell for on their own. The difference is what you are paying for "
             "the placements and the revenue they produce:</p>"
             + _table(["Part of the route", "What it is worth to a lender"], [
                 ["Machines", "Liquidation value; can secure an equipment loan"],
                 ["Location agreements", "The revenue, if they transfer to you"],
                 ["Goodwill", "No collateral value; needs SBA or seller financing"],
                 ["Inventory", "Small; usually bought at cost"],
                 ["Vehicle", "Titled; financed separately if included"],
             ])
             + "<p>Buyer and seller report the price split between equipment, goodwill "
             "and other assets to the IRS on Form 8594. The split matters to you twice: "
             "it decides what you can depreciate, and it shows a lender how much of the "
             "price has collateral behind it.</p>"),
            ("Verify Before You Borrow",
             "<p>A lender will check these, and you should check them first:</p>"
             "<ul>"
             "<li><strong>Sales by machine.</strong> Telemetry or card-reader reports per "
             "machine and location. A route sold on the seller's word is very hard to "
             "finance.</li>"
             "<li><strong>Deposits that match.</strong> Vending still takes cash. Bank "
             "deposits and tax returns should line up with the sales the seller "
             "reports.</li>"
             "<li><strong>Location agreements.</strong> Whether each one is in writing, "
             "how long it runs, whether it can be assigned to a new owner, and the "
             "commission. Handshake placements can walk away after a sale.</li>"
             "<li><strong>Liens on the machines.</strong> Vending machines have no "
             "title; a lender's lien is a UCC-1 filed with the secretary of state. A "
             "UCC search shows whether the seller's machines are already pledged.</li>"
             "<li><strong>Machine age and payment hardware.</strong> Older cash-only "
             "units may need card readers or replacement soon after you buy.</li>"
             "</ul>"),
            ("How Route Purchases Are Structured",
             "<ul>"
             "<li><strong>SBA 7(a).</strong> The usual route for a purchase with "
             "meaningful goodwill. SBA's rules require an equity injection for a "
             "complete change of ownership - at least 10% of the project cost - and a "
             "seller note counts toward it only on full standby and only for part of it. "
             "See <a href=\"/business-acquisition-financing.html\">business acquisition "
             "financing</a>.</li>"
             "<li><strong>Equipment loan plus seller note.</strong> An equipment lender "
             "finances part of the machines' liquidation value, and the seller carries "
             "the rest. Faster than SBA, but the equipment loan covers only the "
             "machines.</li>"
             "<li><strong>Seller financing alone.</strong> Common on small routes. Make "
             "sure the note's terms are written and that a UCC search shows no other "
             "lender on the machines.</li>"
             "<li><strong>Working capital.</strong> Keep some aside. Inventory, fuel and "
             "early repairs come before the first full month of sales.</li>"
             "</ul>"),
            ("A Worked Example",
             "<p>Illustrative arithmetic, not a quote. A buyer agrees $120,000 for a "
             "route of established machines with written, assignable location "
             "agreements:</p>"
             + _table(["Structure", "Figure"], [
                 ["Purchase price", "$120,000"],
                 ["Equity injection (10%)", "$12,000"],
                 ["SBA 7(a) loan", "$108,000"],
                 ["Payment, 11.5% / 10 yrs", "About $1,518"],
             ])
             + "<p>The underwriting question is whether the route's verified cash flow, "
             "after product, commissions, fuel and the buyer's own pay, covers $1,518 "
             "comfortably. Closing costs and the SBA guarantee fee are extra.</p>"),
            ("When a Route Purchase Is Hard to Finance",
             "<ul>"
             "<li><strong>Placements are verbal.</strong> Without written agreements, "
             "there is nothing to show the revenue will stay.</li>"
             "<li><strong>Sales are unverifiable.</strong> No telemetry, no matching "
             "deposits.</li>"
             "<li><strong>The price is mostly goodwill on a small route.</strong> Too "
             "small for SBA to be worth the paperwork, too little collateral for an "
             "equipment lender; seller financing is usually the answer.</li>"
             "</ul>"
             "<p>After the purchase, growing the route is an equipment question again: "
             "see <a href=\"../typical-vending-machine-financing-rates-2026/\">typical "
             "vending machine financing rates</a> and "
             "<a href=\"../micro-market-financing/\">micro-market financing</a>.</p>"),
        ],
        "faqs": [
            ("Can I get a loan to buy a vending route?",
             "Yes. Routes are financed as small business acquisitions - commonly with an "
             "SBA 7(a) loan, an equipment loan on the machines plus a seller note, or "
             "seller financing alone on small routes."),
            ("How much do I need to put down to buy a vending route?",
             "With an SBA 7(a) loan for a complete change of ownership, SBA requires an "
             "equity injection of at least 10% of the project cost. Other structures "
             "vary with the lender and the seller."),
            ("Can a seller note count toward my down payment?",
             "Under SBA rules, only if the note is on full standby for the life of the "
             "SBA loan, and only for part of the required injection."),
            ("What should I check before buying a vending route?",
             "Sales by machine, bank deposits that match, written and assignable location "
             "agreements, a UCC lien search on the machines, and the age of the machines "
             "and payment hardware."),
            ("Will an equipment loan cover the whole route price?",
             "Rarely. An equipment lender lends against the machines' liquidation value, "
             "which is usually well below a route's price. The rest needs SBA financing, "
             "a seller note or your own cash."),
        ],
        "related": [
            ("/vending-machine-financing.html", "Vending machine financing"),
            ("../micro-market-financing/", "Micro-market financing"),
            ("/business-acquisition-financing.html", "Business acquisition financing"),
            ("/match.html", "Get matched"),
        ],
        "sources": [SBA_SOP, IRS_8594, UCC_9310],
    },
]
