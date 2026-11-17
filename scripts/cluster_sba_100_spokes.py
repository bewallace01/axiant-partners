# -*- coding: utf-8 -*-
"""SBA plan Cluster 1 spokes, under /sba-100-percent-financing/articles/.

Six spokes for the 100% owner-occupied pillar (/sba-100-percent-financing.html): the auto repair
shop building, a daycare building, a contractor's yard or land, the 51% occupancy rule, tenant
improvements in a purchase, and assisted living. Plan spokes 7 (owner-occupied vs investment) and
8 (7(a) vs 504 vs conventional) are NOT built: the first is the cited
/commercial-real-estate-loans/articles/owner-occupied-vs-investment-commercial-property-loan/ and
the second is already the pillar's comparison table plus /sba-loans/articles/sba-7a-vs-504-loan/,
so either would cannibalize.

SBA rules read from the SOP 50 10 8.1 .docx (effective 2026-10-01) downloaded from
legacy.sba.gov on 2026-11-13: occupancy and Rentable Property (Sec. A Ch. 3 Para. C), excess land
and passive investment (13 CFR 120.130 restrictions), residential care eligibility, environmental
steps and Appendix 6 NAICS list (8111 automotive repair), child-occupied facility lead testing,
leasehold improvement rules, construction bonding over $350,000, Appendix 17 maturities, Appendix
15 change-of-ownership equity and DSC, Appendix 19 appraisal rules, and the 504 Limited or Special
Purpose Property list and contribution. FY2027 7(a) upfront fees from the NAGGL summary (same
method as the pillar, fee financed). Child care space: 8VAC20-780-310 and Minn. R. 9503.0155,
read 2026-11-13. Every payment and fee below is computed (7.75% / 25 years, the pillar's
illustrative assumption). Never names the program lender; no fixed credit-score or rate floors.
"""
from cluster_table import table
from sba_sources import SOP, FEES, OCC, SBA_7A, SBA_504

PILLAR = "/sba-100-percent-financing.html"
HUB = "/sba-100-percent-financing/articles"

VA_CC = ("https://law.lis.virginia.gov/admincode/title8/agency20/chapter780/section310/",
         "8VAC20-780-310: Areas (Virginia child day centers)",
         "35 square feet of indoor space per child and 75 square feet per child outdoors.")
MN_CC = ("https://www.revisor.mn.gov/rules/9503.0155/",
         "Minnesota Rules 9503.0155: Facility requirements",
         "35 square feet of indoor space per child, 75 square feet outdoors, 1,500 square feet minimum play area.")
AAI = ("https://www.ecfr.gov/current/title-40/chapter-I/subchapter-J/part-312",
       "40 CFR Part 312: All Appropriate Inquiries",
       "The federal standard a Phase I environmental site assessment follows.")

_SOP_A = ('<a href="' + SOP[0] + '" rel="noopener nofollow" target="_blank">SOP 50 10 8.1</a>')
_OCC_A = ('<a href="' + OCC[0] + '" rel="noopener nofollow" target="_blank">13 CFR 120.131</a>')
_P = f'<a href="{PILLAR}">100% SBA financing</a>'
_CTA = ('<p>Talk to an SBA specialist: <a href="tel:+15612680465">(561) 268-0465</a>, or '
        '<a href="/match.html">get matched with lenders</a> who offer this structure.</p>')
_ILL = ("<strong>Illustrative numbers, not a quote or an offer; rates and fees change, and every "
        "loan is subject to approval.</strong> ")

CLUSTER = {
    "pillar": "sba-100-percent-financing.html",
    "hub": "sba-100-percent-financing/articles",
    "crumb": "100% SBA Financing",
    "cta_inline": "Talk to an SBA specialist",
    "cta_button": "Talk to an SBA Specialist",
    "hub_title": "100% SBA Building Financing Guides | Axiant",
    "hub_h1": "100% SBA Financing Articles",
    "hub_lede": "Buying the building your business operates from, by property type and by rule",
    "hub_desc": "Guides to buying your business's building with an SBA 7(a) loan and little or no "
                "money down: auto repair shops, daycares, contractor yards, assisted living, the "
                "51% occupancy rule and tenant improvements.",
    "hub_quick_answer": "As of November 2026, some SBA 7(a) lenders finance up to 100% of a "
                        "building an established business will occupy, on terms up to 25 years. "
                        "Your business must use at least 51% of an existing building. Property "
                        "type changes the file: environmental work for shops, licensing space "
                        "for daycares, used land for yards. Axiant Partners, a broker in Boca "
                        "Raton, matches owners with these lenders.",
    "hub_intro": "The SBA sets the rules, but each lender decides whether to go to 100%. These "
                 "guides cover what changes by property type and the rules every buyer runs "
                 f"into. Start with {_P}, or compare "
                 '<a href="/sba-loans/articles/sba-7a-vs-504-loan/">SBA 7(a) and 504</a>.',
    "hub_cta_h2": "Ready to stop paying rent?",
    "hub_cta_p": "Tell us the building, the price and how much of it you'll use. Talk to an SBA "
                 "specialist at (561) 268-0465.",
}

ARTICLES = [
# ---------------------------------------------------------------- 1. auto repair building
{
    "slug": "buy-auto-repair-shop-building",
    "crumb": "Buying Your Auto Repair Shop Building",
    "title": "SBA Loan to Buy Your Auto Repair Shop Building | Axiant",
    "og_title": "Buying the Building Your Auto Repair Shop Rents: SBA Financing",
    "h1": "Buying the Building Your Auto Repair Shop Rents",
    "headline": "Buying the Building Your Auto Repair Shop Rents: SBA Financing",
    "lede": "Why the environmental report decides these deals, how lifts and bays affect the "
            "appraisal, and what a zero-down purchase looks like for a shop that already operates there",
    "meta_desc": "Buy your auto repair shop's building with an SBA 7(a) loan: the required Phase I, in-ground lifts, zoning, and a $1.15M worked example with no money down.",
    "article_desc": "How an established auto repair shop buys the building it rents with SBA "
                    "financing, including the Phase I requirement and a worked example.",
    "keywords": "sba loan to buy auto repair shop building, buy building for auto repair shop, "
                "auto repair shop real estate loan, phase i environmental auto repair",
    "quick_answer": "As of November 2026, an established auto repair shop can often buy the "
                    "building it rents with an SBA 7(a) loan of up to <strong>25 years</strong>, "
                    "and some lenders finance up to <strong>100%</strong>. Because auto repair is "
                    "on the SBA's environmentally sensitive list, the lender must start with a "
                    "<strong>Phase I environmental site assessment</strong>, whatever the loan "
                    "size. Axiant Partners, a broker in Boca Raton, finds lenders for these deals. "
                    "Terms are typical ranges, not a quote.",
    "sections": [
        ("Why a Shop That Already Rents Has an Edge",
         f"<p>This guide is for an operating shop buying its own building, the case {_P} covers. "
         "If you are buying the business too, that is a change of ownership with a 10% minimum "
         "equity injection; see <a href=\"/articles/how-to-finance-buy-an-auto-repair-shop/\">"
         "how to finance buying an auto repair shop</a>.</p>"
         "<p>A tenant shop has three things a lender likes. Its rent history shows it can carry an "
         "occupancy cost. It already uses the space, so the occupancy test is easy. And the "
         "lender can compare the new mortgage payment with rent the shop is already paying. "
         "The question becomes whether your cash flow covers the payment plus the taxes, "
         "insurance and repairs a landlord used to absorb.</p>"),
        ("The Environmental Report Comes First",
         f"<p>Under {_SOP_A}, the lender checks the property's current and past uses against the "
         "SBA's list of environmentally sensitive industries. Automotive repair and maintenance "
         "(NAICS 8111) is on it, so the investigation must begin with a <strong>Phase I</strong> "
         "regardless of loan amount. A Phase I is always required if the property sells or "
         "dispenses fuel, even when the use isn't on the list.</p>"
         "<ul>"
         "<li><strong>Who does it.</strong> An environmental professional, following the federal "
         "All Appropriate Inquiries standard. The report must be dated within one year of the "
         "SBA loan number.</li>"
         "<li><strong>What it looks for.</strong> Waste oil, solvents, old floor drains, "
         "oil-water separators, and tanks above or below ground. A long history of repair work "
         "on the site matters even if your shop is clean.</li>"
         "<li><strong>If it finds something.</strong> The lender follows the professional's "
         "recommendation, usually a Phase II with soil or groundwater testing. Contamination "
         "doesn't end every deal, but it adds reporting to the SBA, time and cost.</li>"
         "</ul>"
         "<p>Order the Phase I early. It is the item most likely to push a closing date, and "
         "you want to know before your purchase contract's inspection period ends.</p>"),
        ("Lifts, Bays and the Appraisal",
         "<p>An appraisal by a state-licensed or certified appraiser is required, and over "
         "$1 million in value the appraiser must be state-certified. The SOP's list of limited "
         "or special purpose properties includes service centers with pits and in-ground "
         "lifts. A building like that has fewer buyers, which some lenders weigh when deciding "
         "how far to go. A shop with surface-mounted lifts and standard bay doors usually "
         "appraises as a flex or light-industrial building with a wider market.</p>"
         "<p>Lifts bolted to the floor are usually part of the real estate. New lifts, alignment "
         "racks and scan tools are better financed separately: see "
         '<a href="/auto-repair-business-financing/financing-auto-lifts-shop-equipment/">'
         "financing auto lifts and shop equipment</a>.</p>"),
        ("Worked Example: A $1,150,000 Shop Building",
         f"<p>{_ILL}A shop that has rented its six-bay building for eight years buys it from the "
         "landlord. Fees are computed from the FY2027 7(a) fee schedule, with the guaranty fee "
         "financed.</p>"
         + table(["Item", "Amount"], [
             ["Purchase price", "$1,150,000"],
             ["Phase I, appraisal, title", "$16,500"],
             ["7(a) packaging fee (estimate)", "$2,500"],
             ["SBA guaranty fee (computed)", "About $31,513"],
             ["<strong>SBA 7(a) loan, $0 down</strong>", "<strong>About $1,200,513</strong>"],
             ["Assumed rate and term", "7.75%, 25 years"],
             ["Monthly principal and interest", "About $9,068"],
         ])
         + "<p>If rent is $8,500 a month, the payment is about $568 more before property taxes "
         "and insurance. In return the shop builds equity and can't be priced out at renewal. "
         "The lender wants last year's and this year's cash flow to cover the full payment, not "
         "projections.</p>"),
        ("Zoning and the Rest of the Lot",
         "<ul>"
         "<li><strong>Zoning.</strong> Many towns only allow vehicle repair in certain districts "
         "or under a special permit. Confirm the use is allowed, or legally nonconforming, and "
         "that the permit transfers. A lender won't finance a use the zoning won't support.</li>"
         "<li><strong>Parking and storage.</strong> Paved parking for customer cars is part of "
         "the business. Extra acreage the shop doesn't use is excess land the SBA won't fund.</li>"
         "<li><strong>Extra units.</strong> In a building you don't fully use, your shop must "
         "occupy at least 51% of the rentable space. Our "
         '<a href="' + HUB + '/sba-51-percent-occupancy-rule/">51% occupancy rule guide</a> '
         "shows how that's measured.</li>"
         "</ul>"
         + _CTA),
    ],
    "faqs": [
        ("Does every auto repair building need a Phase I for an SBA loan?",
         "Yes. Automotive repair is on the SBA's list of environmentally sensitive industries, so "
         "the environmental investigation must begin with a Phase I regardless of loan size."),
        ("Can I buy my shop's building with no money down?",
         "Some SBA 7(a) lenders finance up to 100% for an established shop that occupies the "
         "building and has the cash flow to cover the payment. Many still ask for 10% or more."),
        ("What happens if the Phase I finds contamination?",
         "The lender usually orders a Phase II test. If contamination is confirmed, the loan can "
         "still be made in some cases, but the lender must report it to the SBA and it adds time."),
        ("Are in-ground lifts a problem?",
         "Service centers with pits and in-ground lifts are on the SBA's list of special purpose "
         "properties. That doesn't make them ineligible, but some lenders are more cautious."),
        ("Should the shop equipment go in the same loan?",
         "Fixtures that are part of the building go with it. New equipment is usually financed "
         "separately over a shorter term that matches its useful life."),
    ],
    "related": [
        (PILLAR, "100% SBA financing"),
        (HUB + "/sba-51-percent-occupancy-rule/", "The SBA 51% occupancy rule"),
        (HUB + "/tenant-improvements-sba-building-purchase/", "Tenant improvements in a purchase"),
        ("/auto-repair-business-financing.html", "Auto repair financing"),
        ("/articles/how-to-finance-buy-an-auto-repair-shop/", "Buying an auto repair business"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, AAI, FEES, OCC, SBA_7A],
},
# ---------------------------------------------------------------- 2. daycare building
{
    "slug": "sba-loan-daycare-building",
    "crumb": "SBA Loan for a Daycare Building",
    "title": "SBA Loans for Daycare Buildings: Space Rules | Axiant",
    "og_title": "SBA Loan for a Daycare Building: Licensing Space, Lead Testing and 100% Financing",
    "h1": "Buying a Daycare Building With an SBA Loan",
    "headline": "Buying a Daycare Building With an SBA Loan: Licensing Space, Lead Testing and Zoning",
    "lede": "How licensed capacity drives the value of a child care building, what the SBA "
            "requires for older buildings, and a worked purchase with renovation",
    "meta_desc": "Buy a daycare building with an SBA loan: how 35 and 75 square feet per child set capacity, lead testing for pre-1978 buildings, zoning, and a worked example.",
    "article_desc": "How a child care operator buys its building with SBA financing, with "
                    "licensing space rules, lead testing and a computed example.",
    "keywords": "sba loan for daycare building, buy daycare building, child care center real "
                "estate loan, daycare building financing, 100% financing daycare",
    "quick_answer": "As of November 2026, an established child care operator can buy its "
                    "building with an SBA 7(a) loan over up to <strong>25 years</strong>, and "
                    "some lenders go to <strong>100%</strong> with renovation included. Licensed "
                    "capacity drives the numbers: many states require about <strong>35 sq ft"
                    "</strong> indoors and <strong>75 sq ft</strong> outdoors per child. Buildings "
                    "from before 1978 need lead testing. Axiant Partners, a broker in Boca Raton, "
                    "finds these lenders. Terms are typical, not a quote.",
    "sections": [
        ("Capacity Is What the Lender Underwrites",
         f"<p>A daycare building is worth what it can be licensed for. This guide is about the "
         "building. For running or buying the center itself, see the "
         '<a href="/childcare-financing-guide/">childcare financing guide</a>; for the zero-down '
         f"structure in general, see {_P}.</p>"
         "<p>State rules set capacity. Virginia and Minnesota, for example, both require "
         "<strong>35 square feet</strong> of usable indoor space per child and <strong>75 square "
         "feet</strong> per child using the outdoor play area at one time. Minnesota excludes "
         "hallways, bathrooms, kitchens and closets, and requires a play area of at least 1,500 "
         "square feet. Your state's numbers may differ, so check them before you sign.</p>"
         + table(["Usable classroom space", "Children at 35 sq ft", "Outdoor area for all at once", "Payment per child per month*"], [
             ["3,500 sq ft", "100", "7,500 sq ft", "About $151"],
             ["5,000 sq ft", "142", "10,650 sq ft", "About $106"],
             ["7,000 sq ft", "200", "15,000 sq ft", "About $75"],
         ])
         + "<p>*Using the worked example's $15,062 monthly payment below. Many centers rotate "
         "groups outside, which lowers the outdoor area needed. The lender will compare the "
         "licensed capacity and your enrollment history with the payment.</p>"),
        ("Lead Testing for Older Buildings",
         f"<p>{_SOP_A} treats a daycare as a child-occupied facility. If the building was "
         "built before 1978, the lender must get a <strong>lead risk assessment</strong> and test "
         "drinking water at every tap and fountain children might use. Both must be done within "
         "one year of the SBA loan number, and the lender can't disburse until the lead risk is "
         "minimized.</p>"
         "<p>Budget for this and any fixes. Replacing fixtures or abating paint can go into the "
         "renovation line of the loan, and doing it before closing protects your license "
         "inspection too.</p>"),
        ("Zoning, Permits and the Play Yard",
         "<ul>"
         "<li><strong>Zoning.</strong> Many towns allow child care only in some districts or by "
         "special use permit. A building that houses a licensed center today is the safest buy; "
         "converting an office or church building needs zoning and licensing checked first.</li>"
         "<li><strong>Outdoor space.</strong> The fenced play yard is used land, so it is "
         "financeable. Unused acreage is excess land, which SBA proceeds can't fund.</li>"
         "<li><strong>Deed restrictions.</strong> Some properties carry environmental deed "
         "restrictions against use as a day care center. The title search must clear this.</li>"
         "<li><strong>Extra space.</strong> If you lease part of the building out, your center "
         'must occupy at least 51%. See <a href="' + HUB + '/sba-51-percent-occupancy-rule/">'
         "how the 51% occupancy rule is measured</a>.</li>"
         "</ul>"),
        ("Worked Example: Buying and Updating a $1.8M Center",
         f"<p>{_ILL}An operator who has leased for six years buys the building and spends "
         "$120,000 on a new play yard, fencing and classroom updates. Fees are computed from the "
         "FY2027 7(a) schedule, with the guaranty fee financed.</p>"
         + table(["Item", "Amount"], [
             ["Purchase price", "$1,800,000"],
             ["Renovation (yard, classrooms)", "$120,000"],
             ["Reports, lead tests, title", "$18,000"],
             ["7(a) packaging fee (estimate)", "$2,500"],
             ["SBA guaranty fee (computed)", "About $53,584"],
             ["<strong>SBA 7(a) loan, $0 down</strong>", "<strong>About $1,994,084</strong>"],
             ["Assumed rate and term", "7.75%, 25 years"],
             ["Monthly principal and interest", "About $15,062"],
         ])
         + "<p>With work this size, the renovation is part of the real estate loan. When "
         "renovation goes over a third of the purchase price, the appraisal must value the "
         "building as completed. For larger build-outs, see "
         '<a href="' + HUB + '/tenant-improvements-sba-building-purchase/">adding improvements '
         "to an SBA purchase</a>.</p>"),
        ("What Lenders Want From a Child Care Operator",
         "<ul>"
         "<li><strong>Two or more years operating,</strong> with tax returns and current-year "
         "statements showing the payment is covered.</li>"
         "<li><strong>Your license and inspection history,</strong> plus enrollment and waitlist "
         "numbers.</li>"
         "<li><strong>Subsidy mix.</strong> Lenders look at how much tuition comes from state "
         "subsidy programs and how reliably they pay.</li>"
         "<li><strong>Credit.</strong> Many SBA lenders look for roughly 650-680 or higher; some "
         "go lower with strong cash flow.</li>"
         "</ul>"
         + _CTA),
    ],
    "faqs": [
        ("Can I get an SBA loan to buy a daycare building with no money down?",
         "Some SBA 7(a) lenders finance up to 100% for an established operator that occupies the "
         "building and can show the cash flow to support the payment. Start-ups need at least 10%."),
        ("How many children can a building be licensed for?",
         "It's set by your state. Many states require about 35 square feet of usable indoor space "
         "per child and 75 square feet per child outdoors, excluding hallways, bathrooms and kitchens."),
        ("Does the SBA require lead testing for a daycare?",
         "Yes, for buildings built before 1978: a lead risk assessment and drinking water tests at "
         "all taps children could use, both within a year of the loan number."),
        ("Can renovation be included in the loan?",
         "Yes. Improvements to the space your center uses can be financed with the building. "
         "Space leased to someone else can't be improved with SBA proceeds."),
        ("Is SBA 504 better for a daycare building?",
         "A 504 offers a fixed rate on part of the loan but needs at least 10% down. A 7(a) can "
         "reach 100% with some lenders, usually on an adjustable rate."),
    ],
    "related": [
        (PILLAR, "100% SBA financing"),
        ("/childcare-financing-guide/", "Childcare financing guide"),
        (HUB + "/tenant-improvements-sba-building-purchase/", "Tenant improvements in a purchase"),
        (HUB + "/sba-51-percent-occupancy-rule/", "The SBA 51% occupancy rule"),
        ("/sba-loans/articles/sba-7a-vs-504-loan/", "SBA 7(a) vs 504"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, VA_CC, MN_CC, FEES, SBA_7A],
},
# ---------------------------------------------------------------- 3. contractor yard / land
{
    "slug": "sba-loan-contractor-yard-land",
    "crumb": "SBA Loan for a Contractor Yard",
    "title": "SBA Loan for a Contractor Yard or Business Land | Axiant",
    "og_title": "Financing a Contractor's Yard or Land Your Business Uses With an SBA Loan",
    "h1": "Financing a Contractor's Yard or Land Your Business Uses",
    "headline": "Financing a Contractor's Yard or Land Your Business Uses With an SBA Loan",
    "lede": "When land qualifies for SBA financing, why a storage yard counts toward occupancy, "
            "and what happens to the acres you don't use",
    "meta_desc": "SBA loans for a contractor yard or business land: what counts as used land, the excess land rule, yard space in the occupancy test, and a worked example.",
    "article_desc": "How contractors and trucking or landscaping companies finance a yard and "
                    "shop with an SBA 7(a) loan, and why excess land is excluded.",
    "keywords": "sba loan for land, contractor yard financing, sba loan to buy land for business, "
                "equipment yard loan, buy land for construction company",
    "quick_answer": "As of November 2026, an SBA 7(a) loan can finance land your business "
                    "actively uses, such as a contractor's storage yard with a shop, over up to "
                    "<strong>25 years</strong>, and some lenders go to <strong>100%</strong> for "
                    "established companies. Land bought for the future, to resell or to lease out "
                    "is <strong>excess land</strong> and can't be financed with SBA proceeds. "
                    "Axiant Partners, a broker in Boca Raton, finds lenders for yard purchases. "
                    "Terms are typical, not a quote.",
    "sections": [
        ("Used Land Versus Excess Land",
         f"<p>{_SOP_A} bars SBA proceeds from property held for future development, sale, lease "
         "or investment, and from <strong>excess land</strong>: land not in immediate use as part "
         "of the project. So the test isn't whether it's land, it's whether your business uses it "
         f"now. This is the land side of {_P}.</p>"
         + table(["Usually financeable", "Usually not"], [
             ["Fenced storage yard", "Acreage held for a future building"],
             ["Shop, office and wash bay", "Lots you plan to sell or lease"],
             ["Daily truck parking, staging", "Raw land with no business use yet"],
             ["Land under a new building", "Speculative homes or spec buildings"],
         ])
         + "<p>Farming has its own rule: farm land beyond the operation's needs is excess, and "
         "the SOP specifically bars buying vacant or row-crop land for future use or to lease.</p>"),
        ("Why the Yard Counts Toward Occupancy",
         "<p>Your business must occupy at least 51% of an existing property's rentable space. The "
         "SOP lets exterior space count when it is actively used in the business, and names "
         "<strong>outdoor storage yards for general contractors, trucking companies and moving "
         "and storage companies</strong> as examples. Parking areas don't count.</p>"
         "<p>Example: a 4,000 sq ft shop and a 30,000 sq ft storage yard you use, plus a 6,000 "
         "sq ft building you lease to a tenant. You occupy 34,000 of 40,000 square feet, or 85%. "
         "Counting buildings alone, you'd be at 40% and fail. See the "
         '<a href="' + HUB + '/sba-51-percent-occupancy-rule/">51% occupancy rule</a> for the '
         "full measuring rules.</p>"),
        ("Worked Example: A Two-Acre Yard With a Shop",
         f"<p>{_ILL}A paving contractor with nine years of history buys a $900,000 property: a "
         "shop, a fenced yard and a back acre it has no use for. The appraiser values that acre "
         "at $120,000, so the SBA loan covers the rest and the buyer pays for the acre another "
         "way. Fees are from the FY2027 7(a) schedule, financed.</p>"
         + table(["Item", "Amount"], [
             ["Purchase price", "$900,000"],
             ["Excess acre, not SBA-funded", "-$120,000"],
             ["Reports, survey, title (est.)", "$14,500"],
             ["7(a) packaging fee (estimate)", "$2,500"],
             ["SBA guaranty fee (computed)", "About $21,485"],
             ["<strong>SBA 7(a) loan</strong>", "<strong>About $818,485</strong>"],
             ["Assumed rate and term", "7.75%, 25 years"],
             ["Monthly principal and interest", "About $6,182"],
         ])
         + "<p>The extra acre can be bought with cash or a separate non-SBA loan, or left out of "
         "the deal. Lenders differ on how they treat a small unused strip, so raise it early.</p>"),
        ("Environmental Checks on a Yard",
         "<p>Heavy and civil engineering construction (NAICS 237) is on the SBA's environmentally "
         "sensitive list, so those buyers start with a Phase I. So do trucking companies with "
         "service bays, truck washing or fuel tanks. Any site where fuel is dispensed needs a "
         "Phase I. A yard with past fueling, equipment repair or buried tanks gets close review "
         "whatever your trade. Other buyers over $250,000 start with a questionnaire and records "
         "search, which can lead to a Phase I.</p>"),
        ("Building on the Land",
         "<p>If you'll build a shop, SBA rules add a period for construction to the 25-year term. "
         "Above $350,000 of construction, the lender generally needs a licensed contractor with "
         "full performance and payment bonds, unless a construction manager controls the funds. "
         "When building new, you must occupy 60% of the rentable space.</p>"
         "<p>Need the equipment as well? See <a href=\"/contractor-financing.html\">contractor "
         "financing</a> or <a href=\"/landscaping-business-financing.html\">landscaping business "
         "financing</a>.</p>"
         + _CTA),
    ],
    "faqs": [
        ("Can I use an SBA loan to buy land for my business?",
         "Yes, if your business will use the land now, for example as a storage yard or for a "
         "building you'll construct. Land held for future use, resale or lease is not eligible."),
        ("What is excess land in an SBA loan?",
         "Land that isn't in immediate use as part of the project. SBA proceeds can't pay for it, "
         "so it's carved out of the loan and paid another way, or left out of the purchase."),
        ("Does an outdoor storage yard count toward the 51% occupancy rule?",
         "Yes, if it's actively used. The SOP names storage yards for contractors, trucking and "
         "moving companies. Parking areas don't count."),
        ("Can I buy farm land with an SBA loan?",
         "Only land the farming operation needs. Excess farm land, and vacant or row-crop land "
         "for future use or to lease, can't be financed."),
        ("Can I get 100% financing on a yard?",
         "Some 7(a) lenders go to 100% for established companies with the cash flow to cover the "
         "payment. Many ask for 10% or more, especially on land-heavy deals."),
    ],
    "related": [
        (PILLAR, "100% SBA financing"),
        (HUB + "/sba-51-percent-occupancy-rule/", "The SBA 51% occupancy rule"),
        (HUB + "/buy-auto-repair-shop-building/", "Buying an auto repair building"),
        ("/contractor-financing.html", "Contractor financing"),
        ("/real-estate-secured-business-loan.html", "Real estate secured business loans"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, OCC, FEES, SBA_7A],
},
# ---------------------------------------------------------------- 4. 51% occupancy rule
{
    "slug": "sba-51-percent-occupancy-rule",
    "crumb": "The SBA 51% Occupancy Rule",
    "title": "SBA 51% Occupancy Rule: How It's Measured | Axiant",
    "og_title": "The SBA 51% Occupancy Rule: How Owner Occupancy Is Measured",
    "h1": "The SBA 51% Occupancy Rule, Explained",
    "headline": "The SBA 51% Occupancy Rule: How Owner Occupancy Is Measured",
    "lede": "What counts as rentable property, how the 60% new construction rule works, and "
            "how a holding company owns the building and still qualifies",
    "meta_desc": "The SBA 51% occupancy rule: how rentable property is measured, the 60% rule for new construction, holding company (EPC/OC) structures, and worked calculations.",
    "article_desc": "How the SBA's 51% and 60% owner-occupancy rules are measured, with "
                    "rentable property definitions, EPC/OC structures and examples.",
    "keywords": "sba 51 percent occupancy rule, sba owner occupied requirement, sba 60 percent "
                "occupancy new construction, eligible passive company, epc oc sba",
    "quick_answer": "As of November 2026, an SBA loan for an existing building requires your "
                    "business to occupy at least <strong>51%</strong> of the rentable property, "
                    "and you can lease out up to 49%. For new construction it's <strong>60%"
                    "</strong>, with 20% leased permanently and 20% temporarily. A holding company "
                    "can own the building if it leases 100% to your operating company. Axiant "
                    "Partners, a broker in Boca Raton, can review your layout with lenders.",
    "sections": [
        ("The Rule in One Table",
         f"<p>{_OCC_A} and {_SOP_A} set the occupancy test whenever SBA money buys, improves or "
         "refinances real estate. It is what separates an owner-occupied loan from an investment "
         f"property, and it applies to the 100% structure in {_P}.</p>"
         + table(["", "Existing building", "New construction"], [
             ["Your business must occupy", "At least 51%", "At least 60%"],
             ["Permanent lease to others", "Up to 49%", "Up to 20%"],
             ["Temporary lease to others", "Not needed", "Up to 20% more"],
             ["Temporary space deadline", "None", "Use some within 3 years, all within 10"],
         ])
         + "<p>The lender can give up to one year after closing to reach occupancy, for example "
         "while a tenant's existing lease runs out. Never more.</p>"),
        ("What Counts as Rentable Property",
         "<p>The SOP defines rentable property as the total square footage of buildings used for "
         "business operations, <strong>excluding</strong> stairways, elevators and mechanical "
         "areas and <strong>including</strong> common areas. Exterior space can count if it's "
         "actively used, like a contractor's storage yard or a marina's slips, but parking "
         "doesn't. The lender may give your business the square footage of common areas.</p>"
         "<p>That choice can decide a close deal. Take a 12,000 sq ft building with 600 sq ft of "
         "stairs, elevator and mechanical rooms, leaving 11,400 rentable. You use 5,400 sq ft and "
         "a tenant uses 5,400 sq ft, and there is a 600 sq ft shared lobby.</p>"
         + table(["How it's counted", "Your share", "Result"], [
             ["Lobby credited to you", "6,000 / 11,400 = 52.6%", "Passes"],
             ["Lobby not credited to you", "5,400 / 11,400 = 47.4%", "Fails"],
         ])
         + "<p>Measured floor plans beat estimates. Bring them to the first lender call.</p>"),
        ("Holding Company Ownership (EPC/OC)",
         "<p>Many owners hold the building in a separate LLC. The SBA allows this as an "
         "<strong>Eligible Passive Company (EPC)</strong> that leases to your <strong>Operating "
         "Company (OC)</strong>, under strict conditions:</p>"
         "<ul>"
         "<li>The EPC must lease <strong>100%</strong> of the property to the operating company, "
         "which then occupies at least 51% (or 60% new) and can sublease the rest.</li>"
         "<li>The EPC can't do any other business, and rent can't exceed the loan payment plus "
         "the EPC's direct costs of holding the property.</li>"
         "<li>The EPC assigns its rents to the lender as collateral.</li>"
         "<li>Every owner of 20% or more of either company guarantees the loan.</li>"
         "<li>Only one EPC per transaction, though several properties can be in it if they're "
         "all leased to the same operating companies.</li>"
         "</ul>"),
        ("Spaces That Trip Buyers Up",
         "<ul>"
         "<li><strong>Residential units.</strong> In a mixed-use building, residential space "
         "can be rented out within the 49%. An owner's apartment only counts as the business's if "
         "the business needs someone on site, like livestock care, and it can't exceed 49% of the "
         "property.</li>"
         "<li><strong>Tenant space improvements.</strong> SBA proceeds can't improve space you "
         "lease to others. See <a href=\"" + HUB + "/tenant-improvements-sba-building-purchase/\">"
         "tenant improvements in an SBA purchase</a>.</li>"
         "<li><strong>Illegal tenants.</strong> Leasing to a business that is illegal under any "
         "law, including federal law, such as a marijuana dispensary, is not allowed for the life "
         "of the loan.</li>"
         "<li><strong>Yards.</strong> See <a href=\"" + HUB + "/sba-loan-contractor-yard-land/\">"
         "financing a contractor's yard</a> for how outdoor space counts.</li>"
         "</ul>"),
        ("If You Can't Reach 51%",
         "<p>A building where your business would use less than half is an investment property "
         "to the SBA. The options are a conventional or "
         '<a href="/real-estate-secured-business-loan.html">real estate secured loan</a>, a '
         "smaller building, or a plan to take back tenant space within a year of closing. For "
         "how lenders price owner-occupied against investment property, see "
         '<a href="/commercial-real-estate-loans/articles/owner-occupied-vs-investment-commercial-property-loan/">'
         "owner-occupied vs investment loans</a>.</p>"
         + _CTA),
    ],
    "faqs": [
        ("What is the SBA 51% occupancy rule?",
         "For an existing building bought, improved or refinanced with an SBA loan, your business "
         "must occupy at least 51% of the rentable property. You may lease the rest to others."),
        ("What is the occupancy requirement for new construction?",
         "60%. You can lease up to 20% permanently and another 20% temporarily, if you plan to use "
         "some of that space within 3 years and all of it within 10."),
        ("Do common areas count toward my 51%?",
         "The lender may include common areas in your share. Stairways, elevators and mechanical "
         "areas are excluded from the total, and parking doesn't count."),
        ("Can my real estate LLC own the building?",
         "Yes, as an Eligible Passive Company, if it leases 100% to your operating company, does "
         "no other business and charges rent no higher than the loan payment plus holding costs."),
        ("How long do I have to meet occupancy?",
         "The lender can allow time after closing, for example while an existing tenant's lease "
         "ends, but never more than one year."),
        ("Does the rule apply to SBA 504 loans too?",
         "Yes. Both 7(a) and 504 use the same 51% and 60% rules."),
    ],
    "related": [
        (PILLAR, "100% SBA financing"),
        (HUB + "/sba-loan-contractor-yard-land/", "Contractor yard and land"),
        (HUB + "/tenant-improvements-sba-building-purchase/", "Tenant improvements in a purchase"),
        ("/sba-loans/articles/sba-loan-owner-occupied-commercial-property/", "SBA 7(a) vs 504 for your building"),
        ("/commercial-real-estate-loans/articles/owner-occupied-vs-investment-commercial-property-loan/", "Owner-occupied vs investment"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [OCC, SOP, SBA_7A, SBA_504],
},
# ---------------------------------------------------------------- 5. tenant improvements
{
    "slug": "tenant-improvements-sba-building-purchase",
    "crumb": "Improvements in an SBA Purchase",
    "title": "Adding Improvements to an SBA Building Purchase | Axiant",
    "og_title": "Adding Tenant Improvements and Renovation to an SBA Building Purchase",
    "h1": "Adding Improvements to an SBA Building Purchase",
    "headline": "Adding Tenant Improvements and Renovation to an SBA Building Purchase",
    "lede": "What renovation can ride on the purchase loan, what can't, when bonds and an "
            "as-completed appraisal kick in, and how the term changes",
    "meta_desc": "Add renovation or tenant improvements to an SBA building purchase: what's eligible, the one-third and $350,000 thresholds, terms, and a $2.25M worked example.",
    "article_desc": "How buyers fold renovation and build-out costs into an SBA 7(a) building "
                    "purchase, with SOP thresholds and a computed example.",
    "keywords": "sba loan tenant improvements, sba loan purchase and renovation, build out "
                "financing sba, leasehold improvements sba loan, sba renovation loan",
    "quick_answer": "As of November 2026, renovation of the space your business will use can "
                    "be added to an SBA 7(a) building purchase and repaid over the same "
                    "<strong>25-year</strong> real estate term, plus time to build. Space you "
                    "lease to others can't be improved with SBA money. Work over <strong>"
                    "$350,000</strong> usually needs bonded contractors, and renovation over a "
                    "third of the price needs an as-completed appraisal. Axiant Partners, a "
                    "broker in Boca Raton, can help.",
    "sections": [
        ("What the Loan Can and Can't Pay For",
         f"<p>Buying a building rarely means moving in as is. Under {_SOP_A}, build-out of the "
         "space your business uses is part of the real estate project, so it can be financed "
         f"with the purchase, including under {_P}.</p>"
         + table(["Can be in the loan", "Can't be in the loan"], [
             ["Walls, offices, restrooms", "Build-out of space leased to a tenant"],
             ["HVAC, electrical, plumbing", "Work on excess land"],
             ["Code, ADA, licensing work", "Cost overruns after approval (lender's call)"],
             ["Architect and permit costs", "Improvements to an apartment you rent out"],
         ])
         + "<p>If a seller or landlord gives you an improvement allowance, the SOP says it must "
         "first pay down the loan, unless the lender has already counted it in its working "
         "capital analysis.</p>"),
        ("Owned Building Versus Leased Space",
         "<p>The SOP sets different terms for improvements depending on who owns the building:</p>"
         + table(["You are", "Maximum term on the improvements", "What the lender also needs"], [
             ["Buying the building", "Up to 25 years with the real estate, plus construction time", "Appraisal, environmental review"],
             ["Improving a building you lease", "10 years, plus up to 12 months to finish", "Lease and landlord waiver in larger cases"],
         ])
         + "<p>Leasehold improvements over $500,000, or over 30% of the loan (whichever is "
         "less), trigger lease review: for 7(a), the lease plus renewal options should run as "
         "long as the loan. That's one reason growing companies buy instead of building out a "
         "space they rent.</p>"),
        ("Thresholds That Change the Process",
         "<ul>"
         "<li><strong>Over $350,000 of construction.</strong> The lender generally needs a "
         "licensed contractor with 100% performance and payment bonds, builder's risk and "
         "workers' comp, unless a construction manager controls the funds. Below $350,000 the "
         "lender can use its normal construction practices.</li>"
         "<li><strong>Renovation over one-third of the price.</strong> That's substantial "
         "renovation, so the appraisal must value the building as completed. At the end, the "
         "lender needs confirmation the work matches the plans, or a new appraisal.</li>"
         "<li><strong>Doing it yourself.</strong> The SOP calls owner-as-contractor projects "
         "generally unsatisfactory. Allowed only if the lender can justify it.</li>"
         "<li><strong>Lien waivers.</strong> Required from every contractor, subcontractor and "
         "supplier before final payment.</li>"
         "</ul>"),
        ("Worked Example: $2,000,000 Building Plus $250,000 of Work",
         f"<p>{_ILL}A distributor buys a 20,000 sq ft building, occupies 14,000 sq ft and leases "
         "6,000 sq ft. It spends $250,000 on its own office and warehouse space. The tenant "
         "space is left as is. Fees are from the FY2027 7(a) schedule, financed.</p>"
         + table(["Item", "Amount"], [
             ["Purchase price", "$2,000,000"],
             ["Work on buyer's 14,000 sq ft", "$250,000"],
             ["Reports, plans, permits, title", "$21,000"],
             ["7(a) packaging fee (estimate)", "$2,500"],
             ["SBA guaranty fee (computed)", "About $63,220"],
             ["<strong>SBA 7(a) loan, $0 down</strong>", "<strong>About $2,336,720</strong>"],
             ["Assumed rate and term", "7.75%, 25 years"],
             ["Monthly principal and interest", "About $17,650"],
         ])
         + "<p>$250,000 is under both thresholds: it's below $350,000, and well under a third of "
         "$2 million. Occupancy is 70%, which passes the "
         '<a href="' + HUB + '/sba-51-percent-occupancy-rule/">51% occupancy rule</a>. '
         "Lenders typically want the work funded within a few months of closing, so have bids "
         "in hand.</p>"),
        ("Getting the Budget Right",
         "<p>The lender and SBA aren't obligated to raise the loan for overruns, and before "
         "approving a contract change the lender needs proof you can pay the extra. Carry a "
         "contingency in the budget and keep cash for surprises. For older buildings, the "
         '<a href="' + HUB + '/sba-loan-daycare-building/">daycare building guide</a> shows how '
         "lead testing adds to the scope.</p>"
         + _CTA),
    ],
    "faqs": [
        ("Can I add renovation costs to an SBA loan to buy a building?",
         "Yes. Improvements to the space your business will use can be financed with the "
         "purchase and repaid over the real estate term."),
        ("Can SBA money pay for a tenant's build-out?",
         "No. SBA proceeds can't improve or renovate space leased to a third party."),
        ("When do I need bonded contractors?",
         "When the construction part of a 7(a) loan is over $350,000, unless the lender uses a "
         "construction manager that controls the funds."),
        ("What is an as-completed appraisal?",
         "When renovation costs exceed a third of the purchase price, the appraiser values the "
         "property as it will be once the work is done."),
        ("What's the term on leasehold improvements if I don't own the building?",
         "Up to 10 years, plus up to 12 months to complete the work."),
    ],
    "related": [
        (PILLAR, "100% SBA financing"),
        (HUB + "/sba-51-percent-occupancy-rule/", "The SBA 51% occupancy rule"),
        (HUB + "/sba-loan-daycare-building/", "Daycare building financing"),
        ("/commercial-real-estate-loans/articles/construction-to-permanent-financing/", "Construction-to-permanent financing"),
        ("/sba-loans/articles/sba-7a-vs-504-loan/", "SBA 7(a) vs 504"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, FEES, OCC, SBA_7A],
},
# ---------------------------------------------------------------- 6. assisted living
{
    "slug": "assisted-living-facility-sba-loan",
    "crumb": "Assisted Living SBA Financing",
    "title": "SBA Loans for Assisted Living Facilities | Axiant",
    "og_title": "SBA Loans for Assisted Living and Memory Care Facilities",
    "h1": "SBA Loans for Assisted Living and Memory Care Facilities",
    "headline": "SBA Loans for Assisted Living and Memory Care Facilities: Eligibility and Structure",
    "lede": "Which residential care businesses are eligible, the difference between an operator "
            "buying its building and buying a facility, and how payer mix shapes the deal",
    "meta_desc": "SBA loans for assisted living and memory care: the licensing test for eligibility, 100% for operators buying their building, 10% on acquisitions, and examples.",
    "article_desc": "How licensed assisted living and memory care operators use SBA 7(a) and "
                    "504 loans, with the SOP's eligibility test and computed examples.",
    "keywords": "sba loan assisted living facility, assisted living financing, memory care "
                "facility loan, sba loan residential care facility, buy assisted living facility",
    "quick_answer": "As of November 2026, assisted living and memory care facilities qualify for "
                    "SBA loans if they're <strong>licensed</strong> and provide healthcare "
                    "services such as medication help or wellness checks. Unlicensed residential "
                    "homes don't. An established operator buying its own building may find "
                    "100% financing; buying a running facility needs at least <strong>10%"
                    "</strong> down. Axiant Partners, a broker in Boca Raton, finds these lenders.",
    "sections": [
        ("The Eligibility Test",
         f"<p>{_SOP_A} makes nursing homes, assisted living facilities and state-licensed "
         "equivalents eligible when they <strong>provide healthcare or medical services</strong>. "
         "It lists wellness checks, monitoring or helping with medication, monitoring blood "
         "sugar and having medical staff on site, even part time. Residential facilities that "
         "aren't licensed this way and don't provide those services are ineligible, as are "
         "apartment buildings. The lender reads your license to decide.</p>"
         "<p>Memory care usually qualifies under the same test, since it's licensed care with "
         "medication oversight. Independent living that only rents units and serves meals "
         "usually doesn't.</p>"),
        ("Two Very Different Deals",
         table(["", "Operator buys its building", "Buyer acquires a running facility"], [
             ["SBA treatment", "Real estate purchase, no ownership change", "Change of ownership"],
             ["Minimum equity", "No fixed SBA minimum; some lenders go to 100%", "10% of total project cost"],
             ["Cash flow test", "Lender's analysis of history", "1.25x debt service coverage"],
             ["Maximum term", "25 years", "25 years if 85%+ of project is real estate"],
             ["Valuation", "Real estate appraisal", "Going concern appraisal by a specialist"],
         ])
         + f"<p>The first column is the {_P} case. In the second, the SOP treats an assisted "
         "living building as a special purpose property. When the building can't be separated "
         "from the business and is 85% or more of the cost, the whole loan can run 25 years. The "
         "appraiser must have done at least four going concern appraisals of similar properties "
         "in the last 36 months.</p>"),
        ("Worked Examples",
         f"<p>{_ILL}Fees are from the FY2027 7(a) schedule, financed.</p>"
         + table(["", "Operator buys its building", "Buyer acquires a facility"], [
             ["Price", "$3,200,000", "$4,000,000"],
             ["Reports and packaging (est.)", "$26,500", "$32,500"],
             ["Cash down", "$0", "About $403,250 (10%)"],
             ["SBA guaranty fee (computed)", "About $90,799", "About $102,454"],
             ["<strong>SBA 7(a) loan</strong>", "<strong>About $3,317,299</strong>", "<strong>About $3,731,704</strong>"],
             ["Payment, 7.75% over 25 yrs", "About $25,057", "About $28,187"],
         ])
         + "<p>On the acquisition, annual payments of about $338,240 mean the facility needs "
         "about $422,800 of cash flow for debt service to clear 1.25x, from last year's or a "
         "two-year average of actual results.</p>"),
        ("Payer Mix and What Lenders Look At",
         "<p>This is lender practice, not SBA rule. Most lenders are most comfortable with "
         "facilities that are mostly private pay. Heavy reliance on Medicaid waiver programs "
         "usually means tighter margins and state rate risk, so expect more questions and "
         "sometimes more cash down. Lenders also look at:</p>"
         "<ul>"
         "<li><strong>Occupancy history</strong> by month for two or three years.</li>"
         "<li><strong>State survey results</strong> and any citations or enforcement.</li>"
         "<li><strong>Licensed beds versus occupied beds</strong>, and whether the license "
         "transfers to a buyer.</li>"
         "<li><strong>Staffing costs and the administrator's experience.</strong></li>"
         "<li><strong>Management agreements.</strong> The lender must review them; an agreement "
         "that hands control to an outside operator can make the business an ineligible passive "
         "company.</li>"
         "</ul>"),
        ("SBA 504 as an Alternative",
         "<p>A 504 offers a fixed rate on the SBA portion. Because assisted living is on the "
         "SOP's limited or special purpose list, the borrower contributes at least "
         "<strong>15%</strong>, or <strong>20%</strong> if the business is also new. On a "
         "$4,000,000 project at 15%, that's $600,000 down, a $2,000,000 bank loan and a "
         "$1,400,000 debenture. See <a href=\"/sba-loans/articles/sba-504-loan-fees/\">504 loan "
         "fees</a> for the costs. For other healthcare real estate, see the "
         '<a href="/healthcare-practice-financing-guide/">healthcare practice financing guide</a>.</p>'
         + _CTA),
    ],
    "faqs": [
        ("Are assisted living facilities eligible for SBA loans?",
         "Yes, if they are licensed as assisted living or nursing homes, or a state equivalent, "
         "and provide healthcare services such as medication help or wellness checks."),
        ("Can an unlicensed group home get an SBA loan?",
         "No. Residential facilities that aren't licensed as nursing homes or assisted living and "
         "don't provide healthcare services are ineligible."),
        ("How much down do I need to buy an assisted living facility?",
         "Buying a running facility is a change of ownership, so the SBA minimum is 10% of the "
         "total project cost. An operator buying its own building may find lenders that go to 100%."),
        ("What term can I get?",
         "Up to 25 years on real estate. On an acquisition, the whole loan can be 25 years if the "
         "property is 85% or more of the project and can't be separated from the business."),
        ("Do lenders care about Medicaid residents?",
         "Many lenders prefer mostly private-pay facilities and look harder at heavy Medicaid "
         "reliance. That's lender practice, not an SBA rule, and lenders differ."),
        ("How much is down on an SBA 504 for assisted living?",
         "At least 15%, because it's a special purpose property, or 20% for a new business."),
    ],
    "related": [
        (PILLAR, "100% SBA financing"),
        (HUB + "/sba-51-percent-occupancy-rule/", "The SBA 51% occupancy rule"),
        (HUB + "/tenant-improvements-sba-building-purchase/", "Improvements in a purchase"),
        ("/healthcare-practice-financing-guide/", "Healthcare practice financing"),
        ("/business-acquisition-financing/articles/buy-a-business-with-5-percent-down/", "Buying a business with 5% down"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [SOP, FEES, SBA_7A, SBA_504],
},
]
