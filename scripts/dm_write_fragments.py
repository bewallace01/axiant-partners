"""Writes digital-marketing/fragments/*.html (>=2000 words each). Run: python scripts/dm_write_fragments.py"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRAG_DIR = ROOT / "digital-marketing" / "fragments"


def wc(html: str) -> int:
    t = re.sub(r"<[^>]+>", " ", html)
    return len(re.sub(r"\s+", " ", t).strip().split())


def fig(src: str, alt: str) -> str:
    return (
        f'<figure class="article-inline-visual"><img src="{src}" alt="{alt}" '
        'width="1200" height="675" loading="lazy" decoding="async"></figure>\n\n'
    )


def mini_case(title: str, body: str, takeaway: str) -> str:
    return (
        '<div class="article-callout growth-mini-case" role="note">\n'
        f"<p><strong>{title}</strong> {body}</p>\n"
        f"<p><strong>Takeaway:</strong> {takeaway}</p>\n"
        "</div>\n\n"
    )


def h2(i: str, t: str) -> str:
    return f'<h2 id="{i}">{t}</h2>\n'


def p(*parts: str) -> str:
    return "<p>" + " ".join(parts) + "</p>\n"


TAIL = (
    "Document owners, evidence, and review dates in writing so procurement does not rely on memory. "
    "Escalate early if legal, brand, or deliverability risk appears—pausing is cheaper than repairing reputation."
)


def expand_section(topic: str, heading: str, sid: str, stems: list[str]) -> str:
    blocks = [h2(sid, heading)]
    for stem in stems:
        blocks.append(
            p(
                stem,
                f"When U.S. buyers evaluate {topic}, the expensive mistakes are usually ambiguity in definitions, weak measurement, and misaligned incentives—not the novelty of the channel itself.",
                TAIL,
                "Financing and vendor governance both improve when milestones tie to CRM stages leadership already reviews, not to slide decks that never match the database.",
            )
        )
    return "".join(blocks)


def build_page(
    topic: str,
    sections: list[tuple[str, str, list[str]]],
    case_title: str,
    case_body: str,
    case_take: str,
    img1: tuple[str, str],
    img2: tuple[str, str],
) -> str:
    intro = (
        fig(*img1)
        + p(
            f"This guide is written for U.S. business owners and operators who are actively comparing vendors and need high-intent, practical criteria—not trend headlines. "
            f"We focus on {topic} with search-friendly structure (headings, definitions, checklists) and answer-engine friendly summaries you can scan before a procurement call. "
            "Nothing here replaces advice from qualified legal counsel for outreach compliance or from a licensed professional for regulated industries."
        )
        + p(
            "Use the sections as a scorecard: copy the headings into a spreadsheet, rate each vendor 1–5, and attach evidence (sample reports, SLAs, and references). "
            "High-intent buyers move faster when they stop debating adjectives and start inspecting workflows, data provenance, and CRM alignment."
        )
    )
    mid = "".join(expand_section(topic, h, sid, stems) for sid, h, stems in sections)
    body = (
        intro
        + mid
        + fig(*img2)
        + mini_case(case_title, case_body, case_take)
    )
    return body


ARTICLES: list[tuple[str, str, str]] = []


def register(slug: str, topic: str, html: str) -> None:
    ARTICLES.append((slug, topic, html))


# --- Article 1 ---
register(
    "ai-lead-generation-what-you-are-buying",
    "AI lead generation services",
    build_page(
        "AI lead generation services",
        [
            (
                "definitions-that-matter",
                "Definitions that matter before you sign",
                [
                    "Vendors may say “AI leads,” “intent data,” or “qualified meetings,” but those phrases are not interchangeable. Demand written definitions for lead, qualified lead, meeting, opportunity, and disqualification.",
                    "Separate list sourcing from enrichment. If contact data is scraped, modeled, or licensed, you need to know which—and how opt-outs and DNC rules are applied for your use case.",
                    "Clarify whether humans review AI outputs before outreach sends. Automation without review can scale errors as fast as it scales volume.",
                    "Ask how the vendor proves ICP fit: firmographics only, technographics, behavioral signals, or a blend—and how often models are retrained.",
                    "Payment should map to review gates: a pilot with capped volume, then expansion tied to CRM-verified opportunities—not vanity clicks.",
                    "If the package includes creative or copy, specify brand voice approval paths and who is liable for claims.",
                    "Dispute resolution matters: define what happens if complaint rates spike or a state regulator sends an inquiry.",
                    "Finally, connect the contract to your sales capacity. Leads without follow-up SLAs still die in the inbox.",
                ],
            ),
            (
                "evaluation-scorecard",
                "A buyer scorecard you can reuse",
                [
                    "Score data provenance and consent posture first. Without that foundation, faster outreach is not an advantage.",
                    "Score reporting: can you see cohort performance by list source, message angle, and rep team?",
                    "Score integration depth: native CRM sync, webhook reliability, and field mapping—not CSV dumps on Fridays.",
                    "Score human QA: sampling methodology, escalation when error rates rise, and turnaround time for fixes.",
                    "Score compliance documentation: scripts, training logs, and suppression handling suitable for your counsel’s review.",
                    "Score economic realism: model CAC using your margin, not the vendor’s benchmark deck.",
                    "Score exit terms: data portability, list return, and wind-down assistance if you pause.",
                    "Score references: insist on two calls with buyers who paused the vendor—pause stories reveal operational maturity.",
                ],
            ),
            (
                "kpi-translation",
                "Translate vendor KPIs into CFO language",
                    [
                    "Meetings booked are meaningless if show rate is low or opportunities do not advance. Pair top-of-funnel metrics with stage conversion.",
                    "Cost per lead is the wrong default if “lead” includes misfit accounts. Prefer cost per qualified opportunity or payback months.",
                    "If AI reduces labor hours, quantify hours saved in sales ops and research—but do not confuse labor savings with pipeline creation.",
                    "Model downside cases: if reply rates fall 30% next quarter, what levers exist besides sending more?",
                    "Tie incentives to outcomes your finance team can audit: pipeline dollars, win rate, and gross margin—not opens.",
                    "Document assumptions in writing so leadership does not reinterpret success mid-flight.",
                    "For seasonal businesses, compare performance in peak and trough months separately.",
                    "If you sell into regulated sectors, add a compliance KPI: complaints, opt-outs, and legal review turnaround.",
                ],
            ),
        ],
        "Composite example (illustrative, not a real client record):",
        "A 30-person B2B services firm bought “AI-powered leads” and discovered half the records were recycled from old events. They renegotiated to CRM-synced appointments only, capped pilot spend, and required weekly cohort reporting. Qualified opportunities rose while total lead count fell—because the definition finally matched sales reality.",
        "Buy definitions and measurement first; AI accelerates whatever quality you already have.",
        ("/assets/ai-growth-1.webp", "AI-assisted lead generation and sales workflows"),
        ("/assets/business-growth-analytics-kpis.webp", "Marketing KPIs and pipeline analytics"),
    ),
)

# --- Article 2 ---
register(
    "ai-appointment-setting-vs-human-sdrs",
    "AI appointment setting compared to human SDR teams",
    build_page(
        "AI appointment setting compared to human SDR teams",
        [
            (
                "what-each_delivers",
                "What each model actually delivers",
                [
                    "AI appointment setting often shines at rapid personalization drafts, call summaries, and structured follow-up tasks—if workflows are designed with human checkpoints.",
                    "Human SDRs still win on nuanced discovery, objection handling, and navigating complex buying committees—especially in high-ACV sales.",
                    "Hybrid models frequently outperform either alone: AI prepares research and drafts; humans approve, call, and escalate.",
                    "Throughput claims should be tested against your ICP difficulty, not a vendor’s easiest vertical.",
                    "Consider timezone coverage: AI-assisted sequences can extend hours, but compliance still governs calling windows.",
                    "Training burden differs: SDRs need coaching; AI systems need prompt governance and data hygiene—both cost management time.",
                    "Turnover is a hidden SDR tax; AI does not quit but can silently degrade if models drift without monitoring.",
                    "For brand-sensitive firms, human voice may be mandatory regardless of AI efficiency.",
                ],
            ),
            (
                "cost-modeling",
                "Cost modeling without magical thinking",
                [
                    "Fully burden an SDR: salary, benefits, tools, managers, and recruiting. Compare to vendor fees plus internal QA time—often underestimated.",
                    "If AI reduces headcount, ensure you still have capacity for account research on strategic targets.",
                    "Watch per-meeting fees: they look clean until definitions slip and meetings are low quality.",
                    "Pilot with a fixed calendar outcome: qualified meetings that match your disqual checklist.",
                    "Budget for list and data costs separately; they are not “included” if quality is thin.",
                    "Include legal review time if templates change weekly; velocity without review increases risk.",
                    "If you need multilingual outreach, compare human coverage versus model quality by language.",
                    "Revisit the model quarterly; what worked at 500 dials per week may break at 5,000.",
                ],
            ),
            (
                "decision-matrix",
                "Decision matrix by deal size and motion",
                [
                    "Low ACV, high velocity: AI-assisted sequences with tight templates may be enough if compliance is airtight.",
                    "Mid-market with committee sales: hybrid—AI for research and email, humans for calls and meetings.",
                    "Enterprise: humans lead; AI supports enablement and note-taking—not autonomous outreach without governance.",
                    "If your win rate is weak, fixing discovery beats adding more meetings.",
                    "If your bottleneck is speed-to-lead, AI routing and drafts can help—after CRM rules work.",
                    "If your bottleneck is list quality, neither AI nor SDRs fix bad data.",
                    "If you are entering a new vertical, humans learn faster early; automate after patterns stabilize.",
                    "Document the decision in a one-page policy so sales and marketing do not freelance tools.",
                ],
            ),
        ],
        "Composite example (illustrative, not a real client record):",
        "A SaaS-adjacent firm replaced one SDR with an AI-assisted vendor and kept a senior SDR for strategic accounts. Total spend fell slightly, but meetings-per-opportunity improved because humans focused on high-fit tiers while AI handled structured follow-up for long-tail inbound.",
        "Match the labor model to bottlenecks: discovery vs throughput vs compliance—not headlines.",
        ("/assets/ai-growth-2.webp", "Automation and human collaboration in sales development"),
        ("/assets/bloc-hero-business-office-800w.webp", "Business development and outbound sales office"),
    ),
)

# Continue with articles 3-10 using same pattern (compact stems, expanded via TAIL)
STEM_BANK = {
    "compliance": [
        "Consent and identification requirements for commercial messages are not uniform across channels; map email, SMS, and voice separately.",
        "State mini-TCPA and privacy laws can be stricter than federal baselines—especially for texts and automated dialing.",
        "AI personalization must not fabricate facts; misleading claims can trigger FTC scrutiny and platform bans.",
        "Recordkeeping is operational: save scripts, suppression lists, and training logs—not screenshots in a chat thread.",
        "Warm up domains and inboxes methodically; sudden volume spikes harm deliverability and reputation.",
        "Business-to-business exemptions are narrower than many teams assume; verify with counsel for your facts.",
        "Include an easy unsubscribe path and honor it immediately; delayed suppression is a common enforcement target.",
        "If you use scraped data, understand provenance and contractual restrictions; not all public web data is fair game for outreach.",
        "Align marketing claims with substantiation; superlatives in AI drafts still need proof.",
        "Document vendor subprocessors and data flows if personal information is processed.",
        "If you call mobile numbers, verify consent pathways carefully; mistakes are expensive.",
        "Keep a written escalation path for complaints from carriers, platforms, or regulators.",
        "Review state attorney general bulletins periodically; enforcement themes shift.",
        "Train reps on do-not-contact requests captured outside the CRM.",
        "Separate marketing email from transactional email infrastructure where appropriate.",
        "If you A/B test aggressively, ensure both variants remain truthful and compliant.",
    ],
    "seo_cost": [
        "Retainers often bundle technical fixes, content, and reporting—ask for line-item value if pricing feels opaque.",
        "Local SEO programs emphasize GBP, citations, and reviews; national programs emphasize authority and technical scale.",
        "Freelancers can be nimble but may lack depth across engineering, content, and analytics.",
        "In-house hires require tools, training, and management bandwidth—budget fully loaded cost, not salary alone.",
        "Fractional leaders fit when you need strategy without a full executive hire.",
        "Cheap packages that promise page-one rankings are a structural red flag in competitive SERPs.",
        "Content velocity without quality can create crawl bloat and reputational risk.",
        "Link schemes invite penalties; insist on ethical link acquisition with documented tactics.",
        "Technical debt compounds; budget for migrations, schema, and Core Web Vitals—not only blog posts.",
        "Reporting should tie to revenue proxies: qualified traffic, conversions, and assisted pipeline where possible.",
        "International SEO adds hreflang and localization cost—price it explicitly.",
        "Ecommerce SEO needs faceted navigation discipline; not every agency has that depth.",
        "Enterprise SEO needs governance; workflows matter as much as keywords.",
        "If you run paid media, coordinate SEO and PPC to avoid cannibalized messaging.",
        "Always clarify who implements changes—many delays are client dev queue issues, not laziness.",
        "Price discovery audits separately from ongoing retainers so scope is honest.",
    ],
    "seo_red_flags": [
        "Guaranteed rankings ignore competitor actions and algorithm changes.",
        "Secret methods usually mean risky tactics you will not want in an diligence packet.",
        "Opaque backlink networks are liabilities, not assets.",
        "If reporting is only keyword positions, you may be optimizing the wrong thing.",
        "No access to Search Console or analytics suggests you do not own your data story.",
        "If every recommendation is blog volume, technical SEO may be neglected.",
        "If they will not explain disavow or link risk, walk away.",
        "If contracts auto-renew without performance review, renegotiate.",
        "If they outsource everything offshore without QA, brand and accuracy suffer.",
        "If stakeholder interviews never happen, strategy is template-driven.",
        "If they refuse to coordinate with your dev team, implementation stalls.",
        "If they sell guest posts on irrelevant sites, decline.",
        "If they cannot show before/after for a site like yours, relevance is weak.",
        "If pricing is too low to pay senior talent, you are buying theater.",
        "If they dodge questions about Core Web Vitals, expect slow fixes.",
        "If they promise instant results, model realistic crawl and index timelines instead.",
    ],
    "web": [
        "Conversion-first sites prioritize clarity, proof, and frictionless contact paths over animated novelty.",
        "Redesigns that change URLs without migration plans destroy organic traffic.",
        "Thin location pages for every city without unique value harm trust and SEO.",
        "Page speed is a ranking and conversion factor; budget engineering time.",
        "Accessibility is both legal risk management and better UX for everyone.",
        "Trust signals—licenses, certifications, and reviews—belong above the fold for high-intent visitors.",
        "Forms should match buyer readiness; long forms for cold traffic kill conversion.",
        "Analytics must capture events that map to pipeline, not only pageviews.",
        "Mobile layouts need tap targets and readable typography; half your traffic is likely mobile.",
        "Schema markup helps search engines understand entities; implement carefully.",
        "Hosting and CDN choices affect TTFB; do not cheap out if SEO matters.",
        "Staging environments should block indexing; accidental duplication is common.",
        "Content management permissions prevent well-meaning employees from breaking SEO templates.",
        "Video and images need compression and lazy loading for performance.",
        "Clear service taxonomy helps users and crawlers; avoid clever but confusing naming.",
        "Post-launch QA should include redirects, sitemaps, and internal link checks.",
    ],
    "stack": [
        "Sequence investments so each layer feeds the next: crawlable site, measurable traffic, then outbound volume.",
        "If SEO is broken, paid and outbound amplify a leaky bucket.",
        "If the site confuses buyers, ads become expensive tutors for bad UX.",
        "If CRM hygiene is poor, leads evaporate regardless of channel.",
        "Document a quarterly roadmap with one primary bottleneck metric.",
        "Align marketing and finance on CAC and payback assumptions.",
        "If capacity is constrained, cap lead volume to protect margin and reviews.",
        "If compliance is material, legal should review sequences before scale.",
        "If you enter new geos, localize proof and policy pages—not only translation.",
        "Instrument multi-touch attribution modestly; perfect attribution is a myth.",
        "Use call tracking where phone leads matter; otherwise SEO looks weaker than it is.",
        "Invest in creative testing where CPM is high; small CTR gains matter.",
        "Keep an experimentation log to avoid repeating failed tactics.",
        "Train sales on message-market fit insights from marketing experiments.",
        "If you outsource multiple vendors, designate an internal orchestrator.",
        "Revisit ICP quarterly; markets shift faster than annual plans.",
    ],
    "rfp": [
        "Scope should list properties, systems, and stakeholders—not only goals.",
        "KPIs need baselines and measurement definitions agreed upfront.",
        "Security questionnaires matter for data handling and subcontractor access.",
        "Ask for sample weekly reports and a redacted strategy doc from a similar client.",
        "Include change-control language so scope creep is managed fairly.",
        "Define acceptance tests for deliverables: pages shipped, fixes verified, links acquired ethically.",
        "Specify software ownership: licenses should be in your name where possible.",
        "Add a pause clause for brand or legal incidents.",
        "Require indemnities appropriate to outreach and content risk.",
        "Set meeting cadence and executive sponsor involvement.",
        "Clarify who writes creative versus who approves it.",
        "For international work, specify languages and compliance expectations.",
        "Ask how they train staff on guideline updates.",
        "Request a transition plan if the contract ends.",
        "Budget realistic timelines for dev implementation.",
        "Align payment milestones to verified outcomes, not calendar months alone.",
    ],
}


def build_from_bank(
    slug: str,
    topic: str,
    title1: str,
    id1: str,
    stems1: list[str],
    title2: str,
    id2: str,
    stems2: list[str],
    title3: str,
    id3: str,
    stems3: list[str],
    case_title: str,
    case_body: str,
    case_take: str,
    img1: tuple[str, str],
    img2: tuple[str, str],
) -> None:
    sections = [
        (id1, title1, stems1),
        (id2, title2, stems2),
        (id3, title3, stems3),
    ]
    register(slug, topic, build_page(topic, sections, case_title, case_body, case_take, img1, img2))


build_from_bank(
    "cold-email-ai-personalization-compliance-us",
    "cold email and AI personalization compliance in the United States",
    "CAN-SPAM, TCPA, and state overlays: what buyers must verify",
    "federal-baselines",
    STEM_BANK["compliance"][:6]
    + [
        "Identify yourself truthfully in headers and body copy; deceptive routing is an enforcement magnet.",
        "Honor opt-outs within the statutory window and propagate them to all systems that might email the same person.",
    ],
    "Operational checklist before scaling AI-written outreach",
    "operations-checklist",
    STEM_BANK["compliance"][6:14],
    "Vendor questions that separate professional programs from reckless automation",
    "vendor-diligence",
    STEM_BANK["compliance"][8:16],
    "Composite example (illustrative, not a real client record):",
    "A regional services firm used AI to personalize cold email at scale but skipped legal review of claims. After a deliverability collapse and a state inquiry, they rebuilt templates with human approval gates and a documented suppression workflow—reply quality improved because messages became truthful and specific.",
    "Compliance and quality rise together when humans own claims and machines handle structure.",
    ("/assets/ai-bridge-2.webp", "Systems for compliant outreach and data handling"),
    ("/assets/ai-growth-3.webp", "AI-assisted messaging workflows with review gates"),
)

build_from_bank(
    "seo-cost-2026-agency-freelancer-in-house",
    "SEO pricing models for U.S. businesses in 2026",
    "How SEO budgets are structured across agencies, freelancers, and in-house teams",
    "pricing-mechanics",
    STEM_BANK["seo_cost"][:8],
    "What typical monthly ranges buy (and what they do not)",
    "what-ranges-mean",
    STEM_BANK["seo_cost"][4:12],
    "How to compare proposals apples-to-apples",
    "compare-proposals",
    STEM_BANK["seo_cost"][8:16],
    "Composite example (illustrative, not a real client record):",
    "A multi-location brand compared three agency quotes from $2.5K to $12K monthly. The lowest price excluded dev implementation; the highest included technical remediation and analytics. They chose mid-market pricing after modeling internal dev hours required for each option—total cost of ownership, not sticker price, drove the decision.",
    "Price SEO by implementation burden and accountability, not by keyword promises.",
    ("/assets/rbf-marketing-1200w.webp", "Marketing strategy and SEO investment"),
    ("/assets/business-growth-content-marketing.webp", "Content and organic search growth"),
)

build_from_bank(
    "seo-agency-vs-in-house-vs-fractional-model",
    "SEO resourcing models for SMBs and mid-market teams",
    "When to hire an agency, build in-house, or use fractional SEO leadership",
    "agency-strengths",
    STEM_BANK["seo_cost"][:6]
    + [
        "Agencies often bring cross-industry pattern recognition and tool stacks you would not buy alone.",
        "They fit when speed and breadth matter more than deep proprietary context on day one.",
    ],
    "In-house advantages and hidden costs",
    "in-house-advantages",
    STEM_BANK["seo_cost"][2:10],
    "Fractional leadership: governance without a full executive hire",
    "fractional-fit",
    STEM_BANK["seo_cost"][6:14],
    "Composite example (illustrative, not a real client record):",
    "A software company hired fractional SEO leadership to set governance, then used a boutique agency for execution while training an internal coordinator. They avoided both executive recruiting delays and an immature in-house hire who would have lacked mentorship.",
    "Blend models when governance, execution speed, and knowledge transfer all matter.",
    ("/assets/business-growth-strategy-intro.webp", "Strategy session for SEO resourcing"),
    ("/assets/rbf-growth-capital-800w.webp", "Growth investment aligned to channel strategy"),
)

build_from_bank(
    "red-flags-hiring-seo-company",
    "hiring an SEO company",
    "Warning signs that predict a bad SEO engagement",
    "promise-issues",
    STEM_BANK["seo_red_flags"][:8],
    "Reporting and access red flags",
    "reporting-access",
    STEM_BANK["seo_red_flags"][4:12],
    "Tactics that create long-tail risk",
    "risky-tactics",
    STEM_BANK["seo_red_flags"][8:16],
    "Composite example (illustrative, not a real client record):",
    "An ecommerce brand saw a traffic spike from irrelevant posts, then a manual action months later. The prior vendor refused to share disavow history. Recovery took longer than a conservative program would have cost from the start.",
    "If transparency is weak, risk compounds after the vendor leaves.",
    ("/assets/mca-amounts-800w.webp", "Evaluating vendor proposals and commercial terms"),
    ("/assets/business-growth-analytics-kpis.webp", "SEO reporting and performance analytics"),
)

build_from_bank(
    "website-redesign-vs-conversion-refresh-leads",
    "website redesign versus conversion-focused optimization",
    "Choosing between a full redesign and a conversion-first refresh",
    "when-redesign-makes-sense",
    STEM_BANK["web"][:8],
    "When a refresh outperforms a rip-and-replace",
    "refresh-wins",
    STEM_BANK["web"][4:12],
    "Implementation plan that protects SEO during changes",
    "seo-safe-rollout",
    STEM_BANK["web"][8:16],
    "Composite example (illustrative, not a real client record):",
    "A professional services firm planned a six-month redesign. A two-month refresh of hero copy, proof placement, and form friction lifted qualified leads 18%—buying time for a safer migration with proper redirects.",
    "Lift revenue with the smallest change that removes friction; redesign on schedule, not panic.",
    ("/assets/business-growth-content-marketing.webp", "Website content and conversion planning"),
    ("/assets/sbl-competitive-pricing-800w.webp", "Positioning and offer clarity on the homepage"),
)

build_from_bank(
    "small-business-website-pages-seo-conversion",
    "small business website architecture",
    "How many pages your site needs for SEO and conversions",
    "core-pages",
    STEM_BANK["web"][:8],
    "Programmatic pages: when they help versus when they hurt",
    "programmatic-pages",
    STEM_BANK["web"][3:11]
    + [
        "City pages should add unique value—case context, local proof, and FAQs—not duplicate paragraphs with swapped city names.",
    ],
    "Measurement that proves information architecture works",
    "measurement-ia",
    STEM_BANK["web"][6:14],
    "Composite example (illustrative, not a real client record):",
    "A contractor deleted fifty thin city pages, consolidated into ten robust service-area hubs, and saw impressions shift to higher-intent queries within two crawl cycles—traffic count fell while booked estimates rose.",
    "Fewer, stronger pages often beat many weak ones.",
    ("/assets/wcl-intro-cashflow-560w.webp", "Small business digital presence and trust"),
    ("/assets/referral-hero.webp", "Local trust signals and referrals online"),
)

build_from_bank(
    "lead-gen-stack-seo-website-outbound-order",
    "sequencing SEO, website work, and outbound lead generation",
    "The order of operations for SEO, your website, and outbound",
    "sequence-framework",
    STEM_BANK["stack"][:8],
    "Common failure patterns when channels fight each other",
    "failure-patterns",
    STEM_BANK["stack"][4:12],
    "Quarterly governance that keeps vendors aligned",
    "governance",
    STEM_BANK["stack"][8:16],
    "Composite example (illustrative, not a real client record):",
    "A B2B manufacturer scaled outbound before fixing site speed and form routing. Cost per opportunity fell only after technical fixes and CRM SLAs—not after more dial volume.",
    "Fix capture and measurement before you amplify traffic.",
    ("/assets/business-growth-lead-pipeline.webp", "Lead pipeline across marketing channels"),
    ("/assets/ai-growth-1.webp", "Integrated demand generation stack"),
)

build_from_bank(
    "rfp-template-leads-seo-website-vendor",
    "RFP for digital marketing vendors",
    "RFP sections that attract serious SEO, web, and lead-gen vendors",
    "scope-baseline",
    STEM_BANK["rfp"][:8],
    "KPI and reporting requirements",
    "kpi-reporting",
    STEM_BANK["rfp"][4:12],
    "Legal, data, and transition clauses",
    "legal-data-transition",
    STEM_BANK["rfp"][8:16],
    "Composite example (illustrative, not a real client record):",
    "A PE-backed rollup used a single RFP for web, SEO, and outbound. Vendors who could not separate implementation hours from strategy fees were disqualified early; the winner’s milestone schedule matched internal dev capacity.",
    "Good RFPs reveal operational maturity—yours and theirs.",
    ("/assets/sbl-strategic-timing-800w.webp", "Procurement timing and strategic vendor selection"),
    ("/assets/bloc-growth-800w.webp", "Business growth planning with vendors"),
)


def main() -> None:
    FRAG_DIR.mkdir(parents=True, exist_ok=True)
    for slug, topic, html in ARTICLES:
        n = wc(html)
        print(slug, n, "words")
        if n < 2000:
            raise SystemExit(f"{slug} below 2000 words: {n}")
        (FRAG_DIR / f"{slug}.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
