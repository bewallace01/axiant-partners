# -*- coding: utf-8 -*-
"""USDA Business & Industry (B&I) guaranteed loans - SBA plan Cluster 3, spokes and hub.

The pillar /usda-business-loans.html is built from cluster_usda_pillar.py: a root page needs its
own crumb trail (Home > SBA Loans > USDA Business Loans), while these spokes sit under the new
hub usda-business-loans/articles/ with the pillar as their parent, and article_v2 takes the trail
from the cluster, not the article.

    python scripts/build-cluster.py usda_pillar --apply
    python scripts/build-cluster.py usda --apply

Rules read on 2026-11-13 from 7 CFR part 5001 (eCFR, current; the OneRD guarantee rule that
replaced 4279/4287 for B&I): 5001.3 rural area, 5001.105 eligible projects and equity table,
5001.115/118/122 ineligible projects and uses, 5001.126 borrower eligibility, 5001.203 appraisals,
5001.306 feasibility study, 5001.401 rates, 5001.402 terms, 5001.406 loan limits, 5001.407
guarantee percentage, 5001.454/455 fees. Fee rates and guarantee percentages from the FY2026
OneRD annual notice (FR Doc. 2026-04581, 91 FR 11272, March 9, 2026, effective October 1, 2025),
the latest published when this was written; no FY2027 notice was found. The rd.usda.gov program
page returned 403 to every fetch, so no fact rests on it alone. Every dollar figure is computed
below. Never names a lender; "about 80% LTV" is framed as lender practice (plan content rules).
"""
from cluster_table import table
from sba_sources import SOP, SBA_7A

# ---- sources --------------------------------------------------------------------------------
def _cfr(sec, name, desc):
    return (f"https://www.law.cornell.edu/cfr/text/7/5001.{sec}", f"7 CFR 5001.{sec}: {name}", desc)

RURAL = _cfr("3", "Definitions", "The B&amp;I definition of a rural area: outside any city or town of more "
             "than 50,000 people and its contiguous urbanized area.")
PROJ = _cfr("105", "Eligible B&amp;I projects and requirements", "Eligible uses, hotels and assisted "
            "living, and the minimum equity table for existing and new businesses.")
INEL = _cfr("115", "Ineligible projects", "Projects no OneRD guarantee can cover, including golf courses, "
            "lines of credit and passive commercial rental.")
USES = _cfr("122", "Ineligible uses of loan funds", "Uses loan proceeds cannot pay for, including "
            "loan finder or broker fees.")
BORR = _cfr("126", "Borrower eligibility", "Who can borrow: entities, tribes, public bodies and "
            "individuals who are U.S. citizens or permanent residents.")
APPR = _cfr("203", "Appraisals", "Appraisal rules, including deducting going-concern value before "
            "collateral is discounted.")
FEAS = _cfr("306", "Specific application requirements for B&amp;I projects", "When a feasibility study "
            "is required, including loans over $1 million to a new business.")
RATE = _cfr("401", "Interest rate provisions", "Rates are negotiated between lender and borrower; "
            "variable rates adjust no more than quarterly.")
TERM = _cfr("402", "Term length, loan schedule, and repayment", "Terms up to the useful life of the "
            "assets, capped at 40 years, with no balloon payments.")
LIMIT = _cfr("406", "Guaranteed loan amounts", "B&amp;I loans of up to $25 million per borrower.")
FEE = _cfr("454", "Guarantee fee", "How the one-time guarantee fee is calculated, the 5% ceiling for "
           "B&amp;I, and the reduced-fee criteria.")
RET = _cfr("455", "Periodic guarantee retention fee", "The annual fee on the guaranteed share of the "
           "outstanding balance, fixed for the life of the loan.")
NOTICE = ("https://www.govinfo.gov/content/pkg/FR-2026-03-09/pdf/2026-04581.pdf",
          "OneRD Annual Notice of Fee Rates and Guarantee Percentages, FY2026 (91 FR 11272)",
          "B&amp;I guarantee fee 3.0%, retention fee 0.55% and guarantee of 85% under $5 million or 80% "
          "from $5 million to $25 million; reduced-fee tier 1.0% and 0.50%.")
MAP = ("https://eligibility.sc.egov.usda.gov/eligibility/welcomeAction.do",
       "USDA Rural Development Property Eligibility Map",
       "The map the rule itself points to for checking whether an address is in an eligible area.")
PROGRAM = ("https://www.rd.usda.gov/programs-services/business-programs/business-industry-loan-guarantees",
           "USDA Rural Development: Business &amp; Industry Loan Guarantees",
           "Program overview from USDA Rural Development.")


def _a(src, text=None):
    return f'<a href="{src[0]}" rel="noopener nofollow" target="_blank">{text or src[1]}</a>'


# ---- numbers --------------------------------------------------------------------------------
PRIME = 7.00          # Fed H.15 bank prime, Nov 11 2026 (same as cluster_hotel_spokes)
FEE_STD, RET_STD = 3.0, 0.55      # FY2026 notice, B&I
FEE_RED, RET_RED = 1.0, 0.50      # FY2026 notice, B&I reduced fee
G_UNDER5, G_5TO25 = 85, 80        # FY2026 guarantee percentages


def pmt(p, rate_pct, years):
    r, n = rate_pct / 1200, years * 12
    return p * r / (1 - (1 + r) ** -n)


def guar_pct(loan):
    return G_UNDER5 if loan < 5_000_000 else G_5TO25


def g_fee(loan, rate=FEE_STD, pct=None):
    return loan * (pct or guar_pct(loan)) / 100 * rate / 100


def retention_total(loan, rate_pct, years, ret=RET_STD, pct=None):
    """Annual retention fee on the guaranteed share of the year-start balance, summed over the life."""
    pct = pct or guar_pct(loan)
    bal, tot, m = loan, 0.0, pmt(loan, rate_pct, years)
    r = rate_pct / 1200
    for _ in range(years):
        tot += bal * pct / 100 * ret / 100
        for _ in range(12):
            bal -= m - bal * r
    return tot


def d(x):
    return f"${x:,.0f}"


def d_round(x, to=10):
    return f"${round(x / to) * to:,.0f}"


CTA = ('<p><a href="/match.html">Get matched with USDA and SBA lenders</a>, or talk to a specialist: '
       '(561) 268-0465.</p>')

CLUSTER = {
    "pillar": "usda-business-loans.html",
    "hub": "usda-business-loans/articles",
    "crumb": "USDA Business Loans",
    "cta_inline": "Check whether your project fits USDA",
    "cta_button": "Talk to a Specialist",
    "hub_title": "USDA Business Loan Guides | Axiant Partners",
    "hub_h1": "USDA Business Loan Articles",
    "hub_lede": "Rural eligibility, fees, hotels and how USDA B&I compares with SBA 7(a)",
    "hub_desc": "Guides to USDA Business & Industry guaranteed loans: which towns qualify, the "
                "guarantee and retention fees, hotel loans, and USDA B&I vs SBA 7(a).",
    "hub_quick_answer": "USDA Business &amp; Industry loans are bank loans with a USDA guarantee, for "
                        "businesses outside cities of more than 50,000 people. They go up to "
                        "<strong>$25 million</strong> per borrower, against <strong>$5 million</strong> "
                        "on an SBA 7(a). Axiant Partners, a broker in Boca Raton, matches rural "
                        "projects with lenders that use the program.",
    "hub_intro": "The B&amp;I program is narrower than SBA lending on location and wider on size and "
                 "term. These guides take one question each. Start with "
                 '<a href="/usda-business-loans.html">USDA business loans</a> for the overview, '
                 'or see <a href="/sba-loans.html">SBA loans</a> if your project is in a city.',
    "hub_cta_h2": "Have a project in a small town?",
    "hub_cta_p": "Send us the address, the project cost and what you are buying or building. We will "
                 "tell you whether USDA, SBA or a conventional loan is the realistic route. "
                 "Or call (561) 268-0465.",
}

_PILLAR = '<a href="/usda-business-loans.html">USDA Business &amp; Industry loans</a>'
_ELIG = '<a href="/usda-business-loans/articles/usda-eligible-areas/">USDA eligible areas</a>'
_VS = '<a href="/usda-business-loans/articles/usda-b-and-i-vs-sba-7a/">USDA B&amp;I vs SBA 7(a)</a>'
_HOTEL = '<a href="/usda-business-loans/articles/usda-hotel-loans/">USDA hotel loans</a>'
_FEES = '<a href="/usda-business-loans/articles/usda-b-and-i-loan-rates-fees/">USDA B&amp;I rates and fees</a>'

# ---- spoke 1: eligible areas ---------------------------------------------------------------
ELIG = {
    "slug": "usda-eligible-areas",
    "crumb": "USDA Eligible Areas",
    "title": "USDA B&I Eligible Areas: Is Your Town Rural? | Axiant",
    "og_title": "USDA B&I Eligible Areas: How to Tell if Your Town Counts as Rural",
    "h1": "USDA B&amp;I Eligible Areas: How to Tell if Your Town Counts as Rural",
    "headline": "USDA B&I Eligible Areas: How to Tell if Your Town Counts as Rural",
    "lede": "The 50,000-person test, the urbanized-area catch that trips up edge-of-town sites, "
            "and how to check an address on USDA's map before you sign anything",
    "meta_desc": "USDA B&I eligible areas: the 50,000 population rule, the urbanized-area exclusion, "
                 "how to read USDA's eligibility map, and what to do if your site is borderline.",
    "article_desc": "How USDA defines a rural area for Business & Industry loans and how to check "
                    "whether a property address qualifies.",
    "keywords": "usda eligible areas, usda b&i eligibility map, usda rural area definition business, "
                "is my town eligible for usda business loan, 50000 population usda",
    "quick_answer": "For a USDA Business &amp; Industry loan, the project must sit outside any city or "
                    "town of more than <strong>50,000</strong> people <strong>and</strong> outside the "
                    "urbanized area that touches such a city, using the latest decennial census. USDA "
                    "points to its Property Eligibility Map to check an address. Axiant Partners, a broker "
                    "in Boca Raton, can check a site and match the project with B&amp;I lenders. This is "
                    "the federal rule, not a lender's quote.",
    "sections": [
        ("The Rule in One Sentence",
         f"<p>Under {_a(RURAL, '7 CFR 5001.3')}, a rural area is any part of a state that is not in a city "
         "or town of more than 50,000 inhabitants and not in the urbanized area contiguous and adjacent "
         "to such a city or town. USDA uses the latest decennial census to decide. That is all of it, and "
         "the second half matters more than people expect.</p>"
         "<p>So the question isn't how many people live in your town. It is whether the parcel sits inside "
         "the built-up area that has grown out from a bigger city. A town of 8,000 can fail if it has "
         "become a suburb of a metro. A town of 45,000 standing on its own can pass.</p>"
         f"<p>This page covers only location. For the program itself, see {_PILLAR}.</p>"),
        ("How Typical Locations Fall Under the Rule",
         "<p>These are applications of the rule's text to common situations, not determinations. Only "
         "USDA's own review decides a specific address.</p>"
         + table(["Where the site is", "Usual result", "Why"], [
             ["Remote town of 30,000", "Generally eligible", "Under 50,000 and not in a larger city's urbanized area"],
             ["City of 62,000", "Not eligible", "Over 50,000 inhabitants"],
             ["Suburb of 9,000 in a metro", "Usually not eligible", "In the urbanized area contiguous to a city over 50,000"],
             ["Just past a city's urban edge", "Often eligible", "Outside both the city and its urbanized area"],
             ["Site split by the boundary", "Partly eligible", "USDA guarantees only the share located in the rural area"],
         ])
         + "<p>The last row is easy to miss. Under "
         f"{_a(PROJ, '7 CFR 5001.105(c)')}, when a project sits partly in a rural area and partly outside "
         "it, the guarantee covers only the amount needed for the rural part.</p>"),
        ("How to Check an Address on USDA's Map",
         f"<p>The rule names the {_a(MAP, 'USDA Property Eligibility Map')} as the place where areas "
         "next to an urbanized area are shown as ineligible. It is run from census tract data.</p>"
         "<ol>"
         "<li><strong>Use the business programs map.</strong> The site also has housing maps, and USDA's "
         "housing programs use different rules. Pick the business program option that covers B&amp;I.</li>"
         "<li><strong>Enter the exact property address,</strong> not the mailing address of the business "
         "or the seller's office.</li>"
         "<li><strong>Read the shading at parcel level.</strong> Zoom in. Boundaries often run along "
         "highways and town lines, and a site near one can land on either side.</li>"
         "<li><strong>Save the result</strong> as a screenshot or printout with the date. Your lender will "
         "still confirm it, but it saves a wasted application.</li>"
         "<li><strong>Check every parcel.</strong> A hotel with overflow parking across the road, or a plant "
         "with a separate warehouse, may cover more than one tract.</li>"
         "</ol>"
         "<p>Eligibility is a condition of approval, not something to fix later. The rule says applications "
         "cannot be approved subject to meeting the rural area requirement.</p>"),
        ("If Your Site Is Borderline",
         "<p>Two exceptions in 7 CFR 5001.3 can pull a site inside an urbanized area back into eligibility. "
         "Both depend on a determination that the area is <strong>rural in character</strong>, made by "
         "the Under Secretary for Rural Development:</p>"
         "<ul>"
         "<li><strong>A large, spread-out urbanized area.</strong> It has two points on its boundary at "
         "least 40 miles apart and doesn't touch a city of more than 150,000 people or that city's "
         "urbanized area.</li>"
         "<li><strong>Close to a rural area.</strong> The site is in an urbanized area next to a city of "
         "more than 50,000 but within a quarter mile of a rural area.</li>"
         "</ul>"
         "<p>A unit of local government, such as the town or county, files the petition through the Rural "
         "Development State Director. Determinations are project specific, so a neighbor's approval "
         "doesn't carry over to your site. Allow for the time this takes before you set a closing date.</p>"
         "<p>Two kinds of projects can be outside rural areas entirely: cooperatives doing value-added "
         "agricultural processing for producers within 80 miles, and local food projects that meet the "
         "conditions in 5001.105(b)(15). For most hotels, plants and shops, the rural test applies.</p>"),
        ("What Location Doesn't Settle",
         "<p>Passing the map is only the first gate. A rural site still has to be an eligible project, "
         "with enough equity and collateral, and a lender willing to make it. Golf courses, racetracks, "
         "apartments and passive rental property are out wherever they are. Lenders also look harder at "
         "small markets, where resale value and demand are thinner.</p>"
         f"<p>For what the program will pay for, see {_PILLAR}. For hotels and motels specifically, see "
         f"{_HOTEL}. If your town is over the line, compare an SBA loan in {_VS}, since SBA has no "
         "population test.</p>"
         + CTA),
    ],
    "faqs": [
        ("What population counts as rural for a USDA business loan?",
         "For B&amp;I, any area outside a city or town of more than 50,000 inhabitants and outside the "
         "urbanized area contiguous and adjacent to that city, based on the latest decennial census."),
        ("Can a small town near a big city be ineligible?",
         "Yes. If the town sits inside the urbanized area attached to a city of more than 50,000, it is "
         "generally ineligible even if the town itself is small, unless a rural-in-character determination applies."),
        ("Where do I check whether an address is eligible?",
         "USDA's Rural Development Property Eligibility Map, using the business programs map rather than "
         "the housing maps. Your lender and USDA confirm it during the application."),
        ("Can I apply and fix the location question later?",
         "No. The rule says applications cannot be approved subject to meeting the rural area requirement."),
        ("What if part of my project is in an ineligible area?",
         "USDA guarantees only the amount needed to finance the part of the project located in the eligible rural area."),
        ("Do USDA housing maps apply to business loans?",
         "No. Housing programs use their own definitions, so use the business program view of the map for B&amp;I."),
    ],
    "related": [
        ("/usda-business-loans.html", "USDA business loans"),
        ("/usda-business-loans/articles/usda-hotel-loans/", "USDA hotel loans"),
        ("/usda-business-loans/articles/usda-b-and-i-vs-sba-7a/", "USDA B&I vs SBA 7(a)"),
        ("/usda-business-loans/articles/usda-b-and-i-loan-rates-fees/", "USDA B&I rates and fees"),
        ("/sba-loans.html", "SBA loans"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [RURAL, PROJ, MAP, INEL, PROGRAM],
}

# ---- spoke 2: USDA B&I vs SBA 7(a) ----------------------------------------------------------
VS_LOAN = 4_000_000
VS_RATE, VS_YRS = 8.0, 25
_vs_usda_fee = g_fee(VS_LOAN)
_vs_usda_ret1 = VS_LOAN * guar_pct(VS_LOAN) / 100 * RET_STD / 100
_vs_pay = pmt(VS_LOAN, VS_RATE, VS_YRS)

VS = {
    "slug": "usda-b-and-i-vs-sba-7a",
    "crumb": "USDA B&I vs SBA 7(a)",
    "title": "USDA B&I vs SBA 7(a): Which Loan Fits? | Axiant",
    "og_title": "USDA B&I vs SBA 7(a): Size, Location, Fees and Who Each Fits",
    "h1": "USDA B&amp;I vs SBA 7(a): Size, Location, Fees and Who Each Fits",
    "headline": "USDA B&I vs SBA 7(a): Size, Location, Fees and Who Each Fits",
    "lede": "Both put a federal guarantee behind a bank loan. They differ on where you can be, how big "
            "the loan can get, how long it runs and who can own the business",
    "meta_desc": "USDA B&I vs SBA 7(a) compared: $25M vs $5M limits, rural-only location, 40-year terms, "
                 "equity rules, fees and citizenship, with a rule-of-thumb for choosing.",
    "article_desc": "A side-by-side comparison of USDA Business & Industry guaranteed loans and SBA 7(a) "
                    "loans, with guidance on which fits which project.",
    "keywords": "usda b&i vs sba 7a, usda business loan vs sba loan, usda b&i or sba, "
                "rural business loan comparison, usda vs sba hotel loan",
    "quick_answer": "Pick <strong>USDA B&amp;I</strong> when the project is rural and needs more than the "
                    "SBA's <strong>$5 million</strong> 7(a) limit or a longer term: B&amp;I goes to "
                    "<strong>$25 million</strong> per borrower with terms up to the assets' useful life, "
                    "capped at <strong>40 years</strong>. Pick <strong>SBA 7(a)</strong> when the site is in "
                    "or near a city, or the deal is smaller and needs SBA's capped rates. Axiant Partners, "
                    "a broker in Boca Raton, compares both for a project. These are program rules, not quotes.",
    "sections": [
        ("Side by Side",
         table(["", "USDA B&amp;I", "SBA 7(a)"], [
             ["Where the business can be", "Rural areas only (outside cities over 50,000 and their urbanized areas)", "Anywhere in the U.S."],
             ["Maximum loan", "$25 million per borrower", "$5 million"],
             ["Guarantee share (FY2026)", "85% under $5M, 80% from $5M to $25M", "Set by the SBA by loan size"],
             ["Longest term", "Useful life of the assets, up to 40 years", "Up to 25 years on real estate"],
             ["Balloon payments", "Not allowed; must fully amortize", "Generally fully amortizing"],
             ["Interest rate", "Negotiated, no higher than the lender's customary rate", "Negotiated under SBA maximums"],
             ["Equity, existing business", "10% by one of three tests", "Lender and SBA judgment; 10% on a change of ownership"],
             ["Individual owners", "U.S. citizens or green-card holders", "U.S. citizens or nationals"],
             ["Lines of credit", "Ineligible", "Available through SBA line programs"],
         ])
         + f"<p>USDA rows come from 7 CFR part 5001 and the FY2026 annual notice; SBA rows from the "
         f"SBA's 7(a) program page and {_a(SOP, 'SOP 50 10 8.1')}. For the full USDA picture, see "
         f"{_PILLAR}.</p>"),
        ("Where USDA B&I Wins",
         "<ul>"
         "<li><strong>Size.</strong> A rural plant expansion, a larger hotel or an acquisition above $5 "
         "million can't fit in a single 7(a). Under "
         f"{_a(LIMIT, '7 CFR 5001.406(c)')}, B&amp;I goes to $25 million per borrower, counting existing "
         "B&amp;I balances.</li>"
         "<li><strong>Term.</strong> The maximum is the justified useful life of what's financed or pledged, "
         "up to 40 years. A long-lived building can carry a lower payment than a 25-year schedule.</li>"
         "<li><strong>Permanent residents.</strong> An individual borrower can be a U.S. citizen or a "
         "lawful permanent resident with a green card. The SBA now requires U.S. citizens or nationals "
         "for 7(a) owners.</li>"
         "<li><strong>Equity on paper.</strong> An existing business can meet the 10% test with balance "
         "sheet equity it already has, not only cash put into the project, which can lower the cash an "
         "established company brings.</li>"
         "</ul>"),
        ("Where SBA 7(a) Wins",
         "<ul>"
         "<li><strong>Location.</strong> Most U.S. businesses are in or next to a city of more than 50,000, "
         f"and B&amp;I can't help them. Check a site in {_ELIG}.</li>"
         "<li><strong>Rate caps.</strong> SBA sets maximum spreads on 7(a) loans. B&amp;I has no published "
         "cap; the rule only says the rate can't exceed what the lender charges on similar unguaranteed "
         "loans.</li>"
         "<li><strong>Lender supply.</strong> Many more banks make SBA loans than B&amp;I loans, so a small "
         "deal is usually quicker to place through SBA.</li>"
         "<li><strong>Smaller deals.</strong> On a few hundred thousand dollars, the fixed costs of an "
         "appraisal and a USDA application weigh more.</li>"
         "</ul>"),
        (f"Fees on the Same {d(VS_LOAN)} Loan",
         "<p><strong>Illustrative, not a quote.</strong> Here is the USDA side of a "
         f"{d(VS_LOAN)} loan at an assumed {VS_RATE:.2f}% over {VS_YRS} years, using the FY2026 B&amp;I "
         f"rates in the {_a(NOTICE, 'annual notice')}.</p>"
         + table(["USDA B&amp;I item", "How it's figured", "Amount"], [
             ["Guarantee percentage", "Under $5 million", f"{guar_pct(VS_LOAN)}%"],
             ["One-time guarantee fee", f"{d(VS_LOAN)} x {guar_pct(VS_LOAN)}% x {FEE_STD:.1f}%", d(_vs_usda_fee)],
             ["Retention fee, first year", f"Balance x {guar_pct(VS_LOAN)}% x {RET_STD:.2f}%", d(_vs_usda_ret1)],
             ["Retention fee, full term", "Same, on each year's balance", d_round(retention_total(VS_LOAN, VS_RATE, VS_YRS))],
             ["Monthly principal and interest", f"{VS_RATE:.2f}%, {VS_YRS} years", d(_vs_pay)],
         ])
         + "<p>The SBA also charges an upfront guaranty fee on the guaranteed share and an annual "
         "service fee, set each fiscal year. For the current SBA fee math on a real estate deal, see the "
         'worked example in <a href="/sba-100-percent-financing.html">100% SBA financing</a>. Compare '
         f"both all-in, including rate, rather than fee to fee. More detail on the USDA side is in {_FEES}.</p>"),
        ("A Simple Way to Choose",
         "<ol>"
         "<li><strong>Check the address first.</strong> If the site isn't rural, the choice is made.</li>"
         "<li><strong>Size the project.</strong> Over $5 million in one loan points to B&amp;I, or to an "
         "SBA 504 for real estate.</li>"
         "<li><strong>Look at ownership.</strong> If an owner holds a green card but isn't a citizen, "
         "B&amp;I may be the only guaranteed option.</li>"
         "<li><strong>Price both if the deal is rural and under $5 million.</strong> Rate, term, fees and "
         "equity can each tip it.</li>"
         "<li><strong>Ask about timing.</strong> USDA issues a conditional commitment before closing and a "
         "loan note guarantee after; build that into your contract dates.</li>"
         "</ol>"
         f"<p>Hotel buyers should also read {_HOTEL}, since both programs lend on lodging under different "
         'rules, and <a href="/hotel-financing.html">hotel financing</a> for the SBA side.</p>'
         + CTA),
    ],
    "faqs": [
        ("Is a USDA B&amp;I loan better than an SBA loan?",
         "Neither is better in general. B&amp;I fits rural projects that need more than $5 million or a longer "
         "term; SBA 7(a) fits businesses anywhere and smaller deals with capped rates."),
        ("Can a business use USDA B&amp;I in a city?",
         "Generally no. The project must be in a rural area, with narrow exceptions for certain cooperatives "
         "and local food projects."),
        ("Which program allows a bigger loan?",
         "USDA B&amp;I, at up to $25 million per borrower. A 7(a) loan tops out at $5 million."),
        ("Can a green-card holder get a USDA business loan?",
         "An individual borrower can be a U.S. citizen or a lawful permanent resident with a green card under "
         "7 CFR 5001.126. SBA 7(a) now requires owners to be U.S. citizens or nationals."),
        ("Does USDA cap interest rates like the SBA?",
         "No published cap. Rates are negotiated, and the lender can't charge more than it charges on similar "
         "loans without a guarantee."),
        ("Can USDA B&amp;I fund a line of credit?",
         "No. Lines of credit are ineligible; working capital is financed as a permanent term loan."),
    ],
    "related": [
        ("/usda-business-loans.html", "USDA business loans"),
        ("/sba-loans/articles/sba-7a-vs-504-loan/", "SBA 7(a) vs 504"),
        ("/usda-business-loans/articles/usda-eligible-areas/", "USDA eligible areas"),
        ("/usda-business-loans/articles/usda-b-and-i-loan-rates-fees/", "USDA B&I rates and fees"),
        ("/sba-loans.html", "SBA loans"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [LIMIT, TERM, RATE, BORR, PROJ, NOTICE, SBA_7A, SOP],
}

# ---- spoke 3: hotels -------------------------------------------------------------------------
H_PRICE, H_PIP, H_SOFT = 7_200_000, 900_000, 180_000
H_TOTAL = H_PRICE + H_PIP + H_SOFT
H_EQ_PCT = 20
H_EQ = H_TOTAL * H_EQ_PCT / 100
H_LOAN = H_TOTAL - H_EQ
H_RATE, H_YRS = 8.25, 25
H_PAY = pmt(H_LOAN, H_RATE, H_YRS)
H_DS = H_PAY * 12
# B&B owner's quarters example (5001.105(b)(8))
BB_PRICE, BB_SQFT, BB_OWNER = 900_000, 4_000, 800
BB_OUT = BB_PRICE * BB_OWNER / BB_SQFT

HOTEL = {
    "slug": "usda-hotel-loans",
    "crumb": "USDA Hotel Loans",
    "title": "USDA Hotel Loans: B&I Financing in Small Towns | Axiant",
    "og_title": "USDA Hotel Loans: Using B&I to Buy or Renovate a Hotel in a Small Town",
    "h1": "USDA Hotel Loans: Using B&amp;I to Buy or Renovate a Hotel in a Small Town",
    "headline": "USDA Hotel Loans: Using B&I to Buy or Renovate a Hotel in a Small Town",
    "lede": "Hotels, motels and B&amp;Bs are named in the B&amp;I rule. What the program covers, the two "
            "hotel-specific catches, and a worked purchase with a PIP",
    "meta_desc": "USDA hotel loans through B&I: eligibility of hotels and motels, going-concern value in "
                 "the appraisal, owner's quarters, equity, and an $8.28M worked example.",
    "article_desc": "How USDA Business & Industry guaranteed loans finance hotel and motel purchases, "
                    "renovations and PIPs in rural towns.",
    "keywords": "usda hotel loan, usda b&i hotel financing, rural hotel loan, usda loan for motel, "
                "small town hotel financing, usda b&i hospitality",
    "quick_answer": "Yes, USDA Business &amp; Industry loans can finance a hotel or motel in a rural town: "
                    "the rule lists hotels, motels and bed and breakfasts as eligible. Loans go to "
                    "<strong>$25 million</strong> per borrower, more than an SBA 7(a), with terms up to the "
                    "building's useful life, capped at <strong>40 years</strong>. The site must be outside "
                    "cities of more than 50,000 people and their urbanized areas. Axiant Partners, a broker "
                    "in Boca Raton, matches rural hotel deals with B&amp;I lenders. Ranges here aren't quotes.",
    "sections": [
        ("Hotels Are Named in the Rule",
         f"<p>{_a(PROJ, '7 CFR 5001.105(b)(8)')} lists tourist and recreation facilities, including hotels, "
         "motels, bed and breakfast establishments, resort trailer parks and campgrounds, run as a public "
         "or private commercial enterprise. Purchases, expansions, renovations and permanent working "
         "capital can all be part of the project, along with refinancing in some cases.</p>"
         "<p>That makes B&amp;I a real option for highway-exit motels, small-town flagged hotels and resort "
         "properties near parks and lakes, as long as the address passes the "
         f"{_ELIG} test. Timeshares and residential housing are excluded. For the program overall, see "
         f"{_PILLAR}.</p>"),
        ("Two Hotel Catches in the Appraisal and the Owner's Apartment",
         "<p><strong>Going-concern value comes out.</strong> Hotel appraisals usually value the property as "
         f"an operating business. {_a(APPR, '7 CFR 5001.203')} says any business or going-concern value must "
         "be deducted from the market value before the lender discounts collateral. So the collateral number "
         "is lower than the price you agreed, and the gap is part of why lenders ask hotel buyers for more "
         "equity or extra collateral.</p>"
         "<p><strong>The owner's living quarters are carved out.</strong> Owner-occupied housing in a hotel, "
         "motel or B&amp;B is allowed only if the pro rata value of the direct owner's living quarters, "
         "based on square footage, is deducted from the use of loan proceeds. For example, an owner buying a "
         f"{d(BB_PRICE)} B&amp;B of {BB_SQFT:,} square feet and living in {BB_OWNER:,} square feet of it "
         f"would fund {d(BB_OUT)} of the price some other way.</p>"),
        ("What Lenders Want on a Rural Hotel",
         "<ul>"
         "<li><strong>Equity.</strong> The rule's floor for an existing business is 10% by one of three "
         "tests. A new company formed to buy the hotel can be treated as a new business, with 20% balance "
         "sheet equity or 25% of project cost; with construction and an early guarantee, 25%. Lenders "
         "commonly ask more on hotels and stay near 80% of collateral value.</li>"
         "<li><strong>Operating history.</strong> Three years of financials, occupancy, average daily rate "
         "and STR reports where they exist. Small markets get extra scrutiny on demand.</li>"
         "<li><strong>Experience.</strong> The lender's credit review covers management. Prior hotel "
         "ownership or a proven general manager is usually expected.</li>"
         "<li><strong>A feasibility study</strong> for a new business borrowing more than $1 million, "
         f"prepared by an independent consultant USDA accepts ({_a(FEAS, '7 CFR 5001.306')}). USDA can "
         "ask for one on smaller loans too.</li>"
         "<li><strong>The brand's PIP.</strong> If a sale triggers a property improvement plan, lenders "
         "want the scope, contractor pricing and the brand's deadline.</li>"
         "</ul>"),
        ("Worked Example: A Flagged Hotel With a PIP",
         "<p><strong>Illustrative, not a quote or an offer.</strong> An operating company that already "
         f"owns two hotels buys a third in a town of about 14,000, at {d(H_PRICE)} with a "
         f"{d(H_PIP)} PIP and {d(H_SOFT)} of closing and soft costs. The lender asks for {H_EQ_PCT}% "
         "equity, above the rule's 10% floor for an existing business. Fees use the FY2026 B&amp;I rates.</p>"
         + table(["Item", "Amount"], [
             ["Total project cost", d(H_TOTAL)],
             [f"Buyer equity ({H_EQ_PCT}%)", d(H_EQ)],
             ["B&amp;I loan", d(H_LOAN)],
             ["USDA guarantee", f"{guar_pct(H_LOAN)}% (loan is $5 million or more)"],
             ["Guarantee fee (3.0%)", d(g_fee(H_LOAN))],
             ["Retention fee, year 1 (0.55%)", d(H_LOAN * guar_pct(H_LOAN) / 100 * RET_STD / 100)],
             ["Assumed rate and term", f"{H_RATE:.2f}%, {H_YRS} years"],
             ["Monthly principal and interest", d(H_PAY)],
             ["Cash flow needed at 1.25x", d(H_DS * 1.25) + " a year"],
         ])
         + f"<p>An SBA 7(a) alone stops at $5 million, so this deal would need a much bigger down payment "
         f"or a second loan through SBA. The {d(H_LOAN)} loan fits in one B&amp;I note. The coverage "
         "ratio is a common lender test, not a USDA number, and the cash flow should come from the hotel's "
         "history, not the room rate you expect after the PIP.</p>"),
        ("USDA or SBA for Your Hotel",
         "<p>The SBA side has its own hotel rules: more than half of revenue from stays of 30 days or less, "
         "a 504 minimum of 15% for this property type, and the 7(a) $5 million limit. "
         '<a href="/hotel-financing.html">Hotel financing</a> covers them, and '
         '<a href="/commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/">SBA vs '
         "CMBS vs conventional</a> compares larger structures.</p>"
         f"<p>For a rural hotel above $5 million, B&amp;I is often the only guaranteed route. Under that, "
         f"compare rate and equity in {_VS}. Fees are broken down in {_FEES}.</p>"
         + CTA),
    ],
    "faqs": [
        ("Can a USDA loan be used to buy a hotel?",
         "Yes, if it's in an eligible rural area. 7 CFR 5001.105(b)(8) lists hotels, motels, bed and breakfasts, "
         "resort trailer parks and campgrounds as eligible B&amp;I projects."),
        ("How much can a USDA B&amp;I hotel loan be?",
         "Up to $25 million per borrower, including existing B&amp;I balances. Lenders size the loan to the "
         "hotel's cash flow and collateral, so many deals end up smaller."),
        ("How much down payment does a USDA hotel loan need?",
         "The rule's floor is 10% for an existing business and 20-25% for a new one, by the tests in 7 CFR "
         "5001.105(d). Lenders commonly ask more on hotels."),
        ("Can USDA finance a hotel PIP?",
         "Renovation and expansion are eligible uses, so a PIP can be part of the project cost, which also "
         "raises the equity needed."),
        ("Can I live in the hotel I buy with a USDA loan?",
         "Yes, but the pro rata value of your living quarters, by square footage, has to be paid for outside "
         "the loan proceeds."),
        ("Does USDA finance new hotel construction?",
         "Construction is an eligible use. A new business borrowing over $1 million needs a feasibility study, "
         "and for a new business a 25% equity floor applies when the guarantee is issued before construction is done."),
    ],
    "related": [
        ("/usda-business-loans.html", "USDA business loans"),
        ("/hotel-financing.html", "Hotel financing"),
        ("/commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/", "SBA vs CMBS vs conventional hotel loans"),
        ("/usda-business-loans/articles/usda-eligible-areas/", "USDA eligible areas"),
        ("/usda-business-loans/articles/usda-b-and-i-vs-sba-7a/", "USDA B&I vs SBA 7(a)"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [PROJ, APPR, FEAS, LIMIT, TERM, NOTICE, RURAL],
}

# ---- spoke 4: rates, fees and terms ---------------------------------------------------------
FEE_SIZES = [1_000_000, 3_000_000, 4_900_000, 5_000_000, 10_000_000, 25_000_000]
R_LOAN, R_YRS = 3_000_000, 25
R_RATES = [7.5, 8.5, 9.5]
L_LOAN, L_RATE, L_YRS = 4_000_000, 8.0, 25

RATES = {
    "slug": "usda-b-and-i-loan-rates-fees",
    "crumb": "USDA B&I Rates and Fees",
    "title": "USDA B&I Loan Rates, Fees and Terms 2026 | Axiant",
    "og_title": "USDA B&I Loan Rates, Fees and Terms in 2026: Every Number, Computed",
    "h1": "USDA B&amp;I Loan Rates, Fees and Terms in 2026",
    "headline": "USDA B&I Loan Rates, Fees and Terms in 2026",
    "lede": "The guarantee fee, the annual retention fee, the guarantee percentage by loan size, how "
            "rates are set and how long the loan can run, with the math done for you",
    "meta_desc": "USDA B&I fees for 2026: 3.0% guarantee fee and 0.55% annual retention fee on the "
                 "guaranteed share, 85% or 80% guarantee, terms to 40 years, computed tables.",
    "article_desc": "The current USDA Business & Industry guaranteed loan fees, guarantee percentages, "
                    "rate rules and terms, with computed examples by loan size.",
    "keywords": "usda b&i loan rates, usda b&i guarantee fee, usda b&i annual renewal fee, usda business "
                "loan interest rate, usda b&i loan terms, usda guarantee percentage",
    "quick_answer": "Under the FY2026 USDA notice, B&amp;I loans carry a one-time <strong>3.0%</strong> "
                    "guarantee fee and a <strong>0.55%</strong> annual retention fee, both on the guaranteed "
                    "share; USDA guarantees <strong>85%</strong> of loans under $5 million and "
                    "<strong>80%</strong> from $5 million to $25 million. Rates are negotiated with the "
                    "lender, and terms run up to the assets' useful life, capped at 40 years. Axiant "
                    "Partners, a broker in Boca Raton, compares B&amp;I lenders. Rates here are illustrative.",
    "sections": [
        ("The Fee and Guarantee Table",
         f"<p>USDA sets these once a year in a Federal Register notice. The latest published is the "
         f"{_a(NOTICE, 'FY2026 OneRD notice')}, effective October 1, 2025. Check for a newer notice before "
         "you close; the rates in effect when your guarantee is obligated stay with the loan.</p>"
         + table(["B&amp;I loan type", "Guarantee fee", "Annual retention fee", "Guarantee"], [
             ["Under $5 million", f"{FEE_STD:.1f}%", f"{RET_STD:.2f}%", f"{G_UNDER5}%"],
             ["$5 million to $25 million", f"{FEE_STD:.1f}%", f"{RET_STD:.2f}%", f"{G_5TO25}%"],
             ["Reduced-fee projects", f"{FEE_RED:.1f}%", f"{RET_RED:.2f}%", "80%"],
             ["Guarantee before completion", "Add 0.50%", "-", "-"],
         ])
         + f"<p>Both fees are charged on the <strong>guaranteed share</strong>, not the whole loan "
         f"({_a(FEE, '7 CFR 5001.454')}, {_a(RET, '5001.455')}). The lender pays USDA and may pass the "
         "cost to you. The rule caps the B&amp;I guarantee fee at 5%, and the guarantee itself at 90%.</p>"),
        ("The Guarantee Fee by Loan Size",
         "<p>Computed from the FY2026 rates. Notice the step at $5 million, where the guarantee drops from "
         "85% to 80%:</p>"
         + table(["Loan", "Guarantee", "Guaranteed share", "Fee at 3.0%", "Fee at 1.0% (reduced)"], [
             [d(L), f"{guar_pct(L)}%", d(L * guar_pct(L) / 100), d(g_fee(L)),
              d(g_fee(L, FEE_RED, 80))] for L in FEE_SIZES
         ])
         + "<p>Who gets the reduced fee: the rule lists projects in distressed communities, places with "
         "long-term population decline, persistent poverty counties, recent disaster areas, places with "
         "unemployment at 125% or more of the national rate, and tribal lands, plus certain local food, "
         "value-added and regional plan projects. The lender has to request it, and annual limits apply.</p>"),
        ("What the Retention Fee Adds Up To",
         f"<p>The retention fee is charged every year on the guaranteed share of the outstanding balance, "
         "so it shrinks as you pay down. On an assumed "
         f"{d(L_LOAN)} loan at {L_RATE:.2f}% over {L_YRS} years ({guar_pct(L_LOAN)}% guaranteed):</p>"
         + table(["Item", "Amount"], [
             ["First year", d(L_LOAN * guar_pct(L_LOAN) / 100 * RET_STD / 100)],
             ["Over the full term", d_round(retention_total(L_LOAN, L_RATE, L_YRS))],
             ["Same loan, reduced 0.50% fee", d_round(retention_total(L_LOAN, L_RATE, L_YRS, RET_RED, 80))],
             ["One-time guarantee fee", d(g_fee(L_LOAN))],
         ])
         + "<p>Retention fees not paid within 60 days of the due date are delinquent and can lead to "
         "cancellation of the guarantee, so lenders usually build the fee into your payment schedule.</p>"),
        ("How Rates Are Set",
         f"<p>USDA doesn't publish B&amp;I rates. Under {_a(RATE, '7 CFR 5001.401')}, the rate is negotiated "
         "between you and the lender. It can be fixed, variable or a mix, and:</p>"
         "<ul>"
         "<li>it can't be more than the lender charges on similar loans without a guarantee;</li>"
         "<li>a variable rate must follow a published base rate, such as Prime, and can adjust no more "
         "often than quarterly;</li>"
         "<li>the guaranteed and unguaranteed parts can carry different rates.</li>"
         "</ul>"
         f"<p>With Prime at about {PRIME:.2f}%, here is what a {d(R_LOAN)} loan over {R_YRS} years costs "
         "at three illustrative rates:</p>"
         + table(["Rate", "Monthly P&amp;I", "Annual debt service"], [
             [f"{r:.2f}%", d(pmt(R_LOAN, r, R_YRS)), d(pmt(R_LOAN, r, R_YRS) * 12)] for r in R_RATES
         ])
         + "<p>These are examples, not a rate quote. Lenders price to the deal, the collateral and your "
         "credit, and many offer a fixed rate for a period before it adjusts.</p>"),
        ("Terms, Payments and Other Costs",
         f"<ul>"
         f"<li><strong>Term.</strong> Set by the lender with USDA concurrence, up to the useful life of the "
         f"assets financed or pledged, never more than 40 years ({_a(TERM, '7 CFR 5001.402')}). Lenders "
         "commonly match shorter terms to equipment and working capital.</li>"
         "<li><strong>No balloons.</strong> The loan must fully amortize. Payments are at least annual.</li>"
         "<li><strong>Interest-only start.</strong> Allowed, but the first full payment must begin within 3 "
         "years.</li>"
         "<li><strong>Lender fees.</strong> Reasonable and customary, the same as on the lender's other "
         "loans; prepayment penalties are allowed if written into the documents.</li>"
         "<li><strong>Broker fees.</strong> Loan proceeds can't pay loan finder or broker fees "
         f"({_a(USES, '7 CFR 5001.122')}).</li>"
         "<li><strong>Third-party costs.</strong> Appraisals for real estate or existing equipment over "
         "$250,000, and a feasibility study when required.</li>"
         "</ul>"
         f"<p>For how these terms compare with SBA, see {_VS}. For whether your project qualifies at all, "
         f"start with {_PILLAR}.</p>"
         + CTA),
    ],
    "faqs": [
        ("What is the USDA B&amp;I guarantee fee in 2026?",
         "3.0% of the guaranteed share under the FY2026 notice, or 1.0% for projects that qualify for the "
         f"reduced fee. On a $3 million loan guaranteed at 85%, that's {d(g_fee(3_000_000))}."),
        ("What is the USDA B&amp;I annual renewal fee?",
         "It's called the periodic guarantee retention fee: 0.55% a year on the guaranteed share of the "
         "outstanding balance under the FY2026 notice, or 0.50% for reduced-fee projects."),
        ("What percentage does USDA guarantee on a B&amp;I loan?",
         "85% on loans under $5 million and 80% from $5 million to $25 million under the FY2026 notice. The "
         "rule allows up to 90%."),
        ("What interest rate do USDA business loans have?",
         "There's no USDA rate. It's negotiated with the lender, can be fixed or variable, and can't exceed what "
         "the lender charges on similar unguaranteed loans."),
        ("How long can a USDA B&amp;I loan be?",
         "Up to the useful life of the assets financed or used as collateral, with a 40-year maximum and no balloon payment."),
        ("Can the fees be financed?",
         "The lender pays the fees to USDA and may pass them to the borrower. Whether they're rolled into the "
         "loan is part of the lender's structure."),
    ],
    "related": [
        ("/usda-business-loans.html", "USDA business loans"),
        ("/usda-business-loans/articles/usda-b-and-i-vs-sba-7a/", "USDA B&I vs SBA 7(a)"),
        ("/usda-business-loans/articles/usda-hotel-loans/", "USDA hotel loans"),
        ("/sba-loans/articles/typical-sba-loan-rates-2026/", "Typical SBA loan rates"),
        ("/business-loan-rates-2026/", "Business loan rates"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [NOTICE, FEE, RET, RATE, TERM, USES, APPR],
}

ARTICLES = [ELIG, VS, HOTEL, RATES]
