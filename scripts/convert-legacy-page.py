# -*- coding: utf-8 -*-
"""
Convert a legacy .ef-hero page onto the v2 design system, whole.

Fourteen pages still carry the pre-v2 template. 828 use .hero-compact. The
conversion is all-or-nothing: swapping the hero alone leaves it unstyled,
because .hero-compact lives in axiant-v2.css and these pages load
axiant-v2-chrome.css + axiant-v2-legacy-body.css instead. Swapping only the
stylesheet strands the body, because axiant-v2.css has no rules for
.about-section, .relevant-post-card, .industry-equipment-row, .section-cta,
.blog-card-link, .ef-phone-cta or .mobile-cta-bar.

So all three move together:

  hero        .ef-hero              -> section.hero-compact + .hero-media img
  body        .about-section        -> section.section[.section-alt]
                                         > .container > .group
                                           > .group-head > h2
                                           > .prose
              .quick-answer         -> .callout
              .relevant-post-card   -> .cards.cards-left > article.card
              .section-cta          -> .cta-actions > a.btn.btn-primary
              .ef-phone-cta         -> a.btn.btn-secondary
              .ef-page-wrap
              .form-container       -> unwrapped
              .mobile-cta-bar       -> dropped; the hero CTA carries it
  stylesheet  chrome + legacy-body  -> axiant-v2.css
              inline <style>        -> deleted

Run with --apply to write; default is a dry run.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HERO = re.compile(r'<section class="ef-hero"[^>]*>(.*?)</section>', re.S)
BG = re.compile(r"\.ef-hero\s*\{[^}]*url\('([^']+)'", re.S)


def hero_block(inner, img, eyebrow):
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", inner, re.S)
    sub = re.search(r'<p class="ef-subhead"[^>]*>(.*?)</p>', inner, re.S)
    bullets = re.findall(r"<li[^>]*>(.*?)</li>", inner, re.S)
    ctas = re.search(r'<div class="ef-hero-ctas"[^>]*>(.*?)</div>', inner, re.S)
    o = ['<section class="hero-compact">']
    if img:
        o.append('<div class="hero-media"><img alt="" decoding="async" '
                 'fetchpriority="high" height="1071" src="%s" width="1920"/>'
                 "</div>" % img)
    o += ['<div class="container">', '<div class="inner">',
          '<p class="eyebrow">%s</p>' % eyebrow,
          "<h1>%s</h1>" % h1.group(1).strip()]
    if sub:
        o.append('<p class="lede">%s</p>' % sub.group(1).strip())
    if bullets:
        o.append('<ul class="hero-checks">')
        for b in bullets:
            t = re.sub(r"^\s*(?:<span[^>]*>)?\s*[✓✔]?\s*", "", b.strip())
            t = re.sub(r"</span>\s*$", "", t).strip()
            o.append('<li><span class="tick">✓</span><span>%s</span></li>' % t)
        o.append("</ul>")
    if ctas:
        o.append('<div class="actions">')
        for href, label in re.findall(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                                      ctas.group(1), re.S):
            label = re.sub(r"<[^>]+>", "", label).strip()
            if href.startswith("tel:"):
                o.append('<span class="call">Or call <a href="%s">%s</a></span>'
                         % (href, label.replace("Call Now: ", "")))
            else:
                o.append('<a class="btn btn-primary btn-lg" href="%s">%s</a>'
                         % (href, label))
        o.append("</div>")
    o += ["</div>", "</div>", "</section>"]
    return "\n".join(o)


def convert(path, apply_changes):
    rel = os.path.relpath(path, ROOT)
    s = io.open(path, encoding="utf-8").read()
    m = HERO.search(s)
    if not m:
        print("  !! %-44s no ef-hero" % rel)
        return False

    bg = BG.search(s)
    crumb = re.search(r'class="crumbs".*?&rsaquo;\s*<a[^>]*>([^<]*)</a>', s, re.S)
    eyebrow = ("Industry financing"
               if crumb and "industr" in crumb.group(1).lower()
               else "Financing program")
    s = s[:m.start()] + hero_block(m.group(1), bg.group(1) if bg else None,
                                   eyebrow) + s[m.end():]

    # stylesheet: the two partial sheets become the real one
    s = re.sub(r'<link[^>]+axiant-v2-chrome\.css[^>]*>\s*', "", s)
    s = re.sub(r'<link[^>]+(?:styles|critical|blog-layout|article-rail|'
               r'article-layout)\.css[^>]*>\s*', "", s)
    s = re.sub(r'<noscript>\s*<link[^>]+styles\.css[^>]*>\s*</noscript>\s*',
               "", s)
    s = re.sub(r'<link[^>]+axiant-v2-legacy-body\.css[^>]*>',
               '<link href="/axiant-v2.css" rel="stylesheet"/>', s)
    s = re.sub(r"<style[^>]*>.*?</style>\s*", "", s, flags=re.S)

    # Unwrap the page-level <div class="container">. On this template it wraps
    # the whole body including the hero; axiant-v2.css gives .container
    # max-width:1200px, so the hero rendered as a 1200px box instead of
    # full-bleed. On the reference page each section is a direct child of body
    # and carries its own .container inside.
    head_end = s.find("AXIANT-HEADER:END")
    op = s.find('<div class="container">', head_end)
    if op != -1 and s.find("<section", head_end) > op:
        depth, k = 0, op
        while k < len(s):
            nd = s.find("<div", k + 1)
            cd = s.find("</div>", k + 1)
            if cd == -1:
                break
            if nd != -1 and nd < cd:
                depth += 1
                k = nd
            else:
                if depth == 0:
                    s = s[:op] + s[op + len('<div class="container">'):cd] +                         s[cd + len("</div>"):]
                    break
                depth -= 1
                k = cd

    # the v2-body class and the sheet that gave it meaning are both gone
    s = s.replace('<body class="v2-body">', "<body>")

    # The breadcrumb and dateline were direct children of the container just
    # unwrapped, so they lost their column and sat at x=0. Wrap them in the
    # section/container the rest of the page now uses.
    WRAP = re.compile(r'(<nav[^>]*class="crumbs".*?</nav>\s*'
                      r'(?:<p class="dateline">.*?</p>\s*)?)', re.S)
    s = WRAP.sub(lambda m: ('<section class="section section-tight">'
                            '<div class="container">' + m.group(1) +
                            '</div></section>'), s, count=1)

    # language-switcher.js is the legacy scroll-reveal script. It adds
    # .reveal/.visible and animates the hero, and the transform that leaves
    # behind creates a containing block, which made the hero photograph
    # invisible: .hero-media sits at z-index:-2 and ended up painting behind
    # the section's own navy background. The reference page does not load it,
    # and the contract bans motion on scroll or page load.
    s = re.sub(r'<script[^>]+language-switcher\.js[^>]*>\s*</script>\s*', "", s)
    s = re.sub(r'\sclass="(reveal|reveal visible)"', "", s)

    # body vocabulary
    s = s.replace('<div class="quick-answer"', '<div class="callout"')
    s = re.sub(r'<div class="ef-page-wrap"[^>]*>', "", s)
    s = re.sub(r'<div class="form-container[^"]*"[^>]*>', "", s)
    s = re.sub(r'<div class="section-cta">', '<div class="cta-actions">', s)
    # a second CTA block sits further down the page in the same legacy
    # wrapper; v2 styles .cta-actions, nothing styles .ef-hero-ctas now
    s = re.sub(r'<div class="ef-hero-ctas"[^>]*>', '<div class="cta-actions">', s)
    s = re.sub(r'class="btn-primary"', 'class="btn btn-primary"', s)
    s = re.sub(r'class="ef-phone-cta"[^>]*', 'class="btn btn-secondary"', s)
    # The bar is a single flat div holding two anchors. Matching it with
    # `.*?</div>\s*</div>` looked safe and was not: the bar has no nested div,
    # so the pattern ran past it and swallowed everything up to the next
    # doubled close - which sat beyond the footer, deleting it. Close it on
    # its own tag instead.
    s = re.sub(r'<div class="mobile-cta-bar">(?:(?!</div>).)*?</div>\s*', "", s,
               flags=re.S)

    # relevant-post-card -> the v2 card
    s = s.replace('<article class="relevant-post-card">',
                  '<article class="card" data-tone="blue">')
    s = re.sub(r'<div class="relevant-posts-grid"[^>]*>',
               '<div class="cards cards-left">', s)

    # about-section -> section / group / prose, alternating tone
    idx = [0]

    def band(mm):
        idx[0] += 1
        alt = " section-alt" if idx[0] % 2 == 0 else ""
        return ('<section class="section%s">\n<div class="container">\n'
                '<div class="group">\n<div class="prose">' % alt)

    # Close only the sections this pass opened. Rewriting every </section> in
    # the document also rewrote the header's and the footer's, which deleted
    # the footer outright the first time this ran - and check-page.py still
    # reported the page conformant, because a missing footer is only a warning.
    OPEN = re.compile(r'<section class="about-section(?:[^"]*)">')
    out, pos = [], 0
    for mm in OPEN.finditer(s):
        if mm.start() < pos:
            continue
        end = s.find("</section>", mm.end())
        if end < 0:
            continue
        out.append(s[pos:mm.start()])
        out.append(band(mm))
        out.append(s[mm.end():end])
        out.append("</div>\n</div>\n</div>\n</section>")
        pos = end + len("</section>")
    out.append(s[pos:])
    s = "".join(out)

    print("  %-46s hero+body+sheets" % rel)
    if apply_changes:
        io.open(path, "w", encoding="utf-8", newline="").write(s)
    return True


def main(argv):
    ap = "--apply" in argv
    names = [a for a in argv if a.endswith(".html")]
    n = sum(convert(os.path.join(ROOT, x), ap) for x in names)
    print("\n  %d page(s)%s" % (n, "  applied" if ap else "  dry run"))


if __name__ == "__main__":
    main(sys.argv[1:])
