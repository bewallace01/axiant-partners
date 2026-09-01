# -*- coding: utf-8 -*-
"""Batch 1 content — construction / heavy-equipment niches. All hand-authored, unique."""

TO = '<table style="width:100%; border-collapse: collapse; margin: 1.5rem 0;"><thead><tr style="background: var(--bg-card);">'
def _th(h): return f'<th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">{h}</th>'
def _td(c): return f'<td style="padding: 12px 16px; border: 1px solid var(--border-color);">{c}</td>'
def tbl(headers, rows):
    s = TO + "".join(_th(h) for h in headers) + "</tr></thead><tbody>"
    for r in rows:
        s += "<tr>" + "".join(_td(c) for c in r) + "</tr>"
    return s + "</tbody></table>"

EQ_COMMON = [
    ("/equipment-financing.html", "Equipment Financing Hub"),
    ("../equipment-financing-requirements/", "Equipment Financing Requirements"),
    ("../section-179-tax-strategy-2026/", "Section 179 Tax Strategy"),
    ("../can-you-finance-used-equipment/", "Can You Finance Used Equipment?"),
    ("../equipment-financing-vs-sba-loan/", "Equipment Financing vs SBA Loan"),
    ("/sba-loans/articles/sba-504-vs-7a-decision-tree/", "SBA 504 vs 7(a)"),
]

PAGES = []

# ============================================================ 1. GENERATOR
PAGES.append({
 "slug":"commercial-generator-financing",
 "breadcrumb":"Commercial Generator Financing",
 "title":"Commercial Generator Financing (2026) | Axiant",
 "meta":"Commercial generator financing: standby & backup power units cost $10K–$1M+. Equipment loans, SBA, and Section 179 for healthcare, data centers, and grocery.",
 "og_title":"Commercial Generator Financing (2026)",
 "og_desc":"Finance standby and backup power generators: diesel and natural-gas units, automatic transfer switches, and installation. Equipment loans, SBA 7(a)/504, and Section 179.",
 "tw_desc":"Commercial generator financing: 100kW units $25K–$60K, 1MW+ $400K–$1M+. Equipment loans 8–13% APR, plus installation.",
 "schema_desc":"Financing for commercial standby and backup power generators, automatic transfer switches, and installation — by unit size, fuel type, and lender path.",
 "keywords":"commercial generator financing, standby generator financing, backup power financing, diesel generator loan, natural gas generator financing, automatic transfer switch financing",
 "h1":"Commercial Generator Financing: Standby &amp; Backup Power Systems",
 "tagline":"How businesses finance standby and backup power &mdash; what diesel and natural-gas generators, transfer switches, and installation cost, and which financing path fits",
 "quick_facts":"100kW unit $25K&ndash;$60K. 500kW $60K&ndash;$150K. 1MW+ $400K&ndash;$1M+. Installation often 50&ndash;100% of unit cost. Equipment loans 8&ndash;13% APR. SBA 504 for unit + electrical + install. Section 179 + bonus depreciation may apply.",
 "rail_cta_h":"Need backup power financing?",
 "rail_cta_p":"Get matched with equipment lenders and SBA banks that fund generators plus installation.",
 "cta_label":"Get Matched for Generator Financing",
 "quick_answer":"Commercial generator financing covers standby and backup power for facilities that can&rsquo;t afford to go dark. <strong>Unit cost by size</strong>: 20&ndash;60kW $10K&ndash;$30K; 100&ndash;150kW $25K&ndash;$60K; 250&ndash;500kW $60K&ndash;$150K; 750kW&ndash;1MW $150K&ndash;$400K; 1&ndash;2MW+ $400K&ndash;$1M+. <strong>Add the automatic transfer switch</strong> ($2K&ndash;$25K) and <strong>installation</strong> &mdash; electrical, pad, fuel, permitting &mdash; which often runs <strong>50&ndash;100% of the unit price</strong>. <strong>Financing paths</strong>: equipment loans (8&ndash;13% APR, 48&ndash;84 months) for the genset itself; SBA 7(a)/504 when you&rsquo;re bundling the unit with electrical work and install; manufacturer/dealer financing from Generac, Cummins, Kohler, and Caterpillar dealers. <strong>Section 179 and bonus depreciation</strong> often apply to qualifying standby units. All figures are illustrative estimates, not quotes.",
 "intro":"A backup generator is rarely an impulse purchase &mdash; it&rsquo;s bought because a power outage costs a business real money or, in healthcare, risks lives. That&rsquo;s also why generators finance well: lenders understand the asset holds value, serves a clear purpose, and is often required by code. The tricky part is that the generator is only half the project &mdash; the transfer switch, electrical tie-in, concrete pad, fuel system, and permitting frequently cost as much as the unit itself, and how you structure financing depends on whether you treat the whole thing as equipment or as a building improvement. For the broader hub, see <a href=\"/equipment-financing.html\">equipment financing</a>.",
 "sections":[
   {"id":"generator-costs","h2":"Commercial Generator Costs by Size",
    "body":tbl(["Generator size","Typical unit cost","Common use"],[
      ["Portable / light commercial (20&ndash;60kW)","$10K&ndash;$30K","Small retail, restaurants, offices"],
      ["100&ndash;150kW standby","$25K&ndash;$60K","Mid-size facilities, multi-tenant"],
      ["250&ndash;500kW","$60K&ndash;$150K","Grocery, cold storage, large clinics"],
      ["750kW&ndash;1MW","$150K&ndash;$400K","Hospitals, manufacturing, telecom"],
      ["1&ndash;2MW+ (paralleling sets)","$400K&ndash;$1M+","Data centers, campuses, utilities"],
      ["Automatic transfer switch (ATS)","$2K&ndash;$25K","Required to switch loads automatically"],
      ["Installation (electrical, pad, fuel, permit)","50&ndash;100% of unit","Often the larger line item"],
    ]) + "<p style=\"margin-top:1rem;\">Top manufacturers: Generac, Cummins, Kohler, Caterpillar, and MTU. Natural-gas units suit facilities with utility gas and tighter emissions rules; diesel suits remote sites and longer-runtime needs. Figures are illustrative ranges, not quotes &mdash; use the <a href=\"/calculator.html\">payment calculator</a> to estimate monthly cost.</p>"},
   {"id":"financing-paths","h2":"How to Finance a Commercial Generator",
    "body":"<ul>"
      "<li><strong>Equipment loan (8&ndash;13% APR, 48&ndash;84 months).</strong> The standard path for the genset and transfer switch when the unit is the main cost. 10&ndash;20% down is typical; strong credit and established businesses see less.</li>"
      "<li><strong>SBA 7(a) up to $5M.</strong> Best when the generator is part of a larger project &mdash; electrical upgrades, a new pad, fuel storage, or a facility build-out &mdash; because you can bundle equipment, installation labor, and working capital into one note.</li>"
      "<li><strong>SBA 504.</strong> Fits when the generator is permanently affixed to owned real estate and treated as a building system; 10% down, long amortization, blended rate. See <a href=\"/sba-loans/articles/sba-504-vs-7a-decision-tree/\">SBA 504 vs 7(a)</a>.</li>"
      "<li><strong>Manufacturer / dealer financing.</strong> Generac, Cummins, Kohler, and Cat dealers frequently offer in-house or captive financing, sometimes with promotional rates on the unit (installation usually financed separately).</li>"
      "<li><strong>$1-buyout or FMV lease.</strong> Useful for preserving cash; a $1-buyout lease keeps the asset on your books for depreciation, while an FMV lease lowers payments if you expect to upgrade.</li>"
      "</ul>"},
   {"id":"why-businesses-finance","h2":"Why Businesses Finance Backup Power",
    "body":"<ul>"
      "<li><strong>Code and life-safety requirements.</strong> Hospitals, surgery centers, and many senior-care facilities are required to maintain emergency power under NFPA 110; the generator isn&rsquo;t optional, so financing spreads a mandatory cost.</li>"
      "<li><strong>Outage cost.</strong> Grocery and cold storage lose inventory in hours; data centers and telecom lose revenue and SLAs by the minute. The monthly payment is usually a fraction of a single avoided outage.</li>"
      "<li><strong>Preserving cash.</strong> A six-figure power project drains reserves that owners would rather keep for operations; financing converts it to a predictable monthly cost.</li>"
      "<li><strong>Tax treatment.</strong> Qualifying standby generators may be eligible for <a href=\"../section-179-tax-strategy-2026/\">Section 179</a> expensing and bonus depreciation &mdash; confirm with your CPA, since permanently-affixed building systems are treated differently than portable units.</li>"
      "</ul>"},
   {"id":"lender-scrutiny","h2":"What Lenders Look At",
    "body":"<ul>"
      "<li><strong>Equipment vs. real-property classification.</strong> A portable or skid-mounted genset is clean equipment collateral. A permanently-installed unit wired into a building may be treated as a fixture &mdash; which can push the deal toward SBA 504 or a real-estate-secured structure.</li>"
      "<li><strong>Installation share.</strong> When install exceeds the unit cost, lenders want a contractor quote separating hard equipment from soft costs, because labor is weaker collateral than the genset.</li>"
      "<li><strong>Time in business and cash flow.</strong> Standard <a href=\"../equipment-financing-requirements/\">equipment financing requirements</a> apply &mdash; most lenders want 2+ years and clean recent bank statements; newer businesses can still qualify with stronger down payments.</li>"
      "<li><strong>Fuel and permitting timeline.</strong> Diesel storage and emissions permits can delay commissioning; lenders may stage funding to install milestones.</li>"
      "</ul>"},
   {"id":"next-step","h2":"Next Step",
    "body":"<p><a href=\"/match.html\">Get matched with generator equipment lenders and SBA banks</a> that fund the unit plus installation. See also <a href=\"../equipment-financing-vs-sba-loan/\">equipment financing vs SBA loan</a> and <a href=\"../how-fast-can-equipment-financing-be-approved/\">how fast equipment financing can be approved</a>.</p>"},
 ],
 "faqs":[
   ("How much does a commercial standby generator cost?","Illustrative ranges: 20&ndash;60kW $10K&ndash;$30K; 100&ndash;150kW $25K&ndash;$60K; 250&ndash;500kW $60K&ndash;$150K; 750kW&ndash;1MW $150K&ndash;$400K; 1&ndash;2MW+ $400K&ndash;$1M+. Add an automatic transfer switch ($2K&ndash;$25K) and installation, which often runs 50&ndash;100% of the unit price. These are estimates, not quotes."),
   ("Can I finance generator installation, not just the unit?","Yes. Equipment loans typically cover the genset and transfer switch; when electrical work, a concrete pad, fuel storage, and permitting are significant, an SBA 7(a) loan lets you bundle equipment, installation labor, and working capital into one note."),
   ("Does Section 179 apply to a commercial generator?","Qualifying standby generators may be eligible for Section 179 expensing and bonus depreciation, but permanently-affixed units wired into a building are sometimes treated as real property and depreciated differently. Confirm treatment with your CPA."),
   ("What credit score do I need to finance a generator?","Most equipment lenders look for 600&ndash;650+ FICO with 2+ years in business; SBA programs generally want 680+. Newer businesses or thinner files can still qualify with a larger down payment or by financing through a dealer captive program."),
   ("Should I use an equipment loan or an SBA loan for backup power?","Use an equipment loan when the generator is the main cost and you want speed. Use SBA 7(a)/504 when the generator is part of a larger electrical or facility project and you want to bundle install and working capital over a longer term."),
 ],
 "howto_name":"How to finance a commercial generator",
 "howto_desc":"Five steps to finance a standby or backup power generator and its installation.",
 "howto_steps":[
   ("Get an itemized quote separating unit, ATS, and installation","Ask your Generac, Cummins, Kohler, or Cat dealer for a quote that breaks out the genset, transfer switch, electrical, pad, fuel, and permitting so the lender can see equipment vs. soft costs."),
   ("Decide equipment loan vs. SBA","If the unit is the main cost and you want speed, choose an equipment loan. If electrical and install are large or it&rsquo;s part of a build-out, choose SBA 7(a) or 504."),
   ("Confirm classification with your CPA","Determine whether the unit is portable equipment or a permanently-affixed building system &mdash; this affects collateral, loan type, and Section 179 / depreciation treatment."),
   ("Apply with business financials and the contractor quote","Provide 2+ years of returns or bank statements plus the itemized install quote. Stronger files get lower down payments."),
   ("Stage funding to install milestones","For larger projects, lenders may release funds against delivery, install, and commissioning milestones, especially when permitting or fuel storage adds time."),
 ],
 "related":EQ_COMMON,
})

# ============================================================ 2. TELEHANDLER
PAGES.append({
 "slug":"telehandler-financing",
 "breadcrumb":"Telehandler Financing",
 "title":"Telehandler Financing (2026) | Axiant Partners",
 "meta":"Telehandler financing: compact units $50K–$80K, high-reach $140K–$250K, rotating telehandlers $200K–$400K. Equipment loans, leases, and Section 179.",
 "og_title":"Telehandler Financing (2026)",
 "og_desc":"Finance telescopic handlers for construction and agriculture: compact, high-capacity, and rotating telehandlers. Equipment loans, leases, captive financing, and Section 179.",
 "tw_desc":"Telehandler financing: compact $50K–$80K, mid 8–10K lb $90K–$130K, rotating $200K–$400K. Loans 7–12% APR, used finances well.",
 "schema_desc":"Financing for telescopic handlers (telehandlers) in construction and agriculture — by lift capacity and reach, new vs. used, loan vs. lease.",
 "keywords":"telehandler financing, telescopic handler financing, JCB telehandler finance, rotating telehandler financing, used telehandler financing, construction equipment loan",
 "h1":"Telehandler Financing: Compact, High-Reach &amp; Rotating Models",
 "tagline":"How contractors and farms finance telescopic handlers &mdash; what telehandlers cost by capacity and reach, and how to structure a loan or lease",
 "quick_facts":"Compact (5&ndash;6K lb) $50K&ndash;$80K. Mid (8&ndash;10K lb) $90K&ndash;$130K. High-reach (12K+ lb) $140K&ndash;$250K. Rotating (roto) $200K&ndash;$400K. Loans 7&ndash;12% APR, 48&ndash;72 months. Used 30&ndash;50% less and finances well. Section 179 may apply.",
 "rail_cta_h":"Financing a telehandler?",
 "rail_cta_p":"Get matched with construction and ag equipment lenders for new or used telehandlers.",
 "cta_label":"Get Matched for Telehandler Financing",
 "quick_answer":"Telehandler financing covers telescopic handlers used across construction, framing, masonry, and agriculture. <strong>Cost by class</strong>: compact 5&ndash;6K lb capacity $50K&ndash;$80K; mid-range 8&ndash;10K lb $90K&ndash;$130K; high-capacity / high-reach 12K+ lb $140K&ndash;$250K; rotating &ldquo;roto&rdquo; telehandlers $200K&ndash;$400K. <strong>Financing paths</strong>: equipment loans (7&ndash;12% APR, 48&ndash;72 months, 10&ndash;20% down), $1-buyout or FMV leases, and manufacturer captive programs (JCB, Genie, JLG, CAT, Manitou, Bobcat). <strong>Used telehandlers</strong> run 30&ndash;50% below new and finance well up to roughly 8&ndash;10 model years with reasonable hours. <strong>Section 179</strong> expensing often applies. All figures are illustrative estimates, not quotes.",
 "intro":"A telehandler is one of the most versatile machines on a jobsite or farm &mdash; lift forks one hour, a bucket or work platform the next &mdash; which is exactly why it&rsquo;s a strong financing candidate: broad demand, deep used market, and predictable resale. The financing question usually comes down to capacity and reach (which drive price), new vs. used, and whether a loan or lease fits how long you&rsquo;ll keep the machine. For the broader hub, see <a href=\"/equipment-financing.html\">equipment financing</a>.",
 "sections":[
   {"id":"telehandler-costs","h2":"Telehandler Costs by Class",
    "body":tbl(["Class","Lift capacity / reach","Typical cost"],[
      ["Compact telehandler","5,000&ndash;6,000 lb, ~19 ft","$50K&ndash;$80K"],
      ["Mid-range","8,000&ndash;10,000 lb, ~42 ft","$90K&ndash;$130K"],
      ["High-capacity / high-reach","12,000 lb+, 44&ndash;55 ft","$140K&ndash;$250K"],
      ["Rotating (&ldquo;roto&rdquo;) telehandler","360&deg; rotation, 60&ndash;100+ ft","$200K&ndash;$400K"],
      ["Used (8&ndash;10 yr, moderate hours)","Varies by class","30&ndash;50% below new"],
    ]) + "<p style=\"margin-top:1rem;\">Leading makers: JCB, Genie, JLG, Caterpillar, Manitou, and Bobcat. Attachments &mdash; buckets, grapples, work platforms, truss booms &mdash; can be financed with the machine. Figures are illustrative ranges, not quotes.</p>"},
   {"id":"financing-paths","h2":"Loan vs. Lease for a Telehandler",
    "body":"<ul>"
      "<li><strong>Equipment loan (7&ndash;12% APR, 48&ndash;72 months).</strong> Best when you&rsquo;ll keep the machine long-term and want to build equity. 10&ndash;20% down is typical; established contractors with strong credit see less.</li>"
      "<li><strong>$1-buyout lease.</strong> Functions like a loan for tax and ownership purposes &mdash; you own the telehandler for a dollar at term end &mdash; and pairs well with Section 179.</li>"
      "<li><strong>FMV (fair-market-value) lease.</strong> Lower monthly payments and an easy upgrade path; good for fleets that cycle machines every few years.</li>"
      "<li><strong>Manufacturer captive financing.</strong> JCB Finance and other captives often run promotional rates or deferred-payment offers on new units; compare the all-in cost against an independent equipment lender.</li>"
      "<li><strong>Rental-purchase (RPO).</strong> Some dealers apply rental payments toward purchase &mdash; useful when you&rsquo;re unsure how long you&rsquo;ll need the machine.</li>"
      "</ul>"},
   {"id":"new-vs-used","h2":"New vs. Used Telehandlers",
    "body":"<p>The used telehandler market is deep, and lenders are comfortable with it. A well-maintained unit 8&ndash;10 years old with moderate hours typically finances at rates close to new, often with a 12-month term reduction. Because telehandlers hold value, used machines at 30&ndash;50% below new pricing can be the better cash-on-cash play for contractors who don&rsquo;t need the latest emissions tier or telematics. See <a href=\"../can-you-finance-used-equipment/\">can you finance used equipment</a> for how age and hours affect terms.</p>"},
   {"id":"lender-scrutiny","h2":"What Lenders Look At",
    "body":"<ul>"
      "<li><strong>Hours and model year</strong> on used machines &mdash; high hours shorten the term or raise the rate.</li>"
      "<li><strong>Capacity class</strong> &mdash; rotating telehandlers are higher-ticket and may need a larger down payment or appraisal.</li>"
      "<li><strong>Time in business and credit</strong> &mdash; standard <a href=\"../equipment-financing-requirements/\">equipment financing requirements</a>; 2+ years and 600&ndash;650+ FICO is a common bar, with newer businesses qualifying on stronger down payments.</li>"
      "<li><strong>Industry use</strong> &mdash; construction and agriculture are well-understood; specialty rental fleets may see fleet-level underwriting.</li>"
      "</ul>"},
   {"id":"next-step","h2":"Next Step",
    "body":"<p><a href=\"/match.html\">Get matched with telehandler lenders</a> for new or used machines. See also <a href=\"/sba-loans/articles/sba-504-vs-7a-decision-tree/\">SBA 504 vs 7(a)</a> for larger fleet purchases and <a href=\"../section-179-tax-strategy-2026/\">Section 179 tax strategy</a>.</p>"},
 ],
 "faqs":[
   ("How much does a telehandler cost?","Illustrative ranges: compact (5&ndash;6K lb) $50K&ndash;$80K; mid-range (8&ndash;10K lb) $90K&ndash;$130K; high-reach (12K+ lb) $140K&ndash;$250K; rotating telehandlers $200K&ndash;$400K. Used machines run 30&ndash;50% below new. These are estimates, not quotes."),
   ("Can you finance a used telehandler?","Yes. The used market is deep and lenders are comfortable with it. A well-maintained unit up to roughly 8&ndash;10 years old with moderate hours typically finances at rates close to new, sometimes with a slightly shorter term."),
   ("Is it better to lease or buy a telehandler?","Buy (loan or $1-buyout lease) if you&rsquo;ll keep it long-term and want equity and Section 179 benefits. Choose an FMV lease if you cycle machines every few years and prefer lower payments and an easy upgrade path."),
   ("Does Section 179 apply to telehandlers?","Telehandlers used in a trade or business generally qualify for Section 179 expensing and bonus depreciation. A $1-buyout lease or equipment loan keeps the asset on your books; confirm specifics with your CPA."),
   ("What credit and time in business do telehandler lenders want?","A common bar is 2+ years in business and 600&ndash;650+ FICO, though newer businesses qualify with a larger down payment. Rotating telehandlers, being higher-ticket, may require more documentation or an appraisal."),
 ],
 "howto_name":"How to finance a telehandler",
 "howto_desc":"Five steps to finance a new or used telescopic handler.",
 "howto_steps":[
   ("Pick capacity and reach for your work","Match lift capacity and reach to your tasks &mdash; compact for tight sites, high-reach for steel and framing, rotating for placement work. This sets the price band."),
   ("Decide new vs. used","Used machines 8&ndash;10 years old finance well at 30&ndash;50% below new; choose new for the latest emissions tier, telematics, or warranty."),
   ("Choose loan vs. lease","Loan or $1-buyout lease to own and depreciate; FMV lease for lower payments and frequent upgrades."),
   ("Compare captive vs. independent financing","Check JCB Finance or other manufacturer captives against an independent equipment lender for the lowest all-in cost."),
   ("Apply with financials and the equipment quote","Provide business returns or bank statements plus the dealer quote with hours and model year for used units."),
 ],
 "related":EQ_COMMON,
})

# ============================================================ 3. CRANE
PAGES.append({
 "slug":"crane-financing",
 "breadcrumb":"Crane Financing",
 "title":"Crane Financing (2026): Boom, Crawler &amp; Tower | Axiant",
 "meta":"Crane financing: boom trucks $150K–$500K, all-terrain $800K–$2M, crawler cranes $500K–$3M+. Heavy-equipment loans, leases, and specialty lenders.",
 "og_title":"Crane Financing (2026): Boom, Crawler &amp; Tower",
 "og_desc":"Finance mobile, rough-terrain, all-terrain, crawler, and tower cranes. Heavy-equipment loans and leases up to several million, with specialty lenders and appraisals.",
 "tw_desc":"Crane financing: boom truck $150K–$500K, all-terrain $800K–$2M, crawler $500K–$3M+. Heavy-equipment loans 60–84 months.",
 "schema_desc":"Financing for mobile, rough-terrain, all-terrain, crawler, and tower cranes — by crane type, value, and lender path including specialty heavy-equipment lenders.",
 "keywords":"crane financing, crane loan, boom truck crane financing, crawler crane financing, tower crane financing, all-terrain crane finance, heavy equipment financing",
 "h1":"Crane Financing: Boom, Rough-Terrain, Crawler &amp; Tower",
 "tagline":"How crane operators and contractors finance high-value lifting equipment &mdash; what each crane type costs and how heavy-equipment lenders structure the deal",
 "quick_facts":"Boom truck crane $150K&ndash;$500K. Rough-terrain $300K&ndash;$800K. All-terrain $800K&ndash;$2M. Crawler $500K&ndash;$3M+. Tower crane $300K&ndash;$1.5M. Loans/leases 60&ndash;84 months, larger down. Specialty heavy-equipment lenders; appraisals common above ~$500K.",
 "rail_cta_h":"Financing a crane?",
 "rail_cta_p":"Get matched with specialty heavy-equipment lenders that fund high-value crane purchases.",
 "cta_label":"Get Matched for Crane Financing",
 "quick_answer":"Crane financing is heavy-equipment financing at the high end of the value scale, so it leans on specialty lenders, appraisals, and longer terms. <strong>Cost by type</strong>: boom truck crane $150K&ndash;$500K; rough-terrain crane $300K&ndash;$800K; all-terrain crane $800K&ndash;$2M; crawler crane $500K&ndash;$3M+; tower crane $300K&ndash;$1.5M. <strong>Financing paths</strong>: equipment loans and leases (typically 60&ndash;84 months) up to several million through specialty heavy-equipment lenders; SBA caps at $5M and can work for smaller cranes but is often too small or slow for large units. <strong>Expect</strong> a larger down payment, an equipment appraisal above roughly $500K, and underwriting that weighs operator certification (NCCCO), machine age/hours, and your contract pipeline. Figures are illustrative estimates, not quotes.",
 "intro":"Cranes are among the highest-value assets a contractor finances, and the lending market reflects that: the machine is excellent collateral, but the size of the loan means underwriting is closer to commercial lending than a quick equipment approval. Whether you&rsquo;re adding a boom truck to a service fleet or a crawler for heavy lift work, the structure hinges on crane type, age, your operator credentials, and the work backing the purchase. For the broader hub, see <a href=\"/equipment-financing.html\">equipment financing</a>.",
 "sections":[
   {"id":"crane-costs","h2":"Crane Costs by Type",
    "body":tbl(["Crane type","Typical cost","Notes"],[
      ["Boom truck / mounted crane","$150K&ndash;$500K","Service work, mid-rise, fleet additions"],
      ["Rough-terrain crane","$300K&ndash;$800K","Off-road jobsites, confined access"],
      ["All-terrain crane","$800K&ndash;$2M","Road-legal plus jobsite mobility"],
      ["Crawler crane","$500K&ndash;$3M+","Heavy lift, infrastructure, longer setups"],
      ["Tower crane","$300K&ndash;$1.5M","High-rise construction (often rented)"],
    ]) + "<p style=\"margin-top:1rem;\">Leading makers: Grove, Liebherr, Tadano, Link-Belt, Manitowoc, and National Crane. A robust used market exists for boom trucks and rough-terrain units. Figures are illustrative ranges, not quotes.</p>"},
   {"id":"financing-paths","h2":"How Crane Financing Is Structured",
    "body":"<ul>"
      "<li><strong>Specialty heavy-equipment loans/leases.</strong> The primary path. Lenders that focus on cranes and heavy iron lend up to several million over 60&ndash;84 months and understand resale values by make and model.</li>"
      "<li><strong>SBA 7(a) up to $5M.</strong> Workable for smaller cranes (boom trucks, rough-terrain) bundled with working capital, but the $5M cap and slower timeline make it a poor fit for large all-terrain or crawler purchases.</li>"
      "<li><strong>$1-buyout vs. FMV lease.</strong> $1-buyout to own and depreciate; FMV to lower payments when you cycle equipment or take on a defined-length project.</li>"
      "<li><strong>Recourse and collateral.</strong> Given the loan size, expect a personal guarantee, a first lien on the crane, and possibly cross-collateral or an appraisal above ~$500K.</li>"
      "</ul>"},
   {"id":"used-and-appraisal","h2":"Used Cranes, Age &amp; Appraisal",
    "body":"<p>Cranes hold value for decades when maintained, so used units finance well &mdash; but the higher the value, the more the lender relies on a third-party appraisal rather than the invoice. Above roughly $500K, plan for an equipment appraisal and detailed maintenance and inspection records. Annual crane inspections and a clean history materially improve terms. For how age and hours move rates generally, see <a href=\"../can-you-finance-used-equipment/\">can you finance used equipment</a>.</p>"},
   {"id":"lender-scrutiny","h2":"What Lenders Look At",
    "body":"<ul>"
      "<li><strong>Operator certification (NCCCO)</strong> and a qualified crew &mdash; lenders want to know the machine will be operated and maintained properly.</li>"
      "<li><strong>Contract pipeline.</strong> Signed work or a backlog supports the payment; new entrants without a pipeline face more scrutiny.</li>"
      "<li><strong>Machine age, hours, and inspection history</strong> &mdash; central to high-value collateral and appraisal.</li>"
      "<li><strong>Balance sheet and guarantees.</strong> Because crane loans are large, underwriting weighs business financials and a personal guarantee more heavily than a small-ticket equipment deal. See <a href=\"../equipment-financing-vs-sba-loan/\">equipment financing vs SBA loan</a>.</li>"
      "</ul>"},
   {"id":"next-step","h2":"Next Step",
    "body":"<p><a href=\"/match.html\">Get matched with specialty heavy-equipment lenders</a> that fund cranes. See also <a href=\"../equipment-financing-requirements/\">equipment financing requirements</a> and <a href=\"../section-179-tax-strategy-2026/\">Section 179 tax strategy</a>.</p>"},
 ],
 "faqs":[
   ("How much does a crane cost?","Illustrative ranges: boom truck crane $150K&ndash;$500K; rough-terrain $300K&ndash;$800K; all-terrain $800K&ndash;$2M; crawler crane $500K&ndash;$3M+; tower crane $300K&ndash;$1.5M. These are estimates, not quotes, and vary by make, model, and condition."),
   ("Can you finance a crane with an SBA loan?","SBA 7(a) caps at $5M and can work for smaller cranes (boom trucks, rough-terrain) bundled with working capital. For large all-terrain or crawler cranes, specialty heavy-equipment lenders are usually a better fit on size and speed."),
   ("Do crane lenders require an appraisal?","Above roughly $500K, expect a third-party equipment appraisal plus detailed maintenance and annual-inspection records. The lender relies on independent value rather than the invoice for high-ticket collateral."),
   ("Can I finance a used crane?","Yes. Cranes hold value for decades when maintained, and the used market is active for boom trucks and rough-terrain units. Clean inspection history and maintenance records improve your terms."),
   ("What do crane lenders look for beyond credit?","Operator certification (NCCCO), a qualified crew, a contract pipeline backing the payment, machine age and hours, and business financials with a personal guarantee. Loan size pushes underwriting toward commercial-style review."),
 ],
 "howto_name":"How to finance a crane",
 "howto_desc":"Five steps to finance a boom truck, rough-terrain, all-terrain, crawler, or tower crane.",
 "howto_steps":[
   ("Match crane type to your work and pipeline","Choose the crane class for your jobs and confirm the contracts or backlog that will support the payment."),
   ("Gather machine records","For used cranes, pull maintenance logs and annual inspection history; above ~$500K, arrange a third-party appraisal."),
   ("Go to a specialty heavy-equipment lender","Crane-focused lenders understand resale by make/model and lend up to several million over 60&ndash;84 months."),
   ("Prepare financials and guarantee","Provide business financials; expect a first lien on the crane and a personal guarantee given the loan size."),
   ("Choose loan vs. lease and close","Pick a $1-buyout to own and depreciate or an FMV lease for lower payments, then close with proof of NCCCO-certified operators."),
 ],
 "related":EQ_COMMON,
})

# ============================================================ 4. CONCRETE PUMP / MIXER TRUCK
PAGES.append({
 "slug":"concrete-pump-mixer-truck-financing",
 "breadcrumb":"Concrete Pump &amp; Mixer Truck Financing",
 "title":"Concrete Pump &amp; Mixer Truck Financing (2026) | Axiant",
 "meta":"Concrete pump and mixer truck financing: line pumps $40K–$120K, boom pumps $300K–$1.2M, ready-mix mixer trucks $150K–$250K. Equipment & vocational-truck loans.",
 "og_title":"Concrete Pump &amp; Mixer Truck Financing (2026)",
 "og_desc":"Finance concrete boom pumps, line/trailer pumps, and ready-mix mixer trucks. Equipment loans, vocational-truck lenders, and on-road title considerations.",
 "tw_desc":"Concrete equipment financing: line pumps $40K–$120K, truck boom pumps $300K–$1.2M, mixer trucks $150K–$250K new.",
 "schema_desc":"Financing for concrete boom pumps, line and trailer pumps, and ready-mix mixer trucks — by equipment type, on-road vs. off-road, and lender path.",
 "keywords":"concrete pump financing, concrete mixer truck financing, ready-mix truck financing, boom pump financing, line pump financing, vocational truck loan",
 "h1":"Concrete Pump &amp; Mixer Truck Financing",
 "tagline":"How concrete contractors and ready-mix suppliers finance boom pumps, line pumps, and mixer trucks &mdash; costs by type and how titled vehicles change the deal",
 "quick_facts":"Trailer/line pump $40K&ndash;$120K. Truck-mounted boom pump (28&ndash;42m) $300K&ndash;$700K. Large boom (50m+) $700K&ndash;$1.2M. New ready-mix mixer truck $150K&ndash;$250K; used $50K&ndash;$120K. Equipment & vocational-truck loans, 48&ndash;72 months. Titled trucks need different docs than pumps.",
 "rail_cta_h":"Financing concrete equipment?",
 "rail_cta_p":"Get matched with equipment and vocational-truck lenders for pumps and mixer trucks.",
 "cta_label":"Get Matched for Concrete Equipment Financing",
 "quick_answer":"Concrete pump and mixer truck financing spans two collateral types &mdash; pumping equipment and on-road vocational trucks &mdash; which changes the paperwork. <strong>Cost by type</strong>: trailer/line pumps $40K&ndash;$120K; truck-mounted boom pumps (28&ndash;42m) $300K&ndash;$700K; large boom pumps (50m+) $700K&ndash;$1.2M; new ready-mix mixer trucks $150K&ndash;$250K; used mixers $50K&ndash;$120K. <strong>Financing paths</strong>: equipment loans and leases (48&ndash;72 months) for pumps, and vocational-truck lenders for mixer and boom-pump trucks, which are titled, on-road vehicles requiring DOT/registration documentation. <strong>Expect</strong> 10&ndash;20% down, CDL-qualified drivers, and underwriting that weighs mileage/hours and your ready-mix or pumping contract base. Figures are illustrative estimates, not quotes.",
 "intro":"Concrete is a cash-intensive, schedule-driven business: a single boom pump or a couple of mixer trucks can be the difference between bidding bigger pours or turning them down. Financing this equipment is straightforward once you separate the two asset types &mdash; pumps are clean equipment collateral, while mixer and boom-pump trucks are titled, on-road vehicles that vocational-truck lenders handle a little differently. For the broader hub, see <a href=\"/equipment-financing.html\">equipment financing</a>.",
 "sections":[
   {"id":"concrete-costs","h2":"Concrete Pump &amp; Mixer Truck Costs",
    "body":tbl(["Equipment","Typical cost","Notes"],[
      ["Trailer / line pump","$40K&ndash;$120K","Smaller pours, interior, high-rise line work"],
      ["Truck-mounted boom pump (28&ndash;42m)","$300K&ndash;$700K","Most common production boom pump"],
      ["Large boom pump (50m+)","$700K&ndash;$1.2M","High-reach, large commercial pours"],
      ["Ready-mix mixer truck (new)","$150K&ndash;$250K","Front- or rear-discharge"],
      ["Ready-mix mixer truck (used)","$50K&ndash;$120K","Strong used market"],
    ]) + "<p style=\"margin-top:1rem;\">Leading makers: Schwing, Putzmeister, and Alliance (pumps); McNeilus, Con-Tech, and Oshkosh (mixer bodies/trucks). Figures are illustrative ranges, not quotes.</p>"},
   {"id":"titled-vs-equipment","h2":"Titled Trucks vs. Pumping Equipment",
    "body":"<p>This is the detail that trips up first-time buyers. A <strong>trailer or stationary line pump</strong> is pure equipment collateral &mdash; financed like any other machine. A <strong>boom-pump truck or ready-mix mixer truck</strong> is a titled, on-road vehicle, so the lender needs DOT registration, the title, and proof of CDL-qualified drivers, and may treat it under a vocational-truck program rather than a generic equipment loan. The asset is the same value either way; the documentation and sometimes the lender differ. When you finance the chassis and the mixer body together, make sure the quote separates them so the lender can title correctly.</p>"},
   {"id":"financing-paths","h2":"Financing Paths",
    "body":"<ul>"
      "<li><strong>Equipment loan / lease (48&ndash;72 months).</strong> Standard for trailer and line pumps; 10&ndash;20% down, 8&ndash;13% APR depending on credit and age.</li>"
      "<li><strong>Vocational-truck lenders.</strong> For mixer trucks and boom-pump trucks, specialized commercial-truck lenders understand the chassis-plus-body structure and on-road titling.</li>"
      "<li><strong>$1-buyout vs. FMV lease.</strong> $1-buyout to own and depreciate; FMV for lower payments if you cycle trucks.</li>"
      "<li><strong>SBA 7(a)</strong> when bundling equipment with working capital for a growing ready-mix or pumping operation. See <a href=\"../equipment-financing-vs-sba-loan/\">equipment financing vs SBA loan</a>.</li>"
      "</ul>"},
   {"id":"lender-scrutiny","h2":"What Lenders Look At",
    "body":"<ul>"
      "<li><strong>Mileage and hours.</strong> Mixer trucks are judged on mileage and drum hours; pumps on pumping hours and boom condition.</li>"
      "<li><strong>CDL drivers and DOT compliance</strong> for titled trucks.</li>"
      "<li><strong>Contract base.</strong> Ready-mix supply agreements or a steady pumping schedule support the payment.</li>"
      "<li><strong>Standard credit and time in business</strong> &mdash; see <a href=\"../equipment-financing-requirements/\">equipment financing requirements</a>; newer operations qualify with larger down payments.</li>"
      "</ul>"},
   {"id":"next-step","h2":"Next Step",
    "body":"<p><a href=\"/match.html\">Get matched with concrete equipment and vocational-truck lenders</a>. See also <a href=\"../section-179-tax-strategy-2026/\">Section 179 tax strategy</a> and <a href=\"../can-you-finance-used-equipment/\">can you finance used equipment</a>.</p>"},
 ],
 "faqs":[
   ("How much does a concrete pump cost?","Illustrative ranges: trailer/line pumps $40K&ndash;$120K; truck-mounted boom pumps (28&ndash;42m) $300K&ndash;$700K; large boom pumps (50m+) $700K&ndash;$1.2M. These are estimates, not quotes."),
   ("How much does a ready-mix mixer truck cost?","A new ready-mix mixer truck typically runs $150K&ndash;$250K; used trucks run $50K&ndash;$120K depending on mileage, drum condition, and discharge type. These are illustrative figures."),
   ("Is a mixer truck financed as equipment or as a vehicle?","As a titled, on-road vehicle. Vocational-truck lenders handle the chassis-plus-mixer-body structure and require DOT registration, the title, and CDL-qualified drivers — unlike a stationary line pump, which is pure equipment collateral."),
   ("Can I finance a used concrete pump or mixer truck?","Yes. Both have active used markets. Pumps are judged on pumping hours and boom condition; mixer trucks on mileage and drum hours. Clean maintenance records improve terms."),
   ("What down payment is typical for concrete equipment?","Around 10&ndash;20% is common, lower for established contractors with strong credit and a steady contract base. Newer operations can offset thinner history with a larger down payment."),
 ],
 "howto_name":"How to finance concrete pumps and mixer trucks",
 "howto_desc":"Five steps to finance concrete pumping equipment and ready-mix mixer trucks.",
 "howto_steps":[
   ("Separate pumps from titled trucks","Identify which items are equipment (line/trailer pumps) and which are titled on-road vehicles (boom-pump trucks, mixer trucks) — they take different lenders and documents."),
   ("Get an itemized quote (chassis vs. body)","For trucks, ask the dealer to break out chassis and mixer/pump body so the lender can title and collateralize correctly."),
   ("Choose the right lender","Use an equipment lender for pumps and a vocational-truck lender for mixer and boom-pump trucks."),
   ("Document drivers and contracts","Provide CDL driver info, DOT registration for trucks, and ready-mix or pumping agreements that support the payment."),
   ("Pick loan vs. lease and close","Choose $1-buyout to own and depreciate or FMV for lower payments, then close with 10&ndash;20% down."),
 ],
 "related":EQ_COMMON,
})

# ============================================================ 5. ASPHALT / PAVING
PAGES.append({
 "slug":"asphalt-paving-equipment-financing",
 "breadcrumb":"Asphalt &amp; Paving Equipment Financing",
 "title":"Asphalt &amp; Paving Equipment Financing (2026) | Axiant",
 "meta":"Asphalt and paving equipment financing: pavers $40K–$500K, milling machines $200K–$800K, rollers $30K–$120K. Seasonal-payment equipment loans and Section 179.",
 "og_title":"Asphalt &amp; Paving Equipment Financing (2026)",
 "og_desc":"Finance pavers, milling machines, rollers, distributor trucks, and sealcoating rigs. Seasonal-payment equipment loans, leases, and Section 179 for paving contractors.",
 "tw_desc":"Paving equipment financing: pavers $40K–$500K, cold planers $200K–$800K, rollers $30K–$120K. Seasonal payment plans available.",
 "schema_desc":"Financing for asphalt and paving equipment — pavers, milling machines, rollers, distributor trucks, and sealcoating rigs — with seasonal-payment structures for paving contractors.",
 "keywords":"asphalt equipment financing, paving equipment financing, paver financing, asphalt milling machine financing, sealcoating equipment financing, seasonal equipment loan",
 "h1":"Asphalt &amp; Paving Equipment Financing",
 "tagline":"How paving contractors finance pavers, milling machines, rollers, and sealcoating rigs &mdash; costs by machine and how seasonal payment structures fit the paving calendar",
 "quick_facts":"Commercial paver $40K&ndash;$500K. Cold planer / milling machine $200K&ndash;$800K. Double-drum roller $30K&ndash;$120K. Asphalt distributor truck $120K&ndash;$250K. Sealcoating rig $15K&ndash;$60K. Seasonal/skip-payment plans common. Section 179 may apply.",
 "rail_cta_h":"Financing paving equipment?",
 "rail_cta_p":"Get matched with equipment lenders that offer seasonal payment structures for paving contractors.",
 "cta_label":"Get Matched for Paving Equipment Financing",
 "quick_answer":"Asphalt and paving equipment financing is built around one reality: in much of the country, paving is seasonal, so the best structures let you pay more in the busy months and less in winter. <strong>Cost by machine</strong>: commercial pavers $40K&ndash;$500K (small/commercial $40K&ndash;$120K, full-size $150K&ndash;$500K); cold planers / milling machines $200K&ndash;$800K; double-drum rollers and compactors $30K&ndash;$120K; asphalt distributor trucks $120K&ndash;$250K; sealcoating rigs $15K&ndash;$60K; portable asphalt plants $500K&ndash;$2M+. <strong>Financing paths</strong>: equipment loans and leases (48&ndash;72 months) with <strong>seasonal or skip-payment options</strong>, plus Section 179 expensing. <strong>Expect</strong> 10&ndash;20% down and underwriting that accounts for the seasonal revenue curve. Figures are illustrative estimates, not quotes.",
 "intro":"Paving contractors live and die by the season &mdash; revenue concentrates in warm months, then slows or stops when temperatures drop. Generic equipment loans with flat year-round payments fight that cash-flow curve, which is why the right paving-equipment financing offers seasonal or skip-payment structures. This guide covers what the core machines cost and how to structure financing so payments line up with the paving calendar. For the broader hub, see <a href=\"/equipment-financing.html\">equipment financing</a>.",
 "sections":[
   {"id":"paving-costs","h2":"Asphalt &amp; Paving Equipment Costs",
    "body":tbl(["Equipment","Typical cost","Notes"],[
      ["Commercial paver (small)","$40K&ndash;$120K","Driveways, parking lots, small crews"],
      ["Commercial paver (full-size)","$150K&ndash;$500K","Road and large commercial work"],
      ["Cold planer / milling machine","$200K&ndash;$800K","Mill-and-fill, resurfacing"],
      ["Double-drum roller / compactor","$30K&ndash;$120K","Compaction behind the paver"],
      ["Asphalt distributor truck","$120K&ndash;$250K","Tack and prime coat application"],
      ["Sealcoating rig","$15K&ndash;$60K","Maintenance and sealcoat businesses"],
      ["Portable asphalt plant","$500K&ndash;$2M+","Producing your own mix"],
    ]) + "<p style=\"margin-top:1rem;\">Leading makers: Caterpillar, Wirtgen/Roadtec, BOMAG, Volvo, and Weiler. Figures are illustrative ranges, not quotes.</p>"},
   {"id":"seasonal-structures","h2":"Seasonal &amp; Skip-Payment Structures",
    "body":"<p>The defining feature of smart paving-equipment financing is matching payments to revenue. Common structures include:</p><ul>"
      "<li><strong>Seasonal payments</strong> &mdash; higher monthly amounts during the paving season (spring&ndash;fall) and reduced payments in winter.</li>"
      "<li><strong>Skip payments</strong> &mdash; a set number of payment-free months each year (often the deep-winter months) baked into the contract.</li>"
      "<li><strong>Deferred first payment</strong> &mdash; 60&ndash;90 days before the first payment so a new machine can start earning before it costs.</li>"
      "<li><strong>Step payments</strong> &mdash; lower payments early, increasing as the new equipment ramps production.</li>"
      "</ul><p>Not every lender offers these, which is why matching to a paving-aware lender matters more than chasing the last quarter-point of rate.</p>"},
   {"id":"financing-paths","h2":"Financing Paths",
    "body":"<ul>"
      "<li><strong>Equipment loan / lease (48&ndash;72 months).</strong> The core path; pair with seasonal/skip structures. 10&ndash;20% down, 8&ndash;13% APR by credit and machine age.</li>"
      "<li><strong>$1-buyout lease</strong> to own and capture <a href=\"../section-179-tax-strategy-2026/\">Section 179</a>; <strong>FMV lease</strong> for lower payments and upgrades.</li>"
      "<li><strong>SBA 7(a)</strong> for larger fleet build-outs or a portable plant bundled with working capital &mdash; see <a href=\"../equipment-financing-vs-sba-loan/\">equipment financing vs SBA loan</a>.</li>"
      "<li><strong>Used equipment</strong> &mdash; rollers and distributor trucks hold value and finance well used; see <a href=\"../can-you-finance-used-equipment/\">can you finance used equipment</a>.</li>"
      "</ul>"},
   {"id":"lender-scrutiny","h2":"What Lenders Look At",
    "body":"<ul>"
      "<li><strong>Seasonality of your revenue</strong> &mdash; lenders that offer seasonal terms want to see the revenue curve and a realistic off-season plan.</li>"
      "<li><strong>Machine age and hours</strong> on used pavers and mills.</li>"
      "<li><strong>Time in business and credit</strong> &mdash; standard <a href=\"../equipment-financing-requirements/\">equipment financing requirements</a>; newer contractors offset with larger down payments.</li>"
      "<li><strong>Owner-operator vs. fleet</strong> &mdash; fleet operators may get fleet-level structures and pricing.</li>"
      "</ul>"},
   {"id":"next-step","h2":"Next Step",
    "body":"<p><a href=\"/match.html\">Get matched with paving-equipment lenders that offer seasonal payments</a>. See also <a href=\"/sba-loans/articles/sba-504-vs-7a-decision-tree/\">SBA 504 vs 7(a)</a> and <a href=\"../how-fast-can-equipment-financing-be-approved/\">how fast equipment financing can be approved</a>.</p>"},
 ],
 "faqs":[
   ("How much does paving equipment cost?","Illustrative ranges: commercial pavers $40K&ndash;$500K; cold planers/milling machines $200K&ndash;$800K; double-drum rollers $30K&ndash;$120K; asphalt distributor trucks $120K&ndash;$250K; sealcoating rigs $15K&ndash;$60K; portable asphalt plants $500K&ndash;$2M+. These are estimates, not quotes."),
   ("Can I get seasonal payments on paving equipment?","Yes — paving-aware lenders offer seasonal payments (higher in season, lower in winter), skip-payment months, deferred first payments, and step payments that ramp with production. Not every lender offers these, so match to one that does."),
   ("Does Section 179 apply to asphalt and paving equipment?","Pavers, rollers, milling machines, and distributor trucks used in your business generally qualify for Section 179 expensing and bonus depreciation. A $1-buyout lease or equipment loan keeps the asset on your books; confirm with your CPA."),
   ("Can I finance used paving equipment?","Yes. Rollers, distributor trucks, and pavers have active used markets and finance well; lenders weigh machine age and hours. Clean maintenance records and reasonable hours keep rates competitive."),
   ("What down payment do paving lenders want?","Around 10&ndash;20% is typical, lower for established contractors with strong credit. Newer paving businesses can offset limited history with a larger down payment or a deferred-first-payment structure."),
 ],
 "howto_name":"How to finance asphalt and paving equipment",
 "howto_desc":"Five steps to finance pavers, milling machines, rollers, and sealcoating equipment with seasonal payments.",
 "howto_steps":[
   ("List the machines and total project","Price the paver, roller, milling machine, distributor truck, or sealcoating rig you need so the lender sees the full package."),
   ("Find a paving-aware lender","Prioritize lenders that offer seasonal or skip-payment structures over the lowest flat-rate quote — cash-flow fit matters more in a seasonal business."),
   ("Choose the payment structure","Match payments to your revenue curve: seasonal, skip-payment, deferred first payment, or step payments."),
   ("Decide new vs. used and loan vs. lease","Used rollers and trucks finance well; choose $1-buyout to own and depreciate or FMV for lower payments."),
   ("Apply with financials and a season plan","Provide business financials, the equipment quote, and a realistic off-season plan so the lender is comfortable with seasonal terms."),
 ],
 "related":EQ_COMMON,
})
