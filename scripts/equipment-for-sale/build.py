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
# Component CSS.
#
# Built on the site's EXISTING theme tokens (critical.css), NOT hardcoded hex.
# The site ships a working dark-mode toggle (`data-theme="dark"`), so baking in
# the light palette would break every category page in dark mode. These vars
# resolve to the light catalog look by default and stay correct in dark.
#   --a  = --accent-color  (#2d7fb8)      --ink  = --text-primary
#   --ad = --accent-dark   (#1e3a5f)      --body = --text-secondary
#   --card/--line from --bg-card/--border-color
# Fonts are the site's real ones: Playfair Display (display) + Inter (body).
# --------------------------------------------------------------------------
CSS = """<style>
  .efs{--a:var(--accent-color);--ad:var(--accent-dark);--ink:var(--text-primary);
    --body:var(--text-secondary);--mut:var(--text-tertiary);--card:var(--bg-card);
    --line:var(--border-color);--green:#2fa36b;--navy:#0d1f3c;
    --sh:0 1px 3px rgba(20,40,80,.05),0 6px 22px -12px rgba(20,40,80,.18);
    font-variant-numeric:tabular-nums}
  html[data-theme="dark"] .efs{--green:#4ade80;
    --sh:0 1px 3px rgba(0,0,0,.4),0 10px 26px -14px rgba(0,0,0,.6)}
  .efs .serif{font-family:'Playfair Display',Georgia,serif}
  .efs-wrap{max-width:1160px;margin:0 auto;padding:22px 20px 44px}

  /* breadcrumb.
     NOTE: this <header> sits OUTSIDE .efs, and the site's global stylesheet
     styles bare `header` as the full-bleed hero (header-overlay background,
     60px padding, centred white text). Without these overrides the breadcrumb
     renders as a giant empty blue band. Deliberately unscoped + !important to
     beat that global rule -- same thing the old .mx-crumbhead rule did. */
  header.efs-crumbhead{background:var(--bg-nav) !important;padding:0 !important;margin:0 !important;
    border-bottom:1px solid var(--border-color);text-align:left !important;color:inherit !important;
    overflow:visible !important;min-height:0 !important}
  .efs-crumb{max-width:1160px;margin:0 auto;padding:13px 20px;font-size:.79rem;
    color:var(--text-tertiary)}
  .efs-crumb a{color:var(--accent-color);text-decoration:none}
  .efs-crumb a:hover{text-decoration:underline}
  .efs-crumb b{color:var(--text-primary);font-weight:600}

  /* 1. dealer strip */
  .efs-dealer{background:var(--card);border:1px solid var(--line);border-radius:13px;
    padding:14px 18px;display:flex;align-items:center;gap:14px;margin:16px 0 24px;box-shadow:var(--sh)}
  .efs-dlogo{height:44px;width:auto;flex:0 0 auto;background:#fff;border-radius:9px;padding:5px}
  .efs-dtext{min-width:0}
  .efs-dname{font-size:.95rem;font-weight:700;color:var(--ink)}
  .efs-dblurb{font-size:.76rem;color:var(--mut);margin-top:2px}
  .efs-dc{margin-left:auto;display:flex;gap:9px;flex-wrap:wrap}
  .efs-dbtn{font-size:.79rem;font-weight:600;border:1px solid var(--line);border-radius:20px;
    padding:8px 14px;color:var(--ink);background:var(--card);text-decoration:none;white-space:nowrap}
  .efs-dbtn:hover{border-color:var(--a);color:var(--a)}

  /* 2. hero */
  .efs-eyebrow{font-size:.72rem;letter-spacing:.09em;text-transform:uppercase;
    color:var(--a);font-weight:700;margin-bottom:8px}
  .efs h1{font-family:'Playfair Display',Georgia,serif;font-size:clamp(1.9rem,4.4vw,2.65rem);
    color:var(--ink);font-weight:600;line-height:1.06;margin:0 0 14px}
  .efs-intro{font-size:.95rem;line-height:1.62;color:var(--body);max-width:76ch;margin:0 0 8px}
  .efs-intro b{color:var(--ink)}
  .efs-introlink{font-size:.88rem;color:var(--a);font-weight:600;text-decoration:none}
  .efs-introlink:hover{text-decoration:underline}

  /* balanced hero row: photo is wider, finance card matches its height */
  .efs-herorow{display:grid;grid-template-columns:1.5fr 1fr;gap:20px;margin-top:24px;align-items:stretch}
  .efs-photo{border-radius:16px;overflow:hidden;position:relative;background:var(--navy);min-height:340px}
  .efs-photo img{width:100%;height:100%;object-fit:cover;display:block}
  .efs-photo .cap{position:absolute;bottom:10px;left:14px;font-size:.63rem;letter-spacing:.09em;
    text-transform:uppercase;color:rgba(255,255,255,.72);text-shadow:0 1px 6px rgba(0,0,0,.6)}

  .efs-fcard{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px;
    box-shadow:var(--sh);display:flex;flex-direction:column}
  .efs-fcard .fe{font-size:.68rem;letter-spacing:.09em;text-transform:uppercase;color:var(--a);
    font-weight:700;margin-bottom:8px}
  .efs-fcard h2{font-family:'Playfair Display',Georgia,serif;font-size:1.4rem;color:var(--ink);
    font-weight:600;margin:0 0 10px}
  .efs-fcard p{font-size:.87rem;line-height:1.56;color:var(--body);margin:0 0 16px}
  .efs-cta{display:block;text-align:center;background:var(--a);color:#fff !important;font-size:.92rem;
    font-weight:700;border-radius:10px;padding:13px;text-decoration:none;
    box-shadow:0 6px 16px -4px rgba(45,127,184,.45);transition:background .15s,transform .1s}
  .efs-cta:hover{background:var(--ad);transform:translateY(-1px)}
  .efs-cta2{display:block;text-align:center;border:1px solid var(--line);color:var(--a) !important;
    font-size:.85rem;font-weight:600;border-radius:10px;padding:11px;text-decoration:none;margin-top:9px}
  .efs-cta2:hover{border-color:var(--a)}
  /* margin-top:auto is what fills the empty wedge -- checks sink to the card
     floor so the card always matches the photo's height */
  .efs-checks{margin-top:auto;padding-top:16px;list-style:none}
  .efs-checks li{display:flex;align-items:center;gap:9px;font-size:.8rem;color:var(--body);padding:5px 0}
  .efs-checks li::before{content:"\\2713";color:var(--green);font-weight:800}

  /* 3. model cards */
  .efs-sec{margin-top:46px}
  .efs-sh{font-family:'Playfair Display',Georgia,serif;font-size:clamp(1.4rem,3vw,1.8rem);
    color:var(--ink);font-weight:600;margin:0 0 4px}
  .efs-ss{font-size:.86rem;color:var(--mut);margin:0 0 20px}
  .efs-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
  .efs-card{background:var(--card);border:1px solid var(--line);border-radius:15px;overflow:hidden;
    box-shadow:var(--sh);display:flex;flex-direction:column;transition:transform .18s,box-shadow .18s}
  .efs-card:hover{transform:translateY(-3px);box-shadow:0 14px 34px -14px rgba(13,31,60,.35)}
  .efs-cimg{position:relative;aspect-ratio:3/2;overflow:hidden;background:var(--navy)}
  .efs-cimg img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s}
  .efs-card:hover .efs-cimg img{transform:scale(1.04)}
  .efs-cap{position:absolute;top:11px;left:11px;background:rgba(255,255,255,.95);color:#0d1f3c;
    font-size:.68rem;font-weight:800;border-radius:20px;padding:4px 11px;
    box-shadow:0 2px 8px rgba(0,0,0,.22)}
  .efs-cbody{padding:15px 16px 17px;display:flex;flex-direction:column;flex:1}
  .efs-ct{font-size:1.02rem;font-weight:700;color:var(--ink);font-family:'Playfair Display',Georgia,serif}
  .efs-chips{display:flex;flex-wrap:wrap;gap:6px;margin:11px 0 14px}
  .efs-chip{font-size:.7rem;color:var(--body);background:var(--bg-secondary);border:1px solid var(--line);
    border-radius:7px;padding:4px 9px}
  .efs-cbtns{margin-top:auto;display:flex;gap:8px}
  .efs-cb1,.efs-cb2{flex:1;text-align:center;font-size:.76rem;border-radius:9px;padding:10px 6px;
    text-decoration:none;font-weight:700}
  .efs-cb1{color:#fff !important;background:var(--a)}
  .efs-cb1:hover{background:var(--ad)}
  .efs-cb2{color:var(--a) !important;border:1px solid var(--line);font-weight:600}
  .efs-cb2:hover{border-color:var(--a)}
  .efs-viewall{font-size:.86rem;color:var(--a);font-weight:600;margin-top:16px;display:inline-block;
    text-decoration:none}
  .efs-viewall:hover{text-decoration:underline}
  .efs-note{font-size:.72rem;color:var(--mut);margin-top:16px;line-height:1.5;max-width:90ch}

  /* full lineup table (deep categories only) */
  .efs-full{margin-top:22px;border:1px solid var(--line);border-radius:14px;background:var(--card);
    overflow:hidden}
  .efs-full>summary{cursor:pointer;padding:14px 18px;font-weight:700;font-size:.88rem;color:var(--ink);
    list-style:none}
  .efs-full>summary::-webkit-details-marker{display:none}
  .efs-full>summary::after{content:"\\25BE";float:right;color:var(--a)}
  .efs-full[open]>summary::after{content:"\\25B4"}
  .efs-tblwrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
  .efs-tbl{width:100%;border-collapse:collapse;font-size:.86rem;min-width:520px}
  .efs-tbl thead th{text-align:left;font-size:.64rem;letter-spacing:.06em;text-transform:uppercase;
    color:var(--mut);font-weight:700;padding:12px 18px;border-top:1px solid var(--line);
    border-bottom:1.5px solid var(--line);background:var(--bg-secondary)}
  .efs-tbl td{padding:12px 18px;border-bottom:1px solid var(--line);color:var(--body);vertical-align:top}
  .efs-tbl tr:last-child td{border-bottom:none}
  .efs-tbl .mdl{font-weight:700;color:var(--ink);white-space:nowrap;
    font-family:'Playfair Display',Georgia,serif}
  .efs-tbl .cap{font-weight:600;color:var(--a);white-space:nowrap}
  .efs-tbl .lk{text-align:right;white-space:nowrap}
  .efs-tbl .lk a{color:var(--a);text-decoration:none;font-weight:700}

  /* 3b. related categories -- preserves the sibling cross-links */
  .efs-rel{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}
  .efs-relcard{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;
    text-decoration:none;box-shadow:var(--sh);transition:transform .18s}
  .efs-relcard:hover{transform:translateY(-3px);border-color:var(--a)}
  .efs-relcard .ri{aspect-ratio:3/2;overflow:hidden;background:var(--navy)}
  .efs-relcard .ri img{width:100%;height:100%;object-fit:cover;display:block}
  .efs-relcard .rn{padding:11px 13px;font-size:.82rem;font-weight:700;color:var(--ink)}

  /* estimator (carried over from the pages that already had one -- do not drop) */
  .efs-est{background:var(--bg-secondary);border:1px solid var(--line);border-radius:12px;
    padding:13px 14px;margin:0 0 13px}
  .efs-est>label{display:block;font-size:.66rem;letter-spacing:.06em;text-transform:uppercase;
    color:var(--mut);font-weight:700;margin-bottom:8px}
  .efs-est-in{display:flex;align-items:center;gap:6px;background:var(--card);border:1px solid var(--line);
    border-radius:9px;padding:9px 11px;color:var(--ink);font-weight:700}
  .efs-est-in input{flex:1;min-width:0;border:0;background:transparent;color:var(--ink);font:inherit;
    font-weight:700;outline:none;padding:0}
  .efs-est-in input::placeholder{color:var(--mut);font-weight:500}
  .efs-est-row{display:flex;gap:9px;margin-top:9px}
  .efs-est-row label{flex:1;font-size:.66rem;color:var(--mut);font-weight:600;display:flex;
    flex-direction:column;gap:4px}
  .efs-est-row select{border:1px solid var(--line);background:var(--card);color:var(--ink);
    border-radius:9px;padding:7px 8px;font:inherit;font-size:.84rem;font-weight:700}
  .efs-est-out{margin-top:10px;font-size:.95rem;color:var(--body)}
  .efs-est-out b{font-family:'Playfair Display',Georgia,serif;font-size:1.35rem;color:var(--a)}
  .efs-est-note{font-size:.67rem;color:var(--mut);line-height:1.45;margin-top:7px}
  .efs-rr{font-size:.7rem;color:var(--mut);text-align:center;margin-top:8px;line-height:1.4}

  /* 4. finance band */
  .efs-band{margin-top:44px;background:linear-gradient(120deg,#1c3358,#0f1d33);border-radius:18px;
    padding:28px 30px;display:flex;align-items:center;gap:26px;color:#fff}
  .efs-band .bl{flex:1;min-width:0}
  .efs-band h2{font-family:'Playfair Display',Georgia,serif;font-size:clamp(1.3rem,2.6vw,1.5rem);
    color:#fff;font-weight:600;margin:0 0 7px}
  .efs-band p{font-size:.87rem;color:rgba(255,255,255,.82);line-height:1.55;max-width:62ch;margin:0}
  .efs-props{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:14px;list-style:none}
  .efs-props li{font-size:.76rem;color:rgba(255,255,255,.87);display:flex;align-items:center;gap:7px}
  .efs-props li::before{content:"\\2713";color:#4ade80;font-weight:800}
  .efs-bandcta{display:flex;flex-direction:column;gap:9px;flex:0 0 auto}
  .efs-bandcta a:first-child{background:#fff;color:#245a94 !important;font-weight:700;font-size:.9rem;
    border-radius:10px;padding:13px 22px;white-space:nowrap;text-decoration:none;text-align:center}
  .efs-bandcta a:first-child:hover{background:#eaf2fa}
  .efs-bandphone{color:rgba(255,255,255,.85) !important;font-size:.8rem;text-align:center;
    text-decoration:none;font-weight:600}
  .efs-bandphone:hover{color:#fff !important}

  /* 5. preserved SEO prose -- same typographic rhythm, copy untouched */
  .efs-seo{margin-top:48px}
  .efs-seo section{padding:16px 0 8px}
  .efs-seo .mx-sec-h{font-family:'Playfair Display',Georgia,serif;
    font-size:clamp(1.3rem,2.8vw,1.7rem);color:var(--ink);font-weight:600;margin:0 0 6px}
  .efs-seo .mx-intro{font-size:.95rem;color:var(--body);max-width:80ch;line-height:1.64}
  .efs-seo .mx-intro b{color:var(--ink)}
  .efs-seo a{color:var(--a);font-weight:600}
  .efs-seo h3{color:var(--ink)}
  .efs-seo .mx-flist{margin:14px 0 0;padding:0;list-style:none;display:grid;gap:9px;max-width:80ch}
  .efs-seo .mx-flist li{padding-left:24px;position:relative;color:var(--body);font-size:.9rem}
  .efs-seo .mx-flist li::before{content:"\\2713";position:absolute;left:0;color:var(--a);font-weight:800}

  /* responsive: hero stacks, cards 3-up -> 2-up -> 1-up */
  @media (max-width:900px){
    .efs-herorow{grid-template-columns:1fr}
    .efs-photo{min-height:240px}
    .efs-band{flex-direction:column;align-items:flex-start}
    .efs-bandcta{width:100%}
    .efs-bandcta a:first-child{display:block}
  }
  @media (max-width:820px){.efs-cards{grid-template-columns:1fr 1fr}.efs-rel{grid-template-columns:1fr 1fr}}
  @media (max-width:560px){
    .efs-cards,.efs-rel{grid-template-columns:1fr}
    .efs-dealer{flex-wrap:wrap}
    .efs-dc{margin-left:0;width:100%}
  }
</style>"""


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
        f'<div class="efs-dc"><a class="efs-dbtn" href="{d["phone_href"]}">&#9742; {d["phone"]}</a>'
        f'<a class="efs-dbtn" href="{d["website_href"]}" target="_blank" rel="noopener">'
        f'&#127760; {d["website"]}</a></div></div>'
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

    # CSS is emitted before the breadcrumb because the breadcrumb <header> lives
    # outside .efs and needs the override above to beat the global `header` rule.
    crumb = (
        CSS
        + '<header class="efs-crumbhead"><nav class="efs-crumb" aria-label="Breadcrumb">'
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


if __name__ == "__main__":
    slugs = sys.argv[1:] or [
        f[:-5] for f in sorted(os.listdir(DATA))
        if f.endswith(".json") and not f.startswith("_")
    ]
    print(f"Building {len(slugs)} category page(s):")
    for s in slugs:
        render(s)
    print("Done.")
