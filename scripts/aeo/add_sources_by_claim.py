#!/usr/bin/env python3
"""AEO plan 1e: a "Sources & Further Reading" block on every article and money page.

131 pages had one. This extends it without filler: a primary source is attached to a page
ONLY when the page's own visible copy makes the kind of claim that source backs (it says
"Section 179" -> IRS Publication 946; "SOFR" -> the New York Fed's SOFR page; "Coast Guard
documentation" -> the USCG documentation center). A page whose copy matches nothing gets
nothing and is listed, rather than a generic list.

Every URL is either already used by the cluster modules (vetted when those were built) or
was checked to return HTTP 200 on 2026-10-22: SOFR, H.15, the CFPB medical-credit-card
report and uscourts.gov bankruptcy. FinCEN BOI is left out: its reporting rules changed in
2025, so a link would date the page.

Markup, disclaimer and placement are the ones scripts/add-article-sources.py uses
(h2#article-sources-h2 before the FAQ heading, or before the closing CTA). Scope: every
indexable /articles/ page plus scripts/aeo/money-pages.txt. Pages rendered by cluster
modules already carry sources (article_v2.py requires them) and are skipped by the
"already has one" check.

    python scripts/aeo/add_sources_by_claim.py            # dry run: what each page would get
    python scripts/aeo/add_sources_by_claim.py --apply
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAX_SOURCES = 4


def S(url, name, desc, trigger, min_hits=1):
    """min_hits > 1 for broad terms, so a passing mention does not earn the source."""
    return {"url": url, "name": name, "desc": desc, "re": re.compile(trigger, re.I), "min": min_hits}


CATALOG = [
    S("https://www.sba.gov/funding-programs/loans/7a-loans", "SBA 7(a) Loan Program",
      "Official terms, eligibility and the $5 million program maximum for the SBA's primary business loan.",
      r"\bSBA\b|7\(a\)", 2),
    S("https://www.sba.gov/funding-programs/loans/504-loans", "SBA 504 Loan Program",
      "Official 504 program terms: a bank, a Certified Development Company and the borrower's own injection.",
      r"SBA 504|\b504 (?:loan|program|project|refinanc)|\bCDC\b"),
    S("https://www.sba.gov/funding-programs/loans/lender-match", "SBA Lender Match",
      "The SBA's own tool for connecting a borrower with participating SBA lenders.",
      r"Lender Match"),
    S("https://www.irs.gov/publications/p946", "IRS Publication 946: How To Depreciate Property",
      "The authority on Section 179 expensing and depreciation for financed equipment and vehicles.",
      r"Section 179|bonus depreciation|depreciation deduction|tax depreciation|deduct(?:ion|ible)"),
    S("https://www.irs.gov/publications/p527", "IRS Publication 527: Residential Rental Property",
      "IRS rules on rental income, expenses and depreciation for residential rental property.",
      r"rental propert"),
    S("https://www.fedsmallbusiness.org/", "Federal Reserve Small Business Credit Survey",
      "Survey data on how small firms apply for and receive credit: approval rates, funding speed and reasons for denial.",
      r"approv(?:al|ed) (?:rate|odds)|\bdenied\b|\bdenial|declined"),
    S("https://www.federalreserve.gov/data/sloos.htm", "Federal Reserve Senior Loan Officer Opinion Survey",
      "Quarterly survey of bank lending standards, including commercial real estate and business loans.",
      r"commercial real estate|\bCRE\b|lending standards|underwriting standards", 2),
    S("https://www.federalreserve.gov/releases/h15/", "Federal Reserve H.15: Selected Interest Rates",
      "The Federal Reserve's published series for the bank prime loan rate and Treasury yields.",
      r"prime rate|\bprime\s*\+|Treasury yield"),
    S("https://www.newyorkfed.org/markets/reference-rates/sofr", "Federal Reserve Bank of New York: SOFR",
      "The administrator's daily publication of the Secured Overnight Financing Rate that floating loans price over.",
      r"\bSOFR\b"),
    S("https://www.consumerfinance.gov/data-research/small-business-lending/", "CFPB Small Business Lending Research",
      "CFPB research and rulemaking on small business credit, including how cost is disclosed to borrowers.",
      r"factor rate|merchant cash advance|\bMCA\b|APR[- ]equivalent"),
    S("https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic",
      "FTC: Protecting Small Businesses Seeking Financing",
      "The FTC's guidance to lenders, brokers and merchant cash advance providers on misrepresented costs, unlawful collection and false claims of government affiliation.",
      r"predatory|stacking|confession of judgment|\bscams?\b|red flags? (?:in|to avoid|and what to avoid)|hidden fees?|upfront fees?"),
    S("https://www.consumerfinance.gov/data-research/research-reports/medical-credit-cards-and-financing-plans/",
      "CFPB: Medical Credit Cards and Financing Plans",
      "CFPB research on patient financing products, including deferred-interest promotions.",
      r"CareCredit|PatientFi|patient financing|medical credit card|deferred[- ]interest"),
    S("https://www.finra.org/investors/insights/securities-backed-lines-credit", "FINRA: Securities-Backed Lines of Credit Explained",
      "FINRA's guidance on SBLOCs, including maintenance requirements and what happens when collateral falls.",
      r"securities[- ]based|\bSBLOC|margin call|pledged (?:securities|portfolio)"),
    S("https://www.hud.gov/program_offices/housing/mfh", "HUD Multifamily Housing Programs",
      "Federal multifamily loan programs and their requirements, a benchmark for multifamily terms.",
      r"multifamily", 2),
    S("https://www.consumerfinance.gov/ask-cfpb/what-is-a-home-equity-loan-en-106/", "CFPB: What is a home equity loan?",
      "The CFPB's plain explanation of borrowing against a home, and what is at risk if payments stop.",
      r"home equity|\bHELOC"),
    S("https://www.census.gov/constructionspending/", "U.S. Census Bureau: Construction Spending",
      "Monthly national construction put-in-place data, the context for contractor job volume.",
      r"construction spending|construction (?:volume|activity)"),
    S("https://www.faa.gov/licenses_certificates/aircraft_certification", "FAA Aircraft Certification",
      "FAA certification and airworthiness rules that determine whether an aircraft is financeable collateral.",
      r"\baircraft\b|airframe|airworth"),
    S("https://www.faa.gov/uas/commercial_operators", "FAA Commercial UAS Operators",
      "FAA rules for flying drones commercially under Part 107.",
      r"Part 107|\bdrones?\b"),
    S("https://www.dco.uscg.mil/Our-Organization/Deputy-for-Operations-Policy-and-Capabilities-DCO-D/National-Vessel-Documentation-Center/",
      "US Coast Guard National Vessel Documentation Center",
      "Federal documentation of commercial vessels, the record a marine lender's preferred mortgage is filed against.",
      r"Coast Guard|\bUSCG\b|documented vessel|vessel documentation|preferred (?:ship )?mortgage"),
    S("https://www.fisheries.noaa.gov/topic/laws-policies", "NOAA Fisheries Laws and Policies",
      "Federal fisheries rules and permits, which shape the revenue a fishing vessel loan is underwritten on.",
      r"\bNOAA\b|fishing permit|fisheries|commercial fishing"),
    S("https://www.fmcsa.dot.gov/registration/commercial-drivers-license", "FMCSA Commercial Driver Licensing",
      "Federal registration and licensing rules for commercial motor vehicles and their drivers.",
      r"\bFMCSA\b|\bCDL\b|\bUSDOT\b|DOT number|operating authority|MC number"),
    S("https://www.bts.gov/", "Bureau of Transportation Statistics",
      "Federal freight and trucking data, the public record behind claims about volumes and rates.",
      r"freight (?:volume|rate|market)|spot rate"),
    S("https://www.dol.gov/agencies/whd/flsa", "US Department of Labor: Fair Labor Standards Act",
      "Federal wage and overtime rules, which set the floor for a labor-heavy business's payroll.",
      r"\bovertime\b|\bFLSA\b|minimum wage"),
    S("https://sam.gov/", "SAM.gov",
      "The federal registration system a business must be active in to hold a federal contract.",
      r"government contract|federal contract|SAM\.gov"),
    S("https://www.energy.gov/eere/buildings/data-centers-and-servers", "US Department of Energy: Data Centers and Servers",
      "DOE material on data center energy use, the largest operating cost behind a data center budget.",
      r"data cent(?:er|re)"),
    S("https://www.appraisers.org/", "American Society of Appraisers",
      "The professional body for machinery, equipment and business appraisers.",
      r"equipment apprais|appraiser|fair market value"),
    S("https://www.uscourts.gov/services-forms/bankruptcy", "U.S. Courts: Bankruptcy Basics",
      "The federal courts' explanation of business bankruptcy chapters and what each does to creditors.",
      r"bankruptcy|Chapter (?:7|11|13)\b"),
]

DISCLAIMER = ("<p>Rate, fee, and policy figures cited above reflect current "
              "published guidance as of the article publication date. Always "
              "confirm current figures with the cited source or your lender "
              "before acting on financing decisions.</p>")
ANCHORS = (
    re.compile(r'<h2[^>]*id="faq"'),
    re.compile(r'<h2[^>]*id="ax-faq-h"'),
    re.compile(r'<h2[^>]*>\s*Frequently Asked Questions', re.I),
    re.compile(r'<div class="faq">'),
    re.compile(r'<h2[^>]*id="[^"]*-faqs?"'),            # money pages: "<topic>-faqs"
    re.compile(r'<h2[^>]*id="related-reading"'),        # short articles with no FAQ
    re.compile(r'<h2[^>]*id="ready-to-get-funded"'),
    re.compile(r'<h2[^>]*id="financing-guides-for-'),   # industry pillars: before the guide list
)


def outside_wrappers(s, at):
    """v2 sections wrap their heading: <div class="group" ...>\\n<div class="group-head"><h2>.
    Inserting at the <h2> would put the sources inside that section's header box, so step
    back past the group-head and then the group opener when they sit directly before it."""
    # Also an empty jump target (<span id="frequently-asked-questions"></span>) that belongs
    # to the heading: links to it must still land on the FAQ, not on the sources.
    for opener in (r'<span id="[^"]*"></span>\s*$', r'<div class="group-head">\s*$', r'<div class="group"[^>]*>\s*$'):
        m = re.search(opener, s[max(0, at - 200):at])
        if m:
            at = max(0, at - 200) + m.start()
    return at


def closing_cta(s):
    """Fallback: the last section before the footer, when it is the closing call to action
    (it holds the cta-actions buttons) - the same spot as the ready-to-get-funded anchor."""
    end = s.find("<!-- AXIANT-FOOTER:START")
    i = s.rfind('<div class="group-head"><h2', 0, end if end > 0 else len(s))
    if i > 0 and "cta-actions" in s[i:end]:
        return i
    return None
STRIP = [re.compile(p, re.S) for p in (
    r"<head>.*?</head>", r"<script\b.*?</script>", r"<style\b.*?</style>", r"<nav\b.*?</nav>",
    r"<footer\b.*?</footer>", r"<aside\b.*?</aside>",
    r"<!-- AXIANT-HEADER:START.*?<!-- AXIANT-HEADER:END -->",
    r"<!-- AXIANT-FOOTER:START.*?<!-- AXIANT-FOOTER:END -->",
    r"<!-- AXIANT-GETMATCHED:START.*?<!-- AXIANT-GETMATCHED:END -->",
    # A link names another page; its words are not a claim this page makes.
    r"<a\b[^>]*>.*?</a>",
    # Related-resources / guide tile grids at the end of a page.
    r'<h2[^>]*id="(?:related-[a-z-]*|cluster-guides|financing-guides-for-[a-z-]*)".*?(?=<h2|<!-- AXIANT-FOOTER)')]


def visible_text(html):
    for p in STRIP:
        html = p.sub(" ", html)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))


def pick(text):
    scored = []
    for i, src in enumerate(CATALOG):
        n = len(src["re"].findall(text))
        if n >= src["min"]:
            scored.append((-n, i, src))
    scored.sort(key=lambda t: (t[0], t[1]))
    return [s for _, _, s in scored[:MAX_SOURCES]]


def block(sources, nl):
    items = nl.join(
        f'<li><a href="{s["url"]}" rel="noopener nofollow" target="_blank">{s["name"]}</a> '
        f'&mdash; {s["desc"]}</li>' for s in sources)
    return (f'<h2 id="article-sources-h2">Sources &amp; Further Reading</h2>{nl}'
            f'<ul>{nl}{items}{nl}</ul>{nl}{DISCLAIMER}{nl}')


def targets():
    pages = [p for p in ROOT.glob("**/articles/*/index.html")
             if "node_modules" not in p.parts and not any(x.startswith("_backup") for x in p.parts)]
    for line in (ROOT / "scripts/aeo/money-pages.txt").read_text(encoding="utf-8").splitlines():
        if line.startswith("/"):
            pages.append(ROOT / line.lstrip("/"))
    return pages


def main(apply):
    added = has = none = noanchor = noindex = 0
    unmatched = []
    for f in targets():
        s = f.read_bytes().decode("utf-8")
        if re.search(r'<meta[^>]+name="robots"[^>]+noindex', s):
            noindex += 1
            continue
        if "article-sources-h2" in s:
            has += 1
            continue
        chosen = pick(visible_text(s))
        rel = f.relative_to(ROOT).as_posix()
        if not chosen:
            none += 1
            unmatched.append(rel)
            continue
        m = next((a.search(s) for a in ANCHORS if a.search(s)), None)
        at = m.start() if m else closing_cta(s)
        if at is None:
            print(f"  NO ANCHOR  {rel}")
            noanchor += 1
            continue
        at = outside_wrappers(s, at)
        nl = "\r\n" if "\r\n" in s else "\n"
        if apply:
            f.write_bytes((s[:at] + block(chosen, nl) + s[at:]).encode("utf-8"))
        added += 1
        print(f"  +{len(chosen)}  {rel}  [{', '.join(c['name'].split(':')[0][:28] for c in chosen)}]")
    print(f"\n{'added' if apply else 'would add'} {added}, already had {has}, no matching claim {none}, "
          f"no anchor {noanchor}, noindex {noindex}")
    if unmatched:
        print("pages with no claim any catalog source backs (left without a block):")
        for u in unmatched:
            print("   ", u)
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
