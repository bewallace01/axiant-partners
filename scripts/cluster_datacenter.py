# -*- coding: utf-8 -*-
"""Data center and IT infrastructure financing - 4 articles.
Thin verticals, 4 of 4.

Pillar deepened to 1,856 words with a comparison table before this cluster was
built, per the plan's gate.

Ranges are described as conventional across lenders, never quoted as anyone's
terms. No funded totals, no years in business, no testimonials, no invented
figures. One entity: Axiant Partners, (561) 268-0465, Boca Raton.
"""

CLUSTER = {
    "pillar": "data-center-financing.html",
    "hub": "data-center-financing/articles",
    "crumb": "Data Center Financing",
    "cta_inline": "See what your deployment supports",
    "cta_button": "Get Matched for Data Center Financing",
    "hub_title": "Data Center and IT Infrastructure Financing Guides | Axiant "
                 "Partners",
    "hub_h1": "Data Center Financing Articles",
    "hub_lede": "Compute, colocation, GPUs and the power layer - financed on "
                "different clocks",
    "hub_desc": "Guides to financing data center and IT infrastructure: server "
                "and networking equipment, colocation build-outs, GPU clusters, "
                "and power, cooling and UPS infrastructure.",
    "hub_intro": "A data center deployment is not one purchase. Compute "
                 "refreshes on a short cycle, power and cooling last a decade, "
                 "and a colocation build-out is mostly leasehold work in "
                 "somebody else's building. These guides cover how each layer "
                 "is financed and why the terms differ. Start with "
                 "<a href=\"/data-center-financing.html\">data center "
                 "financing</a>, or see "
                 "<a href=\"/equipment-appraisal.html\">how equipment is "
                 "appraised</a>.",
    "hub_cta_h2": "Planning a build-out or a refresh?",
    "hub_cta_p": "Tell us the deployment, the timeline and the amount. We will "
                 "tell you plainly what terms are realistic.",
}

DOE = ("https://www.energy.gov/eere/buildings/data-centers-and-servers",
       "US Department of Energy: Data Centers and Servers",
       "Federal guidance on data center energy use, efficiency measures and "
       "the infrastructure that consumes the load.")
ENERGY_STAR = ("https://www.energystar.gov/products/data_center_equipment",
               "ENERGY STAR Data Center Equipment",
               "Efficiency specifications for servers, storage and UPS "
               "equipment, and the programs that recognize them.")
EIA = ("https://www.eia.gov/todayinenergy/",
       "US Energy Information Administration",
       "Official energy data and analysis, including electricity demand from "
       "commercial and industrial consumers.")
SBA_504 = ("https://www.sba.gov/funding-programs/loans/504-loans",
           "SBA 504 Loan Program",
           "Long-term, fixed-rate financing for major fixed assets, including "
           "owner-occupied facilities and heavy building infrastructure.")
SBA_7A = ("https://www.sba.gov/funding-programs/loans/7a-loans",
          "SBA 7(a) Loan Program",
          "Official terms and eligibility for the SBA's primary business loan.")
IRS_179 = ("https://www.irs.gov/publications/p946",
           "IRS Publication 946: How to Depreciate Property",
           "The authoritative source on depreciation and the Section 179 "
           "deduction, including what qualifies and the annual limits.")
SLOOS = ("https://www.federalreserve.gov/data/sloos.htm",
         "Federal Reserve Senior Loan Officer Opinion Survey",
         "Quarterly survey of bank lending standards and collateral "
         "requirements.")

ARTICLES = [
    {
        "slug": "server-and-networking-equipment-financing",
        "crumb": "Server and Networking Equipment",
        "title": "Server and Networking Equipment Financing | Axiant Partners",
        "og_title": "Server and Networking Equipment Financing: Matching the "
                    "Refresh Cycle",
        "h1": "Server and Networking Equipment Financing",
        "headline": "Server and Networking Equipment Financing",
        "lede": "Why compute is financed short and what happens when it is not",
        "meta_desc": "How server and networking equipment is financed: matching "
                     "the term to the refresh cycle, why compute depreciates "
                     "fast, and when leasing beats owning.",
        "article_desc": "How compute and network hardware is financed, and why "
                        "term length is the decision that matters most.",
        "keywords": "server financing, networking equipment loan, IT equipment "
                    "finance, server lease, switch and router financing",
        "quick_answer": "Servers and networking gear are financed on "
                        "<strong>short terms matched to the refresh "
                        "cycle</strong> &mdash; commonly three years, sometimes "
                        "four or five for network hardware that ages more "
                        "slowly. The mistake that hurts is a five-year loan on "
                        "a three-year asset, which leaves you paying for "
                        "equipment you have already replaced.",
        "sections": [
            ("Compute Ages Differently From Everything Else",
             "<p>Almost every financing error in this category comes from the "
             "same place: treating compute as though it were machinery.</p>"
             "<p>A CNC machine bought today is worth using in twelve years. A "
             "server bought today is competing against something meaningfully "
             "faster within three, and against something meaningfully cheaper "
             "per unit of work within four. That is not wear. The hardware "
             "still runs; it simply stops being the sensible thing to run the "
             "workload on.</p>"
             "<p>Lenders know this, which is why the terms offered on compute "
             "are shorter than the terms on almost anything else a business "
             "buys at the same price. It is not a worse deal. It is the term "
             "matching the asset.</p>"),
            ("Terms by Layer",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Layer</th><th>Typical useful life</th>"
             "<th>How it is usually financed</th></tr></thead><tbody>"
             '<tr><td data-label="Layer">Servers and compute</td>'
             '<td data-label="Life">Around three years</td>'
             '<td data-label="Financed">Lease or short-term loan</td></tr>'
             '<tr><td data-label="Layer">Storage arrays</td>'
             '<td data-label="Life">Three to five years</td>'
             '<td data-label="Financed">Lease or term loan</td></tr>'
             '<tr><td data-label="Layer">Switches and routers</td>'
             '<td data-label="Life">Five years or more</td>'
             '<td data-label="Financed">Term loan; ownership makes sense</td></tr>'
             '<tr><td data-label="Layer">Racks and cabling</td>'
             '<td data-label="Life">A decade or more</td>'
             '<td data-label="Financed">Owned, often inside a build-out '
             "facility</td></tr>"
             '<tr><td data-label="Layer">Software and licenses</td>'
             '<td data-label="Life">Subscription</td>'
             '<td data-label="Financed">Operating cost, not capital</td></tr>'
             "</tbody></table></div>"
             "<p>A deployment that mixes all five and finances them on one "
             "term gets the term wrong for most of them. Splitting the request "
             "by layer is more work up front and materially cheaper across the "
             "life of the equipment.</p>"),
            ("Lease Against Own",
             "<p>The honest version of this comparison is shorter than most "
             "vendors make it.</p>"
             "<p><strong>Lease</strong> when you intend to refresh on schedule "
             "and want the upgrade path built in. You are paying for the use of "
             "current hardware and handing back the disposal problem, which for "
             "servers holding data is a real problem worth handing back.</p>"
             "<p><strong>Own</strong> when the equipment will outlive the "
             "finance term and you will still want it &mdash; network hardware, "
             "racks, anything structural. Ownership also matters where a "
             "Section 179 deduction is part of the plan, and the "
             '<a href="https://www.irs.gov/publications/p946" '
             'rel="noopener nofollow" target="_blank">IRS depreciation '
             "guidance</a> is the place to confirm what qualifies rather than a "
             "vendor's summary of it.</p>"),
            ("What Lenders Ask an IT Buyer",
             "<p>The questions are predictable and worth preparing for.</p>"
             "<p>What is the workload, and is it contracted or internal? Where "
             "will the equipment physically sit, and do you control that space? "
             "What happens to the current estate &mdash; sold, redeployed, or "
             "carried alongside the new gear? Is any of this a replacement for "
             "cloud spend, and if so, what does the comparison actually look "
             "like?</p>"
             "<p>That last one comes up more than it used to. A lender is "
             "reasonably interested in whether an on-premises deployment is "
             "cheaper than what it replaces, because that is the cash flow "
             "servicing the loan.</p>"),
            ("Getting the Structure Right",
             "<ul>"
             "<li><strong>Split the request by layer</strong> and match each "
             "term to its life.</li>"
             "<li><strong>Never finance compute past its refresh</strong> "
             "&mdash; the classic and expensive mistake.</li>"
             "<li><strong>Treat licenses as operating cost</strong>, not "
             "capital.</li>"
             "<li><strong>Plan the disposal</strong> of the outgoing estate, "
             "including data destruction.</li>"
             "<li><strong>Confirm the tax treatment</strong> with your "
             "accountant before it drives the structure.</li>"
             "</ul>"
             "<p>None of this is complicated, but it is easy to skip when a "
             "vendor offers a single facility covering the whole quote. That "
             "convenience is usually paid for twice: once in the term applied "
             "to the wrong layer, and again at the refresh, when part of the "
             "old estate is still on the books. Ten minutes splitting the "
             "budget by useful life is the highest-return work in the whole "
             "purchase.</p>"
             '<p>See <a href="../power-cooling-and-ups-infrastructure-financing/">'
             "power, cooling and UPS financing</a> for the long-lived half of "
             "the same deployment.</p>"),
        ],
        "faqs": [
            ("How long should a server loan run?",
             "Roughly as long as you intend to run the servers &mdash; commonly "
             "about three years. Financing compute over five leaves you making "
             "payments on hardware you have already replaced, which is the most "
             "common and most expensive mistake in this category."),
            ("Should I lease or buy servers?",
             "Lease if you refresh on a schedule and want the upgrade path and "
             "disposal handled. Buy if the equipment will outlive the finance "
             "term and you will still want it, which is more often true of "
             "network hardware than of compute."),
            ("Can networking equipment be financed for longer?",
             "Usually yes. Switches and routers age more slowly than servers "
             "and stay useful for five years or more, so lenders are "
             "comfortable with longer terms and ownership generally makes more "
             "sense."),
            ("Does Section 179 apply to IT equipment?",
             "It can, for equipment you own and place in service. The IRS "
             "publication on depreciation is the authoritative source on what "
             "qualifies and the annual limits &mdash; confirm the treatment "
             "with your accountant rather than relying on a vendor summary."),
            ("Do lenders care that I am replacing cloud spend?",
             "Yes, and favorably when the numbers hold up. If the deployment is "
             "cheaper than the cloud spend it replaces, that saving is part of "
             "the cash flow servicing the loan and is worth showing "
             "explicitly."),
        ],
        "related": [
            ("/data-center-financing.html", "Data center financing"),
            ("../power-cooling-and-ups-infrastructure-financing/",
             "Power, cooling and UPS infrastructure financing"),
            ("../gpu-cluster-financing/", "GPU cluster financing"),
            ("../colocation-buildout-financing/", "Colocation build-out financing"),
        ],
        "sources": [IRS_179, ENERGY_STAR, SLOOS],
    },
]

# The remaining data center articles live in companion modules.
from cluster_datacenter_b import MORE as _B
ARTICLES = ARTICLES + _B

from cluster_datacenter_c import MORE as _C
ARTICLES = ARTICLES + _C
