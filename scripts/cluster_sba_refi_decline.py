# -*- coding: utf-8 -*-
"""SBA plan Clusters 5 and 6, two pages in sba-loans/articles/ (no_hub, like cluster_sba_mca_refi.py):

  what-debt-can-sba-loan-refinance   Appendix 14: eligible debt types, the 12-month current rule,
                                     the 10% payment improvement test and its exceptions, MCAs,
                                     factoring, seller notes, same-institution debt
  businesses-sba-lenders-decline     13 CFR 120.110 / SOP ineligible types vs eligible businesses
                                     many lenders still pass on, each with the Axiant page that fits

Rules read from SOP 50 10 8.1 (effective 2026-10-01; .docx downloaded from legacy.sba.gov on
2026-11-13): Appendix 14, Appendix 18 rate caps, Section A Ch. 2 Para. E (ineligible
businesses), Appendix 7 / Phase I for NAICS 457, start-up equity and projections. The lender
declines are framed as common practice, never as SBA rules, and no lender is named. Kept apart
from sba-504-refinance (504 only), refinancing-business-debt-guide (general consolidation),
sba-loan-denied-reasons-fix-before-reapplying (why an application failed) and
sba-loan-alternatives-when-you-dont-qualify (products by credit profile). Payments computed here.
"""
from cluster_table import table
from sba_sources import SOP, SBA_7A

SOP14 = (SOP[0], "SBA SOP 50 10 8.1, Appendix 14: 7(a) Debt Refinancing Requirements (effective October 1, 2026)",
         "Eligible debt types, the 12-month current rule, the 10% installment improvement test, and the "
         "rules for MCAs, factoring, seller notes and same-institution debt.")
SOPE = (SOP[0], "SBA SOP 50 10 8.1, Section A, Ch. 2: Types of Ineligible Businesses (effective October 1, 2026)",
        "The SBA's list of ineligible business types, with the limited exceptions, plus Appendix 7 on gas stations.")
CFR110 = ("https://www.law.cornell.edu/cfr/text/13/120.110",
          "13 CFR 120.110: What businesses are ineligible for SBA business loans?",
          "The regulation behind the SBA's ineligible business list.")
CFR201 = ("https://www.law.cornell.edu/cfr/text/13/120.201",
          "13 CFR 120.201: Is there a limit on refinancing?",
          "SBA loan proceeds may not pay a creditor in a position to sustain a loss.")

_SOP_A = ('<a href="' + SOP[0] + '" rel="noopener nofollow" target="_blank">SOP 50 10 8.1</a>')


def pmt(principal, rate, months):
    i = rate / 12
    return principal * i / (1 - (1 + i) ** -months)


def usd(x):
    return f"${x:,.0f}"


# 10% improvement worked example: two term debts into one 7(a) loan, 10.5% over 10 years
_DEBTS = [("Online term loan", 150_000, 6_200), ("3-year equipment loan", 85_000, 2_300)]
_OLD = sum(p for _, _, p in _DEBTS)
_BAL = sum(b for _, b, _ in _DEBTS)
_LIMIT = _OLD * 0.90
_NEW = pmt(_BAL, 0.105, 120)

_END = ('<p>Talk to an SBA specialist: <a href="tel:+15612680465">(561) 268-0465</a>, or '
        '<a href="/match.html">get matched with lenders</a>.</p>')

CLUSTER = {
    "pillar": "sba-loans.html",
    "hub": "sba-loans/articles",
    "no_hub": True,
    "back_href": "/sba-loans.html",
    "crumb": "SBA Loans",
    "cta_inline": "See if your debt qualifies",
    "cta_button": "Talk to an SBA Specialist",
}

ARTICLES = [{
    "slug": "what-debt-can-sba-loan-refinance",
    "crumb": "What Debt Can an SBA Loan Refinance?",
    "title": "What Debt Can an SBA Loan Refinance? 2026 Rules | Axiant",
    "og_title": "What Debt Can an SBA 7(a) Loan Refinance? The 2026 Rules",
    "h1": "What Debt Can an SBA 7(a) Loan Refinance? The 2026 Rules",
    "headline": "What Debt Can an SBA 7(a) Loan Refinance? The 2026 Rules",
    "lede": "Term loans, lines, credit cards and seller notes can qualify. MCAs and factoring mostly "
            "can't. The tests every refinance has to pass, from the SBA's own rulebook",
    "meta_desc": "What debt an SBA 7(a) loan can refinance in 2026: eligible debt types, the 12-month current rule, the 10% payment test, MCAs, factoring and seller notes.",
    "article_desc": "Which business debts an SBA 7(a) loan can refinance under SOP 50 10 8.1 Appendix "
                    "14, with the 10% payment improvement test and a worked example.",
    "keywords": "what debt can sba loan refinance, sba 7a debt refinance rules, sba refinance credit card "
                "debt, sba 10 percent payment improvement, refinance business debt with sba loan",
    "quick_answer": "Under SBA SOP 50 10 8.1, a 7(a) loan can refinance business term loans, balloon and "
                    "demand notes, lines of credit, business credit cards and HELOCs, and seller notes after "
                    "<strong>36 months</strong>. The debt must have been <strong>current for 12 months</strong>, "
                    "and in most cases the new payment must be at least <strong>10% lower</strong>. Active MCAs "
                    "and factoring don't qualify. Axiant Partners, a broker in Boca Raton, can check your debts "
                    "against the rules. Lenders also apply their own credit standards.",
    "sections": [
        ("Debt an SBA 7(a) Loan Can Refinance",
         f"<p>{_SOP_A}, Appendix 14, lists the business debt 7(a) proceeds can pay off. This page covers 7(a); "
         'refinancing a building through the 504 program has its own rules, covered in <a href="/sba-loans/articles/'
         'sba-504-refinance/">SBA 504 refinance</a>.</p>'
         + table(["Type of debt", "Eligible?", "Condition"], [
             ["Demand or balloon note", "Yes", "Exempt from the 10% payment test"],
             ["Rate above SBA maximum", "Yes", "Rate exceeds the SBA cap for its size or term; must pass the 10% payment test"],
             ["Maturity too short", "Yes", "Such as a 3-year loan on 15-year equipment; must pass the 10% payment test"],
             ["Over-collateralized debt", "Yes", "Judged against SBA collateral rules"],
             ["Revolving line of credit", "Yes", "If the lender won't renew it, or for a lower rate or longer term"],
             ["Business credit cards", "Yes", "You certify it was used only for the business"],
             ["Business-use HELOC", "Yes", "Same certification"],
             ["Seller note", "Yes", "After 36 months in place and current, not on standby"],
             ["Another lender's 7(a)", "Yes", "Subsidy recoupment fees may apply"],
             ["Merchant cash advance", "Only if converted", "Converted to a term loan and amortized 24+ months"],
             ["Factoring agreement", "No", "Not eligible"],
             ["SBIC or NMVC debt", "No", "Debt owed to an SBIC or New Markets Venture company; 13 CFR 120.130(b)"],
         ])
         + "<p>Debt on the business balance sheet also has to show on the business tax returns, with the "
         "interest expense, to be refinanced. Paying trade payables to suppliers isn't treated as debt "
         "refinancing under these rules.</p>"),
        ("The Two Tests Every Refinance Must Pass",
         "<ul>"
         "<li><strong>Current for 12 months.</strong> The debt must be current now and for the last 12 months, "
         "or its whole life if shorter. Current means no payment unpaid for more than 29 days. A loan that "
         "matured and wasn't paid within 29 days isn't eligible. The rule exists because "
         '<a href="https://www.law.cornell.edu/cfr/text/13/120.201" rel="noopener nofollow" target="_blank">13 '
         "CFR 120.201</a> bars SBA proceeds from paying a creditor that's about to take a loss.</li>"
         "<li><strong>10% lower payment.</strong> The new installment must be at least 10% less than the "
         "debts it replaces, added together. Escalating payments are measured against what's due in the next "
         "12 months. Balloon and demand notes, business credit cards, business HELOCs and lines the lender won't "
         "renew are exempt.</li>"
         "</ul>"
         "<p>Each lender also writes up why the debt was taken on, why it no longer fits, and how the new loan "
         "improves your position, with an itemized list of every creditor paid $10,000 or more.</p>"),
        ("Worked Example: Two Expensive Loans Into One",
         "<p><strong>Illustrative, not a quote.</strong> A contractor carries two term debts, both paid on time "
         "for over a year. The lender proposes one 7(a) loan for both balances at an assumed 10.5% over 10 years.</p>"
         + table(["Debt", "Balance", "Monthly payment"],
                 [[n, usd(b), usd(p)] for n, b, p in _DEBTS]
                 + [["<strong>Total</strong>", f"<strong>{usd(_BAL)}</strong>", f"<strong>{usd(_OLD)}</strong>"]])
         + table(["Test", "Result"], [
             ["Max new payment (90%)", usd(_LIMIT)],
             ["New 7(a) payment", f"About {usd(_NEW)} on {usd(_BAL)}"],
             ["Payment improvement", f"About {(_OLD - _NEW) / _OLD:.0%}, so it passes"],
         ])
         + "<p>A refinance from one cheap, long loan to another rarely clears 10%; one from short, high-rate "
         "debt usually does. Check the "
         '<a href="/sba-loans/articles/typical-sba-loan-rates-2026/">typical SBA loan rates</a> before you run '
         "your own numbers.</p>"),
        ("MCAs, Factoring and Other Hard Cases",
         "<ul>"
         "<li><strong>Merchant cash advances.</strong> An active sales-based agreement isn't eligible. It can be "
         "refinanced only after it's converted to a term loan, has amortized 24 months, and no new advances were "
         'taken since. <a href="/sba-loans/articles/can-you-refinance-mca-with-sba-loan/">Can you refinance an MCA '
         'with an SBA loan?</a> walks through it, and <a href="/mca-consolidation-loan.html">MCA consolidation</a> '
         "is the usual route meanwhile.</li>"
         "<li><strong>Factoring.</strong> Not eligible to refinance. A bank line or "
         '<a href="/invoice-factoring.html">a better factoring agreement</a> is the realistic swap.</li>'
         "<li><strong>Your own bank's debt.</strong> Allowed, but the lender must show 36 months of payment "
         "history and explain any late payments, and can't use the SBA to shift a likely loss.</li>"
         "<li><strong>An SBA 504 loan.</strong> A 7(a) can refinance one only if the bank first loan is paid off "
         "too, or as part of a larger expansion; prepayment penalties still apply.</li>"
         "<li><strong>Debt from an ineligible purpose.</strong> Not refinanceable unless the ineligibility no "
         "longer exists.</li>"
         "</ul>"),
        ("Rate Caps That Make Debt Eligible",
         "<p>One eligible type is debt priced above what an SBA loan of that size may charge. Appendix 18 caps "
         "variable 7(a) rates at the base rate plus a spread:</p>"
         + table(["7(a) loan amount", "Maximum variable rate"], [
             ["$50,000 or less", "Base rate + 6.5%"],
             ["$50,001 to $250,000", "Base rate + 6.0%"],
             ["$250,001 to $350,000", "Base rate + 4.5%"],
             ["Over $350,000", "Base rate + 3.0%"],
         ])
         + "<p>Most online term loans and card balances sit far above those caps. For a wider look at "
         'consolidating debt, SBA or not, see <a href="/refinancing-business-debt-guide/">business debt '
         'refinancing</a>, or the <a href="/sba-loans.html">SBA loans</a> overview.</p>'
         + _END),
    ],
    "faqs": [
        ("Can an SBA loan refinance business credit card debt?",
         "Yes. You certify that the card debt was used only for the business, and it's exempt from the 10% "
         "payment improvement test. It must also have been current."),
        ("What is the SBA 10% rule for refinancing?",
         "The new loan's installment must be at least 10% lower than the combined payments on the debt it "
         "replaces. Balloon and demand notes, business cards, business HELOCs and qualifying lines are exempt."),
        ("Can I refinance a loan I'm behind on with an SBA loan?",
         "Generally no. The debt must have been current for the last 12 months or its life, with no payment more "
         "than 29 days late."),
        ("Can an SBA 7(a) loan pay off a merchant cash advance?",
         "Not while it's active. Only an MCA converted to a term loan that has amortized at least 24 months, with "
         "no new advances since, can be refinanced."),
        ("Can I refinance a seller note with an SBA loan?",
         "Yes, once it has been in place and current, not on standby, for 36 months, and the refinance meets the "
         "10% improvement test."),
        ("Can an SBA loan refinance another SBA loan?",
         "A 7(a) can refinance another lender's 7(a) loan if the Appendix 14 conditions are met. Refinancing your "
         "own lender's 7(a) or a 504 loan has narrower rules."),
    ],
    "related": [
        ("/sba-loans.html", "SBA loans"),
        ("/sba-loans/articles/can-you-refinance-mca-with-sba-loan/", "Refinancing an MCA with an SBA loan"),
        ("/sba-loans/articles/sba-504-refinance/", "SBA 504 refinance"),
        ("/sba-loans/articles/businesses-sba-lenders-decline/", "Businesses SBA lenders often decline"),
        ("/refinancing-business-debt-guide/", "Business debt refinancing guide"),
        ("/business-acquisition-financing/articles/sba-seller-note-equity-injection-rules/", "SBA seller note rules"),
    ],
    "sources": [SOP14, CFR201, SBA_7A],
}, {
    "slug": "businesses-sba-lenders-decline",
    "crumb": "Businesses SBA Lenders Decline",
    "title": "Businesses SBA Lenders Decline, and Options | Axiant",
    "og_title": "Businesses SBA Lenders Often Decline, and Where to Go Instead",
    "h1": "Businesses SBA Lenders Often Decline, and Where to Go Instead",
    "headline": "Businesses SBA Lenders Often Decline, and Where to Go Instead",
    "lede": "Some businesses are barred by SBA rules. Many more are eligible but turned down by most "
            "SBA lenders. Telling the two apart decides where to apply next",
    "meta_desc": "Which businesses the SBA won't finance under 13 CFR 120.110, which ones lenders often decline anyway (gas stations, bars, vape shops), and the alternative for each.",
    "article_desc": "SBA-ineligible business types under 13 CFR 120.110 and SOP 50 10 8.1, the "
                    "eligible businesses many SBA lenders still decline, and alternatives for each.",
    "keywords": "businesses not eligible for sba loans, sba ineligible businesses list, sba loan gas station, "
                "sba loan restaurant bar, sba loan vape shop, why sba lenders decline",
    "quick_answer": "Two different lists. The SBA bars certain types outright under 13 CFR 120.110, such as "
                    "lenders, passive real estate landlords, apartment buildings, gambling-led businesses and "
                    "cannabis. Many other businesses are <strong>eligible</strong> but declined by most SBA "
                    "lenders, such as gas stations, restaurants and bars, vape shops and delivery routes. Those can "
                    "still find a lender. Axiant Partners, a broker in Boca Raton, finds the lenders that say yes.",
    "sections": [
        ("Ineligible Under SBA Rules",
         f"<p>{_SOP_A} lists the types no 7(a) or 504 lender can finance, for any purpose, including buying a "
         "building for the business's own use. The main ones:</p>"
         + table(["Ineligible type", "Note"], [
             ["Lenders and finance cos.", "Banks, finance, factoring and bail bond companies; pawn shops and check cashers can qualify on revenue mix"],
             ["Passive real estate", "Landlords, developers, property held to lease; apartment buildings and mobile home parks included; hotels qualify with 50%+ stays of 30 days or less"],
             ["Life insurance carriers", "Independent agents are eligible"],
             ["Pyramid or multilevel", "Pyramid or multilevel sales plans"],
             ["Gambling-led businesses", "Over one-third of revenue from gambling; casinos and skill-game businesses at any share"],
             ["Illegal activity", "Illegal under federal, state or local law; includes marijuana businesses; hemp and CBD only within federal law and FDA rules"],
             ["Prurient sexual content", "Over 5% of revenue"],
             ["Restricted patronage", "Or discriminatory hiring"],
             ["Government or political", "Government-owned, political or lobbying businesses; tribe-owned businesses can qualify"],
             ["Speculative businesses", "Including R&D, oil wildcatting and spec homes outside Builders CAPLines"],
             ["Prior loss to government", "Unless fully satisfied"],
             ["Abroad or Coastal Barrier", "Located outside the U.S. or in the Coastal Barrier Resources System"],
         ])
         + "<p>If your business is on this list, no SBA lender can help, and the question is which non-SBA "
         'product fits. <a href="/real-estate-secured-business-loan.html">Real estate secured loans</a> and '
         '<a href="/business-term-loans.html">conventional term loans</a> are the usual starting points.</p>'),
        ("Eligible, but Often Declined",
         "<p>These are SBA-eligible businesses that many SBA lenders exclude under their own credit policy. "
         "Lenders differ, which is the reason to shop the deal. Typical reasons and realistic options:</p>"
         + table(["Business", "Why lenders hesitate", "Where to look instead"], [
             ["Gas stations and USTs", "Underground tank contamination risk; SBA requires a Phase I for NAICS 457 and Appendix 7 review",
              '<a href="/sba-loans/articles/gas-station-convenience-store-financing/">Lenders that do gas stations</a>, '
              '<a href="/real-estate-secured-business-loan.html">real estate secured</a>'],
             ["Restaurants and bars", "Thin margins, high failure rates, alcohol liability",
              '<a href="/restaurants-business-financing.html">Restaurant financing</a>, '
              '<a href="/working-capital-loans/articles/restaurant-working-capital/">restaurant working capital</a>'],
             ["Vape and smoke shops", "Fast-changing regulation and product bans", '<a href="/revenue-based-financing.html">Revenue-based financing</a>'],
             ["Delivery routes", "FedEx-style contracts: revenue depends on one contract that can end",
              '<a href="/equipment-financing/articles/sprinter-van-financing-last-mile-delivery/">Delivery van financing</a>'],
             ["Fleet-heavy companies", "Depreciating vehicles carry the collateral",
              '<a href="/trucking-business-financing/small-fleet-truck-financing-under-10-trucks/">Fleet truck financing</a>, '
              '<a href="/commercial-truck-title-loan.html">truck title loans</a>'],
             ["Projections-only start-ups", "No cash flow history to underwrite", '<a href="/startup-financing.html">Startup financing</a>'],
             ["Standalone working capital", "No hard asset behind the loan",
              '<a href="/business-line-of-credit.html">Lines of credit</a>, '
              '<a href="/invoice-factoring.html">invoice factoring</a>'],
         ])),
        ("What the SBA Rules Actually Allow for These",
         "<ul>"
         "<li><strong>Start-ups.</strong> SBA allows them. A business operating a year or less needs at least "
         "10% equity, and projections must show debt service coverage of 1.15 within two years. Many lenders "
         "still want industry experience and some history.</li>"
         "<li><strong>Working capital.</strong> Eligible. When 50% or more of the proceeds are working capital, "
         "the lender has to justify it in the credit memo, which is one reason many avoid it.</li>"
         "<li><strong>Gas stations.</strong> Eligible, but the environmental investigation must start with a "
         "Phase I, which adds cost and time and can uncover cleanup.</li>"
         "<li><strong>Restaurants and bars.</strong> Eligible if they don't restrict patronage. A restaurant "
         "employing servers of only one gender is the SOP's own example of an ineligible one.</li>"
         "<li><strong>Credit elsewhere.</strong> Every SBA lender must certify you can't get the money on "
         "reasonable terms without the SBA. A strong borrower may be told to use a conventional loan.</li>"
         "</ul>"),
        ("Declined Once? Separate the Two Kinds of No",
         "<p>A \"no\" because your business type is ineligible is final across all SBA lenders. A \"no\" based on "
         "credit policy only covers that lender. If you were declined for cash flow, credit or missing "
         'paperwork, <a href="/sba-loans/articles/sba-loan-denied-reasons-fix-before-reapplying/">SBA loan denial '
         "reasons</a> explains how to fix the file; if SBA simply isn't the right product, "
         '<a href="/sba-loans/articles/sba-loan-alternatives-when-you-dont-qualify/">SBA loan alternatives</a> '
         "compares the options by credit profile.</p>"
         "<p>Three questions get to the bottom of a decline:</p>"
         "<ol>"
         "<li><strong>Was it the business type or the file?</strong> Ask which policy it failed.</li>"
         "<li><strong>Is the problem the collateral?</strong> If yes, adding real estate or a "
         '<a href="/sba-100-percent-financing.html">building purchase</a> can change the answer.</li>'
         "<li><strong>Is debt the real issue?</strong> If you have stacked advances, an SBA loan probably can't "
         'pay them off yet; see <a href="/sba-loans/articles/what-debt-can-sba-loan-refinance/">what debt an SBA '
         "loan can refinance</a>.</li>"
         "</ol>"
         + _END),
    ],
    "faqs": [
        ("What businesses are not eligible for SBA loans?",
         "Under 13 CFR 120.110: lenders and finance companies, passive real estate businesses, life insurers, "
         "pyramid sales, businesses with over one-third of revenue from gambling, illegal businesses, prurient "
         "businesses, government-owned and political businesses, speculative businesses and a few more."),
        ("Can a gas station get an SBA loan?",
         "Yes, gas stations are eligible, but the environmental review must begin with a Phase I and follow SBA's "
         "gas station appendix. Many SBA lenders decline them as policy, so it takes the right lender."),
        ("Can a restaurant or bar get an SBA loan?",
         "Yes, they're eligible. Many SBA lenders limit or avoid them because of failure rates and liability, "
         "so approval depends heavily on the lender and on cash flow history."),
        ("Can a cannabis business get an SBA loan?",
         "Marijuana businesses generally can't, because federal law still prohibits marijuana. Hemp and CBD "
         "businesses can qualify only if their products meet federal law and FDA rules."),
        ("Can an apartment building get an SBA loan?",
         "No. Apartment buildings, mobile home parks and businesses that own real estate to lease are passive "
         "businesses and ineligible. Hotels can qualify if most revenue comes from stays of 30 days or less."),
        ("If one SBA lender declines my business, will all of them?",
         "Only if the business type is ineligible under SBA rules. A decline based on lender policy only reflects "
         "that lender, and others may approve it."),
    ],
    "related": [
        ("/sba-loans.html", "SBA loans"),
        ("/sba-loans/articles/sba-loan-denied-reasons-fix-before-reapplying/", "SBA loan denied: reasons and fixes"),
        ("/sba-loans/articles/sba-loan-alternatives-when-you-dont-qualify/", "SBA loan alternatives"),
        ("/sba-loans/articles/what-debt-can-sba-loan-refinance/", "What debt an SBA loan can refinance"),
        ("/real-estate-secured-business-loan.html", "Real estate secured business loans"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOPE, CFR110, SBA_7A],
}]
