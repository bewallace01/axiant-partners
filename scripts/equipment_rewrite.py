#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rewrite the content of an /equipment/<type>/ page in place from a data module.

    python scripts/equipment_rewrite.py equip_wheel_loaders            # dry run, prints word count
    python scripts/equipment_rewrite.py equip_wheel_loaders --apply

Daily page batch 2026-11-14. The /equipment/ pages share one old template whose
sections (why finance, what is it, why it is different, options, cost, rates,
requirements, what to have ready, when to apply, tips, mistakes, process) read
the same on every page and push sibling pages over 40% shared text (simscan).
This keeps the page chrome exactly as it is (head tags and tracking, header,
hero image, the Related cards, In-Depth guides, More Resources tiles, the final
CTA and footer) and replaces everything else with the module's own sections,
in the shape of the rewritten /equipment/cnc-machines/ page (Nov 13): dateline,
Quick Answer, At a Glance, page-specific sections, FAQ matching FAQPage JSON-LD,
Sources.

A module scripts/equip_<name>.py exports PAGE with: path, date, date_text, title,
og_title, desc, h1, lede, checks (4), intro, quick_answer, qa_link, glance
(6 x (key, label)), sections ([(h2, html, cta_or_None)]), faqs ([(q, a)]),
sources ([(url, name, note)]), headline, article_desc, glance_h2, faq_h2;
optional drop: h2 prefixes of kept sections to remove (e.g. a stale In-Depth list).
"""
import html, importlib, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

KEEP = ("Related ", "In-Depth ", "More ", "Ready ")
TONES = ["teal", "indigo", "bronze", "rust", "blue"]


def pmt(principal, apr_pct, months):
    """Level monthly payment, computed by formula so page tables never carry hand math."""
    r = apr_pct / 100 / 12
    return principal / months if r == 0 else principal * r / (1 - (1 + r) ** -months)


def usd(x):
    return f"${x:,.0f}"


def pay_row(principal, apr_pct, months):
    m = pmt(principal, apr_pct, months)
    return [usd(principal), f"{months} months", usd(m), usd(m * months - principal)]


def table(heads, rows):
    head = "".join(f"<th>{h}</th>" for h in heads)
    body = "".join("<tr>" + "".join(f'<td data-label="{h}">{c}</td>' for h, c in zip(heads, r)) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table>\n<thead>\n<tr>{head}</tr>\n</thead>\n<tbody>\n{body}\n</tbody>\n</table></div>'


def slug(s):
    s = html.unescape(re.sub(r"<[^>]+>", "", s)).lower().replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def attr(s):
    return s.replace('"', "&quot;")


def text(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def section(h2, inner, tone, cta=None):
    c = (f'<p class="cta-actions cta-actions-left"><a class="btn btn-primary" href="/match.html">{cta}</a></p>\n'
         if cta else "")
    return (f'<section class="section">\n<div class="container">\n<div class="group" data-tone="{tone}">\n'
            f'<div class="group-head"><h2 id="{slug(h2)}">{h2}</h2></div>\n{inner}\n{c}</div>\n</div>\n</section>')


def render(p, src):
    h = src
    # ---- head
    h = re.sub(r"<title>.*?</title>", f"<title>{p['title']}</title>", h, count=1, flags=re.S)
    for name in ("description", "twitter:description"):
        h = re.sub(rf'<meta content="[^"]*" name="{name}"', f'<meta content="{attr(p["desc"])}" name="{name}"', h)
    h = re.sub(r'<meta content="[^"]*" property="og:description"',
               f'<meta content="{attr(p["desc"])}" property="og:description"', h)
    h = re.sub(r'<meta content="[^"]*" property="og:title"', f'<meta content="{attr(p["og_title"])}" property="og:title"', h)
    h = re.sub(r'<meta content="[^"]*" name="twitter:title"', f'<meta content="{attr(p["og_title"])}" name="twitter:title"', h)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": text(q), "acceptedAnswer": {"@type": "Answer", "text": text(a)}}
        for q, a in p["faqs"]]}
    h, n = re.subn(r'(<script type="application/ld\+json">\s*)\{"@context": ?"https://schema.org", ?"@type": ?"FAQPage".*?(\s*</script>)',
                   lambda m: m.group(1) + json.dumps(faq_ld, ensure_ascii=False) + m.group(2), h, count=1, flags=re.S)
    assert n == 1, "FAQPage JSON-LD not found"

    def art(m):
        d = json.loads(m.group(2))
        d["headline"], d["description"], d["dateModified"] = text(p["headline"]), text(p["article_desc"]), p["date"]
        return m.group(1) + json.dumps(d, ensure_ascii=False) + m.group(3)
    h, n = re.subn(r'(<script type="application/ld\+json">\s*)(\{"@context": ?"https://schema.org", ?"@type": ?"Article".*?\})(\s*</script>)',
                   art, h, count=1, flags=re.S)
    assert n == 1, "Article JSON-LD not found"

    # ---- body
    pre, rest = h.split("<!-- AXIANT-HEADER:END -->", 1)
    body, post = rest.split("<!-- AXIANT-FOOTER:START", 1)
    hero = re.search(r'<section class="hero-compact">.*?</section>', body, re.S).group(0)
    hero2 = re.sub(r"<h1>.*?</h1>", f"<h1>{p['h1']}</h1>", hero, count=1, flags=re.S)
    hero2 = re.sub(r'<p class="lede">.*?</p>', f'<p class="lede">{p["lede"]}</p>', hero2, count=1, flags=re.S)
    checks = "\n".join(f'<li><span class="tick">✓</span><span>{c}</span></li>' for c in p["checks"])
    hero2 = re.sub(r'<ul class="hero-checks">.*?</ul>', f'<ul class="hero-checks">\n{checks}\n</ul>', hero2, count=1, flags=re.S)

    secs = re.findall(r'<section class="section[^"]*">.*?</section>', body, re.S)

    def h2of(s):
        m = re.search(r"<h2[^>]*>(.*?)</h2>", s, re.S)
        return text(m.group(1)).strip() if m else ""
    glance = next(s for s in secs if h2of(s).endswith("at a Glance"))
    kept = [s for s in secs if h2of(s).startswith(KEEP) and not h2of(s).startswith(tuple(p.get("drop", ())))]
    tail_names = ("More ", "Ready ")
    mid_keep = [s for s in kept if not h2of(s).startswith(tail_names)]
    end_keep = [s for s in kept if h2of(s).startswith(tail_names)]

    keys = iter(p["glance"])
    def stat(m):
        k, l = next(keys)
        return f'<span class="stat-key">{k}</span><span class="stat-label">{l}</span>'
    glance = re.sub(r'<span class="stat-key">.*?</span><span class="stat-label">.*?</span>', stat, glance, flags=re.S)
    glance = re.sub(r"<h2[^>]*>.*?</h2>", f'<h2 id="{slug(p["glance_h2"])}">{p["glance_h2"]}</h2>', glance, count=1, flags=re.S)

    out = []
    out.append('<section class="section section-tight">\n<div class="container">\n<div class="group" data-tone="blue">\n'
               f'<div class="prose">\n<p class="dateline">Updated {p["date_text"]}</p>\n{p["intro"]}\n</div>\n</div>\n</div>\n</section>')
    out.append(section("Quick Answer", '<div class="callout quick-answer">\n<div class="prose">\n'
                       f'<p>{p["quick_answer"]}</p>\n<p><a href="/match.html">{p["qa_link"]} &rarr;</a></p>\n</div>\n</div>', "teal"))
    out.append(glance)
    for i, (h2, inner, cta) in enumerate(p["sections"]):
        out.append(section(h2, inner, TONES[i % len(TONES)], cta))
    out.extend(mid_keep)
    faq = "\n".join(f"<details>\n<summary>{q}</summary>\n<div class=\"answer\"><p>{a}</p></div>\n</details>" for q, a in p["faqs"])
    out.append(section(p["faq_h2"], f'<div class="faq">\n{faq}\n</div>', "bronze"))
    src_li = "\n".join(f'<li><a href="{u}" rel="noopener nofollow" target="_blank">{n}</a> &mdash; {d}</li>' for u, n, d in p["sources"])
    out.append(section("Sources &amp; Further Reading", f'<div class="prose">\n<ul>\n{src_li}\n</ul>\n'
                       "<p>Rates, terms and prices on this page are ranges commonly seen across lenders and dealers, "
                       "not a quote. Confirm current terms with your lender.</p>\n</div>", "blue")
               .replace('id="sources-and-further-reading"', 'id="article-sources-h2"'))
    out.extend(end_keep)

    # alternate backgrounds after the tight dateline block, starting with -alt (as the old pages did)
    fixed = [out[0]]
    for i, s in enumerate(out[1:]):
        cls = "section section-alt" if i % 2 == 0 else "section"
        fixed.append(re.sub(r'^<section class="section[^"]*">', f'<section class="{cls}">', s))
    newbody = "\n" + hero2 + "\n" + "\n".join(fixed) + "\n"
    return pre + "<!-- AXIANT-HEADER:END -->" + newbody + "<!-- AXIANT-FOOTER:START" + post


def words(s):
    b = s.split("<!-- AXIANT-HEADER:END -->")[1].split("<!-- AXIANT-FOOTER:START")[0]
    return len(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>", " ", b, flags=re.S)).split())


if __name__ == "__main__":
    mod = importlib.import_module(sys.argv[1])
    p = mod.PAGE
    path = os.path.join(ROOT, p["path"])
    src = open(path, encoding="utf-8").read()
    out = render(p, src)
    print(f"{p['path']}: {words(src)} -> {words(out)} words")
    if "--apply" in sys.argv:
        open(path, "w", encoding="utf-8").write(out)
        print("written")
