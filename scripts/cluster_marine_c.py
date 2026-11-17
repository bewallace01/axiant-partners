# -*- coding: utf-8 -*-
"""Commercial marine financing, articles 4-5."""
from cluster_marine import (USCG_NVDC, NOAA, SBA_7A, CFPB, FTC, SBCS, SLOOS)
from cluster_table import table

FFP = ("https://www.fisheries.noaa.gov/national/funding-and-financial-services/fisheries-finance-program",
       "NOAA Fisheries Finance Program",
       "What the federal program finances, its 0.5% filing fee, and the bar on "
       "refits that materially increase harvesting capacity.")
FFP_CFR = ("https://www.law.cornell.edu/cfr/text/50/253.11",
           "50 CFR 253.11: FFP credit standards",
           "The 80%-of-actual-cost ceiling and the rate set at 2% above the "
           "Treasury's cost of borrowing.")
FISHERY_END = ("https://www.law.cornell.edu/uscode/text/46/12113",
               "46 U.S.C. 12113: Fishery endorsement",
               "Owner citizenship rules for a vessel's fishery endorsement.")

TREASURY = ("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve",
            "U.S. Treasury: Daily Treasury Par Yield Curve Rates",
            "The 10- and 20-year yields used to illustrate the program's Treasury + 2% rate (November 10, 2026).")
SBA_SOP = ("https://www.sba.gov/document/sop-50-10-lender-development-company-loan-programs",
           "SBA SOP 50 10 8.1",
           "The 7(a) rules, including the minimum equity injection for start-ups and changes of ownership.")
TRE = ('<a href="https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve" '
       'rel="noopener nofollow" target="_blank">Treasury yield curve</a>')

MORE = [
    {
        # Search Console, Oct 9 - Nov 6 2026: "commercial fishing boat loans" 253
        # impressions (best position 24) and "commercial fishing boat financing" 157
        # (best 18), split between this page, the marine hub and the Louisiana page.
        # Strengthened 2026-11-08 inside the marine cluster (no new root). No boat
        # loan rates: the site publishes none and Alex's ranges aren't in yet. NOAA
        # Fisheries Finance Program terms from 50 CFR 253.11 and NOAA's program page.
        # 2026-11-12 (Search Console Oct 13 - Nov 9): target page for "commercial
        # fishing boat loans" 279 and "commercial fishing boat financing" 205, which
        # were split with the Louisiana page (pos 39) and the marine hub (pos 27-31).
        # Added: the program's rate at today's Treasury yields (computed), a first-time
        # buyer section and two FAQs. The Louisiana page and hub now link here.
        "slug": "commercial-fishing-vessel-financing",
        "date_published": "2026-11-08",
        "crumb": "Fishing Boat Loans",
        "title": "Commercial Fishing Boat Loans and Financing | Axiant",
        "og_title": "Commercial Fishing Boat Loans: Vessel, Permit and Lenders",
        "h1": "Commercial Fishing Boat Loans: Vessel, Permit and Who Lends",
        "headline": "Commercial Fishing Boat Loans: Vessel, Permit and Who Lends",
        "lede": "Who finances a commercial fishing boat, what the federal program "
                "covers, and why the permit can decide the deal",
        "meta_desc": "Commercial fishing boat loans: who lends, NOAA's Fisheries Finance "
                     "Program (up to 80% of cost), SBA 7(a) to $5 million, and how the "
                     "permit changes the deal.",
        "article_desc": "Who finances commercial fishing boats, what NOAA's Fisheries "
                        "Finance Program covers, and how permits and quota affect the loan.",
        "keywords": "commercial fishing boat loans, commercial fishing boat financing, "
                    "fishing vessel loan, fisheries finance program, fishing permit loan",
        "quick_answer": "As of November 2026, commercial fishing boat loans come from marine lenders, banks with "
                        "fishing customers, SBA 7(a) loans of up to <strong>$5 million</strong>, "
                        "and NOAA&rsquo;s Fisheries Finance Program, which can lend up to "
                        "<strong>80%</strong> of the cost of an existing vessel at a fixed rate "
                        "<strong>2%</strong> above the Treasury&rsquo;s borrowing cost. Lenders "
                        "typically want a survey, a multi-season landings history and proof the "
                        "permit transfers. Axiant Partners, a business-loan broker in Boca Raton, "
                        "matches fishing operators with marine lenders.",
        "sections": [
            ("Who Lends on Commercial Fishing Boats",
             "<p>Fishing boat finance is a small market, and most general equipment "
             "lenders stay out of it. The realistic sources, and what each tends to "
             "fit:</p>"
             + table(["Source", "Best fit", "Watch for"], [
                 ["Marine lenders", "Used boats, quick purchases, refinancing",
                  "Survey and lien rules; terms set by the boat&rsquo;s age"],
                 ["Fishing-focused banks", "Established operators in ports they know",
                  "Usually want a long relationship and landings history"],
                 ["SBA 7(a) through a bank", "Boat plus working capital, up to $5 million",
                  "Slower; the bank decides if it lends on vessels"],
                 ["NOAA finance program", "Buying or refurbishing an existing boat, refinancing",
                  "No capacity-increasing refits; slower than a private loan"],
                 ["Seller financing", "Covering a permit a lender won&rsquo;t take",
                  "Needs the same transfer checks as any sale"],
             ])
             + "<p>The source matters less than the file. Every one of them will ask the "
             "same three questions: what the boat is worth, what the permit is worth and "
             "whether it transfers, and what the boat has landed over several seasons. "
             "For the wider marine picture, including workboats and charter boats, see "
             '<a href="/commercial-marine-financing.html">commercial marine financing</a>.</p>'),
            ("NOAA's Fisheries Finance Program in Plain Terms",
             "<p>The federal program is the one source built only for this trade. Its "
             "rules are public, so they can be stated plainly:</p>"
             "<ul>"
             "<li><strong>What it finances:</strong> buying, refurbishing or modernizing "
             "existing fishing vessels and shore facilities, certain federal catch-share "
             "privileges and quota, and refinancing debt taken on for those purposes.</li>"
             "<li><strong>How much:</strong> no more than <strong>80% of actual cost</strong>, "
             "and the program can approve less (50 CFR 253.11).</li>"
             "<li><strong>Rate:</strong> fixed, <strong>2% above the U.S. Treasury&rsquo;s cost "
             "of borrowing</strong> for a similar maturity at closing.</li>"
             "<li><strong>Fee:</strong> a one-time filing and commitment fee of "
             "<strong>0.5%</strong> of the proposed loan.</li>"
             "<li><strong>What it won&rsquo;t do:</strong> fund a refit that materially "
             "increases the boat&rsquo;s harvesting capacity, or lend to an applicant who "
             "can&rsquo;t document fishing industry experience.</li>"
             "</ul>"
             '<p>Source: <a href="https://www.fisheries.noaa.gov/national/funding-and-financial-services/fisheries-finance-program" '
             'rel="noopener nofollow" target="_blank">NOAA Fisheries Finance Program</a> and '
             '<a href="https://www.law.cornell.edu/cfr/text/50/253.11" rel="noopener nofollow" '
             'target="_blank">50 CFR 253.11</a>. Because it is slower than a private loan, '
             "buyers on a deadline often close with a marine lender and look at the program "
             "for refinancing later. Ask before you sign whether the private loan allows "
             "that.</p>"),
            ("Worked Example: A $450,000 Boat-and-Permit Purchase",
             "<p><strong>Illustrative numbers, not a quote.</strong> A buyer agrees to pay "
             "$300,000 for a used vessel and $150,000 for the permit that goes with it. How "
             "much of that a lender will finance depends on which half it can secure:</p>"
             + table(["Case", "Financeable cost", "Loan at 80%", "Buyer brings"], [
                 ["Permit can be financed", "$450,000", "$360,000", "$90,000"],
                 ["Vessel only", "$300,000", "$240,000",
                  "$210,000, or a seller note for the permit"],
             ])
             + "<p>&ldquo;Permit can be financed&rdquo; means the permit is a federal "
             "catch-share privilege the program can lend against. In that case the "
             "program&rsquo;s 0.5% filing fee on $360,000 is "
             "$1,800. The gap in the second case is why the permit question comes first: "
             "the same boat needs $120,000 more from the buyer when the permit can&rsquo;t "
             "be pledged. The 80% figure is the program&rsquo;s ceiling. Private marine "
             "lenders set their own advance, so ask each one what share of the boat and "
             "the permit it will count.</p>"),
            ("What the Federal Program's Rate Looks Like Today",
             "<p>No private marine lender publishes a fishing boat rate, and we don&rsquo;t "
             "either. The federal program is the exception, because its rate is a formula: "
             "Treasury&rsquo;s cost of borrowing for a similar maturity, plus 2%. Treasury "
             "sets that cost at closing, so the market yields below are a guide, not the "
             "program&rsquo;s number. On November 10, 2026 the " + TRE + " showed:</p>"
             + table(["Maturity", "Treasury yield", "Plus 2%", "Payment on $360,000"], [
                 ["10 years", "4.98%", "About 6.98%", "About $4,176 a month"],
                 ["20 years", "5.39%", "About 7.39%", "About $2,876 a month"],
             ])
             + "<p><strong>Illustrative, not a quote.</strong> The $360,000 is the loan from "
             "the worked example below, paid monthly over the full term. The program sets "
             "the maturity for each project, so a 20-year term may not be offered for your "
             "boat. Over 10 years the interest adds about $141,000; over 20 years about "
             "$330,000, which is the price of the lower payment. Private loans are priced "
             "case by case and usually close faster.</p>"),
            ("First-Time Buyers: From Deckhand to Owner",
             "<p>Most first boats are bought by people who have fished for years on someone "
             "else&rsquo;s deck. That experience is the qualification lenders ask about "
             "first, because the program requires documented industry experience and private "
             "lenders want the same comfort.</p>"
             "<ul>"
             "<li><strong>Show your seasons:</strong> settlement sheets, crew shares or a "
             "letter from the captain you fished for stand in for an operating history.</li>"
             "<li><strong>Expect to bring cash:</strong> the program lends at most 80% of "
             "cost, and SBA 7(a) loans for a start-up or a change of ownership require an "
             "equity injection of at least 10% under "
             '<a href="https://www.sba.gov/document/sop-50-10-lender-development-company-loan-programs" '
             'rel="noopener nofollow" target="_blank">SOP 50 10 8.1</a>.</li>'
             "<li><strong>Ask the seller:</strong> a seller note on the permit is common when "
             "a lender will finance only the hull.</li>"
             "<li><strong>Price the first season:</strong> fuel, ice, bait, insurance and crew "
             "before the first landing, which is a working capital need, not part of the "
             "boat loan.</li>"
             "</ul>"
             "<p>If the boat comes with a business, such as a dock lease or a buyer "
             "relationship, see <a href=\"/business-acquisition-financing.html\">business "
             "acquisition financing</a>.</p>"),
            ("The Permit Is Part of the Business, and Sometimes Most of It",
             "<p>This is the feature that makes fishing vessel finance unlike "
             "any other marine lending.</p>"
             "<p>In many managed fisheries, the right to fish is a limited, "
             "transferable asset &mdash; a permit, a license, or an allocation "
             "of quota. It is bought and sold in its own right, and in some "
             "fisheries it is worth considerably more than the vessel that uses "
             "it.</p>"
             "<p>The consequence for financing is direct. A buyer purchasing "
             "\"a fishing boat\" is often purchasing two distinct assets, and a "
             "lender securing only the hull is securing the smaller half. "
             "Whether and how the permit can be pledged, and whether it "
             "transfers cleanly to a buyer, is central rather than "
             "incidental.</p>"
             "<p>The most common way these purchases fall apart is a buyer assuming the "
             "permit comes with the boat. Some permits transfer freely, some require the "
             "buyer to meet eligibility rules, some are restricted by region, length or "
             "history, and some don't transfer at all. Get the answer in writing from the "
             "managing authority, not the seller, before you make an offer.</p>"
             "<p>Federal fisheries regulation, including permit and quota "
             "systems, is set out by "
             '<a href="https://www.fisheries.noaa.gov/topic/laws-policies" '
             'rel="noopener nofollow" target="_blank">NOAA Fisheries</a>. The '
             "rules differ by fishery and by region, which is exactly why this "
             "cannot be generalised.</p>"),
            ("What the Two Halves Look Like",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th></th><th>The vessel</th><th>The permit or quota</th>"
             "</tr></thead><tbody>"
             '<tr><td data-label=""><strong>What it is</strong></td>'
             '<td data-label="Vessel">A physical, surveyable asset</td>'
             '<td data-label="Permit">A regulatory right, often transferable</td></tr>'
             '<tr><td data-label=""><strong>Valued by</strong></td>'
             '<td data-label="Vessel">Marine surveyor</td>'
             '<td data-label="Permit">Market for that fishery</td></tr>'
             '<tr><td data-label=""><strong>Secured by</strong></td>'
             '<td data-label="Vessel">Preferred ship mortgage or state lien</td>'
             '<td data-label="Permit">Depends entirely on the fishery</td></tr>'
             '<tr><td data-label=""><strong>Transfers</strong></td>'
             '<td data-label="Vessel">With the sale</td>'
             '<td data-label="Permit">Only under the fishery&rsquo;s rules</td></tr>'
             '<tr><td data-label=""><strong>Risk</strong></td>'
             '<td data-label="Vessel">Condition, market</td>'
             '<td data-label="Permit">Regulatory change</td></tr>'
             "</tbody></table></div>"
             "<p>That last row is the one to sit with. Permit value depends on "
             "management decisions that can change, and a lender lending against "
             "it is taking regulatory risk as well as credit risk.</p>"
             "<p>Ownership matters too. A documented fishing vessel needs a fishery "
             "endorsement, and "
             '<a href="https://www.law.cornell.edu/uscode/text/46/12113" rel="noopener nofollow" '
             'target="_blank">46 U.S.C. 12113</a> sets U.S. citizenship rules for the owner. '
             "A financing or lease structure that puts title with an ineligible owner can "
             "cost the boat its endorsement, which is why marine lenders check it.</p>"),
            ("Seasonality and Landings History",
             "<p>Fishing revenue is seasonal, weather-dependent and "
             "quota-constrained, which makes a single quarter almost "
             "meaningless as evidence.</p>"
             "<p>What lenders want instead is a <strong>multi-season landings "
             "history</strong> &mdash; what was caught, when, and what it "
             "realised. That shows the operation's actual capacity rather than "
             "one good or bad run, and it is the closest thing this trade has to "
             "contracted revenue.</p>"
             "<p>Alongside it, expect questions on how the off-season is funded and "
             "whether the boat works a second fishery. If you want a seasonal payment "
             "schedule, ask for it at term-sheet stage.</p>"),
            ("Preparing a Fishing Boat Loan Application",
             "<ol>"
             "<li><strong>Confirm permit transferability in writing</strong> "
             "from the managing authority, before an offer.</li>"
             "<li><strong>Value the two halves separately</strong> &mdash; "
             "survey for the vessel, market evidence for the permit.</li>"
             "<li><strong>Bring multi-season landings data</strong>, not one "
             "year.</li>"
             "<li><strong>Document the permit or quota holding</strong> and any "
             "conditions attached.</li>"
             "<li><strong>Run a lien search</strong> on the vessel &mdash; and "
             "ask whether anything is secured against the permit.</li>"
             "<li><strong>Get commercial cover quoted</strong> for the actual "
             "fishery and waters.</li>"
             "</ol>"
             "<p>Then compare sources side by side. "
             '<a href="/match.html">Get matched with marine lenders</a>, or read '
             '<a href="../commercial-vessel-loan-requirements/">what vessel lenders '
             "require</a> first.</p>"),
        ],
        "faqs": [
            ("What is the interest rate on a commercial fishing boat loan?",
             "Private marine lenders price each boat and file, and none publish a fishing "
             "rate. NOAA's Fisheries Finance Program is fixed at 2% above Treasury's cost "
             "of borrowing for a similar maturity. With Treasury yields of 4.98% (10-year) "
             "and 5.39% (20-year) on November 10, 2026, that is roughly 7.0-7.4%, set at "
             "closing. This is an illustration, not a quote."),
            ("Can a first-time buyer get a commercial fishing boat loan?",
             "Yes, if you can document fishing experience, such as settlement sheets or crew "
             "shares, and bring cash. The federal program lends at most 80% of cost, and "
             "SBA 7(a) loans for a start-up or change of ownership need at least 10% equity. "
             "A seller note on the permit often fills the gap."),
            ("Who gives loans for commercial fishing boats?",
             "Marine lenders, banks with fishing customers, SBA 7(a) lenders, NOAA's "
             "Fisheries Finance Program and sometimes the seller. Most general equipment "
             "lenders don't lend on fishing vessels."),
            ("How much will NOAA's Fisheries Finance Program lend?",
             "Up to 80% of actual cost under 50 CFR 253.11, and it can approve less. The "
             "rate is fixed at 2% above the Treasury's cost of borrowing, and there is a "
             "0.5% filing and commitment fee."),
            ("Can the Fisheries Finance Program pay for a new boat?",
             "Its program page describes financing for buying, refurbishing or modernizing "
             "existing vessels and refinancing related debt, and it won't fund a refit that "
             "materially increases harvesting capacity. Ask NOAA's Financial Services staff "
             "about your project before planning around it."),
            ("Can a fishing permit be worth more than the boat?",
             "In many managed fisheries, yes. Permits and quota allocations are "
             "limited, transferable assets traded in their own right, and in "
             "some fisheries they carry considerably more value than the vessel "
             "using them."),
            ("Does the permit automatically transfer with the vessel?",
             "No, and assuming it does is the most common way these purchases "
             "collapse. Transfer rules vary by fishery &mdash; some permits "
             "transfer freely, some require buyer eligibility, some are "
             "restricted, and some do not transfer at all."),
            ("What revenue evidence do lenders want?",
             "A multi-season landings history rather than a single year &mdash; "
             "what was caught, when, and what it realised. Fishing revenue is "
             "seasonal, weather-dependent and quota-constrained, so one period "
             "tells a lender very little."),
        ],
        "related": [
            ("/commercial-marine-financing.html", "Commercial marine financing"),
            ("../commercial-vessel-loan-requirements/",
             "Commercial vessel loan requirements"),
            ("../commercial-vessel-loan-vs-marine-lease/",
             "Commercial vessel loan vs marine lease"),
            ("../marine-survey-what-lenders-require/",
             "What a marine survey covers"),
            ("/equipment-financing/articles/louisiana-commercial-fishing-financing/",
             "Louisiana commercial fishing financing"),
            ("/match.html", "Get matched with marine lenders"),
        ],
        "sources": [FFP, FFP_CFR, TREASURY, NOAA, USCG_NVDC, FISHERY_END, SBA_7A, SBA_SOP],
    },
    {
        "slug": "workboat-and-tug-financing",
        "crumb": "Workboats and Tugs",
        "title": "Workboat and Tug Financing | Axiant Partners",
        "og_title": "Workboat and Tug Financing: Long-Lived, Slow to Sell",
        "h1": "Workboat and Tug Financing",
        "headline": "Workboat and Tug Financing",
        "lede": "Assets that last decades and sell slowly - what that does to "
                "terms, and why the contract carries the file",
        "meta_desc": "Workboats and tugs are long-lived but specialised, so "
                     "they sell slowly. How that shapes advance rates and terms, "
                     "and why contracted work carries the application.",
        "article_desc": "How workboat and tug financing is underwritten and what "
                        "strengthens an application.",
        "keywords": "workboat financing, tug boat loan, crew boat financing, "
                    "offshore support vessel finance",
        "quick_answer": "Workboats and tugs are <strong>long-lived and "
                        "specialised</strong>, which pulls in two directions: a "
                        "well-maintained hull can work for decades, but the "
                        "buyer pool is narrow so a forced sale is slow. Lenders "
                        "resolve that by leaning on the "
                        "<strong>contracted work</strong> behind the vessel more "
                        "than on the hull, and by pricing conservatively where "
                        "there is none.",
        "sections": [
            ("Long Life, Thin Market",
             "<p>These vessels sit at an unusual point. A properly maintained "
             "tug or workboat can be productive for a very long time &mdash; far "
             "longer than most financed equipment. That argues for a long "
             "term.</p>"
             "<p>Against it, the buyer pool is narrow. A purpose-built tug suits "
             "a small number of operators, and selling one quickly means "
             "accepting a substantial discount. That argues for conservatism.</p>"
             "<p>Lenders resolve the tension by looking past the hull to the "
             "work. A vessel with contracted employment is financeable on its "
             "revenue; one sitting idle is financeable only on a slow-moving "
             "asset, and priced accordingly.</p>"),
            ("How the Segments Differ",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Vessel</th><th>Typical employment</th>"
             "<th>What lenders weigh</th></tr></thead><tbody>"
             '<tr><td data-label="Vessel">Harbour tug</td>'
             '<td data-label="Employment">Ship assist, berthing</td>'
             '<td data-label="Weigh">Port contracts; steady but competitive</td></tr>'
             '<tr><td data-label="Vessel">Push boat</td>'
             '<td data-label="Employment">Inland barge movements</td>'
             '<td data-label="Weigh">Long-lived; river trade cycles</td></tr>'
             '<tr><td data-label="Vessel">Crew boat</td>'
             '<td data-label="Employment">Offshore personnel transfer</td>'
             '<td data-label="Weigh">Tied to the offshore cycle</td></tr>'
             '<tr><td data-label="Vessel">Utility and supply</td>'
             '<td data-label="Employment">Construction, survey support</td>'
             '<td data-label="Weigh">Project-based; contract duration matters</td></tr>'
             '<tr><td data-label="Vessel">Dredge support</td>'
             '<td data-label="Employment">Civil works</td>'
             '<td data-label="Weigh">Often public contracts; slow but '
             "reliable</td></tr>"
             "</tbody></table></div>"
             "<p>Offshore-exposed vessels are read against the cycle. An "
             "application during a downturn faces a harder valuation "
             "conversation than the same vessel in a strong market, even where "
             "the operator is unchanged.</p>"),
            ("Contracts Do the Heavy Lifting",
             "<p>Because the asset sells slowly, employment is what makes these "
             "files work.</p>"
             "<ul>"
             "<li><strong>Contract duration.</strong> A multi-year charter is "
             "close to the strongest thing an operator can bring.</li>"
             "<li><strong>Counterparty credit.</strong> Who is paying matters as "
             "much as the rate &mdash; the same logic as factoring.</li>"
             "<li><strong>Renewal history.</strong> Repeated renewals with the "
             "same client read almost as well as a long contract.</li>"
             "<li><strong>Day rates against operating cost</strong>, so the "
             "margin is visible rather than asserted.</li>"
             "<li><strong>Utilisation</strong> across your existing fleet, if "
             "you have one.</li>"
             "</ul>"
             "<p>An operator buying speculatively into a soft market is asking "
             "for the hardest version of this. It is not impossible, but expect "
             "lower leverage and a shorter term.</p>"),
            ("Repower and Life Extension",
             "<p>Because hulls outlast machinery by a wide margin in this "
             "segment, a large share of lending is repower rather than "
             "purchase.</p>"
             "<p>The distinction a lender draws is whether the work "
             "<strong>extends the vessel's life and value</strong> or merely "
             "maintains it. New main engines, gear or generators in a sound hull "
             "do the former and support lending; routine maintenance does not, "
             "however necessary.</p>"
             "<p>Expect an itemised yard quote, staged disbursement against "
             "milestones, and a plan for the downtime &mdash; a vessel in the "
             "yard earns nothing, and that period is often the tightest cash "
             "month of the year. The pillar covers this in more detail under "
             '<a href="/commercial-marine-financing.html">commercial marine '
             "financing</a>.</p>"),
            ("Strengthening a Workboat Application",
             "<ul>"
             "<li><strong>Lead with the contract</strong> &mdash; duration, "
             "counterparty, day rate.</li>"
             "<li><strong>Show utilization history</strong> on existing vessels "
             "if you operate a fleet.</li>"
             "<li><strong>Document maintenance</strong>; on a long-lived asset "
             "it is the difference between decades of service and a tired "
             "hull.</li>"
             "<li><strong>Get an accredited survey</strong> from a surveyor who "
             "knows commercial workboats, not yachts.</li>"
             "<li><strong>Clarify documentation status</strong> and run a lien "
             "search early.</li>"
             "<li><strong>Be realistic about the cycle</strong> if the work is "
             "offshore-exposed &mdash; lenders will be.</li>"
             "</ul>"
             "<p>What separates a strong workboat file from a weak one is "
             "rarely the vessel. It is whether the operator can show the work "
             "is there and the boat has been kept ready for it. A well-"
             "maintained hull under contract borrows on better terms than a "
             "newer one sitting idle, because the lender is pricing the "
             "cash flow first and the steel second.</p>"),
        ],
        "faqs": [
            ("Why are workboats financed conservatively despite lasting so long?",
             "Because long life and liquidity are different things. A tug can "
             "work productively for decades, but the buyer pool is narrow, so "
             "selling one quickly means a substantial discount. Lenders price "
             "the slow sale, not the long life."),
            ("Do I need a contract in place to finance a workboat?",
             "Not always, but it changes the terms substantially. Because the "
             "asset sells slowly, contracted employment is what carries the "
             "file. Buying speculatively into a soft market usually means lower "
             "leverage and a shorter term."),
            ("Can I finance a repower rather than a purchase?",
             "Yes, and it is a large share of lending in this segment because "
             "hulls outlast machinery. Lenders distinguish work that extends the "
             "vessel's life and value from routine maintenance, and fund the "
             "former against an itemised yard quote."),
            ("Does the offshore cycle affect my application?",
             "For offshore-exposed vessels, considerably. The same vessel and "
             "operator face a harder valuation conversation in a downturn than "
             "in a strong market, because the lender is assessing what it could "
             "recover in the conditions that would exist if things went wrong."),
            ("What survey do I need?",
             "An accredited condition and valuation survey from a surveyor "
             "experienced with commercial workboats specifically. A yacht "
             "surveyor and a workboat surveyor are not interchangeable, and "
             "lenders in this segment know the difference."),
        ],
        "related": [
            ("/commercial-marine-financing.html", "Commercial marine financing"),
            ("../commercial-vessel-loan-requirements/",
             "Commercial vessel loan requirements"),
            ("../marine-survey-what-lenders-require/",
             "What a marine survey covers"),
            ("/equipment-appraisal.html", "Equipment appraisal"),
        ],
        "sources": [USCG_NVDC, SLOOS, SBCS],
    },
]
