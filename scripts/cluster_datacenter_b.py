# -*- coding: utf-8 -*-
"""Data center cluster, articles 2 and 3."""

from cluster_datacenter import (DOE, ENERGY_STAR, EIA, SBA_504, SBA_7A,
                                IRS_179, SLOOS)

MORE = [
    {
        "slug": "colocation-buildout-financing",
        "crumb": "Colocation Build-Out",
        "title": "Colocation Build-Out Financing | Axiant Partners",
        "og_title": "Colocation Build-Out Financing: Spending in Someone "
                    "Else's Building",
        "h1": "Colocation Build-Out Financing",
        "headline": "Colocation Build-Out Financing",
        "lede": "How lenders treat capital you sink into leased rack space",
        "meta_desc": "How colocation build-outs are financed: which costs are "
                     "movable assets, which are leasehold improvements, and why "
                     "the facility lease term shapes the loan.",
        "article_desc": "Financing a colocation deployment, where much of the "
                        "spend cannot be repossessed.",
        "keywords": "colocation financing, data center build out loan, colo "
                    "deployment financing, leasehold improvement financing",
        "quick_answer": "A colocation build-out splits into two kinds of "
                        "spending: <strong>movable equipment</strong> you can "
                        "take with you, and <strong>leasehold work</strong> you "
                        "cannot. The first finances normally. The second is "
                        "harder, shorter and usually needs to fit inside the "
                        "facility lease term &mdash; no lender wants collateral "
                        "bolted into a building you may leave.",
        "sections": [
            ("The Split That Governs Everything",
             "<p>Before anything else, separate the invoice into what leaves "
             "with you and what stays behind.</p>"
             "<p>Servers, storage, switches, PDUs and the racks themselves are "
             "yours; they can be uninstalled, moved and sold. Structured "
             "cabling run through a facility's trays, custom containment, "
             "electrical work terminated in the provider's plant and anything "
             "physically integrated into the building is a leasehold "
             "improvement. You paid for it, and you cannot take it.</p>"
             "<p>Lenders draw exactly this line. It is not an accounting "
             "nicety; it decides which parts of the project are securable and "
             "therefore which parts get reasonable terms.</p>"),
            ("What Each Category Looks Like",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Cost</th><th>Category</th>"
             "<th>Financing character</th></tr></thead><tbody>"
             '<tr><td data-label="Cost">Servers, storage, network</td>'
             '<td data-label="Category">Movable equipment</td>'
             '<td data-label="Character">Standard equipment finance</td></tr>'
             '<tr><td data-label="Cost">Racks, rails, PDUs</td>'
             '<td data-label="Category">Movable equipment</td>'
             '<td data-label="Character">Financeable, modest value</td></tr>'
             '<tr><td data-label="Cost">Structured cabling</td>'
             '<td data-label="Category">Leasehold</td>'
             '<td data-label="Character">Hard to secure; shorter term</td></tr>'
             '<tr><td data-label="Cost">Containment and airflow work</td>'
             '<td data-label="Category">Leasehold</td>'
             '<td data-label="Character">Hard to secure</td></tr>'
             '<tr><td data-label="Cost">Electrical termination</td>'
             '<td data-label="Category">Leasehold</td>'
             '<td data-label="Character">Hard to secure</td></tr>'
             '<tr><td data-label="Cost">Deposits and cross-connect fees</td>'
             '<td data-label="Category">Operating</td>'
             '<td data-label="Character">Working capital</td></tr>'
             "</tbody></table></div>"
             "<p>A project that is mostly the top two rows finances easily. One "
             "that is mostly the middle three needs either a stronger balance "
             "sheet, a shorter term, or a structure that leans on the business "
             "rather than the improvements.</p>"),
            ("The Lease Term Is a Ceiling",
             "<p>The single constraint operators most often overlook is the "
             "facility contract itself.</p>"
             "<p>If your colocation agreement runs three years, a lender is "
             "unwilling to write five years of finance against work embedded in "
             "that space. The reasoning is plain: at the end of year three you "
             "may not be there, and the collateral cannot follow you. Where the "
             "lease has renewal options, say so and document them &mdash; a "
             "long agreement with a stable provider changes what a lender will "
             "consider.</p>"
             "<p>The practical consequence is that lease negotiation and "
             "finance planning belong in the same conversation. Signing a short "
             "facility term and then seeking long finance for a heavy build-out "
             "puts the two documents in conflict.</p>"),
            ("Power and Density Change the Numbers",
             "<p>Colocation is priced on power far more than on floor space, "
             "and modern deployments draw more of it per rack.</p>"
             "<p>Higher density means more electrical work, more containment "
             "and sometimes liquid cooling &mdash; all of which pushes the "
             "project toward the leasehold side of the table. The "
             '<a href="https://www.energy.gov/eere/buildings/data-centers-and-servers" '
             'rel="noopener nofollow" target="_blank">Department of Energy\'s '
             "guidance on data centers and servers</a> is a useful reference "
             "on where the load actually goes.</p>"
             "<p>It also affects the operating case a lender is underwriting. "
             "If your contracted power draw is rising, the monthly bill rises "
             "with it, and that belongs in the projections rather than as a "
             "surprise in month four.</p>"),
            ("Structuring a Colocation Project",
             "<ul>"
             "<li><strong>Split the budget</strong> into movable, leasehold and "
             "operating before you approach anyone.</li>"
             "<li><strong>Match the finance term to the lease term</strong>, "
             "including documented renewal options.</li>"
             "<li><strong>Finance the equipment conventionally</strong> and "
             "treat the improvements as the harder ask.</li>"
             "<li><strong>Model the power bill</strong> at your real target "
             "density, not the starting one.</li>"
             "<li><strong>Bring the customer contracts</strong> if the "
             "deployment serves external clients.</li>"
             "</ul>"
             "<p>The reason this ordering works is that it answers the "
             "underwriter's questions in the sequence they will be asked. What "
             "can you take with you, how long are you entitled to be there, and "
             "what does the space cost to run at the density you are planning. "
             "A budget that arrives already organized around those three "
             "questions tends to move faster than a larger one that is not.</p>"
             '<p>See <a href="../server-and-networking-equipment-financing/">'
             "server and networking equipment financing</a> for the movable "
             "half, or "
             '<a href="../power-cooling-and-ups-infrastructure-financing/">'
             "power and cooling infrastructure</a> where you own the "
             "building.</p>"),
        ],
        "faqs": [
            ("Can I finance a colocation build-out?",
             "The movable equipment, yes, on ordinary equipment finance terms. "
             "The leasehold work &mdash; cabling, containment, electrical "
             "termination &mdash; is harder, because it cannot be repossessed "
             "and stays with the provider's building."),
            ("Why does my facility lease term affect the loan?",
             "Because collateral embedded in leased space is only useful to a "
             "lender while you are in that space. Finance written past the "
             "lease term is secured against something you may no longer have "
             "access to, so lenders generally will not do it."),
            ("What counts as a leasehold improvement in a colo?",
             "Anything physically integrated into the provider's facility: "
             "structured cabling in their trays, custom containment, airflow "
             "work, and electrical terminated in their plant. If it cannot be "
             "unbolted and moved, treat it as leasehold."),
            ("How should I present a colocation project to a lender?",
             "Split the budget into movable equipment, leasehold work and "
             "operating costs, and bring the facility lease with any renewal "
             "options documented. That split is the first thing an underwriter "
             "will do anyway."),
            ("Does higher rack density make financing harder?",
             "Somewhat, because density pushes spend toward electrical and "
             "cooling work that sits on the leasehold side. It also raises the "
             "monthly power bill, which belongs in the projections from the "
             "start."),
        ],
        "related": [
            ("/data-center-financing.html", "Data center financing"),
            ("../server-and-networking-equipment-financing/",
             "Server and networking equipment financing"),
            ("../power-cooling-and-ups-infrastructure-financing/",
             "Power, cooling and UPS infrastructure financing"),
            ("../gpu-cluster-financing/", "GPU cluster financing"),
        ],
        "sources": [DOE, SBA_7A, SLOOS],
    },
    {
        "slug": "gpu-cluster-financing",
        "crumb": "GPU Cluster Financing",
        "title": "GPU Cluster Financing | Axiant Partners",
        "og_title": "GPU Cluster Financing: Expensive, Fast-Moving, Contract-"
                    "Driven",
        "h1": "GPU Cluster Financing",
        "headline": "GPU Cluster Financing",
        "lede": "High value, short life and a resale market nobody can promise "
                "you",
        "meta_desc": "How GPU clusters are financed: why the hardware's value "
                     "is real but volatile, what lenders ask about utilization "
                     "and contracts, and which terms fit.",
        "article_desc": "Financing accelerated compute, where the collateral is "
                        "valuable and the market is unpredictable.",
        "keywords": "gpu cluster financing, ai hardware financing, gpu server "
                    "loan, accelerated compute finance",
        "quick_answer": "GPU hardware is unusual collateral: <strong>genuinely "
                        "valuable</strong>, but on a short and unpredictable "
                        "curve. Lenders respond with shorter terms and more "
                        "attention to <strong>contracted utilization</strong> "
                        "than to the equipment list. A cluster with committed "
                        "workload behind it finances on very different terms "
                        "from one bought speculatively.",
        "sections": [
            ("Valuable Collateral, Uncertain Curve",
             "<p>GPU clusters break the usual pattern. The hardware is "
             "expensive enough to be worth securing against, which is unusual "
             "for IT equipment, and its value moves in ways that are hard to "
             "underwrite.</p>"
             "<p>Demand has been strong enough that used accelerators have held "
             "value better than most compute. But the same hardware sits in a "
             "market shaped by supply allocation, new architecture releases and "
             "the appetite of a small number of very large buyers. A lender "
             "looking at a three-year residual is being asked to forecast "
             "something nobody in the industry forecasts confidently.</p>"
             "<p>The result is not refusal. It is caution: shorter terms, more "
             "equity, and considerably more interest in what the cluster is "
             "contracted to do.</p>"),
            ("What Changes the Terms",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Factor</th><th>Helps</th>"
             "<th>Hurts</th></tr></thead><tbody>"
             '<tr><td data-label="Factor">Workload</td>'
             '<td data-label="Helps">Contracted, named counterparty</td>'
             '<td data-label="Hurts">Speculative capacity</td></tr>'
             '<tr><td data-label="Factor">Utilization</td>'
             '<td data-label="Helps">Existing clusters running near '
             "capacity</td>"
             '<td data-label="Hurts">No operating history</td></tr>'
             '<tr><td data-label="Factor">Hosting</td>'
             '<td data-label="Helps">Power and cooling already secured</td>'
             '<td data-label="Hurts">No site able to take the load</td></tr>'
             '<tr><td data-label="Factor">Term</td>'
             '<td data-label="Helps">Two to three years</td>'
             '<td data-label="Hurts">Five years on this hardware</td></tr>'
             '<tr><td data-label="Factor">Equity</td>'
             '<td data-label="Helps">Meaningful contribution</td>'
             '<td data-label="Hurts">Full-value request</td></tr>'
             "</tbody></table></div>"
             "<p>Read down the middle column and a pattern emerges: everything "
             "that helps is evidence the cluster will earn, not evidence it is "
             "worth money.</p>"),
            ("The Power Problem Comes First",
             "<p>A surprising number of GPU financing conversations stall on "
             "something that has nothing to do with credit.</p>"
             "<p>Accelerated compute draws far more power per rack than "
             "conventional servers, and rejects far more heat. Many facilities "
             "cannot supply it, and securing the power can take longer than "
             "securing the finance. The "
             '<a href="https://www.eia.gov/todayinenergy/" '
             'rel="noopener nofollow" target="_blank">Energy Information '
             "Administration</a> tracks the electricity demand picture "
             "commercial consumers are competing inside of.</p>"
             "<p>Establish where the cluster will live and that the site can "
             "actually power and cool it before you arrange finance. A lender "
             "asking that question and receiving a vague answer will slow "
             "down.</p>"),
            ("Terms That Fit the Asset",
             "<p>Because the residual is uncertain, the sensible structures are "
             "short and tied to revenue.</p>"
             "<p>Two to three years is the common range, with payments sized "
             "against contracted utilization rather than projected demand. "
             "Where the workload is genuinely committed &mdash; a customer "
             "contract, an internal program with a budget behind it &mdash; "
             "that commitment does more for the terms than any argument about "
             "the hardware's resale value.</p>"
             "<p>Where it is not committed, be honest about that. Speculative "
             "capacity is financeable, but at terms that reflect what it is, "
             "and pretending otherwise wastes everyone's time in "
             "diligence.</p>"
             "<p>Equity contribution is the other lever. A lender uncertain "
             "about a residual becomes considerably more comfortable when the "
             "borrower is carrying part of that uncertainty alongside them, and "
             "on this asset class a meaningful contribution often does more for "
             "the rate than any amount of argument about demand.</p>"),
            ("Preparing a GPU Cluster Request",
             "<ul>"
             "<li><strong>Lead with the contracted workload</strong>, "
             "counterparty and term.</li>"
             "<li><strong>Secure the site first</strong> &mdash; power, "
             "cooling and space.</li>"
             "<li><strong>Show utilization</strong> on anything you already "
             "run.</li>"
             "<li><strong>Keep the term short</strong> and match it to the "
             "revenue commitment.</li>"
             "<li><strong>Expect to contribute equity</strong> on a volatile "
             "asset class.</li>"
             "<li><strong>Separate the power build</strong> from the hardware "
             "request; they finance differently.</li>"
             "</ul>"
             "<p>Underneath all of it is one idea worth holding on to: in this "
             "category the collateral is the weaker argument and the workload "
             "is the stronger one. That is the reverse of most equipment "
             "lending, and operators who lead with the hardware spend the "
             "conversation defending a residual nobody can forecast instead of "
             "presenting revenue they can evidence.</p>"
             '<p>See <a href="../power-cooling-and-ups-infrastructure-financing/">'
             "power, cooling and UPS financing</a> for the site side of the "
             "same project.</p>"),
        ],
        "faqs": [
            ("Can GPU hardware be used as collateral?",
             "Yes, more readily than most IT equipment, because the units are "
             "valuable and identifiable. What lenders discount is the residual: "
             "the market is shaped by supply allocation and new architecture "
             "releases, so a three-year value is hard to forecast."),
            ("What term should a GPU cluster be financed over?",
             "Commonly two to three years. Longer terms put payments beyond the "
             "point where the hardware is competitive for the workload, which "
             "is the same mismatch that catches operators financing ordinary "
             "servers over five years."),
            ("Does contracted workload really change the terms?",
             "More than anything else in the file. A cluster with a named "
             "counterparty and a committed term is underwritten on that "
             "revenue. Speculative capacity is financeable but on terms that "
             "reflect the risk being taken."),
            ("Why do lenders ask about power before credit?",
             "Because accelerated compute draws far more power and rejects far "
             "more heat per rack than conventional servers, and many sites "
             "simply cannot host it. Securing the site often takes longer than "
             "arranging the finance."),
            ("Should the power build be in the same facility?",
             "Usually not. Hardware and infrastructure have very different "
             "useful lives, and bundling them into one term gets the term wrong "
             "for at least one of them. Split the request and match each part "
             "to its own life."),
        ],
        "related": [
            ("/data-center-financing.html", "Data center financing"),
            ("../power-cooling-and-ups-infrastructure-financing/",
             "Power, cooling and UPS infrastructure financing"),
            ("../server-and-networking-equipment-financing/",
             "Server and networking equipment financing"),
            ("../colocation-buildout-financing/", "Colocation build-out financing"),
        ],
        "sources": [EIA, DOE, SLOOS],
    },
]
