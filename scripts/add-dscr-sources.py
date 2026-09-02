# -*- coding: utf-8 -*-
"""
Give the two moved DSCR articles the sources block their 60 siblings have.

60 of the 62 cluster articles end in a "Sources & Further Reading" list citing
two or three federal sources; these two do not, because they predate the
cluster generator and were moved into the hub rather than built by it. On YMYL
financial pages an inconsistent citation pattern across one cluster is exactly
the kind of thing a quality rater notices, and it costs nothing to fix.

Every URL below returned 200 when checked. The two that looked plausible and
were not live - an FHFA national-mortgage-database path - were dropped rather
than guessed at.

Inserted immediately before the CTA section, in the same markup the generator
emits, so the two pages become indistinguishable from their siblings.

Run with --apply to write; default is a dry run.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SOURCES = {
    "dscr-loans/articles/dscr-loan-vs-conventional-mortgage/index.html": [
        ("https://www.consumerfinance.gov/rules-policy/regulations/1026/43/",
         "CFPB Regulation Z &sect;1026.43: Ability to Repay",
         "The ability-to-repay rule that governs a conventional consumer "
         "mortgage - and the reason a DSCR loan, made for business purpose, "
         "is underwritten on the property instead of your income."),
        ("https://www.irs.gov/publications/p527",
         "IRS Publication 527: Residential Rental Property",
         "The federal definition of rental income and deductible expenses, "
         "which is the schedule an underwriter reads when your return is on "
         "file."),
        ("https://www.federalreserve.gov/data/sloos.htm",
         "Federal Reserve Senior Loan Officer Opinion Survey",
         "Quarterly survey of bank lending standards. The public record of "
         "whether conventional underwriting is tightening or loosening."),
    ],
    "dscr-loans/articles/dscr-rental-loans-real-estate-investors/index.html": [
        ("https://www.irs.gov/publications/p527",
         "IRS Publication 527: Residential Rental Property",
         "How the IRS treats rental income, depreciation and expenses on an "
         "investment property held in a rental business."),
        ("https://www.consumerfinance.gov/rules-policy/regulations/1026/43/",
         "CFPB Regulation Z &sect;1026.43: Ability to Repay",
         "The consumer-mortgage rule a business-purpose DSCR loan sits "
         "outside of, which is what makes property-based underwriting "
         "possible."),
        ("https://www.federalreserve.gov/data/sloos.htm",
         "Federal Reserve Senior Loan Officer Opinion Survey",
         "Quarterly survey of bank lending standards and collateral "
         "requirements across real estate lending."),
    ],
}

SECTION = re.compile(r'<section class="section[^"]*">')


def block(items):
    """These two use the v1 section idiom, not the v2 article template, so the
    list is wrapped the way the rest of the page wraps content. A bare h2 and
    ul dropped between sections would sit outside .container and render
    full-bleed and unstyled."""
    lis = "\n".join(
        f'<li><a href="{u}" rel="noopener nofollow" target="_blank">{t}</a>'
        f" &mdash; {d}</li>"
        for u, t, d in items)
    return ('<section class="section">\n<div class="container">\n'
            '<div class="group" data-tone="blue">\n'
            '<div class="group-head">'
            '<h2 id="article-sources-h2">Sources &amp; Further Reading</h2>'
            "</div>\n"
            f'<div class="prose">\n<ul>\n{lis}\n</ul>\n</div>\n'
            "</div>\n</div>\n</section>\n")


def cta_start(s):
    """The CTA is the section carrying a cta-action paragraph. Sources go
    immediately before it, which is where the generator puts them on the
    other 60."""
    for m in SECTION.finditer(s):
        end = s.find("</section>", m.end())
        if end > 0 and "cta-action" in s[m.end():end]:
            return m.start()
    return -1


def main(apply_changes):
    for rel, items in SOURCES.items():
        p = os.path.join(ROOT, *rel.split("/"))
        s = io.open(p, encoding="utf-8").read()
        if "article-sources-h2" in s:
            print(f"     {rel:62} already has one")
            continue
        at = cta_start(s)
        if at < 0:
            print(f"  !! {rel:62} no CTA section to anchor to")
            continue
        out = s[:at] + block(items) + s[at:]
        print(f"     {rel:62} +{len(items)} sources")
        if apply_changes:
            io.open(p, "w", encoding="utf-8", newline="").write(out)
    print("\n  applied" if apply_changes else "\n  dry run - pass --apply")


if __name__ == "__main__":
    main("--apply" in sys.argv)
