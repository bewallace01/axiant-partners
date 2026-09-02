# -*- coding: utf-8 -*-
"""
Two embed pages were sending the wrong indexing signal.

calculator-embed.html is the iframe payload -- the thing other sites load
inside an <iframe>, 137 words with an off-screen h1. It carried TWO robots
tags, "noindex, follow" on line 18 and "index, follow, max-snippet:-1,
max-image-preview:large" two lines later. Google resolves a conflict like that
by taking the most restrictive directive, so the page was already effectively
noindex -- but the contradiction is the kind of thing that survives until
someone deletes the wrong one. It also self-canonicalised, where every other
embed on the site points at the page it belongs to. Now: one robots tag, and
the canonical points at /calculator.html.

embed-calculator.html is the opposite page and had the opposite problem. It is
the public "put our calculator on your site" offer -- the asset that exists to
earn embeds and links back. It was marked noindex, so nobody could find it. It
also shipped a meta description that had been truncated mid-sentence into
"free, with a? For U". Now indexable, with a description that reads.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def write(p, s):
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(s)


def fix_iframe_payload(apply_changes):
    p = os.path.join(ROOT, "calculator-embed.html")
    s = read(p)
    before = s

    # Drop the indexable directive; keep the noindex one that appears above it.
    s = re.sub(
        r'[ \t]*<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">[ \t]*\r?\n?',
        "", s, count=1)

    # Point at the page this embed is a component of, matching the other embeds.
    s = s.replace(
        '<link rel="canonical" href="https://axiantpartners.com/calculator-embed.html">',
        '<link rel="canonical" href="https://axiantpartners.com/calculator.html">')

    changed = s != before
    if changed and apply_changes:
        write(p, s)
    return "calculator-embed.html", changed


def fix_embed_offer(apply_changes):
    p = os.path.join(ROOT, "embed-calculator.html")
    s = read(p)
    before = s

    s = s.replace(
        '<meta content="noindex, follow" name="robots"/>',
        '<meta content="index, follow, max-snippet:-1, max-image-preview:large" name="robots"/>')

    s = re.sub(
        r'<meta content="Embed our free Equipment[^"]*" name="description"/>',
        '<meta content="Put our free equipment and truck payment calculator on '
        'your own site. Copy one line of embed code - no signup, no fees, no '
        'branding requirements. Built for dealers, brokers and trucking blogs." '
        'name="description"/>',
        s, count=1)

    changed = s != before
    if changed and apply_changes:
        write(p, s)
    return "embed-calculator.html", changed


def main(apply_changes):
    print("APPLIED" if apply_changes else "DRY RUN")
    for name, changed in (fix_iframe_payload(apply_changes),
                          fix_embed_offer(apply_changes)):
        print(f"  {name:26} {'changed' if changed else 'NO MATCH - check by hand'}")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
