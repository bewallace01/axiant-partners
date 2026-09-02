# -*- coding: utf-8 -*-
"""
Point the six pillar heroes at their own images.

Five pillars - aircraft, commercial marine, data center, drone and HELOC - all
used assets/bloc-hero-business-office.webp, a stock shot of people at a desk
with laptops. A sixth, security guard, borrowed hero-invoice-factoring.webp,
which belongs to the invoice-factoring page. Six pages whose lead image said
nothing about the subject, and on four of them the subject is a brand-new
cluster.

Each page references its hero in four or five places, and they have to move
together:

    og:image        the social card
    twitter:image   the social card
    <link preload>  fetches the hero early - if this still points at the old
                    file the browser downloads an image the page never paints
    .ef-hero        the actual background
    (security guard carries a second background rule that overrides the first)

So this replaces the asset name everywhere it appears on the page rather than
editing the CSS rule alone, and it preserves any ?v= cache-busting suffix
already on the reference.

Run with --apply to write; default is a dry run.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MAP = {
    "aircraft-financing.html":
        ("bloc-hero-business-office", "aircraft-financing-hero"),
    "commercial-marine-financing.html":
        ("bloc-hero-business-office", "commercial-marine-financing-hero"),
    "data-center-financing.html":
        ("bloc-hero-business-office", "data-center-financing-hero"),
    "drone-financing.html":
        ("bloc-hero-business-office", "drone-financing-hero"),
    "heloc-for-business.html":
        ("bloc-hero-business-office", "heloc-for-business-hero"),
    "security-guard-business-financing.html":
        ("hero-invoice-factoring", "security-guard-financing-hero"),
}


def main(apply_changes):
    total = 0
    for name, (old, new) in MAP.items():
        p = os.path.join(ROOT, name)
        s = io.open(p, encoding="utf-8").read()
        if not os.path.exists(os.path.join(ROOT, "assets", new + ".webp")):
            print(f"  !! {name:42} assets/{new}.webp not built yet")
            continue
        n = s.count(old)
        if not n:
            print(f"     {name:42} already repointed")
            continue
        out = s.replace(old, new)
        total += n
        print(f"     {name:42} {n} refs  {old} -> {new}")
        if apply_changes:
            io.open(p, "w", encoding="utf-8", newline="").write(out)
    print(f"\n  {total} references"
          + ("  applied" if apply_changes else "  dry run - pass --apply"))


if __name__ == "__main__":
    main("--apply" in sys.argv)
