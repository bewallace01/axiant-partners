#!/usr/bin/env python3
"""
One-time migrator: read an existing /equipment-for-sale/<slug>/ page (the old
inlined `.mx` layout) and split it into the template's data file + the verbatim
SEO sidecars.

    python3 scripts/equipment-for-sale/extract.py <slug> [<slug> ...]
    python3 scripts/equipment-for-sale/build.py <slug>

What it does NOT do: author content. Meta, JSON-LD and the prose sections are
copied byte-for-byte into `_<slug>.{meta,schema,seo}.html`. Everything else it
pulls out of the existing markup (dealer, hero, finance card, model rows, related
grid, closer) so the redesign is a pure re-layout.

Keep this script after the migration -- it documents where every field came from.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "scripts", "equipment-for-sale", "data")

# Section headings that are LAYOUT, not SEO prose. Everything else is preserved.
LAYOUT_H2 = re.compile(
    r"^(finance any|.*\bmodels$|more .* equipment|flagship .*|ready to |"
    r".*\binventory$|electric & hybrid power options|albach diamant 2000 specifications)",
    re.I,
)


def txt(x):
    return re.sub(r"<[^>]+>", "", x or "").strip()


def sec_of(html, h2_pat):
    m = re.search(r"<section[^>]*>(?:(?!<section).)*?" + h2_pat + r".*?</section>", html, re.S | re.I)
    return m.group(0) if m else ""


def equip_q(name):
    n = txt(name).replace("&amp;", "&")
    return (n.replace("&", "%26").replace(" ", "%20").replace("/", "%2F"))


def extract(slug):
    src = os.path.join(ROOT, "equipment-for-sale", slug, "index.html")
    h = io.open(src, encoding="utf-8").read()

    # ---------------- verbatim SEO sidecars (never authored here) -------------
    meta = h[h.index('<meta name="description"'):h.index("</title>") + len("</title>")]
    schema = "\n    ".join(re.findall(r'<script type="application/ld\+json">.*?</script>', h, re.S))

    body = h[h.index('<div class="mx-wrap-fam">'):]
    prose = []
    for s in re.findall(r"<section[^>]*>(?:(?!<section).)*?</section>", body, re.S):
        m = re.search(r"<h2[^>]*>(.*?)</h2>", s, re.S)
        if not m:
            continue
        # STRUCTURAL check first: a section holding the card grid is layout, not
        # prose -- it becomes the related row. Heading text alone is too fragile
        # (drilling-rigs calls its grid "Service King drilling rigs", which reads
        # exactly like a prose heading, and it ended up rendered twice).
        if "mx-related" in s or "mx-modtbl" in s:
            continue
        if not LAYOUT_H2.match(txt(m.group(1))):
            prose.append(s)

    # ---------------- dealer strip -------------------------------------------
    # NB: anchor on mx-dtitle. A non-greedy `.*?</div></div>` stops at the end of
    # the inner .mx-bmain block and silently drops the phone/website chips.
    brand = re.search(r'<div class="mx-brand">.*?(?=<div class="mx-dtitle">)', body, re.S).group(0)
    logo = re.search(r'class="mx-blogo" src="([^"]+)"', brand).group(1)
    dname = re.search(r"<b>(.*?)</b>", brand, re.S).group(1)
    dblurb = re.search(r"<span>(.*?)</span>", brand, re.S).group(1)
    chips = re.findall(r'<a class="mx-chip" href="([^"]+)"[^>]*>(.*?)</a>', brand, re.S)
    phone = next((c for c in chips if c[0].startswith("tel:")), ("", ""))
    web = next((c for c in chips if c[0].startswith("http")), ("", ""))

    # ---------------- hero ----------------------------------------------------
    eyebrow = txt(re.search(r'<div class="mx-dcat">(.*?)</div>', body, re.S).group(1))
    h1 = re.search(r"<h1>(.*?)</h1>", body, re.S).group(1)
    intro_m = re.search(r'<p class="mx-intro"[^>]*>(.*?)</p>', body, re.S)
    intro = intro_m.group(1)
    link_m = re.search(r'<a href="([^"]+)"[^>]*>([^<]*&rarr;)</a>\s*$', intro.strip())
    intro_link = {"href": link_m.group(1), "label": link_m.group(2)} if link_m else None
    if link_m:
        intro = intro[:link_m.start()].strip()
    hero_img = re.search(r'<div class="mx-photo-lg"><img src="([^"]+)"[^>]*alt="([^"]*)"', body, re.S)

    # ---------------- finance card -------------------------------------------
    fin = re.search(r'<aside class="mx-finbox">.*?</aside>', body, re.S).group(0)
    ctas = re.findall(r'<a href="([^"]+)"[^>]*class="mx-cta2?"[^>]*>(.*?)</a>', fin, re.S)
    if not ctas:
        ctas = re.findall(r'<a[^>]*class="mx-cta2?"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', fin, re.S)
    checks = [c for c in re.findall(r"<li>(.*?)</li>", fin, re.S)]
    # The old REW widget was fixed at 10% down / 60 months and its note said so.
    # The template's estimator makes both selectable, so carrying that note over
    # would contradict the controls sitting right above it. Use the template's
    # default note instead.
    has_est = bool(re.search(r'id="(sbPrice|rewPrice)"', fin))

    # ---------------- models (the spec table) --------------------------------
    models = []
    tbody = re.search(r"<tbody>(.*?)</tbody>", body, re.S)
    for tr in re.findall(r"<tr>(.*?)</tr>", tbody.group(1), re.S) if tbody else []:
        tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        if len(tds) < 3:
            continue
        link = re.search(r'href="([^"]+)"', tds[-1])
        models.append({
            "name": tds[0].strip(),
            "capacity": tds[1].strip(),
            "chips": [c.strip() for c in re.split(r"&middot;", txt(tds[2])) if c.strip()][:3],
            "spec": tds[2].strip(),
            # TODO(data): per-model photos mostly do not exist. null -> falls back
            # to the category hero image (build.py prints these).
            "image": None,
            "image_alt": None,
            "inventory_url": link.group(1) if link else "",
        })

    # ---------------- related grid (KEEP: holds the sibling internal links) ---
    rel, rel_heading = [], "Related equipment"
    rm = re.search(r'<section[^>]*>\s*<h2[^>]*>(.*?)</h2>\s*<div class="mx-related">(.*?)</div></section>',
                   body, re.S)
    model_urls = {m["inventory_url"] for m in models}
    if rm:
        rel_heading = rm.group(1)
        for card in re.findall(r'<a class="mx-fcard" href="([^"]+)".*?<img src="([^"]+)" alt="([^"]*)".*?'
                               r'class="mx-fname"[^>]*>(.*?)</div>', rm.group(2), re.S):
            href, img, alt, name = card
            # drop entries that merely duplicate a model card / the view-all link
            if href in model_urls:
                continue
            rel.append({"href": href, "image": img, "alt": alt, "name": name.strip()})

    # per-model photo: look for an asset whose FILENAME matches the model name
    # (Service King ships sk-475.jpg, sk-575.jpg ... -> real per-model photos).
    # Mix Right and REW only have one photo per category, so those stay null and
    # fall back to the category hero -- that's the outstanding TODO.
    asset_dir = os.path.dirname(logo.lstrip("/"))
    for m in models:
        stem = re.sub(r"[^a-z0-9]+", "-", txt(m["name"]).lower()).strip("-")
        for ext in (".jpg", ".webp", ".png", ".jpeg"):
            cand = os.path.join(ROOT, asset_dir, stem + ext)
            if os.path.exists(cand):
                m["image"] = "/" + os.path.join(asset_dir, stem + ext).replace(os.sep, "/")
                m["image_alt"] = f"{dname} {txt(m['name'])}"
                break

    # ---------------- closer -> finance band ---------------------------------
    # Reuse the page's OWN copy. Where a closer exists, lift it; otherwise fall
    # back to the finance card's existing wording. Nothing is invented here.
    closer = sec_of(body, r'<h2[^>]*>Ready to')
    fin_h2 = txt(re.search(r"<h2[^>]*>(.*?)</h2>", fin, re.S).group(1))
    fin_p = re.search(r"<p>(.*?)</p>", fin, re.S).group(1)
    if closer:
        b_title = re.search(r"<h2[^>]*>(.*?)</h2>", closer, re.S).group(1)
        b_body = re.search(r'<p class="mx-intro"[^>]*>(.*?)</p>', closer, re.S).group(1)
    else:
        b_title, b_body = fin_h2, fin_p

    apply_href = f"/match.html?type=equipment&amp;equipment={equip_q(h1)}"
    data = {
        "slug": slug,
        "breadcrumb_label": h1,
        "_seo_note": "meta / schema / prose are preserved VERBATIM in the _*.html sidecars. "
                     "This is a re-layout -- do not rewrite them here.",
        "meta_file": f"_{slug}.meta.html",
        "schema_file": f"_{slug}.schema.html",
        "seo_sections_file": f"_{slug}.seo.html",
        "dealer": {
            "name": dname, "logo": logo, "logo_w": 158, "logo_h": 52, "blurb": dblurb,
            "phone": txt(phone[1]).replace("☎", "").strip(), "phone_href": phone[0],
            "website": txt(web[1]).replace("\U0001f310", "").strip(), "website_href": web[0],
            "inventory_url": web[0],
            "disclosure": re.search(r'<div class="mx-fine">(.*?)</div>', body, re.S).group(1).strip(),
        },
        "hero": {
            "eyebrow": eyebrow, "h1": h1, "intro_html": intro.strip(),
            "intro_link": intro_link or {"href": "/equipment-financing.html",
                                         "label": "How financing works &rarr;"},
            "image": hero_img.group(1), "image_alt": hero_img.group(2),
            "image_caption": f"{dname} &mdash; {txt(h1)}",
        },
        "finance_card": {
            "eyebrow": "Finance with Axiant",
            "title": fin_h2,
            "body": fin_p.strip(),
            "cta": {"label": txt(ctas[0][1]) if ctas else "Get pre-approved", "href": ctas[0][0] if ctas else apply_href},
            "cta2": {"label": ctas[1][1].strip() if len(ctas) > 1 else "View inventory &#8599;",
                     "href": ctas[1][0] if len(ctas) > 1 else web[0]},
            "checks": checks,
        },
        "models_section": {
            "heading": txt(re.search(r'<h2 class="mx-sec-h serif">(.*?)</h2>', body, re.S).group(1)),
            "subhead": f"All financeable through Axiant. Live inventory &amp; pricing on {dname}.",
            "view_all": {"label": txt(re.search(r'<a class="mx-catlink" href="[^"]+"[^>]*>(.*?)</a>', body, re.S).group(1))
                         if re.search(r'mx-catlink', body) else f"View {dname}&rsquo;s full range &#8599;",
                         "href": re.search(r'<a class="mx-catlink" href="([^"]+)"', body).group(1)
                         if re.search(r'mx-catlink', body) else web[0]},
            "table_heading": "Full lineup &amp; specs",
        },
        "models": models,
        "related": rel,
        "related_heading": rel_heading,
        "band": {
            "title": b_title, "body": b_body,
            "proofs": ["24-hour approvals", "New &amp; used", "Asset-based &mdash; the equipment carries the deal"],
            "cta": {"label": "Get pre-approved &rarr;", "href": apply_href},
            "phone": {"label": "Call (561) 268-0465", "href": "tel:+15612680465"},
        },
    }
    if has_est:
        data["finance_card"]["estimator"] = {"equip": equip_q(h1)}

    io.open(os.path.join(DATA, f"_{slug}.meta.html"), "w", encoding="utf-8", newline="\n").write(meta)
    io.open(os.path.join(DATA, f"_{slug}.schema.html"), "w", encoding="utf-8", newline="\n").write(schema)
    io.open(os.path.join(DATA, f"_{slug}.seo.html"), "w", encoding="utf-8", newline="\n").write("\n".join(prose))
    io.open(os.path.join(DATA, f"{slug}.json"), "w", encoding="utf-8", newline="\n").write(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n")

    print(f"  {slug}: {len(models)} models, {len(prose)} prose sections, {len(rel)} related, "
          f"{'estimator' if has_est else 'no estimator'}, "
          f"{sum(1 for m in models if m['image'])}/{len(models)} model photos")


if __name__ == "__main__":
    for s in sys.argv[1:]:
        extract(s)
