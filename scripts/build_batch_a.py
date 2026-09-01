"""Batch A of 11 — articles #21-#24 (hotel, self-storage, SBA franchise, construction equipment)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from article_engine import run

ARTICLES = [
    # ===== #21 Hotel Financing =====
    {
        "file": "commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/index.html",
        "canonical": "https://axiantpartners.com/commercial-real-estate-loans/articles/hotel-financing-sba-cmbs-conventional/",
        "breadcrumb_cluster": "Commercial Real Estate Loans",
        "breadcrumb_cluster_url": "https://axiantpartners.com/commercial-real-estate-loans.html",
        "breadcrumb_articles_url": "https://axiantpartners.com/commercial-real-estate-loans/articles/",
        "breadcrumb_article_name": "Hotel Financing: SBA, CMBS, Conventional",
        "title_tag": "Hotel Financing: SBA 504, CMBS, Conventional Bank Compared (2026) | Axiant",
        "og_title": "Hotel Financing: SBA 504 vs CMBS vs Conventional Bank (2026)",
        "meta_desc": "Hotel financing programs compared: SBA 504 (10% down, ~6%, $5.5M cap), CMBS ($5M+, 6.5-8%, 10-yr balloon), conventional bank ($10M+, 25-30% down). By deal size and flag.",
        "og_desc": "Hotel acquisition + refinance: SBA 504 for under $5.5M, CMBS for $5M-$50M flagged properties, conventional bank for $10M+ stronger sponsors. Rates, equity, structure.",
        "twitter_desc": "Hotel financing: SBA 504 under $5.5M, CMBS $5M-50M, conventional $10M+. By deal size + flag.",
        "section": "Commercial Real Estate Loans",
        "article_headline": "Hotel Financing: SBA, CMBS, Conventional",
        "article_desc": "How hotel acquisitions and refinances get financed across SBA 504, CMBS, and conventional bank programs by deal size, flag, and sponsor profile.",
        "image_url": "https://axiantpartners.com/assets/multifamily-loan-hero.webp",
        "keywords": "hotel financing, hotel acquisition loan, hotel SBA loan, hotel CMBS, hospitality financing, hotel franchise financing, hotel construction loan",
        "speakable_name": "Hotel Financing: SBA, CMBS, Conventional Compared",
        "faqs": [
            ("How do you finance a hotel purchase?", "Three main paths in 2026. <strong>SBA 504</strong> for hotels up to $5.5M (50% bank loan + 40% SBA debenture + 10% buyer equity, ~6% blended, 20&ndash;25 yr term). <strong>CMBS</strong> for flagged hotels $5M&ndash;$50M (25&ndash;30% down, 6.5&ndash;8% fixed, 10-yr balloon with 25&ndash;30 yr amortization). <strong>Conventional bank or life-company debt</strong> for stronger sponsors on $10M+ deals (25&ndash;35% down, 6&ndash;7.5%). Independent hotels and economy properties usually go SBA 504; major-brand flagged hotels go CMBS."),
            ("What credit score do you need for a hotel loan?", "<strong>SBA 504</strong>: 680+ FICO, 10&ndash;15% buyer equity, 2+ years management experience strongly preferred. <strong>CMBS</strong>: focused on the property cash flow and flag rather than personal FICO, but sponsors typically 680+ with $1M+ net worth and prior hotel ownership. <strong>Conventional bank</strong>: 700+ FICO, $5M+ liquid net worth, prior hotel operating experience required for most lenders."),
            ("What's the typical DSCR requirement for a hotel loan?", "<strong>DSCR 1.30&ndash;1.40x</strong> minimum for most hotel lenders &mdash; meaning trailing 12-month NOI must cover annual debt service by at least 30%. CMBS lenders often want <strong>1.40x</strong> at close on stabilized properties. New-build or value-add hotels with projected DSCR may qualify at 1.20x with reserves. RevPAR (revenue per available room) volatility means hotel lenders run more conservative DSCR than multifamily or industrial."),
            ("Can you get a hotel loan for a franchise (Marriott, Hilton, Holiday Inn)?", "Yes &mdash; <strong>flagged hotel financing</strong> is often easier than independent hotel financing because lenders view brand systems as lower risk. Most major flags (Marriott, Hilton, IHG, Hyatt, Wyndham, Choice) have preferred-lender lists with banks experienced in their PIP (Property Improvement Plan) and franchise agreement requirements. Lenders will require an executed franchise agreement + PIP estimate as part of the loan file."),
            ("How long does hotel financing take to close?", "<strong>SBA 504 hotel</strong>: 60&ndash;90 days through a Preferred Lender Bank. <strong>CMBS</strong>: 60&ndash;90 days from term sheet (longer with PIP estimates and franchise approval). <strong>Conventional bank</strong>: 45&ndash;75 days. <strong>Hotel bridge loan</strong> for acquisitions needing fast close: 21&ndash;45 days at 9&ndash;12% rates. Plan 90&ndash;120 days from LOI to close on permanent debt deals."),
        ],
        "howto_name": "How to finance a hotel acquisition",
        "howto_desc": "Five-step process for hotel acquisitions across SBA 504, CMBS, and conventional financing.",
        "howto_steps": [
            ("Choose the program by deal size and flag", "Under $5.5M: SBA 504 wins on rate. $5M&ndash;$50M flagged: CMBS. $10M+ strong sponsor: conventional or life-company."),
            ("Get a property STR (Smith Travel Research) report", "Lender wants trailing-12 RevPAR, ADR, occupancy. STR competitive set analysis becomes the underwriting basis."),
            ("Secure franchise approval + PIP estimate (flagged hotels)", "Brand approves the buyer; PIP estimate becomes a holdback or escrow in the loan. No franchise approval = no flagged hotel loan."),
            ("Engage SBA Preferred Lender Bank or CMBS originator", "PLP banks: Live Oak, Celtic, Wells Fargo SBA. CMBS originators: JPMorgan, Wells Fargo, Deutsche Bank, Citi."),
            ("Close with reserves + franchise/PIP holdbacks", "Standard: 6&ndash;12 months reserves at close, PIP escrow if required by franchise agreement."),
        ],
        "h1": "Hotel Financing: SBA 504, CMBS &amp; Conventional Bank Compared",
        "tagline": "How hotel acquisitions and refinances get financed in 2026 &mdash; SBA 504 for under $5.5M, CMBS for $5M-$50M flagged, conventional for $10M+ with strong sponsors",
        "rail_back_text": "Back to CRE Loan Articles",
        "rail_back_href": "../",
        "rail_facts": "SBA 504: up to $5.5M, 10% down, ~6%, 25-yr. CMBS: $5M-$50M, 25-30% down, 6.5-8%, 10-yr balloon. Conventional: $10M+, 25-35% down. DSCR 1.30-1.40x. Franchise approval + PIP required on flagged.",
        "rail_cta_h3": "Need hotel financing?",
        "rail_cta_p": "Get matched with SBA hotel lenders, CMBS originators, and conventional hotel banks.",
        "rail_cta_btn": "Get Matched for Hotel Financing",
        "quick_answer_html": 'Hotel financing in 2026 splits across three main programs by deal size and flag. <strong>SBA 504</strong> finances hotels up to <strong>$5.5M</strong> at 10% down, ~6% blended rate, 20&ndash;25 year amortization &mdash; best for independent and economy properties. <strong>CMBS</strong> finances flagged hotels <strong>$5M&ndash;$50M</strong> at 25&ndash;30% down, 6.5&ndash;8% fixed rate, 10-year balloon with 25&ndash;30 year amortization &mdash; standard for Marriott, Hilton, IHG, Hyatt, Wyndham, Choice properties. <strong>Conventional bank or life-company debt</strong> handles $10M+ deals with strong sponsors at 25&ndash;35% down. <strong>DSCR 1.30&ndash;1.40x</strong> minimum across all programs. Franchise approval + PIP estimate required on flagged.',
        "intro_html": '<p>Hotel financing is one of the most segmented categories in commercial real estate lending. Lenders treat a $4M independent economy hotel completely differently from a $20M Marriott Courtyard, and the right financing program varies by deal size, flag, and sponsor experience. This guide breaks down the three main paths &mdash; SBA 504, CMBS, conventional &mdash; with rate, equity, and timing benchmarks for each. For related see <a href="../../sba-loans/articles/sba-7a-vs-504-loan/">SBA 7(a) vs 504</a> and <a href="../cmbs-vs-life-company-vs-agency-debt/">CMBS vs life-company vs agency debt</a>.</p>',
        "body_sections_html": (
            '<h2 id="sba-hotel">SBA 504 for Hotels Under $5.5M</h2>'
            '<p>The default program for owner-operators buying independent, economy, or smaller flagged hotels:</p>'
            '<ul>'
            '<li><strong>Structure:</strong> 50% bank first mortgage + 40% SBA debenture + 10% buyer equity</li>'
            '<li><strong>Loan size:</strong> Up to $5M ($5.5M for projects meeting public-policy or green-energy criteria)</li>'
            '<li><strong>Rate:</strong> ~6% blended (debenture portion fixed at 25-yr rate, currently ~5.5&ndash;6%; bank first mortgage 6&ndash;8%)</li>'
            '<li><strong>Term:</strong> 20&ndash;25 years amortization on real estate, 10 years on FF&amp;E (furniture, fixtures, equipment)</li>'
            '<li><strong>Equity:</strong> 10% standard; 15% on new construction or change-of-ownership where the buyer has no prior hotel experience</li>'
            '<li><strong>Close time:</strong> 60&ndash;90 days through a Preferred Lender Bank</li>'
            '<li><strong>Lenders:</strong> Live Oak Bank (specialty hotel team), Celtic Bank, Byline Bank, US Bank Practice + Hospitality</li>'
            '</ul>'
            '<p>SBA 504 hotels typically come with the most flexibility on first-time buyers and value-add deals. The trade-off is the 60&ndash;90 day close and SBA documentation overhead.</p>'
            '<h2 id="cmbs-hotel">CMBS for Flagged Hotels $5M&ndash;$50M</h2>'
            '<p>CMBS (Commercial Mortgage-Backed Securities) is the standard for institutional-quality flagged hotels:</p>'
            '<ul>'
            '<li><strong>Loan size:</strong> $5M to $100M+ (sweet spot $5M&ndash;$50M for flagged hotel CMBS)</li>'
            '<li><strong>Rate:</strong> 6.5&ndash;8% fixed (10-yr Treasury + 250&ndash;400 bps spread)</li>'
            '<li><strong>Term:</strong> 10-year balloon with 25&ndash;30 year amortization &mdash; refinance or sell at maturity</li>'
            '<li><strong>LTV:</strong> 65&ndash;70% max (25&ndash;35% buyer equity required)</li>'
            '<li><strong>DSCR:</strong> 1.40x at close standard</li>'
            '<li><strong>Non-recourse</strong> typically (unlike SBA which always requires personal guarantee)</li>'
            '<li><strong>Prepayment:</strong> Defeasance or yield maintenance &mdash; expensive to refinance early</li>'
            '<li><strong>Top originators:</strong> JPMorgan, Wells Fargo, Deutsche Bank, Citi, Morgan Stanley, Goldman Sachs</li>'
            '</ul>'
            '<p>CMBS is the right tool for sponsors who want non-recourse debt on a stabilized, flagged property and don&apos;t plan to refinance before year 10.</p>'
            '<h2 id="conventional-hotel">Conventional Bank &amp; Life-Company Debt $10M+</h2>'
            '<p>For experienced sponsors with deeper balance sheets:</p>'
            '<ul>'
            '<li><strong>Rate:</strong> 6&ndash;7.5% (life-company often best in class)</li>'
            '<li><strong>LTV:</strong> 60&ndash;75% (25&ndash;40% equity)</li>'
            '<li><strong>Term:</strong> 5, 7, or 10-year balloon with 25-yr amortization</li>'
            '<li><strong>Recourse:</strong> Usually partial recourse on stronger sponsors; full recourse on weaker</li>'
            '<li><strong>Flexibility:</strong> More flexible covenants than CMBS; better treatment of bridge-to-perm scenarios</li>'
            '<li><strong>Top providers:</strong> Wells Fargo, JPMorgan, Bank of America commercial; Prudential, MetLife, New York Life (life-company)</li>'
            '</ul>'
            '<h2 id="bridge">Hotel Bridge &amp; Construction Loans</h2>'
            '<p>For acquisition timing or new-build:</p>'
            '<ul>'
            '<li><strong>Bridge loans:</strong> 9&ndash;12% interest-only, 12&ndash;36 month terms, 65&ndash;75% LTV. Used for value-add or distressed acquisitions where you&apos;ll refinance into permanent debt after stabilization.</li>'
            '<li><strong>Construction loans:</strong> 70&ndash;75% LTC (loan-to-cost), 8&ndash;11% rate, interest-only during construction. Convert to permanent (SBA 504, CMBS, or conventional) at certificate of occupancy.</li>'
            '<li><strong>Top providers:</strong> Madison Realty Capital, Mosaic Real Estate, Calmwater Capital, RREEF, plus regional bridge specialty lenders.</li>'
            '</ul>'
            '<h2 id="franchise">Franchise Approval &amp; PIP</h2>'
            '<p>For flagged hotels, the deal won&apos;t close without two pieces:</p>'
            '<ul>'
            '<li><strong>Franchise approval letter:</strong> Brand approves the buyer as an acceptable franchisee. Each major flag has a different approval timeline (Marriott 60&ndash;90 days, Hilton 45&ndash;75 days, IHG 30&ndash;60 days).</li>'
            '<li><strong>PIP (Property Improvement Plan):</strong> Brand-mandated upgrades to bring the property up to current standards. PIP estimate becomes a holdback or escrow at close. Range $500K&ndash;$5M+ depending on flag, age, and condition.</li>'
            '</ul>'
            '<p>Start the franchise approval process at LOI &mdash; it&apos;s often the bottleneck on closing timeline.</p>'
            '<h2 id="next-step">Next Step</h2>'
            '<p><a href="/match.html">Get matched with hotel lenders</a> &mdash; SBA Preferred Lender Banks, CMBS originators, life-company, and bridge specialists. See also <a href="../../sba-loans/articles/sba-504-vs-7a-decision-tree/">SBA 504 vs 7(a) decision tree</a> and <a href="../cmbs-vs-life-company-vs-agency-debt/">CMBS vs life-company vs agency debt</a>.</p>'
        ),
        "related_links": [
            ("../../sba-loans/articles/sba-504-vs-7a-decision-tree/", "SBA 504 vs 7(a) Decision Tree"),
            ("../cmbs-vs-life-company-vs-agency-debt/", "CMBS vs Life-Company vs Agency"),
            ("../multifamily-loan-down-payment/", "Multifamily Loan Down Payment"),
            ("../how-fast-can-you-close-commercial-bridge-loan/", "How Fast Can You Close a Bridge Loan"),
            ("/sba-loans.html", "SBA Loans Hub"),
            ("/commercial-real-estate-loans.html", "CRE Loans Hub"),
        ],
        "related_cta_text": "Get Matched for Hotel Financing",
        "toc": [("#sba-hotel","SBA 504 Under $5.5M"),("#cmbs-hotel","CMBS $5M&ndash;$50M"),("#conventional-hotel","Conventional/Life-Co $10M+"),("#bridge","Bridge &amp; Construction"),("#franchise","Franchise Approval &amp; PIP"),("#next-step","Next Step")],
    },

    # ===== #22 Self-Storage Facility Financing =====
    {
        "file": "commercial-real-estate-loans/articles/self-storage-facility-financing-acquisitions/index.html",
        "canonical": "https://axiantpartners.com/commercial-real-estate-loans/articles/self-storage-facility-financing-acquisitions/",
        "breadcrumb_cluster": "Commercial Real Estate Loans",
        "breadcrumb_cluster_url": "https://axiantpartners.com/commercial-real-estate-loans.html",
        "breadcrumb_articles_url": "https://axiantpartners.com/commercial-real-estate-loans/articles/",
        "breadcrumb_article_name": "Self-Storage Facility Financing",
        "title_tag": "Self-Storage Facility Financing & Acquisitions (2026) | Axiant",
        "og_title": "Self-Storage Financing: SBA 504, CMBS, Bridge (2026)",
        "meta_desc": "Self-storage facility financing: SBA 504 (under $5.5M, 10% down, ~6%), CMBS ($3M+, 25-30% down, 6.5-8%), bridge for lease-up (9-12%). Acquisition + construction structures.",
        "og_desc": "Finance self-storage acquisitions and development: SBA 504, CMBS, bridge loans, construction. Stabilized vs lease-up vs ground-up. Rates, LTV, and operator requirements.",
        "twitter_desc": "Self-storage financing: SBA 504 under $5.5M, CMBS $3M+, bridge for lease-up. Stabilized vs ground-up structures.",
        "section": "Commercial Real Estate Loans",
        "article_headline": "Self-Storage Facility Financing",
        "article_desc": "Financing self-storage facility acquisitions, refinances, lease-up, and ground-up development across SBA 504, CMBS, bridge, and construction programs.",
        "image_url": "https://axiantpartners.com/assets/multifamily-loan-hero.webp",
        "keywords": "self storage financing, self storage facility loan, self storage acquisition loan, self storage SBA, self storage CMBS, storage facility construction loan",
        "speakable_name": "Self-Storage Facility Financing and Acquisitions",
        "faqs": [
            ("How do you finance a self-storage facility purchase?", "Four main paths in 2026. <strong>SBA 504</strong> for stabilized facilities up to $5.5M (10% down, ~6% blended, 25-yr amort). <strong>CMBS</strong> for $3M+ stabilized facilities (25&ndash;30% down, 6.5&ndash;8% fixed, 10-yr balloon). <strong>Bridge loans</strong> for lease-up (under 70% occupancy) acquisitions at 9&ndash;12%, 12&ndash;36 month terms. <strong>Construction loans</strong> for ground-up development at 70&ndash;75% LTC, 8&ndash;11% rate."),
            ("What occupancy does a self-storage facility need to qualify for permanent debt?", "<strong>85%+ economic occupancy</strong> for 90&ndash;120 days minimum to qualify for stabilized permanent debt (SBA 504, CMBS, conventional). Below 85% is typically lease-up territory &mdash; either bridge financing until stabilized, or permanent debt with reserves and lower LTV (60&ndash;65%). New-build facilities go through bridge or construction-to-perm; refinance into permanent debt 12&ndash;24 months after CO."),
            ("What's the typical DSCR requirement for self-storage?", "<strong>DSCR 1.25&ndash;1.35x</strong> on stabilized self-storage &mdash; slightly more lenient than hotel (1.40x) because of self-storage&apos;s lower revenue volatility and lower capex requirements. CMBS lenders may require 1.30x; SBA 504 typically 1.25x. Bridge lenders are more flexible on going-in DSCR if the underwriting projects stabilized DSCR &ge; 1.30x within 18&ndash;24 months."),
            ("Can you finance a self-storage facility through an SBA loan?", "<strong>Yes</strong> &mdash; self-storage is an eligible use of <strong>SBA 504</strong> for owner-operators. The owner-occupancy requirement is met by the operator running the business from the facility (office on site, manager presence). SBA 504 self-storage loans typically run 10% buyer equity, ~6% blended rate, 25-year amortization. SBA 7(a) is also possible for smaller deals or those needing more working capital flexibility."),
            ("What credit score is needed for a self-storage loan?", "<strong>680+ FICO</strong> standard for SBA 504 and CMBS. <strong>700+</strong> gets best pricing. <strong>Net worth requirements</strong>: $500K&ndash;$1M for SBA 504 deals; $1M+ for CMBS. Prior self-storage ownership or strong commercial real estate operator history reduces credit-score-driven repricing. First-time storage operators often need to bring a partner with operating experience."),
        ],
        "howto_name": "How to finance a self-storage facility",
        "howto_desc": "Five-step framework for self-storage acquisition or refinance.",
        "howto_steps": [
            ("Determine stabilized vs lease-up vs ground-up", "Stabilized (85%+ occupancy, 12+ months): SBA 504 or CMBS. Lease-up (60-85%): bridge then refi. Ground-up: construction loan to permanent."),
            ("Get trailing-12 financials + rent roll + comp set", "Lender wants T-12 + rent roll showing unit mix, occupancy, ECRI history. Comp set from STR, Yardi Matrix, or Inside Self-Storage."),
            ("Pick the program by deal size + stabilization", "Under $5.5M stabilized: SBA 504. $3M-$50M stabilized: CMBS. Lease-up: bridge. Ground-up: construction-to-perm."),
            ("Choose Preferred Lender Bank, CMBS originator, or bridge specialist", "SBA: Live Oak, Celtic, Byline. CMBS: JPMorgan, Wells Fargo, Deutsche. Bridge: Mosaic, RREEF, Madison Realty Capital."),
            ("Close with reserves + management plan", "Lender wants 3-6 months reserves; outside professional management vs operator-managed; CapEx budget for any deferred maintenance."),
        ],
        "h1": "Self-Storage Facility Financing: SBA 504, CMBS, Bridge &amp; Construction",
        "tagline": "How self-storage acquisitions, refinances, lease-up, and ground-up developments get financed in 2026 &mdash; by stabilization stage and deal size",
        "rail_back_text": "Back to CRE Loan Articles",
        "rail_back_href": "../",
        "rail_facts": "Stabilized SBA 504: under $5.5M, 10% down, ~6%, 25-yr. CMBS: $3M+, 25-30% down, 6.5-8%. Bridge for lease-up: 9-12%, 12-36 mo. Construction 70-75% LTC. DSCR 1.25-1.35x. 85%+ occupancy for permanent debt.",
        "rail_cta_h3": "Need self-storage financing?",
        "rail_cta_p": "Get matched with self-storage SBA, CMBS, bridge, and construction lenders.",
        "rail_cta_btn": "Get Matched for Self-Storage Financing",
        "quick_answer_html": 'Self-storage facility financing in 2026 splits four ways. <strong>SBA 504</strong> for owner-operated stabilized facilities up to <strong>$5.5M</strong> at 10% down, ~6% blended rate, 25-yr amortization. <strong>CMBS</strong> for stabilized facilities <strong>$3M+</strong> at 25&ndash;30% down, 6.5&ndash;8% fixed rate, 10-yr balloon. <strong>Bridge loans</strong> for lease-up (under 70% occupancy) acquisitions at <strong>9&ndash;12%</strong>, 12&ndash;36 month terms, refinanced into permanent debt at stabilization. <strong>Construction loans</strong> for ground-up at <strong>70&ndash;75% LTC</strong>, 8&ndash;11% rate, interest-only during build, converting to permanent at CO. <strong>DSCR 1.25&ndash;1.35x</strong>, <strong>85%+ economic occupancy</strong> for permanent debt qualification.',
        "intro_html": '<p>Self-storage has been one of the strongest-performing commercial real estate categories of the past decade, driven by population mobility, household downsizing, and small-business storage demand. Lender appetite reflects this: self-storage is one of the easier CRE categories to finance in 2026, with multiple competitive programs across the deal-size spectrum. This guide covers how acquisitions and developments get financed by stabilization stage. For related see <a href="../cmbs-vs-life-company-vs-agency-debt/">CMBS vs life-company vs agency debt</a>.</p>',
        "body_sections_html": (
            '<h2 id="sba-storage">SBA 504 for Owner-Operated Stabilized Facilities</h2>'
            '<ul>'
            '<li><strong>Loan size:</strong> Up to $5M ($5.5M with public-policy criteria)</li>'
            '<li><strong>Structure:</strong> 50/40/10 (bank/SBA debenture/buyer equity)</li>'
            '<li><strong>Rate:</strong> ~6% blended</li>'
            '<li><strong>Term:</strong> 25-yr amortization</li>'
            '<li><strong>Owner-occupancy requirement:</strong> Met by operator presence on site (office, manager)</li>'
            '<li><strong>Best for:</strong> Single-site or small-portfolio owner-operators buying stabilized facilities</li>'
            '</ul>'
            '<h2 id="cmbs-storage">CMBS for Larger Stabilized Portfolios</h2>'
            '<ul>'
            '<li><strong>Loan size:</strong> $3M&ndash;$100M+ (sweet spot $5M&ndash;$50M)</li>'
            '<li><strong>Rate:</strong> 6.5&ndash;8% (10-yr Treasury + 200&ndash;350 bps)</li>'
            '<li><strong>Term:</strong> 10-yr balloon with 25&ndash;30 yr amortization</li>'
            '<li><strong>LTV:</strong> 65&ndash;75% (DSCR-constrained at 1.30x)</li>'
            '<li><strong>Non-recourse</strong> typical &mdash; the property is the collateral, no personal guarantee on stabilized deals</li>'
            '<li><strong>Best for:</strong> $5M+ stabilized facilities, especially multi-property portfolios</li>'
            '</ul>'
            '<h2 id="bridge-storage">Bridge Loans for Lease-Up Acquisitions</h2>'
            '<p>Buying a facility under 85% occupancy &mdash; either recent build or value-add &mdash; usually doesn&apos;t qualify for permanent debt. The bridge-then-refi path:</p>'
            '<ul>'
            '<li><strong>Bridge structure:</strong> 65&ndash;75% LTV, 9&ndash;12% interest-only, 12&ndash;36 month term</li>'
            '<li><strong>Game plan:</strong> Lease up to 85%+ economic occupancy over 12&ndash;24 months, then refinance into SBA 504 or CMBS permanent debt</li>'
            '<li><strong>Reserves:</strong> 6&ndash;12 months interest reserves built into the bridge loan</li>'
            '<li><strong>Top providers:</strong> Mosaic Real Estate, Madison Realty Capital, RREEF, Calmwater Capital, regional bridge specialists</li>'
            '</ul>'
            '<h2 id="construction">Construction &amp; Construction-to-Permanent</h2>'
            '<p>For ground-up self-storage development (single-site or full-acreage):</p>'
            '<ul>'
            '<li><strong>Construction loan:</strong> 70&ndash;75% LTC, 8&ndash;11% rate, interest-only during construction, typical 18&ndash;24 month construction period</li>'
            '<li><strong>Lender requires:</strong> General contractor with self-storage experience, feasibility study with demand analysis, signed pre-leasing or marketing plan, equity injection from sponsor</li>'
            '<li><strong>Conversion to permanent:</strong> At certificate of occupancy or 80%+ economic occupancy, refinance into SBA 504, CMBS, or conventional. Some lenders offer construction-to-perm in one package.</li>'
            '</ul>'
            '<h2 id="ops">What Lenders Look at on Self-Storage Operations</h2>'
            '<ul>'
            '<li><strong>Economic occupancy</strong> (rent-paying units / total units), not just physical occupancy</li>'
            '<li><strong>Unit mix</strong> &mdash; small unit volume (5x5, 5x10) drives revenue density; oversized warehouse-style units have weaker absorption</li>'
            '<li><strong>Rent rate trends</strong> &mdash; ECRI (Existing Customer Rate Increase) frequency and amount</li>'
            '<li><strong>Climate-controlled mix</strong> &mdash; premium for climate-controlled units; lender weights this favorably</li>'
            '<li><strong>Trade area demand</strong> &mdash; population within 3- and 5-mile radius, household income, competing supply</li>'
            '<li><strong>Management</strong> &mdash; outside professional management (Public Storage, Extra Space Storage management arms, Storable-powered third-party managers) often gets better rate than owner-managed</li>'
            '</ul>'
            '<h2 id="next-step">Next Step</h2>'
            '<p><a href="/match.html">Get matched with self-storage lenders</a> across SBA, CMBS, bridge, and construction. See also <a href="../cmbs-vs-life-company-vs-agency-debt/">CMBS vs life-company vs agency debt</a> and <a href="../../sba-loans/articles/sba-504-vs-7a-decision-tree/">SBA 504 vs 7(a) decision tree</a>.</p>'
        ),
        "related_links": [
            ("../cmbs-vs-life-company-vs-agency-debt/", "CMBS vs Life-Company vs Agency"),
            ("../../sba-loans/articles/sba-504-vs-7a-decision-tree/", "SBA 504 vs 7(a) Decision Tree"),
            ("../hotel-financing-sba-cmbs-conventional/", "Hotel Financing: SBA, CMBS, Conventional"),
            ("../how-fast-can-you-close-commercial-bridge-loan/", "How Fast Can You Close a Bridge Loan"),
            ("/sba-loans.html", "SBA Loans Hub"),
            ("/commercial-real-estate-loans.html", "CRE Loans Hub"),
        ],
        "related_cta_text": "Get Matched for Self-Storage Financing",
        "toc": [("#sba-storage","SBA 504 Owner-Operated"),("#cmbs-storage","CMBS Larger Portfolios"),("#bridge-storage","Bridge for Lease-Up"),("#construction","Construction-to-Permanent"),("#ops","What Lenders Look At"),("#next-step","Next Step")],
    },

    # ===== #23 SBA Loan to Buy a Franchise =====
    {
        "file": "sba-loans/articles/sba-loan-buy-franchise/index.html",
        "canonical": "https://axiantpartners.com/sba-loans/articles/sba-loan-buy-franchise/",
        "breadcrumb_cluster": "SBA Loans",
        "breadcrumb_cluster_url": "https://axiantpartners.com/sba-loans.html",
        "breadcrumb_articles_url": "https://axiantpartners.com/sba-loans/articles/",
        "breadcrumb_article_name": "SBA Loan to Buy a Franchise",
        "title_tag": "SBA Loan to Buy a Franchise: 7(a) Up to $5M (2026) | Axiant",
        "og_title": "SBA Loan to Buy a Franchise: 7(a) Up to $5M (2026)",
        "meta_desc": "SBA 7(a) loans for franchise purchases up to $5M: 10-15% buyer equity, ~10% rate, 10-yr term. SBA Franchise Directory eligibility, FDD, top franchise SBA lenders.",
        "og_desc": "Use SBA 7(a) to buy a franchise: 10-15% equity, ~10% rate, 10-yr term, up to $5M. Franchise must be in SBA Franchise Directory. Process, FDD review, and PLP lender list.",
        "twitter_desc": "SBA 7(a) for franchise purchase: up to $5M, 10-15% equity, ~10% rate. SBA Franchise Directory required.",
        "section": "SBA Loans",
        "article_headline": "SBA Loan to Buy a Franchise",
        "article_desc": "How SBA 7(a) loans work for franchise purchases: eligibility, FDD review, buyer equity, rates, and the top franchise-experienced SBA lenders.",
        "image_url": "https://axiantpartners.com/assets/sba-504.webp",
        "keywords": "sba loan franchise, sba franchise loan, sba loan to buy a franchise, franchise financing, sba 7a franchise, franchise sba lender, franchise SBA directory",
        "speakable_name": "SBA Loan to Buy a Franchise",
        "faqs": [
            ("Can you use an SBA loan to buy a franchise?", "<strong>Yes &mdash; SBA 7(a) is the most common path</strong> for franchise purchases up to <strong>$5M</strong>. Standard structure: <strong>10&ndash;15% buyer equity</strong>, 90% SBA-guaranteed loan at <strong>prime + 2.5&ndash;3%</strong> (~10% in 2026), <strong>10-year amortization</strong> on the goodwill portion. The franchise must be listed in the <strong>SBA Franchise Directory</strong> (~3,000+ approved brands). Most major franchises are listed; some smaller or newer brands need to be added before SBA financing is available."),
            ("What is the SBA Franchise Directory and why does it matter?", "The <strong>SBA Franchise Directory</strong> is the list of franchise systems with approved Franchise Disclosure Documents and standard franchise agreements that SBA has reviewed. If your franchise is on the list, your loan can move through standard SBA underwriting. If it&apos;s not, your franchisor must submit their FDD and franchise agreement to SBA for review &mdash; adds 30&ndash;60 days. Check <a href='https://www.sba.gov/about-sba/sba-locations/headquarters-offices/office-credit-risk-management' rel='nofollow'>SBA.gov</a> for current directory."),
            ("How much equity does a franchise buyer need?", "<strong>10&ndash;15% buyer equity</strong> is standard SBA 7(a). Some lenders require <strong>15&ndash;20%</strong> on newer brands or first-time franchise buyers. The buyer equity must be in liquid form (cash, marketable securities) at close &mdash; you cannot finance the SBA equity injection from another loan. Seller financing of 5&ndash;10% on top of buyer equity is allowed and common on franchise resales."),
            ("Which franchises are easiest to get SBA financing for?", "Franchises with <strong>long SBA lending history</strong>, <strong>stable unit economics</strong>, and <strong>healthy SBA default rates</strong> get the easiest financing. <strong>Top tier:</strong> Subway, Dunkin&apos;, Jersey Mike&apos;s, Wingstop, Tropical Smoothie Caf&eacute;, Smoothie King, Marco&apos;s Pizza, Anytime Fitness, The UPS Store, Mathnasium. <strong>Tougher:</strong> newer concepts with under 50 units, brands with high SBA default rates, or franchises in volatile categories (full-service casual dining, fitness with high closure rates). Check the SBA Franchise Findings Report for default-rate data."),
            ("How long does franchise SBA financing take to close?", "<strong>45&ndash;75 days</strong> through a Preferred Lender Bank for franchises in the SBA Franchise Directory. Adds 30&ndash;60 days if the franchise needs to be added to the directory. <strong>SBA Express</strong> at $500K can close in 2&ndash;3 weeks for smaller franchise purchases, but the rate is higher (prime + 4.5&ndash;6.5%). Top franchise SBA lenders: Live Oak Bank, Celtic Bank, Byline Bank, US Bank, Wells Fargo SBA Lending."),
        ],
        "howto_name": "How to use an SBA loan to buy a franchise",
        "howto_desc": "Five-step process for franchise acquisitions through SBA 7(a) financing.",
        "howto_steps": [
            ("Confirm the franchise is in the SBA Franchise Directory", "Check SBA Franchise Directory before signing the franchise agreement. If not listed, your franchisor needs to add it &mdash; adds 30-60 days to your timeline."),
            ("Get the Franchise Disclosure Document (FDD)", "Item 19 (Financial Performance Representations) is critical. Lender uses Item 19 to underwrite. No Item 19 disclosure makes lending harder."),
            ("Arrange 10-15% buyer equity in liquid cash", "Cannot be borrowed from another loan. Document source of funds (savings, IRA rollover via ROBS, gift from family with gift letter)."),
            ("Apply with a Preferred Lender Bank with franchise experience", "Live Oak Bank, Celtic Bank, Byline Bank, US Bank, Wells Fargo SBA all have dedicated franchise teams. Apply to 2-3."),
            ("Close in 45-75 days with personal guarantee + franchise agreement assignment", "PG from 20%+ owners. Franchise agreement assignment from seller to buyer (on resales) or original signing (on new units)."),
        ],
        "h1": "SBA Loan to Buy a Franchise: 7(a) Up to $5M",
        "tagline": "How franchise buyers use SBA 7(a) for new-unit purchases and franchise resales &mdash; FDD review, SBA Franchise Directory, equity requirements, and the lenders who actually fund franchise deals",
        "rail_back_text": "Back to SBA Loan Articles",
        "rail_back_href": "../",
        "rail_facts": "SBA 7(a): up to $5M, 10-15% buyer equity, ~10% rate, 10-yr term. SBA Franchise Directory required. FDD Item 19 drives underwriting. Top lenders: Live Oak, Celtic, Byline, US Bank.",
        "rail_cta_h3": "Need franchise SBA financing?",
        "rail_cta_p": "Get matched with franchise-experienced SBA Preferred Lender Banks.",
        "rail_cta_btn": "Get Matched for Franchise SBA Loan",
        "quick_answer_html": 'Yes &mdash; <strong>SBA 7(a) loans</strong> are the most common path for franchise purchases up to <strong>$5M</strong>. Standard structure: <strong>10&ndash;15% buyer equity</strong> (cash, no borrowed funds), 90% SBA-guaranteed loan at <strong>prime + 2.5&ndash;3%</strong> (~10% in 2026), <strong>10-year amortization</strong> on goodwill, longer if real estate is included. The franchise must be in the <strong>SBA Franchise Directory</strong> &mdash; most major brands (Subway, Dunkin&apos;, Jersey Mike&apos;s, Wingstop, Anytime Fitness, The UPS Store) are listed. <strong>Close time:</strong> 45&ndash;75 days through a Preferred Lender Bank. <strong>Top franchise SBA lenders:</strong> Live Oak Bank, Celtic Bank, Byline Bank, US Bank, Wells Fargo SBA Lending.',
        "intro_html": '<p>Franchise financing through SBA 7(a) is one of the highest-volume SBA loan use cases &mdash; the SBA approves thousands of franchise loans every year across the 3,000+ approved franchise systems. The economics work because franchise systems offer brand recognition, operational support, and historical performance data that reduce lender risk vs financing an independent business. This guide covers how SBA franchise lending actually works, what makes a franchise easier or harder to finance, and the lenders who do the most volume in the space. For related see <a href="../sba-7a-vs-504-loan/">SBA 7(a) vs 504</a> and <a href="../how-much-down-payment-required-sba-loan/">SBA down payment</a>.</p>',
        "body_sections_html": (
            '<h2 id="how-it-works">How SBA Franchise Financing Works</h2>'
            '<ul>'
            '<li><strong>Program:</strong> SBA 7(a) (occasionally Express for smaller deals)</li>'
            '<li><strong>Loan size:</strong> Up to $5M (Express up to $500K with faster decision)</li>'
            '<li><strong>Rate:</strong> Prime + 2.5&ndash;3% on 7(a) (~10% in 2026); prime + 4.5&ndash;6.5% on Express</li>'
            '<li><strong>Term:</strong> 10 years on goodwill + working capital, 25 years if real estate included</li>'
            '<li><strong>Buyer equity:</strong> 10&ndash;15% (cash, no borrowed funds)</li>'
            '<li><strong>Seller carry:</strong> 5&ndash;10% second-position note allowed and common on resales</li>'
            '<li><strong>Personal guarantee:</strong> Required from 20%+ owners</li>'
            '<li><strong>Close time:</strong> 45&ndash;75 days at a Preferred Lender Bank</li>'
            '</ul>'
            '<h2 id="franchise-directory">The SBA Franchise Directory</h2>'
            '<p>The directory is the gating mechanism. SBA reviews and approves a franchise system&apos;s standard franchise agreement and FDD; if your brand is on the list, your loan moves through normal underwriting. If not listed, your franchisor must submit their documents to SBA (30&ndash;60 days). Major brands are listed; many newer or smaller brands aren&apos;t.</p>'
            '<p>Brands with smooth SBA approval history (high tier for ease of financing): <strong>Subway, Dunkin&apos;, Jersey Mike&apos;s, Wingstop, Tropical Smoothie Caf&eacute;, Smoothie King, Marco&apos;s Pizza, Anytime Fitness, Snap Fitness, The UPS Store, Mathnasium, Kumon, Christian Brothers Automotive, Jiffy Lube, Servpro</strong>.</p>'
            '<p>Categories that face more SBA scrutiny: full-service casual dining (high failure rate), bar/lounge concepts, certain fitness models with high closure rates, multi-level marketing-adjacent concepts.</p>'
            '<h2 id="fdd-item-19">FDD Item 19 &mdash; The Underwriting Source</h2>'
            '<p>The Franchise Disclosure Document Item 19 is the financial performance representation. It&apos;s the lender&apos;s primary tool for underwriting franchise unit economics:</p>'
            '<ul>'
            '<li><strong>Average unit volume (AUV)</strong> &mdash; revenue per location</li>'
            '<li><strong>Royalty + marketing fee structure</strong></li>'
            '<li><strong>Typical buildout cost</strong></li>'
            '<li><strong>Operating expense ranges</strong></li>'
            '<li><strong>Break-even timeline</strong></li>'
            '</ul>'
            '<p>Franchises without Item 19 disclosure (legally permitted but rare among mature brands) are significantly harder to finance &mdash; lender has no underwriting basis. If you&apos;re considering a brand that doesn&apos;t provide Item 19, expect lender pushback.</p>'
            '<h2 id="equity">Equity Injection Sources</h2>'
            '<ul>'
            '<li><strong>Personal savings:</strong> Cleanest source. Document with bank statements.</li>'
            '<li><strong>ROBS (Rollover for Business Startups):</strong> Use retirement account (401k, IRA) to fund equity injection without early-withdrawal penalty. Specialized providers: Guidant Financial, Benetrends, Tenet Financial Group.</li>'
            '<li><strong>Gift from family:</strong> Allowed with a gift letter (no expectation of repayment) and seasoning in your account 60+ days.</li>'
            '<li><strong>Home equity line of credit:</strong> Allowed by SBA but reduces your liquidity buffer; lenders may pressure-test it.</li>'
            '<li><strong>NOT allowed:</strong> Borrowing the equity injection from another loan or credit card.</li>'
            '</ul>'
            '<h2 id="lenders">Top Franchise SBA Lenders</h2>'
            '<ul>'
            '<li><strong>Live Oak Bank</strong> &mdash; largest SBA lender, dedicated franchise team, broad brand coverage</li>'
            '<li><strong>Celtic Bank</strong> &mdash; strong on QSR (quick-service restaurant) franchises</li>'
            '<li><strong>Byline Bank</strong> &mdash; fitness, education, service franchise specialty</li>'
            '<li><strong>US Bank Practice Finance + Franchise</strong> &mdash; mainstream brands, fast on returning borrowers</li>'
            '<li><strong>Wells Fargo SBA Lending</strong> &mdash; large brand coverage</li>'
            '<li><strong>Pinnacle Bank</strong> &mdash; regional but strong franchise specialty</li>'
            '<li><strong>Newtek (formerly Newtek Business Services Corp)</strong> &mdash; SBA non-bank lender, flexible on smaller deals</li>'
            '</ul>'
            '<h2 id="next-step">Next Step</h2>'
            '<p><a href="/match.html">Get matched with franchise-experienced SBA Preferred Lender Banks</a>. See also <a href="../sba-7a-vs-504-loan/">SBA 7(a) vs 504</a>, <a href="../how-long-sba-loan-approval/">SBA approval timeline</a>, and <a href="../can-you-use-sba-loan-to-buy-a-business/">SBA loan to buy a business</a>.</p>'
        ),
        "related_links": [
            ("../sba-7a-vs-504-loan/", "SBA 7(a) vs 504 Loan"),
            ("../how-long-sba-loan-approval/", "SBA Loan Approval Time"),
            ("../can-you-use-sba-loan-to-buy-a-business/", "SBA Loan to Buy a Business"),
            ("../how-much-down-payment-required-sba-loan/", "SBA Down Payment Requirements"),
            ("../sba-loan-vs-business-line-of-credit/", "SBA Loan vs Line of Credit"),
            ("/sba-loans.html", "SBA Loans Hub"),
        ],
        "related_cta_text": "Get Matched for Franchise SBA Loan",
        "toc": [("#how-it-works","How SBA Franchise Financing Works"),("#franchise-directory","SBA Franchise Directory"),("#fdd-item-19","FDD Item 19"),("#equity","Equity Injection Sources"),("#lenders","Top Franchise SBA Lenders"),("#next-step","Next Step")],
    },

    # ===== #24 Construction Equipment Financing =====
    {
        "file": "equipment-financing/articles/construction-equipment-financing-excavators-dozers/index.html",
        "canonical": "https://axiantpartners.com/equipment-financing/articles/construction-equipment-financing-excavators-dozers/",
        "breadcrumb_cluster": "Equipment Financing",
        "breadcrumb_cluster_url": "https://axiantpartners.com/equipment-financing.html",
        "breadcrumb_articles_url": "https://axiantpartners.com/equipment-financing/articles/",
        "breadcrumb_article_name": "Construction Equipment Financing",
        "title_tag": "Construction Equipment Financing: Excavators, Dozers, Loaders (2026) | Axiant",
        "og_title": "Construction Equipment Financing: Excavators, Dozers, Loaders",
        "meta_desc": "Construction equipment financing for excavators ($75K-$500K), dozers ($150K-$800K), loaders ($100K-$400K), skid steers ($30K-$80K). 6-12% APR, 36-72 month terms.",
        "og_desc": "Finance the full construction fleet: excavators, dozers, wheel loaders, skid steers, articulated trucks, motor graders. 6-12% APR, 0-20% down at 600+ FICO.",
        "twitter_desc": "Construction equipment financing: excavators $75K-500K, dozers $150K-800K, loaders, skid steers. 6-12% APR, 0-20% down.",
        "section": "Equipment Financing",
        "article_headline": "Construction Equipment Financing",
        "article_desc": "Equipment financing for construction contractors: excavators, dozers, wheel loaders, skid steers, articulated trucks, motor graders.",
        "image_url": "https://axiantpartners.com/assets/equipment-financing-hero.webp",
        "keywords": "construction equipment financing, excavator financing, dozer financing, wheel loader financing, skid steer financing, heavy equipment loan, caterpillar john deere financing",
        "speakable_name": "Construction Equipment Financing",
        "faqs": [
            ("How much does construction equipment cost?", "Wide range by class. <strong>Excavators</strong> (mini through large): $30K&ndash;$500K+. <strong>Bulldozers</strong>: $150K&ndash;$800K. <strong>Wheel loaders</strong>: $100K&ndash;$400K. <strong>Skid steers + compact track loaders</strong>: $30K&ndash;$80K. <strong>Backhoe loaders</strong>: $80K&ndash;$150K. <strong>Articulated dump trucks</strong>: $400K&ndash;$700K. <strong>Motor graders</strong>: $250K&ndash;$500K. <strong>Pavers + compactors</strong>: $50K&ndash;$300K. Most growing construction contractors finance the full fleet."),
            ("What credit score is needed for construction equipment financing?", "<strong>600+ FICO</strong> qualifies most established contractors. <strong>680+</strong> gets best rates. Specialty heavy-equipment lenders are flexible if the contractor has 2+ years operating + active contracts. New contractors with under 1 year operating typically need 25&ndash;30% down or a stronger personal credit anchor. OEM captive programs (Cat Financial, John Deere Financial, Komatsu Financial) often beat third-party rates on new equipment."),
            ("Should I buy or rent construction equipment?", "<strong>Buy if utilization is 70%+</strong> across the equipment&apos;s useful life. Equipment used 200+ days per year pays back the financing cost vs renting. <strong>Rent if utilization is under 50%</strong> or the equipment is for a specific project. Most established contractors own their core fleet (high-utilization machines) and rent peak-season or specialty equipment from a major rental house (United Rentals, Sunbelt Rentals, Herc Rentals)."),
            ("Can I finance used construction equipment?", "Yes &mdash; most lenders finance used construction equipment up to <strong>8&ndash;12 years old</strong> at similar rates to new with a 12-month dealer warranty. Auction purchases (Ritchie Bros, IronPlanet) finance but usually require 20&ndash;25% down. The equipment&apos;s hour meter, service history, and inspection report drive financing approval &mdash; lenders check these as carefully as the year-of-manufacture."),
            ("How do construction equipment financing rates compare to other equipment?", "Construction equipment runs <strong>6&ndash;12% APR</strong> in 2026 &mdash; comparable to most general equipment financing. OEM captive programs (Cat Financial, John Deere Financial) often beat third-party by 1&ndash;2%, especially on new equipment with promotional 0% or 1.99% offers. The premium over absolute floor rates reflects the equipment&apos;s exposure to construction-cycle volatility &mdash; recessions hit construction first."),
        ],
        "howto_name": "How to finance construction equipment",
        "howto_desc": "Five-step process for construction contractors financing excavators, dozers, loaders, and supporting equipment.",
        "howto_steps": [
            ("Get dealer quote with full spec sheet", "Cat, John Deere, Komatsu, Volvo Construction, Hyundai, Hitachi, Doosan, Kobelco are the major brands. Itemize attachments (buckets, hammers, augers), service contract, telematics."),
            ("Compare OEM captive + specialty + generalist lenders", "OEM captive (Cat Financial, John Deere Financial, Komatsu Financial) on new equipment. Specialty heavy-equipment (PEAC Solutions, Wells Fargo Equipment Finance, Pawnee). Generalist (Stearns, Live Oak)."),
            ("Pick loan vs lease vs $1 buyout based on use", "Loan or $1 buyout if 8+ year hold. Operating lease for 3-5 year refresh cycles. Section 179 + bonus depreciation favors loan structure."),
            ("Apply with contract pipeline + financials", "Contractors: include backlog/pipeline of signed contracts. 2-3 years tax returns, YTD P&L, bonding history, equipment insurance binders."),
            ("Close in 3-10 days with delivery acceptance", "Equipment loan close fast. First payment 30-45 days after funding."),
        ],
        "h1": "Construction Equipment Financing: Excavators, Dozers, Loaders &amp; More",
        "tagline": "Equipment financing for construction contractors &mdash; excavators, bulldozers, wheel loaders, skid steers, articulated trucks, motor graders &mdash; rate ranges, lenders, and OEM captive programs",
        "rail_back_text": "Back to Equipment Financing Articles",
        "rail_back_href": "../",
        "rail_facts": "Excavators $30K-$500K+, dozers $150K-$800K, loaders $100K-$400K, skid steers $30K-$80K. 6-12% APR, 36-72 mo, 0-20% down at 600+ FICO. OEM captives (Cat Financial, JD Financial) often best on new.",
        "rail_cta_h3": "Need construction equipment funded?",
        "rail_cta_p": "Get matched with construction equipment lenders and OEM captives.",
        "rail_cta_btn": "Get Matched for Construction Equipment",
        "quick_answer_html": 'Construction equipment financing covers the full contractor fleet: <strong>excavators</strong> ($30K&ndash;$500K+), <strong>bulldozers</strong> ($150K&ndash;$800K), <strong>wheel loaders</strong> ($100K&ndash;$400K), <strong>skid steers and compact track loaders</strong> ($30K&ndash;$80K), <strong>backhoe loaders</strong> ($80K&ndash;$150K), <strong>articulated dump trucks</strong> ($400K&ndash;$700K), <strong>motor graders</strong> ($250K&ndash;$500K), <strong>pavers and compactors</strong> ($50K&ndash;$300K). Financing runs <strong>6&ndash;12% APR</strong> over <strong>36&ndash;72 month terms</strong> with <strong>0&ndash;20% down</strong> at <strong>600+ FICO</strong>. <strong>OEM captives</strong> (Cat Financial, John Deere Financial, Komatsu Financial, Volvo Construction) often beat third-party rates by 1&ndash;2% on new equipment.',
        "intro_html": '<p>Construction equipment is one of the largest categories in equipment financing, driven by infrastructure spending, residential and commercial construction cycles, and demolition + site-prep volume. The four major OEMs &mdash; Caterpillar, John Deere, Komatsu, Volvo Construction Equipment &mdash; dominate the market with strong captive financing programs that compete hard with third-party lenders. This guide covers what construction equipment financing looks like by class, the loan-vs-lease question, and how to think about OEM captive vs specialty lender pricing. For the broader hub see <a href="/equipment-financing.html">equipment financing</a>.</p>',
        "body_sections_html": (
            '<h2 id="cost-table">Cost Ranges by Equipment Class</h2>'
            '<table style="width:100%; border-collapse: collapse; margin: 1.5rem 0;">'
            '<thead><tr style="background: var(--bg-card);"><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">Equipment</th><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">New</th><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">Used (3&ndash;5 yr)</th></tr></thead>'
            '<tbody>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Mini excavator (1&ndash;8 ton)</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$30K&ndash;$90K</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$15K&ndash;$55K</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Mid-size excavator (10&ndash;25 ton)</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$90K&ndash;$220K</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$50K&ndash;$140K</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Large excavator (30&ndash;90 ton)</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$250K&ndash;$500K+</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$130K&ndash;$320K</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Small dozer (D3&ndash;D6)</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$150K&ndash;$350K</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$80K&ndash;$220K</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Large dozer (D8&ndash;D11)</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$400K&ndash;$800K</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$220K&ndash;$500K</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Wheel loader</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$100K&ndash;$400K</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$50K&ndash;$240K</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Skid steer + compact track loader</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$30K&ndash;$80K</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$15K&ndash;$50K</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Backhoe loader</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$80K&ndash;$150K</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$40K&ndash;$90K</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Articulated dump truck</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$400K&ndash;$700K</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$220K&ndash;$450K</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Motor grader</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$250K&ndash;$500K</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$120K&ndash;$320K</td></tr>'
            '</tbody></table>'
            '<h2 id="brands">Major Brands &amp; OEM Captives</h2>'
            '<ul>'
            '<li><strong>Caterpillar</strong> &mdash; market leader; <strong>Cat Financial Services</strong> is the captive. Often runs 0%, 1.99%, or 2.99% promotional rates on new equipment 2&ndash;4 times per year.</li>'
            '<li><strong>John Deere Construction &amp; Forestry</strong> &mdash; <strong>John Deere Financial</strong> captive. Strong on excavators and skid steers.</li>'
            '<li><strong>Komatsu</strong> &mdash; <strong>Komatsu Financial</strong>. Strong on large excavators and articulated trucks.</li>'
            '<li><strong>Volvo Construction Equipment</strong> &mdash; <strong>Volvo Financial Services</strong>. Strong on wheel loaders and articulated trucks.</li>'
            '<li><strong>Hyundai Construction Equipment</strong>, <strong>Hitachi</strong>, <strong>Doosan</strong>, <strong>Kobelco</strong>, <strong>JCB</strong> &mdash; smaller market shares but competitive captive financing programs.</li>'
            '<li><strong>Bobcat</strong> (Doosan brand) &mdash; dominates the compact equipment segment.</li>'
            '</ul>'
            '<h2 id="lenders">Third-Party Lenders</h2>'
            '<ul>'
            '<li><strong>PEAC Solutions</strong> (formerly Marlin Capital) &mdash; heavy equipment specialty</li>'
            '<li><strong>Wells Fargo Equipment Finance</strong> &mdash; generalist with strong construction experience</li>'
            '<li><strong>Pawnee Leasing</strong> &mdash; flexible on used + challenged credit</li>'
            '<li><strong>Stearns Bank</strong> &mdash; broad equipment, fast approval</li>'
            '<li><strong>Live Oak Bank</strong> &mdash; SBA-experienced on $500K+ deals</li>'
            '<li><strong>Beacon Funding</strong>, <strong>Mission Financial</strong>, <strong>Currency Capital</strong> &mdash; specialty construction equipment lenders</li>'
            '</ul>'
            '<h2 id="loan-vs-lease">Loan vs Lease for Construction Equipment</h2>'
            '<ul>'
            '<li><strong>Equipment loan</strong> (36&ndash;72 mo, 6&ndash;12% APR, 0&ndash;20% down): owned at end, Section 179 + bonus depreciation in year one. Best when running equipment 8&ndash;12 year useful life.</li>'
            '<li><strong>$1 buyout lease</strong> (similar economics to loan): treated as financed purchase for tax. Section 179 + bonus depreciation apply.</li>'
            '<li><strong>Operating lease</strong> (36&ndash;60 mo): lower monthly than loan, no end-of-term ownership, fully deductible lease payment. Best for 3&ndash;5 yr refresh cycles.</li>'
            '<li><strong>Rental</strong>: not financing &mdash; pay daily/weekly/monthly rates. United Rentals, Sunbelt Rentals, Herc Rentals dominate. Right answer for low-utilization or project-specific equipment.</li>'
            '</ul>'
            '<h2 id="next-step">Next Step</h2>'
            '<p><a href="/match.html">Get matched with construction equipment lenders</a> &mdash; OEM captives, specialty heavy-equipment, and generalist in one application. See also <a href="../what-are-typical-equipment-financing-rates/">typical equipment financing rates</a> and <a href="../equipment-lease-vs-loan-vs-cash/">equipment lease vs loan vs cash</a>.</p>'
        ),
        "related_links": [
            ("../what-are-typical-equipment-financing-rates/", "Typical Equipment Financing Rates"),
            ("../equipment-lease-vs-loan-vs-cash/", "Equipment Lease vs Loan vs Cash"),
            ("../can-you-finance-used-equipment/", "Can You Finance Used Equipment?"),
            ("../do-you-need-down-payment-for-equipment-financing/", "Down Payment for Equipment Financing"),
            ("../section-179-tax-strategy-2026/", "Section 179 Tax Strategy 2026"),
            ("/equipment-financing.html", "Equipment Financing Hub"),
        ],
        "related_cta_text": "Get Matched for Construction Equipment",
        "toc": [("#cost-table","Cost Ranges"),("#brands","Brands &amp; OEM Captives"),("#lenders","Third-Party Lenders"),("#loan-vs-lease","Loan vs Lease"),("#next-step","Next Step")],
    },
]

if __name__ == "__main__":
    run(ARTICLES)
