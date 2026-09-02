# -*- coding: utf-8 -*-
"""Data center cluster, article 4."""

from cluster_datacenter import (DOE, ENERGY_STAR, EIA, SBA_504, SBA_7A,
                                IRS_179, SLOOS)

MORE = [
    {
        "slug": "power-cooling-and-ups-infrastructure-financing",
        "crumb": "Power, Cooling and UPS",
        "title": "Power, Cooling and UPS Infrastructure Financing | Axiant "
                 "Partners",
        "og_title": "Power, Cooling and UPS Infrastructure Financing",
        "h1": "Power, Cooling and UPS Infrastructure Financing",
        "headline": "Power, Cooling and UPS Infrastructure Financing",
        "lede": "The long-lived half of a data center, and why it finances "
                "like a building",
        "meta_desc": "How data center power, cooling and UPS infrastructure is "
                     "financed: long terms for long-lived plant, why ownership "
                     "of the premises matters, and where SBA 504 fits.",
        "article_desc": "Financing the electrical and mechanical plant behind a "
                        "deployment, on terms that match its life.",
        "keywords": "ups financing, data center cooling financing, generator "
                    "financing, crac unit loan, power infrastructure finance",
        "quick_answer": "Power and cooling plant lasts far longer than the "
                        "compute it supports &mdash; often <strong>ten years or "
                        "more</strong> &mdash; and finances accordingly, on "
                        "longer terms than servers. The decisive question is "
                        "whether you <strong>own the building</strong>. In an "
                        "owned facility this is real, securable infrastructure; "
                        "in leased space much of it becomes a leasehold "
                        "improvement.",
        "sections": [
            ("A Different Clock Entirely",
             "<p>The mechanical and electrical layer is the part of a data "
             "center that behaves like ordinary industrial plant.</p>"
             "<p>Switchgear, generators, uninterruptible power supplies, "
             "computer room air handlers, chillers and containment do not "
             "become obsolete when a faster processor is announced. They are "
             "sized for a load, they wear rather than age out, and with "
             "maintenance they run for a decade or considerably longer. That is "
             "why they finance on terms that would be reckless for "
             "compute.</p>"
             "<p>Operators who bundle the whole deployment into one facility "
             "usually end up on the compute clock, paying off long-lived plant "
             "in three years because that is what the server portion "
             "dictated.</p>"),
            ("Component Lives and How They Finance",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Component</th><th>Useful life</th>"
             "<th>Financing note</th></tr></thead><tbody>"
             '<tr><td data-label="Component">Switchgear and distribution</td>'
             '<td data-label="Life">Twenty years or more</td>'
             '<td data-label="Note">Building infrastructure; longest terms</td></tr>'
             '<tr><td data-label="Component">Standby generators</td>'
             '<td data-label="Life">Twenty years or more</td>'
             '<td data-label="Note">Identifiable, resaleable, good '
             "collateral</td></tr>"
             '<tr><td data-label="Component">UPS systems</td>'
             '<td data-label="Life">Around ten years; batteries far less</td>'
             '<td data-label="Note">Budget battery replacement separately</td></tr>'
             '<tr><td data-label="Component">CRAC and CRAH units</td>'
             '<td data-label="Life">Fifteen years or so</td>'
             '<td data-label="Note">Conventional equipment finance</td></tr>'
             '<tr><td data-label="Component">Chillers and condensers</td>'
             '<td data-label="Life">Twenty years or so</td>'
             '<td data-label="Note">Often building-attached</td></tr>'
             '<tr><td data-label="Component">Containment and airflow</td>'
             '<td data-label="Life">Long, but fixed in place</td>'
             '<td data-label="Note">Leasehold unless you own</td></tr>'
             "</tbody></table></div>"
             "<p>Batteries deserve a separate line in any budget. The UPS lasts "
             "a decade; the batteries inside it do not, and a replacement cycle "
             "that arrives unbudgeted is a genuinely unpleasant surprise.</p>"),
            ("Owning the Building Changes the Structure",
             "<p>This is the fork in the road, and it decides which products "
             "are even available.</p>"
             "<p>In an owned facility, the electrical and mechanical plant is "
             "part of the real property improvement, which opens longer-term "
             "options including the "
             '<a href="https://www.sba.gov/funding-programs/loans/504-loans" '
             'rel="noopener nofollow" target="_blank">SBA 504 program</a>, '
             "designed for exactly this kind of major fixed asset. Terms run "
             "long because the asset does.</p>"
             "<p>In leased space, the same equipment installed the same way is "
             "frequently a leasehold improvement, and the finance term is "
             "capped by the lease. It is the identical chiller doing the "
             "identical job, financed on entirely different terms because of "
             "who owns the slab it sits on.</p>"),
            ("Efficiency Is Part of the Case",
             "<p>Power is the dominant operating cost in this category, so an "
             "efficiency upgrade is partly a financing argument.</p>"
             "<p>Higher-efficiency UPS units, better containment and modern "
             "cooling reduce the monthly bill, and that saving services debt. "
             "The "
             '<a href="https://www.energystar.gov/products/data_center_equipment" '
             'rel="noopener nofollow" target="_blank">ENERGY STAR '
             "specifications for data center equipment</a> are a reasonable "
             "reference point for what qualifies as efficient, and utility "
             "incentive programs sometimes contribute to the cost.</p>"
             "<p>Where the saving is real, quantify it. A project that reduces "
             "a known monthly cost is easier to underwrite than one that only "
             "adds capacity, because part of the repayment is already visible "
             "in the existing bills.</p>"),
            ("Structuring the Infrastructure Layer",
             "<ul>"
             "<li><strong>Finance it separately from compute</strong> and match "
             "the term to the plant's life.</li>"
             "<li><strong>Establish ownership of the premises first</strong>; "
             "it decides the available structures.</li>"
             "<li><strong>Budget UPS batteries</strong> as a separate "
             "replacement cycle.</li>"
             "<li><strong>Quantify the efficiency saving</strong> against "
             "current bills.</li>"
             "<li><strong>Size for the load you are heading toward</strong>, "
             "not today's, if density is rising.</li>"
             "<li><strong>Check utility incentives</strong> before finalizing "
             "the budget.</li>"
             "</ul>"
             "<p>Sized and financed properly, this layer is the least "
             "troublesome part of a deployment. It is well understood, it is "
             "durable, and lenders are comfortable with it. The projects that "
             "go wrong are almost always the ones where the plant was treated "
             "as an accessory to the servers rather than as the long-lived "
             "infrastructure that outlives three generations of them.</p>"
             '<p>See <a href="../server-and-networking-equipment-financing/">'
             "server and networking equipment financing</a> for the short-cycle "
             "half, or "
             '<a href="../colocation-buildout-financing/">colocation build-out '
             "financing</a> if the space is leased.</p>"),
        ],
        "faqs": [
            ("How long can power and cooling infrastructure be financed for?",
             "Considerably longer than compute. Switchgear, generators and "
             "chillers last fifteen to twenty years or more, so terms are "
             "matched to that life rather than to a server refresh cycle."),
            ("Should power infrastructure be in the same loan as servers?",
             "No. The two have very different useful lives, and one term cannot "
             "suit both. Bundling them usually means paying off long-lived "
             "plant on the compute clock, which is expensive."),
            ("Does SBA 504 apply to data center infrastructure?",
             "It can, where you own the facility and the work is a major fixed "
             "asset improvement. The program is designed for long-term, "
             "fixed-rate financing of exactly that kind of asset."),
            ("Why are UPS batteries budgeted separately?",
             "Because they wear out far sooner than the UPS itself. The unit "
             "may run for a decade while the batteries inside need replacing "
             "well before that, and an unbudgeted replacement cycle is a common "
             "cash flow shock."),
            ("Do efficiency upgrades help a financing case?",
             "Yes, when the saving is quantified. A reduction in a known "
             "monthly power bill is visible cash flow that services the debt, "
             "which is a stronger argument than added capacity alone. Utility "
             "incentive programs may also offset part of the cost."),
        ],
        "related": [
            ("/data-center-financing.html", "Data center financing"),
            ("../server-and-networking-equipment-financing/",
             "Server and networking equipment financing"),
            ("../colocation-buildout-financing/", "Colocation build-out financing"),
            ("../gpu-cluster-financing/", "GPU cluster financing"),
        ],
        "sources": [SBA_504, ENERGY_STAR, DOE],
    },
]
