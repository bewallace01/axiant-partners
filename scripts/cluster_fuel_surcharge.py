# -*- coding: utf-8 -*-
"""Fuel surcharges and owner-operator margins - rewrite, daily batch 2026-11-13.

The page was 369 words (pagehealth thin list) with no Quick Answer, FAQ, table or sources,
and a title asking what financing "Axiant offers". Search Console since Aug 1 shows 1
impression ("looking for companies that offer fuel advances for trucking business"), so the
rewrite aims at the question the URL asks: why the fuel surcharge does not cover the fuel
bill, and how to fund the gap. It is scoped away from fuel-advance-cash-crunch (which is
about fuel advances on a load) and ifta-quarterly-tax-bill-cash-crunch, and links to both.
Same URL; date_published keeps 2026-03-23.

Facts: EIA publishes the weekly U.S. on-highway diesel price that most surcharge tables
key off (eia.gov/petroleum/gasdiesel). 49 CFR 376.12(d), (g) and (h) read from the CFR
text (Cornell LII): compensation stated in the lease, a rated freight bill when pay is a
percentage of revenue, charge-backs itemized with how each is computed. The surcharge
formula (current price - base price) / mpg is the common method, described as common,
not universal. The worked example uses stated assumptions and was computed by script.
Factoring 1-5% per invoice and 80-95% advances, LOC 8-13% bank / 14-30%+ online: the
site's published ranges. No named lenders.
"""
from cluster_table import table

EIA = ("https://www.eia.gov/petroleum/gasdiesel/", "EIA: Gasoline and Diesel Fuel Update",
       "The weekly U.S. and regional on-highway diesel prices most fuel surcharge tables use.")
CFR_376 = ("https://www.law.cornell.edu/cfr/text/49/376.12", "49 CFR 376.12: Written lease requirements",
           "Truth-in-leasing rules: compensation, rated freight bills and charge-backs for leased owner-operators.")
FMCSA = ("https://www.fmcsa.dot.gov/regulations/title49/part/376", "FMCSA: Part 376, Lease and Interchange of Vehicles",
         "FMCSA's copy of the leasing regulations that govern owner-operator agreements.")

CLUSTER = {
    "pillar": "trucking-business-financing.html",
    "hub": "trucking-business-financing",
    "no_hub": True,
    "back_href": "/trucking-business-financing.html",
    "crumb": "Trucking Financing",
    "cta_inline": "Tell us your lanes, your fuel bill and how you get paid",
    "cta_button": "Get Matched for Trucking Financing",
}

ARTICLES = [{
    "slug": "fuel-surcharges-killing-margins-financing-owner-operators",
    "date_published": "2026-03-23",
    "crumb": "Fuel Surcharges and Margins",
    "title": "Fuel Surcharge Not Covering Diesel? Owner-Operator Fixes",
    "og_title": "Why Your Fuel Surcharge Doesn't Cover Your Diesel Bill, and How to Fund the Gap",
    "h1": "Why Your Fuel Surcharge Doesn&rsquo;t Cover Your Diesel Bill, and How to Fund the Gap",
    "headline": "Why Your Fuel Surcharge Doesn't Cover Your Diesel Bill, and How to Fund the Gap",
    "lede": "How surcharge tables are calculated, the four places the money leaks, a worked "
            "example by diesel price, and the financing that fits each leak",
    "meta_desc": "Why fuel surcharges fall short for owner-operators: base price, mpg divisor, "
                 "unpaid deadhead and lag. Worked example and how to fund the fuel gap.",
    "article_desc": "How trucking fuel surcharges are calculated, why they rarely cover an owner-"
                    "operator's full fuel cost, and which financing fits the gap.",
    "keywords": "fuel surcharge owner operator, fuel surcharge not covering fuel, fuel surcharge "
                "calculation trucking, owner operator fuel costs financing, diesel prices trucking margins",
    "quick_answer": "As of November 2026, most fuel surcharges pay (diesel price minus a base "
                    "price) divided by an assumed mpg, on loaded miles only. Unpaid deadhead, a "
                    "truck that gets fewer miles per gallon than the formula, and a week of lag "
                    "leave a gap: in the example on this page about <strong>$470 a month</strong> "
                    "at <strong>$3.75 diesel</strong>. Fix the contract first, then fund the timing "
                    "with factoring or a line of credit. Axiant Partners, a business-loan broker in "
                    "Boca Raton, matches owner-operators with lenders. Typical ranges, not a quote.",
    "sections": [
        ("How a Fuel Surcharge Is Calculated",
         "<p>A fuel surcharge (FSC) is meant to move the cost of diesel above a set level from the "
         "carrier to the shipper. The common formula is:</p>"
         "<p><strong>FSC per mile = (current diesel price &minus; base price) &divide; mpg "
         "divisor</strong></p>"
         "<ul>"
         "<li><strong>Current price</strong> is usually the "
         "<a href=\"https://www.eia.gov/petroleum/gasdiesel/\" rel=\"noopener nofollow\" target=\"_blank\">EIA "
         "weekly on-highway diesel average</a>, national or regional, published each week.</li>"
         "<li><strong>Base price</strong> is the diesel price already built into the line-haul "
         "rate. Below it, no surcharge is paid.</li>"
         "<li><strong>Mpg divisor</strong> is the fuel economy the table assumes. A divisor of 6.0 "
         "pays for 6 miles per gallon whether your truck gets 5.5 or 7.</li>"
         "</ul>"
         "<p>Each shipper, broker and carrier sets its own base, divisor and index, so two loads "
         "on the same day can carry very different surcharges.</p>"),
        ("Four Reasons the Surcharge Falls Short",
         "<ol>"
         "<li><strong>Deadhead isn&rsquo;t paid.</strong> The surcharge is paid on loaded or "
         "billed miles. Fuel burned driving empty to the next pickup comes out of your rate.</li>"
         "<li><strong>Your mpg is below the divisor.</strong> Heavy loads, mountains, idling and an "
         "older engine all cut real fuel economy. Every tenth of a mpg below the divisor is fuel "
         "you buy and aren&rsquo;t paid for.</li>"
         "<li><strong>Lag.</strong> A weekly index trails the pump. When diesel climbs fast you pay "
         "this week&rsquo;s price and are reimbursed on last week&rsquo;s.</li>"
         "<li><strong>All-in rates.</strong> On many spot loads the surcharge is folded into one "
         "rate per mile. When diesel rises after you book, nothing adjusts.</li>"
         "</ol>"
         "<p>On top of those, the cash timing: you pay for fuel at the pump, and the freight bill "
         "that carries the surcharge may not pay for 30 days or more. See "
         "<a href=\"/trucking-business-financing/broker-net-30-net-45-cash-gap/\">the net-30 cash "
         "gap</a>.</p>"),
        ("Worked Example: The Gap at Three Diesel Prices",
         "<p><strong>Illustrative assumptions, not a quote.</strong> An owner-operator runs 10,000 "
         "loaded and 1,500 empty miles a month at 6.2 mpg. The surcharge table uses a $1.25 base "
         "and a 6.0 divisor, paid on loaded miles. That is about 1,855 gallons a month.</p>"
         + table(["Diesel price", "FSC per loaded mile", "Fuel cost above base", "Surcharge paid", "Monthly gap"], [
             ["$3.25", "$0.333", "$3,710", "$3,333", "$376"],
             ["$3.75", "$0.417", "$4,637", "$4,167", "$470"],
             ["$4.25", "$0.500", "$5,565", "$5,000", "$565"],
         ])
         + "<p>The gap grows with the price because the unpaid deadhead gallons get more expensive. "
         "Over a year at $3.75 it is about <strong>$5,600</strong>, before any lag or all-in "
         "loads. The total fuel bill in this example is about $6,956 a month at $3.75, paid weeks "
         "before the loads that carry the surcharge settle.</p>"),
        ("Fix the Contract Before You Finance the Gap",
         "<ul>"
         "<li><strong>Ask for the table in writing</strong>: base price, divisor, index (national or "
         "regional) and the day of the week it resets.</li>"
         "<li><strong>Quote spot loads with a separate FSC</strong>, or price the all-in rate off "
         "today&rsquo;s diesel, not last month&rsquo;s.</li>"
         "<li><strong>Cut deadhead</strong> with backhauls and lane planning; it is the biggest "
         "unpaid line. See <a href=\"/trucking-business-financing/deadhead-miles-cash-drain/\">deadhead "
         "miles</a>.</li>"
         "<li><strong>If you are leased on</strong>, federal truth-in-leasing rules apply. "
         "<a href=\"https://www.law.cornell.edu/cfr/text/49/376.12\" rel=\"noopener nofollow\" "
         "target=\"_blank\">49 CFR 376.12</a> requires your pay to be stated in the lease, gives you "
         "a copy of the rated freight bill when you are paid a percentage of the load&rsquo;s "
         "revenue, and requires charge-backs to be itemized with how each is computed. That is how "
         "you check whether the surcharge the shipper paid reached you.</li>"
         "</ul>"),
        ("Financing That Fits the Fuel Gap",
         "<p>Financing doesn&rsquo;t close a pricing gap; it carries the timing while you fix it. "
         "Ranges are the ones the site publishes, typical and not quotes.</p>"
         + table(["Option", "Typical cost", "Fits"], [
             ["Freight factoring with fuel advance", "About 1-5% per invoice; 80-95% advanced",
              "You wait 30+ days on brokers and shippers"],
             ["Business line of credit", "8-13% APR at banks; 14-30%+ online",
              "Fuel price spikes and slow weeks, drawn and repaid"],
             ["Equipment refinance or truck title loan", "Priced on the truck's equity",
              "A one-time cash need when you own the truck"],
             ["Merchant cash advance", "Factor 1.15-1.50", "Rarely: it adds a daily debit to a fuel problem"],
         ])
         + "<p>More on each: <a href=\"/trucking-business-financing/fuel-advance-cash-crunch/\">fuel "
         "advances and the cash crunch</a>, <a href=\"/invoice-factoring.html\">invoice factoring</a>, "
         "<a href=\"/working-capital-loans/articles/freight-broker-financing/\">freight financing</a> and "
         "<a href=\"/commercial-truck-title-loan.html\">semi truck title loans</a>. If the quarterly "
         "fuel tax is the problem, see <a href=\"/trucking-business-financing/ifta-quarterly-tax-bill-cash-crunch/\">"
         "the IFTA cash crunch</a>.</p>"),
        ("What Lenders Look at on an Owner-Operator File",
         "<ul>"
         "<li><strong>Settlement statements and bank deposits</strong>, commonly three to six "
         "months, showing steady loads.</li>"
         "<li><strong>Your operating authority</strong> or lease agreement and how long you have run "
         "under it.</li>"
         "<li><strong>Who your customers are</strong>: factoring companies price on the brokers&rsquo; "
         "and shippers&rsquo; credit, not only yours.</li>"
         "<li><strong>Fuel cards and existing advances</strong> already drawing on settlements.</li>"
         "<li><strong>The truck</strong>: year, mileage and what is owed, if you borrow against it.</li>"
         "</ul>"
         "<p>Ready to compare? <a href=\"/match.html\">Get matched with lenders that fund "
         "owner-operators</a>, or start from <a href=\"/trucking-business-financing.html\">trucking "
         "business financing</a>.</p>"),
    ],
    "faqs": [
        ("Why doesn't my fuel surcharge cover my fuel cost?",
         "Because it is usually paid on loaded miles only, assumes an mpg your truck may not get, "
         "and trails the pump by up to a week. In the example on this page those leaks add up to "
         "about $470 a month at $3.75 diesel."),
        ("How is a trucking fuel surcharge calculated?",
         "Commonly as (current diesel price minus a base price) divided by an mpg divisor, paid per "
         "mile. The current price is usually the EIA weekly on-highway diesel average."),
        ("Do I get a fuel surcharge on deadhead miles?",
         "Usually not. Surcharges are paid on loaded or billed miles, so fuel burned running empty "
         "is a cost you carry unless the rate covers it."),
        ("Can a leased owner-operator see what fuel surcharge the shipper paid?",
         "If you are paid a percentage of the load's revenue, 49 CFR 376.12 requires the carrier to "
         "give you a copy of the rated freight bill, and lets you examine the documents rates are "
         "computed from."),
        ("What is the best financing for high fuel costs?",
         "For timing, freight factoring with a fuel advance or a business line of credit. Factoring "
         "typically costs about 1-5% per invoice; a line commonly runs 8-13% APR at a bank. Typical "
         "ranges, not a quote."),
        ("Should an owner-operator use a merchant cash advance for fuel?",
         "Rarely. A factor of 1.15-1.50 repaid by daily debits adds a fixed payment to a business "
         "whose problem is already cash timing."),
    ],
    "related": [
        ("/trucking-business-financing/fuel-advance-cash-crunch/", "Fuel advances and the cash crunch"),
        ("/trucking-business-financing/deadhead-miles-cash-drain/", "Deadhead miles cash drain"),
        ("/trucking-business-financing/ifta-quarterly-tax-bill-cash-crunch/", "IFTA quarterly tax bill"),
        ("/trucking-business-financing/broker-net-30-net-45-cash-gap/", "Broker net-30 and net-45 cash gap"),
        ("/trucking-business-financing.html", "Trucking business financing"),
        ("/match.html", "Get matched with lenders"),
    ],
    "sources": [EIA, CFR_376, FMCSA],
}]
