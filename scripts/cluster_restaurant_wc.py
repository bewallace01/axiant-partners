# -*- coding: utf-8 -*-
"""Restaurant working capital - new spoke, daily batch 2026-11-12.

Search Console, Oct 13 - Nov 9 2026: "restaurant working capital" 29 impressions at
position 22, "restaurant working capital loans" 6 at 37 and "restaurant working capital
loan" 5 at 32, all landing on /restaurants-business-financing.html, which covers working
capital in one section. No page answered it on its own (checked the sitemap: equipment,
SBA acquisition, MCA for restaurants, multi-unit term loan and debt relief pages exist).
Scoped away from mca-for-restaurants (which is about the MCA itself) and linked to it.

Ranges reuse what the site publishes: line of credit 8-13% APR at banks and 14-30%+
online (typical LOC rates page), online term loans 14-30% (working capital rates page),
MCA factor 1.15-1.50 and roughly 40-100%+ effective APR (MCA rates page), SBA 7(a)
maximum rate base + 6.0% for $50,001-$250,000 ($100K page, from the SBA). The worked
example uses stated assumptions and was computed by script. No named lenders.
"""
from cluster_table import table

SBA_7A = ("https://www.sba.gov/funding-programs/loans/7a-loans", "SBA 7(a) Loans",
          "Uses of 7(a) proceeds, including working capital, and the program's maximum rates.")
SBCS = ("https://www.fedsmallbusiness.org/", "Federal Reserve Small Business Credit Survey",
        "Survey data on how small firms, including restaurants, apply for and use credit.")
FTC = ("https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic",
       "FTC: Protecting Small Businesses Seeking Financing",
       "The FTC's guidance on misrepresented costs by lenders, brokers and merchant cash advance providers.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Research on small business credit, including how costs are disclosed to borrowers.")

CLUSTER = {
    "pillar": "working-capital-loans.html",
    "hub": "working-capital-loans/articles",
    "no_hub": True,
    "back_href": "/working-capital-loans/articles/",
    "crumb": "Working Capital Loans",
    "cta_inline": "Tell us your slow months and your sales",
    "cta_button": "Get Matched for Restaurant Working Capital",
}

ARTICLES = [{
    "slug": "restaurant-working-capital",
    "crumb": "Restaurant Working Capital",
    "title": "Restaurant Working Capital Loans: Options and Costs | Axiant",
    "og_title": "Restaurant Working Capital: Funding Payroll, Inventory and Slow Months",
    "h1": "Restaurant Working Capital: Funding Payroll, Inventory and Slow Months",
    "headline": "Restaurant Working Capital: Funding Payroll, Inventory and Slow Months",
    "lede": "You are paid every day and still run short. Which product fits each gap, what it "
            "typically costs, and a slow-season example you can rerun on your own numbers",
    "meta_desc": "Restaurant working capital loans compared: lines of credit at about 8-13% APR at "
                 "banks, SBA 7(a), term loans and MCAs, with a slow-season example and costs.",
    "article_desc": "How restaurants fund payroll, inventory, repairs and slow seasons: lines of "
                    "credit, SBA 7(a), term loans and merchant cash advances compared, with a "
                    "worked off-season example.",
    "keywords": "restaurant working capital, restaurant working capital loans, restaurant line of "
                "credit, slow season restaurant financing, restaurant payroll funding",
    "quick_answer": "As of November 2026, restaurant working capital usually comes from a business "
                    "line of credit, commonly about <strong>8-13% APR</strong> at banks and "
                    "14-30%+ online, an SBA 7(a) loan, or a short online term loan. Merchant cash "
                    "advances are faster but often cost <strong>40-100%+</strong> in effective APR, "
                    "because they are repaid from daily card sales. Restaurants run short on "
                    "seasons, repairs and openings, not unpaid invoices. Axiant Partners, a "
                    "business-loan broker in Boca Raton, matches restaurants with lenders. These "
                    "are typical ranges, not a quote.",
    "sections": [
        ("Why Restaurants Run Short Even Though They Are Paid Daily",
         "<p>Most businesses that need working capital are waiting on customers who pay in 30 or 60 "
         "days. A restaurant isn&rsquo;t: card sales settle within days and cash comes in every "
         "night. The gaps come from somewhere else.</p>"
         "<ul>"
         "<li><strong>Seasons.</strong> Rent, salaried staff, insurance and loan payments stay the "
         "same in a slow month while sales drop. A beach town or a college town can lose half its "
         "volume for a season.</li>"
         "<li><strong>Repairs that can&rsquo;t wait.</strong> A walk-in cooler, a hood system or a "
         "dish machine fails on a Friday and has to be fixed before service.</li>"
         "<li><strong>Inventory runs on short terms.</strong> Food suppliers commonly want payment "
         "weekly or on delivery, so a menu change or a holiday stock-up is paid before it sells.</li>"
         "<li><strong>Openings and remodels.</strong> Hiring and training a crew, opening stock and "
         "weeks of reduced sales come before the dining room is full.</li>"
         "<li><strong>Money that isn&rsquo;t yours.</strong> Sales tax collected and tips owed to "
         "staff sit in the same account and can make the balance look larger than it is.</li>"
         "</ul>"
         "<p>Because the gap is about time and seasons rather than receivables, invoice factoring "
         "rarely fits a restaurant. Revolving credit and planned borrowing do. Catering and "
         "contract food service, which do bill on terms, are the exception.</p>"),
        ("Restaurant Working Capital Options Compared",
         "<p>The ranges below are the ones the site publishes on each product&rsquo;s own page, "
         "typical across lenders and not quotes.</p>"
         + table(["Option", "Typical cost", "Speed", "Fits"], [
             ["Business line of credit", "About 8-13% APR at banks; 14-30%+ online",
              "Weeks at a bank; days online", "Seasons and repairs, drawn and repaid"],
             ["SBA 7(a) working capital", "Capped by SBA, e.g. base rate + 6.0% on $50,001-$250,000",
              "Slowest", "A planned, larger need, such as a remodel"],
             ["Online term loan", "About 14-30%", "Days", "A one-time need with a clear payback"],
             ["Merchant cash advance", "Factor 1.15-1.50; roughly 40-100%+ effective APR",
              "Fastest", "A true emergency, short and small"],
             ["Equipment financing", "Priced on the asset and your credit", "Days to weeks",
              "Replacing kitchen equipment instead of paying cash"],
         ])
         + "<p>Detail behind each row: <a href=\"/business-line-of-credit/articles/typical-business-line-of-credit-rates-2026/\">"
         "line of credit rates</a>, <a href=\"/working-capital-loans/articles/typical-working-capital-loan-rates-2026/\">"
         "working capital loan rates</a>, <a href=\"/merchant-cash-advance/articles/typical-merchant-cash-advance-rates-2026/\">"
         "merchant cash advance rates</a> and <a href=\"/equipment-financing/articles/restaurant-equipment-financing/\">"
         "restaurant equipment financing</a>. The SBA lists working capital among the uses of "
         '<a href="https://www.sba.gov/funding-programs/loans/7a-loans" rel="noopener nofollow" '
         'target="_blank">7(a) loan proceeds</a>.</p>'),
        ("Worked Example: Funding a Four-Month Off-Season",
         "<p><strong>Illustrative assumptions, not a quote.</strong> A seasonal restaurant sells "
         "$150,000 a month in season and $60,000 a month for four slow months. Food and beverage "
         "cost is assumed at 30% of sales, slow-season labor $30,000 a month, and rent and other "
         "fixed costs $22,000 a month. Each slow month then runs $10,000 short ($60,000 less "
         "$18,000, $30,000 and $22,000), and the month before reopening adds $20,000 for stock and "
         "hiring.</p>"
         + table(["Month", "What happens", "Line of credit balance"], [
             ["1-4", "Draw $10,000 each slow month", "$10,000 rising to $40,000"],
             ["5", "Draw $20,000 to restock and hire", "$60,000"],
             ["6", "Season opens; repay $30,000", "$30,000"],
             ["7", "Repay the rest", "$0"],
         ])
         + "<p>At an illustrative 12% APR, charged at 1% a month on each month&rsquo;s balance, the "
         "interest on that schedule is about <strong>$1,900</strong>. The same $60,000 from a "
         "merchant cash advance at a 1.30 factor costs <strong>$18,000</strong>, and its holdback "
         "comes out of card sales during the slow months, when there is least to spare. In this "
         "example a peak month leaves about $35,000 after costs (at an assumed $48,000 of in-season "
         "labor), so repaying the line in two months is realistic. Put in your own numbers before "
         "you size a line.</p>"),
        ("Card Sales, Holdbacks and Why the Choice Matters",
         "<p>Restaurants get offered merchant cash advances more than almost any other business, "
         "because card sales are easy to see and easy to collect from. The advance is repaid from a "
         "share of each day&rsquo;s card receipts, so it is quick to get and hard to live with in a "
         "slow stretch. Two checks before signing anything: ask for the total repayment in writing, "
         "and convert it to an APR over the expected payback period. Our "
         "<a href=\"/merchant-cash-advance/articles/mca-for-restaurants/\">MCA for restaurants</a> "
         "guide covers holdbacks in detail. The "
         '<a href="https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic" '
         'rel="noopener nofollow" target="_blank">FTC</a> has warned providers against '
         "misrepresenting these costs.</p>"
         "<p>If you already carry advances that are squeezing the slow season, see "
         "<a href=\"/business-debt-relief/articles/restaurant-debt-relief/\">restaurant debt relief</a> "
         "before adding another one.</p>"),
        ("What Lenders Check on a Restaurant File",
         "<ul>"
         "<li><strong>Bank and card processing statements</strong>, commonly three to six months, "
         "and a full year if you are seasonal, so the lender sees the slow months as well as the "
         "good ones.</li>"
         "<li><strong>The lease.</strong> Years left on the lease, and whether it runs past the loan "
         "term, matter because the location is the business.</li>"
         "<li><strong>Existing daily or weekly debits.</strong> Advances already on the account "
         "limit what a bank will add.</li>"
         "<li><strong>Time open and ownership.</strong> Two or more years under the same owner opens "
         "more bank and SBA options.</li>"
         "<li><strong>Personal credit</strong> of the owners, since most restaurant loans carry a "
         "personal guarantee.</li>"
         "</ul>"
         "<p>See <a href=\"/working-capital-loans/articles/working-capital-loan-requirements/\">working "
         "capital loan requirements</a> for the full checklist.</p>"),
        ("How to Line Up Working Capital Before the Slow Season",
         "<ol>"
         "<li><strong>Map last year month by month</strong>: sales, food cost, labor and fixed costs. "
         "The low point is the size of the line you need.</li>"
         "<li><strong>Apply in season</strong>, while deposits are strong. A bank line is far easier "
         "to get in July than in January.</li>"
         "<li><strong>Keep sales tax and tips separate</strong> so they are never spent as working "
         "capital.</li>"
         "<li><strong>Finance equipment as equipment.</strong> Don&rsquo;t drain the line for a "
         "replacement cooler that a lease or loan can cover.</li>"
         "<li><strong>Set a repayment rule</strong>, such as repaying the line within two peak "
         "months, so it is clear by the next slow season.</li>"
         "</ol>"
         "<p>When you have the numbers, <a href=\"/match.html\">get matched with lenders that fund "
         "restaurants</a>, or start from <a href=\"/restaurants-business-financing.html\">restaurant "
         "business financing</a> for every product.</p>"),
    ],
    "faqs": [
        ("What is the best working capital option for a restaurant?",
         "For seasons and repairs, usually a business line of credit, commonly about 8-13% APR at a "
         "bank and 14-30%+ online, because you draw only what you need and repay in busy months. An "
         "SBA 7(a) loan suits a larger planned need. These are typical ranges, not a quote."),
        ("Why do restaurants need working capital if they are paid daily?",
         "Because costs don't fall with sales. Rent, salaried staff and insurance stay the same in a "
         "slow month, repairs can't wait, suppliers want payment weekly or on delivery, and openings "
         "and remodels cost money before sales arrive."),
        ("Is a merchant cash advance a good idea for a restaurant?",
         "Usually only for a short, small emergency. Factor rates of 1.15-1.50 repaid from daily card "
         "sales often work out to roughly 40-100%+ in effective APR, and the holdback bites hardest in "
         "slow months. Compare the total repayment with a line of credit first."),
        ("Can a restaurant use an SBA loan for working capital?",
         "Yes. Working capital is an allowed use of SBA 7(a) proceeds, and the SBA caps the rate, for "
         "example at the base rate plus 6.0% on loans of $50,001-$250,000. It is slower than other "
         "options, so it fits a planned need better than an emergency."),
        ("How much working capital does a restaurant need?",
         "Enough to cover the deepest point of your slow season plus a repair reserve. Map last year "
         "month by month; in the example on this page, four slow months and a restock add up to "
         "$60,000."),
        ("When should a restaurant apply for a line of credit?",
         "During the busy season, while deposits are strongest. Lenders read recent bank statements, "
         "so applying in the slow months makes the business look weaker than it is."),
    ],
    "related": [
        ("/restaurants-business-financing.html", "Restaurant business financing"),
        ("/merchant-cash-advance/articles/mca-for-restaurants/", "MCA for restaurants"),
        ("/working-capital-loans/articles/working-capital-loan-seasonal-businesses/", "Working capital for seasonal businesses"),
        ("/working-capital-loans/articles/working-capital-loan-vs-business-line-of-credit/", "Working capital loan vs line of credit"),
        ("/equipment-financing/articles/restaurant-equipment-financing/", "Restaurant equipment financing"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SBA_7A, SBCS, FTC, CFPB],
}]
