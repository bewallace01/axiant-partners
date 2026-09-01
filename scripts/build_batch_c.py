"""Batch C of 11 — articles #29-#31 (denied loan, CMBS vs life-co vs agency, commercial solar)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from article_engine import run

ARTICLES = [
    # ===== #29 Business Loan Denied: What to Do =====
    {
        "file": "articles/business-loan-denied-what-to-do/index.html",
        "canonical": "https://axiantpartners.com/articles/business-loan-denied-what-to-do/",
        "breadcrumb_cluster": "Articles",
        "breadcrumb_cluster_url": "https://axiantpartners.com/articles/",
        "breadcrumb_articles_url": "https://axiantpartners.com/articles/",
        "breadcrumb_article_name": "Business Loan Denied: What to Do Next",
        "title_tag": "Business Loan Denied: What to Do Next (2026 Recovery Playbook) | Axiant",
        "og_title": "Business Loan Denied: 7 Steps to Reapproval",
        "meta_desc": "Business loan denied? Get the actual denial reason from the lender, fix the specific problem (credit, DSCR, time-in-business, docs), then reapply at a different lender type or with restructured deal.",
        "og_desc": "Recovery playbook for business loan denial: get the FCRA-required denial reason letter, identify the specific issue (credit, DSCR, TIB, collateral, docs), fix it, then reapply at the right lender type.",
        "twitter_desc": "Business loan denied: get the reason, fix the specific problem, reapply at the right lender type. 7-step recovery playbook.",
        "section": "Articles",
        "article_headline": "Business Loan Denied: What to Do Next",
        "article_desc": "Recovery playbook when a business loan application is denied: understanding the denial reason, fixing the underlying issue, and reapplying with a different lender or restructured deal.",
        "image_url": "https://axiantpartners.com/assets/axiant-hero-branded.webp",
        "keywords": "business loan denied, business loan denial reasons, what to do when denied a business loan, business loan rejected, denied SBA loan, business credit denied, reapply for business loan",
        "speakable_name": "Business Loan Denied: What to Do Next",
        "faqs": [
            ("Why was my business loan denied?", "The top 5 denial reasons in 2026 are: <strong>(1) Credit score below threshold</strong> &mdash; usually 600 for online, 680 for SBA, 720 for bank. <strong>(2) DSCR too low</strong> &mdash; lender&apos;s NOI/debt-service calc came out below 1.20&ndash;1.30x. <strong>(3) Time in business under threshold</strong> &mdash; 6 months for some online, 2+ years for SBA, 3+ years for bank. <strong>(4) Industry restriction</strong> &mdash; lender doesn&apos;t fund your industry (cannabis, adult, certain restaurants). <strong>(5) Documentation gaps</strong> &mdash; missing tax returns, no signed lease, no business plan. Get the FCRA-required denial reason letter to see your specific issue."),
            ("Does a denied business loan hurt my credit?", "<strong>Hard credit inquiries</strong> from loan applications drop your FICO 5&ndash;10 points temporarily &mdash; they age off after 12 months and stop affecting your score after 24 months. <strong>Multiple hard inquiries</strong> for the same loan type within 14&ndash;45 days are typically treated as one inquiry by FICO. The denial itself isn&apos;t reported to credit bureaus &mdash; only the inquiry. So 1&ndash;2 denials don&apos;t do lasting damage; 10+ inquiries in a quarter is a problem."),
            ("How long should I wait before reapplying for a business loan?", "Depends on what changed. <strong>Same lender + same situation</strong>: 90+ days minimum. <strong>Different lender type with the same deal</strong>: immediately (e.g., SBA denied $\\rightarrow$ try equipment loan or online). <strong>After fixing the denial reason</strong> (paid down debt, got new contract, fixed credit): 30&ndash;60 days after the fix is documented. <strong>After credit improvement</strong>: wait until next monthly credit reporting cycle so the lender sees the new score."),
            ("Can I get an SBA loan if I was denied conventional?", "<strong>Yes, often.</strong> SBA programs exist specifically to fund deals that don&apos;t fit standard bank underwriting. If you were denied by a bank because of: <strong>low collateral</strong> &mdash; SBA backstop solves this. <strong>Limited time in business</strong> &mdash; SBA Express and Microloans are more flexible than bank LOCs. <strong>Industry concern</strong> &mdash; SBA has broader industry tolerance than most banks. Common path: bank denial $\\rightarrow$ SBA Preferred Lender Bank with the same file."),
            ("What's the best alternative if I get denied by every lender?", "<strong>Revenue-based financing (RBF)</strong> or <strong>AR factoring</strong> for B2B businesses with receivables &mdash; these underwrite on revenue and customer credit, not your personal credit. <strong>Equipment-only financing</strong> if you need equipment specifically &mdash; the equipment serves as collateral, easier approval. <strong>Microloans</strong> from CDFIs (Community Development Financial Institutions) or non-profits if you&apos;re minority-owned, women-owned, or in an underserved community. <strong>Avoid MCAs</strong> unless absolutely emergency &mdash; 60&ndash;100% effective APR."),
        ],
        "howto_name": "How to recover from a business loan denial",
        "howto_desc": "Seven-step recovery playbook for business loan denials.",
        "howto_steps": [
            ("Get the FCRA-required denial reason letter", "Within 30 days of denial, the lender must send you a letter stating the reason (credit, DSCR, TIB, collateral, docs). This is your roadmap to fixing the problem."),
            ("Pull your business + personal credit reports", "Get free annual report from annualcreditreport.com. Check for errors. Dispute any inaccuracies. Address paid collections, recent late payments, credit utilization."),
            ("Identify the specific failure point", "Is it FICO, DSCR, time-in-business, industry, or documentation? Each has a different fix."),
            ("Fix the specific issue", "Credit: pay down revolving debt, dispute errors. DSCR: get new contracts, defer non-essential expenses. TIB: wait or use lenders with shorter TIB minimum. Docs: package complete file before reapplying."),
            ("Pick the right lender type for your reapplication", "Bank denial often = try SBA. SBA denial = try equipment loan or online lender. All denied = AR factoring or RBF if B2B with receivables."),
            ("Reapply with restructured deal if needed", "Sometimes a smaller loan, larger down payment, or additional collateral converts a denial to approval. Be willing to restructure."),
            ("Use a broker to shop pre-qualified offers", "Brokers can pre-screen which lenders will approve based on your profile, avoiding additional hard inquiries on lenders who will decline."),
        ],
        "h1": "Business Loan Denied: 7-Step Recovery Playbook",
        "tagline": "What to do when your business loan application gets denied &mdash; identify the actual reason, fix the specific problem, and reapply at the right lender type",
        "rail_back_text": "Back to Articles",
        "rail_back_href": "../",
        "rail_facts": "Top 5 denial reasons: low FICO, low DSCR, time in business, industry restriction, missing docs. FCRA denial letter within 30 days. Hard inquiries drop FICO 5-10 pts temporarily. Bank denial often = try SBA. Avoid MCAs unless emergency.",
        "rail_cta_h3": "Recently denied? Need a path forward?",
        "rail_cta_p": "Get matched with lenders likely to approve your specific situation.",
        "rail_cta_btn": "Get Matched for Business Financing",
        "quick_answer_html": 'When a business loan is denied, follow the 7-step recovery playbook. <strong>(1) Get the FCRA-required denial letter</strong> within 30 days &mdash; it states the specific reason. <strong>(2) Pull your business + personal credit reports</strong> and dispute any errors. <strong>(3) Identify the specific failure point</strong>: credit score, DSCR, time in business, industry, or documentation. <strong>(4) Fix the specific issue</strong> (different fix for each). <strong>(5) Pick the right lender type for reapplication</strong> &mdash; bank denial often means try SBA; SBA denial means try equipment loan or online lender. <strong>(6) Reapply with restructured deal</strong> if needed (smaller loan, larger down payment, additional collateral). <strong>(7) Use a broker</strong> to pre-screen lenders most likely to approve your profile. Hard inquiries drop FICO 5&ndash;10 pts temporarily; multiple inquiries for same loan type within 14&ndash;45 days count as one.',
        "intro_html": '<p>Getting denied for a business loan is more common than business owners realize &mdash; SBA denial rates run 30&ndash;40% across all submitted applications, and bank denial rates are even higher. Most denials are recoverable: the specific reason determines the specific fix, and many businesses that were denied by one lender type get approved by another type within 30&ndash;90 days. This guide is the actual recovery playbook. For related see <a href="../why-applying-multiple-banks-blindly-hurts-approval-odds/">why mass-applying hurts approval odds</a> and <a href="../how-to-compare-business-loan-offers/">how to compare business loan offers</a>.</p>',
        "body_sections_html": (
            '<h2 id="reasons">Top 5 Denial Reasons</h2>'
            '<table style="width:100%; border-collapse: collapse; margin: 1.5rem 0;">'
            '<thead><tr style="background: var(--bg-card);"><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">Denial Reason</th><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">Typical Trigger</th><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">Fix</th></tr></thead>'
            '<tbody>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Low credit score</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">FICO under lender threshold (varies 600&ndash;720)</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Pay down revolving, dispute errors, wait for reporting cycle</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Low DSCR</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">NOI/debt-service under 1.20&ndash;1.30x</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">New contracts, defer expenses, smaller loan, add equity</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Time in business</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Under lender minimum (6 mo&ndash;3 yr)</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Wait or try lender with shorter TIB minimum</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Industry restriction</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Lender doesn&apos;t fund your industry</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Switch to industry-friendly lender</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Documentation gaps</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Missing tax returns, lease, business plan</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Package complete file before reapplying</td></tr>'
            '</tbody></table>'
            '<h2 id="denial-letter">The FCRA Denial Reason Letter</h2>'
            '<p>Federal Fair Credit Reporting Act requires lenders to provide a written denial reason within 30 days. This letter is your roadmap. Common phrasings:</p>'
            '<ul>'
            '<li><strong>\"Insufficient income to support debt service\"</strong> = DSCR issue. Either grow revenue or reduce loan size.</li>'
            '<li><strong>\"Limited time in business\"</strong> = TIB threshold. Either wait or find shorter-TIB lender.</li>'
            '<li><strong>\"Credit score below acceptable range\"</strong> = FICO issue. Either improve credit or use lender with lower threshold.</li>'
            '<li><strong>\"Insufficient collateral\"</strong> = needs more collateral or equity. SBA programs designed to solve this.</li>'
            '<li><strong>\"Industry / business type not supported\"</strong> = industry restriction. Switch lenders.</li>'
            '</ul>'
            '<p>If your denial letter is vague, call the lender and ask specifically what factor would&apos;ve changed the decision. Most lenders will tell you.</p>'
            '<h2 id="lender-switch">Lender Type Switching</h2>'
            '<p>Denial at one lender type often means approval at another. Common pivots:</p>'
            '<ul>'
            '<li><strong>Bank denied $\\rightarrow$ SBA</strong>: SBA programs solve collateral, TIB, and industry restrictions that block bank approval. Apply through a Preferred Lender Bank (PLP).</li>'
            '<li><strong>SBA denied $\\rightarrow$ equipment loan</strong>: If the deal is equipment-heavy, equipment lenders use the asset as collateral and approve where SBA can&apos;t.</li>'
            '<li><strong>Bank + SBA denied $\\rightarrow$ online lender</strong>: Bluevine, OnDeck, Fundbox accept higher credit risk and price for it.</li>'
            '<li><strong>All denied $\\rightarrow$ AR factoring or RBF</strong>: B2B businesses with receivables qualify on customer credit, not personal credit.</li>'
            '<li><strong>Newer / minority-owned business denied $\\rightarrow$ CDFI / microloan</strong>: CDFIs (Community Development Financial Institutions) target underserved markets.</li>'
            '</ul>'
            '<h2 id="restructure">Restructuring the Deal</h2>'
            '<p>Sometimes a different deal structure converts denial to approval:</p>'
            '<ul>'
            '<li><strong>Smaller loan amount.</strong> Lender may approve $200K but not $300K. Reduce the ask.</li>'
            '<li><strong>Larger down payment.</strong> 10% denied $\\rightarrow$ 20% may approve. Reduces lender risk.</li>'
            '<li><strong>Additional collateral.</strong> Pledging additional business assets, personal assets, or a co-signer.</li>'
            '<li><strong>Shorter term.</strong> 10-yr denied $\\rightarrow$ 5-yr approved (less principal risk for lender).</li>'
            '<li><strong>Seller financing.</strong> On business acquisitions, seller carry of 10&ndash;15% reduces required bank loan.</li>'
            '</ul>'
            '<h2 id="avoid">What to Avoid</h2>'
            '<ul>'
            '<li><strong>Mass-applying to every lender</strong> &mdash; multiple hard inquiries drop your FICO further and don&apos;t fix the underlying issue.</li>'
            '<li><strong>MCAs as a quick fix</strong> &mdash; 60&ndash;100% effective APR. Should be true emergency only.</li>'
            '<li><strong>Stacking MCAs</strong> &mdash; multiple MCAs simultaneously is a death spiral. Default is common.</li>'
            '<li><strong>Predatory \"guaranteed approval\" lenders</strong> &mdash; usually MCA or factor-rate products marketed as loans. Read the fine print.</li>'
            '<li><strong>Personal credit damage</strong> &mdash; don&apos;t max personal cards to make business work; protects future personal financing options.</li>'
            '</ul>'
            '<h2 id="next-step">Next Step</h2>'
            '<p><a href="/match.html">Get matched with lenders likely to approve your situation</a> &mdash; brokers pre-screen so you&apos;re only applying where you have approval odds. See also <a href="../why-applying-multiple-banks-blindly-hurts-approval-odds/">why mass-applying hurts approval odds</a>, <a href="../business-loan-approval-timeline-by-lender-type/">approval timeline by lender type</a>, and <a href="../how-to-prequalify-business-loan/">how to prequalify for a business loan</a>.</p>'
        ),
        "related_links": [
            ("../why-applying-multiple-banks-blindly-hurts-approval-odds/", "Why Mass-Applying Hurts Approval Odds"),
            ("../business-loan-approval-timeline-by-lender-type/", "Business Loan Approval Timeline"),
            ("../how-to-prequalify-business-loan/", "How to Prequalify for a Business Loan"),
            ("../how-to-compare-business-loan-offers/", "How to Compare Business Loan Offers"),
            ("../../sba-loans/articles/sba-loan-vs-business-line-of-credit/", "SBA Loan vs Line of Credit"),
            ("/sba-loans.html", "SBA Loans Hub"),
        ],
        "related_cta_text": "Get Matched for Business Financing",
        "toc": [("#reasons","Top 5 Denial Reasons"),("#denial-letter","FCRA Denial Letter"),("#lender-switch","Lender Type Switching"),("#restructure","Restructuring the Deal"),("#avoid","What to Avoid"),("#next-step","Next Step")],
    },

    # ===== #30 CMBS vs Life-Co vs Agency =====
    {
        "file": "commercial-real-estate-loans/articles/cmbs-vs-life-company-vs-agency-debt/index.html",
        "canonical": "https://axiantpartners.com/commercial-real-estate-loans/articles/cmbs-vs-life-company-vs-agency-debt/",
        "breadcrumb_cluster": "Commercial Real Estate Loans",
        "breadcrumb_cluster_url": "https://axiantpartners.com/commercial-real-estate-loans.html",
        "breadcrumb_articles_url": "https://axiantpartners.com/commercial-real-estate-loans/articles/",
        "breadcrumb_article_name": "CMBS vs Life-Company vs Agency Debt",
        "title_tag": "CMBS vs Life-Company vs Agency Debt: Commercial Mortgage Compared (2026) | Axiant",
        "og_title": "CMBS vs Life-Company vs Agency Debt (2026)",
        "meta_desc": "CMBS, life-insurance company, and agency (Fannie/Freddie/FHA) debt compared: rates, LTV, terms, recourse, prepayment. By property type and sponsor profile.",
        "og_desc": "Commercial mortgage decision tree: CMBS for non-recourse 10-yr balloon, life-company for lowest fixed rates, Fannie/Freddie/FHA for multifamily. Side-by-side comparison.",
        "twitter_desc": "CMBS vs life-co vs agency debt: rates, LTV, recourse, prepayment compared. By property type + sponsor.",
        "section": "Commercial Real Estate Loans",
        "article_headline": "CMBS vs Life-Company vs Agency Debt",
        "article_desc": "Decision framework comparing CMBS, life-insurance company, and agency (Fannie Mae, Freddie Mac, FHA) commercial mortgage programs by property type and sponsor profile.",
        "image_url": "https://axiantpartners.com/assets/multifamily-loan-hero.webp",
        "keywords": "cmbs vs life company, agency debt vs cmbs, fannie mae multifamily, freddie mac optigo, life insurance company commercial mortgage, FHA 223f, commercial mortgage comparison",
        "speakable_name": "CMBS vs Life-Company vs Agency Debt",
        "faqs": [
            ("What's the difference between CMBS and life-company debt?", "<strong>CMBS</strong> (Commercial Mortgage-Backed Securities) loans are originated by banks and securitized into bond pools sold to investors. Standard terms: 65&ndash;75% LTV, 6.5&ndash;8% rate, 10-yr balloon with 25&ndash;30 yr amortization, non-recourse, expensive prepayment (defeasance). <strong>Life-company debt</strong> is held on the insurance company&apos;s balance sheet rather than securitized. Standard terms: 60&ndash;70% LTV, 6&ndash;7.5% rate (often cheapest on stronger sponsors), 5/7/10/15-yr terms, partial recourse common, more flexible prepayment. Life-companies prefer stronger sponsors and lower-leverage deals."),
            ("What is agency debt for multifamily?", "<strong>Agency debt</strong> = Fannie Mae and Freddie Mac multifamily mortgages, plus FHA/HUD programs. <strong>Fannie Mae DUS</strong> (Delegated Underwriting and Servicing) is the standard multifamily product for $1M+ loans, 65&ndash;80% LTV, ~6&ndash;7% rate, 5/7/10/12/15-yr terms, partial recourse. <strong>Freddie Mac Optigo</strong> is the Fannie equivalent with similar terms. <strong>FHA 223(f) for multifamily refinance/acquisition</strong>: 85% LTV, 35-yr fully amortizing, 6&ndash;7%, fully assumable, but 6&ndash;9 month close."),
            ("Which is cheapest for a $5M apartment building?", "Depends on sponsor. <strong>For stabilized $5M multifamily</strong>: <strong>Freddie SBL (Small Balance Loan)</strong> often best at $1M&ndash;$7.5M &mdash; 80% LTV, ~6&ndash;7% rate, non-recourse, no environmental requirement on smaller deals. <strong>Fannie DUS</strong> close second. <strong>Life-company</strong> may match if sponsor is strong and willing to accept partial recourse. <strong>CMBS</strong> usually beat on rate by 50&ndash;100 bps for multifamily because agencies have funding cost advantage."),
            ("Which is best for retail / office / industrial?", "<strong>CMBS</strong> is the default for non-multifamily commercial. Office, retail, industrial, hospitality at 65&ndash;75% LTV $5M&ndash;$50M typically go CMBS for non-recourse + max leverage. <strong>Life-company</strong> wins on lower-leverage (under 65% LTV) deals with strong sponsors who want partial or no recourse and flexible prepayment. <strong>Conventional bank</strong> wins on $1M&ndash;$5M deals or sponsors with existing bank relationships."),
            ("What's the prepayment penalty difference?", "<strong>CMBS:</strong> Defeasance (replacing the property collateral with Treasuries) or yield maintenance. Expensive &mdash; $50K&ndash;$500K+ to exit early. <strong>Life-company:</strong> Yield maintenance typical, simpler than CMBS defeasance. <strong>Fannie/Freddie:</strong> Yield maintenance during locked period, then step-down (e.g., 5-4-3-2-1%) in later years. <strong>FHA:</strong> Step-down prepay over first 5&ndash;10 years. <strong>Bank conventional:</strong> Often simple 3-5% declining or no penalty after year 3."),
        ],
        "howto_name": "How to choose between CMBS, life-company, and agency debt",
        "howto_desc": "Five-step decision framework for picking the right commercial mortgage program.",
        "howto_steps": [
            ("Identify property type", "Multifamily: agency (Fannie/Freddie/FHA) usually wins. Retail/office/industrial: CMBS or life-company. Hotel: CMBS or SBA 504. Self-storage: agency or CMBS."),
            ("Identify LTV target", "Max leverage (75-80%): CMBS or agency. Moderate (60-70%): life-company or CMBS. Conservative (under 60%): life-company often best rate."),
            ("Identify recourse tolerance", "Non-recourse required: CMBS, agency, or life-company (some). Recourse OK: bank conventional or SBA 504 (cheaper rate)."),
            ("Identify hold period", "10-yr hold: CMBS or 10-yr life-co. 5-7 yr: life-company. 15+ yr: FHA 223(f) or 35-yr fully amort."),
            ("Identify prepayment flexibility need", "May refinance early: avoid CMBS (expensive defeasance). Hold to maturity: CMBS fine. Want flexibility: life-co or bank conventional."),
        ],
        "h1": "CMBS vs Life-Company vs Agency Debt: Commercial Mortgage Compared",
        "tagline": "Decision framework for commercial mortgage programs &mdash; when CMBS wins, when life-insurance company debt is cheaper, when Fannie/Freddie/FHA agency debt is the right call for multifamily",
        "rail_back_text": "Back to CRE Loan Articles",
        "rail_back_href": "../",
        "rail_facts": "CMBS: 65-75% LTV, 6.5-8%, 10-yr balloon, non-recourse, defeasance prepay. Life-co: 60-70% LTV, 6-7.5%, flex term, partial recourse, YM prepay. Agency multifamily (Fannie/Freddie/FHA): 65-85% LTV, 6-7%, various terms.",
        "rail_cta_h3": "Need a commercial mortgage?",
        "rail_cta_p": "Get matched with CMBS originators, life-companies, and agency multifamily lenders.",
        "rail_cta_btn": "Get Matched for CRE Financing",
        "quick_answer_html": 'Three main institutional commercial mortgage programs in 2026. <strong>CMBS</strong> (Commercial Mortgage-Backed Securities): 65&ndash;75% LTV, 6.5&ndash;8% rate, 10-yr balloon with 25&ndash;30 yr amortization, non-recourse, expensive defeasance prepayment. Best for max-leverage retail/office/industrial $5M&ndash;$50M. <strong>Life-insurance company debt</strong>: 60&ndash;70% LTV, 6&ndash;7.5% rate (often cheapest), 5/7/10/15-yr flexible terms, partial recourse common, simpler yield-maintenance prepayment. Best for lower-leverage stronger-sponsor deals. <strong>Agency multifamily</strong>: Fannie DUS, Freddie Optigo SBL, FHA 223(f). 65&ndash;85% LTV, 6&ndash;7%, varied terms. Best for $1M+ multifamily acquisition/refinance &mdash; usually beats CMBS on rate by 50&ndash;100 bps.',
        "intro_html": '<p>Commercial mortgage programs are deeply segmented &mdash; the right product for a $5M Class-A multifamily acquisition is fundamentally different from a $20M Marriott CMBS refinance or a $15M industrial life-company permanent debt. This guide breaks down when each program wins and the trade-offs between them. For property-specific deep-dives see <a href="../multifamily-loan-down-payment/">multifamily loan down payment</a>, <a href="../hotel-financing-sba-cmbs-conventional/">hotel financing</a>, and <a href="../self-storage-facility-financing-acquisitions/">self-storage financing</a>.</p>',
        "body_sections_html": (
            '<h2 id="comparison-table">Side-by-Side Comparison</h2>'
            '<table style="width:100%; border-collapse: collapse; margin: 1.5rem 0;">'
            '<thead><tr style="background: var(--bg-card);"><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">Dimension</th><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">CMBS</th><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">Life-Company</th><th style="padding: 12px 16px; text-align: left; border: 1px solid var(--border-color);">Agency Multifamily</th></tr></thead>'
            '<tbody>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Loan size</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$3M&ndash;$200M+</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$10M&ndash;$300M+</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">$1M&ndash;$200M+</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Rate (2026)</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">6.5&ndash;8%</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">6&ndash;7.5%</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">6&ndash;7%</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">LTV max</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">75%</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">70% (typical)</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">80%, FHA 85%</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Term</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">10-yr balloon</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">5, 7, 10, 15-yr</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">5, 7, 10, 12, 15-yr; FHA 35-yr</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Amortization</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">25&ndash;30 yr</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">25&ndash;30 yr</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">25&ndash;30 yr; FHA fully amort</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Recourse</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Non-recourse</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Partial / non-recourse</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Non-recourse w/ standard carve-outs</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Prepayment</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Defeasance / YM</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Yield maintenance</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">YM then step-down</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Close time</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">60&ndash;90 days</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">60&ndash;120 days</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">45&ndash;75 days; FHA 6&ndash;9 mo</td></tr>'
            '<tr><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Best property types</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Retail, office, industrial, hotel</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">All except hotel; stronger sponsors</td><td style="padding: 12px 16px; border: 1px solid var(--border-color);">Multifamily only (Fannie/Freddie/FHA)</td></tr>'
            '</tbody></table>'
            '<h2 id="cmbs">When CMBS Wins</h2>'
            '<ul>'
            '<li><strong>Non-multifamily commercial</strong> at max leverage (70&ndash;75% LTV) on stabilized properties</li>'
            '<li><strong>Hold-to-maturity strategy</strong> &mdash; you intend to sell or refinance at the 10-yr balloon, so expensive prepayment doesn&apos;t hurt</li>'
            '<li><strong>Need non-recourse</strong> debt without the constraints of life-company underwriting</li>'
            '<li><strong>Top originators:</strong> JPMorgan, Wells Fargo, Deutsche Bank, Citi, Morgan Stanley, Goldman Sachs, Bank of America</li>'
            '</ul>'
            '<h2 id="life-company">When Life-Company Wins</h2>'
            '<ul>'
            '<li><strong>Lower-leverage deals</strong> (60&ndash;65% LTV) &mdash; life-companies price these below CMBS</li>'
            '<li><strong>Strong-sponsor borrowers</strong> with track record + balance sheet</li>'
            '<li><strong>Need flexible term</strong> &mdash; 5, 7, 15-yr options vs CMBS&apos; rigid 10-yr</li>'
            '<li><strong>May refinance early</strong> &mdash; yield maintenance simpler than CMBS defeasance</li>'
            '<li><strong>Top life-companies:</strong> Prudential, MetLife, New York Life, Northwestern Mutual, TIAA, Principal, Pacific Life, Mass Mutual, Voya</li>'
            '</ul>'
            '<h2 id="agency">When Agency (Fannie/Freddie/FHA) Wins for Multifamily</h2>'
            '<ul>'
            '<li><strong>Multifamily acquisition or refinance</strong> &mdash; agencies have funding cost advantage of 50&ndash;100 bps over CMBS for multifamily</li>'
            '<li><strong>Fannie DUS</strong>: $1M+, 65&ndash;80% LTV, 5/7/10/12/15-yr, ~6&ndash;7%, partial recourse on standard structure</li>'
            '<li><strong>Freddie Optigo Conventional</strong>: $1M+, similar terms to Fannie DUS</li>'
            '<li><strong>Freddie SBL (Small Balance Loan)</strong>: $1M&ndash;$7.5M, 80% LTV, ~6&ndash;7%, non-recourse, no environmental on under $5M &mdash; often best on smaller multifamily</li>'
            '<li><strong>FHA 223(f)</strong>: 85% LTV, 35-yr fully amortizing, ~6&ndash;7%, fully assumable. 6&ndash;9 month close.</li>'
            '<li><strong>Top agency originators:</strong> Walker &amp; Dunlop, Berkadia, CBRE Capital, JLL, Greystone, Newmark, Hunt Capital Partners</li>'
            '</ul>'
            '<h2 id="decision">Decision Shortcut</h2>'
            '<ul>'
            '<li><strong>Multifamily $1M&ndash;$7.5M:</strong> Freddie SBL first.</li>'
            '<li><strong>Multifamily $5M+:</strong> Fannie DUS or Freddie Optigo Conventional.</li>'
            '<li><strong>Multifamily refi with long-term hold:</strong> FHA 223(f) for 35-yr fully amort.</li>'
            '<li><strong>Office/retail/industrial at max leverage:</strong> CMBS.</li>'
            '<li><strong>Office/retail/industrial moderate leverage, strong sponsor:</strong> Life-company.</li>'
            '<li><strong>Hotel:</strong> CMBS at $5M+, SBA 504 under $5.5M. See <a href="../hotel-financing-sba-cmbs-conventional/">hotel financing</a>.</li>'
            '</ul>'
            '<h2 id="next-step">Next Step</h2>'
            '<p><a href="/match.html">Get matched with CRE lenders</a> across CMBS, life-company, and agency multifamily. See also <a href="../multifamily-loan-down-payment/">multifamily loan down payment</a>, <a href="../hotel-financing-sba-cmbs-conventional/">hotel financing</a>, and <a href="../self-storage-facility-financing-acquisitions/">self-storage financing</a>.</p>'
        ),
        "related_links": [
            ("../multifamily-loan-down-payment/", "Multifamily Loan Down Payment"),
            ("../hotel-financing-sba-cmbs-conventional/", "Hotel Financing: SBA, CMBS, Conventional"),
            ("../self-storage-facility-financing-acquisitions/", "Self-Storage Facility Financing"),
            ("../dscr-rental-loans-real-estate-investors/", "DSCR Rental Loans"),
            ("../how-fast-can-you-close-commercial-bridge-loan/", "How Fast Can You Close a Bridge Loan"),
            ("/commercial-real-estate-loans.html", "CRE Loans Hub"),
        ],
        "related_cta_text": "Get Matched for CRE Financing",
        "toc": [("#comparison-table","Side-by-Side Comparison"),("#cmbs","When CMBS Wins"),("#life-company","When Life-Company Wins"),("#agency","When Agency Wins (Multifamily)"),("#decision","Decision Shortcut"),("#next-step","Next Step")],
    },

    # ===== #31 Commercial Solar Financing =====
    {
        "file": "equipment-financing/articles/commercial-solar-financing/index.html",
        "canonical": "https://axiantpartners.com/equipment-financing/articles/commercial-solar-financing/",
        "breadcrumb_cluster": "Equipment Financing",
        "breadcrumb_cluster_url": "https://axiantpartners.com/equipment-financing.html",
        "breadcrumb_articles_url": "https://axiantpartners.com/equipment-financing/articles/",
        "breadcrumb_article_name": "Commercial Solar Financing",
        "title_tag": "Commercial Solar Financing: PPA, Lease, Loan, C-PACE Compared (2026) | Axiant",
        "og_title": "Commercial Solar Financing: PPA vs Lease vs Loan vs C-PACE",
        "meta_desc": "Commercial solar financing: solar loans (5-9% APR, ownership + ITC), PPAs (no upfront cost, 10-25 yr off-take), operating leases, and C-PACE. By system size and ownership preference.",
        "og_desc": "Commercial solar financing options for businesses: solar loans capturing 30%+ ITC + accelerated depreciation, PPAs for no-upfront systems, operating leases, C-PACE for property-secured.",
        "twitter_desc": "Commercial solar financing: solar loan (own + 30% ITC), PPA (no upfront), lease, C-PACE. By system size + ownership pref.",
        "section": "Equipment Financing",
        "article_headline": "Commercial Solar Financing",
        "article_desc": "Financing for commercial solar installations: solar loans, power purchase agreements, operating leases, and C-PACE programs for businesses and property owners.",
        "image_url": "https://axiantpartners.com/assets/equipment-financing-hero.webp",
        "keywords": "commercial solar financing, solar loan, solar PPA, solar lease, commercial solar PPA, C-PACE solar, solar ITC, business solar financing",
        "speakable_name": "Commercial Solar Financing",
        "faqs": [
            ("How do businesses finance commercial solar?", "Four main paths in 2026. <strong>Solar loan</strong> (5&ndash;9% APR, 10&ndash;20 yr term): business owns the system and captures the 30% federal Investment Tax Credit (ITC) + accelerated depreciation (MACRS bonus). <strong>Power Purchase Agreement (PPA)</strong>: third party owns the system on your roof; you buy the electricity at a fixed rate for 10&ndash;25 years. No upfront cost but you don&apos;t capture ITC. <strong>Operating lease</strong>: middle ground &mdash; lower upfront than loan, lessee gets some tax benefits. <strong>C-PACE</strong> (Commercial Property Assessed Clean Energy): property-secured financing repaid through property tax assessment, 20&ndash;30 yr term, transferable on property sale."),
            ("What's the federal Investment Tax Credit (ITC) for solar in 2026?", "<strong>30% federal ITC</strong> on qualifying commercial solar installations through 2032 under the Inflation Reduction Act. The credit applies to system + installation costs and can be combined with <strong>accelerated depreciation</strong> (MACRS 5-year + bonus depreciation). Combined federal benefits typically recover <strong>40&ndash;50% of system cost</strong> in the first 1&ndash;6 years for owned systems. PPA arrangements don&apos;t capture ITC for the customer &mdash; the third-party owner does."),
            ("How much does commercial solar cost?", "Wide range by system size. <strong>Small commercial (50&ndash;200 kW)</strong>: $1.50&ndash;$2.50 per watt installed = $75K&ndash;$500K. <strong>Mid-size (200&ndash;500 kW)</strong>: $1.30&ndash;$2.00 per watt = $260K&ndash;$1M. <strong>Large commercial / industrial (500 kW&ndash;1 MW+)</strong>: $1.10&ndash;$1.80 per watt = $550K&ndash;$1.8M+. Costs include panels, inverters, racking, installation, interconnection, permitting. Costs have come down 60% over the past decade."),
            ("Should I use a solar loan or PPA?", "<strong>Solar loan</strong> if: business is profitable enough to capture ITC + depreciation benefits, plans to own the building 8+ years, has access to financing. <strong>PPA</strong> if: business doesn&apos;t have tax appetite to use ITC (non-profit, low-profit), wants zero upfront cost, doesn&apos;t want operations responsibility for the system, willing to forgo long-term ownership economics. Loan typically has better 10-yr economics for tax-paying businesses; PPA easier and risk-free."),
            ("What is C-PACE and how does it work for solar?", "<strong>C-PACE (Commercial Property Assessed Clean Energy)</strong> is property-secured financing for energy efficiency and renewable improvements, repaid through a special tax assessment on the property. <strong>20&ndash;30 year terms</strong>, <strong>fixed rate ~5&ndash;7%</strong>, <strong>up to 100% project financing</strong> (no down payment). <strong>Transferable on property sale</strong> &mdash; the obligation stays with the property. Available in <strong>30+ states</strong> with active C-PACE programs. Best for commercial property owners doing larger solar + efficiency projects."),
        ],
        "howto_name": "How to finance commercial solar",
        "howto_desc": "Five-step process for choosing and structuring commercial solar financing.",
        "howto_steps": [
            ("Get 3+ installer quotes with system specs", "Reputable installers will quote $/watt, expected production (kWh/yr), warranty terms. Compare apples-to-apples by $/kWh produced lifetime."),
            ("Determine ITC + depreciation appetite", "If business is profitable, owned system captures 30% ITC + MACRS bonus depreciation - 40-50% federal benefit. Talk to CPA on your tax situation."),
            ("Pick the financing structure", "Profitable + 8+ yr hold + want ownership: solar loan. No tax appetite or want zero risk: PPA. Property-secured + larger project: C-PACE. Middle ground: operating lease."),
            ("Lock interconnection + utility agreements", "Utility interconnection approval takes 30-90 days. Net metering or NEM 3.0 terms determine production economics. Some states have queues."),
            ("Close + install (90-180 days total)", "Permits 30-60 d, install 30-60 d, interconnection commissioning 30-60 d. ITC + depreciation captured in tax year system is placed in service."),
        ],
        "h1": "Commercial Solar Financing: Loan, PPA, Lease &amp; C-PACE Compared",
        "tagline": "How businesses finance commercial solar in 2026 &mdash; capturing the 30% federal ITC + accelerated depreciation through ownership, vs PPA for zero upfront cost, plus C-PACE for property-secured financing",
        "rail_back_text": "Back to Equipment Financing Articles",
        "rail_back_href": "../",
        "rail_facts": "Solar loan: 5-9% APR, 10-20 yr, captures 30% ITC + MACRS depreciation. PPA: zero upfront, 10-25 yr off-take, no ITC for customer. C-PACE: 20-30 yr, 5-7%, up to 100% LTV, transferable. Costs $1.10-$2.50/watt installed.",
        "rail_cta_h3": "Need commercial solar financing?",
        "rail_cta_p": "Get matched with solar loan lenders, PPA providers, and C-PACE programs.",
        "rail_cta_btn": "Get Matched for Solar Financing",
        "quick_answer_html": 'Commercial solar financing in 2026 has four main paths. <strong>Solar loan</strong> (5&ndash;9% APR, 10&ndash;20 yr term): business owns the system, captures <strong>30% federal Investment Tax Credit (ITC)</strong> + <strong>accelerated MACRS depreciation</strong> (combined 40&ndash;50% federal benefit recovered in first 1&ndash;6 years). <strong>Power Purchase Agreement (PPA)</strong>: third-party owns the system, business buys electricity at fixed rate for 10&ndash;25 years, zero upfront cost but no ITC for customer. <strong>Operating lease</strong>: middle ground &mdash; lower upfront than loan, lessee gets some tax benefits. <strong>C-PACE</strong> (Commercial Property Assessed Clean Energy): property-secured financing repaid via property tax assessment, 20&ndash;30 yr term, 5&ndash;7% rate, up to 100% LTV, transferable on property sale. <strong>Installed cost</strong>: $1.10&ndash;$2.50 per watt depending on system size.',
        "intro_html": '<p>Commercial solar economics in 2026 have never been better &mdash; system costs have dropped ~60% in the past decade, the federal Investment Tax Credit is locked at 30% through 2032, and financing options have matured. The right financing path depends on tax appetite, ownership preference, and project size. This guide breaks down the four main structures and when each wins. For related see <a href="../section-179-tax-strategy-2026/">Section 179 tax strategy 2026</a> and <a href="/equipment-financing.html">equipment financing</a>.</p>',
        "body_sections_html": (
            '<h2 id="solar-loan">Solar Loan (Ownership + Tax Benefits)</h2>'
            '<ul>'
            '<li><strong>Rate:</strong> 5&ndash;9% APR (lower with strong credit and SBA-backed solar programs)</li>'
            '<li><strong>Term:</strong> 10&ndash;20 years typical</li>'
            '<li><strong>Down payment:</strong> 0&ndash;20%</li>'
            '<li><strong>Tax benefits captured:</strong> 30% federal ITC, MACRS 5-year accelerated depreciation, bonus depreciation (60% in 2026)</li>'
            '<li><strong>Best for:</strong> Profitable businesses with tax appetite, 8+ year property hold, want long-term system economics</li>'
            '<li><strong>Top lenders:</strong> Sunrun Commercial, Mosaic, Sungage Financial, Live Oak Bank solar, GreenTree Energy Finance, regional banks with solar specialty</li>'
            '</ul>'
            '<h2 id="ppa">Power Purchase Agreement (PPA)</h2>'
            '<ul>'
            '<li><strong>Structure:</strong> Third-party developer installs and owns the system on your roof / property. You buy the electricity it generates at a fixed $/kWh rate for the term.</li>'
            '<li><strong>Upfront cost:</strong> $0 to customer</li>'
            '<li><strong>Term:</strong> 10&ndash;25 years</li>'
            '<li><strong>Rate structure:</strong> Fixed $/kWh, typically 10&ndash;30% below current utility rate, with annual escalator (1&ndash;3%)</li>'
            '<li><strong>Tax benefits:</strong> Captured by the system owner (developer), not you. Pass-through pricing reflects developer&apos;s benefit.</li>'
            '<li><strong>Best for:</strong> Non-profits, low-profit businesses with no tax appetite, businesses that want zero risk and no operational responsibility</li>'
            '<li><strong>Top providers:</strong> Sunrun Commercial, Sunrock Distributed Solar, Standard Solar, Cypress Creek Renewables</li>'
            '</ul>'
            '<h2 id="operating-lease">Operating Lease</h2>'
            '<ul>'
            '<li><strong>Structure:</strong> Lease the system from a financing company; payments deductible as operating expense; some lease structures give lessee depreciation benefits</li>'
            '<li><strong>Upfront cost:</strong> $0&ndash;10% down</li>'
            '<li><strong>Term:</strong> 10&ndash;15 years</li>'
            '<li><strong>Best for:</strong> Middle ground between loan and PPA &mdash; some tax benefits captured, less risk than ownership, more economics than PPA</li>'
            '<li><strong>Top providers:</strong> Sungage Financial, Renew Financial, Sunrun TPO (third-party ownership)</li>'
            '</ul>'
            '<h2 id="c-pace">C-PACE (Commercial Property Assessed Clean Energy)</h2>'
            '<p>Property-secured financing repaid via special property tax assessment:</p>'
            '<ul>'
            '<li><strong>Term:</strong> 20&ndash;30 years (matches useful life of improvements)</li>'
            '<li><strong>Rate:</strong> 5&ndash;7% fixed (often best rate available)</li>'
            '<li><strong>LTV:</strong> Up to 100% project financing &mdash; no down payment required</li>'
            '<li><strong>Repayment:</strong> Added to property tax bill as a special assessment, paid alongside normal taxes</li>'
            '<li><strong>Transferable:</strong> Obligation stays with the property on sale &mdash; new owner picks up the C-PACE payment</li>'
            '<li><strong>Eligible projects:</strong> Solar PV, energy efficiency, water conservation, resilience (storm-hardening)</li>'
            '<li><strong>Available in 30+ states</strong>: CA, NY, FL, TX, CO, OH, MD, MN, MO, NV, RI, VT, CT, DC, others. Programs vary by state.</li>'
            '<li><strong>Best for:</strong> Commercial property owners on larger solar + efficiency projects; especially attractive to owners planning to sell within 5&ndash;10 years (obligation transfers with property)</li>'
            '</ul>'
            '<h2 id="economics">Worked Economics: $300K Solar System</h2>'
            '<p>200 kW commercial rooftop, $1.50/watt installed = $300K project cost. Profitable business at 25% effective tax rate.</p>'
            '<h3>Solar Loan Path</h3>'
            '<ul>'
            '<li>Cash at close: $30K (10% down)</li>'
            '<li>Loan: $270K at 7% over 15 years &mdash; ~$2,425/mo</li>'
            '<li>30% ITC = $90K credit against current-year tax liability</li>'
            '<li>MACRS bonus depreciation year one = ~$110K deduction = ~$27.5K tax savings</li>'
            '<li>Year 1 net cash flow: -$30K (down) + $90K (ITC) + $27.5K (depreciation savings) - $29K (loan payments) = <strong>+$58.5K positive</strong></li>'
            '<li>Plus electricity savings of ~$30K/yr going forward</li>'
            '</ul>'
            '<h3>PPA Path</h3>'
            '<ul>'
            '<li>Cash at close: $0</li>'
            '<li>Electricity cost reduction: ~$15K/yr (smaller than ownership because developer captures the difference)</li>'
            '<li>Year 1 net cash flow: +$15K</li>'
            '<li>No ITC, no depreciation</li>'
            '<li>20-yr total benefit: ~$300K (less than ownership&apos;s ~$500K+)</li>'
            '</ul>'
            '<p>For profitable businesses, ownership wins on 20-year economics. PPA is simpler and zero-risk.</p>'
            '<h2 id="next-step">Next Step</h2>'
            '<p><a href="/match.html">Get matched with commercial solar lenders</a> &mdash; solar loan providers, PPA developers, C-PACE programs. See also <a href="../section-179-tax-strategy-2026/">Section 179 tax strategy 2026</a> and <a href="/equipment-financing.html">equipment financing</a>.</p>'
        ),
        "related_links": [
            ("../section-179-tax-strategy-2026/", "Section 179 Tax Strategy 2026"),
            ("../equipment-lease-vs-loan-vs-cash/", "Equipment Lease vs Loan vs Cash"),
            ("../what-are-typical-equipment-financing-rates/", "Typical Equipment Financing Rates"),
            ("../manufacturing-equipment-financing-cnc-press-brakes/", "Manufacturing Equipment Financing"),
            ("../warehouse-racking-storage-financing/", "Warehouse Racking + Storage Financing"),
            ("/equipment-financing.html", "Equipment Financing Hub"),
        ],
        "related_cta_text": "Get Matched for Solar Financing",
        "toc": [("#solar-loan","Solar Loan"),("#ppa","Power Purchase Agreement"),("#operating-lease","Operating Lease"),("#c-pace","C-PACE"),("#economics","Worked Economics"),("#next-step","Next Step")],
    },
]

if __name__ == "__main__":
    run(ARTICLES)
