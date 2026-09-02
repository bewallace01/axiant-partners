# -*- coding: utf-8 -*-
"""
Show the last-updated date on the nine cluster pillars.

Each pillar now carries dateModified in its JSON-LD (6b9be0869), which is what
the audit's GEO check reads, but nothing on the page says so. A visible date
is the half a human sees, and assistants that summarise a page read the
rendered text as readily as the markup - a financing page with no date on it
reads as undated whatever the schema says.

The date is not invented and not today's date by default: it is read out of
the page's own dateModified, so the visible line and the machine-readable one
can never disagree.

PLACEMENT
Not in the hero. The ef-hero section sits on a dark ground - its own CTAs
override to color:#fff - and a muted grey dateline there would be
low-contrast and hard to read. It goes at the top of the light content area
instead, immediately after the hero, or after the breadcrumb where one
follows the hero (3 of the 9), so a date never sits above the breadcrumb
trail.

STYLING
.dateline is declared in axiant-v2.css, which these pillars do not load - they
load axiant-v2-chrome.css plus axiant-v2-legacy-body.css. Adding the class
alone would render an unstyled paragraph, so the same declaration is rebuilt
in axiant-v2-legacy-body.css on that sheet's own --v2-* tokens, scoped under
.v2-body like every other rule in it. All nine pillars carry v2-body.

Idempotent: a pillar that already has a dateline is skipped.

Run with --apply to write; default is a dry run.
"""
import datetime
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PILLARS = [
    "aircraft-financing.html",
    "commercial-marine-financing.html",
    "drone-financing.html",
    "data-center-financing.html",
    "commercial-truck-title-loan.html",
    "heloc-for-business.html",
    "equipment-appraisal.html",
    "security-guard-business-financing.html",
    "real-estate-secured-business-loan.html",
]

HERO_END = re.compile(r'<section class="ef-hero"[^>]*>.*?</section>', re.S)
CRUMBS = re.compile(r'\A\s*<nav[^>]*class="crumbs"[^>]*>.*?</nav>', re.S)


def main(apply_changes):
    done = skipped = 0
    for name in PILLARS:
        p = os.path.join(ROOT, name)
        s = io.open(p, encoding="utf-8").read()
        if 'class="dateline"' in s:
            print(f"     {name:42} already has one")
            skipped += 1
            continue
        if "v2-body" not in s:
            print(f"  !! {name:42} no v2-body, rule would not apply")
            skipped += 1
            continue
        m = re.search(r'"dateModified":\s*"(\d{4}-\d{2}-\d{2})"', s)
        if not m:
            print(f"  !! {name:42} no dateModified to read")
            skipped += 1
            continue
        d = datetime.date.fromisoformat(m.group(1))
        # the article template renders "Updated September 02, 2026";
        # keep the zero padding so the two read identically
        text = "Updated " + d.strftime("%B %d, %Y")

        hero = HERO_END.search(s)
        if not hero:
            print(f"  !! {name:42} no ef-hero to anchor to")
            skipped += 1
            continue
        at = hero.end()
        crumb = CRUMBS.match(s[at:])
        if crumb:
            at += crumb.end()
        line = f'\n<p class="dateline">{text}</p>'
        out = s[:at] + line + s[at:]
        print(f"     {name:42} {text}"
              f"{'  (after breadcrumb)' if crumb else ''}")
        done += 1
        if apply_changes:
            io.open(p, "w", encoding="utf-8", newline="").write(out)
    print(f"\n  datelines added {done}, skipped {skipped}")
    print("  applied" if apply_changes else "  dry run - pass --apply")


if __name__ == "__main__":
    main("--apply" in sys.argv)
