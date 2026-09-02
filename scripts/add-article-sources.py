# -*- coding: utf-8 -*-
"""
Add a "Sources & Further Reading" block to the pages that earn impressions and
no clicks.

Why these pages. Search Console (_analysis/gsc.json) lists 35 URLs ranking in
the top 15 on 300+ impressions with a click-through rate under 1% -- 34,744
impressions returning 33 clicks. Their titles and descriptions are already
specific and carry real figures, so the snippet is not the problem: the answer
is being read in the SERP. What these pages lack is a reason for a model or a
reader to treat them as the source of the number rather than one more site
repeating it. 33 of the 35 cite nothing at all.

Every URL below returned HTTP 200 and its page title was checked to confirm it
covers the claim it is attached to. investor.gov was dropped from the
securities-based lending set during that check -- the bulletin ID resolved to
"Microcap Stock Basics", not securities-backed credit.

The markup copies the one page on the site that already does this,
articles/same-day-business-funding-whats-actually-possible/: an
<h2 id="article-sources-h2">, a <ul> of links with rel="noopener nofollow", and
the same as-of disclaimer. The block goes immediately before <div class="faq">,
where that page puts it.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SBA_504 = ("https://www.sba.gov/funding-programs/loans/504-loans",
           "SBA 504 Loan Program",
           "The official program terms behind the ~10% borrower equity figure: "
           "504 deals are structured as roughly 50% third-party lender, 40% CDC "
           "debenture, 10% borrower injection.")
SBA_7A = ("https://www.sba.gov/funding-programs/loans/7a-loans",
          "SBA 7(a) Loan Program",
          "Official terms, eligibility and the $5 million program maximum for "
          "the SBA's primary business loan.")
SBA_MATCH = ("https://www.sba.gov/funding-programs/loans/lender-match",
             "SBA Lender Match",
             "The SBA's own lender-matching tool -- useful as the realistic "
             "floor for how quickly an SBA file can reach an approved lender.")
SLOOS = ("https://www.federalreserve.gov/data/sloos.htm",
         "Federal Reserve Senior Loan Officer Opinion Survey",
         "Quarterly survey of bank lending standards, including commercial real "
         "estate. The primary public record of whether underwriting is "
         "tightening or loosening.")
SBCS = ("https://www.fedsmallbusiness.org/",
        "Federal Reserve Small Business Credit Survey",
        "Survey data on how small firms actually apply for and receive credit -- "
        "approval rates, funding speed and reasons for denial.")
CFPB = ("https://www.consumerfinance.gov/data-research/small-business-lending/",
        "CFPB Small Business Lending Research",
        "Consumer Financial Protection Bureau research and rulemaking on small "
        "business credit, including factor-rate and APR-equivalent disclosure.")
IRS_946 = ("https://www.irs.gov/publications/p946",
           "IRS Publication 946: How To Depreciate Property",
           "The authority on Section 179 expensing and bonus depreciation for "
           "financed equipment -- what actually determines the after-tax cost.")
FINRA_SBLOC = ("https://www.finra.org/investors/insights/securities-backed-lines-credit",
               "FINRA: Securities-Backed Lines of Credit Explained",
               "FINRA's investor guidance on SBLOCs, including how maintenance "
               "requirements and margin calls work when collateral falls.")
HUD_MF = ("https://www.hud.gov/program_offices/housing/mfh",
          "HUD Multifamily Housing Programs",
          "Federal multifamily loan programs and their equity requirements, the "
          "benchmark most conventional multifamily terms are quoted against.")
CENSUS_CONST = ("https://www.census.gov/constructionspending/",
                "U.S. Census Bureau: Construction Spending",
                "Monthly national construction put-in-place data -- the context "
                "for how contractor receivables and job volume move.")
FTC = ("https://www.ftc.gov/business-guidance/credit-finance-trade",
       "FTC Business Credit and Finance Guidance",
       "Federal Trade Commission guidance on fair lending practice, fee "
       "disclosure and the warning signs of predatory business credit.")

PAGES = {
    "commercial-real-estate-loans/articles/how-much-down-payment-required-commercial-property-loan/index.html":
        [SBA_504, SBA_7A, SLOOS, HUD_MF],
    "construction-business-financing/why-contractors-need-working-capital/index.html":
        [SBCS, CENSUS_CONST, CFPB],
    "sba-loans/articles/how-long-sba-loan-approval/index.html":
        [SBA_7A, SBA_504, SBA_MATCH],
    "equipment/semi-trucks/semi-truck-financing-down-payment/index.html":
        [SBCS, IRS_946],
    "equipment-financing/articles/how-fast-can-equipment-financing-be-approved/index.html":
        [SBCS, CFPB],
    "construction-business-financing/progress-payment-cash-flow-gaps/index.html":
        [SBCS, CENSUS_CONST],
    "business-line-of-credit/articles/how-fast-can-you-get-approved-business-line-of-credit/index.html":
        [SBCS, CFPB, SLOOS],
    "sba-loans/articles/sba-loan-vs-business-line-of-credit/index.html":
        [SBA_7A, SBCS],
    "securities-based-lending/articles/securities-based-lending-traps-margin-calls-cross-collateral-concentration/index.html":
        [FINRA_SBLOC],
    "securities-based-lending/articles/how-much-can-you-borrow-with-securities-based-lending/index.html":
        [FINRA_SBLOC],
    "equipment-financing/articles/equipment-financing-requirements/index.html":
        [SBCS, IRS_946],
    "commercial-real-estate-loans/articles/multifamily-loan-down-payment/index.html":
        [HUD_MF, SBA_504, SLOOS],
    "commercial-real-estate-loans/articles/what-credit-score-needed-commercial-real-estate-loan/index.html":
        [SLOOS, SBA_7A],
    "sba-loans/articles/sba-loan-restaurant-acquisition/index.html":
        [SBA_7A, SBA_504],
    "business-loan-calculator-guide/index.html":
        [CFPB, FTC],
    "articles/business-loan-guarantee-traps/index.html":
        [FTC, CFPB, SBA_7A],
    "equipment-financing/articles/equipment-financing-vs-sba-loan/index.html":
        [SBA_7A, IRS_946, SBCS],
    "revenue-based-financing/articles/revenue-based-financing-vs-merchant-cash-advance/index.html":
        [CFPB, FTC],
    "commercial-real-estate-loans/articles/how-long-close-commercial-real-estate-loan/index.html":
        [SLOOS, SBA_504],
    "merchant-cash-advance/articles/merchant-cash-advance-vs-working-capital-loan/index.html":
        [CFPB, FTC, SBCS],
}

DISCLAIMER = ("<p>Rate, fee, and policy figures cited above reflect current "
              "published guidance as of the article publication date. Always "
              "confirm current figures with the cited source or your lender "
              "before acting on financing decisions.</p>")

# The block goes after the article body and before the page closes out.
#
# Anchor on the FAQ *heading*, never on <div class="faq">. The div is a sibling
# that follows the <h2>, so inserting before it drops the sources block between
# "Frequently Asked Questions" and its own questions -- an orphaned heading with
# someone else's content under it. Three templates are in use here (h2#faq +
# div.faq, h2#ax-faq-h, and no FAQ at all), so fall through to the closing CTA
# on pages that have no FAQ.
ANCHORS = (
    re.compile(r'<h2[^>]*id="faq"'),
    re.compile(r'<h2[^>]*id="ax-faq-h"'),
    re.compile(r'<h2[^>]*>\s*Frequently Asked Questions', re.I),
    re.compile(r'<div class="faq">'),
    re.compile(r'<h2[^>]*id="ready-to-get-funded"'),
)
ALREADY = re.compile(r'article-sources-h2')


def find_anchor(src):
    for pat in ANCHORS:
        m = pat.search(src)
        if m:
            return m
    return None


def block(sources):
    items = "\n".join(
        f'<li><a href="{url}" rel="noopener nofollow" target="_blank">{name}</a> '
        f'&mdash; {desc}</li>'
        for url, name, desc in sources)
    return ('<h2 id="article-sources-h2">Sources &amp; Further Reading</h2>\n'
            f'<ul>\n{items}\n</ul>\n{DISCLAIMER}\n')


def main(apply_changes):
    added = skipped = missing = noanchor = 0
    print("APPLIED" if apply_changes else "DRY RUN")
    for rel, sources in PAGES.items():
        path = os.path.join(ROOT, rel.replace("/", os.sep))
        if not os.path.exists(path):
            print(f"  MISSING   {rel}")
            missing += 1
            continue
        with open(path, encoding="utf-8") as fh:
            src = fh.read()
        if ALREADY.search(src):
            print(f"  has one   {rel}")
            skipped += 1
            continue
        m = find_anchor(src)
        if not m:
            print(f"  NO ANCHOR  {rel}")
            noanchor += 1
            continue
        out = src[:m.start()] + block(sources) + src[m.start():]
        if apply_changes:
            with open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(out)
        added += 1
        print(f"  +{len(sources)} sources  {rel}")
    print(f"\n  added {added}, already had {skipped}, missing {missing}, no anchor {noanchor}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
