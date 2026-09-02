# -*- coding: utf-8 -*-
"""Commercial marine financing, articles 2-5."""
from cluster_marine import (USCG_NVDC, NOAA, SBA_7A, CFPB, FTC, SBCS, SLOOS)

MORE = [
    {
        "slug": "marine-survey-what-lenders-require",
        "crumb": "The Marine Survey",
        "title": "Marine Survey: What Lenders Require | Axiant Partners",
        "og_title": "The Marine Survey: What Lenders Require and Why",
        "h1": "Marine Survey: What Lenders Require",
        "headline": "Marine Survey: What Lenders Require",
        "lede": "The inspection that sets the advance and where most vessel "
                "deals change shape",
        "meta_desc": "A condition and valuation survey from an accredited "
                     "surveyor decides the advance on a vessel loan. What it "
                     "covers, who pays, and what happens when it finds "
                     "something.",
        "article_desc": "What a marine survey covers and how lenders use the "
                        "findings.",
        "keywords": "marine survey lender, vessel condition survey, accredited "
                    "marine surveyor, boat survey financing",
        "quick_answer": "Lenders require a <strong>condition and valuation "
                        "survey</strong> from an accredited surveyor, "
                        "commissioned by the buyer. It sets the advance and it "
                        "is where most deals change shape &mdash; corrosion, "
                        "structural repairs and machinery condition surface "
                        "here. Book it <strong>early</strong>: a finding in week "
                        "one is a renegotiation, the same finding at closing is "
                        "a collapse.",
        "sections": [
            ("The Marine Equivalent of an Appraisal",
             "<p>A survey does two jobs at once, and it is worth separating "
             "them.</p>"
             "<p>The <strong>condition</strong> half assesses what state the "
             "vessel is actually in &mdash; hull, structure, machinery, systems "
             "and safety equipment. The <strong>valuation</strong> half puts a "
             "figure on it, on a stated basis, which is what the lender "
             "advances against.</p>"
             "<p>As with "
             '<a href="/equipment-appraisal/articles/orderly-vs-forced-liquidation-value/">'
             "equipment valuation generally</a>, the basis matters. A market "
             "value assumes an unhurried sale; a lender sizing recovery may work "
             "from something more conservative, and the two are not "
             "interchangeable.</p>"),
            ("What the Survey Covers",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Area</th><th>What is examined</th></tr></thead><tbody>"
             '<tr><td data-label="Area">Hull and structure</td>'
             '<td data-label="Examined">Plating or laminate condition, framing, '
             "previous repairs, corrosion or osmosis</td></tr>"
             '<tr><td data-label="Area">Machinery</td>'
             '<td data-label="Examined">Main engines, gearboxes, shafts, '
             "steering, generators, hours and service history</td></tr>"
             '<tr><td data-label="Area">Systems</td>'
             '<td data-label="Examined">Electrical, fuel, bilge, fire '
             "suppression</td></tr>"
             '<tr><td data-label="Area">Safety equipment</td>'
             '<td data-label="Examined">Present, in date, and appropriate to the '
             "trade</td></tr>"
             '<tr><td data-label="Area">Out-of-water inspection</td>'
             '<td data-label="Examined">Below the waterline &mdash; hull, '
             "running gear, anodes, through-hulls</td></tr>"
             '<tr><td data-label="Area">Valuation</td>'
             '<td data-label="Examined">A figure, on a stated basis, with '
             "comparables</td></tr>"
             "</tbody></table></div>"
             "<p>The out-of-water portion is the one buyers try to save on and "
             "should not. Most of what changes a valuation is below the "
             "waterline, and a survey that never lifted the vessel has assumed "
             "rather than seen.</p>"),
            ("Who Commissions It, and Why That Matters",
             "<p>The buyer, and for the same reason a buyer commissions an "
             "aircraft pre-buy: a report paid for by the party carrying the risk "
             "is the one whose findings can be relied on.</p>"
             "<p>A survey supplied by the seller answers the seller's question. "
             "Some lenders will not accept one at all; others will only accept "
             "it if the surveyor re-addresses the report to them, which makes "
             "the lender the client.</p>"
             "<p>Two practical points. Choose a surveyor with experience of the "
             "vessel type and trade &mdash; a yacht surveyor and a commercial "
             "workboat surveyor are not interchangeable. And check whether the "
             "lender maintains an approved list before instructing, because "
             "paying for a survey they will not accept is an expensive way to "
             "learn that.</p>"),
            ("When the Survey Finds Something",
             "<p>It usually does, and that is not a failure of the process. The "
             "question is what category the finding falls into.</p>"
             "<ul>"
             "<li><strong>Structural or safety-critical.</strong> Generally has "
             "to be rectified before funding, and may become a condition of the "
             "loan.</li>"
             "<li><strong>Value-affecting but not urgent.</strong> Reduces the "
             "valuation, which reduces the advance &mdash; usually renegotiated "
             "into the price.</li>"
             "<li><strong>Deferred maintenance.</strong> Ordinary on a working "
             "vessel; matters cumulatively rather than individually.</li>"
             "<li><strong>Undisclosed major repair.</strong> The one that ends "
             "deals, less because of the repair than because of what it implies "
             "about everything else represented.</li>"
             "</ul>"
             "<p>Agree in the purchase agreement which category the seller "
             "carries, before the survey rather than after it.</p>"),
            ("Making the Survey Work for You",
             "<ul>"
             "<li><strong>Book it early</strong>, and build the timetable around "
             "it rather than fitting it in near closing.</li>"
             "<li><strong>Budget the haul-out</strong> as part of the cost.</li>"
             "<li><strong>Make the offer conditional</strong> on a satisfactory "
             "survey, with your definition of satisfactory written down.</li>"
             "<li><strong>Attend if you can.</strong> An hour with the surveyor "
             "on the vessel teaches you more than the report will.</li>"
             "<li><strong>Share findings with the lender as they emerge</strong> "
             "rather than presenting a completed report with surprises in "
             "it.</li>"
             "</ul>"
             "<p>A survey is not a hurdle to clear and forget. Its condition "
             "notes become your maintenance plan for the first two years of "
             "the loan, and the valuation sets the number the lender will "
             "carry the vessel at if anything goes wrong. Read it as "
             "operating information rather than paperwork, and it earns back "
             "its cost.</p>"),
        ],
        "faqs": [
            ("What kind of survey do marine lenders require?",
             "A condition and valuation survey from an accredited surveyor, "
             "covering hull and structure, machinery, systems and safety "
             "equipment, with an out-of-water inspection and a valuation on a "
             "stated basis."),
            ("Who pays for the marine survey?",
             "The buyer, and it is payable whether or not the deal completes. "
             "That independence is the point &mdash; a survey commissioned by "
             "the seller answers the seller's question, and some lenders will "
             "not accept one."),
            ("Does the vessel need to come out of the water?",
             "For a lender-grade survey, generally yes. Most of what changes a "
             "valuation is below the waterline, and a survey conducted afloat has "
             "assumed rather than examined the running gear, through-hulls and "
             "hull condition."),
            ("What happens if the survey finds problems?",
             "It depends on category. Structural and safety-critical items "
             "usually have to be rectified before funding; value-affecting items "
             "reduce the advance and are typically renegotiated into the price. "
             "Undisclosed major repairs are the findings that end deals."),
            ("Can I use a survey the seller already has?",
             "Sometimes, but do not rely on it. Many lenders will not accept a "
             "seller-commissioned survey, and those that do usually require the "
             "surveyor to re-address the report to them. Check the lender's "
             "position before paying for anything."),
        ],
        "related": [
            ("/commercial-marine-financing.html", "Commercial marine financing"),
            ("../commercial-vessel-loan-requirements/",
             "Commercial vessel loan requirements"),
            ("/equipment-appraisal.html", "Equipment appraisal"),
            ("../workboat-and-tug-financing/", "Workboat and tug financing"),
        ],
        "sources": [USCG_NVDC, FTC, SLOOS],
    },
    {
        "slug": "charter-boat-business-financing",
        "crumb": "Charter Boat Financing",
        "title": "Charter Boat Business Financing | Axiant Partners",
        "og_title": "Charter Boat Business Financing: What Lenders Look At",
        "h1": "Charter Boat Business Financing",
        "headline": "Charter Boat Business Financing",
        "lede": "Passenger certification, seasonality and bookings - what "
                "carries a charter file",
        "meta_desc": "Charter boat financing turns on passenger certification, "
                     "a documented booking history and how the operator handles "
                     "a season that pays for the whole year.",
        "article_desc": "How charter and tour boat operations are financed and "
                        "what strengthens the file.",
        "keywords": "charter boat financing, tour boat loan, passenger vessel "
                    "financing, dive charter business loan",
        "quick_answer": "Two things carry a charter file: "
                        "<strong>passenger certification</strong>, which is slow "
                        "and expensive to obtain and therefore adds real value "
                        "to a certificated vessel; and a "
                        "<strong>documented booking history</strong> across a "
                        "full year, because the season pays for the whole "
                        "twelve months and lenders want to see you manage that "
                        "deliberately.",
        "sections": [
            ("Certification Is Part of the Asset",
             "<p>A certificated passenger vessel is worth more than an identical "
             "hull without certification, and the gap can be substantial.</p>"
             "<p>The reason is straightforward: certification takes time and "
             "money to obtain, and a buyer acquiring a certificated vessel is "
             "buying the ability to trade from day one rather than a project. "
             "Lenders understand this and it works in your favor on a "
             "purchase.</p>"
             "<p>What follows practically is that documentation of the "
             "certification belongs in the application, alongside the survey. It "
             "is part of what is being valued, and a lender cannot infer it from "
             "the hull.</p>"),
            ("Seasonality, Read Properly",
             "<p>Charter is among the most openly seasonal trades there is. "
             "Lenders who work in the sector expect that and do not react to a "
             "quiet month &mdash; what they look for is evidence the operator "
             "runs the year deliberately.</p>"
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>What lenders want to see</th><th>Why</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Want">A full trading year</td>'
             '<td data-label="Why">The shape is the point; strong months alone '
             "look concealing</td></tr>"
             '<tr><td data-label="Want">Cash carried through the off-season</td>'
             '<td data-label="Why">The clearest single sign of a well-run '
             "seasonal business</td></tr>"
             '<tr><td data-label="Want">Advance bookings</td>'
             '<td data-label="Why">Contracted revenue against projected '
             "revenue</td></tr>"
             '<tr><td data-label="Want">An off-season plan</td>'
             '<td data-label="Why">Maintenance, a second trade, or a budgeted '
             "shutdown</td></tr>"
             '<tr><td data-label="Want">Seasonal payment structure</td>'
             '<td data-label="Why">Available from marine lenders if asked for at '
             "term-sheet stage</td></tr>"
             "</tbody></table></div>"
             "<p>That last row is worth acting on. Skip or reduced payments "
             "through the off-season are a normal arrangement in marine lending "
             "and much harder to introduce once documents are drawn.</p>"),
            ("What the Trade Changes",
             "<p>Charter covers several quite different operations, and the "
             "differences matter to an underwriter:</p>"
             "<ul>"
             "<li><strong>Sightseeing and tour.</strong> High passenger numbers, "
             "shorter trips, heavily seasonal, close certification "
             "scrutiny.</li>"
             "<li><strong>Fishing charter.</strong> Smaller parties, often "
             "owner-operated, revenue tied to the fishery and the weather.</li>"
             "<li><strong>Dive charter.</strong> Specialist equipment and "
             "crewing requirements alongside the vessel.</li>"
             "<li><strong>Private and corporate hire.</strong> Fewer, larger "
             "bookings; concentration risk if a handful of clients dominate.</li>"
             "</ul>"
             "<p>An owner-operated fishing charter is a different credit from a "
             "tour operation running several vessels with employed crew, even at "
             "similar revenue. Say which you are early.</p>"),
            ("Insurance for Carrying Passengers",
             "<p>Passenger operation raises the insurance question sharply, and "
             "it is a closing condition rather than a running cost to sort "
             "later.</p>"
             "<p>Cover has to be written for commercial passenger carriage, at "
             "limits the lender specifies, and it is materially different from "
             "recreational or even from commercial cover for a vessel carrying "
             "no passengers. Crew experience and the waters worked both feed "
             "into it.</p>"
             "<p>Get the quote on the real operation &mdash; passenger numbers, "
             "trip type, waters, night operation &mdash; before committing to a "
             "purchase. A vessel nobody will insure affordably for the trade you "
             "intend is a vessel that cannot be financed for it.</p>"),
            ("Strengthening a Charter Application",
             "<ul>"
             "<li><strong>Bring a full year of accounts</strong>, and the "
             "booking system data behind them.</li>"
             "<li><strong>Document certification</strong> and any inspection "
             "history.</li>"
             "<li><strong>Show advance bookings</strong> for the coming season "
             "&mdash; contracted revenue counts for more than projections.</li>"
             "<li><strong>Explain the off-season</strong> and how it is "
             "funded.</li>"
             "<li><strong>Ask about seasonal payments</strong> at term-sheet "
             "stage.</li>"
             "<li><strong>Have commercial passenger insurance quoted</strong> on "
             "the actual operation.</li>"
             "</ul>"
             "<p>The through-line is that a charter lender is underwriting an "
             "operating business that happens to own a boat, not a boat that "
             "happens to earn. Files that lead with the vessel and treat the "
             "trade as background read weaker than files that do it the other "
             "way round, even when the vessel is the better asset.</p>"),
        ],
        "faqs": [
            ("Does passenger certification affect what I can borrow?",
             "Yes, favorably. A certificated vessel is worth more than an "
             "identical uncertificated hull because certification is slow and "
             "expensive to obtain, and a buyer is acquiring the ability to trade "
             "immediately rather than a project."),
            ("How do lenders handle charter seasonality?",
             "They expect it and read the year as a whole rather than reacting "
             "to quiet months. What they look for is deliberate management "
             "&mdash; cash carried through the off-season, advance bookings, and "
             "a plan for the quiet period."),
            ("Can I get seasonal payments on a charter vessel loan?",
             "Often, from lenders who work in the sector &mdash; reduced or "
             "skipped payments through the off-season so the schedule follows the "
             "revenue. Ask at term-sheet stage; it is much harder to introduce "
             "once documents are drawn."),
            ("What should I supply for a charter application?",
             "A full year of accounts with the booking data behind it, "
             "certification and inspection history, advance bookings for the "
             "coming season, an explanation of how the off-season is funded, and "
             "a commercial passenger insurance quote on the real operation."),
            ("Is an owner-operated charter treated differently?",
             "Yes. An owner-operated fishing charter concentrates the operation "
             "in one person, which affects both insurance and a lender's view of "
             "revenue continuity, and is a different credit from a multi-vessel "
             "tour operation with employed crew at similar revenue."),
        ],
        "related": [
            ("/commercial-marine-financing.html", "Commercial marine financing"),
            ("../commercial-vessel-loan-requirements/",
             "Commercial vessel loan requirements"),
            ("../marine-survey-what-lenders-require/",
             "What a marine survey covers"),
            ("../commercial-fishing-vessel-financing/",
             "Commercial fishing vessel financing"),
        ],
        "sources": [USCG_NVDC, SBCS, CFPB],
    },
]
