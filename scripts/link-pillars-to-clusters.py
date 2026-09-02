# -*- coding: utf-8 -*-
"""
Link every cluster pillar down to its own articles.

The clusters were built with links up (article -> pillar) and sideways
(article -> sibling), which the plan required. Nobody wired the third leg. A
sweep of all nine pillars found zero links down, which means 42 articles are
reachable only from the sitemap and from each other - the hub-and-spoke has no
spokes leaving the hub.

This appends one <section class="about-section"> per pillar, in the page's own
idiom, immediately before the closing cta-section so the call to action stays
last. Each entry is the article title and its lede, so the section reads as
navigation rather than a link dump.

Idempotent: a pillar that already carries the section is skipped.

Run with --apply to write; default is a dry run.
"""
import importlib
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

CTA = re.compile(r'<section class="about-section cta-section"', re.I)
MARKER = 'id="cluster-guides"'

CLUSTERS = ["truck_title", "res_business_loan", "heloc", "equip_appraisal",
            "security_guard", "aircraft", "marine", "drone", "datacenter"]

HEADINGS = {
    "truck_title": "Truck Title Loan Guides",
    "res_business_loan": "Property-Secured Business Loan Guides",
    "heloc": "Business HELOC Guides",
    "equip_appraisal": "Equipment Appraisal Guides",
    "security_guard": "Security Guard Company Financing Guides",
    "aircraft": "Aircraft Financing Guides",
    "marine": "Commercial Marine Financing Guides",
    "drone": "Drone Financing Guides",
    "datacenter": "Data Center Financing Guides",
}


def build_section(mod, key):
    hub = "/" + mod.CLUSTER["hub"] + "/"
    heading = HEADINGS[key]
    items = ""
    for a in mod.ARTICLES:
        lede = a["lede"].rstrip(".")
        items += (f'<li><strong><a href="{hub}{a["slug"]}/">{a["h1"]}</a>'
                  f"</strong> &mdash; {lede}.</li>\n")
    return (
        '<section class="about-section">\n'
        f'<h2 {MARKER}>{heading}</h2>\n'
        f'<p>{mod.CLUSTER["hub_lede"]}. '
        f'<a href="{hub}">See all {len(mod.ARTICLES)} guides</a>.</p>\n'
        f"<ul>\n{items}</ul>\n"
        "</section>\n"
    )


def main(apply_changes):
    for key in CLUSTERS:
        mod = importlib.import_module("cluster_" + key)
        pillar = os.path.join(ROOT, mod.CLUSTER["pillar"])
        if not os.path.exists(pillar):
            print(f"  !! {mod.CLUSTER['pillar']:45} missing")
            continue
        s = io.open(pillar, encoding="utf-8").read()
        if MARKER in s:
            print(f"     {mod.CLUSTER['pillar']:45} already linked")
            continue
        m = CTA.search(s)
        if not m:
            print(f"  !! {mod.CLUSTER['pillar']:45} no cta-section anchor")
            continue
        block = build_section(mod, key)
        out = s[:m.start()] + block + s[m.start():]
        print(f"     {mod.CLUSTER['pillar']:45} "
              f"+{len(mod.ARTICLES)} links")
        if apply_changes:
            io.open(pillar, "w", encoding="utf-8", newline="").write(out)
    print("\n  applied" if apply_changes else "\n  dry run - pass --apply")


if __name__ == "__main__":
    main("--apply" in sys.argv)
