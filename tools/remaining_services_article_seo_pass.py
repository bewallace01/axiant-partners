#!/usr/bin/env python3
"""
Batch SEO pass for remaining service verticals (CRE, bridge, fix-and-flip, MCA, RBF, SBL):
strip batch24, insert lead WebP, bump modified dates.

Run from repo root: python tools/remaining_services_article_seo_pass.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODIFIED = "2026-04-08"

def m(src: str, alt: str, w: int = 800, h: int = 450) -> tuple[str, str, int, int]:
    return (src, alt, w, h)


SERVICE_CONFIG: list[tuple[str, dict[str, tuple[str, str, int, int]], list[tuple[str, str, int, int]]]] = [
    (
        "commercial-real-estate-loans/articles",
        {
            "cash-out-refinance-commercial-property": m(
                "cre-refinance-800w.webp",
                "Cash-out refinance on commercial investment or owner-occupied property",
            ),
            "commercial-real-estate-loan-requirements": m(
                "cre-intro-800w.webp",
                "Commercial real estate loan requirements and lender expectations",
            ),
            "cre-loan-industrial-warehouse-properties": m(
                "cre-industrial-800w.webp",
                "CRE financing for industrial and warehouse assets",
            ),
            "cre-loan-medical-office-buildings": m(
                "cre-medical-800w.webp",
                "Medical office building loans and owner-user structures",
            ),
            "cre-loan-mistakes-delay-deny-closing": m(
                "cre-hero-800w.webp",
                "Mistakes that delay or derail commercial mortgage closings",
            ),
            "cre-loan-red-flags-recourse-prepayment-balloon-closing-costs": m(
                "cre-expertise-800w.webp",
                "Recourse, prepayment, balloons, and closing cost red flags in CRE loans",
            ),
            "cre-loan-retail-strip-centers": m(
                "cre-retail-800w.webp",
                "Retail strip center and CRE financing considerations",
            ),
            "how-long-close-commercial-real-estate-loan": m(
                "cre-speed-800w.webp",
                "Timeline to close a commercial real estate loan",
            ),
            "how-much-down-payment-required-commercial-property-loan": m(
                "cre-amounts-800w.webp",
                "Down payment and equity for commercial property loans",
            ),
            "owner-occupied-vs-investment-commercial-property-loan": m(
                "cre-mixed-use-800w.webp",
                "Owner-occupied versus investment commercial property financing",
            ),
            "reasons-commercial-refinance-gets-delayed": m(
                "cre-refinance-800w.webp",
                "Why commercial refinances stall and how to avoid delays",
            ),
            "reasons-cre-loan-approval-taking-forever": m(
                "cre-speed-800w.webp",
                "Long CRE approval cycles and underwriting bottlenecks",
            ),
            "sba-504-vs-conventional-commercial-real-estate-loan": m(
                "cre-intro-800w.webp",
                "SBA 504 compared with conventional commercial real estate loans",
            ),
            "what-credit-score-needed-commercial-real-estate-loan": m(
                "cre-amounts-800w.webp",
                "Credit score expectations for CRE and SBA commercial mortgages",
            ),
            "what-do-lenders-look-for-commercial-real-estate-loan": m(
                "cre-service-800w.webp",
                "What CRE lenders underwrite on your loan request",
            ),
            "whats-blocking-cre-loan-from-closing": m(
                "cre-flexibility-800w.webp",
                "Common obstacles before CRE loan closing",
            ),
            "why-cre-loan-keeps-coming-back-for-more-documents": m(
                "cre-speed-800w.webp",
                "Repeated document requests in commercial mortgage underwriting",
            ),
        },
        [
            m("cre-hero-800w.webp", "Commercial real estate financing for U.S. properties"),
            m("cre-office-800w.webp", "Office and professional CRE lending"),
            m("cre-industrial-800w.webp", "Industrial and warehouse commercial loans"),
            m("cre-intro-800w.webp", "Introduction to commercial mortgage options"),
        ],
    ),
    (
        "commercial-bridge-loans/articles",
        {
            "bridge-loan-commercial-property-acquisition": m(
                "cbl-acquisition-800w.webp",
                "Bridge loans for commercial property acquisition",
            ),
            "bridge-loan-pay-off-construction-debt": m(
                "cbl-construction-800w.webp",
                "Bridging out construction debt on commercial projects",
            ),
            "bridge-loan-pitfalls-what-can-go-wrong": m(
                "cbl-complex-800w.webp",
                "Pitfalls and risks in commercial bridge financing",
            ),
            "bridge-loan-value-add-commercial-property": m(
                "cbl-value-add-800w.webp",
                "Value-add commercial bridge loans and exit planning",
            ),
            "commercial-bridge-loan-vs-hard-money-loan": m(
                "cbl-asset-focused-800w.webp",
                "Commercial bridge compared with hard money structures",
            ),
            "commercial-bridge-loan-vs-sba-loan": m(
                "cbl-intro-800w.webp",
                "When bridge financing differs from SBA commercial programs",
            ),
            "how-fast-can-you-close-commercial-bridge-loan": m(
                "cbl-speed-800w.webp",
                "How quickly a commercial bridge loan can close",
            ),
            "what-do-lenders-look-for-commercial-bridge-loan": m(
                "cbl-hero-800w.webp",
                "What bridge lenders evaluate on CRE bridge requests",
            ),
            "whats-holding-up-your-bridge-loan-funding": m(
                "cbl-interest-only-800w.webp",
                "Delays to bridge loan funding and wire conditions",
            ),
            "when-should-you-use-commercial-bridge-loan": m(
                "cbl-use-value-add-800w.webp",
                "Use cases for short-term commercial bridge capital",
            ),
            "why-bridge-loan-keeps-coming-back-for-more-documents": m(
                "cbl-complex-800w.webp",
                "Document churn in bridge loan underwriting",
            ),
            "why-bridge-loan-timeline-keeps-slipping": m(
                "cbl-speed-800w.webp",
                "Slipping timelines on bridge closings and how to tighten them",
            ),
        },
        [
            m("cbl-hero-800w.webp", "Short-term commercial bridge financing"),
            m("cbl-intro-800w.webp", "Bridge loans for transitional commercial assets"),
            m("cbl-speed-800w.webp", "Fast commercial bridge closings"),
        ],
    ),
    (
        "fix-and-flip/articles",
        {
            "fix-and-flip-first-time-investors": m(
                "faf-intro-800w.webp",
                "First-time investors using fix-and-flip financing",
            ),
            "fix-and-flip-loan-first-time-flippers": m(
                "faf-single-family-800w.webp",
                "Fix-and-flip loans for first-time house flippers",
            ),
            "fix-and-flip-loan-multifamily-properties": m(
                "faf-multifamily-800w.webp",
                "Multifamily fix-and-flip and rehab financing",
            ),
            "fix-and-flip-loan-out-of-state-investors": m(
                "faf-purchase-rehab-800w.webp",
                "Out-of-state fix-and-flip lending and local requirements",
            ),
            "fix-and-flip-loan-red-flags-points-fees-draw-schedule-prepayment": m(
                "faf-draw-schedule-800w.webp",
                "Points, fees, draws, and prepay red flags on flip loans",
            ),
            "fix-and-flip-loan-requirements": m(
                "faf-hero-800w.webp",
                "Requirements for fix-and-flip loan approval",
            ),
            "fix-and-flip-mistakes-to-avoid": m(
                "faf-distressed-800w.webp",
                "Mistakes that hurt fix-and-flip projects and financing",
            ),
            "fix-and-flip-vs-hard-money-loan": m(
                "faf-intro-800w.webp",
                "Fix-and-flip products compared with generic hard money",
            ),
            "how-fast-can-you-close-fix-and-flip-loan": m(
                "faf-fast-close-800w.webp",
                "Closing speed on fix-and-flip loans",
            ),
            "how-much-down-payment-fix-and-flip-loan": m(
                "faf-high-ltv-800w.webp",
                "Down payment and LTV on fix-and-flip financing",
            ),
            "reasons-fix-and-flip-lenders-back-out": m(
                "faf-one-loan-800w.webp",
                "Why flip lenders rescind or fail to fund",
            ),
            "typical-fix-and-flip-loan-rates": m(
                "faf-amounts-800w.webp",
                "Typical rates and pricing on fix-and-flip loans",
            ),
            "what-credit-score-needed-fix-and-flip-loan": m(
                "faf-amounts-800w.webp",
                "Credit expectations for fix-and-flip borrowers",
            ),
            "what-do-lenders-look-for-fix-and-flip-loan": m(
                "faf-hero-800w.webp",
                "What flip lenders underwrite beyond the property",
            ),
            "what-is-arv-fix-and-flip-loan": m(
                "faf-use-single-800w.webp",
                "After-repair value (ARV) in fix-and-flip lending",
            ),
            "what-is-maximum-ltv-fix-and-flip-loan": m(
                "faf-high-ltv-800w.webp",
                "Maximum LTV and leverage on rehab loans",
            ),
            "whats-killing-fix-and-flip-profit": m(
                "faf-distressed-800w.webp",
                "Profit leaks on fix-and-flip rehabs",
            ),
            "why-fix-and-flip-loan-keeps-falling-through": m(
                "faf-fast-close-800w.webp",
                "Why fix-and-flip loans fall out before closing",
            ),
        },
        [
            m("faf-hero-800w.webp", "Fix-and-flip loans for residential investors"),
            m("faf-intro-800w.webp", "Rehab and resale financing"),
            m("faf-purchase-rehab-800w.webp", "Purchase and renovation capital for flips"),
        ],
    ),
    (
        "merchant-cash-advance/articles",
        {
            "how-fast-can-you-get-merchant-cash-advance": m(
                "mca-speed-approval-800w.webp",
                "Speed of merchant cash advance funding",
            ),
            "how-much-can-you-qualify-for-merchant-cash-advance": m(
                "mca-amounts-800w.webp",
                "MCA advance sizing from card and deposit volume",
            ),
            "how-to-apply-merchant-cash-advance": m(
                "mca-intro-800w.webp",
                "Applying for a merchant cash advance",
            ),
            "how-to-get-out-of-an-mca": m(
                "mca-flexible-repayment-800w.webp",
                "Exiting or restructuring stacked MCA obligations",
            ),
            "mca-for-auto-repair-shops": m(
                "mca-hero-800w.webp",
                "Merchant cash advance use in auto repair businesses",
            ),
            "mca-for-restaurants": m(
                "mca-restaurants-800w.webp",
                "Restaurant cash flow and merchant cash advances",
            ),
            "mca-for-retail-stores": m(
                "mca-retail-800w.webp",
                "Retail stores using MCA products for working capital",
            ),
            "mca-mistakes-keep-you-in-cycle": m(
                "mca-daily-sales-800w.webp",
                "Mistakes that trap businesses in MCA cycles",
            ),
            "merchant-cash-advance-requirements": m(
                "mca-intro-800w.webp",
                "Typical requirements to qualify for an MCA",
            ),
            "merchant-cash-advance-vs-working-capital-loan": m(
                "mca-fast-funding-800w.webp",
                "MCA compared with working capital term products",
            ),
            "reasons-mca-funding-gets-delayed": m(
                "mca-speed-approval-800w.webp",
                "Why MCA funding is delayed after approval",
            ),
            "red-flags-mca-agreements": m(
                "mca-flexible-repayment-800w.webp",
                "Red flags in merchant cash advance contracts",
            ),
            "what-credit-score-needed-merchant-cash-advance": m(
                "mca-amounts-800w.webp",
                "How credit factors into MCA offers",
            ),
            "what-do-lenders-look-for-merchant-cash-advance": m(
                "mca-hero-800w.webp",
                "What MCA funders review in underwriting",
            ),
            "what-is-merchant-cash-advance-how-does-it-work": m(
                "mca-intro-800w.webp",
                "How merchant cash advances work for small businesses",
            ),
            "whats-preventing-merchant-cash-advance": m(
                "mca-amounts-800w.webp",
                "Blockers to MCA approval and funding",
            ),
            "why-mca-daily-payment-higher-than-expected": m(
                "mca-daily-sales-800w.webp",
                "Daily MCA remittance amounts and factor math",
            ),
            "why-stuck-in-mca-cycle": m(
                "mca-flexible-repayment-800w.webp",
                "Breaking out of repeated MCA stacking",
            ),
        },
        [
            m("mca-hero-800w.webp", "Merchant cash advance for small business cash flow"),
            m("mca-intro-800w.webp", "MCA funding tied to sales volume"),
            m("mca-fast-funding-800w.webp", "Fast MCA funding timelines"),
        ],
    ),
    (
        "revenue-based-financing/articles",
        {
            "how-fast-can-you-get-revenue-based-financing": m(
                "rbf-fast-funding-800w.webp",
                "How quickly revenue-based financing can fund",
            ),
            "how-much-can-you-qualify-for-revenue-based-financing": m(
                "rbf-amounts-800w.webp",
                "Sizing revenue-based financing from recurring revenue",
            ),
            "revenue-based-financing-d2c-brands": m(
                "rbf-ecommerce-800w.webp",
                "Revenue-based financing for D2C and ecommerce brands",
            ),
            "revenue-based-financing-professional-services": m(
                "rbf-service-800w.webp",
                "RBF for professional and services businesses",
            ),
            "revenue-based-financing-requirements": m(
                "rbf-intro-800w.webp",
                "Requirements to qualify for revenue-based financing",
            ),
            "revenue-based-financing-saas-companies": m(
                "rbf-saas-800w.webp",
                "Revenue-based financing for SaaS and subscription revenue",
            ),
            "revenue-based-financing-traps": m(
                "rbf-no-fixed-800w.webp",
                "Traps and costly terms in some RBF structures",
            ),
            "revenue-based-financing-vs-merchant-cash-advance": m(
                "rbf-flexible-repayment-800w.webp",
                "RBF compared with merchant cash advance products",
            ),
            "what-credit-score-needed-revenue-based-financing": m(
                "rbf-amounts-800w.webp",
                "Credit’s role in revenue-based financing approvals",
            ),
            "what-do-lenders-look-for-revenue-based-financing": m(
                "rbf-hero-800w.webp",
                "What RBF providers underwrite beyond headline revenue",
            ),
            "what-is-revenue-based-financing-how-does-it-work": m(
                "rbf-intro-800w.webp",
                "How revenue-based financing agreements work",
            ),
            "when-is-revenue-based-financing-not-right-option": m(
                "rbf-no-fixed-800w.webp",
                "When RBF is the wrong fit for your capital need",
            ),
            "why-revenue-based-financing-advance-lower-than-needed": m(
                "rbf-amounts-800w.webp",
                "Why RBF advances come in below your request",
            ),
            "why-revenue-based-financing-not-working": m(
                "rbf-growth-capital-800w.webp",
                "When RBF fails to solve the underlying cash need",
            ),
        },
        [
            m("rbf-hero-800w.webp", "Revenue-based financing for growing businesses"),
            m("rbf-intro-800w.webp", "Growth capital tied to sales or MRR"),
            m("rbf-saas-800w.webp", "RBF for recurring-revenue companies"),
        ],
    ),
    (
        "securities-based-lending/articles",
        {
            "how-does-securities-based-lending-work": m(
                "sbl-intro-800w.webp",
                "How securities-based lending and portfolio lines work",
            ),
            "how-much-can-you-borrow-with-securities-based-lending": m(
                "sbl-amounts-800w.webp",
                "Advance rates and borrowing capacity against eligible securities",
            ),
            "securities-based-lending-business-acquisition": m(
                "sbl-acquisition-800w.webp",
                "Using securities-backed liquidity for business acquisitions",
            ),
            "securities-based-lending-real-estate": m(
                "sbl-bridge-800w.webp",
                "Securities-based lending alongside real estate transactions",
            ),
            "securities-based-lending-tax-planning": m(
                "sbl-tax-liquidity-800w.webp",
                "Tax-aware liquidity strategies with securities-based credit",
            ),
            "securities-based-lending-traps-margin-calls-cross-collateral-concentration": m(
                "sbl-concentrated-equity-800w.webp",
                "Margin calls, concentration, and cross-collateral risks in SBL",
            ),
            "what-are-the-risks-of-securities-based-lending": m(
                "sbl-preserve-portfolio-800w.webp",
                "Market and collateral risks in securities-based lending",
            ),
            "when-should-you-use-securities-based-lending": m(
                "sbl-strategic-timing-800w.webp",
                "When securities-based credit fits your liquidity plan",
            ),
        },
        [
            m("sbl-hero-800w.webp", "Securities-based lending for business owners"),
            m("sbl-intro-800w.webp", "Borrowing against investment portfolios"),
            m("sbl-fast-liquidity-800w.webp", "Fast liquidity without selling securities"),
        ],
    ),
]

BATCH24 = re.compile(r"<section\s[^>]*\bdata-batch24[^>]*>[\s\S]*?</section>\s*", re.I)
LEAD_FIGURE_BLOCK = re.compile(
    r'\s*<figure class="article-lead-visual">[\s\S]*?</figure>\s*', re.I
)
MAIN_OPEN = re.compile(r'<main\s+class="blog-post-main"[^>]*>', re.I)

FIGURE = """            <figure class="article-lead-visual">
              <picture>
                <source srcset="/assets/{src}" type="image/webp">
                <img src="/assets/{src}" alt="{alt}" width="{w}" height="{h}" loading="eager" decoding="async" fetchpriority="high">
              </picture>
            </figure>"""


def pick_image(slug: str, slug_map: dict, rotate: list) -> tuple[str, str, int, int]:
    if slug in slug_map:
        return slug_map[slug]
    i = sum(ord(c) for c in slug) % len(rotate)
    return rotate[i]


def strip_batch24(html: str) -> str:
    prev = ""
    while prev != html:
        prev = html
        html = BATCH24.sub("", html, count=1)
    return html


def _insert_offset_after_first_paragraph(chunk: str) -> int | None:
    m = re.search(r"<p\b[^>]*>[\s\S]*?</p>", chunk)
    if not m:
        return None
    after_p = chunk[m.end() :]
    ws = after_p[: len(after_p) - len(after_p.lstrip())]
    tail = after_p.lstrip()
    if tail.startswith("<ul"):
        close = tail.find("</ul>")
        if close < 0:
            return m.end()
        return m.end() + len(ws) + close + len("</ul>")
    if tail.startswith("<ol"):
        close = tail.find("</ol>")
        if close < 0:
            return m.end()
        return m.end() + len(ws) + close + len("</ol>")
    return m.end()


def insert_lead_figure(html: str, slug: str, slug_map: dict, rotate: list) -> str:
    mo = MAIN_OPEN.search(html)
    if not mo:
        return html
    start = mo.end()
    end = html.find("</main>", start)
    if end < 0:
        return html
    chunk = html[start:end]
    off = _insert_offset_after_first_paragraph(chunk)
    if off is None:
        return html
    insert_at = start + off
    src, alt, w, h = pick_image(slug, slug_map, rotate)
    fig = FIGURE.format(src=src, alt=alt.replace('"', "&quot;"), w=w, h=h)
    return html[:insert_at] + "\n" + fig + html[insert_at:]


def bump_modified(html: str) -> str:
    html = re.sub(
        r'<meta property="article:modified_time" content="[^"]*">',
        f'<meta property="article:modified_time" content="{MODIFIED}">',
        html,
        count=1,
    )
    html = re.sub(
        r'"dateModified":"[^"]*"',
        f'"dateModified":"{MODIFIED}"',
        html,
        count=1,
    )
    months = (
        "",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )
    y, mo, d = MODIFIED.split("-")
    label = f"{months[int(mo)]} {int(d)}, {y}"
    html = re.sub(
        r'(<span class="blog-rail-label">Updated</span>\s+)\w+ \d+, \d{4}',
        rf"\g<1>{label}",
        html,
        count=1,
    )
    return html


def process_file(path: Path, slug: str, slug_map: dict, rotate: list) -> bool:
    raw = path.read_text(encoding="utf-8")
    new = strip_batch24(raw)
    new = LEAD_FIGURE_BLOCK.sub("\n", new, count=1)
    new = insert_lead_figure(new, slug, slug_map, rotate)
    new = bump_modified(new)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    total = 0
    for rel, slug_map, rotate in SERVICE_CONFIG:
        base = ROOT / rel
        if not base.is_dir():
            print("skip missing", rel)
            continue
        for d in sorted(base.iterdir()):
            if not d.is_dir() or d.name.startswith("."):
                continue
            idx = d / "index.html"
            if not idx.is_file():
                continue
            if process_file(idx, d.name, slug_map, rotate):
                total += 1
                print("updated", rel, d.name)
    print(f"Done. {total} files changed across {len(SERVICE_CONFIG)} services.")


if __name__ == "__main__":
    main()
