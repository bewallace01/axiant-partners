# -*- coding: utf-8 -*-
"""Drone cluster, article 4."""

from cluster_drone import FAA_COMM, SBA_7A, SBCS, SLOOS

MORE = [
    {
        "slug": "lidar-and-payload-financing",
        "crumb": "LiDAR and Payload Financing",
        "title": "LiDAR and Payload Financing | Axiant Partners",
        "og_title": "LiDAR and Payload Financing: The Expensive Half of a Drone",
        "h1": "LiDAR and Payload Financing",
        "headline": "LiDAR and Payload Financing",
        "lede": "When the sensor costs several times the aircraft, the sensor "
                "is the deal",
        "meta_desc": "How LiDAR and drone payloads are financed: why sensors "
                     "carry the collateral value, how they are appraised, and "
                     "which structures fit a payload purchase.",
        "article_desc": "Financing the sensor rather than the airframe, and why "
                        "lenders treat the two differently.",
        "keywords": "lidar financing, drone payload financing, survey sensor "
                    "equipment loan, thermal camera financing",
        "quick_answer": "Payloads finance better than airframes. A survey-grade "
                        "LiDAR unit can cost <strong>several times the aircraft "
                        "carrying it</strong>, holds value considerably longer, "
                        "and has an identifiable resale market. That makes it "
                        "recognizable collateral, so a payload purchase is often "
                        "structured as ordinary equipment finance where the "
                        "drone alone would not be.",
        "sections": [
            ("The Sensor Is the Asset",
             "<p>Operators consistently describe their spending in the wrong "
             "order. They say they are buying a drone, and mention the sensor "
             "second.</p>"
             "<p>Financially it is the reverse. A survey-grade LiDAR unit, a "
             "calibrated multispectral array or a high-end thermal payload "
             "frequently accounts for most of the invoice. It is serialized, "
             "identifiable, sold through a known dealer network, and does not "
             "become obsolete the moment a new airframe is announced. Every one "
             "of those characteristics is what an equipment lender is looking "
             "for.</p>"
             "<p>Present the purchase accordingly. A request framed as a sensor "
             "acquisition with an airframe attached reads very differently from "
             "one framed as a drone purchase with accessories.</p>"),
            ("How Payload Types Compare",
             '<div class="table-wrap"><table style="width:100%">'
             "<thead><tr><th>Payload</th><th>Typical use</th>"
             "<th>Collateral character</th></tr></thead><tbody>"
             '<tr><td data-label="Payload">Survey-grade LiDAR</td>'
             '<td data-label="Use">Topography, corridor mapping, '
             "volumetrics</td>"
             '<td data-label="Character">Strongest; high value, real resale '
             "market</td></tr>"
             '<tr><td data-label="Payload">Photogrammetry cameras</td>'
             '<td data-label="Use">Mapping, construction progress</td>'
             '<td data-label="Character">Good; widely used, easy to '
             "value</td></tr>"
             '<tr><td data-label="Payload">Thermal / radiometric</td>'
             '<td data-label="Use">Utility, solar, roofing, emergency '
             "response</td>"
             '<td data-label="Character">Moderate; specialist buyers</td></tr>'
             '<tr><td data-label="Payload">Multispectral</td>'
             '<td data-label="Use">Agriculture, vegetation health</td>'
             '<td data-label="Character">Moderate; narrower market</td></tr>'
             '<tr><td data-label="Payload">Gas detection</td>'
             '<td data-label="Use">Pipeline and facility inspection</td>'
             '<td data-label="Character">Moderate; contract-driven '
             "demand</td></tr>"
             '<tr><td data-label="Payload">Gimbals and mounts</td>'
             '<td data-label="Use">Carrying everything above</td>'
             '<td data-label="Character">Weak alone; bundle with the '
             "sensor</td></tr>"
             "</tbody></table></div>"
             "<p>The pattern is that the more a payload is tied to "
             "infrastructure work rather than imagery, the more predictable its "
             "second-hand demand and the better it secures a loan.</p>"),
            ("Calibration, Software and What Travels With the Unit",
             "<p>A LiDAR sensor is not a self-contained object, and lenders who "
             "know the category ask about the parts that travel with it.</p>"
             "<p>Calibration certificates, the processing software license, the "
             "RTK or PPK base that gives the data its accuracy, and the "
             "manufacturer support agreement all affect what the unit is worth "
             "to the next buyer. A sensor sold without its calibration history "
             "or with a non-transferable software license is materially less "
             "valuable than the same hardware sold complete.</p>"
             "<p>Keep the documentation together from the day of purchase. It "
             "protects the resale value you are asking a lender to rely on, and "
             "it is the sort of detail that quietly signals a well-run "
             "operation.</p>"),
            ("Structures That Fit a Payload Purchase",
             "<p>Because the sensor behaves like conventional equipment, the "
             "conventional structures are available.</p>"
             "<p><strong>Equipment finance</strong> is the usual route: a term "
             "matched roughly to the useful life, the sensor as security, and "
             "payments that the contracted work covers. <strong>Leasing</strong> "
             "suits operators who expect to replace the unit as the technology "
             "moves, and it keeps the upgrade decision open. <strong>SBA "
             "lending</strong> fits where the purchase sits inside a broader "
             "expansion, with the "
             '<a href="https://www.sba.gov/funding-programs/loans/7a-loans" '
             'rel="noopener nofollow" target="_blank">7(a) program</a> the '
             "common starting point.</p>"
             "<p>What rarely fits is short-term working capital. Paying for a "
             "long-lived sensor out of a facility repaid in months puts the "
             "cost in one year and the benefit across several, which is the "
             "mismatch that strands otherwise healthy operators.</p>"),
            ("Making the Case for a Payload",
             "<ul>"
             "<li><strong>Quote the sensor and the airframe separately</strong> "
             "so the value is visible.</li>"
             "<li><strong>Name the work it enables</strong> &mdash; contracts, "
             "bids or a client that has asked for the capability.</li>"
             "<li><strong>Match the term to the sensor's life</strong>, not to "
             "the aircraft's.</li>"
             "<li><strong>Keep calibration and license documentation</strong> "
             "with the unit.</li>"
             "<li><strong>Show what it replaces</strong> if you currently "
             "subcontract the capability.</li>"
             "</ul>"
             '<p>See <a href="/equipment-appraisal.html">equipment appraisal</a> '
             "for how a sensor package is valued, or "
             '<a href="../drone-fleet-financing-inspection-surveying/">fleet '
             "financing</a> where several payloads are bundled into one "
             "facility.</p>"),
        ],
        "faqs": [
            ("Can I finance a LiDAR unit on its own?",
             "Yes, and it is often easier than financing the aircraft. A "
             "survey-grade sensor is serialized, valuable and resaleable, which "
             "makes it recognizable collateral in a way that a commercial "
             "airframe usually is not."),
            ("Why do payloads hold value better than drones?",
             "They are not superseded on the same cycle. A new airframe "
             "generation arrives frequently and pushes the old one down, while "
             "a calibrated survey sensor stays useful and saleable across "
             "several airframe generations."),
            ("What documentation affects a sensor's value?",
             "Calibration certificates, a transferable processing software "
             "license, the matching RTK or PPK base, and manufacturer support "
             "records. The same hardware is worth materially less sold without "
             "them."),
            ("Should I lease or buy a payload?",
             "Buy where the capability is stable and the work is contracted; "
             "lease where you expect the technology to move and want the "
             "upgrade decision open. The deciding factor is usually how fast "
             "your clients' accuracy expectations are rising."),
            ("Is working capital a reasonable way to buy a sensor?",
             "Rarely. A facility repaid over months against an asset earning "
             "over years puts the whole cost in one period, and that mismatch "
             "strands operators whose underlying business is sound."),
        ],
        "related": [
            ("/drone-financing.html", "Drone financing"),
            ("../drone-fleet-financing-inspection-surveying/",
             "Drone fleet financing for inspection and surveying"),
            ("../part-107-operator-equipment-financing/",
             "Part 107 operator equipment financing"),
            ("/equipment-appraisal.html", "Equipment appraisal"),
        ],
        "sources": [SBA_7A, FAA_COMM, SLOOS],
    },
]
