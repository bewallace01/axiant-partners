#!/usr/bin/env python3
"""AEO plan 1c: contextual in-body links into the money pages.

Each entry adds one sentence right after an existing sentence (AFTER, which must occur
exactly once in the page) on a page that already discusses the money page's need. Anchor
text is the buyer's phrase, not the page title. Idempotent: a page that already links the
money page in its body is skipped.

Only hand-maintained pages are listed; none of them is rendered by a cluster module.
Measure with:  python scripts/count_money_page_links.py --list

    python scripts/aeo/add_money_page_links.py [--dry]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TT = "/commercial-truck-title-loan.html"
RE = "/real-estate-secured-business-loan.html"
TOW = "/towing-business-financing.html"
SG = "/security-guard-business-financing.html"
MAR = "/commercial-marine-financing.html"
HEQ = "/heavy-equipment-equity-loan.html"
VEND = "/vending-machine-financing.html"


def a(href, text):
    return f'<a href="{href}">{text}</a>'


# (page, money page, sentence the new one follows, new sentence)
LINKS = [
    # Truck title: owners of paid-off trucks reading the purchase pages
    ("/equipment/semi-trucks/", TT,
     "paying cash ties up capital you need for fuel, maintenance, insurance, and payroll.",
     f"Already own a paid-off rig? You can {a(TT, 'borrow against a semi you own')} instead of financing another."),
    ("/equipment/dump-trucks/", TT,
     "They haul sand, gravel, dirt, and demolition debris.",
     f"If a dump truck in your fleet is already paid off, its equity can fund the next job: see {a(TT, 'borrowing against a dump truck you own')}."),
    ("/equipment/box-trucks/", TT,
     "paying cash ties up capital you need for fuel, payroll, and operations.",
     f"If you own a box truck outright, you can also {a(TT, 'borrow against the truck’s equity')}."),
    ("/trucking-business-financing.html", TT,
     "Small fleets need cash-cycle flexibility between settlements, fuel, insurance, and maintenance.",
     f"Owners with paid-off tractors can also {a(TT, 'borrow against a truck they already own')} to cover that gap."),
    ("/equipment/semi-trucks/semi-truck-financing-bad-credit/", TT,
     "That is why bad credit isn't the end of the conversation.",
     f"If you already own a truck free and clear, a {a(TT, 'title loan against that truck')} leans more on the truck’s value than on the score."),

    # Real-estate secured: owners pulling equity from property they hold
    ("/commercial-real-estate-loans/articles/cash-out-refinance-commercial-property/", RE,
     "It can be more cost-effective than layering additional debt on top of your existing mortgage.",
     f"If the existing mortgage has a rate worth keeping, compare {a(RE, 'a business loan secured by the property’s equity')}, which leaves it in place."),
    ("/commercial-real-estate-loans/articles/cash-out-vs-rate-and-term-commercial-refinance/", RE,
     "or seed a down payment on another property.",
     f"If the existing mortgage carries a rate worth keeping, compare {a(RE, 'a second-position loan against the equity')} instead."),
    ("/commercial-real-estate-loans/articles/commercial-real-estate-refinance/", RE,
     "needs to be replaced with permanent financing.",
     f"To raise cash without replacing the mortgage at all, see {a(RE, 'a business loan secured by property you already own')}."),
    ("/commercial-bridge-loans/articles/bridge-loan-vs-heloc/", RE,
     "rather than collateralize their home for a business purpose.",
     f"Owners who hold commercial or investment property have a third option: {a(RE, 'a business loan secured by that real estate')}."),
    ("/commercial-real-estate-loans/articles/when-to-refinance-commercial-property/", RE,
     "signals 3, 6, and 7 usually point to cash-out.",
     f"If you need cash but want to keep the existing mortgage, compare {a(RE, 'a second-position loan against the property')}."),

    # Towing: pages about the trucks towing companies run
    ("/equipment-financing/articles/tow-truck-wrecker-financing/", TOW,
     "Figures are illustrative ranges, not quotes.",
     f"For working capital on motor-club and police-rotation accounts as well as the trucks, see {a(TOW, 'towing business financing')}."),
    ("/equipment/flatbed-trucks/", TOW,
     "Flatbed trucks haul steel, lumber, machinery, and oversized loads that don't fit in enclosed trailers.",
     f"Rollback carriers run by towing companies are covered under {a(TOW, 'towing business financing')}."),
    ("/trucking-business-financing.html", TOW,
     "Growth-stage fleets need structured capital that supports utilization targets without overextending fixed obligations.",
     f"Towing operators have their own mix of wreckers, rollbacks and net-30 motor-club work: see {a(TOW, 'financing for towing companies')}."),

    # Security guard: payroll-gap and receivables pages
    ("/business-loan-for-payroll.html", SG,
     "can bridge the gap and fund within <strong>1-3 business days</strong>.",
     f"Contract security firms, which pay officers weekly while clients pay on net-30 to net-60, are a common case: see {a(SG, 'payroll funding for security guard companies')}."),
    ("/invoice-factoring.html", SG,
     "trucking carriers, staffing agencies, manufacturers, wholesalers, and service contractors.",
     f"Guard companies are a frequent fit: see {a(SG, 'factoring and payroll funding for security guard companies')}."),
    ("/working-capital-loans/articles/what-is-invoice-factoring/", SG,
     "Staffing agencies factor to make weekly payroll while waiting on client payments.",
     f"Security guard companies do the same: see {a(SG, 'financing for security guard companies')}."),
    ("/working-capital-loans/articles/accounts-receivable-financing/", SG,
     "This focus on receivables means companies with thin credit or limited history can still qualify if they invoice strong customers.",
     f"Contract security firms billing property managers and municipalities are a typical fit; see {a(SG, 'security guard company financing')}."),
    ("/working-capital-loans/articles/working-capital-loan-staffing-agencies/", SG,
     "plus a buffer for disputes or delays.",
     f"Contract security companies face the same cycle; see {a(SG, 'payroll funding for security guard companies')}."),
    ("/working-capital-loans/articles/freight-staffing-factoring/", SG,
     "regardless of when clients actually pay.",
     f"Security guard companies use it the same way for officer payroll: see {a(SG, 'security guard company financing')}."),
    ("/working-capital-loans.html", SG,
     "Payroll due before receivables clear.",
     f"(For contract services that pay staff weekly, see {a(SG, 'security guard payroll funding')}.)"),

    ("/working-capital-loans/articles/working-capital-loan-it-staffing/", SG,
     "it is directly tied to your ability to retain the people who generate your revenue.",
     f"Security guard companies feel the same gap with weekly officer payroll: see {a(SG, 'security guard payroll funding')}."),
    ("/working-capital-loans/articles/home-health-agency-working-capital/", SG,
     "is exactly what working capital is designed to absorb.",
     f"Security guard companies face a similar weekly-payroll gap; see {a(SG, 'financing for security guard companies')}."),

    # Marine: the only other pages that discuss comparable titled, high-value assets
    ("/aircraft-financing.html", MAR,
     "lenders can underwrite it efficiently once the airframe, engine times, and logs check out.",
     f"Commercial vessels are financed on similar lines, with a marine survey in place of the logs: see {a(MAR, 'commercial boat and vessel financing')}."),

    # Heavy equipment equity (AEO 2b, 2026-10-22): owners of paid-off machines on the purchase pages
    ("/equipment/excavators/", HEQ,
     "can strain reserves and limit your ability to bid on new work or cover payroll during slow periods.",
     f"If you already own excavators outright, you can also {a(HEQ, 'borrow against the excavators you own')} instead of paying cash for the next one."),
    ("/equipment/bulldozers/", HEQ,
     "paying cash ties up capital you need for payroll, materials, and growth.",
     f"Already own a paid-off dozer? You can {a(HEQ, 'borrow against the dozer’s equity')} and keep it on the job."),
    ("/equipment/wheel-loaders/", HEQ,
     "paying cash ties up capital you need for payroll, materials, and growth.",
     f"Own a loader outright? See {a(HEQ, 'borrowing against construction equipment you own')}."),
    ("/equipment/skid-steers/", HEQ,
     "paying cash ties up capital you need for payroll, materials, and growth.",
     f"If your skid steers are paid off, {a(HEQ, 'their equity can back a loan')} while they keep working."),
    ("/equipment/backhoes/", HEQ,
     "paying cash ties up capital you need for payroll, materials, and growth.",
     f"If a backhoe in your fleet is paid off, see {a(HEQ, 'borrowing against heavy equipment you own')}."),
    ("/equipment-financing/articles/equipment-refinancing/", HEQ,
     "This is what you want if the payment is straining cash flow.",
     f"To raise cash against machines you own outright, see {a(HEQ, 'heavy equipment equity loans')}."),
    ("/equipment-financing.html", HEQ,
     "Construction companies use equipment financing to expand fleets, replace aging machinery, and take on larger projects.",
     f"Contractors who already own their machines can {a(HEQ, 'borrow against that equipment’s equity')} instead."),

    # Vending: the older spoke stays (it earns non-brand clicks) and points up to the pillar
    ("/equipment-financing/articles/vending-machine-financing/", VEND,
     "route expansion keeps pace with the locations you can land.",
     f"Rates, lease-or-buy, micro-markets and buying a route are covered in {a(VEND, 'vending machine financing for operators')}."),
]

def page_file(url):
    p = ROOT / url.lstrip("/")
    return p / "index.html" if url.endswith("/") else p


def inside(s, i, open_tag, close_tag):
    return s.rfind(open_tag, 0, i) > s.rfind(close_tag, 0, i)


QA_OPEN = re.compile(r'<div[^>]*class="[^"]*\bquick-answer\b[^"]*"[^>]*>|<div class="callout"[^>]*>(?=\s*<p class="eyebrow">Quick answer)'
                     r'|<div class="callout" id="quick">', re.S)
SECTION = re.compile(r'<(?:h2|p class="section-label")[^>]*>', re.S)


def div_end(s, start):
    """Index just past the </div> closing the div opened at start."""
    depth, k = 0, start
    tag = re.compile(r"<(/?)div\b[^>]*>", re.I)
    for t in tag.finditer(s, start):
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return t.end()
    return len(s)


def unsafe(s, i):
    """Why a link may not go at index i, or None. FAQ text must match its FAQPage JSON-LD
    word for word, the Quick Answer stays as 1a left it, and head/scripts are not copy."""
    if i < s.find("<body"):
        return "head"
    if inside(s, i, "<script", "</script>"):
        return "script"
    if inside(s, i, "<details", "</details>"):
        return "FAQ"
    for m in QA_OPEN.finditer(s, 0, i):
        if div_end(s, m.start()) > i:
            return "Quick Answer"
    heads = list(SECTION.finditer(s, 0, i))
    if heads and re.search(r"faq|question", heads[-1].group(0), re.I):
        return "FAQ section"
    return None


def main(dry):
    bad = 0
    for url, money, after, sentence in LINKS:
        f = page_file(url)
        s = f.read_bytes().decode("utf-8")
        body_link = f'<a href="{money}">'
        if body_link in s.split("<!-- AXIANT-FOOTER:START")[0].split("<!-- AXIANT-HEADER:END -->")[-1]:
            print(f"  already links: {url} -> {money}")
            continue
        n = s.count(after)
        if n != 1:
            print(f"  ANCHOR x{n}: {url}: {after[:60]}")
            bad += 1
            continue
        i = s.index(after) + len(after)
        why = unsafe(s, i)
        if why:
            print(f"  REFUSED ({why}): {url}")
            bad += 1
            continue
        new = s[:i] + " " + sentence + s[i:]
        if not dry:
            f.write_bytes(new.encode("utf-8"))
        print(f"  {'would add' if dry else 'added'}: {url} -> {money}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main("--dry" in sys.argv))
