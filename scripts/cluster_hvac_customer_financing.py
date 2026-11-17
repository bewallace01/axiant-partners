# -*- coding: utf-8 -*-
"""In-house financing for HVAC customers - new spoke, daily batch 2026-11-13.

Search Console, Oct 14 - Nov 11 2026: "how to set up in house financing for hvac business"
28 impressions at position 19, landing on articles/how-to-finance-buy-hvac-business/ (an
acquisition guide). No HVAC page covers offering financing to homeowners (checked
hvac-business-financing.html, its three spokes, hvac-business-loans and the guide), so
the intent is distinct and the query is not split.

Scope: business-side guidance for a contractor deciding between referring customers to a
third-party consumer finance program and carrying the notes itself, and how the contractor
funds either. Not legal advice; the page says to use counsel.

Facts read from the rule text (Cornell LII and leg.state.fl.us): Reg Z 12 CFR
1026.2(a)(17) creditor test (finance charge or more than four installments; regularly =
more than 25 times a year, more than 5 if dwelling-secured); FTC Holder Rule 16 CFR 433.2
(notice in consumer credit contracts, including purchase money loans); FTC Cooling-Off
Rule 16 CFR 429.0 ($25+ at the buyer's home; buyer-initiated repair and emergency
exclusions); Florida Home Improvement Sales and Finance Act, Fla. Stat. 520.60-520.98,
license at 520.63, exemption for licensed trades incl. central heating and air-conditioning
installation at 520.68. No dealer-fee percentages quoted (no source); the worked example
uses stated assumptions and was computed by script. LOC 8-13% APR at banks: the site's
published range. No named lenders or finance programs.
"""
from cluster_table import table

REGZ = ("https://www.law.cornell.edu/cfr/text/12/1026.2", "12 CFR 1026.2: Regulation Z definitions",
        "Who counts as a creditor under the Truth in Lending Act, including the 25-transaction test.")
HOLDER = ("https://www.law.cornell.edu/cfr/text/16/433.2", "16 CFR 433.2: FTC Holder Rule",
          "The notice consumer credit contracts must carry when a seller finances or arranges financing.")
COOLING = ("https://www.law.cornell.edu/cfr/text/16/429.0", "16 CFR 429.0: FTC Cooling-Off Rule definitions",
           "When an in-home sale carries a three-day right to cancel, and the repair exclusions.")
FL_HI = ("http://www.leg.state.fl.us/statutes/index.cfm?App_mode=Display_Statute&URL=0500-0599/0520/0520PartVContentsIndex.html",
         "Florida Statutes 520.60-520.98: Home Improvement Sales and Finance",
         "Florida's rules for financed home improvement contracts, licensing (520.63) and exemptions (520.68).")

CLUSTER = {
    "pillar": "hvac-business-financing.html",
    "hub": "hvac-business-financing",
    "no_hub": True,
    "back_href": "/hvac-business-financing.html",
    "crumb": "HVAC Business Financing",
    "cta_inline": "Tell us how many jobs you finance a month",
    "cta_button": "Get Matched for HVAC Financing",
}

ARTICLES = [{
    "slug": "in-house-financing-for-hvac-customers",
    "crumb": "In-House Financing for HVAC Customers",
    "title": "In-House Financing for HVAC Customers: How to Set It Up",
    "og_title": "How to Set Up In-House Financing for HVAC Customers",
    "h1": "How to Set Up In-House Financing for HVAC Customers",
    "headline": "How to Set Up In-House Financing for HVAC Customers",
    "lede": "Third-party programs vs carrying the notes yourself, the federal and Florida rules "
            "that apply, and what a year of in-house notes does to your cash",
    "meta_desc": "How HVAC contractors set up in-house financing: third-party programs vs carrying "
                 "notes, Truth in Lending, the FTC Holder Rule, Florida rules and the cash it takes.",
    "article_desc": "How an HVAC company can offer financing to homeowners: third-party consumer "
                    "programs versus true in-house notes, the rules that apply, and how to fund it.",
    "keywords": "in house financing for hvac business, hvac customer financing, how to offer "
                "financing to hvac customers, hvac financing program for contractors, hvac in-house financing",
    "quick_answer": "As of November 2026, most HVAC companies that &ldquo;offer financing&rdquo; "
                    "refer customers to a third-party consumer lender, which pays the contractor and "
                    "carries the risk. True in-house financing makes you the lender: a creditor under "
                    "Truth in Lending once you extend credit <strong>more than 25 times</strong> a "
                    "year, and the cash for every system stays tied up. Four <strong>$12,000</strong> "
                    "notes a month is about $534,000 out after one year. Axiant Partners, a "
                    "business-loan broker in Boca Raton, funds the contractor side. Typical, not "
                    "legal advice.",
    "sections": [
        ("Two Ways to Offer HVAC Financing",
         table(["", "Third-party program", "True in-house notes"], [
             ["Who lends", "A consumer finance company", "Your company"],
             ["When you are paid", "Typically days after the job, less any plan fee", "Monthly, over the note's term"],
             ["Who carries default risk", "The lender, under its program terms", "You"],
             ["Compliance work", "Mostly the lender's; you follow its sales rules", "Yours: disclosures, contracts, collections"],
             ["Capital needed", "Little", "The full price of every financed system"],
             ["What you control", "Little: the lender approves the customer", "Rate, term and who gets approved"],
         ])
         + "<p>&ldquo;Promotional&rdquo; plans such as no interest for a period are usually paid for "
         "by the contractor through a fee taken from the funding. Ask each program for its fee "
         "schedule by plan in writing and price it into the job, the way you would a card fee.</p>"),
        ("The Rules That Apply When You Carry the Note",
         "<p>Offering consumer credit puts consumer-credit rules on your contracts. A summary, not "
         "legal advice; have a Florida attorney review your paperwork before the first note.</p>"
         "<ul>"
         "<li><strong>Truth in Lending (Regulation Z).</strong> You are a creditor if you regularly "
         "extend consumer credit that carries a finance charge or is payable in more than four "
         "installments. &ldquo;Regularly&rdquo; means more than 25 times in the prior or current "
         "calendar year, or more than 5 if the credit is secured by the home "
         "(<a href=\"https://www.law.cornell.edu/cfr/text/12/1026.2\" rel=\"noopener nofollow\" target=\"_blank\">12 "
         "CFR 1026.2(a)(17)</a>). Creditors give APR and finance-charge disclosures.</li>"
         "<li><strong>FTC Holder Rule.</strong> A consumer credit contract you take, or a purchase "
         "money loan you accept as payment, must carry the notice that lets the buyer raise claims "
         "against whoever holds the contract "
         "(<a href=\"https://www.law.cornell.edu/cfr/text/16/433.2\" rel=\"noopener nofollow\" target=\"_blank\">16 "
         "CFR 433.2</a>). It matters if you later sell your notes.</li>"
         "<li><strong>FTC Cooling-Off Rule.</strong> A sale of $25 or more made at the buyer&rsquo;s "
         "home generally carries a three-day right to cancel. Repairs the homeowner called you out "
         "for, and true emergencies with a signed waiver, are excluded "
         "(<a href=\"https://www.law.cornell.edu/cfr/text/16/429.0\" rel=\"noopener nofollow\" target=\"_blank\">16 "
         "CFR 429.0</a>). A replacement system sold on a maintenance visit may not be.</li>"
         "<li><strong>Florida.</strong> Installment contracts for home improvements fall under the "
         "Home Improvement Sales and Finance Act, Fla. Stat. 520.60-520.98: contract form, "
         "disclosures, finance charge limits and cancellation. The act licenses home improvement "
         "finance sellers (520.63), but 520.68 exempts licensed trades working within their "
         "license, and names installing central heating and air-conditioning as within it. Confirm "
         "how the rest of the act applies to your contracts.</li>"
         "</ul>"),
        ("Worked Example: What a Year of In-House Notes Ties Up",
         "<p><strong>Illustrative assumptions, not a quote.</strong> A contractor finances four "
         "$12,000 replacement systems a month for customers at 9.99% over 60 months, and funds them "
         "from a business line of credit at an assumed 11%. Computed by script.</p>"
         + table(["Item", "Amount"], [
             ["Customer payment per system", "About $254.91 a month"],
             ["Interest the customer pays over 60 months", "About $3,294 per system"],
             ["Notes outstanding after 12 months (48 systems)", "About $533,900"],
             ["Interest earned from customers in year one", "About $29,700"],
             ["Line of credit interest in year one at 11%", "About $32,700"],
         ])
         + "<p>Two lessons. First, the cash: after one year more than half a million dollars sits in "
         "customer notes instead of the bank. Second, the spread: charging customers less than your "
         "own cost of funds loses money before a single customer stops paying. In-house programs "
         "that work price the note above the contractor&rsquo;s funding cost and budget for "
         "defaults and collections.</p>"),
        ("How Contractors Fund the Program",
         "<ul>"
         "<li><strong>A business line of credit</strong>, commonly about 8-13% APR at banks, carries "
         "notes until they pay down. See <a href=\"/business-line-of-credit.html\">business line of "
         "credit</a>.</li>"
         "<li><strong>Selling the notes</strong> to a finance company that buys consumer paper, "
         "usually at a discount. Holder Rule notices travel with them.</li>"
         "<li><strong>A hybrid</strong>: third-party financing for most customers and in-house notes "
         "only for those the program declines, which keeps the book small.</li>"
         "<li><strong>For the business itself</strong>, separate from customer financing: "
         "<a href=\"/hvac-business-financing/financing-hvac-service-van/\">service vans</a>, "
         "<a href=\"/hvac-business-financing/hvac-parts-inventory-financing/\">parts inventory</a> and "
         "<a href=\"/hvac-business-financing/hvac-slow-season-cash-flow/\">slow-season cash flow</a>.</li>"
         "</ul>"),
        ("How to Set It Up, Step by Step",
         "<ol>"
         "<li><strong>Decide the model</strong>: third-party, in-house or hybrid. Most shops start "
         "third-party.</li>"
         "<li><strong>Compare two or three programs</strong> on approval rates in your market, plan "
         "fees, funding speed and how they handle declines.</li>"
         "<li><strong>If carrying notes</strong>, have counsel draft the contract, disclosures and "
         "cancellation notice, and set an approval standard you apply to everyone.</li>"
         "<li><strong>Line up the funding</strong> before the first note, sized to a year of volume, "
         "and decide when you would sell paper.</li>"
         "<li><strong>Train the sales team</strong> on what they may say about payments, and keep "
         "the financing offer separate from the equipment price.</li>"
         "</ol>"
         "<p>To size and fund the contractor side, <a href=\"/match.html\">get matched with lenders</a> "
         "or start from <a href=\"/hvac-business-financing.html\">HVAC business financing</a>.</p>"),
    ],
    "faqs": [
        ("How do HVAC companies offer financing to customers?",
         "Most refer customers to a third-party consumer finance program, which approves the "
         "homeowner, pays the contractor and carries the risk. A smaller number carry the notes "
         "themselves, which makes them the lender."),
        ("Do I need a license to offer in-house HVAC financing in Florida?",
         "Florida licenses home improvement finance sellers under Fla. Stat. 520.63, but 520.68 "
         "exempts licensed trades working within their license, including central heating and "
         "air-conditioning installation. The rest of the act's contract rules may still apply, so "
         "confirm with a Florida attorney."),
        ("Does Truth in Lending apply to an HVAC contractor's financing?",
         "If you regularly extend consumer credit with a finance charge or more than four "
         "installments, yes. Regularly means more than 25 times a year, or more than 5 if secured by "
         "the home, under 12 CFR 1026.2(a)(17)."),
        ("How much cash does in-house financing tie up?",
         "The full price of each financed system, paid back over the term. In the example on this "
         "page, four $12,000 notes a month leaves about $534,000 outstanding after one year."),
        ("Who pays for 0% financing offers on HVAC systems?",
         "Usually the contractor, through a fee the finance program deducts from the funding. Ask "
         "for the fee schedule by plan and price it into the job."),
        ("Can an HVAC company get a business loan to fund customer financing?",
         "Yes. A business line of credit is the common tool for carrying notes, and some contractors "
         "sell notes to a finance company. Price customer notes above your own cost of funds."),
    ],
    "related": [
        ("/hvac-business-financing.html", "HVAC business financing"),
        ("/articles/hvac-business-loans/", "HVAC business loans"),
        ("/hvac-business-financing/hvac-slow-season-cash-flow/", "HVAC slow season cash flow"),
        ("/business-line-of-credit.html", "Business line of credit"),
        ("/equipment-financing/articles/carecredit-vs-affirm/", "How patient financing programs compare"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [REGZ, HOLDER, COOLING, FL_HI],
}]
