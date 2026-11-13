# -*- coding: utf-8 -*-
"""Hotel financing spokes: SBA plan Cluster 2, under /hotel-financing/articles/.

Five spokes for the /hotel-financing.html pillar: flagged vs independent, PIP financing, flag
conversions, hotel experience, and 2026 rates. The SBA-vs-CMBS-vs-bank program comparison already
exists at /commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/ and is
linked, not duplicated. The USDA hotel page belongs to Cluster 3 (/usda-business-loans/...).

Rules read on 2026-11-13 from the SOP 50 10 8.1 technical-update .docx on legacy.sba.gov
(effective 2026-10-01): hotel eligibility (>50% of prior-year revenue from stays of 30 days or
less), Franchise Directory use (a brand meeting the FTC franchise definition must be listed;
executed franchise agreement before 7(a) disbursement), management-agreement passive-business
review, Appendix 15 (Initial Acquisition 10% that can't be reduced; Business Expansion 10% the
lender may reduce or eliminate; DSC 1.25 vs 1.15; Special Purpose Property 25-year exemption at
85%+ real estate; blended maturity otherwise; projections allowed when the appraisal fully
secures the loan; no QoE), mixed-purpose 51% real estate rule for non-acquisition loans,
construction bonds over $350,000, Section 106 historic review for renovations, the subsidy
recoupment fee, and max variable rate Prime + 3.0% over $350,000. 13 CFR 120.212, 120.910 and
16 CFR 436.2 read on law.cornell.edu. Prime 7.00% (Nov 11) and 10-year Treasury 4.98% (Nov 10)
from Fed H.15. Never names a lender. Every payment and ratio below is computed here.
"""
from cluster_table import table
from sba_sources import SOP, FEES, SBA_7A, SBA_504

# ---------------------------------------------------------------- sources
FRANCHISE_DIR = ("https://www.sba.gov/document/support-sba-franchise-directory",
                 "SBA Franchise Directory",
                 "The SBA's list of brands eligible for SBA financing; a brand that meets the FTC "
                 "definition of a franchise must be listed.")
FTC_436 = ("https://www.law.cornell.edu/cfr/text/16/436.2",
           "16 CFR 436.2: When the franchise disclosure document is due",
           "The FDD must reach a prospective franchisee at least 14 calendar days before signing or paying.")
MAT = ("https://www.law.cornell.edu/cfr/text/13/120.212",
       "13 CFR 120.212: Maturities of 7(a) loans",
       "25-year maximum, plus a period to complete construction or improvements on real property.")
C504 = ("https://www.law.cornell.edu/cfr/text/13/120.910",
        "13 CFR 120.910: 504 borrower contribution",
        "15% for a limited or special purpose building or a business two years old or less; 20% when both apply.")
RECOUP = ("https://www.law.cornell.edu/cfr/text/13/120.223",
          "13 CFR 120.223: Subsidy recoupment fee",
          "The 5%, 3% and 1% fee on large voluntary prepayments of 7(a) loans of 15 years or longer.")
H15 = ("https://www.federalreserve.gov/releases/h15/",
       "Federal Reserve H.15: Selected Interest Rates",
       "Bank prime rate 7.00% on November 11, 2026; 10-year Treasury 4.98% on November 10, 2026.")

_SOP_A = ('<a href="' + SOP[0] + '" rel="noopener nofollow" target="_blank">SBA SOP 50 10 8.1</a>')
_DIR_A = ('<a href="' + FRANCHISE_DIR[0] + '" rel="noopener nofollow" target="_blank">SBA Franchise Directory</a>')

PILLAR = '<a href="/hotel-financing.html">hotel financing</a>'
CMP = '<a href="/commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/">SBA vs CMBS vs bank hotel loans</a>'
S_FLAG = "/hotel-financing/articles/flagged-vs-independent-hotel-sba-loans/"
S_PIP = "/hotel-financing/articles/hotel-pip-financing/"
S_CONV = "/hotel-financing/articles/hotel-flag-conversion-financing/"
S_EXP = "/hotel-financing/articles/hotel-experience-sba-loan/"
S_RATE = "/hotel-financing/articles/typical-hotel-loan-rates-2026/"
USDA_HOTEL = "/usda-business-loans/articles/usda-hotel-loans/"
CTA = ('<p><strong>Talk to an SBA specialist: (561) 268-0465</strong>, or '
       '<a href="/match.html">get matched with hotel lenders</a>.</p>')


# ---------------------------------------------------------------- math
def pmt(p, rate_pct, years):
    r, n = rate_pct / 1200.0, years * 12
    return p * r / (1 - (1 + r) ** -n)


def pv(payment, rate_pct, years):
    r, n = rate_pct / 1200.0, years * 12
    return payment * (1 - (1 + r) ** -n) / r


def guaranty_fee(loan):
    """FY2027 7(a) upfront fee on a loan over $1M at a 75% guaranty (pillar's method)."""
    g = loan * 0.75
    return 0.035 * min(g, 1_000_000) + 0.0375 * max(0.0, g - 1_000_000)


def financed(base):
    """Loan that also carries its own guaranty fee."""
    loan = base
    for _ in range(50):
        loan = base + guaranty_fee(loan)
    return loan


def d(x, step=10):
    return f"${round(x / step) * step:,.0f}"


def pct(x, nd=1):
    return f"{x * 100:.{nd}f}%"


PRIME, T10 = 7.00, 4.98

# --- spoke 1: flagged vs independent (illustrative)
F_PRICE, F_CLOSE = 2_500_000, 50_000
F_COST = F_PRICE + F_CLOSE
F_RATE = 9.5
F_FLAG_EQ, F_IND_EQ = 0.15, 0.20
f_flag_loan = F_COST * (1 - F_FLAG_EQ)
f_ind_loan = F_COST * (1 - F_IND_EQ)
f_flag_pmt = pmt(f_flag_loan, F_RATE, 25)
f_ind_pmt = pmt(f_ind_loan, F_RATE, 25)
f_flag_cf = f_flag_pmt * 12 * 1.25
f_ind_cf = f_ind_pmt * 12 * 1.25

# --- spoke 2: PIP with a purchase (illustrative)
P_RE, P_FFE, P_GW = 2_450_000, 250_000, 100_000          # purchase price allocation
P_PIP_BLDG, P_PIP_FFE = 380_000, 270_000                   # PIP split
P_CLOSE = 45_000
P_PRICE = P_RE + P_FFE + P_GW
P_PIP = P_PIP_BLDG + P_PIP_FFE
P_TOTAL = P_PRICE + P_PIP + P_CLOSE
P_RE_ALL = P_RE + P_PIP_BLDG
P_RE_SHARE = P_RE_ALL / P_TOTAL
P_BLEND = round((P_RE_ALL * 25 + (P_TOTAL - P_RE_ALL) * 10) / P_TOTAL)
P_RATE = 9.5
p_eq10 = P_TOTAL * 0.10
p_eq15 = P_TOTAL * 0.15
p_loan = P_TOTAL - p_eq15
p_pmt_blend = pmt(p_loan, P_RATE, P_BLEND)
p_pmt_25 = pmt(p_loan, P_RATE, 25)
p_no_pip_eq = (P_PRICE + P_CLOSE) * 0.15
assert P_RE_SHARE < 0.85

# --- spoke 3: flag conversion on a hotel you already own (illustrative)
C_BLDG, C_FFE, C_FEE, C_SOFT = 520_000, 260_000, 55_000, 25_000
C_TOTAL = C_BLDG + C_FFE + C_FEE + C_SOFT
C_RE_SHARE = C_BLDG / C_TOTAL
C_RATE = 9.75
C_NOI, C_EXIST_DS = 610_000, 380_000
c_pmt25 = pmt(C_TOTAL, C_RATE, 25)
c_pmt10 = pmt(C_TOTAL, C_RATE, 10)
c_ds25 = c_pmt25 * 12
c_ds10 = c_pmt10 * 12
c_dsc_now = C_NOI / C_EXIST_DS
c_dsc_25 = C_NOI / (C_EXIST_DS + c_ds25)
c_dsc_10 = C_NOI / (C_EXIST_DS + c_ds10)
assert C_RE_SHARE >= 0.51

# --- spoke 4: experience / business expansion DSC (illustrative)
E_CF = 420_000
E_RATE = 9.5
e_ds_125 = E_CF / 1.25
e_ds_115 = E_CF / 1.15
e_loan_125 = pv(e_ds_125 / 12, E_RATE, 25)
e_loan_115 = pv(e_ds_115 / 12, E_RATE, 25)

# --- spoke 5: rates
R_7A_CAP = PRIME + 3.0
R_7A_MID = PRIME + 4.5
R_DEB = 6.984                       # NADCO Oct 2026 effective rate, as on the site's debenture page
R_504_LO = (0.5 * 7.0 + 0.4 * R_DEB) / 0.9
R_504_HI = (0.5 * 9.0 + 0.4 * R_DEB) / 0.9
R_CMBS_LO, R_CMBS_HI = T10 + 2.5, T10 + 4.0
R_LOAN = 3_000_000
r_pay = {r: pmt(R_LOAN, r, 25) for r in (7.0, 8.0, 9.0, 10.0)}
r_bridge_io = R_LOAN * 0.10 / 12
r_fee = guaranty_fee(R_LOAN)
r_recoup = [R_LOAN * 0.30 * x for x in (0.05, 0.03, 0.01)]

CLUSTER = {
    "pillar": "hotel-financing.html",
    "hub": "hotel-financing/articles",
    "back_href": "/hotel-financing/articles/",
    "crumb": "Hotel Financing",
    "cta_inline": "Talk to an SBA specialist",
    "cta_button": "Talk to an SBA Specialist",
    "hub_title": "Hotel Financing Articles: PIPs, Flags & Rates | Axiant",
    "hub_h1": "Hotel Financing Articles",
    "hub_desc": "Guides for hotel buyers and owners: flagged vs independent SBA loans, PIP and flag "
                "conversion financing, the experience lenders want, and 2026 hotel loan rates.",
    "hub_lede": "Specific questions hotel buyers and owners ask before they apply",
    "hub_quick_answer": "Hotels can use SBA 7(a) and 504 loans when more than 50% of prior-year revenue "
                        "comes from guests staying 30 days or less. The guides below cover what changes "
                        "with a flag, how a PIP or conversion gets funded, how lenders judge experience, "
                        "and where rates sit in 2026. Axiant Partners, a broker in Boca Raton, matches "
                        "hotel buyers with lenders.",
    "hub_intro": 'Start with the <a href="/hotel-financing.html">hotel financing guide</a> for SBA '
                 "eligibility, equity and a worked purchase. For the program comparison, see "
                 + CMP + ".",
    "hub_cta_h2": "Talk to an SBA specialist",
    "hub_cta_p": "Call (561) 268-0465, or tell us about the hotel and we'll match you with lenders "
                 "that finance your kind of property.",
}

ARTICLES = [
# ================================================================ 1
{
    "slug": "flagged-vs-independent-hotel-sba-loans",
    "crumb": "Flagged vs Independent Hotels",
    "title": "Flagged vs Independent Hotel SBA Loans | Axiant",
    "og_title": "SBA Loans for Flagged vs Independent Hotels: What Changes",
    "h1": "SBA Loans for Flagged vs Independent Hotels: What Changes",
    "headline": "SBA Loans for Flagged vs Independent Hotels: What Changes",
    "lede": "Both can qualify. A brand adds a Franchise Directory check and a franchise agreement; "
            "an independent puts more weight on the operator and the hotel's own numbers",
    "meta_desc": "Flagged vs independent hotel SBA loans: the Franchise Directory rule, management agreements, what lenders review for each, and a computed equity example.",
    "article_desc": "How SBA lenders treat branded and independent hotels differently, from the "
                    "Franchise Directory check to equity and cash flow.",
    "keywords": "independent hotel sba loan, flagged hotel financing, sba loan franchise hotel, "
                "boutique hotel financing, sba franchise directory hotel",
    "quick_answer": "Both flagged and independent hotels can get SBA 7(a) or 504 loans if more than "
                    "<strong>50%</strong> of revenue comes from stays of 30 days or less. A brand that "
                    "meets the FTC franchise definition must be on the <strong>SBA Franchise "
                    "Directory</strong>. Independents skip that step, but lenders often ask for more "
                    "equity and lean harder on the operator. Axiant Partners, a broker in Boca Raton, "
                    "finds lenders for both. Ranges are typical, not a quote.",
    "sections": [
        ("Where This Fits",
         f"<p>This guide covers one decision inside {PILLAR}: whether the hotel carries a brand. "
         "The SBA eligibility test is the same either way. What changes is the paperwork, the "
         "questions the lender asks and, often, how much cash the lender wants from you. If you are "
         f"weighing SBA against CMBS or a bank loan instead, read {CMP}.</p>"),
        ("What a Flag Changes in SBA Underwriting",
         f"<p>Under {_SOP_A}, if a hotel brand meets the FTC definition of a franchise, it has to be "
         f"listed on the {_DIR_A} before a lender can submit or approve the loan. If the brand isn't "
         "listed, the loan can't go forward until the franchisor gets it added. Most large hotel "
         "brands are already listed, but check the exact brand name and agreement type, not just "
         "the parent company.</p>"
         "<ul>"
         "<li><strong>Executed franchise agreement.</strong> For a 7(a) loan the lender must have "
         "the signed franchise agreement, and anything else the franchisor requires you to sign, "
         "before any money is disbursed. On a 504, the CDC's closing counsel certifies those "
         "documents.</li>"
         "<li><strong>Management agreements.</strong> A hotel management agreement that is part of "
         "the brand's franchise disclosure documents doesn't need a separate review. One that isn't "
         "must be read to make sure it doesn't turn you into an ineligible passive business.</li>"
         "<li><strong>Brand performance data.</strong> Lenders commonly ask for the franchisor's "
         "reports and a competitive-set report alongside the hotel's own financials.</li>"
         "<li><strong>Franchise term.</strong> Lenders often compare the years left on the franchise "
         "agreement with the loan term. A sale usually triggers a new agreement and a PIP; see "
         f'<a href="{S_PIP}">how PIP financing works</a>.</li>'
         "</ul>"),
        ("What Independent Hotels Get Asked Instead",
         "<p>An independent has no Directory step and no franchise agreement, so underwriting rests "
         "on the property and the operator. These are common lender practices, not SBA rules:</p>"
         "<ul>"
         "<li><strong>Booking sources.</strong> How much revenue comes from online travel agencies, "
         "direct bookings, groups and repeat guests, and what that costs in commissions.</li>"
         "<li><strong>Clean books.</strong> Three years of financials that tie to tax returns, plus "
         "the property management system's occupancy and rate reports.</li>"
         "<li><strong>The transient test.</strong> Independents drift into weekly and monthly "
         "rentals more often than branded hotels. More than half of the prior year's revenue has "
         "to come from stays of 30 days or less.</li>"
         "<li><strong>Soft brands and affiliations.</strong> A marketing or soft-brand agreement may "
         "still meet the FTC franchise definition. If it does, it needs to be on the Directory.</li>"
         "<li><strong>Who runs it.</strong> Without brand systems, the lender wants to know who sets "
         'rates, sells rooms and manages staff. See <a href="' + S_EXP + '">how lenders judge '
         "hotel experience</a>.</li>"
         "</ul>"),
        ("Side by Side",
         table(["", "Flagged hotel", "Independent hotel"], [
             ["SBA eligibility test", "Over 50% of revenue from stays of 30 days or less", "Same"],
             ["Franchise Directory", "Brand must be listed if it meets the FTC definition", "Not needed unless an affiliation meets the definition"],
             ["Key documents", "Franchise agreement, PIP, brand reports", "Own financials, PMS reports, booking mix"],
             ["Management agreement", "Exempt from review if part of the brand's FDD", "Reviewed for passive-business risk"],
             ["Main lender worry", "PIP cost and franchise term", "Rate and occupancy without a brand"],
             ["Equity lenders commonly ask", "About 15%, above the 10% SBA minimum", "Often 15-25%"],
         ])
         + "<p>The 10% is the SBA minimum on a 7(a) initial acquisition. The ranges above are common "
         "lender practice and vary by deal. On a 504, hotels are limited or special purpose "
         "property, so the borrower puts in at least 15%, or 20% if the business is two years old "
         "or less.</p>"),
        ("Worked Example: Same Price, Different Equity",
         "<p><strong>Illustrative numbers, not a quote.</strong> Two hotels sell for "
         f"{d(F_PRICE)} with about {d(F_CLOSE)} of closing costs. Assume one lender asks "
         f"{pct(F_FLAG_EQ, 0)} down on the flagged hotel and {pct(F_IND_EQ, 0)} on the independent, "
         f"a {F_RATE}% rate and a 25-year term. The 25-year term assumes at least 85% of project "
         "costs are real estate, which the SOP requires for that term on a hotel purchase.</p>"
         + table(["", "Flagged", "Independent"], [
             ["Project cost", d(F_COST), d(F_COST)],
             ["Buyer's cash", d(F_COST * F_FLAG_EQ), d(F_COST * F_IND_EQ)],
             ["Loan", d(f_flag_loan), d(f_ind_loan)],
             ["Monthly payment", d(f_flag_pmt), d(f_ind_pmt)],
             ["Cash flow needed at 1.25x", d(f_flag_cf) + " a year", d(f_ind_cf) + " a year"],
         ])
         + f"<p>The independent buyer brings {d(F_COST * (F_IND_EQ - F_FLAG_EQ))} more cash but "
         f"needs about {d(f_flag_cf - f_ind_cf)} less cash flow a year to cover the payment. "
         "Guaranty fees are left out to keep the comparison clean.</p>"),
        ("Before You Make an Offer",
         "<ol>"
         "<li><strong>Look up the brand</strong> on the SBA Franchise Directory by its exact name.</li>"
         "<li><strong>Run the transient test</strong> on last year's revenue by length of stay.</li>"
         "<li><strong>Ask the brand what a sale triggers:</strong> new agreement, PIP, fees.</li>"
         "<li><strong>For an independent, pull booking-channel data</strong> and three years of books.</li>"
         "<li><strong>Read any management agreement</strong> for who controls staff, money and accounts.</li>"
         "</ol>"
         f'<p>Rates differ less by flag than by deal size and cash flow; see <a href="{S_RATE}">hotel '
         f'loan rates for 2026</a>. In a small town, a <a href="{USDA_HOTEL}">USDA hotel loan</a> '
         "may also fit.</p>" + CTA),
    ],
    "faqs": [
        ("Can an independent hotel get an SBA loan?",
         "Yes. Hotels are eligible if more than 50% of the prior year's revenue comes from guests "
         "staying 30 days or less, whether or not they carry a brand. Lenders lean more on the "
         "operator and the hotel's own records."),
        ("Does my hotel brand have to be on the SBA Franchise Directory?",
         "Yes, if the brand meets the FTC definition of a franchise. A lender can't submit or approve "
         "the loan until the brand is listed."),
        ("Is it easier to finance a flagged hotel?",
         "Often. Brand systems and reporting give lenders more to rely on. The trade-off is a PIP "
         "and franchise fees that raise the project cost."),
        ("Does a hotel management company make me a passive owner?",
         "It can. Unless the agreement is part of a listed brand's disclosure documents, the lender "
         "must check that it doesn't give the manager sole control of staff, finances and bank accounts."),
        ("How much down for an independent hotel?",
         "The SBA minimum on a 7(a) purchase is 10%, and many lenders want more on independents, often "
         "15-25%. A 504 needs at least 15%."),
    ],
    "related": [
        ("/hotel-financing.html", "Hotel financing guide"),
        (S_PIP, "Hotel PIP financing"),
        (S_EXP, "Hotel experience lenders want"),
        ("/commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/", "SBA vs CMBS vs bank hotel loans"),
        ("/sba-loans/articles/sba-loan-buy-franchise/", "SBA loans for franchises"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, FRANCHISE_DIR, C504, SBA_7A],
},
# ================================================================ 2
{
    "slug": "hotel-pip-financing",
    "crumb": "Hotel PIP Financing",
    "title": "Hotel PIP Financing: How to Fund Brand Upgrades | Axiant",
    "og_title": "Hotel PIP Financing: Paying for a Property Improvement Plan",
    "h1": "Hotel PIP Financing: Paying for a Property Improvement Plan",
    "headline": "Hotel PIP Financing: Paying for a Property Improvement Plan",
    "lede": "How a PIP gets rolled into an SBA purchase loan, why the split between building work "
            "and furniture changes your term, and the construction rules that come with it",
    "meta_desc": "Hotel PIP financing with an SBA loan: rolling the PIP into a purchase, how FF&E vs building work sets the term, bonds over $350,000, and a computed example.",
    "article_desc": "How hotel buyers finance a brand's property improvement plan with an SBA loan, "
                    "including term, equity and construction rules.",
    "keywords": "hotel pip financing, property improvement plan loan, pip loan hotel, sba loan hotel "
                "renovation, hotel renovation financing",
    "quick_answer": "A hotel PIP can usually be rolled into an SBA 7(a) or 504 purchase loan because "
                    "renovating an existing building is an eligible use. The PIP raises total project "
                    "cost, so your equity rises with it. Building work can get up to "
                    "<strong>25 years</strong>, but furniture and soft goods pull the blended term "
                    "down. Renovation over <strong>$350,000</strong> brings bonding or construction "
                    "monitoring. Axiant Partners, a broker in Boca Raton, finds hotel lenders. Typical "
                    "ranges, not a quote.",
    "sections": [
        ("What a PIP Covers and Why Lenders Care",
         f"<p>A property improvement plan is the brand's list of required upgrades. A sale or a new "
         f"franchise agreement usually triggers one. The {PILLAR} guide covers the basics; this "
         "page is about paying for it. Lenders split a PIP into two kinds of spending:</p>"
         "<ul>"
         "<li><strong>Building work:</strong> roofs, HVAC, elevators, fire and life safety, "
         "bathrooms, parking, exterior and signage structures.</li>"
         "<li><strong>FF&amp;E and soft goods:</strong> beds, case goods, carpet, TVs, lobby furniture, "
         "linens and technology.</li>"
         "</ul>"
         "<p>That split matters because SBA term limits follow what the money buys. Ask the brand "
         "for the PIP early and get contractor quotes for each line. A budget built from the brand's "
         "estimate alone tends to come in low.</p>"),
        ("How the PIP Changes Your Term",
         f"<p>Under {_SOP_A} Appendix 15, a hotel purchase can get a single <strong>25-year</strong> "
         "term when at least 85% of total project costs are real estate. A PIP heavy in furniture "
         "and soft goods can push you under that line. Then the maturity is blended. The real "
         "estate share gets up to 25 years, everything else 10 years, and the result is weighted "
         "by use of proceeds and rounded to the nearest year.</p>"
         '<p><a href="https://www.law.cornell.edu/cfr/text/13/120.212" rel="noopener nofollow" '
         'target="_blank">13 CFR 120.212</a> also lets the real property portion run 25 years plus '
         "the time needed to finish the improvements. A long PIP doesn't eat into your amortization.</p>"),
        ("Construction Rules That Come With a PIP",
         "<ul>"
         "<li><strong>Bonds or monitoring above $350,000.</strong> If the construction part of a "
         "7(a) loan is over $350,000, the contractor needs 100% performance and payment bonds plus "
         "builder's risk and workers' comp. The exception is a lender that uses a third-party "
         "construction manager or its own construction department with funds control. At "
         "$350,000 or less, the lender can follow its usual construction practice.</li>"
         "<li><strong>Historic review.</strong> If you plan to alter or renovate the property, the "
         "lender must ask SBA counsel for a Section 106 historic preservation review. Older "
         "downtown hotels can take extra time here.</li>"
         "<li><strong>No do-it-yourself.</strong> The SOP warns lenders that owner-run construction "
         "causes lien and completion problems. Expect to use a licensed general contractor.</li>"
         "<li><strong>Draws.</strong> Lenders commonly hold the PIP money and release it as work is "
         "inspected, with lien waivers at each draw.</li>"
         "</ul>"),
        ("Worked Example: A Purchase With a $650,000 PIP",
         "<p><strong>Illustrative numbers, not a quote.</strong> A buyer pays "
         f"{d(P_PRICE)} for a limited-service hotel: {d(P_RE)} allocated to real estate, "
         f"{d(P_FFE)} to existing FF&amp;E and {d(P_GW)} to goodwill. The brand's PIP is "
         f"{d(P_PIP)}: {d(P_PIP_BLDG)} of building work and {d(P_PIP_FFE)} of FF&amp;E. Closing "
         f"costs are {d(P_CLOSE)}.</p>"
         + table(["Item", "Amount"], [
             ["Total project cost", d(P_TOTAL)],
             ["Real estate share of costs", f"{d(P_RE_ALL)} ({pct(P_RE_SHARE)})"],
             ["Passes the 85% test?", "No"],
             ["Blended term (25/10 yrs)", f"{P_BLEND} years"],
             ["SBA minimum equity (10%)", d(p_eq10)],
             ["Equity at 15%", d(p_eq15)],
             ["Loan at 85%", d(p_loan)],
             [f"Payment, {P_RATE}% over {P_BLEND} yrs", d(p_pmt_blend)],
             [f"Same loan over 25 years", d(p_pmt_25)],
         ])
         + f"<p>Without the PIP, 15% equity would have been {d(p_no_pip_eq)}. The PIP adds "
         f"{d(p_eq15 - p_no_pip_eq)} of cash at closing and about {d(p_pmt_blend - p_pmt_25)} a "
         "month from the shorter blended term. Moving the existing FF&amp;E and goodwill into a "
         "smaller share, or paying for soft goods with cash, can get a deal over the 85% line. "
         "The SBA guaranty fee, usually financed, is left out here.</p>"),
        ("A PIP on a Hotel You Already Own",
         "<p>If you aren't buying, the change-of-ownership rules don't apply. For a loan with mixed "
         "uses, the SOP allows up to 25 years if at least 51% of the proceeds go to real estate. "
         "Otherwise the term is blended. A PIP at renewal is often mostly building work, so it can "
         "clear 51% when the 85% purchase test would have failed. If the PIP comes with a new brand, "
         f'see <a href="{S_CONV}">flag conversion financing</a>.</p>'
         "<p>Some owners finance FF&amp;E separately with "
         '<a href="/equipment-financing.html">equipment financing</a> so the SBA loan stays mostly '
         "real estate. Compare the total cost both ways before deciding.</p>"),
        ("Steps",
         "<ol>"
         "<li><strong>Get the PIP and quotes</strong> before you set the price.</li>"
         "<li><strong>Tag each line</strong> as building work or FF&amp;E, then work out the real estate share.</li>"
         "<li><strong>Agree the completion deadline</strong> with the brand, and match the loan's draw schedule to it.</li>"
         "<li><strong>Pick a licensed, bondable contractor</strong> if the work tops $350,000.</li>"
         "<li><strong>Budget a contingency.</strong> Overruns usually come out of your cash, not the loan.</li>"
         "</ol>" + CTA),
    ],
    "faqs": [
        ("Can an SBA loan pay for a hotel PIP?",
         "Usually. Converting or renovating an existing building is an eligible use of SBA loan "
         "proceeds, so a PIP can be part of the project when you buy or as a separate loan later."),
        ("Does a PIP increase my down payment?",
         "Yes. SBA equity minimums are based on total project cost, and the PIP is part of that cost."),
        ("Why would a PIP shorten my loan term?",
         "On a hotel purchase, a single 25-year term needs 85% or more of project costs in real "
         "estate. Furniture and soft goods count as other uses, so a FF&E-heavy PIP can force a "
         "blended, shorter term."),
        ("Does the contractor need to be bonded?",
         "If the construction part of a 7(a) loan is over $350,000, generally yes. The exception is a "
         "lender that uses third-party or in-house construction management with funds control."),
        ("Can I do the PIP work myself?",
         "Lenders generally won't allow it. The SOP calls owner-run construction generally unsatisfactory "
         "because of lien and completion risk."),
        ("What if the PIP runs over budget?",
         "Overruns usually fall on the owner. Build a contingency into your budget and keep cash in reserve."),
    ],
    "related": [
        ("/hotel-financing.html", "Hotel financing guide"),
        (S_CONV, "Hotel flag conversion financing"),
        (S_FLAG, "Flagged vs independent hotels"),
        ("/equipment-financing.html", "Equipment financing for FF&E"),
        ("/sba-100-percent-financing.html", "100% SBA financing"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, MAT, SBA_7A, SBA_504],
},
# ================================================================ 3
{
    "slug": "hotel-flag-conversion-financing",
    "crumb": "Flag Conversion Financing",
    "title": "Hotel Flag Conversion Financing in 2026 | Axiant",
    "og_title": "Hotel Flag Conversion Financing: Costs, Loans and Timing",
    "h1": "Hotel Flag Conversion Financing: Costs, Loans and Timing",
    "headline": "Hotel Flag Conversion Financing: Costs, Loans and Timing",
    "lede": "Moving an independent to a brand, or one brand to another: what the conversion costs, "
            "how an SBA loan can fund it, and how lenders size it on today's numbers",
    "meta_desc": "Hotel flag conversion financing: conversion costs, the FDD 14-day rule, the SBA Franchise Directory, the 51% real estate term rule, and a computed DSCR example.",
    "article_desc": "How hotel owners finance a change of brand, including conversion costs, "
                    "SBA rules and a worked debt-coverage example.",
    "keywords": "hotel flag conversion financing, hotel rebranding loan, convert independent hotel "
                "to franchise, hotel conversion loan, change hotel brand",
    "quick_answer": "A flag conversion is usually financed as a renovation of a hotel you already "
                    "own, often with an SBA 7(a) loan. If at least <strong>51%</strong> of proceeds go "
                    "to real estate, the term can reach <strong>25 years</strong>. The new brand must be "
                    "on the SBA Franchise Directory, and you get its disclosure document at least "
                    "<strong>14 days</strong> before signing. Lenders size the loan on current cash "
                    "flow. Axiant Partners, a broker in Boca Raton, finds hotel lenders. Typical "
                    "ranges, not a quote.",
    "sections": [
        ("What a Conversion Costs",
         f"<p>Converting is a renovation project with a franchise attached. The {PILLAR} guide "
         "explains SBA eligibility for hotels; this page is about the conversion itself. Costs "
         "usually fall into five buckets:</p>"
         "<ul>"
         "<li><strong>Conversion PIP:</strong> building work and FF&amp;E to meet the new brand's "
         "standards.</li>"
         "<li><strong>Signage and technology:</strong> exterior signs, property management and "
         "reservation systems, key cards and Wi-Fi.</li>"
         "<li><strong>Initial franchise fee</strong> and any application fee, listed in the "
         "disclosure document.</li>"
         "<li><strong>Exit costs</strong> if you're leaving a brand early. Read your current "
         "agreement for termination or liquidated damages clauses.</li>"
         "<li><strong>Carrying costs:</strong> rooms out of service and a ramp-up period after the "
         "new flag goes up.</li>"
         "</ul>"
         "<p>A conversion done as part of a purchase is underwritten with the purchase. See "
         f'<a href="{S_PIP}">PIP financing with a purchase</a>.</p>'),
        ("Franchise Rules That Set the Timeline",
         '<ul><li><strong>Disclosure first.</strong> Under <a href="https://www.law.cornell.edu/cfr/text/16/436.2" '
         'rel="noopener nofollow" target="_blank">16 CFR 436.2</a>, the brand must give you its '
         "franchise disclosure document at least 14 calendar days before you sign or pay anything. "
         "Item 7 of that document estimates your initial investment, which is a good cross-check "
         "on your budget.</li>"
         f"<li><strong>Directory check.</strong> Under {_SOP_A}, a brand that meets the FTC franchise "
         f"definition must be on the {_DIR_A} before an SBA lender can approve the loan. A new or "
         "smaller brand may not be listed yet.</li>"
         "<li><strong>Signed agreement before funding.</strong> On a 7(a), the lender needs the "
         "executed franchise agreement before disbursing.</li>"
         "<li><strong>Two agreements at once.</strong> If you still operate under the old brand at "
         "closing, every agreement that meets the FTC definition must be on the Directory, or the "
         "application can't proceed.</li></ul>"),
        ("How an SBA Loan Can Fund It",
         "<p>Converting, expanding or renovating an existing building is an eligible use of SBA "
         "proceeds. If you already own the hotel, there's no change of ownership, so Appendix 15's "
         "purchase rules don't apply. Instead:</p>"
         "<ul>"
         "<li><strong>Term.</strong> A loan with mixed uses can run up to 25 years if 51% or more of "
         "the proceeds go to real estate; otherwise the maturity is blended.</li>"
         "<li><strong>Equity.</strong> The SOP's fixed 10% minimums apply to start-ups and changes "
         "of ownership. For an existing owner, the lender decides whether your equity and "
         "debt-to-worth are acceptable, so ask early.</li>"
         "<li><strong>Construction rules.</strong> Work over $350,000 brings bonding or lender "
         "construction monitoring, and renovation triggers a historic review. See the PIP guide.</li>"
         "<li><strong>Existing mortgage.</strong> Some owners refinance the current loan into the "
         "same SBA loan, which has its own eligibility rules. The "
         '<a href="/sba-loans/articles/sba-504-refinance/">504 refinance program</a> is one option '
         "for the real estate.</li>"
         "</ul>"),
        ("Worked Example: Converting a 64-Room Independent",
         "<p><strong>Illustrative numbers, not a quote.</strong> An owner converts to a mid-scale "
         f"brand. Building work is {d(C_BLDG)}, FF&amp;E and technology {d(C_FFE)}, an assumed "
         f"initial franchise fee of {d(C_FEE)} and {d(C_SOFT)} of soft costs. The hotel earns "
         f"{d(C_NOI)} of net operating income and pays {d(C_EXIST_DS)} a year on its current "
         f"mortgage. Rate assumed at {C_RATE}%.</p>"
         + table(["Item", "Amount"], [
             ["Conversion budget", d(C_TOTAL)],
             ["Real estate share", f"{pct(C_RE_SHARE)} (51% or more allows up to 25 years)"],
             ["Monthly payment over 25 years", d(c_pmt25)],
             ["Monthly payment over 10 years", d(c_pmt10)],
             ["Debt coverage today", f"{c_dsc_now:.2f}x"],
             ["Coverage, 25-year term", f"{c_dsc_25:.2f}x"],
             ["Coverage, 10-year term", f"{c_dsc_10:.2f}x"],
         ])
         + f"<p>On today's income, the 25-year structure keeps coverage at {c_dsc_25:.2f}x, above "
         "the 1.25x many lenders want. A 10-year term would drop it to "
         f"{c_dsc_10:.2f}x, below that line. Lenders count the post-conversion lift in room rate as upside, not as "
         "the way you repay. That's why the term matters more than the brand's rate projections.</p>"),
        ("Before You Sign With the New Brand",
         "<ol>"
         "<li><strong>Price the exit</strong> from your current agreement, if any.</li>"
         "<li><strong>Read the FDD</strong>, especially Items 5, 6 and 7 on fees and investment.</li>"
         "<li><strong>Confirm the brand is on the SBA Franchise Directory.</strong></li>"
         "<li><strong>Tag the budget</strong> as building work vs FF&amp;E to check the 51% line.</li>"
         "<li><strong>Talk to lenders before you sign.</strong> A franchise agreement with a fixed "
         "opening date and no funding in place is a risky place to be.</li>"
         "</ol>"
         f'<p>Rates for conversion loans follow the same market as other hotel loans: see <a href="{S_RATE}">'
         "hotel loan rates for 2026</a>.</p>" + CTA),
    ],
    "faqs": [
        ("What is a hotel flag conversion?",
         "Changing a hotel's brand: an independent joining a brand, or a branded hotel switching to a "
         "different one. It usually comes with a new franchise agreement and a conversion PIP."),
        ("Can I use an SBA loan to convert my hotel to a franchise?",
         "Often. Converting or renovating an existing building is an eligible use, and the new brand "
         "must be on the SBA Franchise Directory if it meets the FTC franchise definition."),
        ("How long can a conversion loan run?",
         "If at least 51% of proceeds go to real estate and you aren't buying the business, up to 25 "
         "years. Otherwise the term is blended by use of proceeds."),
        ("Will a lender count the higher room rate after conversion?",
         "Generally only as support. Lenders size the loan on current cash flow and treat the "
         "post-conversion lift as upside."),
        ("How much do I need to put in?",
         "For an owner who isn't buying, the SOP sets no fixed percentage; the lender decides whether "
         "equity is adequate. Many will still want some cash in the project."),
    ],
    "related": [
        ("/hotel-financing.html", "Hotel financing guide"),
        (S_PIP, "Hotel PIP financing"),
        (S_FLAG, "Flagged vs independent hotels"),
        ("/sba-loans/articles/sba-504-refinance/", "SBA 504 refinance"),
        ("/sba-loans/articles/sba-loan-franchise-acquisition/", "SBA franchise loans"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, FTC_436, FRANCHISE_DIR, MAT, SBA_7A],
},
# ================================================================ 4
{
    "slug": "hotel-experience-sba-loan",
    "crumb": "Hotel Experience Lenders Want",
    "title": "Hotel Experience for an SBA Loan: What Lenders Want | Axiant",
    "og_title": "How Much Hotel Experience Do SBA Lenders Want?",
    "h1": "How Much Hotel Experience Do SBA Lenders Want?",
    "headline": "How Much Hotel Experience Do SBA Lenders Want?",
    "lede": "The SBA sets no minimum years. Lenders still have to document who will run the hotel, "
            "and existing owners get two real advantages under the 2026 rules",
    "meta_desc": "Hotel experience for an SBA loan: what the SOP requires, what lenders commonly ask, how to show it with a GM or manager, and the Business Expansion rules for owners.",
    "article_desc": "What SBA lenders mean by hotel experience, how first-time buyers can show "
                    "it, and how existing hotel owners qualify under Business Expansion rules.",
    "keywords": "hotel experience sba loan, first time hotel buyer sba, buy a hotel with no "
                "experience, hotel general manager sba loan, sba business expansion hotel",
    "quick_answer": "SBA rules set no minimum years of hotel experience, but lenders must document "
                    "your management depth and who runs the property day to day. Many lenders expect "
                    "prior hotel ownership or general manager time. A first-time buyer can bridge the "
                    "gap with a strong GM or a manager. An owner with two or more years of hotel "
                    "operations buying another hotel can qualify at <strong>1.15x</strong> coverage "
                    "instead of 1.25x. Axiant Partners, a broker in Boca Raton, finds hotel lenders. "
                    "Typical ranges, not a quote.",
    "sections": [
        ("What the SBA Actually Requires",
         f"<p>{_SOP_A} asks lenders to weigh the depth of management experience in the industry "
         "or a related one. On a purchase, Appendix 15 also requires a written description of your "
         "industry experience and management team, and of how daily operations will run if you "
         "aren't on site every day. There is no fixed number of years. That's why the answer "
         f"varies so much by lender, and it's covered here rather than in the {PILLAR} overview.</p>"),
        ("What Lenders Commonly Look For",
         "<p>These are common lender practices, not SBA rules:</p>"
         "<ul>"
         "<li><strong>Prior ownership</strong> of a hotel of similar size and service level is the "
         "strongest case.</li>"
         "<li><strong>General manager or regional experience</strong>, often a few years, with "
         "responsibility for the P&amp;L, revenue management and staffing.</li>"
         "<li><strong>Related experience</strong> such as multi-unit restaurants, property "
         "management or senior living can count when paired with an experienced GM.</li>"
         "<li><strong>Brand approval.</strong> Flagged hotels need the franchisor to approve you as "
         "a franchisee. That is a separate test from the lender's, but lenders notice it.</li>"
         "</ul>"
         "<p>Strong experience often moves a lender on other terms too: more willingness on an "
         "independent, a smaller equity ask, or a faster approval.</p>"),
        ("How a First-Time Buyer Can Show It",
         "<ul>"
         "<li><strong>Hire the GM before closing.</strong> Include the GM's resume and a signed "
         "offer letter in the application, plus how long the GM has run similar hotels.</li>"
         "<li><strong>Keep the seller's team.</strong> A transition agreement with the seller and "
         "key staff can help, and lenders often like a seller who stays on for a period.</li>"
         "<li><strong>Use a management company carefully.</strong> A third-party manager can supply "
         "experience. Unless its agreement is part of a listed brand's disclosure documents, the "
         "lender must check it doesn't give the manager sole control of staff, finances and bank "
         "accounts. If it does, you become an ineligible passive owner.</li>"
         "<li><strong>Start smaller.</strong> A first hotel with fewer rooms and a strong flag is "
         'easier to place. See <a href="' + S_FLAG + '">flagged vs independent hotels</a>.</li>'
         "<li><strong>Write a real operating plan</strong> that covers revenue management, staffing, "
         "sales and capital spending, not just a resume.</li>"
         "</ul>"),
        ("If You Already Own a Hotel",
         "<p>Under Appendix 15, an existing business that has operated for at least two full fiscal "
         "years under its current owners, buying 100% of another business in the same four-digit "
         "NAICS industry group, is a <strong>Business Expansion</strong>. For hotels, that group is "
         "traveler accommodation. Two rules then work in your favor:</p>"
         + table(["", "First hotel (Initial Acquisition)", "Second hotel (Business Expansion)"], [
             ["SBA minimum equity", "10%, can't be reduced", "10%, lender may reduce or eliminate"],
             ["Debt service coverage", "1.25x", "1.15x"],
             ["Condition for less equity", "Not available", "Enough liquidity, and no negative net worth at last year-end"],
         ])
         + "<p>If the lender waives the equity, it can't add dedicated working capital to the loan "
         "within 90 days. Working capital for the deal has to come from cash or a line of credit.</p>"),
        ("Worked Example: What 1.15x Is Worth",
         "<p><strong>Illustrative numbers, not a quote.</strong> The hotel being bought has "
         f"{d(E_CF)} a year of cash flow available for debt service. Rate {E_RATE}%, 25 years.</p>"
         + table(["", "First hotel at 1.25x", "Second hotel at 1.15x"], [
             ["Maximum annual debt service", d(e_ds_125), d(e_ds_115)],
             ["Largest loan that supports", d(e_loan_125, 1000), d(e_loan_115, 1000)],
         ])
         + f"<p>The same hotel supports about {d(e_loan_115 - e_loan_125, 1000)} more debt for an "
         "experienced operator, before any equity waiver. Lenders can still set tighter coverage "
         "than the SBA minimum.</p>"),
        ("Checklist",
         "<ol>"
         "<li><strong>Resume</strong> for every owner and the GM, focused on hotel P&amp;L results.</li>"
         "<li><strong>Operating history</strong> of hotels you run now: financials and STR or brand reports.</li>"
         "<li><strong>Management plan</strong> showing who runs the hotel day to day.</li>"
         "<li><strong>Any management agreement</strong>, reviewed for control terms before you apply.</li>"
         "<li><strong>Franchisor approval status</strong> if the hotel is flagged.</li>"
         "</ol>"
         f'<p>Financing a renovation after you buy? See <a href="{S_PIP}">hotel PIP financing</a>.</p>'
         + CTA),
    ],
    "faqs": [
        ("Can I buy a hotel with no hotel experience?",
         "Sometimes. SBA rules set no minimum years, but lenders must document management. First-time "
         "buyers usually need an experienced GM, a strong brand or a manager whose agreement passes "
         "the passive-business review."),
        ("How many years of hotel experience do lenders want?",
         "There's no SBA number. Many lenders look for prior hotel ownership or a few years as a "
         "general manager with P&L responsibility."),
        ("Can a hotel management company count as my experience?",
         "It can help, but the lender must make sure the agreement doesn't make you a passive owner, "
         "unless it's part of a listed brand's disclosure documents."),
        ("Is it easier to finance a second hotel?",
         "Often. An owner with two full years of operations buying another hotel can qualify at "
         "1.15x coverage, and the lender may reduce or waive the 10% equity."),
        ("Does franchisor approval replace lender approval?",
         "No. The brand approves you as a franchisee and the lender approves the loan. Lenders "
         "consider the brand's approval, but they make their own decision."),
    ],
    "related": [
        ("/hotel-financing.html", "Hotel financing guide"),
        (S_FLAG, "Flagged vs independent hotels"),
        (S_RATE, "Hotel loan rates 2026"),
        ("/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/", "Buying a business with 5% down"),
        ("/sba-loans/articles/what-do-lenders-look-for-sba-loan-approval/", "What SBA lenders look for"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, SBA_7A, FRANCHISE_DIR],
},
# ================================================================ 5
{
    "slug": "typical-hotel-loan-rates-2026",
    "crumb": "Hotel Loan Rates 2026",
    "title": "Hotel Loan Rates 2026: SBA, Bank, CMBS, Bridge | Axiant",
    "og_title": "Typical Hotel Loan Rates and Terms in 2026",
    "h1": "Typical Hotel Loan Rates and Terms in 2026",
    "headline": "Typical Hotel Loan Rates and Terms in 2026",
    "lede": "Where hotel loan rates sit in November 2026, computed from prime and Treasury yields, "
            "with payments, fees and prepayment terms",
    "meta_desc": f"Hotel loan rates in November 2026: SBA 7(a) capped at {R_7A_CAP:.2f}%, 504 about "
                 f"{R_504_LO:.1f}-{R_504_HI:.1f}% blended, CMBS {R_CMBS_LO:.1f}-{R_CMBS_HI:.1f}%, bridge 9-12%, with payments and fees.",
    "article_desc": "Typical 2026 hotel loan rates and terms by program, computed from current prime "
                    "and Treasury yields, with payments, fees and prepayment rules.",
    "keywords": "hotel loan rates, hotel loan rates 2026, sba hotel loan rates, hotel mortgage rates, "
                "hotel cmbs rates, hotel bridge loan rates",
    "quick_answer": f"In November 2026, SBA 7(a) hotel loans over $350,000 are capped at "
                    f"<strong>{R_7A_CAP:.2f}%</strong> variable (prime {PRIME:.2f}% plus 3%). A 504 "
                    f"blends to about <strong>{R_504_LO:.1f}-{R_504_HI:.1f}%</strong> on the borrowed "
                    f"share. CMBS prices near <strong>{R_CMBS_LO:.1f}-{R_CMBS_HI:.1f}%</strong> fixed "
                    "at today's 10-year Treasury, and bridge loans run about "
                    "<strong>9-12%</strong> plus points. Axiant Partners, a broker in Boca Raton, "
                    "compares hotel lenders. Typical ranges, not a quote.",
    "sections": [
        ("Rates at a Glance, November 2026",
         f"<p>This is the rate companion to {PILLAR}. For which program fits which deal, see {CMP}. "
         "Here the numbers are rebuilt from today's benchmarks so you can check any quote.</p>"
         + table(["Program", "How it's priced", "Typical rate now", "Term"], [
             ["SBA 7(a), over $350K", "Prime + up to 3.0% (SBA cap), usually variable",
              f"Up to {R_7A_CAP:.2f}%; lenders may price below", "Up to 25 years on real estate"],
             ["SBA 504", "Bank first lien (~50%) + fixed CDC debenture (~40%)",
              f"About {R_504_LO:.1f}-{R_504_HI:.1f}% blended", "10, 20 or 25 years on the debenture"],
             ["CMBS", "10-year Treasury + 2.50-4.00%",
              f"About {R_CMBS_LO:.1f}-{R_CMBS_HI:.1f}% fixed", "10-year balloon, 25-30 year amortization"],
             ["Bank or life company", "Case by case, larger sponsors", "6-7.5% as published in May 2026",
              "5-10 year balloon"],
             ["Bridge", "Fixed or SOFR-based, interest-only", "About 9-12% plus 1-4 points",
              "12-36 months"],
         ])
         + f"<p>Prime is {PRIME:.2f}% (Federal Reserve H.15, November 11, 2026) and the 10-year "
         f"Treasury {T10:.2f}% (November 10). The 504 blend uses the 6.984% effective debenture "
         "rate from NADCO's October 2026 example and a 7-9% bank first lien. The CMBS spread and "
         "the bank and bridge ranges are the ones on our comparison page. Bank rates there "
         "were published in May 2026, and Treasury yields have risen since.</p>"),
        ("What a $3,000,000 Hotel Loan Costs Each Month",
         table(["Rate", "Monthly payment, 25-year amortization", "Annual debt service"], [
             [f"{r:.2f}%", d(p), d(p * 12)] for r, p in r_pay.items()
         ])
         + f"<p>A bridge loan at 10% interest-only costs about {d(r_bridge_io)} a month on the same "
         f"{d(R_LOAN)}, before points. It's cheaper each month than amortizing debt but has to be "
         f"refinanced. Each 1% of rate on this loan moves the payment by roughly "
         f"{d((r_pay[10.0] - r_pay[7.0]) / 3)} a month. For SBA cap tables on smaller loans, see "
         '<a href="/sba-loans/articles/typical-sba-loan-rates-2026/">typical SBA loan rates</a>.</p>'),
        ("What Moves a Hotel's Rate",
         "<ul>"
         "<li><strong>Coverage.</strong> Hotels carry more income volatility than offices or "
         "warehouses, so lenders price for it. Higher debt coverage gets better pricing.</li>"
         "<li><strong>Flag and segment.</strong> Strong brands and limited-service hotels usually "
         'price better than weak independents. See <a href="' + S_FLAG + '">flagged vs '
         "independent</a>.</li>"
         "<li><strong>Trend.</strong> Lenders read the trailing-12-month revenue per available room "
         "against the competitive set.</li>"
         "<li><strong>PIP status.</strong> An unfunded PIP raises risk. A funded one, held by the "
         'lender, lowers it. See <a href="' + S_PIP + '">PIP financing</a>.</li>'
         "<li><strong>Operator.</strong> Experienced owners get better terms; see "
         f'<a href="{S_EXP}">hotel experience</a>.</li>'
         "<li><strong>Location.</strong> In towns under about 50,000 people, a "
         f'<a href="{USDA_HOTEL}">USDA hotel loan</a> can be another option.</li>'
         "</ul>"),
        ("Fees and Prepayment",
         table(["Program", "Upfront", "Paying off early"], [
             ["SBA 7(a)", f"Guaranty fee, about {d(r_fee)} on a {d(R_LOAN)} loan (FY2027 estimate)",
              "Subsidy recoupment fee of 5%, 3%, 1% in years 1-3 on loans of 15+ years"],
             ["SBA 504", "Debenture and CDC fees, usually financed", "Declining prepayment premium over the first half of the term"],
             ["CMBS", "Origination and third-party costs", "Defeasance or yield maintenance"],
             ["Bridge", "1-4 points", "Usually open or a short lockout"],
         ])
         + "<p>On a 7(a), the recoupment fee applies only if you voluntarily prepay more than 25% "
         "of the loan in a year during the first three years. Prepaying 30% of a "
         f"{d(R_LOAN)} loan would cost about {d(r_recoup[0])} in year one, {d(r_recoup[1])} in year "
         f"two and {d(r_recoup[2])} in year three. 504 details: "
         '<a href="/sba-loans/articles/sba-504-loan-fees/">504 fees</a> and the '
         '<a href="/sba-loans/articles/sba-504-loan-amortization-schedule/">amortization '
         "schedule</a>, which shows the prepayment premium.</p>"),
        ("How to Read a Hotel Term Sheet",
         "<ol>"
         "<li><strong>Find the index and the spread.</strong> A 7(a) quote should say prime plus X; "
         "check it doesn't exceed prime plus 3% on a loan over $350,000.</li>"
         "<li><strong>Check how often it adjusts.</strong> Many 7(a) loans reset quarterly.</li>"
         "<li><strong>Ask for the amortization and the maturity.</strong> A low rate with a 5-year "
         "balloon is a different loan from a fully amortizing 25-year SBA loan.</li>"
         "<li><strong>Add every fee</strong> and compare total cost, not the headline rate.</li>"
         "<li><strong>Read the prepayment section</strong> if you might sell or refinance within five years.</li>"
         "</ol>" + CTA),
    ],
    "faqs": [
        ("What are hotel loan rates right now?",
         f"In November 2026: SBA 7(a) up to {R_7A_CAP:.2f}% variable on loans over $350,000, SBA 504 "
         f"about {R_504_LO:.1f}-{R_504_HI:.1f}% blended, CMBS about {R_CMBS_LO:.1f}-{R_CMBS_HI:.1f}% "
         "fixed and bridge loans about 9-12% plus points. These are typical ranges, not quotes."),
        ("What is the maximum rate on an SBA hotel loan?",
         f"For a variable 7(a) loan over $350,000, prime plus 3.0%. With prime at {PRIME:.2f}%, that "
         f"is {R_7A_CAP:.2f}%. Smaller loans have higher caps."),
        ("Are hotel loans more expensive than other commercial real estate loans?",
         "Usually somewhat, because hotel income changes nightly and lenders price for that volatility."),
        ("Is a 504 cheaper than a 7(a) for a hotel?",
         "Often on rate, because the debenture is fixed for its full term. A 504 needs at least 15% "
         "down on a hotel, though, and 20% for a business two years old or less."),
        ("Is there a prepayment penalty on an SBA hotel loan?",
         "On a 7(a) of 15 years or longer, a fee of 5%, 3% or 1% applies to voluntary prepayments over "
         "25% in any of the first three years. A 504 debenture has its own declining premium."),
    ],
    "related": [
        ("/hotel-financing.html", "Hotel financing guide"),
        ("/commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/", "SBA vs CMBS vs bank hotel loans"),
        ("/sba-loans/articles/typical-sba-loan-rates-2026/", "Typical SBA loan rates"),
        ("/sba-loans/articles/sba-504-loan-rates/", "SBA 504 loan rates"),
        ("/commercial-bridge-loans/articles/typical-commercial-bridge-loan-rates-2026/", "Commercial bridge loan rates"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [H15, SOP, RECOUP, C504, FEES, SBA_504],
},
]
