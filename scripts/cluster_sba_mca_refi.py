# -*- coding: utf-8 -*-
"""Can you refinance an MCA with an SBA loan? - SBA plan Cluster 5, spoke 2.

Search Console, Oct 7 to Nov 4 2026: "refinance merchant cash advance with sba loan" 1
impression at position 5, on a page that wrongly said yes; the wider "refinance merchant cash
advance" is 30 at 21 and "mca debt refinancing" 25 at 19. Thin direct demand, shipped because
the plan calls it a strong AEO question and the site's own pages contradicted the SOP. Rule read
from SOP 50 10 8.1, Appendix 14 on 2026-11-07: active sales-based agreements are ineligible, and
converted ones need 24 months of amortization. Never names the program lender. no_hub.
"""
from cluster_table import table
from sba_sources import SOP, SBA_7A

PN2024 = ("https://starfieldsmith.com/2024/12/best-practices-refinancing-mca-debt/",
          "Starfield & Smith: Refinancing MCA Debt (December 2024)",
          "Law-firm summary of Procedural Notice 5000-862692, which briefly allowed MCA refinancing.")
SOP8 = ("https://starfieldsmith.com/2025/04/best-practices-sba-issues-sop-50-10-8/",
        "Starfield & Smith: SBA Issues SOP 50 10 8 (April 2025)",
        "Law-firm summary of the June 2025 SOP, which made MCAs and factoring ineligible for refinancing.")
FTC = ("https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic",
       "FTC: Protecting Small Businesses Seeking Financing",
       "FTC guidance on misrepresented financing costs and terms offered to small businesses.")

_SOP_A = ('<a href="' + SOP[0] + '" rel="noopener nofollow" target="_blank">SOP 50 10 8.1</a>')

CLUSTER = {
    "pillar": "sba-loans.html",
    "hub": "sba-loans/articles",
    "no_hub": True,
    "back_href": "/sba-loans.html",
    "crumb": "SBA Loans",
    "cta_inline": "See which way out fits your MCA",
    "cta_button": "Talk to an SBA Specialist",
}

ARTICLES = [{
    "slug": "can-you-refinance-mca-with-sba-loan",
    "crumb": "Refinance an MCA With an SBA Loan?",
    "title": "Can You Refinance an MCA With an SBA Loan? | Axiant",
    "og_title": "Can You Refinance a Merchant Cash Advance With an SBA Loan?",
    "h1": "Can You Refinance a Merchant Cash Advance With an SBA Loan?",
    "headline": "Can You Refinance a Merchant Cash Advance With an SBA Loan?",
    "lede": "Not while it's active. The SBA rule since October 2026, the narrow exception, and where to go "
            "if your advance doesn't qualify",
    "meta_desc": "Generally no: an active MCA can't be refinanced with an SBA 7(a) loan unless converted to a term loan and amortized 24 months. See the rule and your options.",
    "article_desc": "SBA's current rule on refinancing merchant cash advances under SOP 50 10 8.1, the "
                    "conversion exception, and the alternatives for an active advance.",
    "keywords": "refinance merchant cash advance with sba loan, can you refinance an mca with an sba loan, "
                "sba mca refinance rule, sop 50 10 8.1 merchant cash advance, sales-based repayment agreement",
    "quick_answer": "Generally <strong>no</strong>. Under SBA's SOP 50 10 8.1, effective October 1, 2026, an active "
                    "merchant cash advance isn't eligible for 7(a) refinancing. The exception: it was converted to a "
                    "term loan, has amortized for at least <strong>24 months</strong>, and no new agreements have been "
                    "added since. Factoring isn't eligible at all. Axiant Partners, a business-loan broker in Boca "
                    "Raton, can match you with non-SBA ways out. Lender requirements can go beyond these minimums.",
    "sections": [
        ("What the SBA Rule Says",
         "<p>Appendix 14 of " + _SOP_A + " covers 7(a) debt refinancing. It calls an MCA a "
         "<em>sales-based repayment agreement</em>: a cash advance repaid from a percentage of future sales. The "
         "key sentence is direct: these agreements are only eligible if the original agreement "
         "“has been converted to a term loan, has amortized for at least 24 months, and no additional "
         "Agreements have been implemented since the conversion.” If the agreement is still active, it isn't "
         "eligible. A separate line says factoring agreements aren't eligible either.</p>"
         + table(["Your situation", "Eligible for 7(a) refinance?", "Why"], [
             ["Active MCA", "No", "Still a live sales-based agreement"],
             ["Stacked MCAs", "No", "Each one is still active"],
             ["Converted 10 months ago", "Not yet", "Under 24 months of amortization"],
             ["Converted 24+ months ago", "Possibly", "If no new advances, and other tests pass"],
             ["Converted, new advance", "No", "A new agreement breaks the condition"],
             ["Factoring agreement", "No", "Listed as not eligible"],
         ])),
        ("Why You May Have Read the Opposite",
         "<p>Older guides, including some older pages on this site, said SBA could pay off MCAs, because the rule "
         "has changed three times in about two years. Confirm which version any source is describing.</p>"
         + table(["Effective", "Document", "Position on MCAs"], [
             ["December 6, 2024", "Procedural Notice 5000-862692", "Eligible to refinance"],
             ["June 1, 2025", "SOP 50 10 8", "Not eligible"],
             ["October 1, 2026", "SOP 50 10 8.1", "Only if converted, amortized 24 months, no new agreements"],
         ])
         + "<p>Version 8.1 applies to applications issued an SBA loan number on or after October 1, 2026. If someone "
         "promises an SBA payoff of an active advance, ask them to show you the section. Lender overlays can be "
         "stricter than the SOP, and they can differ, but no lender can make an ineligible use of proceeds eligible.</p>"),
        ("The Other Tests a Converted MCA Must Pass",
         "<p>Meeting the 24-month condition only gets the debt to the starting line. The general refinance rules in "
         "Appendix 14 apply as well:</p>"
         "<ul>"
         "<li><strong>Current for 12 months.</strong> The debt must have been current for the last 12 months or its "
         "life, whichever is less. A payment unpaid for more than 29 days isn't current.</li>"
         "<li><strong>No creditor in a position to lose.</strong> Proceeds can't pay a creditor that would otherwise "
         "take a loss, so settled or workout balances raise questions.</li>"
         "<li><strong>10% lower payment.</strong> The new installment must generally be at least 10% below the existing "
         "installments, in aggregate. An existing $4,000 monthly payment would need to fall to $3,600 or less.</li>"
         "<li><strong>A written case.</strong> The lender must document why the debt was taken on, why restructuring "
         "helps, and itemize creditors being paid $10,000 or more.</li>"
         "<li><strong>On your tax returns.</strong> Debt on the balance sheet needs to appear on the business return "
         "with its interest expense.</li>"
         "</ul>"
         "<p>Ask for the conversion in writing as a real term loan with a fixed schedule. A modified holdback percentage "
         "may not be a conversion at all, so have the lender read the agreement before you count months.</p>"),
        ("What to Do With an Active MCA",
         "<p>You can't wait 24 months on a debit that's choking the business, so the realistic paths are outside SBA:</p>"
         + table(["Option", "Fits when", "Watch for"], [
             ['<a href="/mca-consolidation-loan.html">MCA consolidation</a>', "You're current and the deposits support one payment", "Compare the total repayment, not just the payment"],
             ['<a href="/merchant-cash-advance/articles/refinance-mca-to-term-loan-30-day-playbook/">Non-SBA term loan</a>', "You have enough credit and time in business", "Most need solid history and clean statements"],
             ['<a href="/real-estate-secured-business-loan.html">Real estate loan</a>', "You own property with equity", "Your property is at risk if you default"],
             ['<a href="/commercial-truck-title-loan.html">Truck-secured loan</a>', "You own titled trucks free and clear", "The truck is the collateral"],
             ['<a href="/business-debt-relief.html">Debt relief</a>', "You can't keep up with the debits", "Fees, and the effect of stopping payments"],
         ])
         + "<p>Illustrative math from our <a href=\"/merchant-cash-advance/articles/refinance-mca-to-term-loan-30-day-playbook/\">"
         "refinance playbook</a>: $100,000 at 12% over five years is about $2,224 a month, against roughly $10,400 in daily "
         "debits on the advance in that example. These aren't quotes, and the "
         '<a href="https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic" '
         'rel="noopener nofollow" target="_blank">FTC</a> has warned funders against misrepresenting terms, so get every '
         "figure in writing. For more on the exit itself, read "
         '<a href="/merchant-cash-advance/articles/how-to-get-out-of-an-mca/">how to get out of an MCA</a>.</p>'),
        ("Can You Get an SBA Loan for Something Else While You Have an MCA?",
         "<p>This is a different question, and it's often missed. The appendix limits what proceeds can refinance. Having "
         "an advance isn't, by itself, the same as being barred from an SBA loan, but the debits reduce the cash flow a "
         "lender can count and may be treated as a warning sign. Lenders vary widely here. Many will want the advance "
         "gone, or will decline until it is. See "
         '<a href="/sba-loans/articles/sba-loan-alternatives-when-you-dont-qualify/">SBA loan alternatives</a> if you get a no, '
         "and <a href=\"/sba-loans/articles/sba-loan-denied-reasons-fix-before-reapplying/\">why SBA loans get denied</a> before you reapply.</p>"),
        ("A Plan That Leads Back to SBA",
         "<ol>"
         "<li><strong>List every agreement.</strong> Note the funder, balance, debit, and whether it's still sales-based.</li>"
         "<li><strong>Stop adding.</strong> Any new agreement after a conversion breaks the condition.</li>"
         "<li><strong>Exit or convert.</strong> Use one of the options above, and get any conversion in writing.</li>"
         "<li><strong>Stay current.</strong> Keep 12 clean months, because a payment over 29 days late counts against you.</li>"
         "<li><strong>Revisit SBA later.</strong> Lower-cost, longer-term debt may be open once the file is clean.</li>"
         "</ol>"
         '<p>Talk to an SBA specialist at <a href="tel:+15612680465">(561) 268-0465</a>, or '
         '<a href="/match.html">get matched</a> and we can review which path your file supports. See the '
         '<a href="/sba-loans.html">SBA loans overview</a> for the wider program.</p>'),
    ],
    "faqs": [
        ("Can you refinance a merchant cash advance with an SBA loan?",
         "Generally no. Under SOP 50 10 8.1, effective October 1, 2026, an active MCA isn't eligible for 7(a) refinancing. "
         "It's eligible only if it was converted to a term loan, has amortized for at least 24 months, and no additional "
         "agreements have been added since."),
        ("Can SBA loans pay off factoring?",
         "No. Appendix 14 of SOP 50 10 8.1 says factoring agreements are not eligible for refinancing."),
        ("Didn't SBA allow MCA refinancing?",
         "Briefly. A notice effective December 6, 2024 allowed it. SOP 50 10 8 removed it on June 1, 2025, and SOP 50 10 8.1 "
         "added the narrow conversion path on October 1, 2026."),
        ("What counts as converting an MCA to a term loan?",
         "The SOP doesn't give a checklist beyond requiring the agreement to be converted to a term loan and to amortize. "
         "Expect a lender to read the document, and don't assume a lower holdback or a payment plan qualifies."),
        ("Does stacking affect the rule?",
         "Yes. Each active agreement is ineligible, and a new agreement after a conversion breaks the condition."),
        ("What are my options if my MCA doesn't qualify?",
         "Common options are an MCA consolidation loan, a non-SBA term loan, a loan secured by real estate or a truck you own, "
         "or a restructuring. Each has its own cost and risk, so compare the total repayment."),
    ],
    "related": [
        ("/mca-consolidation-loan.html", "MCA consolidation loans"),
        ("/merchant-cash-advance/articles/refinance-mca-to-term-loan-30-day-playbook/", "Refinance an MCA to a term loan"),
        ("/merchant-cash-advance/articles/how-to-get-out-of-an-mca/", "How to get out of an MCA"),
        ("/sba-loans/articles/sba-loan-alternatives-when-you-dont-qualify/", "SBA loan alternatives"),
        ("/sba-loans.html", "SBA loans"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, SBA_7A, PN2024, SOP8, FTC],
}]
