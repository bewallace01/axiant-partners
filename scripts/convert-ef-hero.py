# -*- coding: utf-8 -*-
"""
Convert the last 14 .ef-hero pages onto the v2 .hero-compact template.

828 pages on the site use .hero-compact. 14 still use .ef-hero, a legacy
template that carries its own inline CSS, its own breakpoints and its own
colour rules - and those 14 are exactly the pages that read as a different
site. construction-business-financing.html is the reference; this produces
the same markup.

    .ef-hero                       ->  section.hero-compact
      background:url(...) in CSS   ->    div.hero-media > img
      .ef-hero-copy h1             ->    h1
      .ef-subhead                  ->    p.lede
      .ef-hero-bullets li          ->    ul.hero-checks > li > span.tick
      .ef-hero-ctas                ->    div.actions > a.btn.btn-primary.btn-lg
                                                     + span.call

The eyebrow is taken from the breadcrumb's own section label ("Industries" ->
"Financing program" when the page is a program), so it is not invented.

Run with --apply to write; default is a dry run. Pass page names to limit it.
"""
import html
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HERO = re.compile(r'<section class="ef-hero"[^>]*>(.*?)</section>', re.S)
BG = re.compile(r"\.ef-hero\s*\{[^}]*url\('([^']+)'", re.S)


def build(inner, img, eyebrow):
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", inner, re.S)
    sub = re.search(r'<p class="ef-subhead"[^>]*>(.*?)</p>', inner, re.S)
    bullets = re.findall(r"<li[^>]*>(.*?)</li>", inner, re.S)
    ctas = re.search(r'<div class="ef-hero-ctas"[^>]*>(.*?)</div>', inner, re.S)

    out = ['<section class="hero-compact">']
    if img:
        out.append('<div class="hero-media">\n<img alt="" decoding="async" '
                   'fetchpriority="high" height="1071" src="%s" width="1920"/>\n'
                   "</div>" % img)
    out.append('<div class="container">\n<div class="inner">')
    out.append('<p class="eyebrow">%s</p>' % eyebrow)
    out.append("<h1>%s</h1>" % h1.group(1).strip())
    if sub:
        out.append('<p class="lede">%s</p>' % sub.group(1).strip())
    if bullets:
        out.append('<ul class="hero-checks">')
        for b in bullets:
            t = re.sub(r"^\s*(?:<span[^>]*>)?\s*[✓✔]?\s*", "",
                       b.strip())
            t = re.sub(r"</span>\s*$", "", t).strip()
            out.append('<li><span class="tick">✓</span><span>%s</span></li>'
                       % t)
        out.append("</ul>")
    if ctas:
        body = ctas.group(1)
        links = re.findall(r'<a\s[^>]*href="([^"]+)"[^>]*>(.*?)</a>', body, re.S)
        out.append('<div class="actions">')
        for href, label in links:
            label = re.sub(r"<[^>]+>", "", label).strip()
            if href.startswith("tel:"):
                out.append('<span class="call">Or call <a href="%s">%s</a></span>'
                           % (href, label.replace("Call Now: ", "")))
            else:
                out.append('<a class="btn btn-primary btn-lg" href="%s">%s</a>'
                           % (href, label))
        out.append("</div>")
    out.append("</div>\n</div>\n</section>")
    return "\n".join(out)


def convert(path, apply_changes):
    rel = os.path.relpath(path, ROOT)
    s = io.open(path, encoding="utf-8").read()
    m = HERO.search(s)
    if not m:
        print("  !! %-44s no ef-hero" % rel)
        return False
    bg = BG.search(s)
    img = bg.group(1) if bg else None
    crumb = re.search(r'class="crumbs"[^>]*>.*?<a[^>]*>[^<]*</a>\s*&rsaquo;\s*'
                      r'<a[^>]*>([^<]*)</a>', s, re.S)
    eyebrow = "Financing program"
    if crumb and "industr" in crumb.group(1).lower():
        eyebrow = "Industry financing"
    new = build(m.group(1), img, eyebrow)
    out = s[:m.start()] + new + s[m.end():]
    print("  %-46s img=%s bullets=%d" %
          (rel, (img or "none").split("/")[-1][:28],
           len(re.findall(r"<li", m.group(1)))))
    if apply_changes:
        io.open(path, "w", encoding="utf-8", newline="").write(out)
    return True


def main(argv):
    apply_changes = "--apply" in argv
    names = [a for a in argv if a.endswith(".html")]
    if not names:
        names = [os.path.relpath(p, ROOT) for p in
                 [os.path.join(ROOT, f) for f in os.listdir(ROOT)
                  if f.endswith(".html")]
                 if "ef-hero" in io.open(p, encoding="utf-8",
                                         errors="replace").read()]
    n = sum(convert(os.path.join(ROOT, x), apply_changes) for x in sorted(names))
    print("\n  %d page(s)%s" % (n, "  applied" if apply_changes
                                else "  dry run - pass --apply"))


if __name__ == "__main__":
    main(sys.argv[1:])
