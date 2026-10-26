# -*- coding: utf-8 -*-
"""Commercial truck title loans, articles 9-11: one spoke per truck class
(dump, box, tow). Imported by cluster_truck_title.

Each spoke has to stand on its own facts, not a find-and-replace of the semi
article: what that class is worth, where it sits in the advance range, who
lends on it, what the appraiser checks on that body, and when a title loan is
the wrong tool for that kind of operator.

Price ranges are the ones the site already publishes on the matching
equipment pages (equipment/dump-trucks, equipment/box-trucks, the tow truck
and wrecker guide). The advance range (roughly 50-80% of forced liquidation
value) is the one the equipment refinancing and heavy-equipment equity pages
already use. Worked examples are labelled illustrative. No named-lender rates,
no funded totals, no testimonials.
"""
from cluster_truck_title import FMCSA, IRS_946, FTC

OCC_ABL = ("https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/files/asset-based-lending/index-asset-based-lending.html",
           "OCC Comptroller's Handbook: Asset-Based Lending",
           "The federal bank examiners' handbook on collateral lending, including "
           "orderly and forced liquidation value - the bases lenders advance "
           "against instead of market value.")
FHWA_BRIDGE = ("https://ops.fhwa.dot.gov/freight/sw/brdg_frm_wghts/bridge_formula_weights.htm",
               "FHWA: Bridge Formula Weights",
               "The federal axle-spacing and weight rule that decides how much a dump "
               "truck can legally haul, and so how useful it is to the next owner.")
AFDC_CLASSES = ("https://afdc.energy.gov/data/10380",
                "U.S. Department of Energy: Vehicle Weight Classes and Categories",
                "The Class 1-8 gross vehicle weight bands used to describe box trucks, "
                "from Class 3 cutaways to Class 7 straight trucks.")
ECFR_CDL = ("https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-383/subpart-F/section-383.91",
            "49 CFR 383.91: Commercial Motor Vehicle Groups",
            "The federal rule that puts a single vehicle over 26,000 pounds GVWR in "
            "the Class B CDL group - the line that splits the box truck resale "
            "market in two.")

MORE = [
    {
        "slug": "dump-truck-title-loan",
        "crumb": "Dump Truck Title Loans",
        "title": "Dump Truck Title Loans: Value, LTV, Lenders | Axiant",
        "og_title": "Can You Get a Title Loan on a Dump Truck?",
        "h1": "Dump Truck Title Loans",
        "headline": "Dump Truck Title Loans: What the Truck Supports and Who Lends",
        "lede": "Borrowing against a dump truck you own - what single, tandem and "
                "tri-axle units are worth to a lender, and where the body and the "
                "season change the answer",
        "meta_desc": "A dump truck title loan advances against liquidation value, "
                     "not price. What tandem and tri-axle units support, who lends "
                     "on them, what the appraiser checks, and when it is the wrong tool.",
        "article_desc": "How lenders value and lend against a dump truck that is "
                        "already owned, by axle configuration and body.",
        "keywords": "dump truck title loan, borrow against dump truck, dump truck "
                    "equity loan, cash out dump truck, tandem dump truck loan",
        "quick_answer": "Yes, as a business-purpose loan secured by the title. "
                        "Axiant Partners, a business-loan broker in Boca Raton, sees "
                        "lenders advance roughly <strong>50-80% of forced liquidation "
                        "value</strong>, less anything still owed. New dump trucks run "
                        "about <strong>$70,000 for a single-axle to $280,000+ for a "
                        "tri-axle</strong>, but the lender values the used truck as it "
                        "sits: body wear, axle setup and the hoist move the number more "
                        "than the chassis badge.",
        "sections": [
            ("What a Dump Truck Is Worth to a Lender",
             "<p>Start from the configuration, because the buyer pool for each one is "
             "different and a lender is pricing the buyer pool. New prices, as published "
             "on our <a href=\"/equipment/dump-trucks/\">dump truck financing</a> page:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Configuration</th><th>Typical new price</th>"
             "<th>Where it tends to sit in the advance range</th></tr></thead><tbody>"
             "<tr><td data-label=\"Configuration\">Single-axle</td>"
             "<td data-label=\"New price\">$70,000-$120,000</td>"
             "<td data-label=\"Advance\">Middle: easy to sell, but a low dollar base</td></tr>"
             "<tr><td data-label=\"Configuration\">Tandem-axle</td>"
             "<td data-label=\"New price\">$120,000-$180,000</td>"
             "<td data-label=\"Advance\">Upper: the most common spec, the deepest resale market</td></tr>"
             "<tr><td data-label=\"Configuration\">Tri-axle / vocational</td>"
             "<td data-label=\"New price\">$180,000-$280,000+</td>"
             "<td data-label=\"Advance\">Middle to upper, if axle spacing fits local weight rules</td></tr>"
             "<tr><td data-label=\"Configuration\">Specialty bodies</td>"
             "<td data-label=\"New price\">Varies widely</td>"
             "<td data-label=\"Advance\">Lower: side dumps and super dumps sell to fewer buyers</td></tr>"
             "</tbody></table></div>"
             "<p>A used unit is valued as it sits, not against the new price. A "
             "five-year-old tandem is a different number again, and the lender's number "
             "is the <strong>forced liquidation value</strong> - what it would fetch "
             "sold quickly - not what a dealer would list it at.</p>"),
            ("Loan-to-Value: How the Advance Is Sized",
             "<p>Lenders that cash out equity in owned equipment commonly advance "
             "<strong>roughly 50-80% of forced liquidation value</strong>, then take off "
             "any payoff to an existing lienholder. That range is conventional across "
             "lenders, not anyone's quote, and dump trucks move within it for reasons "
             "specific to the trade:</p>"
             "<ul>"
             "<li><strong>Axle spacing and legal weight.</strong> What a truck can "
             "legally haul depends on axle count and spacing under the federal bridge "
             "formula and state rules. A truck that carries a full load where the next "
             "owner works is worth more than one that has to run light.</li>"
             "<li><strong>Body material and wear.</strong> A steel body that has hauled "
             "rock for years has a thinned floor and worn liner. Aluminum bodies weigh "
             "less and carry more payload, but cost more to repair.</li>"
             "<li><strong>Seasonality.</strong> Construction slows in winter across "
             "much of the country, and the auction market for dump trucks moves with "
             "it. A lender pricing a quick sale prices that in.</li>"
             "</ul>"
             "<p>For the general arithmetic, see "
             "<a href=\"../how-much-can-you-borrow-against-a-semi/\">how much a truck "
             "supports</a>; the dump-specific part is the body and the axles.</p>"),
            ("A Worked Example (Illustrative)",
             "<p>Take a used tandem whose forced liquidation value an appraiser puts at "
             "$90,000, with $20,000 still owed on it. The figures are illustrative, not "
             "a quote:</p>"
             "<ul>"
             "<li>50-80% of $90,000 is <strong>$45,000-$72,000</strong></li>"
             "<li>Less the $20,000 payoff leaves <strong>$25,000-$52,000</strong></li>"
             "<li>Less title work, lien filing and any inspection</li>"
             "</ul>"
             "<p>Where the truck lands in that band is decided by the inspection below. "
             "A clean body, a sound hoist and service records push it up; a worn floor, "
             "frame cracks and no paperwork pull it down.</p>"),
            ("Who Lends on a Dump Truck",
             "<ul>"
             "<li><strong>Equipment and vocational-truck finance companies</strong> "
             "that refinance owned units and pay out the equity. The most common home "
             "for a business-purpose dump truck title loan.</li>"
             "<li><strong>Heavy-equipment lenders</strong> that will take dump trucks "
             "alongside loaders and excavators in one package. The trucks carry a title "
             "lien; the yellow iron, which usually has no title, takes a UCC-1 filing. "
             "See <a href=\"/heavy-equipment-equity-loan.html\">borrowing against "
             "construction equipment you own</a>.</li>"
             "<li><strong>Banks and credit unions</strong>, usually for an existing "
             "customer with financial statements, and usually slower.</li>"
             "<li><strong>Consumer car-title lenders.</strong> These are what a search "
             "often turns up, but they are built for personal vehicles under state "
             "consumer rules, with loan caps sized to cars. Many will not take a "
             "commercial truck or a business borrower at all.</li>"
             "</ul>"),
            ("What the Appraiser Checks on a Dump Truck",
             "<p>The chassis checks are the same as any heavy truck - see "
             "<a href=\"../what-a-truck-appraiser-looks-for/\">what a truck appraiser "
             "looks for</a>. The dump-specific ones are where the value is won or "
             "lost:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Area</th><th>What they look at</th></tr></thead><tbody>"
             "<tr><td data-label=\"Area\">Body and floor</td>"
             "<td data-label=\"Looks at\">Floor thickness, liner, patched holes, tailgate "
             "hinges and latch</td></tr>"
             "<tr><td data-label=\"Area\">Hoist</td>"
             "<td data-label=\"Looks at\">Cylinder leaks, raise and lower under load, "
             "pivot wear</td></tr>"
             "<tr><td data-label=\"Area\">PTO and hydraulics</td>"
             "<td data-label=\"Looks at\">Pump, lines, valves, PTO hours where they are "
             "recorded</td></tr>"
             "<tr><td data-label=\"Area\">Frame</td>"
             "<td data-label=\"Looks at\">Cracks and repairs behind the cab and at the "
             "hoist mounts, from years of shock loads</td></tr>"
             "<tr><td data-label=\"Area\">Axles and suspension</td>"
             "<td data-label=\"Looks at\">Configuration, lift or pusher axles, spacing "
             "against local weight rules</td></tr>"
             "<tr><td data-label=\"Area\">Paperwork</td>"
             "<td data-label=\"Looks at\">Clean title, registered weight, service "
             "records, any body replacement documented</td></tr>"
             "</tbody></table></div>"
             "<p>A replaced body with an invoice is worth more than the same body "
             "without one. Keep the paper.</p>"),
            ("When a Title Loan Is the Wrong Tool",
             "<ul>"
             "<li><strong>You are buying another truck.</strong> An equipment loan on "
             "the new unit is usually cheaper and longer than cashing out the old one. "
             "Use the title loan for the down payment only if that is the gap.</li>"
             "<li><strong>The problem is a general contractor paying slowly.</strong> "
             "That is a receivables gap, and "
             "<a href=\"/invoice-factoring.html\">invoice factoring</a> or a line of "
             "credit matches it better than a lien on the truck.</li>"
             "<li><strong>It is January and the work is not there.</strong> Borrowing "
             "against the truck to cover a slow season puts the asset at risk exactly "
             "when it is earning least. Size any loan to the spring work you can see.</li>"
             "<li><strong>There is little equity.</strong> A truck most of the way "
             "through its original loan has little to lend against, whatever it is "
             "worth.</li>"
             "</ul>"
             "<p>If none of those applies, "
             "<a href=\"/match.html\">send us the VIN, mileage and payoff</a> and we "
             "will tell you plainly what the truck supports.</p>"),
        ],
        "faqs": [
            ("Can I get a title loan on my dump truck?",
             "Yes, as a business-purpose loan secured by the truck's title. Lenders "
             "advance against the truck's forced liquidation value, commonly in the "
             "range of 50-80% of it, less anything still owed, and you keep the truck "
             "working."),
            ("How much is my dump truck worth to a lender?",
             "Less than its listing price. New dump trucks run roughly $70,000 for a "
             "single-axle to $280,000 or more for a tri-axle, but a lender values the "
             "used truck at what it would fetch sold quickly, then advances a "
             "percentage of that."),
            ("Does the dump body affect the loan amount?",
             "Considerably. The appraiser checks floor thickness, liner, the hoist "
             "cylinder and frame cracks at the hoist mounts. A worn body or a leaking "
             "hoist lowers the valuation more than mileage on the chassis does."),
            ("Will a car title lender take a dump truck?",
             "Often not. Consumer title lenders are built for personal vehicles under "
             "state consumer rules, with caps sized to cars. A dump truck title loan "
             "usually goes through an equipment or vocational-truck lender."),
            ("Can I borrow against dump trucks and excavators together?",
             "Yes, with lenders that package construction equipment. The trucks carry "
             "a title lien and the machines, which usually have no title, take a UCC-1 "
             "filing, but both can secure one facility."),
        ],
        "related": [
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("/equipment/dump-trucks/", "Dump truck financing"),
            ("/heavy-equipment-equity-loan.html", "Heavy equipment equity loans"),
            ("../what-a-truck-appraiser-looks-for/", "What a truck appraiser looks for"),
        ],
        "sources": [OCC_ABL, FHWA_BRIDGE, IRS_946, FTC],
    },
    {
        "slug": "box-truck-title-loan",
        "crumb": "Box Truck Title Loans",
        "title": "Box Truck Title Loans: Value, LTV, Lenders | Axiant",
        "og_title": "Can You Get a Title Loan on a Box Truck?",
        "h1": "Box Truck Title Loans",
        "headline": "Box Truck Title Loans: What the Truck Supports and Who Lends",
        "lede": "Borrowing against a box truck you own - why the dollar amount, not "
                "the percentage, is usually the limit, and where the 26,000-pound "
                "line matters",
        "meta_desc": "A box truck title loan is limited by the truck's dollar value "
                     "more than the advance rate. What Class 3-7 units support, who "
                     "lends, what the appraiser checks, and when to use something else.",
        "article_desc": "How lenders value and lend against an owned box truck, "
                        "by weight class and body.",
        "keywords": "box truck title loan, borrow against box truck, box truck "
                    "equity loan, straight truck title loan, cash out box truck",
        "quick_answer": "Yes, as a business-purpose loan against the title. Axiant "
                        "Partners, a business-loan broker in Boca Raton, sees lenders "
                        "advance roughly <strong>50-80% of forced liquidation "
                        "value</strong>, less any payoff. New box trucks run about "
                        "<strong>$35,000 to $100,000+</strong>, so a used one often "
                        "supports a modest sum: the dollar value, not the percentage, "
                        "is usually the limit. Units at or under <strong>26,000 lb "
                        "GVWR</strong> sell to buyers without a CDL, which helps "
                        "resale.",
        "sections": [
            ("What a Box Truck Is Worth to a Lender",
             "<p>Box trucks span four weight classes, and the class decides both the "
             "price and who can buy it. New prices, as published on our "
             "<a href=\"/equipment/box-trucks/\">box truck financing</a> page:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Size and class</th><th>Typical new price</th>"
             "<th>What it means for a loan</th></tr></thead><tbody>"
             "<tr><td data-label=\"Size\">10-16 ft, Class 3-4</td>"
             "<td data-label=\"New price\">$35,000-$75,000</td>"
             "<td data-label=\"Loan\">Easy to sell; a used one may support only a small advance</td></tr>"
             "<tr><td data-label=\"Size\">16-22 ft, Class 5-6</td>"
             "<td data-label=\"New price\">$75,000-$90,000</td>"
             "<td data-label=\"Loan\">The sweet spot: no CDL needed, wide buyer pool</td></tr>"
             "<tr><td data-label=\"Size\">22-26 ft, Class 6-7</td>"
             "<td data-label=\"New price\">$90,000-$100,000+</td>"
             "<td data-label=\"Loan\">Over 26,000 lb GVWR needs a CDL, so fewer buyers</td></tr>"
             "</tbody></table></div>"
             "<p>Used box trucks typically cost 30-50% less than new equivalents, and "
             "large delivery and rental fleets cycle units into the used market "
             "continuously. That keeps resale liquid but keeps prices low, which is "
             "why the advance on a box truck is usually a smaller number than owners "
             "hope.</p>"),
            ("Loan-to-Value: Why the Dollar Amount Is the Limit",
             "<p>Lenders commonly advance <strong>roughly 50-80% of forced liquidation "
             "value</strong> on owned trucks. That range is conventional across lenders, "
             "not anyone's quote. A box truck can sit in the upper part of it, because "
             "the market is deep and the trucks are easy to sell, and still produce a "
             "small loan, because the value underneath it is small.</p>"
             "<p>Two things specific to box trucks move it:</p>"
             "<ul>"
             "<li><strong>The 26,000-pound line.</strong> Under federal rules, a single "
             "vehicle rated over 26,000 lb GVWR needs a Class B CDL. A Class 6 box truck "
             "can be driven by anyone with a regular license; a Class 7 cannot. More "
             "buyers means a faster sale, which is what a lender prices.</li>"
             "<li><strong>Stop-and-go mileage.</strong> Delivery miles are hard miles: "
             "brakes, transmission and idling hours wear faster than on a highway truck "
             "with the same odometer reading.</li>"
             "</ul>"
             "<p>Because closing costs are largely fixed - title work, filing, any "
             "inspection - they take a bigger share of a small advance. Run the "
             "arithmetic before you start.</p>"),
            ("A Worked Example (Illustrative)",
             "<p>Take a used 24-foot Class 6 box truck, owned outright, whose forced "
             "liquidation value is put at $40,000. The figures are illustrative, not a "
             "quote:</p>"
             "<ul>"
             "<li>50-80% of $40,000 is <strong>$20,000-$32,000</strong></li>"
             "<li>No payoff, so that is the gross advance</li>"
             "<li>Less title work, lien filing and any inspection</li>"
             "</ul>"
             "<p>Compare that with the same owner's two- or three-truck fleet pledged "
             "together. One facility against several titles spreads the fixed costs and "
             "usually makes a more useful number - see "
             "<a href=\"../owner-operator-vs-fleet-title-loan-terms/\">owner-operator "
             "versus fleet terms</a>.</p>"),
            ("Who Lends on a Box Truck",
             "<ul>"
             "<li><strong>Equipment and commercial-vehicle finance companies</strong> "
             "that refinance owned trucks and pay out the equity. Some have a minimum "
             "loan size, which a single older box truck may not reach.</li>"
             "<li><strong>Fleet and delivery-business lenders</strong> that will take "
             "several titles in one facility, often alongside vans.</li>"
             "<li><strong>Banks and credit unions</strong>, mostly for existing "
             "customers; a smaller box truck is sometimes handled like any other "
             "business vehicle loan.</li>"
             "<li><strong>Consumer car-title lenders.</strong> A Class 3 cutaway looks "
             "close to a pickup, and some will take one, but under consumer rules and "
             "for a personal borrower. For business-purpose money, a commercial lender "
             "is the right home.</li>"
             "</ul>"),
            ("What the Appraiser Checks on a Box Truck",
             "<p>The chassis work is covered in "
             "<a href=\"../what-a-truck-appraiser-looks-for/\">what a truck appraiser "
             "looks for</a>. On a box truck the body is a large share of the value and "
             "the most variable part:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Area</th><th>What they look at</th></tr></thead><tbody>"
             "<tr><td data-label=\"Area\">Box</td>"
             "<td data-label=\"Looks at\">Panel damage, roof leaks, floor condition, "
             "door and roll-up operation</td></tr>"
             "<tr><td data-label=\"Area\">Liftgate</td>"
             "<td data-label=\"Looks at\">Rated capacity, hydraulics, whether it "
             "works under load</td></tr>"
             "<tr><td data-label=\"Area\">Reefer unit</td>"
             "<td data-label=\"Looks at\">If refrigerated, unit hours and service "
             "history, valued on top of the truck</td></tr>"
             "<tr><td data-label=\"Area\">Weight rating</td>"
             "<td data-label=\"Looks at\">GVWR on the door plate - which side of "
             "26,000 lb it falls</td></tr>"
             "<tr><td data-label=\"Area\">Drivetrain</td>"
             "<td data-label=\"Looks at\">Brakes and transmission wear from delivery "
             "duty; idle hours</td></tr>"
             "<tr><td data-label=\"Area\">Presentation</td>"
             "<td data-label=\"Looks at\">Old fleet graphics, decal removal damage, "
             "interior condition</td></tr>"
             "</tbody></table></div>"),
            ("When a Title Loan Is the Wrong Tool",
             "<ul>"
             "<li><strong>The truck is leased or on a rental contract.</strong> You do "
             "not hold the title, so there is nothing to lend against.</li>"
             "<li><strong>The advance is too small to be worth the cost.</strong> If a "
             "single older truck supports only a few thousand dollars after fees, a "
             "<a href=\"/business-line-of-credit.html\">business line of credit</a> or "
             "working capital loan is usually cheaper per dollar.</li>"
             "<li><strong>The gap is a delivery contract that pays late.</strong> Net "
             "terms from a shipper or platform are a receivables problem; financing "
             "against the invoices matches it better.</li>"
             "<li><strong>You need the truck replaced, not refinanced.</strong> If the "
             "box truck is near the end of its life, the cash is better raised as a "
             "down payment on an equipment loan for the next one.</li>"
             "</ul>"
             "<p>If a title loan does fit, "
             "<a href=\"/match.html\">send the VIN, GVWR and payoff</a> and we will "
             "tell you plainly what it supports.</p>"),
        ],
        "faqs": [
            ("Can I get a title loan on my box truck?",
             "Yes, as a business-purpose loan secured by the title. Lenders advance "
             "against the truck's forced liquidation value, commonly in the range of "
             "50-80% of it, less any payoff, and you keep using the truck."),
            ("How much can I borrow against a box truck?",
             "Usually a modest amount, because the truck's value is modest. New box "
             "trucks run roughly $35,000 to $100,000 or more, used ones less, and a "
             "lender advances a percentage of what the used truck would fetch sold "
             "quickly."),
            ("Does it matter if my box truck needs a CDL?",
             "It can. A single vehicle over 26,000 lb GVWR needs a Class B CDL, so "
             "fewer buyers can use it. A Class 6 truck under that line sells to a wider "
             "pool, which a lender pricing a quick sale counts in its favor."),
            ("Can I borrow against several box trucks at once?",
             "Yes, and it often makes more sense. One facility against several titles "
             "spreads the fixed closing costs and produces a more useful number than a "
             "single older truck."),
            ("Can I get a title loan on a leased box truck?",
             "No. A title loan needs a title you own; on a leased or rental truck the "
             "leasing company holds it. The equity question only arises once the truck "
             "is yours."),
        ],
        "related": [
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("/equipment/box-trucks/", "Box truck financing"),
            ("../owner-operator-vs-fleet-title-loan-terms/", "Owner-operator vs fleet title loan terms"),
            ("../dump-truck-title-loan/", "Dump truck title loans"),
        ],
        "sources": [OCC_ABL, AFDC_CLASSES, ECFR_CDL, IRS_946],
    },
    {
        "slug": "tow-truck-title-loan",
        "crumb": "Tow Truck Title Loans",
        "title": "Tow Truck Title Loans: Value, LTV, Lenders | Axiant",
        "og_title": "Can You Get a Title Loan on a Tow Truck?",
        "h1": "Tow Truck Title Loans",
        "headline": "Tow Truck Title Loans: What the Truck Supports and Who Lends",
        "lede": "Borrowing against a rollback, wrecker or rotator you own - why the "
                "body carries much of the value, and why the net-30 motor-club gap "
                "is usually a different problem",
        "meta_desc": "A tow truck title loan values the chassis and the recovery "
                     "body together. What rollbacks, wreckers and rotators support, "
                     "who lends, what the appraiser checks, and when to skip it.",
        "article_desc": "How lenders value and lend against an owned tow truck, by "
                        "class, chassis and body.",
        "keywords": "tow truck title loan, borrow against tow truck, wrecker title "
                    "loan, rollback equity loan, rotator equity loan",
        "quick_answer": "Yes, as a business-purpose loan against the title. Axiant "
                        "Partners, a business-loan broker in Boca Raton, sees lenders "
                        "advance roughly <strong>50-80% of forced liquidation "
                        "value</strong>, less any payoff. Tow trucks run from about "
                        "<strong>$60,000 for a light-duty wrecker to $500,000+ for a "
                        "rotator</strong> new, and much of that value is in the "
                        "recovery body, so the appraiser values chassis and body "
                        "separately. Rollbacks resell fastest; rotators sell to few "
                        "buyers.",
        "sections": [
            ("What a Tow Truck Is Worth to a Lender",
             "<p>Tow trucks are a chassis with an expensive, specialized body on it, "
             "and the class decides how many operators could buy it. New prices, as "
             "published in our <a href=\"/equipment-financing/articles/tow-truck-wrecker-financing/\">tow "
             "truck and wrecker financing guide</a>:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Class</th><th>Typical new price</th>"
             "<th>Where it tends to sit in the advance range</th></tr></thead><tbody>"
             "<tr><td data-label=\"Class\">Light-duty wrecker</td>"
             "<td data-label=\"New price\">$60K-$120K</td>"
             "<td data-label=\"Advance\">Middle to upper: many buyers</td></tr>"
             "<tr><td data-label=\"Class\">Rollback / flatbed</td>"
             "<td data-label=\"New price\">$90K-$160K</td>"
             "<td data-label=\"Advance\">Upper: the most liquid tow truck there is</td></tr>"
             "<tr><td data-label=\"Class\">Medium-duty</td>"
             "<td data-label=\"New price\">$120K-$250K</td>"
             "<td data-label=\"Advance\">Middle</td></tr>"
             "<tr><td data-label=\"Class\">Heavy-duty wrecker</td>"
             "<td data-label=\"New price\">$200K-$400K</td>"
             "<td data-label=\"Advance\">Middle to lower: fewer buyers, CDL required</td></tr>"
             "<tr><td data-label=\"Class\">Rotator</td>"
             "<td data-label=\"New price\">$400K-$500K+</td>"
             "<td data-label=\"Advance\">Lower: a thin resale market</td></tr>"
             "</tbody></table></div>"
             "<p>A used unit is valued as it sits, at what it would fetch sold quickly, "
             "not against these new prices.</p>"),
            ("Loan-to-Value: The Body Is Half the Story",
             "<p>Lenders commonly advance <strong>roughly 50-80% of forced liquidation "
             "value</strong> on owned trucks. That range is conventional across lenders, "
             "not anyone's quote. What makes tow trucks different is where the value "
             "sits:</p>"
             "<ul>"
             "<li><strong>The body usually rides on the chassis title.</strong> The "
             "lien is recorded on one title, but the appraiser values the chassis and "
             "the wrecker, rollback or rotator body separately and adds them. A good "
             "body on a tired chassis can be moved to a new one, and buyers know "
             "it.</li>"
             "<li><strong>Specialization cuts both ways.</strong> A rotator is worth a "
             "great deal to a heavy-recovery operator and very little to anyone else. "
             "A quick sale has to find that buyer, so the advance is conservative even "
             "though the value is high.</li>"
             "<li><strong>Rollbacks are the easy case.</strong> Light-duty towing, "
             "repo, equipment transport and dealers all buy them, which is why they "
             "sit at the top of the range.</li>"
             "</ul>"),
            ("A Worked Example (Illustrative)",
             "<p>Take a used medium-duty wrecker with a forced liquidation value put at "
             "$70,000 - say $30,000 for the chassis and $40,000 for the body - and "
             "$15,000 still owed. The figures are illustrative, not a quote:</p>"
             "<ul>"
             "<li>50-80% of $70,000 is <strong>$35,000-$56,000</strong></li>"
             "<li>Less the $15,000 payoff leaves <strong>$20,000-$41,000</strong></li>"
             "<li>Less title work, lien filing and the inspection</li>"
             "</ul>"
             "<p>If the chassis were tired and the body sound, the split above is what "
             "keeps the number up. Documented body service is how you show it.</p>"),
            ("Who Lends on a Tow Truck",
             "<ul>"
             "<li><strong>Vocational-truck and equipment finance companies</strong> "
             "that know towing, refinance owned units and pay out the equity. They "
             "understand body value; a generalist may not credit it.</li>"
             "<li><strong>Towing-focused lenders and programs</strong>, sometimes tied "
             "to body builders. These mostly finance new purchases rather than cash-out, "
             "but some will refinance a unit they financed originally.</li>"
             "<li><strong>Banks and credit unions</strong>, mostly for established "
             "operators with financial statements.</li>"
             "<li><strong>Consumer car-title lenders</strong>, which appear in search "
             "results but lend to individuals against personal vehicles, with caps "
             "sized to cars. A wrecker is not what they are set up for.</li>"
             "</ul>"
             "<p>For the full range of towing finance, from equipment to working "
             "capital, see <a href=\"/towing-business-financing.html\">towing and "
             "recovery business financing</a>.</p>"),
            ("What the Appraiser Checks on a Tow Truck",
             "<p>Chassis checks follow "
             "<a href=\"../what-a-truck-appraiser-looks-for/\">what a truck appraiser "
             "looks for</a>. The recovery equipment gets its own inspection:</p>"
             "<div class=\"table-wrap\"><table style=\"width:100%\">"
             "<thead><tr><th>Area</th><th>What they look at</th></tr></thead><tbody>"
             "<tr><td data-label=\"Area\">Body ID</td>"
             "<td data-label=\"Looks at\">Body maker, model and serial plate; rated "
             "capacity</td></tr>"
             "<tr><td data-label=\"Area\">Boom and wheel-lift</td>"
             "<td data-label=\"Looks at\">Extension, cylinder leaks, wear pads, "
             "wheel-lift and underlift operation</td></tr>"
             "<tr><td data-label=\"Area\">Winches and cable</td>"
             "<td data-label=\"Looks at\">Cable condition, winch operation, "
             "replacement records</td></tr>"
             "<tr><td data-label=\"Area\">Rollback deck</td>"
             "<td data-label=\"Looks at\">Deck tilt and slide, bed condition, "
             "hydraulics</td></tr>"
             "<tr><td data-label=\"Area\">PTO hours</td>"
             "<td data-label=\"Looks at\">Recovery work shows up in PTO hours, not "
             "odometer miles</td></tr>"
             "<tr><td data-label=\"Area\">Paperwork</td>"
             "<td data-label=\"Looks at\">Clean title, body invoice if remounted, "
             "inspection and service records</td></tr>"
             "</tbody></table></div>"),
            ("When a Title Loan Is the Wrong Tool",
             "<ul>"
             "<li><strong>The gap is motor-club or police-rotation pay.</strong> Those "
             "accounts often pay on net-30 terms, and the shortfall comes back every "
             "month. A lien on a truck does not fix a recurring receivables gap; see "
             "<a href=\"/towing-business-financing/towing-motor-club-net-30-cash-flow/\">"
             "financing motor-club net-30 cash flow</a>.</li>"
             "<li><strong>You are adding a rotator or heavy wrecker.</strong> Finance "
             "the new unit with an equipment loan; cashing out an existing truck to buy "
             "one is usually the expensive way round.</li>"
             "<li><strong>Losing the truck would cost you a rotation slot.</strong> "
             "Rotation lists generally require trucks in service. A default that puts a "
             "truck at risk can cost the account, not just the asset.</li>"
             "<li><strong>There is little equity.</strong> A recent purchase with most "
             "of its loan outstanding has little to lend against.</li>"
             "</ul>"
             "<p>If a title loan does fit, "
             "<a href=\"/match.html\">send the VIN, body serial and payoff</a> and we "
             "will tell you plainly what the truck supports.</p>"),
        ],
        "faqs": [
            ("Can I get a title loan on my tow truck?",
             "Yes, as a business-purpose loan secured by the title. Lenders advance "
             "against the truck's forced liquidation value, commonly in the range of "
             "50-80% of it, less any payoff, and the truck stays on calls."),
            ("Does the wrecker body count toward the loan?",
             "Yes, and often for much of the value. The lien is recorded on the chassis "
             "title, but the appraiser values the chassis and the recovery body "
             "separately and adds them, so body condition and records matter."),
            ("Can I borrow against a rotator?",
             "Yes, but expect a conservative advance relative to its value. A rotator "
             "sells to few buyers, and a lender sizes the loan to what a quick sale "
             "would fetch, which a thin market pulls down."),
            ("Should I use a title loan to cover slow motor-club payments?",
             "Usually not. Net-30 motor-club and rotation pay is a recurring "
             "receivables gap, and a one-off loan against a truck does not close it. "
             "Working capital or receivables financing fits that problem better."),
            ("Will a car title lender take a tow truck?",
             "Rarely. Consumer title lenders lend to individuals against personal "
             "vehicles under state consumer rules. A business-purpose tow truck loan "
             "goes through a vocational-truck or equipment lender."),
        ],
        "related": [
            ("/commercial-truck-title-loan.html", "Commercial truck title loans"),
            ("/towing-business-financing.html", "Towing and recovery business financing"),
            ("/equipment-financing/articles/tow-truck-wrecker-financing/", "Tow truck and wrecker financing"),
            ("../box-truck-title-loan/", "Box truck title loans"),
        ],
        "sources": [OCC_ABL, FMCSA, IRS_946, FTC],
    },
]
