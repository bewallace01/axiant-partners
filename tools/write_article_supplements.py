# -*- coding: utf-8 -*-
"""Generate per-slug supplemental HTML. Run: python write_article_supplements.py"""
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "article_supplements"
OUT.mkdir(exist_ok=True)

# slug -> unique opening (~130–180 words) + structured deep sections
ARTICLES = [
    {
        "slug": "predictable-lead-pipeline-90-days-without-doubling-ad-spend",
        "topic": "predictable pipeline",
        "a1": "lead quality",
        "a2": "CRM discipline",
        "a3": "channel economics",
        "intro": """<p>If you have ever stared at a dashboard that showed “more leads” while the sales calendar stayed empty, you already understand the difference between motion and predictability. Predictable pipelines are built from definitions: who counts as a qualified lead, how fast someone responds, and which channels create real opportunities instead of polite interest. This extended section translates the ideas above into a leadership operating system you can run without hiring a large revops team—just discipline, a weekly cadence, and willingness to stop doing things that fail your own success criteria.</p>""",
    },
    {
        "slug": "top-line-vs-bottom-line-revenue-profit-cash",
        "topic": "profit and cash",
        "a1": "margin",
        "a2": "working capital",
        "a3": "pricing power",
        "intro": """<p>Revenue celebrations fade quickly when vendors, payroll, and lenders all want cash this week while customers pay next month. The best owners learn to read all three financial stories at once: the P&amp;L story about value creation, the cash story about timing, and the balance sheet story about risk. This addendum focuses on how to keep growth from quietly cannibalizing liquidity—especially when discounts, mix shifts, or large new contracts change how money moves through your business.</p>""",
    },
    {
        "slug": "cold-calling-scripts-sequences-metrics-that-book-meetings",
        "topic": "cold calling",
        "a1": "sequences",
        "a2": "coaching",
        "a3": "metrics",
        "intro": """<p>Cold calling reputation problems usually come from lazy lists and selfish pitches, not from the telephone itself. When reps sound informed, respectful, and specific, buyers often take the meeting—even busy ones. The extended guidance below connects daily behavior to weekly coaching and monthly forecasting so outbound becomes a managed channel instead of a morale drain. You will still hear “no” often; the goal is to make “yes” repeatable enough to forecast.</p>""",
    },
    {
        "slug": "ai-in-sales-and-marketing-practical-and-compliant",
        "topic": "AI adoption",
        "a1": "verification",
        "a2": "brand voice",
        "a3": "data governance",
        "intro": """<p>AI tools can compress first drafts and research time dramatically, but they can also create confident nonsense that damages trust in regulated or reputation-sensitive markets. The winning pattern is human-led judgment with machine-assisted speed: tight prompts, source verification, brand guardrails, and clear rules about customer data. What follows is a practical rollout path that keeps your team fast without turning every email into a liability.</p>""",
    },
    {
        "slug": "turn-website-traffic-into-qualified-opportunities",
        "topic": "inbound conversion",
        "a1": "landing pages",
        "a2": "speed-to-lead",
        "a3": "attribution",
        "intro": """<p>Traffic is expensive even when it is “free” because content and SEO consume time. If visitors cannot understand the offer quickly, or if sales responds slowly, you are effectively donating attention to competitors. This section focuses on tightening the middle of the funnel: matching intent to CTA, reducing friction without inviting spam, and making sure inbound volume shows up in pipeline reviews as qualified opportunities—not vague “interest.”</p>""",
    },
    {
        "slug": "raise-prices-without-losing-clients",
        "topic": "pricing",
        "a1": "value communication",
        "a2": "segmentation",
        "a3": "retention",
        "intro": """<p>Most underpricing is emotional: fear of rejection, attachment to legacy customers, or comparison to the cheapest competitor instead of the best alternative. Strategic pricing is not greed—it is how you fund quality, retain talent, and invest in delivery. The material below walks through how to segment customers, sequence communication, and read results so you capture margin without torching relationships you genuinely want to keep.</p>""",
    },
    {
        "slug": "referral-funnel-service-businesses",
        "topic": "referrals",
        "a1": "partner channels",
        "a2": "timing the ask",
        "a3": "tracking",
        "intro": """<p>Referrals feel magical when they arrive, but they are less mysterious when you treat them as a system: specific moments to ask, language that makes introductions easy, and partners who see mutual benefit. Service businesses often sit on latent referral potential because nobody owns the playbook. This extension shows how to operationalize word-of-mouth without turning every invoice into an awkward pitch.</p>""",
    },
    {
        "slug": "scale-paid-ads-tight-margins-framework",
        "topic": "paid media",
        "a1": "contribution margin",
        "a2": "creative testing",
        "a3": "caps",
        "intro": """<p>Paid media on thin margins is unforgiving: small inefficiencies multiply across thousands of impressions. The framework here is not “spend until it hurts.” It is spend with explicit unit economics, creative refresh discipline, and operational gates so you do not buy demand you cannot serve. Treat ads like a manufacturing line—measure scrap rate (junk leads) and yield (qualified opportunities) as seriously as a factory measures waste.</p>""",
    },
    {
        "slug": "hiring-sdrs-closers-marketing-before-burning-cash",
        "topic": "rev team design",
        "a1": "sequencing hires",
        "a2": "management load",
        "a3": "payback",
        "intro": """<p>Headcount is the most expensive “marketing” line item because salaries compound monthly whether pipeline shows up or not. Sequencing matters: a great closer with no qualified conversations is expensive idle capacity; an SDR team without messaging-market fit burns through lists and morale. The guidance below helps you stage roles so each hire amplifies the previous investment instead of multiplying fixed cost prematurely.</p>""",
    },
    {
        "slug": "finance-growth-inventory-equipment-marketing-without-cash-crisis",
        "topic": "growth financing",
        "a1": "phased draws",
        "a2": "cash forecasting",
        "a3": "use of funds",
        "intro": """<p>Financing can accelerate a working plan—or stretch a broken one. The difference is whether capital is attached to milestones, repayment is modeled against real cash timing, and leadership can explain the use of funds in one page. This section ties marketing, inventory, and equipment decisions to liquidity so you do not confuse borrowing with revenue.</p>""",
    },
    {
        "slug": "why-marketing-feels-broken-five-fixes",
        "topic": "marketing diagnosis",
        "a1": "ICP",
        "a2": "offer clarity",
        "a3": "operations fit",
        "intro": """<p>When marketing feels broken, teams often jump to new tactics: a different agency, a new platform, another brand refresh. Sometimes tactics are the problem—but often the bottleneck is upstream: unclear ICP, vague offers, slow follow-up, misleading metrics, or operations that cannot serve more demand. This extended playbook helps you run a disciplined diagnostic before you spend another quarter burning budget on noise.</p>""",
    },
    {
        "slug": "stop-leaking-deals-crm-speed-to-lead-slas",
        "topic": "deal hygiene",
        "a1": "CRM stages",
        "a2": "SLAs",
        "a3": "forecast quality",
        "intro": """<p>CRM hygiene is not administrative trivia; it is revenue protection. Deals leak when tasks slip, notes are missing, and stages become fiction. Buyers feel the chaos as delayed responses and repeated questions. The addendum below focuses on lightweight governance: simple stage definitions, non-negotiable SLAs, and a weekly hygiene ritual that takes minutes but saves tens of thousands in lost opportunities.</p>""",
    },
    {
        "slug": "wrong-icp-hidden-cost-leads-and-budget",
        "topic": "ICP discipline",
        "a1": "CAC",
        "a2": "disqualification",
        "a3": "segment focus",
        "intro": """<p>A loose ICP feels inclusive; in practice it usually raises acquisition costs, lengthens sales cycles, and fills customer success with poor-fit accounts that churn or drain support. Tight ICP feels scary because it looks like you are walking away from revenue—but you are walking away from revenue that destroys margin. The following sections show how to rebuild ICP from evidence and enforce it without sounding arrogant to prospects.</p>""",
    },
    {
        "slug": "unit-economics-scaling-without-bankruptcy",
        "topic": "unit economics",
        "a1": "CAC and LTV",
        "a2": "cash conversion",
        "a3": "dashboards",
        "intro": """<p>Scaling without unit economics is like driving with a fogged windshield: you can go fast for a while, then discover obstacles too late. Contribution margin, payback, and cash conversion tell you whether each additional sale strengthens the business. This extension translates those metrics into weekly owner habits—not finance theory.</p>""",
    },
    {
        "slug": "cash-flow-traps-after-revenue-spike",
        "topic": "cash timing",
        "a1": "AR and inventory",
        "a2": "hiring lag",
        "a3": "stress tests",
        "intro": """<p>Spikes create emotional highs and operational stress simultaneously. Cash can deteriorate even when the P&amp;L looks strong because receivables stretch, inventory builds, and hiring runs ahead of collections. The guidance below helps you build a forward-looking cash rhythm that survives your success.</p>""",
    },
    {
        "slug": "ai-tools-stack-without-wasting-money-smb",
        "topic": "AI stack",
        "a1": "vendor review",
        "a2": "adoption",
        "a3": "security",
        "intro": """<p>Tool sprawl is expensive, confusing, and demotivating. Employees learn three overlapping products halfway. Subscriptions renew because nobody owns cancellation. The extended material here treats AI purchases like any other operational investment: owner, workflow, measurement, renewal criteria, and data rules.</p>""",
    },
    {
        "slug": "cold-outreach-compliance-prospecting",
        "topic": "compliance",
        "a1": "email and call rules",
        "a2": "deliverability",
        "a3": "training",
        "intro": """<p>Compliance is not only legal protection; it protects deliverability, brand reputation, and rep careers. Aggressive growth and respectful boundaries can coexist when lists, messaging, and opt-out handling are disciplined. This section operationalizes guardrails so leadership can scale outreach without creating a culture of corner-cutting.</p>""",
    },
    {
        "slug": "pause-marketing-fix-operations-first",
        "topic": "ops-first growth",
        "a1": "capacity",
        "a2": "quality",
        "a3": "re-entry gates",
        "intro": """<p>Pausing marketing feels like moving backward; sometimes it is how you avoid a reputational cliff. When delivery quality slips, more leads simply accelerate churn and negative reviews. The playbook below helps you communicate the pause internally, protect revenue where possible, and reopen acquisition with objective gates—not gut feel.</p>""",
    },
    {
        "slug": "slow-season-leads-offers-working-capital",
        "topic": "seasonality",
        "a1": "offers",
        "a2": "nurture",
        "a3": "credit use",
        "intro": """<p>Slow seasons are a planning problem disguised as a surprise. Cash, offers, and light-touch demand gen should be coordinated so you exit the trough with relationships intact and capacity ready. This extension focuses on sequencing: preserve liquidity first, reshape offers second, fund awareness selectively third, and borrow only with a repayment path tied to inbound seasonality.</p>""",
    },
    {
        "slug": "borrow-grow-vs-survive-lender-perspective",
        "topic": "lender narrative",
        "a1": "underwriting",
        "a2": "financial hygiene",
        "a3": "relationships",
        "intro": """<p>Lenders are pattern-matching machines. They have seen survival borrowing dressed up as growth many times. Credibility comes from numbers, documentation, and behavior: stable margins, improving cash conversion, clear use of funds, and proactive communication when assumptions miss. This section helps you align your story with what underwriters actually reward.</p>""",
    },
]


def section(title: str, paras: list[str]) -> str:
    parts = [f"<h2>{title}</h2>"]
    for p in paras:
        parts.append(f"<p>{p}</p>")
    return "\n".join(parts)


def build_supplement(topic: str, a1: str, a2: str, a3: str) -> str:
    return "\n".join(
        [
            section(
                f"Weekly operating rhythm for {topic}",
                [
                    f"Embed {topic} into a fixed weekly meeting with marketing, sales, and finance. Start by reconciling definitions: what is a lead, an MQL, an SQL, and an opportunity in your CRM—write it on one page. If definitions drift, dashboards diverge and arguments recycle. End each meeting with three decisions: one experiment to start, one underperforming tactic to reduce, and one operational fix to protect delivery quality.",
                    f"Assign a single cross-functional owner accountable for {a1} outcomes this quarter. The owner coordinates handoffs, enforces SLAs, and escalates when bottlenecks repeat. They do not need to execute every task; they need to ensure the system does not depend on heroics. In smaller companies this is often a founder; as you grow, consider revops support or a strong sales manager with operational instincts.",
                    f"Keep a decision log tied to {a2}: hypothesis, date, owner, expected signal, and review date. When results arrive weeks later, teams forget what changed. The log becomes your institutional memory and prevents repeating failed tactics. It also accelerates onboarding when new hires ask “why we do it this way.”",
                    f"Escalate {a3} trade-offs explicitly. If you cannot state what you are not doing, you are probably doing too much poorly. Ruthless prioritization is how small teams beat larger, diffuse competitors.",
                ],
            ),
            section(
                "Ninety-day roadmap you can reuse every quarter",
                [
                    f"Days 1–30: measurement and response baseline. Fix tagging, routing, speed-to-lead, and CRM required fields. No major new channel launches unless the business is truly pre-revenue. The objective is trustworthy data and fast follow-up—because {topic} cannot improve if you cannot see it.",
                    f"Days 31–60: run two time-boxed experiments with prewritten success metrics and kill criteria. Experiments fail when success is redefined mid-flight. Document expected cost, expected signal, and what you will do if results are ambiguous. This is where {a1} learning compounds.",
                    f"Days 61–90: scale what cleared the bar; simplify what did not. Scaling can mean budget, touches, or capacity—increase one lever at a time. Finalize playbooks for messaging, objection handling, and CRM updates so {a2} is repeatable. Playbooks beat talent dependency.",
                    f"At day ninety, run a retrospective: what did we learn about customers, message, and margin? Update the next quarter’s roadmap with those lessons so {a3} improves iteratively instead of resetting to zero.",
                ],
            ),
            section(
                "Cash, margin, and risk: keeping growth fundable",
                [
                    f"Model cash weekly with at least three scenarios: base, delayed collections, and a mild revenue miss. Growth plans that only work in the optimistic case are fragile. Tie spending decisions to minimum liquidity buffers so {topic} does not force emergency borrowing.",
                    f"Watch gross margin while revenue accelerates. If margin falls as sales rise, investigate discounting, mix shift, scope creep, or supplier costs. Volume that destroys margin is not strategic growth—it is self-sabotage wearing a revenue costume. {a1} metrics should include margin, not only top line.",
                    f"If you use credit, align instrument to use and phase draws against milestones. Lenders reward clarity: use of funds, timing, and mitigations. Strong {a2} hygiene improves both internal decisions and external credibility.",
                    f"Stress-test hiring and inventory decisions against {a3}. These are the classic cash traps after spikes. If the stress test fails, sequence growth more slowly—survival first, speed second.",
                ],
            ),
            section(
                "Coaching, incentives, and team habits",
                [
                    f"Coach from recordings and dashboards weekly, not from anecdotes. Ten minutes of targeted feedback beats an hour of generic training. Tie incentives to outcomes finance can verify: qualified pipeline, margin-aware wins, and clean CRM hygiene—not just activity volume. {a1} improves when rewards match reality.",
                    f"Celebrate disqualification of bad fits. Reps who stop junk early save the company more than reps who drag unqualified deals. Make {a2} part of your culture, not a punishment metric.",
                    f"Run blameless postmortems on failed campaigns or lost quarters. Ask what the system taught you about message, audience, and timing. Teams that learn fast outrun bigger budgets with slow feedback loops.",
                    f"Protect focus time for deep work: prospecting, writing, building assets. Meeting overload destroys {a3} execution. Calendar design is a strategy decision.",
                ],
            ),
            section(
                "Customer voice: interviews, objections, and proof",
                [
                    f"Run at least two structured customer conversations a month about {topic}. Ask what nearly stopped the deal, what alternatives they considered, and how they would describe your value to a peer. Feed exact phrases into website copy and outbound language—buyers recognize their own words faster than your internal jargon.",
                    f"Catalog top objections and pair each with a proof asset: a short case outline, a metric, a process diagram, or a risk-reversal policy. Reps should never improvise answers to the same objection differently. Consistency builds trust; chaos signals immaturity.",
                    f"Use win/loss reviews honestly. Losses teach more than wins when leadership resists blame. Look for patterns: pricing, timing, competitive displacement, or delivery concerns. If {a1} keeps failing against a specific competitor, study their buyer journey and tighten your differentiation instead of discounting reflexively.",
                    f"Testimonials should emphasize outcomes and constraints—not adjectives. “They were great” is weak. “They cut our onboarding time from six weeks to two without adding headcount” is a claim you can anchor in {a2} discussions and repeat in nurture streams.",
                ],
            ),
            section(
                "Tools, automation, and integration discipline",
                [
                    f"Buy tools to reduce failure modes in {topic}, not to impress investors. Every new system needs an owner, a training path, and a retirement plan. If nobody can explain why a subscription exists, cancel it. Integration beats duplication: one CRM as source of truth, one analytics baseline, one place for handoffs.",
                    f"Automate notifications and routing before you automate content generation. A reliable alert that a hot lead arrived matters more than an AI that drafts mediocre emails. Layer {a3} sophistication only after basics work.",
                    f"Audit integrations quarterly. Broken webhooks, expired API keys, and mis-mapped form fields silently delete leads. Include an end-to-end test in onboarding for new hires: submit a form, call the number, book a meeting—does data land correctly?",
                    f"Security and privacy are part of {a1} performance now. A breach or sloppy data handling destroys trust faster than a weak headline. Document approved tools and prohibited data types for each role.",
                ],
            ),
            section(
                "Monday actions and how Axiant Partners can help",
                [
                    f"Pick one metric for {topic}, define it in writing, and review it weekly for thirty days. Walk five leads or opportunities end-to-end and fix one leakage point you discover. Small compounding fixes beat occasional heroic pushes.",
                    f"For an outside perspective on how growth plans connect to financing, <a href=\"/contact.html\">contact Axiant Partners</a>. When your use of funds and cash story are ready, <a href=\"/match.html\">apply to get matched</a> with lenders suited to your industry and structure.",
                ],
            ),
        ]
    ) + f"""
<h2>Operator FAQ</h2>
<h3>How do we know {topic} initiatives are working?</h3>
<p>You should see movement in both <strong>leading</strong> indicators (meetings, qualified opportunities, stage velocity, response times) and <strong>lagging</strong> outcomes (win rate, margin, cash). If only vanity metrics move, pause and fix measurement before spending more.</p>
<h3>How often should we revisit the plan?</h3>
<p>Review tactics weekly, strategy monthly, and assumptions quarterly—sooner if any red-line metric breaks (liquidity, margin, churn spike). Your bar for {a1} and {a2} should evolve with market conditions; static plans go stale.</p>
<h3>What is the biggest mistake teams make here?</h3>
<p>Chasing new channels before fixing follow-up, definitions, and delivery capacity. Progress on {a3} is fastest when you remove leaks, not when you pour more water into a bucket with holes.</p>
<p>Consistency beats intensity: steady weekly reviews outperform annual overhauls that never stick. Small, documented improvements to {topic} compound when leadership protects focus time and refuses reactive thrash.</p>
"""


def main():
    for item in ARTICLES:
        slug = item["slug"]
        html = item["intro"] + "\n" + build_supplement(item["topic"], item["a1"], item["a2"], item["a3"])
        (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
        print("wrote", slug)
    print("done", len(ARTICLES), "files ->", OUT)


if __name__ == "__main__":
    main()
