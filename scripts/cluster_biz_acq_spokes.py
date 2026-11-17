# -*- coding: utf-8 -*-
"""SBA plan Cluster 4 spokes under business-acquisition-financing/articles/ (no Articles index
there, so no_hub, same as cluster_biz_acq.py):

  sba-seller-note-equity-injection-rules  the Appendix 15 rulebook: equity by transaction type,
                                          what counts, seller notes, standby, valuation gap
  buy-a-competitor-sba-loan               Business Expansion: same 4-digit NAICS, equity the
                                          lender may waive, 1.15 coverage
  large-business-acquisition-loan         $1M-$5M purchases: QoE at $3M, fully secured haircuts,
                                          personal real estate, life insurance, pari passu over $5M

Every rule read from SOP 50 10 8.1 (effective 2026-10-01; the .docx downloaded from
legacy.sba.gov on 2026-11-13): Appendix 15 (changes of ownership), the life insurance paragraph,
Appendix 18 rate caps. Every payment, coverage and collateral figure computed in this module.
Angles kept apart from buy-a-business-with-5-percent-down (one structure, worked through),
how-much-down-payment-required-sba-loan (down payment by use) and
where-sba-loan-down-payment-can-come-from (sources of cash). Never names the program lender.
"""
from cluster_table import table
from sba_sources import SOP, FEES, SBA_7A, EQ

SOP15 = (SOP[0], "SBA SOP 50 10 8.1, Appendix 15: 7(a) Changes of Ownership (effective October 1, 2026)",
         "Transaction types, equity injection by type, seller debt and standby rules, valuation, "
         "Quality of Earnings, debt service coverage and collateral for acquisitions.")
NAICS = ("https://www.census.gov/naics/?input=2382&year=2022&details=2382",
         "U.S. Census Bureau: NAICS 2382, Building Equipment Contractors",
         "The four-digit industry group that holds electrical (238210) and plumbing/HVAC (238220) contractors.")
LLL = ("https://www.law.cornell.edu/cfr/text/12/32.3",
       "12 CFR 32.3: Lending limits",
       "A national bank's limit on loans to one borrower: 15% of capital and surplus, plus 10% more if fully secured by readily marketable collateral.")

_SOP_A = ('<a href="' + SOP[0] + '" rel="noopener nofollow" target="_blank">SOP 50 10 8.1</a>')
_FEE_A = ('<a href="' + FEES[0] + '" rel="noopener nofollow" target="_blank">FY2027 fee notice</a>')


def pmt(principal, rate, months):
    i = rate / 12
    return principal * i / (1 - (1 + i) ** -months)


def usd(x):
    return f"${x:,.0f}"


# --- rulebook: minimum equity by project size (10% total, at least half unlimited sources) ---
_TIERS = [500_000, 1_500_000, 3_000_000]
_TIER_ROWS = [[usd(p), usd(p * .10), usd(p * .05), usd(p * .05)] for p in _TIERS]

# --- competitor: the same $300,000 of cash flow at 1.15 vs 1.25, 10.5% over 10 years ---
_CF = 300_000
_RATE, _N = 0.105, 120
_PER_DOLLAR = pmt(1, _RATE, _N) * 12
_COMP = {d: (_CF / d, _CF / d / _PER_DOLLAR) for d in (1.15, 1.25)}
_TARGET = 1_200_000
_TARGET_PMT = pmt(_TARGET, _RATE, _N)

# --- large deal: $3.5M purchase, 10% equity, collateral haircuts from Appendix 15 C.3.c ---
_PRICE = 3_500_000
_LOAN = _PRICE * 0.90
_EQUIP, _AR, _INV, _FF = 600_000, 400_000, 300_000, 100_000
_C_EQUIP = _EQUIP * 0.50
_C_TRADE = (_AR + _INV) * 0.10
_C_FF = _FF * 0.10
_COLL = _C_EQUIP + _C_TRADE + _C_FF
_SHORT = _LOAN - _COLL
_HOME, _MORT = 900_000, 400_000
_HOME_EQ = _HOME - _MORT
_SHORT2 = _SHORT - _HOME_EQ
_BIG_PMT = pmt(_LOAN, _RATE, _N)
_BIG_CF = _BIG_PMT * 12 * 1.25

CLUSTER = {
    "pillar": "business-acquisition-financing.html",
    "hub": "business-acquisition-financing/articles",
    "no_hub": True,
    "back_href": "/business-acquisition-financing.html",
    "crumb": "Business Acquisition Financing",
    "cta_inline": "Check how your purchase would be structured",
    "cta_button": "Talk to an SBA Specialist",
}

_END = ('<p>Talk to an SBA specialist: <a href="tel:+15612680465">(561) 268-0465</a>, or '
        '<a href="/match.html">get matched with acquisition lenders</a>.</p>')

ARTICLES = [{
    "slug": "sba-seller-note-equity-injection-rules",
    "crumb": "SBA Equity Injection and Seller Note Rules",
    "title": "SBA Seller Note and Equity Injection Rules | Axiant",
    "og_title": "SBA Equity Injection and Seller Note Rules for Buying a Business (2026)",
    "h1": "SBA Equity Injection and Seller Note Rules for Buying a Business (2026)",
    "headline": "SBA Equity Injection and Seller Note Rules for Buying a Business (2026)",
    "lede": "The change-of-ownership rulebook in one place: how much equity each type of deal needs, "
            "what can count, and when a seller note counts as equity or as debt",
    "meta_desc": "SBA equity injection rules for acquisitions under SOP 50 10 8.1: 10% by deal type, what counts, seller notes on full standby, the valuation gap and refinancing.",
    "article_desc": "The SBA's 2026 equity injection and seller note rules for business acquisitions, "
                    "by transaction type, from SOP 50 10 8.1 Appendix 15.",
    "keywords": "sba equity injection rules, sba seller note rules, seller note full standby, sba "
                "seller note equity injection 2026, sba change of ownership equity, sba standby agreement",
    "quick_answer": "Under SBA SOP 50 10 8.1 (effective October 1, 2026), every 7(a) business purchase "
                    "starts at <strong>10% equity</strong> of total project cost. At least half must be "
                    "unborrowed cash or other unlimited sources. A seller note counts toward the other "
                    "half only on <strong>full standby</strong>, with no payments for the life of the loan. "
                    "Only Business Expansions and Owner Buyouts can have the 10% reduced or waived. "
                    "Axiant Partners, a business-loan broker in Boca Raton, can find lenders for each structure.",
    "sections": [
        ("Minimum Equity by Type of Deal",
         f"<p>{_SOP_A}, Appendix 15, sorts every purchase into one of four types. Initial Acquisition is "
         "the default; the lender has to document why a deal fits any of the others. The type sets the "
         "equity, the cash flow test and whether the seller can stay. This is the rule table; for one "
         "structure worked through end to end, see "
         '<a href="/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/">buying '
         "a business with 5% down</a>.</p>"
         + table(["Deal type", "Who it fits", "Minimum equity", "Can lender waive it?", "Coverage"], [
             ["Initial Acquisition", "A new majority or largest owner, or an employee of under 24 months",
              "10% of total project cost", "No", "1.25 to 1"],
             ["Business Expansion", "An operating business, 2+ fiscal years under current owners, buying 100% of a business in its 4-digit NAICS group",
              "10% of total project cost", "Yes, with enough liquidity and no negative net worth", "1.15 to 1"],
             ["Owner Buyout", "Existing owners or 24-month employees buying out a partner",
              "10% of the purchase price", "Yes, same test", "1.25 to 1"],
             ["ESOP or cooperative", "An ESOP or co-op buying 51% or more",
              "None for an ESOP buying control", "Not applicable", "1.25 to 1"],
         ])
         + "<p>Total project cost means all costs to become operational, whatever the source of funds, "
         "except lines of credit and 504 loans. Real estate bought in the same deal follows the same "
         "equity rules; split into two loans, the equity is allocated pro rata, and a 504 for the "
         "building follows 504 equity rules instead.</p>"),
        ("What Counts as Equity, and How Much of Each",
         "<p>The SOP splits sources into two buckets. Unlimited sources can cover all of the "
         "requirement. Limited sources, alone or together, can cover no more than half of it.</p>"
         + table(["Bucket", "Sources the SOP lists", "Cap"], [
             ["Unlimited", "Cash that isn't borrowed (including a gift); a personal loan to a guarantor repaid from outside the business; grants with no clawback; verified prepaid expenses", "None"],
             ["Limited", "Debt on full standby, including a seller note; non-controlling minority investors under 20% with no control", "Half of the required equity, combined"],
             ["Not equity", "Fees paid to an agent, education or advisory costs; seller debt with payments", "Doesn't count"],
         ])
         + "<p>On a deal's required equity, that works out like this:</p>"
         + table(["Total project cost", "10% minimum", "At least this from unlimited sources", "At most this on standby"], _TIER_ROWS)
         + "<p>Money spent on the lender's business valuation or Quality of Earnings report counts toward "
         "the injection, because the SOP treats it as the buyer's out-of-pocket due diligence. Our guide to "
         '<a href="/sba-loans/articles/where-sba-loan-down-payment-can-come-from/">where the down payment can '
         "come from</a> covers documenting gifts and retirement rollovers.</p>"),
        ("The Seller Note: Equity or Debt?",
         "<p>The same promissory note is treated two very different ways depending on its payment terms.</p>"
         "<ul>"
         "<li><strong>Full standby.</strong> No principal or interest for the term of the 7(a) loan. It "
         "counts as equity, up to the half cap. It can accrue interest and be paid after the 7(a) loan is "
         "repaid. The lender uses SBA Form 155 or its own standby agreement with the note attached, the "
         "seller subordinates its liens, and it can't act against the borrower without the lender's "
         "consent. A standby creditor can't also take an equity stake.</li>"
         "<li><strong>Payments from day one.</strong> It's debt, not equity. Its payments go into the cash "
         "flow test, and if it is interest-only, the lender has to underwrite it on an amortization of no "
         "more than 10 years.</li>"
         "<li><strong>Refinancing it later.</strong> Seller debt from the purchase can be refinanced once it "
         "has been in place and current, not on standby, for 36 months, and the new payment is at least 10% "
         "lower. See <a href=\"/sba-loans/articles/what-debt-can-sba-loan-refinance/\">what debt an SBA loan "
         "can refinance</a>.</li>"
         "</ul>"
         "<p>Earnouts to the seller are prohibited. Buyer rebates tied to performance are allowed, but the "
         "money has to pay down the 7(a) loan. A working capital true-up isn't a rebate and can stay in the "
         "business.</p>"),
        ("When the Price Is Higher Than the Valuation",
         "<p>A lender-ordered business valuation must support the Business Purchase Price, which excludes "
         "owner-occupied real estate. Debt that supports the purchase, including seller debt not on full "
         "standby, is capped at the valuation. If the buyer pays more, the difference must be made up by "
         "equity. Here the SOP lets limited sources go past the usual half cap, but only on full standby.</p>"
         "<p>Example: the seller wants $2,000,000 and the valuation comes in at $1,800,000. The $200,000 "
         "gap can't be lent by the bank or carried as an amortizing seller note. The buyer brings it as cash, "
         "the seller carries it on full standby, or the price comes down. A Quality of Earnings report "
         "that lowers earnings can shrink the supportable loan the same way.</p>"
         "<ul>"
         "<li>The valuation must be ordered by and prepared for the lender. Above a $350,000 purchase price it "
         "must come from an accredited appraiser (ASA, CBA, ABV, CVA or BCA).</li>"
         "<li>At $3 million and up, Initial Acquisitions and Business Expansions also need a QoE.</li>"
         "</ul>"),
        ("Partial Buyouts and When the Seller Can Stay",
         "<p>In an Initial Acquisition or Business Expansion the seller must leave, apart from a consulting "
         "contract of up to 24 months in total. In a partial change of ownership the seller can remain. "
         "Then every new direct or indirect owner, however small, joins the loan as co-borrower. A selling "
         "owner who keeps under 20% gives a full guaranty for at least two years after final disbursement. "
         "Someone employed under 24 months can't buy 50% or more, or become the largest owner, through a "
         "buyout without falling back to Initial Acquisition standards. "
         '<a href="/sba-loans/articles/sba-loan-buy-out-business-partner/">Buying out a partner</a> has the '
         "details.</p>"
         + _END),
    ],
    "faqs": [
        ("What is the SBA equity injection for buying a business in 2026?",
         "10% of total project cost for an Initial Acquisition, Business Expansion or ESOP-related deal, "
         "and 10% of the purchase price for an Owner Buyout, under SOP 50 10 8.1. Lenders can require more."),
        ("Can a seller note count toward the SBA equity injection?",
         "Yes, if it is on full standby with no principal or interest payments for the term of the 7(a) loan. "
         "It can then cover up to half of the required equity."),
        ("Can the seller note be paid after two years?",
         "Not if it counts as equity. SOP 50 10 8.1 defines full standby as the life of the 7(a) loan. A note "
         "with payments can still be in the deal, but as debt in the cash flow test, not as equity."),
        ("Can the SBA equity injection be waived?",
         "For a Business Expansion or Owner Buyout, the lender may reduce or eliminate it if the borrower has "
         "enough liquidity and working capital and no negative net worth at the last fiscal year-end. Never on an Initial Acquisition."),
        ("Does the 10% include closing costs and working capital?",
         "Yes. It's based on total project cost, which includes those, except lines of credit and 504 loans. "
         "For an Owner Buyout it's based on the purchase price instead."),
        ("Can a seller earnout be part of an SBA deal?",
         "No. Seller earnouts are prohibited. A rebate from the seller to the buyer based on performance is "
         "allowed, but it has to be applied to the 7(a) loan's principal."),
    ],
    "related": [
        ("/business-acquisition-financing.html", "Business acquisition financing"),
        ("/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/", "Buy a business with 5% down"),
        ("/business-acquisition-financing/articles/buy-a-competitor-sba-loan/", "Buying a competitor with an SBA loan"),
        ("/business-acquisition-financing/articles/large-business-acquisition-loan/", "$1M-$5M acquisition loans"),
        ("/sba-loans/articles/where-sba-loan-down-payment-can-come-from/", "Where an SBA down payment can come from"),
        ("/sba-loans/articles/sba-loan-buy-out-business-partner/", "SBA loan to buy out a partner"),
    ],
    "sources": [SOP15, SBA_7A, EQ],
}, {
    "slug": "buy-a-competitor-sba-loan",
    "crumb": "Buying a Competitor With an SBA Loan",
    "title": "Buying a Competitor With an SBA Loan | Axiant",
    "og_title": "Buying a Competitor With an SBA Loan: When You Can Put Little or Nothing Down",
    "h1": "Buying a Competitor With an SBA Loan: When You Can Put Little or Nothing Down",
    "headline": "Buying a Competitor With an SBA Loan: When You Can Put Little or Nothing Down",
    "lede": "An established company buying another in its own industry group gets the SBA's easiest "
            "acquisition rules: a lighter cash flow test, and equity the lender can waive",
    "meta_desc": "Buying a competitor with an SBA 7(a) loan: the Business Expansion rules, same 4-digit NAICS group, equity a lender may waive, 1.15 coverage, and an example.",
    "article_desc": "How an existing business can buy a competitor with an SBA 7(a) loan under the "
                    "Business Expansion rules in SOP 50 10 8.1, sometimes with no equity injection.",
    "keywords": "buy a competitor sba loan, sba business expansion acquisition, buy competitor no money "
                "down, sba loan acquire another business, sba 1.15 dscr business expansion",
    "quick_answer": "If your company has run for <strong>two full fiscal years</strong> under its current "
                    "owners and buys <strong>100%</strong> of a business in the same four-digit NAICS industry "
                    "group, SBA treats it as a Business Expansion. Equity starts at 10%, but the lender "
                    "<strong>may reduce or waive it</strong>, and the coverage test drops to "
                    "<strong>1.15 to 1</strong>. Axiant Partners, a business-loan broker in Boca Raton, "
                    "can find lenders that use this. Lenders still set their own terms.",
    "sections": [
        ("The Three Tests for a Business Expansion",
         f"<p>{_SOP_A}, Appendix 15, sets a separate category for an operating company that buys another. "
         "To qualify, the lender has to document that:</p>"
         "<ol>"
         "<li><strong>Your company has operated two full fiscal years</strong> under its current ownership.</li>"
         "<li><strong>You're buying 100%</strong> of the other business. A partial stake doesn't qualify.</li>"
         "<li><strong>The target is in your four-digit NAICS industry group.</strong> That's broader than "
         "your exact six-digit code. For example, electrical contractors (238210) and plumbing and HVAC "
         "contractors (238220) both sit in group 2382, Building Equipment Contractors.</li>"
         "</ol>"
         "<p>The deal must also leave at least as many full personal guarantors as your company had before. "
         "Miss any test and the purchase becomes an Initial Acquisition, with a 10% minimum that can't be "
         "waived and a 1.25 coverage test. "
         'The <a href="/business-acquisition-financing.html">business acquisition financing</a> guide covers '
         "the other ways to fund a purchase.</p>"),
        ("Can You Buy a Competitor With No Money Down?",
         "<p>Sometimes. The SOP's minimum is still 10% of total project cost, but for a Business Expansion "
         "the lender may reduce or eliminate it if it decides your company has enough liquidity and "
         "working capital to keep operating after the deal. Your balance sheet can't show negative net "
         "worth at the last fiscal year-end. It's the lender's call, not an SBA entitlement, which is why "
         "one lender asks for 10% and another asks for nothing.</p>"
         "<p>Two strings come with a waiver:</p>"
         "<ul>"
         "<li><strong>No working capital on top.</strong> The lender can't add dedicated permanent working "
         "capital to this or any other 7(a) term loan within 90 days. Any working capital the deal needs has "
         "to come from your cash or a line of credit. A de minimis leftover is allowed, up to the greater of "
         "$10,000 or 0.5% of the loan.</li>"
         "<li><strong>You're judged on your own balance sheet.</strong> The waiver rests on your company being "
         "adequately capitalized, so thin cash or heavy existing debt tends to bring the 10% back.</li>"
         "</ul>"),
        ("Why the 1.15 Coverage Test Matters",
         "<p>An Initial Acquisition needs earnings of at least 1.25 times the debt payments; a Business "
         "Expansion needs 1.15. The lender may also adjust cash flow for savings the combination creates, and "
         "may combine both companies when the target keeps operating separately. Projections can be reviewed "
         "but can't be used to meet the test.</p>"
         f"<p>Here is what {usd(_CF)} of available annual cash flow supports at each ratio, assuming 10.5% "
         "over 10 years (illustrative, not a quote):</p>"
         + table(["Coverage required", "Most annual debt service", "Largest loan it supports"], [
             ["1.25 (Initial Acquisition)", usd(_COMP[1.25][0]), usd(_COMP[1.25][1])],
             ["1.15 (Business Expansion)", usd(_COMP[1.15][0]), usd(_COMP[1.15][1])],
         ])
         + f"<p>Same earnings, about {usd(_COMP[1.15][1] - _COMP[1.25][1])} more loan.</p>"),
        ("Worked Example: An HVAC Company Buys an Electrical Contractor",
         "<p><strong>Illustrative, not a quote; every loan is subject to approval.</strong> An HVAC "
         f"contractor with four years under its owners buys 100% of an electrical contractor for {usd(_TARGET)}. "
         "Same NAICS group (2382), so it's a Business Expansion. The lender's valuation supports the price, "
         "the buyer has ample cash and no negative net worth, so the lender waives the equity.</p>"
         + table(["Item", "Amount"], [
             ["Purchase price", usd(_TARGET)],
             ["Equity from the buyer", "$0 (waived by the lender)"],
             ["Assumed rate and term", "10.5%, 10 years (acquisition loans amortize over 10 years at most)"],
             ["Monthly payment", f"About {usd(_TARGET_PMT)}"],
             ["Annual debt service", f"About {usd(_TARGET_PMT * 12)}"],
             ["Cash flow needed at 1.15", f"About {usd(_TARGET_PMT * 12 * 1.15)}"],
         ])
         + "<p>Closing costs and the SBA guaranty fee, which the "
         f"{_FEE_A} sets at 3.5% of the guaranteed share up to $1 million, are usually financed on top. "
         "Because the equity was waived, the working capital to absorb the new crews comes from the "
         "company's cash or a line of credit.</p>"),
        ("What Else Still Applies",
         "<ul>"
         "<li><strong>Valuation.</strong> An accredited business valuation for the lender, and a Quality of "
         "Earnings report if the price is $3 million or more. Debt is capped at the valuation.</li>"
         "<li><strong>The seller leaves.</strong> Unlike a partner buyout, the seller can't stay as owner, "
         "officer or employee, only as a consultant for up to 24 months.</li>"
         "<li><strong>Borrower structure.</strong> Your company is the borrower; if the target stays a separate "
         "entity, both are co-borrowers.</li>"
         "<li><strong>Lender appetite.</strong> Many SBA lenders still pass on gas stations, restaurants and "
         'bars and some other industries. See <a href="/sba-loans/articles/businesses-sba-lenders-decline/">'
         "businesses SBA lenders often decline</a>.</li>"
         "</ul>"
         "<p>Buying something outside your industry group, or not buying all of it? Then the "
         '<a href="/business-acquisition-financing/articles/sba-seller-note-equity-injection-rules/">equity '
         "and seller note rules</a> for an Initial Acquisition apply. For deals near the $5 million cap, see "
         '<a href="/business-acquisition-financing/articles/large-business-acquisition-loan/">large '
         "acquisition loans</a>.</p>"
         + _END),
    ],
    "faqs": [
        ("Can I buy a competitor with an SBA loan and no down payment?",
         "Possibly. If it qualifies as a Business Expansion, the lender may reduce or eliminate the 10% equity "
         "when your company has enough liquidity and working capital and no negative net worth. Lenders decide case by case."),
        ("What counts as the same industry for a Business Expansion?",
         "The same four-digit NAICS industry group, not the exact six-digit code. For example, electrical and "
         "HVAC contractors are both in group 2382."),
        ("How long must my business have operated?",
         "At least two full fiscal years under its current ownership. Otherwise the purchase is an Initial Acquisition."),
        ("Can I buy part of a competitor with a Business Expansion loan?",
         "No. The rule requires buying 100% of the ownership interest. A partial purchase falls under other categories."),
        ("What debt service coverage do lenders need for a Business Expansion?",
         "At least 1.15 to 1 under SOP 50 10 8.1, against 1.25 for an Initial Acquisition. Lenders often want more."),
        ("Can the owner of the business I'm buying stay on?",
         "Not as an owner, officer or employee. The seller may consult for up to 24 months in total."),
    ],
    "related": [
        ("/business-acquisition-financing.html", "Business acquisition financing"),
        ("/business-acquisition-financing/articles/sba-seller-note-equity-injection-rules/", "SBA equity and seller note rules"),
        ("/business-acquisition-financing/articles/large-business-acquisition-loan/", "$1M-$5M acquisition loans"),
        ("/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/", "Buy a business with 5% down"),
        ("/business-line-of-credit.html", "Business lines of credit"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP15, NAICS, FEES, SBA_7A],
}, {
    "slug": "large-business-acquisition-loan",
    "crumb": "$1M-$5M Business Acquisition Loans",
    "title": "Large Business Acquisition Loans: $1M-$5M | Axiant",
    "og_title": "Business Acquisition Loans From $1 Million to $5 Million: What Changes",
    "h1": "Business Acquisition Loans From $1 Million to $5 Million: What Changes",
    "headline": "Business Acquisition Loans From $1 Million to $5 Million: What Changes",
    "lede": "Bigger purchases trip extra SBA rules: a Quality of Earnings report, a collateral shortfall "
            "that reaches your house, life insurance, and a $5 million ceiling",
    "meta_desc": "Large business acquisition loans of $1M-$5M: the $3M QoE rule, SBA collateral haircuts, personal real estate, life insurance, seller notes and deals over $5M.",
    "article_desc": "Why SBA lenders ask for more collateral, life insurance and bigger seller notes on "
                    "$1 million to $5 million business acquisitions, from SOP 50 10 8.1.",
    "keywords": "large business acquisition loan, $5 million business acquisition loan, sba quality of "
                "earnings $3 million, sba acquisition collateral shortfall, acquisition loan life insurance",
    "quick_answer": "On a $1 million to $5 million purchase, SBA 7(a) rules add weight. A <strong>Quality of "
                    "Earnings report</strong> is required at a <strong>$3 million</strong> purchase price, "
                    "goodwill counts for nothing as collateral, so lenders must take equity in owners' "
                    "<strong>personal real estate</strong>, and <strong>life insurance</strong> can be required. "
                    "7(a) stops at <strong>$5 million</strong>. Axiant Partners, a broker in Boca Raton, can "
                    "find lenders for these deals. Terms vary by lender.",
    "sections": [
        ("What Changes as the Price Goes Up",
         f"<p>{_SOP_A} applies the same Appendix 15 rules to a $400,000 purchase and a $4 million one, but "
         "several of them only bite at size:</p>"
         + table(["Purchase price", "What the SOP adds", "What lenders commonly add"], [
             ["Over $350,000", "Business valuation from an accredited appraiser, ordered by the lender", "Three years of financials, ideally CPA-reviewed"],
             ["$1M-$3M", "Collateral shortfall rules start to reach personal real estate", "More cash or seller debt, a key-person plan"],
             ["$3M and up", "Quality of Earnings report with a cash proof (Initial Acquisition and Business Expansion)", "Covenants, larger seller notes, a line for working capital"],
             ["Over $5M", "7(a) maximum is $5 million", "A pari passu bank loan, conventional debt or other structures"],
         ])
         + "<p>The $3 million QoE threshold is measured on the Business Purchase Price, excluding owner-occupied "
         "real estate, before any equity or seller debt. It's commissioned for the lender, reconciles the "
         "statements, tax returns and IRS transcripts, and its earnings figure is the one used for coverage.</p>"),
        ("Why the Collateral Shortfall Lands on the Owners",
         "<p>Most of a service company's price is goodwill, which isn't a fixed asset. The SOP defines "
         "\"fully secured\" using discounted values:</p>"
         + table(["Asset", "Value counted toward fully secured"], [
             ["Used equipment", "Machinery and equipment: 50% of net book value, or 80% of an orderly liquidation appraisal"],
             ["Improved real estate", "85% of market value"],
             ["Unimproved real estate", "50% of market value"],
             ["Furniture and fixtures", "10% of net book or appraised value"],
             ["Receivables and inventory", "10% of current book value"],
         ])
         + "<p>When a loan isn't fully secured, the lender must take available equity in personal real estate "
         "solely owned by co-borrowers, 20%+ owners and most guarantors, including investment property. "
         "The lien can be limited to the shortfall or to 150% of the equity, and a property with less than 25% "
         "equity doesn't have to be pledged.</p>"),
        ("Worked Example: A $3,500,000 Purchase",
         f"<p><strong>Illustrative, not a quote.</strong> A buyer acquires a distribution company for "
         f"{usd(_PRICE)} with 10% equity (fees and costs left out to keep the math clear), so the 7(a) "
         f"loan is {usd(_LOAN)}. The business has {usd(_EQUIP)} of used equipment at book, {usd(_AR)} of "
         f"receivables, {usd(_INV)} of inventory and {usd(_FF)} of furniture and fixtures.</p>"
         + table(["Item", "Amount"], [
             ["Equipment at 50% of book", usd(_C_EQUIP)],
             ["A/R and inventory at 10%", usd(_C_TRADE)],
             ["Fixtures at 10%", usd(_C_FF)],
             ["<strong>Business collateral value</strong>", f"<strong>{usd(_COLL)}</strong>"],
             ["Shortfall against the loan", usd(_SHORT)],
             ["Buyer's home equity", f"{usd(_HOME)} value less a {usd(_MORT)} mortgage: {usd(_HOME_EQ)} ({_HOME_EQ / _HOME:.0%}), so it must be pledged"],
             ["Shortfall after the home", usd(_SHORT2)],
             ["Monthly payment", f"About {usd(_BIG_PMT)} (10.5%, 10 years)"],
             ["Cash flow needed at 1.25", f"About {usd(_BIG_CF)} a year"],
         ])
         + "<p>The price is above $3 million, so a QoE is also required. If the business depends on this one "
         "owner, life insurance is required for the shortfall amount, as the next section explains.</p>"),
        ("Life Insurance, Seller Notes and Reserves",
         "<ul>"
         "<li><strong>Life insurance.</strong> On a standard 7(a) loan that isn't fully secured, the SOP "
         "requires life insurance in the amount of the collateral shortfall for a sole proprietor, a "
         "single-member LLC or any business dependent on one owner. The policy is collaterally assigned to the "
         "lender, an existing policy can be pledged, and credit life or whole life shouldn't be required. The lender's memo must say who is insured "
         "and for how much, or why none.</li>"
         "<li><strong>Bigger seller notes.</strong> Lenders often ask sellers of larger companies to carry "
         "more, both to cut the loan and to keep the seller invested. Only a note on full standby counts as "
         "equity; see the <a href=\"/business-acquisition-financing/articles/sba-seller-note-equity-injection-rules/\">"
         "seller note rules</a>.</li>"
         "<li><strong>Working capital lines.</strong> The SOP lets a line of credit hold a first lien on "
         "the acquired receivables and inventory if 20% to 50% of its day-one availability is used to fund "
         "part of the price.</li>"
         "<li><strong>Reserves.</strong> Lenders commonly want post-closing liquidity on top of the equity, "
         "and the cash flow test is run on the lower QoE earnings.</li>"
         "</ul>"),
        ("Deals Over $5 Million",
         "<p>A single 7(a) loan tops out at $5 million. Larger purchases usually pair it with another lender. "
         "The SOP bans piggyback structures, where another loan made within 90 days takes a senior lien over "
         "the SBA loan. A shared lien with the bank (pari passu) is allowed if the other loan's maturity isn't "
         "shorter than the SBA loan's. Banks also face lending limits: under 12 CFR 32.3 a national bank can "
         "generally lend one borrower 15% of its capital and surplus, so big deals often need a participation. "
         'Our <a href="/10-million-business-loan.html">$10 million business loan guide</a> covers the '
         "structures above the 7(a) limit.</p>"
         "<p>Related: <a href=\"/business-acquisition-financing/articles/buy-a-competitor-sba-loan/\">buying a "
         "competitor</a> uses a lighter 1.15 coverage test, and the "
         '<a href="/business-acquisition-financing.html">business acquisition financing</a> guide compares '
         "SBA with conventional and seller financing.</p>"
         + _END),
    ],
    "faqs": [
        ("Can you get a $5 million SBA loan to buy a business?",
         "Yes, $5 million is the 7(a) maximum, and acquisitions can use it. At that size expect a Quality of "
         "Earnings report, an accredited valuation and a close look at collateral and coverage."),
        ("When does the SBA require a Quality of Earnings report?",
         "For Initial Acquisitions and Business Expansions with a Business Purchase Price of $3 million or more, "
         "excluding owner-occupied real estate, under SOP 50 10 8.1."),
        ("Will the lender take a lien on my house to buy a business?",
         "Often, on larger deals. If the loan isn't fully secured, the SOP requires the lender to take available "
         "equity in personal real estate of 20%+ owners, unless the equity is under 25% of its value."),
        ("Is life insurance required on an SBA acquisition loan?",
         "On a standard 7(a) loan that isn't fully secured, yes for a sole proprietor, single-member LLC or "
         "business dependent on one owner, in the amount of the collateral shortfall. Otherwise lender policy applies."),
        ("How do you finance an acquisition over $5 million?",
         "Usually by pairing a 7(a) loan with a bank loan that shares the lien and has at least as long a "
         "maturity, or with conventional, seller or equity financing."),
        ("Why do lenders want a bigger seller note on larger deals?",
         "It lowers the loan, keeps the seller invested in the transition and covers part of the collateral "
         "gap. To count as equity it must be on full standby."),
    ],
    "related": [
        ("/business-acquisition-financing.html", "Business acquisition financing"),
        ("/business-acquisition-financing/articles/sba-seller-note-equity-injection-rules/", "SBA equity and seller note rules"),
        ("/business-acquisition-financing/articles/buy-a-competitor-sba-loan/", "Buying a competitor with an SBA loan"),
        ("/10-million-business-loan.html", "$10 million business loans"),
        ("/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/", "Buy a business with 5% down"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP15, SBA_7A, LLL, EQ],
}]
