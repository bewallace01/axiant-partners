# -*- coding: utf-8 -*-
"""Aircraft financing, articles 3-5."""
from cluster_aircraft import (FAA_CERT, FAA_HANDBOOKS, IRS_946, SBA_7A, CFPB,
                              FTC, SLOOS)

MORE = [
    {
        "slug": "used-aircraft-prebuy-inspection-financing",
        "crumb": "The Pre-Buy Inspection",
        "title": "Used Aircraft Pre-Buy Inspection and Financing | Axiant",
        "og_title": "The Pre-Buy Inspection: Why It Decides Aircraft Deals",
        "h1": "Used Aircraft Pre-Buy Inspection and Financing",
        "headline": "Used Aircraft Pre-Buy Inspection and Financing",
        "lede": "The inspection that decides whether the deal happens, who "
                "pays for it, and what to do when it finds something",
        "meta_desc": "A pre-buy inspection is where used aircraft deals are made "
                     "or lost. What it covers, who pays, how lenders treat the "
                     "findings, and how to structure the purchase around it.",
        "article_desc": "How the pre-buy inspection works and how to structure a "
                        "used aircraft purchase around it.",
        "keywords": "aircraft pre-buy inspection, used aircraft purchase, prebuy "
                    "findings, aircraft escrow",
        "quick_answer": "The pre-buy is an independent inspection commissioned "
                        "by the <strong>buyer</strong>, before closing, to "
                        "establish what is actually being bought. It is "
                        "<strong>paid up front and not refundable</strong> if "
                        "the deal collapses &mdash; which is precisely why it is "
                        "worth doing. Lenders treat the findings as part of "
                        "underwriting, and undisclosed damage discovered here "
                        "usually ends the transaction.",
        "sections": [
            ("What It Is and What It Is Not",
             "<p>A pre-buy inspection is not an annual inspection and it is not "
             "a formality. It is an independent assessment, arranged by the "
             "buyer, of the aircraft's actual condition and the completeness of "
             "its records.</p>"
             "<p>Two distinctions worth being clear on. It is not the seller's "
             "inspection &mdash; a report commissioned by the seller answers the "
             "seller's question. And it is not a maintenance event: passing a "
             "pre-buy does not mean the aircraft is airworthy for the next "
             "twelve months, only that it is what it was represented to be.</p>"
             "<p>The scope is negotiable, and it should be set deliberately "
             "rather than left to whoever is doing the work.</p>"),
            ("What It Typically Covers",
             "<ul>"
             "<li><strong>Records review</strong> &mdash; logbooks for airframe, "
             "engines and propellers, and whether they are complete</li>"
             "<li><strong>Airworthiness directive compliance</strong>, verified "
             "rather than assumed</li>"
             "<li><strong>Damage history</strong>, including repairs that were "
             "done properly and repairs that were not</li>"
             "<li><strong>Corrosion</strong>, which on older airframes is often "
             "the finding that matters most</li>"
             "<li><strong>Engine condition</strong> &mdash; borescope, "
             "compression, oil analysis, time against overhaul</li>"
             "<li><strong>Avionics and equipment</strong> against the equipment "
             "list</li>"
             "<li><strong>Life-limited components</strong> and time remaining "
             "on each</li>"
             "</ul>"
             "<p>Records completeness is the item buyers under-weight and "
             'lenders do not. As covered in <a href="/equipment-appraisal.html">'
             "equipment appraisal</a> generally, an undocumented history reduces "
             "value more reliably than most physical faults.</p>"),
            ("Who Pays, and What That Means",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Item</th><th>Usually borne by</th><th>Note</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label="Item">The inspection itself</td>'
             '<td data-label="By">Buyer</td>'
             '<td data-label="Note">Payable whether or not the deal proceeds</td></tr>'
             '<tr><td data-label="Item">Opening the aircraft for access</td>'
             '<td data-label="By">Negotiated</td>'
             '<td data-label="Note">Agree in the purchase agreement, not '
             "afterwards</td></tr>"
             '<tr><td data-label="Item">Correcting airworthiness items</td>'
             '<td data-label="By">Usually seller</td>'
             '<td data-label="Note">Often a defined category in the contract</td></tr>'
             '<tr><td data-label="Item">Discretionary squawks</td>'
             '<td data-label="By">Usually buyer</td>'
             '<td data-label="Note">Or renegotiated into the price</td></tr>'
             '<tr><td data-label="Item">Ferry to the inspection facility</td>'
             '<td data-label="By">Negotiated</td>'
             '<td data-label="Note">Not trivial on a long positioning flight</td></tr>'
             "</tbody></table></div>"
             "<p>The buyer paying is the point rather than a grievance. An "
             "inspection paid for by the person taking the risk is the one whose "
             "findings can be trusted.</p>"),
            ("How Lenders Use the Findings",
             "<p>A lender is not simply waiting for a pass. The report changes "
             "the underwriting in three ways.</p>"
             "<p><strong>Value.</strong> Findings that reduce what the aircraft "
             "is worth reduce the advance, and a buyer who has already agreed a "
             "price may need to bring more equity.</p>"
             "<p><strong>Condition of funding.</strong> Airworthiness items are "
             "commonly required to be rectified before release of funds, which "
             "affects the timetable.</p>"
             "<p><strong>Confidence.</strong> Undisclosed damage found at "
             "pre-buy usually ends the transaction, and not only because of the "
             "damage &mdash; it calls into question everything else the seller "
             "represented, which a lender notices as clearly as a buyer "
             "does.</p>"),
            ("Structuring the Purchase Around It",
             "<ul>"
             "<li><strong>Make the offer subject to a satisfactory pre-buy</strong>, "
             "with your definition of satisfactory written down.</li>"
             "<li><strong>Use escrow</strong> for the deposit, released on "
             "agreed conditions rather than on trust.</li>"
             "<li><strong>Choose the facility yourself</strong>, and choose one "
             "with experience of the type rather than the nearest shop.</li>"
             "<li><strong>Agree the squawk categories in advance</strong> "
             "&mdash; which findings the seller fixes, which reduce the price, "
             "which you accept.</li>"
             "<li><strong>Keep the lender informed as it happens.</strong> A "
             "finding shared early is a conversation; the same finding at "
             "closing is a delay.</li>"
             "<li><strong>Be willing to walk.</strong> The inspection fee is the "
             "price of finding out, and it is far cheaper than the aircraft it "
             "protects you from.</li>"
             "</ul>"),
        ],
        "faqs": [
            ("What is a pre-buy inspection?",
             "An independent inspection commissioned by the buyer before closing "
             "to establish an aircraft's actual condition and the completeness of "
             "its records. It is not the annual inspection and it is not the "
             "seller's report, both of which answer different questions."),
            ("Who pays for the pre-buy?",
             "The buyer, and it is payable whether or not the deal proceeds. "
             "That is the point rather than a grievance &mdash; an inspection "
             "paid for by the party carrying the risk is the one whose findings "
             "can be relied on."),
            ("What happens if the pre-buy finds problems?",
             "It depends what kind. Airworthiness items are commonly the "
             "seller's responsibility and may become a condition of funding; "
             "discretionary items are usually the buyer's or get renegotiated "
             "into the price. Agree those categories in the purchase agreement "
             "before the inspection, not after."),
            ("Can a pre-buy finding kill the financing?",
             "Yes. Findings that reduce value reduce the advance, which can "
             "leave a buyer needing more equity than planned. Undisclosed damage "
             "discovered at pre-buy usually ends the deal outright, because it "
             "undermines confidence in everything else that was represented."),
            ("Who should do the inspection?",
             "A facility with genuine experience of the type, chosen by you "
             "rather than the seller, and ideally not the shop that has been "
             "maintaining the aircraft. Independence and type knowledge matter "
             "more than proximity."),
        ],
        "related": [
            ("/aircraft-financing.html", "Aircraft financing"),
            ("../aircraft-loan-down-payment-and-terms/",
             "Aircraft loan down payment and terms"),
            ("/equipment-appraisal.html", "Equipment appraisal"),
            ("../aircraft-loan-vs-lease/", "Aircraft loan vs lease"),
        ],
        "sources": [FAA_CERT, FAA_HANDBOOKS, FTC],
    },
    {
        "slug": "aircraft-loan-vs-lease",
        "crumb": "Loan vs Lease",
        "title": "Aircraft Loan vs Lease: Which Fits | Axiant Partners",
        "og_title": "Aircraft Loan vs Lease: Which Structure Fits",
        "h1": "Aircraft Loan vs Lease",
        "headline": "Aircraft Loan vs Lease",
        "lede": "Owning the residual against paying to use it - and who "
                "carries the value risk",
        "meta_desc": "Aircraft loan or lease? A loan builds equity and leaves "
                     "you holding residual value risk; a lease lowers the "
                     "payment and shifts it. How to choose on hours and horizon.",
        "article_desc": "How aircraft loans and leases differ on cost, residual "
                        "risk and flexibility.",
        "keywords": "aircraft loan vs lease, aircraft operating lease, aircraft "
                    "finance lease, lease vs buy plane",
        "quick_answer": "A <strong>loan</strong> means you own the aircraft and "
                        "carry the residual value risk &mdash; the upside if it "
                        "holds value, the loss if it does not. A "
                        "<strong>lease</strong> lowers the payment and shifts "
                        "much of that risk to the lessor, at the cost of owning "
                        "nothing at the end. The deciding question is usually "
                        "<strong>how long you intend to keep it</strong>, not "
                        "the monthly figure.",
        "sections": [
            ("Residual Risk Is the Real Difference",
             "<p>Every comparison of these two eventually reduces to one "
             "question: who is exposed if the aircraft is worth less than "
             "expected in five years?</p>"
             "<p>Under a <strong>loan</strong>, you are. You own an asset whose "
             "value moves with the market for that type, and you take the "
             "outcome in both directions.</p>"
             "<p>Under an <strong>operating lease</strong>, the lessor has "
             "priced a residual and largely carries that risk. You pay for use "
             "over a defined term and hand it back.</p>"
             "<p>Everything else &mdash; payment size, flexibility, treatment "
             "&mdash; follows from that allocation.</p>"),
            ("How They Compare",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>Loan</th><th>Operating lease</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label=""><strong>Ownership</strong></td>'
             '<td data-label="Loan">Yours from day one</td>'
             '<td data-label="Lease">Lessor&rsquo;s</td></tr>'
             '<tr><td data-label=""><strong>Residual risk</strong></td>'
             '<td data-label="Loan">Yours</td><td data-label="Lease">Largely the '
             "lessor&rsquo;s</td></tr>"
             '<tr><td data-label=""><strong>Monthly cost</strong></td>'
             '<td data-label="Loan">Higher</td><td data-label="Lease">Lower</td></tr>'
             '<tr><td data-label=""><strong>Up-front cash</strong></td>'
             '<td data-label="Loan">Deposit</td>'
             '<td data-label="Lease">Usually less</td></tr>'
             '<tr><td data-label=""><strong>Hours flown</strong></td>'
             '<td data-label="Loan">Unrestricted</td>'
             '<td data-label="Lease">Often capped, with overage charges</td></tr>'
             '<tr><td data-label=""><strong>Modifications</strong></td>'
             '<td data-label="Loan">Your decision</td>'
             '<td data-label="Lease">Restricted</td></tr>'
             '<tr><td data-label=""><strong>End of term</strong></td>'
             '<td data-label="Loan">You own it</td>'
             '<td data-label="Lease">Return, or buy out if offered</td></tr>'
             "</tbody></table></div>"
             "<p>The hours cap is the row most often overlooked. A lease priced "
             "on assumed utilization becomes expensive quickly if you fly "
             "materially more than that.</p>"),
            ("Finance Lease Against Operating Lease",
             "<p>\"Lease\" covers two quite different things, and conflating "
             "them causes real confusion.</p>"
             "<p>A <strong>finance or capital lease</strong> is ownership in "
             "substance &mdash; typically a nominal buyout at the end, with you "
             "carrying the residual risk much as under a loan. It is a financing "
             "structure wearing a lease's clothes.</p>"
             "<p>An <strong>operating lease</strong> is genuinely paying for "
             "use. The lessor expects the aircraft back and has priced a "
             "residual accordingly.</p>"
             "<p>The accounting and tax treatment differs between them and "
             "depends on the specific terms. <strong>This is general "
             "information, not tax advice &mdash; the treatment turns on how the "
             'agreement is structured, so confirm with your CPA</strong>; '
             '<a href="https://www.irs.gov/publications/p946" rel="noopener '
             'nofollow" target="_blank">IRS Publication 946</a> is the starting '
             "point on depreciation where you own the asset.</p>"),
            ("Which Suits Which Owner",
             "<p><strong>A loan tends to fit when:</strong></p>"
             "<ul>"
             "<li>You intend to keep the aircraft for a long time</li>"
             "<li>Utilisation is high or unpredictable, so an hours cap would "
             "bite</li>"
             "<li>You want to modify or upgrade it</li>"
             "<li>You believe the type holds value and want that upside</li>"
             "</ul>"
             "<p><strong>A lease tends to fit when:</strong></p>"
             "<ul>"
             "<li>The horizon is defined and shorter</li>"
             "<li>Monthly cost and predictability matter more than ownership</li>"
             "<li>You want to avoid residual risk on a type you are unsure "
             "about</li>"
             "<li>You expect to move up or down in type within a few years</li>"
             "</ul>"),
            ("Comparing Them Honestly",
             "<p>The lease payment will be lower. That is not the comparison.</p>"
             "<ul>"
             "<li><strong>Total cost over your actual horizon</strong>, "
             "including the deposit under a loan and any return conditions under "
             "a lease.</li>"
             "<li><strong>What you hold at the end.</strong> Under a loan, an "
             "asset with value. Under an operating lease, nothing.</li>"
             "<li><strong>Return conditions</strong>, in detail. Hours, cycles, "
             "maintenance status and cosmetic condition on return can carry real "
             "cost, and they are specified in the agreement rather than "
             "negotiated at handback.</li>"
             "<li><strong>Early exit.</strong> Both are expensive to leave "
             "early; establish how expensive before signing either.</li>"
             "</ul>"),
        ],
        "faqs": [
            ("Is leasing an aircraft cheaper than buying?",
             "The monthly payment usually is, because you are paying for use "
             "rather than for the whole asset. Whether it is cheaper overall "
             "depends on how long you keep it and what the aircraft is worth at "
             "the end &mdash; under a loan you hold that value, under an "
             "operating lease you do not."),
            ("What is the difference between a finance lease and an operating lease?",
             "A finance or capital lease is ownership in substance, typically "
             "with a nominal buyout and the residual risk sitting with you. An "
             "operating lease is genuinely paying for use, with the lessor "
             "expecting the aircraft back and having priced a residual."),
            ("Do leases limit how much I can fly?",
             "Operating leases commonly cap hours, with charges for exceeding "
             "them, because the pricing assumes a utilization level. If your "
             "flying is high or unpredictable, that cap can turn a cheaper "
             "payment into a more expensive arrangement."),
            ("Can I modify a leased aircraft?",
             "Usually not without the lessor's consent, and often not at all "
             "where the change affects the residual. If avionics upgrades or "
             "interior changes matter to you, ownership is the structure that "
             "permits them."),
            ("How are the two treated for tax?",
             "Differently, and it depends on how the agreement is structured "
             "rather than on what it is called. <strong>This is general "
             "information, not tax advice &mdash; confirm the position with your "
             "CPA.</strong> IRS Publication 946 is the starting point on "
             "depreciation where you own the asset."),
        ],
        "related": [
            ("/aircraft-financing.html", "Aircraft financing"),
            ("../aircraft-loan-down-payment-and-terms/",
             "Aircraft loan down payment and terms"),
            ("../part-91-vs-part-135-financing/", "Part 91 vs Part 135 financing"),
            ("/equipment-financing.html", "Equipment financing"),
        ],
        "sources": [IRS_946, FAA_CERT, SLOOS],
    },
    {
        "slug": "helicopter-financing-for-operators",
        "crumb": "Helicopter Financing",
        "title": "Helicopter Financing for Operators | Axiant Partners",
        "og_title": "Helicopter Financing for Operators: What Differs",
        "h1": "Helicopter Financing for Operators",
        "headline": "Helicopter Financing for Operators",
        "lede": "Why rotorcraft are underwritten on the contract behind them "
                "as much as on the airframe",
        "meta_desc": "Helicopter financing is underwritten on the work as much "
                     "as the airframe: utility, EMS, tour and survey operations "
                     "differ, and component overhaul schedules cap the term.",
        "article_desc": "How helicopter financing differs from fixed-wing and "
                        "what operators should prepare.",
        "keywords": "helicopter financing, rotorcraft loan, EMS helicopter "
                    "finance, utility helicopter financing",
        "quick_answer": "Rotorcraft are financed more like revenue equipment "
                        "than like aircraft. Lenders look hard at "
                        "<strong>the contract behind the machine</strong> "
                        "&mdash; utility, EMS, tour or survey work &mdash; "
                        "because utilization and component overhaul costs are "
                        "high and predictable. The <strong>component overhaul "
                        "schedule</strong> usually caps the term more tightly "
                        "than anything on the buyer's side.",
        "sections": [
            ("Why Rotorcraft Are Underwritten Differently",
             "<p>A privately-flown fixed-wing aircraft is largely a lifestyle "
             "asset. A helicopter is almost always a working machine, and "
             "lenders underwrite it accordingly.</p>"
             "<p>That changes the emphasis. The question is less \"can this "
             "buyer afford the payment\" and more \"does this machine have work, "
             "and does that work cover its running costs as well as the "
             "loan\". It is closer to how equipment finance treats a piece of "
             "revenue-generating plant.</p>"
             "<p>The consequence for an operator is that contracts belong in the "
             "application at the start. An operator with a documented utility or "
             "survey contract is presenting a very different file from one "
             "buying speculatively.</p>"),
            ("Operating Type Changes the File",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Work</th><th>What lenders focus on</th></tr></thead><tbody>"
             '<tr><td data-label="Work">Utility and lift</td>'
             '<td data-label="Focus">Contract duration, seasonality, high '
             "component wear</td></tr>"
             '<tr><td data-label="Work">EMS</td>'
             '<td data-label="Focus">Long contracts and stable revenue; heavy '
             "certification burden</td></tr>"
             '<tr><td data-label="Work">Tour and sightseeing</td>'
             '<td data-label="Focus">Strong seasonality; passenger operation '
             "requirements</td></tr>"
             '<tr><td data-label="Work">Survey and aerial work</td>'
             '<td data-label="Focus">Contract pipeline and specialist equipment '
             "fitted</td></tr>"
             '<tr><td data-label="Work">Training</td>'
             '<td data-label="Focus">Very high utilization and accelerated '
             "component consumption</td></tr>"
             "</tbody></table></div>"
             "<p>High-utilization work is not a negative in itself &mdash; it "
             "generates the revenue. It does mean the overhaul cost arrives "
             "sooner, and the structure has to anticipate that rather than be "
             "surprised by it.</p>"),
            ("Component Overhaul Is the Structural Constraint",
             "<p>This is the single biggest difference from fixed-wing "
             "financing and the one operators most need to plan for.</p>"
             "<p>Rotorcraft carry life-limited components with mandated overhaul "
             "or replacement intervals, and those events are expensive, dated "
             "and unavoidable. A lender will not comfortably amortise past a "
             "major component event without knowing how it will be paid for.</p>"
             "<p>Two consequences follow. The <strong>term is often capped</strong> "
             "by the next major event rather than by the airframe's overall "
             "life. And lenders look favorably on operators who "
             "<strong>accrue reserves</strong> against those costs, because it "
             "converts a cliff into a run rate.</p>"
             "<p>An operator who can show a reserve accrual per flight hour is "
             "presenting a materially stronger file than one who intends to "
             "\"deal with it when it comes\".</p>"),
            ("Insurance and Crew",
             "<p>Insurance is a larger factor here than in most categories, and "
             "it is a closing condition rather than a background cost.</p>"
             "<ul>"
             "<li><strong>Pilot hours in type</strong> matter to underwriters "
             "and can be decisive on cover for a specific machine.</li>"
             "<li><strong>The mission</strong> is priced &mdash; external load, "
             "EMS and tour operations carry different exposures.</li>"
             "<li><strong>Crew depth.</strong> A single-pilot operation "
             "concentrates risk in one person, which affects both insurance and "
             "the lender's view of revenue continuity.</li>"
             "</ul>"
             "<p>Get quotes at the required limits, for the actual crew, before "
             "committing. A machine nobody will insure at a workable price is a "
             "machine that cannot be financed.</p>"),
            ("Preparing a Rotorcraft Application",
             "<ul>"
             "<li><strong>Contracts first.</strong> Signed work, duration, and "
             "who the counterparty is.</li>"
             "<li><strong>Component status</strong> for every life-limited item, "
             "with time remaining.</li>"
             "<li><strong>Utilisation history</strong> on your existing fleet, "
             "if you have one &mdash; hours flown and revenue per machine.</li>"
             "<li><strong>Reserve policy</strong>, and evidence you actually "
             "accrue it.</li>"
             "<li><strong>Insurance quote</strong> at the limits required, for "
             "the crew who will fly it.</li>"
             "<li><strong>Maintenance arrangements</strong> &mdash; in-house or "
             "contracted, and with whom.</li>"
             "</ul>"
             "<p>An operator with those six ready is a straightforward file. One "
             "without them is asking a lender to take a view on an expensive "
             "machine with unknown running costs.</p>"),
        ],
        "faqs": [
            ("How is helicopter financing different from fixed-wing?",
             "Rotorcraft are underwritten more like revenue equipment. Lenders "
             "look at the contract behind the machine, because utilization is "
             "high and component overhaul costs are large, predictable and "
             "unavoidable."),
            ("What caps the term on a helicopter loan?",
             "The component overhaul schedule, usually. Life-limited components "
             "have mandated intervals and the associated costs are dated and "
             "expensive, so lenders are reluctant to amortise past a major event "
             "without knowing how it will be funded."),
            ("Do I need contracts in place to finance a helicopter?",
             "Not always, but it changes the file substantially. An operator "
             "with documented utility, EMS or survey work is financing a machine "
             "with revenue attached; one buying speculatively is asking the "
             "lender to take a view on both the asset and the demand."),
            ("Why do lenders ask about overhaul reserves?",
             "Because accruing per flight hour converts a large future cliff "
             "into a predictable run rate. An operator who can evidence a "
             "reserve policy presents far better than one intending to deal with "
             "the cost when it arrives."),
            ("How much does insurance matter?",
             "A great deal, and it is a closing condition. Pilot hours in type, "
             "the mission flown and crew depth all affect whether cover is "
             "available and at what price. A machine nobody will insure "
             "affordably cannot be financed."),
        ],
        "related": [
            ("/aircraft-financing.html", "Aircraft financing"),
            ("../part-91-vs-part-135-financing/", "Part 91 vs Part 135 financing"),
            ("../aircraft-loan-down-payment-and-terms/",
             "Aircraft loan down payment and terms"),
            ("/equipment-financing.html", "Equipment financing"),
        ],
        "sources": [FAA_HANDBOOKS, FAA_CERT, SBA_7A],
    },
]
