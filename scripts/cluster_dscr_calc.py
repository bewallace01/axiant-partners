# -*- coding: utf-8 -*-
"""How DSCR is calculated - rewrite on the v2 renderer, 2026-11-11 daily batch.

Same URL (dscr-loans/articles/how-dscr-is-calculated/), original datePublished 2026-09-02 kept.
First built by build-dscr-articles.py from dscr_articles_batch1.py; that entry is now superseded
by this module, so rebuild this page from here, not from batch1.

Search Console, Oct 13 to Nov 9 2026: "how to calculate dscr" 156 impressions at position 78,
"dscr formula" 29 at 66, "dscr preparation" 20 at 69. The old page put the formula after a long
intro and the worked example fourth. Now the formula and the worked example come first, followed
by a table of example DSCRs (rate and loan size) and a preparation checklist.

Every figure was computed by script (standard monthly amortization, 30 years): the original
example's $1,480 principal and interest on $225,000 is about a 6.9% rate; at 6.5/7/7.5/8% the
same loan gives DSCRs of 1.05/1.01/0.98/0.94 with $5,340 a year of taxes and insurance; at 7% a
$200,000/$180,000/$160,000 loan gives 1.11/1.20/1.30; the largest loan at 7% for 1.00/1.20/1.25
is about $228,918/$179,618/$169,757. Thresholds (1.00 floor, 1.20-1.25 comfortable) are the
page's existing typical-range framing. hub_by_hand: the DSCR hub comes from build-dscr-hub.py.
"""
from cluster_table import table

IRS527 = ("https://www.irs.gov/publications/p527", "IRS Publication 527: Residential Rental Property",
          "The federal definition of rental income and deductible expenses - the same schedule an underwriter "
          "reads when your return is on file.")
SLOOS = ("https://www.federalreserve.gov/data/sloos.htm", "Federal Reserve Senior Loan Officer Opinion Survey",
         "Quarterly survey of bank lending standards, including commercial real estate. The public record of "
         "whether underwriting is tightening.")
HVS = ("https://www.census.gov/housing/hvs/index.html", "U.S. Census Bureau Housing Vacancy Survey",
       "Quarterly rental vacancy rates by region - the public check on whether a market rent assumption is realistic.")

CLUSTER = {
    "pillar": "dscr-loans.html",
    "hub": "dscr-loans/articles",
    "hub_by_hand": True,
    "crumb": "DSCR Loans",
    "cta_inline": "Get matched with DSCR lenders",
    "cta_button": "Get Matched for a DSCR Loan",
}

ARTICLES = [{
    "slug": "how-dscr-is-calculated",
    "date_published": "2026-09-02",
    "crumb": "How DSCR Is Calculated",
    "title": "How to Calculate DSCR: Formula and Worked Examples | Axiant",
    "og_title": "How to Calculate DSCR: The Formula, a Worked Example and Ratio Tables",
    "h1": "How to Calculate DSCR: The Formula and Worked Examples",
    "headline": "How to Calculate DSCR: The Formula and Worked Examples",
    "lede": "The formula first, then a rental worked line by line, a table of how rate and loan size move "
            "the ratio, and what to prepare before a lender runs it",
    "meta_desc": "DSCR formula: net operating income divided by annual debt service. A worked rental example, a "
                 "table of DSCRs by rate and loan size, and a preparation checklist.",
    "article_desc": "How to calculate DSCR for a rental loan: the formula, a worked example, tables showing how "
                    "the interest rate and loan amount change the ratio, the largest loan that hits 1.20 or 1.25, "
                    "and what to prepare before applying.",
    "keywords": "how to calculate dscr, dscr formula, dscr calculation, debt service coverage ratio formula, dscr "
                "preparation, dscr example, dscr loan calculation",
    "quick_answer": "<strong>DSCR = net operating income &divide; annual debt service.</strong> A rental with "
                    "$23,616 of net operating income and $23,100 of yearly principal, interest, taxes and "
                    "insurance has a DSCR of <strong>1.02</strong>. Most DSCR lenders want at least 1.00, and "
                    "<strong>1.20 to 1.25</strong> is commonly treated as comfortable. Those are typical "
                    "thresholds, not a quote; Axiant Partners, a business-loan broker in Boca Raton, runs the "
                    "ratio the way lenders do before you apply.",
    "sections": [
        ("The DSCR Formula, Worked Through",
         "<p><strong>DSCR = Net Operating Income &divide; Annual Debt Service</strong></p>"
         "<p>Take a single-family rental bought for $300,000, renting at $2,400 a month, financed with a "
         "$225,000 loan over 30 years at about 6.9%.</p>"
         + table(["Line", "Monthly", "Annual"], [
             ["Gross rent", "$2,400", "$28,800"],
             ["Less vacancy allowance (5%)", "&minus;$120", "&minus;$1,440"],
             ["Less property management (8%)", "&minus;$192", "&minus;$2,304"],
             ["Less maintenance reserve", "&minus;$120", "&minus;$1,440"],
             ["<strong>Net operating income</strong>", "<strong>$1,968</strong>", "<strong>$23,616</strong>"],
             ["Principal &amp; interest", "$1,480", "$17,760"],
             ["Taxes", "$310", "$3,720"],
             ["Insurance", "$135", "$1,620"],
             ["<strong>Annual debt service (PITI)</strong>", "<strong>$1,925</strong>", "<strong>$23,100</strong>"],
         ])
         + "<p>$23,616 &divide; $23,100 = <strong>1.02</strong>. The property covers its debt, but only "
         "just. A ratio of 1.00 means rent exactly covers the payment; below 1.00 you fund the gap every "
         "month; above 1.00 is cushion. On a program that wants 1.20 this file doesn't work as structured, "
         "and the fix is arithmetic: a smaller loan, a lower rate or a different property.</p>"),
        ("DSCR Examples: How Rate and Loan Size Move the Ratio",
         "<p>Same property, same $23,616 of net operating income and the same $5,340 a year of taxes and "
         "insurance. Only the loan changes. All loans are 30-year, fully amortizing.</p>"
         + table(["$225,000 loan at", "P&amp;I per month", "Annual debt service", "DSCR"], [
             ["6.5%", "$1,422", "$22,406", "1.05"],
             ["7.0%", "$1,497", "$23,303", "1.01"],
             ["7.5%", "$1,573", "$24,219", "0.98"],
             ["8.0%", "$1,651", "$25,152", "0.94"],
         ])
         + "<p>Half a point of rate moves this ratio by about 0.04. Now hold the rate at 7% and change the "
         "loan amount instead:</p>"
         + table(["Loan at 7%", "P&amp;I per month", "Annual debt service", "DSCR"], [
             ["$200,000", "$1,331", "$21,307", "1.11"],
             ["$180,000", "$1,198", "$19,711", "1.20"],
             ["$160,000", "$1,064", "$18,114", "1.30"],
         ])
         + "<p>Working backward is often more useful. At 7%, the largest loan this rent supports is about "
         "<strong>$228,900</strong> for a 1.00 ratio, <strong>$179,600</strong> for 1.20 and "
         "<strong>$169,800</strong> for 1.25. On a $300,000 purchase, a 1.25 minimum means roughly 43% "
         "down, not 25%. That is why the ratio, not the loan-to-value, usually sets the size of a DSCR loan. "
         "Figures are rounded and come from standard monthly amortization.</p>"),
        ("What Goes in Net Operating Income",
         "<p>Net operating income is gross rent minus operating expenses, before any mortgage payment. "
         "Underwriters usually deduct:</p>"
         "<ul><li><strong>Vacancy</strong>, as an allowance even if the unit is leased today</li>"
         "<li><strong>Property management</strong>, often imputed as a percentage of rent even if you self-manage</li>"
         "<li><strong>Maintenance and reserves</strong> on many programs</li>"
         "<li><strong>Taxes, insurance and HOA dues</strong>, unless the program counts them in debt service instead</li></ul>"
         "<p>Leave out the mortgage, capital improvements, depreciation and your own labor. Depreciation "
         "trips people up: it is often the biggest line on a Schedule E, but it is a tax deduction, not "
         'cash spent. For which rent counts, see <a href="/dscr-loans/articles/what-counts-as-rental-income-dscr/">what '
         "counts as rental income on a DSCR loan</a>.</p>"),
        ("What Goes in Annual Debt Service",
         "<p>Debt service is twelve months of payments on the loan being underwritten. Programs differ on "
         "what that includes, and it changes the answer more than anything else:</p>"
         + table(["Denominator", "Effect on the ratio", "Where you see it"], [
             ["Principal + interest only", "Highest ratio", "Some portfolio programs; taxes and insurance move to the expense side"],
             ["PITI: principal, interest, taxes, insurance", "Lower ratio", "The common convention on single-family rentals"],
             ["PITIA: PITI plus HOA dues", "Lowest ratio", "Condos and properties with an association"],
         ])
         + "<p>Ask which convention a lender uses before comparing quotes. The same property can show 1.25 "
         "one way and under 1.00 another, and both underwriters are doing it right.</p>"),
        ("DSCR Preparation: What to Gather Before You Apply",
         "<p>Most ratios that fail in underwriting fail because an input changed, not because the math was "
         "wrong. Gather the figures a lender will use and run the ratio yourself first:</p>"
         "<ol>"
         "<li><strong>Rent.</strong> The signed lease, plus a realistic market rent. Underwriters generally "
         "use the lower of the lease and the appraiser's market rent opinion.</li>"
         "<li><strong>Taxes after purchase.</strong> Estimate the reassessed bill, not the seller's current one.</li>"
         "<li><strong>A bound insurance quote.</strong> Premiums in coastal and wildfire markets have moved "
         "sharply; an old estimate is a common reason a file fails late.</li>"
         "<li><strong>HOA dues and special assessments</strong>, if any.</li>"
         "<li><strong>The lender's convention.</strong> P&amp;I or PITI, and whether it imputes management.</li>"
         "<li><strong>The rate you'll actually get</strong>, then rerun at half a point higher to see your margin.</li>"
         "</ol>"
         '<p>Our <a href="/dscr-calculator.html">DSCR calculator</a> takes the same inputs. '
         'The thresholds each program uses are on <a href="/dscr-loan-requirements.html">DSCR loan requirements</a>.</p>'),
        ("How to Raise a Ratio That Falls Short",
         "<ul><li><strong>Put more down.</strong> As the second table shows, cutting the loan is the most direct lever.</li>"
         "<li><strong>Buy down the rate</strong> with points, if the payment drop clears the threshold.</li>"
         "<li><strong>Use an interest-only period</strong> where a program offers one and underwrites to it.</li>"
         "<li><strong>Correct expense assumptions with evidence</strong>, such as a bound insurance quote below the underwriter's estimate.</li></ul>"
         "<p>A strong personal balance sheet doesn't change the ratio. That's the point of a DSCR loan, "
         "and it cuts both ways.</p>"),
        ("DSCR on a Business Loan",
         "<p>Business lenders use the same idea with different inputs: the business's cash flow available "
         "for debt (often net income plus interest, depreciation and amortization) divided by all of its "
         "annual loan payments, sometimes with the owner's personal debts added in a global ratio. The "
         "thresholds are similar; our "
         '<a href="/sba-loans/articles/sba-loan-requirements/">SBA loan requirements</a> page covers what '
         "SBA lenders typically look for.</p>"),
    ],
    "faqs": [
        ("How do you calculate DSCR?",
         "Divide net operating income by annual debt service. Net operating income is rent minus vacancy, "
         "management, maintenance and other operating costs; debt service is a year of loan payments. $23,616 "
         "divided by $23,100 is a DSCR of 1.02."),
        ("What is a good DSCR for a rental property?",
         "1.20 to 1.25 is commonly treated as comfortable, and 1.00 is the usual floor, where the property just "
         "covers its debt. Some lenders go below 1.00 with a larger down payment or reserves, and price for it."),
        ("Does DSCR include taxes and insurance?",
         "It depends on the program. Many single-family rental programs use PITI (principal, interest, taxes "
         "and insurance), and condos add HOA dues (PITIA). Others use principal and interest only and count "
         "taxes and insurance as operating expenses."),
        ("How much can I borrow at a 1.25 DSCR?",
         "Divide net operating income by 1.25 to get the most debt service allowed, subtract taxes and "
         "insurance if the lender uses PITI, and size the loan to that payment. In the example, $23,616 of "
         "income supports about $169,800 at 7% over 30 years."),
        ("Is depreciation included in the DSCR calculation?",
         "No. Depreciation is a tax deduction, not a cash expense, so it is left out of net operating income."),
        ("What rent do underwriters use if my lease is above market?",
         "Generally the lower of the lease and the appraiser's market rent opinion, so an above-market lease "
         "doesn't lift the ratio."),
    ],
    "related": [
        ("/dscr-loans.html", "DSCR Loans: qualify on the property's rent, not your income"),
        ("/dscr-loan-requirements.html", "DSCR loan requirements"),
        ("/dscr-calculator.html", "DSCR calculator"),
        ("/dscr-loans/articles/what-counts-as-rental-income-dscr/", "What counts as rental income on a DSCR loan"),
        ("/dscr-loans/articles/minimum-dscr-ratio-by-lender-type/", "Minimum DSCR ratio by lender type"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [IRS527, SLOOS, HVS],
}]
