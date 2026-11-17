# -*- coding: utf-8 -*-
"""SBA loans for agriculture - new spoke, daily batch 2026-11-14.

Search Console, Oct 15 - Nov 11 2026: "sba loans for agriculture" 17 impressions at position
37, plus "sba agriculture loans ..." 3 at 52, landing on agriculture-business-financing.html,
which only mentions SBA in passing. No page answers whether farms and ranches can use SBA
loans: usda-b-and-i-vs-sba-7a compares two programs for rural businesses in general and is
linked, not repeated. The query is not split between our pages.

Facts read from the regulation text (eCFR, Nov 14 2026): 13 CFR 120.110 ineligible business
list (agriculture is not on it); 13 CFR 121.201 receipts size standards by NAICS (subsectors
111 and 112, values quoted in the table); 13 CFR 121.301(b) alternative size standard for 7(a)
and 504 (tangible net worth <= $20M, average net income after federal income tax <= $6.5M for
the two prior fiscal years, affiliates included); 13 CFR 120.151 ($5,000,000 per 7(a) loan,
$3,750,000 guaranty cap per borrower); 13 CFR 120.212 (10 years unless real estate or equipment
with a useful life over 10 years, 25 years maximum); 7 CFR 761.8 (FSA direct operating
$400,000, direct farm ownership $600,000, guaranteed limits indexed each year); 7 CFR 764.251
(operating loans may buy farm equipment) and 764.254 (term operating loans: useful life or 7
years, whichever is less). Prime 7.00% (H.15, Nov 11) as on the Nov 13 SBA pages; the
SOP 50 10 8.1 cap of prime + 3.0% on 7(a) loans over $350,000 as logged in the plan. Payments
computed by script. No named lenders.
"""
from cluster_table import table

CFR_110 = ("https://www.law.cornell.edu/cfr/text/13/120.110",
           "13 CFR 120.110: businesses ineligible for SBA loans",
           "The list of business types SBA will not finance; agricultural enterprises are not on it.")
CFR_201 = ("https://www.law.cornell.edu/cfr/text/13/121.201",
           "13 CFR 121.201: SBA size standards by NAICS code",
           "Receipts limits for crop production (subsector 111) and animal production (112).")
CFR_301 = ("https://www.law.cornell.edu/cfr/text/13/121.301",
           "13 CFR 121.301: size rules for SBA loans",
           "The alternative size standard: $20 million tangible net worth, $6.5 million average net income.")
CFR_151 = ("https://www.law.cornell.edu/cfr/text/13/120.151",
           "13 CFR 120.151: 7(a) loan and guaranty limits",
           "The $5,000,000 maximum 7(a) loan and the $3,750,000 guaranty cap per borrower.")
CFR_212 = ("https://www.law.cornell.edu/cfr/text/13/120.212",
           "13 CFR 120.212: SBA loan maturities",
           "Ten years, or up to 25 years for real estate and long-life equipment.")
CFR_FSA = ("https://www.law.cornell.edu/cfr/text/7/761.8",
           "7 CFR 761.8: FSA farm loan limits",
           "Direct operating ($400,000) and direct farm ownership ($600,000) limits; guaranteed limits indexed.")
CFR_764 = ("https://www.law.cornell.edu/cfr/text/7/764.254",
           "7 CFR 764.254: FSA operating loan terms",
           "Term operating loans run the useful life of the security or 7 years, whichever is less.")

CLUSTER = {
    "pillar": "agriculture-business-financing.html",
    "hub": "agriculture-business-financing",
    "no_hub": True,
    "back_href": "/agriculture-business-financing.html",
    "crumb": "Agriculture Business Financing",
    "cta_inline": "Tell us what the farm needs to buy or refinance",
    "cta_button": "Get Matched for Farm Financing",
}

ARTICLES = [{
    "slug": "sba-loans-for-agriculture",
    "crumb": "SBA Loans for Agriculture",
    "title": "SBA Loans for Agriculture: Farm Eligibility and Limits",
    "og_title": "SBA Loans for Agriculture: Can a Farm or Ranch Use One?",
    "h1": "SBA Loans for Agriculture: Can a Farm or Ranch Use One?",
    "headline": "SBA Loans for Agriculture: Farm Eligibility, Size Limits and Terms",
    "lede": "Which farms qualify, the size standards by crop and livestock type, how SBA compares "
            "with FSA and USDA B&amp;I, and what the payments look like",
    "meta_desc": "SBA loans for agriculture: farms and ranches are eligible, size limits by NAICS "
                 "code, 7(a) up to $5 million, terms to 25 years, and how SBA compares with FSA.",
    "article_desc": "Whether farms, ranches and growers can use SBA 7(a) and 504 loans: eligibility, "
                    "size standards by agricultural NAICS code, loan limits and terms, and the FSA "
                    "and USDA alternatives.",
    "keywords": "sba loans for agriculture, sba farm loans, sba loan for farm, sba agriculture loans, "
                "can farms get sba loans, sba 7a for ranch",
    "quick_answer": "As of November 2026, farms and ranches can use SBA loans: agriculture is not on "
                    "SBA&rsquo;s ineligible list (13 CFR 120.110). A 7(a) loan goes up to "
                    "<strong>$5 million</strong>, with terms to 10 years for equipment and working "
                    "capital and up to <strong>25 years</strong> for land and buildings. Most farm "
                    "types must stay under a receipts size standard of about "
                    "<strong>$2.25-$5.5 million</strong> a year, or pass SBA&rsquo;s net worth test. "
                    "Axiant Partners, a business-loan broker in Boca Raton, compares SBA, FSA-guaranteed "
                    "and equipment lenders. Typical ranges, not a quote.",
    "sections": [
        ("Can a Farm Get an SBA Loan?",
         "<p>Yes. SBA&rsquo;s list of ineligible businesses names nonprofits, lenders, passive "
         "landlords, life insurers, speculative ventures and a handful of others; crop farms, "
         "ranches, nurseries, dairies and aquaculture are not on it "
         "(<a href=\"https://www.law.cornell.edu/cfr/text/13/120.110\" rel=\"noopener nofollow\" target=\"_blank\">13 "
         "CFR 120.110</a>). In practice the questions a lender asks a farm are the ones it asks any "
         "borrower: is the business small under SBA&rsquo;s rules, does the cash flow cover the "
         "payment, and is the borrower operating the farm rather than only owning land that someone "
         "else farms.</p>"
         "<p>A landowner who only leases ground to a tenant looks like a passive real estate holder, "
         "which SBA excludes outside its eligible passive company rules. An owner-operator buying "
         "the land it farms is the normal case.</p>"
         "<p>Many agricultural lenders steer farm production loans to the Farm Service Agency first, "
         "and some banks that make SBA loans do not make farm loans at all. Ask a lender whether it "
         "does both before you send a file.</p>"),
        ("Size Standards for Farms and Ranches",
         "<p>SBA measures most agricultural businesses by average annual receipts, including "
         "affiliates (<a href=\"https://www.law.cornell.edu/cfr/text/13/121.201\" rel=\"noopener nofollow\" target=\"_blank\">13 "
         "CFR 121.201</a>). A selection of the limits:</p>"
         + table(["Farm type (NAICS)", "Receipts limit"], [
             ["Soybeans (111110)", "$2.25 million"],
             ["Corn (111150)", "$2.5 million"],
             ["Potatoes (111211)", "$4.25 million"],
             ["Other vegetables (111219)", "$3.75 million"],
             ["Orange groves (111310)", "$4.0 million"],
             ["Strawberries (111333)", "$5.5 million"],
             ["Nursery and trees (111421)", "$3.25 million"],
             ["Beef cattle (112111)", "$2.5 million"],
             ["Cattle feedlots (112112)", "$22.0 million"],
             ["Dairy (112120)", "$3.75 million"],
             ["Broilers (112320)", "$3.5 million"],
             ["Chicken eggs (112310)", "$19.0 million"],
             ["Finfish farming (112511)", "$3.75 million"],
         ])
         + "<p>A farm over its receipts limit can still qualify for a 7(a) or 504 loan under the "
         "alternative size standard: tangible net worth of no more than $20 million and average net "
         "income after federal income tax of no more than $6.5 million over the two prior fiscal "
         "years, affiliates included "
         "(<a href=\"https://www.law.cornell.edu/cfr/text/13/121.301\" rel=\"noopener nofollow\" target=\"_blank\">13 "
         "CFR 121.301(b)</a>). For many family operations with high gross sales and thin margins, "
         "that test is the easier one to pass.</p>"),
        ("SBA vs FSA vs USDA B&amp;I vs Equipment Financing",
         table(["", "SBA 7(a)", "FSA farm loans", "USDA B&amp;I", "Equipment loan"], [
             ["Best for", "Land, buildings, equipment, working capital, buying a farm business",
              "Production farms, beginning farmers, operating needs", "Larger rural businesses, often processing",
              "A single tractor, combine or implement"],
             ["Size of loan", "Up to $5 million", "Direct: $400,000 operating, $600,000 ownership; guaranteed limits indexed yearly",
              "Larger; see the USDA page", "The machine&rsquo;s price"],
             ["Term", "10 years; up to 25 for real estate", "Operating term loans: useful life or 7 years",
              "See the USDA page", "Commonly 3-7 years"],
             ["Who lends", "A bank or SBA lender", "FSA directly, or a bank with an FSA guarantee",
              "A bank with a USDA guarantee", "Dealer, captive or independent lender"],
             ["Speed", "Weeks to months", "Weeks to months", "Months", "Days"],
         ])
         + "<p>FSA limits are from <a href=\"https://www.law.cornell.edu/cfr/text/7/761.8\" rel=\"noopener nofollow\" target=\"_blank\">7 "
         "CFR 761.8</a> and its operating loans may buy farm equipment and livestock (7 CFR 764.251). "
         "How B&amp;I and 7(a) compare in detail is on "
         "<a href=\"/usda-business-loans/articles/usda-b-and-i-vs-sba-7a/\">USDA B&amp;I vs SBA 7(a)</a>, "
         "and the B&amp;I program itself on <a href=\"/usda-business-loans.html\">USDA business loans</a>.</p>"),
        ("What SBA Money Can Do on a Farm",
         "<ul>"
         "<li><strong>Buy or expand land and buildings</strong> the operation uses: barns, packing "
         "sheds, greenhouses, a nursery&rsquo;s propagation houses. Real estate can run up to 25 "
         "years (<a href=\"https://www.law.cornell.edu/cfr/text/13/120.212\" rel=\"noopener nofollow\" target=\"_blank\">13 "
         "CFR 120.212</a>).</li>"
         "<li><strong>Equipment packages</strong> that are too mixed for one dealer program, such as "
         "irrigation, a packing line and used tractors on one loan. Single machines usually finance "
         "faster as equipment loans; see <a href=\"/equipment/tractors/\">tractor financing</a>.</li>"
         "<li><strong>Working capital</strong> for inputs and payroll, though a seasonal line is "
         "often a better fit than a 10-year term loan for a crop cycle.</li>"
         "<li><strong>Buying an existing agricultural business</strong>, such as a nursery, a feed "
         "store or a custom harvesting outfit, with goodwill in the price.</li>"
         "</ul>"
         "<p>A 7(a) loan is capped at $5,000,000, and SBA&rsquo;s guaranteed share across all of a "
         "borrower&rsquo;s loans at $3,750,000 "
         "(<a href=\"https://www.law.cornell.edu/cfr/text/13/120.151\" rel=\"noopener nofollow\" target=\"_blank\">13 "
         "CFR 120.151</a>). Long-life buildings with a smaller equipment share sometimes fit the 504 "
         "program better; start from <a href=\"/sba-loans.html\">SBA loans</a>.</p>"),
        ("Worked Example: Equipment and a Packing Shed",
         "<p><strong>Illustrative assumptions, not a quote.</strong> A vegetable grower with "
         "receipts under its $3.75 million size standard borrows for two things. Rates assume prime "
         "of 7.00% (H.15, November 11, 2026) plus 2.75%, on $750,000 of equipment and a $1,500,000 shed, under the prime + 3.0% cap SBA sets for "
         "7(a) loans over $350,000. Computed by script.</p>"
         + table(["Loan", "Term", "About per month", "Total interest"], [
             ["Equipment, SBA, 9.75%", "10 years", "$9,808", "$426,932"],
             ["Shed, SBA, 9.75%", "25 years", "$13,367", "$2,510,118"],
             ["Equipment loan, 8%", "7 years", "$11,690", "$231,932"],
         ])
         + "<p>The SBA term lowers the equipment payment by about $1,900 a month against a 7-year "
         "equipment loan at an assumed 8%, but costs about $195,000 more interest if carried to "
         "term. A grower whose cash comes in at harvest should also ask whether the lender will set "
         "seasonal or annual payments rather than monthly ones.</p>"),
        ("How to Apply as a Farm",
         "<ol>"
         "<li><strong>Find your NAICS code</strong> and check its size standard, or run the net "
         "worth and net income test.</li>"
         "<li><strong>Gather three years of farm tax returns</strong> (Schedule F or entity returns), "
         "a balance sheet, and production or sales records.</li>"
         "<li><strong>Price the project</strong>: land appraisal, building bids, equipment quotes.</li>"
         "<li><strong>Ask two kinds of lender</strong>: one that makes SBA loans to agricultural "
         "borrowers and one that makes FSA-guaranteed loans, and compare terms and payment "
         "schedules.</li>"
         "<li><strong>Expect weeks, not days.</strong> If a planting or harvest date drives the "
         "purchase, start early or bridge the machine with equipment financing.</li>"
         "</ol>"
         "<p>Axiant sends one application to lenders that handle farm files. See also "
         "<a href=\"/agriculture-business-financing.html\">agriculture business financing</a> or "
         "<a href=\"/match.html\">get matched</a>.</p>"),
    ],
    "faqs": [
        ("Can you get an SBA loan for a farm?",
         "Yes. Agricultural businesses are not on SBA's ineligible list in 13 CFR 120.110. The farm "
         "has to meet SBA's size standard and the usual credit tests, and should be operating the "
         "land rather than only leasing it out."),
        ("What is the SBA size standard for a farm?",
         "It depends on the NAICS code. Most crop and livestock codes fall between $2.25 million and "
         "$5.5 million in average annual receipts, with exceptions such as cattle feedlots ($22.0 "
         "million) and egg production ($19.0 million), under 13 CFR 121.201."),
        ("Is an SBA loan or an FSA loan better for a farm?",
         "FSA loans are built for production agriculture and beginning farmers, with direct limits of "
         "$400,000 for operating and $600,000 for farm ownership. SBA 7(a) goes to $5 million and also "
         "fits agricultural businesses that are not farms. Many growers compare both."),
        ("How long can an SBA farm loan run?",
         "Up to 10 years for equipment and working capital, and up to 25 years for real estate or "
         "equipment with a useful life over 10 years, under 13 CFR 120.212."),
        ("Can I buy farmland with an SBA loan?",
         "Farmland the operation itself farms can be financed as real estate. Land bought to lease to "
         "someone else looks passive, which SBA generally does not finance."),
        ("Can an SBA loan pay for a tractor?",
         "Yes, but a single tractor usually finances faster through an equipment loan or dealer "
         "program. SBA fits better when the machine is part of a larger package."),
    ],
    "related": [
        ("/agriculture-business-financing.html", "Agriculture business financing"),
        ("/usda-business-loans/articles/usda-b-and-i-vs-sba-7a/", "USDA B&amp;I vs SBA 7(a)"),
        ("/usda-business-loans.html", "USDA business loans"),
        ("/equipment/tractors/", "Tractor financing"),
        ("/sba-loans.html", "SBA loans"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [CFR_110, CFR_201, CFR_301, CFR_151, CFR_212, CFR_FSA, CFR_764],
}]
