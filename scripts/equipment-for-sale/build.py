#!/usr/bin/env python3
"""
Equipment-for-Sale category page generator.

One template renders every /equipment-for-sale/<slug>/ page from a JSON data
file. Run from the repo root:

    python3 scripts/equipment-for-sale/build.py              # all categories
    python3 scripts/equipment-for-sale/build.py vacuum-trucks

Layout (per the catalog redesign):
  1. dealer strip          2. balanced hero (photo + equal-height finance card)
  3. model cards           4. navy finance band
  5. preserved SEO prose   (verbatim -- never rewritten here)

SEO GUARDRAIL: title, meta description, canonical, og:*, the JSON-LD blocks and
the prose sections are read VERBATIM from the sidecar files named in the data
file (`meta_file` / `schema_file` / `seo_sections_file`). This generator is a
re-layout. It must never author or mutate that content.

No dependencies -- stdlib only, matching the rest of scripts/.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
HERE = os.path.join(ROOT, "scripts", "equipment-for-sale")
DATA = os.path.join(HERE, "data")
OUT = os.path.join(ROOT, "equipment-for-sale")

# Show cards for the headline build types; anything deeper also gets the full
# spec table so a 15-model lineup stays comparable at a glance.
TABLE_THRESHOLD = 6


# --------------------------------------------------------------------------
# Component CSS lives in axiant-v2.css, not here.
#
# It used to be a 16KB <style> block emitted into all 17 generated pages,
# carrying 10 locally-defined tokens, 14 hardcoded colours, 15 !important
# and a third breakpoint. That is exactly the drift the design-system
# contract forbids, and check-page.py failed every page it produced.
#
# The translation was value-identical: the block resolved its colours
# through --accent-color, --text-primary, --bg-card and --border-color,
# which axiant-v2.css already defines as aliases of the real tokens.
# Edit the "EQUIPMENT FOR SALE" section of axiant-v2.css instead.


# --------------------------------------------------------------------------
def read(path):
    return io.open(path, encoding="utf-8").read().strip()


def dealer_strip(d):
    return (
        '<div class="efs-dealer">'
        f'<img class="efs-dlogo" src="{d["logo"]}" width="{d.get("logo_w",158)}" '
        f'height="{d.get("logo_h",52)}" alt="{d["name"]}">'
        f'<div class="efs-dtext"><div class="efs-dname">{d["name"]}</div>'
        f'<div class="efs-dblurb">{d["blurb"]}</div></div>'
        # the icon lives in the data - some dealers use a phone glyph,
        # others an envelope for "Request a quote" - so the template must
        # not prepend one. It used to, which rendered every chip twice.
        f'<div class="efs-dc"><a class="efs-dbtn" href="{d["phone_href"]}">{d["phone"]}</a>'
        f'<a class="efs-dbtn" href="{d["website_href"]}" target="_blank" rel="noopener">'
        f'{d["website"]}</a></div></div>'
    )


def hero(h, fc):
    checks = "".join(f"<li>{c}</li>" for c in fc["checks"])
    return (
        f'<div class="efs-eyebrow">{h["eyebrow"]}</div>'
        f'<h1>{h["h1"]}</h1>'
        f'<p class="efs-intro">{h["intro_html"]} '
        f'<a class="efs-introlink" href="{h["intro_link"]["href"]}">{h["intro_link"]["label"]}</a></p>'
        '<div class="efs-herorow">'
        f'<figure class="efs-photo"><img src="{h["image"]}" width="1200" height="800" '
        f'alt="{h["image_alt"]}"><figcaption class="cap">{h["image_caption"]}</figcaption></figure>'
        '<aside class="efs-fcard">'
        f'<div class="fe">{fc["eyebrow"]}</div><h2 class="serif">{fc["title"]}</h2>'
        f'<p>{fc["body"]}</p>'
        + (estimator(fc["estimator"]) if fc.get("estimator") else "")
        + f'<a class="efs-cta" id="efsCta" href="{fc["cta"]["href"]}">{fc["cta"]["label"]}</a>'
        + ("<div class=\"efs-rr\">Checking options won&rsquo;t affect your credit &middot; 24&ndash;48 hr "
           "decisions &middot; no obligation</div>" if fc.get("estimator") else "")
        + f'<a class="efs-cta2" href="{fc["cta2"]["href"]}" target="_blank" rel="noopener">'
          f'{fc["cta2"]["label"]}</a>'
        f'<ul class="efs-checks">{checks}</ul>'
        "</aside></div>"
    )


def finance_href(model, hero_data):
    """Internal financing funnel. match.html reads ?type / ?amount / ?equipment via
    URLSearchParams and prefills loanType + equipmentDescription -- so tagging the
    model name here is what attributes the lead to the exact machine."""
    if model.get("finance_href"):
        return model["finance_href"]
    name = re.sub(r"<[^>]+>", "", model["name"])
    q = (name.replace("&amp;", "&").replace("&middot;", "-")
             .replace("&", "%26").replace(" ", "%20").replace("/", "%2F"))
    return f"/match.html?type=equipment&amp;equipment={q}"


def model_cards(models, hero_data, sec):
    cards = []
    for m in models:
        # TODO(data): per-model photos do not exist for most categories yet.
        # Falls back to the category hero image until the dealer supplies one.
        img = m.get("image") or hero_data["image"]
        alt = m.get("image_alt") or hero_data["image_alt"]
        chips = "".join(f'<span class="efs-chip">{c}</span>' for c in m.get("chips", []))
        cards.append(
            '<article class="efs-card">'
            f'<div class="efs-cimg"><img src="{img}" width="720" height="480" alt="{alt}" loading="lazy">'
            f'<span class="efs-cap">{m["capacity"]}</span></div>'
            f'<div class="efs-cbody"><h3 class="efs-ct">{m["name"]}</h3>'
            f'<div class="efs-chips">{chips}</div>'
            '<div class="efs-cbtns">'
            f'<a class="efs-cb1" href="{m["inventory_url"]}" target="_blank" rel="noopener">'
            "View inventory &#8599;</a>"
            f'<a class="efs-cb2" href="{finance_href(m, hero_data)}">Estimate financing</a>'
            "</div></div></article>"
        )
    return (
        f'<section class="efs-sec"><h2 class="efs-sh">{sec["heading"]}</h2>'
        f'<p class="efs-ss">{sec["subhead"]}</p>'
        f'<div class="efs-cards">{"".join(cards)}</div>'
    )


def full_table(models, hero_data, sec):
    """Deep lineups keep the comparable spec table so 15 machines stay scannable."""
    rows = "".join(
        f'<tr><td class="mdl">{m["name"]}</td><td class="cap">{m["capacity"]}</td>'
        f'<td>{m.get("spec","")}</td>'
        f'<td class="lk"><a href="{m["inventory_url"]}" target="_blank" rel="noopener">View &#8599;</a> '
        f'&middot; <a href="{finance_href(m, hero_data)}">Finance</a></td></tr>'
        for m in models
    )
    return (
        f'<details class="efs-full"><summary>{sec.get("table_heading","Full lineup &amp; specs")} '
        f'({len(models)} models)</summary><div class="efs-tblwrap"><table class="efs-tbl">'
        "<thead><tr><th>Model</th><th>Capacity</th><th>Configuration</th>"
        '<th style="text-align:right">Links</th></tr></thead>'
        f"<tbody>{rows}</tbody></table></div></details>"
    )


def estimator(est):
    """Inline payment estimator. Carried over verbatim in behaviour from the pages
    that already shipped one (REW + SENNEBOGEN) -- re-laying out a page must not
    delete a working conversion tool. No default price is seeded: these dealers
    quote rather than publish, so the buyer enters the figure they were quoted and
    the output stays "--" until they do."""
    return (
        '<div class="efs-est">'
        '<label for="efsPrice">Estimate your monthly payment</label>'
        '<div class="efs-est-in">$<input type="text" inputmode="numeric" id="efsPrice" '
        f'placeholder="{est.get("placeholder","Price you were quoted")}" aria-label="Equipment price"></div>'
        '<div class="efs-est-row">'
        '<label for="efsDown">Down payment<select id="efsDown">'
        '<option value="0">0%</option><option value="10" selected>10%</option>'
        '<option value="20">20%</option><option value="30">30%</option></select></label>'
        '<label for="efsTerm">Term<select id="efsTerm">'
        '<option value="36">36 mo</option><option value="48">48 mo</option>'
        '<option value="60" selected>60 mo</option><option value="72">72 mo</option>'
        '</select></label></div>'
        '<div class="efs-est-out">&asymp; <b id="efsMo">&mdash;</b> / month</div>'
        f'<div class="efs-est-note">{est.get("note","Illustrative only, at ~9% APR. Your actual rate and term are set on approval.")}</div>'
        '</div>'
    )


def estimator_js(equip_q):
    return (
        "<script>(function(){var p=document.getElementById('efsPrice'),d=document.getElementById('efsDown'),"
        "t=document.getElementById('efsTerm'),mo=document.getElementById('efsMo'),c=document.getElementById('efsCta');"
        "if(!p||!c)return;var EQ='%s',DEF=c.textContent;"
        "function n(v){v=String(v||'').replace(/[^0-9.]/g,'');return v?parseFloat(v):0;}"
        "function f(x){return '$'+Math.round(x).toLocaleString('en-US');}"
        "function pay(P,apr,m){var r=apr/12;return r>0?(P*r)/(1-Math.pow(1+r,-m)):P/m;}"
        "function calc(){var price=n(p.value);"
        "if(!(price>0)){mo.innerHTML='\u2014';c.href='/match.html?type=equipment&equipment='+EQ;c.textContent=DEF;return;}"
        "var loan=price*(1-parseFloat(d.value)/100),m=parseInt(t.value,10);"
        "mo.textContent=f(pay(loan,0.09,m));"
        "c.href='/match.html?type=equipment&amount='+Math.round(loan)+'&equipment='+EQ;"
        "c.textContent='See if you qualify for '+f(loan)+' \u2192';}"
        "p.addEventListener('input',calc);"
        "p.addEventListener('blur',function(){var v=n(p.value);if(v>0)p.value=Math.round(v).toLocaleString('en-US');});"
        "d.addEventListener('change',calc);t.addEventListener('change',calc);calc();})();</script>"
        % equip_q
    )


def related_row(rel, heading):
    """Sibling / dealer cross-links. KEEP THIS: on the Mix Right pages this grid is
    the only internal cross-linking between sibling categories, so dropping it would
    lose internal links. Entries that merely duplicate a model card are filtered out
    by the extractor."""
    if not rel:
        return ""
    cards = "".join(
        f'<a class="efs-relcard" href="{r["href"]}"'
        + ("" if r["href"].startswith("/") else ' target="_blank" rel="noopener"')
        + f'><div class="ri"><img src="{r["image"]}" width="720" height="480" '
          f'alt="{r["alt"]}" loading="lazy"></div><div class="rn">{r["name"]}</div></a>'
        for r in rel
    )
    return (f'<section class="efs-sec"><h2 class="efs-sh" style="font-size:1.2rem">{heading}</h2>'
            f'<div class="efs-rel">{cards}</div></section>')


def band(b):
    props = "".join(f"<li>{p}</li>" for p in b["proofs"])
    phone = (f'<a class="efs-bandphone" href="{b["phone"]["href"]}">{b["phone"]["label"]}</a>'
             if b.get("phone") else "")
    return (
        '<section class="efs-band"><div class="bl">'
        f'<h2 class="serif">{b["title"]}</h2><p>{b["body"]}</p>'
        f'<ul class="efs-props">{props}</ul></div>'
        f'<div class="efs-bandcta"><a href="{b["cta"]["href"]}">{b["cta"]["label"]}</a>{phone}</div>'
        "</section>"
    )


def render(slug):
    cfg = json.loads(read(os.path.join(DATA, f"{slug}.json")))
    chrome = read(os.path.join(HERE, "_chrome.html"))

    meta = read(os.path.join(DATA, cfg["meta_file"]))
    schema = read(os.path.join(DATA, cfg["schema_file"]))
    seo = read(os.path.join(DATA, cfg["seo_sections_file"]))

    h, fc, sec = cfg["hero"], cfg["finance_card"], cfg["models_section"]
    models = cfg["models"]

    crumb = (
        '<header class="efs-crumbhead"><nav class="efs-crumb" aria-label="Breadcrumb">'
        '<a href="/">Home</a> &rsaquo; <a href="/equipment-for-sale/">Equipment for Sale</a> '
        f'&rsaquo; <b>{cfg["breadcrumb_label"]}</b></nav></header>'
    )

    body = [
        '<div class="efs"><div class="efs-wrap">',
        dealer_strip(cfg["dealer"]),
        hero(h, fc),
        model_cards(models, h, sec),
    ]
    if len(models) > TABLE_THRESHOLD:
        body.append(full_table(models, h, sec))
    body += [
        f'<a class="efs-viewall" href="{sec["view_all"]["href"]}" target="_blank" rel="noopener">'
        f'{sec["view_all"]["label"]}</a>',
        f'<p class="efs-note">{cfg["dealer"]["disclosure"]}</p>',
        "</section>",
        related_row(cfg.get("related", []), cfg.get("related_heading", "Related equipment")),
        band(cfg["band"]),
        f'<div class="efs-seo">{seo}</div>' if seo else "",
        "</div></div>",
    ]
    if fc.get("estimator"):
        body.append(estimator_js(fc["estimator"]["equip"]))

    page = (chrome
            .replace("{{META}}", meta)
            .replace("{{SCHEMA}}", schema)
            .replace("{{BREADCRUMB}}", crumb)
            .replace("{{BODY}}", "".join(body)))

    out_dir = os.path.join(OUT, slug)
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "index.html")
    io.open(dest, "w", encoding="utf-8", newline="\n").write(page)

    no_img = [m["name"] for m in models if not m.get("image")]
    print(f"  {slug}: {len(models)} models, "
          f"{'cards + full table' if len(models) > TABLE_THRESHOLD else 'cards'}"
          + (f"  TODO images: {', '.join(no_img)}" if no_img else "  (all models have photos)"))
    return dest



def render_hub():
    """The /equipment-for-sale/ hub.

    Card photos, dealer badges and model counts are DERIVED from the 16 category
    data files, so adding a category keeps the hub in sync automatically. Only the
    industry grouping and the per-card copy live in _hub.json -- both lifted
    verbatim from the previous hub. Meta + JSON-LD come from the sidecars.
    """
    cfg = json.loads(read(os.path.join(DATA, "_hub.json")))
    chrome = read(os.path.join(HERE, "_chrome.html"))
    meta = read(os.path.join(DATA, cfg["meta_file"]))
    schema = read(os.path.join(DATA, cfg["schema_file"]))

    cats = {}
    for f in os.listdir(DATA):
        if f.endswith(".json") and not f.startswith("_"):
            c = json.loads(read(os.path.join(DATA, f)))
            cats[c["slug"]] = c

    h = cfg["hero"]
    hero = (
        '<header class="efs-hero"><div class="efs-hero-in">'
        f'<div class="eb">{h["eyebrow"]}</div><h1>{h["h1"]}</h1><p>{h["intro_html"]}</p>'
        + ('<ul class="efs-hstats">' + "".join(f"<li>{x}</li>" for x in h["stats"]) + "</ul>")
        + "</div></header>"
    )

    chips = ('<div class="efs-jump"><span class="lbl">' + cfg["chips_label"] + "</span>"
             + "".join(f'<a class="mx-chip efs-dbtn" href="#{g["anchor"]}">{g["chip"]}</a>'
                       for g in cfg["groups"]) + "</div>")

    groups = []
    for g in cfg["groups"]:
        cards = []
        for it in g["items"]:
            c = cats[it["slug"]]
            cards.append(
                f'<a class="efs-catcard" href="/equipment-for-sale/{it["slug"]}/">'
                f'<div class="efs-catphoto"><img src="{c["hero"]["image"]}" width="1200" height="800" '
                f'alt="{c["hero"]["image_alt"]}" loading="lazy">'
                f'<span class="efs-catbadge"><img src="{c["dealer"]["logo"]}" width="72" height="24" '
                f'alt="{c["dealer"]["name"]}"></span></div>'
                f'<div class="efs-catbody"><div class="efs-catseries">{it["series"]}</div>'
                f'<div class="efs-catname">{it["name"]}</div>'
                f'<div class="efs-cattag">{it["tag"]}</div>'
                f'<div class="efs-catmore"><span>{it["count"]}</span>'
                "<span>View &amp; finance &rarr;</span></div></div></a>"
            )
        groups.append(
            f'<div class="efs-grouphead" id="{g["anchor"]}"><div class="pe">{g["eyebrow"]}</div>'
            f'<h2>{g["heading"]}</h2></div>'
            f'<div class="efs-catgrid">{"".join(cards)}</div>'
        )

    body = (f'<div class="efs">{hero}<div class="efs-wrap" style="padding-top:34px">'
            + chips + "".join(groups)
            + band(cfg["band"])
            + f'<p class="efs-note">{cfg["fine"]}</p>'
            + "</div></div>")

    page = (chrome.replace("{{META}}", meta).replace("{{SCHEMA}}", schema)
            .replace("{{BREADCRUMB}}", "").replace("{{BODY}}", body))
    dest = os.path.join(OUT, "index.html")
    io.open(dest, "w", encoding="utf-8", newline="\n").write(page)
    n = sum(len(g["items"]) for g in cfg["groups"])
    print(f"  hub: {len(cfg['groups'])} industries, {n} category cards")


if __name__ == "__main__":
    slugs = sys.argv[1:] or [
        f[:-5] for f in sorted(os.listdir(DATA))
        if f.endswith(".json") and not f.startswith("_")
    ]
    print(f"Building {len(slugs)} category page(s) + the hub:")
    for s in slugs:
        render(s)
    render_hub()
    print("Done.")
