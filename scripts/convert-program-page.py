#!/usr/bin/env python3
"""Convert a legacy program page to the v2 hub template.

The 15 built program pages (working-capital-loans, sba-loans, ...) share one
component vocabulary with the old business-growth page, so one mapping covers
them all:

  .trust-stat          -> .stats tiles, each with an icon and its own tone
  .benefit-card        -> .cards.cards-left with .card-media (image preserved)
  .service-card        -> .cards.cards-left, text only
  .step-card           -> .cards.cards-left, numeral badge, tone per step
  .relevant-post-card  -> .cards link cards
  h4/p pairs in a FAQ  -> .faq details/summary  (better for answer engines)
  "Quick Answer" band  -> .callout
  .ic-wrap calculator  -> preserved verbatim, with its inline script
  anything else        -> .prose (+ .prose-figure when the band has an image)

Rules it follows, learned the hard way:
  * prose is collected at ANY depth, minus component subtrees. Taking only
    direct children silently emptied four sections of business-growth.html.
  * every word, heading, link and JSON-LD block is carried over. Run
    scripts/audit-page-parity.py afterwards - it fails on drift over 2%.
  * bands alternate plain/tinted, and one tone per page: a program page is a
    single topic, so cycling five colours through it is decoration, not
    information.

Usage:
    python scripts/convert-program-page.py working-capital-loans.html [...]
    python scripts/convert-program-page.py --all          # every built program page
    python scripts/convert-program-page.py --dry-run x.html
Backs up the original to _backup-pre-v2-swap/ before writing.
"""
import sys, re, shutil, json
from pathlib import Path
import copy
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
BACKUP = ROOT / "_backup-pre-v2-swap"
VERSION = "202609011423"

PROGRAMS = ["working-capital-loans","business-line-of-credit","business-term-loans","sba-loans",
            "startup-financing","contractor-financing","equipment-financing","commercial-real-estate-loans",
            "commercial-bridge-loans","fix-and-flip","invoice-factoring","revenue-based-financing",
            "merchant-cash-advance","securities-based-lending","business-debt-relief",
            "inventory-financing"]

# one tone per page, grouped by what the product actually is
TONE = {"working-capital-loans":"blue","business-line-of-credit":"blue","business-term-loans":"blue",
        "sba-loans":"indigo","startup-financing":"indigo","contractor-financing":"bronze",
        "equipment-financing":"bronze","commercial-real-estate-loans":"teal",
        "commercial-bridge-loans":"teal","fix-and-flip":"teal","invoice-factoring":"blue",
        "revenue-based-financing":"blue","merchant-cash-advance":"rust",
        "securities-based-lending":"indigo","business-debt-relief":"rust",
        "inventory-financing":"blue"}
INDUSTRIES = [
    "construction-business-financing",
    "roofing-business-financing",
    "hvac-business-financing",
    "plumbing-business-financing",
    "fencing-business-financing",
    "landscaping-business-financing",
    "septic-business-financing",
    "trucking-business-financing",
    "towing-business-financing",
    "logistics-warehousing-business-financing",
    "moving-company-business-financing",
    "manufacturing-business-financing",
    "agriculture-business-financing",
    "forestry-business-financing",
    "medical-practices-business-financing",
    "restaurants-business-financing",
    "auto-repair-business-financing",
    "cleaning-business-financing",
]
TONE.update({
    "construction-business-financing": "bronze",
    "roofing-business-financing": "rust",
    "hvac-business-financing": "teal",
    "plumbing-business-financing": "blue",
    "fencing-business-financing": "bronze",
    "landscaping-business-financing": "teal",
    "septic-business-financing": "indigo",
    "trucking-business-financing": "indigo",
    "towing-business-financing": "rust",
    "logistics-warehousing-business-financing": "blue",
    "moving-company-business-financing": "indigo",
    "manufacturing-business-financing": "rust",
    "agriculture-business-financing": "teal",
    "forestry-business-financing": "teal",
    "medical-practices-business-financing": "blue",
    "restaurants-business-financing": "rust",
    "auto-repair-business-financing": "bronze",
    "cleaning-business-financing": "teal",
})
EQUIPMENT = sorted(
    d.name for d in (ROOT / "equipment").iterdir()
    if d.is_dir() and (d / "index.html").exists()
    and (d / "index.html").read_text(encoding="utf-8", errors="ignore").count("<h2") >= 3)
# one tone per guide, grouped the way equipment.html groups them
EQUIP_TONE = [
    ("bronze", ("excavat", "backhoe", "bulldozer", "skid-steer", "loader", "stump",
                "trencher", "dozer", "compact")),
    ("indigo", ("truck", "van", "trailer", "semi", "tanker", "flatbed", "dump", "log-")),
    ("teal",   ("tractor", "combine", "hay", "grain", "sprayer", "greenhouse", "mower",
                "landscape", "forestry")),
    ("rust",   ("kitchen", "restaurant", "refrigerat", "dishwash", "prep-", "ventilation",
                "pos-", "warewash")),
    ("blue",   ("medical", "dental", "surgical", "imaging", "exam", "lab-", "diagnostic")),
]

def equip_tone(slug):
    for tone, words in EQUIP_TONE:
        if any(w in slug for w in words):
            return tone
    return "blue"


def page_key(path):
    """equipment/excavators/index.html -> equipment__excavators. Every guide is
    called index.html, so the backup directory needs a name that survives 56 of
    them sitting side by side."""
    if path.stem == "index":
        # the whole relative path, not just the last two segments: there is an
        # articles/hvac-business-loans/ AND an equipment-financing/articles/
        # hvac-business-loans/, and a two-segment key collides them
        parts = path.resolve().parent.relative_to(ROOT).parts
        # the root index.html is the hand-built homepage; an empty key
        # wrote a backup literally called ".html" and re-templated it
        return "__".join(parts) if parts else "index"
    return path.stem


HERO_FALLBACK = {
    "contact": "/assets/bloc-hero-business-office.webp",
    "vendors": "/assets/cre-office.webp",
    "privacy-policy": "/assets/cre-office.webp",
    "terms-and-conditions": "/assets/cre-office.webp",
}

STEP_TONES = ["blue","teal","indigo","bronze"]
TILE_TONES = ["blue","teal","indigo","bronze","rust"]

_S = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>')
ICONS = {
 "money":  _S % '<rect x="2.5" y="6" width="19" height="12" rx="2"/><circle cx="12" cy="12" r="2.6"/><path d="M6 10v4M18 10v4"/>',
 "clock":  _S % '<circle cx="12" cy="12" r="9"/><path d="M12 7v5.2l3.2 1.9"/>',
 "trend":  _S % '<polyline points="3 17 9.5 10.5 13.5 14.5 21 7"/><polyline points="15 7 21 7 21 13"/>',
 "shield": _S % '<path d="M12 3.2l7 3v5.9c0 4.1-2.9 7.8-7 8.7-4.1-.9-7-4.6-7-8.7V6.2l7-3Z"/><path d="M9.2 12.1l2 2 3.6-3.8"/>',
 "doc":    _S % '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5Z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/>',
 "check":  _S % '<circle cx="12" cy="12" r="9"/><path d="M8.2 12.3l2.6 2.6 5-5.2"/>',
 "target": _S % '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1.2" fill="currentColor" stroke="none"/>',
 "bank":   _S % '<path d="M3 9.5 12 4l9 5.5"/><path d="M5 10v8M9.7 10v8M14.3 10v8M19 10v8"/><path d="M3 20h18"/>',
 "users":  _S % '<circle cx="9" cy="8.5" r="3.2"/><path d="M3 19a6 6 0 0 1 12 0"/><path d="M16 6.2a3.2 3.2 0 0 1 0 6.1"/><path d="M17.5 19a5.6 5.6 0 0 0-1.8-4"/>',
"truck":  _S % '<path d="M3 7.5h10v9H3z"/><path d="M13 10.5h4l3 3v3h-7z"/><circle cx="7" cy="18" r="1.8"/><circle cx="17" cy="18" r="1.8"/>',
 "factory": _S % '<path d="M3 20V10l5 3V10l5 3V6l6 4v10Z"/><path d="M7 20v-3M12 20v-3M17 20v-3"/>',
 "cross":  _S % '<rect x="3.5" y="3.5" width="17" height="17" rx="3"/><path d="M12 8v8M8 12h8"/>',
 "fork":   _S % '<path d="M7 3v7a2 2 0 0 0 4 0V3"/><path d="M9 10v11"/><path d="M17 3c-1.5 1.5-2 3.5-2 6v3h3V3Z"/><path d="M17 12v9"/>',
 "wrench": _S % '<path d="M15.5 3.5a5.5 5.5 0 0 0-5 8.2L3.8 18.4a2 2 0 1 0 2.8 2.8l6.7-6.7a5.5 5.5 0 0 0 6.7-7.6l-3 3-2.8-.7-.7-2.8Z"/>',
 "leaf":   _S % '<path d="M20 4c0 8-5.5 13-12 13H5c0-8 5.5-13 12-13Z"/><path d="M5 20c2-5 5.5-8.5 9.5-10.5"/>',
 "tree":   _S % '<path d="M12 3 6.5 11h3L5 17h14l-4.5-6h3Z"/><path d="M12 17v4"/>',
 "box":    _S % '<path d="M3.5 7.5 12 3l8.5 4.5v9L12 21l-8.5-4.5Z"/><path d="m3.5 7.5 8.5 4.6 8.5-4.6"/><path d="M12 12.1V21"/>',
 "hardhat":_S % '<path d="M4 16a8 8 0 0 1 16 0"/><path d="M9.5 16V7.5a2.5 2.5 0 0 1 5 0V16"/><path d="M2.5 16h19v2.5h-19z"/>',
 "repeat": _S % '<path d="M4 9.5A8 8 0 0 1 17.9 5.1L20 7"/><path d="M20 3.2V7h-3.8"/><path d="M20 14.5a8 8 0 0 1-13.9 4.4L4 17"/><path d="M4 20.8V17h3.8"/>',
}
TILE_WORDS = [
 (r"truck|transport|fleet|logistic|freight|warehous", "truck"),
 (r"manufactur|industrial|factory|machin|fabric", "factory"),
 (r"medical|health|dental|practice|clinic|veterin", "cross"),
 (r"restaurant|food|hospitality|cafe|bar\b|kitchen", "fork"),
 (r"auto|repair|mechanic|body shop|tire", "wrench"),
 (r"agricultur|farm|crop|dairy|ranch", "leaf"),
 (r"landscap|forest|tree|lawn|nursery", "tree"),
 (r"construct|contractor|build|roofing|concrete|hvac|plumb|electric", "hardhat"),
 (r"retail|ecommerce|e-commerce|inventory|distribut|wholesale", "box"),
]
PRODUCT_WORDS = [
 (r"line of credit|revolving|draw|reuse", "repeat"),
 (r"\bsba\b|government|guarantee", "bank"),
 (r"expedit|same-day|next-day|fast|urgent|24|48 hour|speed", "clock"),
 (r"growth|scal|expansion|grow\b", "trend"),
 (r"major|large|facilit|significant|above \$", "bank"),
 (r"new business|startup|early|young", "users"),
 (r"credit-improving|credit\b|score|fico|rebuild", "shield"),
 (r"invoice|factoring|receivable|a/r", "doc"),
 (r"equipment|machin|vehicle|fleet", "truck"),
 (r"real estate|property|building|commercial mortgage", "hardhat"),
 (r"merchant|card volume|advance|mca", "money"),
 (r"inventory|stock|purchase order|supplier", "box"),
 (r"term loan|lump sum|fixed|amortiz", "money"),
 (r"requirement|qualif|eligib|document", "check"),
 (r"season|cash flow|payroll|gap", "repeat"),
]
def product_icon(text):
    tl = text.lower()
    for pat, name in PRODUCT_WORDS:
        if re.search(pat, tl):
            return ICONS[name]
    return ICONS["target"]

def tile_icon(text):
    tl = text.lower()
    for pat, name in TILE_WORDS:
        if re.search(pat, tl):
            return ICONS[name]
    return ICONS["check"]

ICON_WORDS = [
 (r"\$|amount|funding|loan size|capital|cash", "money"),
 (r"speed|hour|day|fast|time|term|decision", "clock"),
 (r"rate|apr|cost|fee|growth|revenue|roi", "trend"),
 (r"credit|score|fico|collateral|risk|secur", "shield"),
 (r"doc|paperwork|statement|applic|requirement", "doc"),
 (r"lender|bank|sba|institution", "bank"),
 (r"business|owner|industr|client|customer", "users"),
 (r"renew|repeat|revolv|draw|cycle|cadence", "repeat"),
 (r"eligib|qualif|approv", "check"),
]
def pick_icon(text):
    t = text.lower()
    for pat, name in ICON_WORDS:
        if re.search(pat, t):
            return ICONS[name]
    return ICONS["target"]

CHROME = {"main-nav","mobile-nav-overlay","mobile-overlay-links","site-footer",
          "mobile-cta-bar","nav-links","nav-dropdown-menu"}

def _is_chrome(el):
    for p in [el] + list(el.parents):
        if CHROME & set(p.get("class") or []):
            return True
    return False

def content_blocks(soup):
    """Every element that owns an <h2> as a direct child, outermost first, in
    document order.

    Selecting `.about-section` alone looked right and quietly skipped the
    `*-intro-text`, `*-amounts-text`, `*-industry-text` and `section.calc`
    blocks - 19% of inventory-financing.html went missing that way. Anything
    with its own h2 is a section, whatever it calls itself.
    """
    cand = []
    for el in soup.find_all(["section", "div", "article"]):
        if _is_chrome(el):
            continue
        # a wrapper that still contains site chrome (the page's <div class=
        # "container"> holds the whole legacy nav) is not a content section.
        # Left in, it swallowed every real section beneath it as "nested".
        if any(CHROME & set(d.get("class") or []) for d in el.find_all(True)):
            continue
        if not any(c.name == "h2" for c in el.find_all(recursive=False)):
            continue
        cand.append(el)
    # keep the innermost: drop any candidate that contains another candidate
    inner = [el for el in cand if not any(o is not el and o in el.descendants for o in cand)]
    # An .about-section often holds the heading/prose in one child div and the
    # illustration in a sibling *-img div. Converting the inner div alone drops
    # the picture, so climb to the section when it wraps exactly this block.
    out = []
    for el in inner:
        sec = el.find_parent(class_="about-section")
        if sec is not None and sum(1 for o in inner if o in sec.descendants) == 1:
            el = sec
        else:
            # The location and loan-amount pages put the <h2> in its own
            # heading wrapper (div.wrap.sh) with the copy in a SIBLING div, so
            # taking the block that owns the heading collected the heading and
            # nothing else - half of each page. Climb to the parent when the
            # parent holds this heading and no other, and carries more text.
            par = el.parent
            if (par is not None and getattr(par, "name", None) in ("section", "div", "article")
                    and not _is_chrome(par)
                    and len(par.find_all("h2")) == sum(1 for o in inner if o in par.descendants)
                    and not any(CHROME & set(d.get("class") or []) for d in par.find_all(True))):
                words_el = sum(len(" ".join(o.get_text(" ").split()).split())
                                for o in inner if o in par.descendants)
                words_par = len(" ".join(par.get_text(" ").split()).split())
                if words_par > words_el * 1.15:
                    el = par
        if el not in out:
            out.append(el)
    # Promotion can lift one block to a shared parent while its siblings stay
    # put, leaving the parent AND its children selected - every paragraph then
    # shipped twice. Keep the outermost of any overlapping pair; the splitter
    # separates it back into one band per heading.
    out = [el for el in out
           if not any(o is not el and el in o.descendants for o in out)]
    return out

SKIP_EXACT = {"trust-stat","trust-band-item","trust-band-num","trust-band-label",
              "wcl-hero-ctas","hero-ctas","ic-cta","calc-cta","step-card","service-card","benefit-card","relevant-post-card",
              "section-cta","ic-wrap","relevant-info-cta","step-number","trust-stat-number",
              "trust-stat-label","blog-card-link"}
SKIP_RE = re.compile(r"-card(-img|-with-img)?$|-ctas?$|-phone-cta$")

def is_button_row(el):
    """A container whose element children are all button links.

    Matching CTA rows by class name kept failing: .section-cta, .wcl-hero-ctas,
    .bloc-cta-buttons ... each page names it differently, and a missed one gets
    emitted as prose - two anchors loose in a paragraph, sitting on top of the
    card grid. Structure is the reliable signal.
    """
    if getattr(el, "name", None) not in ("div", "p"):
        return False
    kids = [c for c in el.find_all(recursive=False)]
    links = [c for c in kids if c.name == "a"]
    if not links or len(links) != len(kids):
        return False
    return all("btn" in " ".join(a.get("class") or []) for a in links)


def is_button(el):
    return getattr(el, "name", None) == "a" and "btn" in " ".join(el.get("class") or [])


def in_component(el):
    """True if the element is inside - or IS - a component we render separately.
    Checking only .parents let a .section-cta div's own text through twice."""
    if is_button(el):
        return True
    for p in [el] + list(el.parents):
        if is_button_row(p):
            return True
        for c in (p.get("class") or []):
            if c in SKIP_EXACT or SKIP_RE.search(c):
                return True
    return False

def split_multi_heading(blocks):
    """One band per <h2>.

    Some sections stack five or six h2 headings inside a single
    .about-section. Emitting one band per section kept the paragraphs but
    dropped every heading after the first - the word count barely moved, so
    nothing looked wrong while four headings quietly disappeared from
    merchant-cash-advance.
    """
    out = []
    for sec in blocks:
        def _starts_group(k):
            # a direct child that is an h2, or a heading wrapper holding one -
            # the location pages put every <h2> in its own <div class="wrap sh">
            # with the copy in the sibling div
            if getattr(k, "name", None) is None:
                return False
            if k.name == "h2":
                return True
            if k.name in ("div", "section", "header"):
                first = k.find(["h2", "h3", "p", "ul", "table"])
                return first is not None and first.name == "h2"
            return False

        heads = [c for c in sec.find_all(recursive=False) if _starts_group(c)]
        if len(heads) < 2:
            out.append(sec)
            continue
        kids = list(sec.find_all(recursive=False))
        groups, current = [], None
        for k in kids:
            if _starts_group(k):
                current = [k]
                groups.append(current)
            elif current is not None:
                current.append(k)
        soup = BeautifulSoup("", "html.parser")
        for g in groups:
            holder = soup.new_tag("section")
            holder["class"] = list(sec.get("class") or [])
            for node in g:
                holder.append(copy.copy(node))
            out.append(holder)
    return out


def prose_html(sec):
    """p/ul/ol/table anywhere in the block, minus component subtrees, plus any
    text-bearing div that holds none of those (callout boxes carry their copy
    as bare div text and were being dropped)."""
    def _pos(el):
        return (el.sourceline or 0, el.sourcepos or 0)

    items = []
    for el in sec.find_all(["p", "ul", "ol", "table", "h3", "h4"]):
        if in_component(el) or el.find_parent("li") or el.find_parent("table"):
            continue
        if el.name in ("h3", "h4"):
            items.append((_pos(el), str(el)))
            continue
        if el.name == "table":
            items.append((_pos(el), '<div class="table-wrap">%s</div>' % str(el)))
        else:
            items.append((_pos(el), str(el)))
    captured = {id(el) for el in sec.find_all(["p", "ul", "ol", "table", "h3", "h4"])}
    # Text-bearing divs at ANY depth, not just direct children. The location
    # pages keep whole paragraphs in nested <div class="wrap"> blocks and the
    # articles keep labels in <div class="tline">; walking direct children only
    # left 100+ words per page on the floor. Innermost ones only, so a wrapper
    # never repeats what its children already contributed.
    for d in sec.find_all(["div", "dd", "dt"]):
        if in_component(d) or not d.get_text(strip=True):
            continue
        if any(id(x) in captured for x in d.find_all(["p", "ul", "ol", "table", "h3", "h4"])):
            continue
        if d.find(["div", "section", "table", "ul", "ol", "p", "dl", "h3", "h4"]):
            continue
        items.append((_pos(d), '<p>%s</p>' % d.decode_contents().strip()))
    items.sort(key=lambda kv: kv[0])          # keep the author's reading order
    out = merge_orphan_line([html for _, html in items])
    return "\n        ".join(out)

LINKLIST_RE = re.compile(r"<ul\b.*?</ul>", re.S)

def tiles_from_list(html):
    """A <ul> whose items are single links becomes a tile grid.

    "Industries we serve" shipped as ten bullets: correct markup, poor target
    size, no visual scent. Same links, same order, same anchor text - only the
    presentation changes.
    """
    def repl(m):
        frag = BeautifulSoup(m.group(0), "html.parser")
        lis = frag.find_all("li")
        if len(lis) < 4:
            return m.group(0)
        linky = [li for li in lis if li.find("a") and len(li.get_text(strip=True)) <= 42]
        if len(linky) < len(lis) * 0.8:
            return m.group(0)
        out = []
        for n, li in enumerate(lis):
            a = li.find("a")
            if not a:
                continue
            label = a.get_text(strip=True)
            href = a.get("href") or "#"
            if href and not href.startswith(("/", "http", "#", "tel:", "mailto:")):
                href = "/" + href
            out.append('        <a class="tile" data-tone="%s" href="%s">'
                       '<span class="tile-icon">%s</span><span>%s</span></a>'
                       % (TILE_TONES[n % 5], href, tile_icon(label), label))
        return '<div class="tiles">\n%s\n      </div>' % "\n".join(out)
    return LINKLIST_RE.sub(repl, html)


AMOUNT_LI = re.compile(r"^(.*?)\s*[\u2014-]\s*(\$[\d,]+(?:\s*(?:to|\u2013|-)\s*\$?[\d,]+\+?)?\+?)\s*(?:for\s+)?(.*)$", re.S)

def table_from_amount_list(html):
    """A list of "Industry - $range - what it funds" becomes a real table.

    Same rows, same links, same numbers - but addressable by an answer engine
    and far quicker to scan than seven wrapped bullets.
    """
    def repl(m):
        frag = BeautifulSoup(m.group(0), "html.parser")
        lis = frag.find_all("li")
        if len(lis) < 4:
            return m.group(0)
        rows, ok = [], 0
        for li in lis:
            inner = li.decode_contents().strip()
            mm = AMOUNT_LI.match(" ".join(inner.split()))
            if not mm:
                rows.append(("", "", inner)); continue
            ok += 1
            rows.append((mm.group(1).strip(), mm.group(2).strip(), mm.group(3).strip()))
        if ok < len(lis) * 0.7:
            return m.group(0)
        body = "\n".join(
            "          <tr><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in rows)
        return ('<div class="table-wrap"><table class="data-table">\n'
                '        <thead><tr><th>Industry</th><th>Typical amount</th><th>What it funds</th></tr></thead>\n'
                '        <tbody>\n%s\n        </tbody>\n      </table></div>' % body)
    return LINKLIST_RE.sub(repl, html)


FEATURE_LI = re.compile(r"^\s*<strong>(.+?)</strong>\s*[\u2014-]?\s*(.+)$", re.S)

def cards_from_feature_list(html):
    """A short list of "**Label** - explanation" bullets becomes cards.

    Four value propositions set as bullets read as fine print; as boxes with a
    symbol and their own colour they read as four reasons. Same words, same
    order. Only fires on 3-6 items that all have a bold lead-in and an actual
    sentence after it, so link lists and amount lists are left to their own
    transforms.
    """
    def repl(m):
        frag = BeautifulSoup(m.group(0), "html.parser")
        lis = frag.find_all("li")
        if not (3 <= len(lis) <= 6):
            return m.group(0)
        parsed = []
        for li in lis:
            inner = " ".join(li.decode_contents().strip().split())
            mm = FEATURE_LI.match(inner)
            if not mm or len(BeautifulSoup(mm.group(2), "html.parser").get_text().split()) < 5:
                return m.group(0)
            parsed.append((mm.group(1).strip(), mm.group(2).strip().lstrip("\u2014- ")))
        out = []
        for n, (label, body) in enumerate(parsed):
            out.append('        <article class="card" data-tone="%s">\n'
                       '          <span class="card-icon">%s</span>\n'
                       '          <h3>%s</h3>\n          <p>%s</p>\n        </article>'
                       % (TILE_TONES[n % 5], product_icon(label + " " + body[:100]),
                          BeautifulSoup(label, "html.parser").get_text(), body))
        return '<div class="cards cards-left">\n%s\n      </div>' % "\n".join(out)
    return LINKLIST_RE.sub(repl, html)


def merge_orphan_line(items):
    """Fold a short trailing paragraph into the one before it.

    Prose is emitted above the component grid, so a one-line caption that sat
    under the grid in the source ended up floating on its own above it. Rather
    than leave a stranded sentence, it joins the previous paragraph.
    """
    if len(items) < 2:
        return items
    last = items[-1]
    if not last.startswith("<p"):
        return items
    text = BeautifulSoup(last, "html.parser").get_text(" ", strip=True)
    if not text or len(text.split()) > 14:
        return items
    prev = items[-2]
    if not prev.startswith("<p"):
        return items
    inner_prev = BeautifulSoup(prev, "html.parser").find("p")
    inner_last = BeautifulSoup(last, "html.parser").find("p")
    merged = "<p>%s %s</p>" % (inner_prev.decode_contents().strip(),
                               inner_last.decode_contents().strip())
    return items[:-2] + [merged]


def fix_broken_apostrophes(html):
    """The source pages carry &mdash; where an apostrophe belongs - "don&mdash;t",
    "here&mdash;s", "we&mdash;ll". Only a suffix that is exactly a contraction
    ending is converted, so genuine em dashes ("growth&mdash;regardless",
    "sell&mdash;so") are left alone."""
    return re.sub("(\\w)(?:&mdash;|\u2014)(t|s|re|ll|ve|d|m)\\b",
                  lambda m: m.group(1) + "\u2019" + m.group(2), html)


GRID_RE = re.compile(r'(<div class="(?:cards[^"]*|tiles)">.*?</div>\s*(?=<|$))', re.S)

def render_prose(pr):
    """Wrap text in .prose, but let generated grids out of it.

    .prose caps at 46rem for readability. A card grid left inside inherits that
    cap and wraps early. Parsed rather than regex-split: the old pattern
    stopped at the first </div>, so any grid containing a nested div escaped it.
    """
    if not pr:
        return ""
    frag = BeautifulSoup("<div id='__r'>%s</div>" % pr, "html.parser").find(id="__r")
    out, buf = [], []

    def flush():
        if buf:
            body = "".join(buf).strip()
            if body:
                out.append('      <div class="prose">\n        %s\n      </div>' % body)
            buf.clear()

    for node in list(frag.children):
        classes = set(getattr(node, "get", lambda *_: [])("class") or [])
        if node.name == "div" and ({"cards", "tiles"} & classes):
            flush()
            out.append("      %s" % str(node))
        else:
            buf.append(str(node))
    flush()
    return "\n".join(out) + "\n"


def cta_html(sec):
    rows = [d for d in sec.find_all(["div", "p"]) if is_button_row(d)]
    seen, links = set(), []
    # plus any stray button that is not inside a card - business-debt-relief
    # keeps one in a bare <div>, which no name-based or all-children rule caught
    loose = [a for a in sec.find_all("a")
             if is_button(a) and not any("card" in " ".join(x.get("class") or []) for x in a.parents)
             and not any(a in r.find_all("a") for r in rows)]
    for row in rows + [None]:
        for a in (row.find_all("a", recursive=False) if row is not None else loose):
            if id(a) in seen:
                continue
            seen.add(id(a))
            href = a.get("href") or "#"
            if href and not href.startswith(("/", "http", "tel:", "mailto:", "#")):
                href = "/" + href
            cls = " ".join(a.get("class") or [])
            kind = "btn-secondary" if "secondary" in cls else "btn-primary"
            links.append('<a class="btn %s" href="%s">%s</a>' % (kind, href, a.get_text(strip=True)))
    if not links:
        return ""
    return ('\n    <p class="cta-actions cta-actions-left">%s</p>' % "".join(links))

def band(title, inner, alt, extra="", tone="blue"):
    return ('<section class="section%s">\n  <div class="container">\n'
            '    <div class="group" data-tone="%s">\n'
            '      <div class="group-head"><h2>%s</h2></div>\n%s%s\n    </div>\n  </div>\n</section>'
            % (" section-alt" if alt else "", tone, title, inner, extra))

def _asset_ok(url):
    if not url or url.startswith(("http", "data:")):
        return True
    f = ROOT / url.split("?")[0].lstrip("/")
    return f.exists() and f.stat().st_size > 0


def usable_pic(el):
    """True unless every file the element points at is missing or zero bytes.
    Two manufacturing PNGs are 0 bytes on disk, so the page shipped a broken
    image icon where a photo should be. A dead image is no image: the band
    falls back to the placeholder panel instead."""
    if el is None:
        return False
    urls = []
    for im in ([el] if el.name == "img" else el.find_all("img")):
        urls.append(im.get("src"))
    for so in ([] if el.name == "img" else el.find_all("source")):
        ss = so.get("srcset") or ""
        if ss:
            urls.append(ss.split()[0])
    urls = [u for u in urls if u]
    return any(_asset_ok(u) for u in urls) if urls else False


def has_class(value, *names):
    """bs4 hands a class_ callable the raw attribute value, which is a string
    for a single-class element - so `any(x == "faq" for x in value)` silently
    iterates characters. Normalise before comparing."""
    if not value:
        return False
    parts = value.split() if isinstance(value, str) else list(value)
    return any(p == n or (n.endswith("*") and p.startswith(n[:-1])) for p in parts for n in names)


def faq_pairs(sec):
    """Q/A pairs wherever the source keeps them - as direct h3/h4 siblings, or
    (the equipment guides) inside a .faq-list wrapper. Matching only direct h4
    children left seven questions rendering as flat prose."""
    pairs = []
    for h in sec.find_all(["h3", "h4"]):
        if in_component(h):
            continue
        q = " ".join(h.get_text(" ").split())
        ans = []
        for sib in h.find_next_siblings():
            if sib.name in ("h2", "h3", "h4"):
                break
            if sib.name in ("p", "ul", "ol"):
                ans.append(str(sib))
            elif sib.name == "div" and sib.get_text(strip=True) and not sib.find(
                    ["h2", "h3", "h4"]):
                inner = sib.decode_contents().strip()
                ans.append(inner if inner.lstrip().startswith("<") else "<p>%s</p>" % inner)
        if q and ans:
            pairs.append((q, "".join(ans)))
    return pairs


def equip_cards(grid):
    """.industry-equipment-grid -> photo cards. Each row is an image plus a
    body (heading, copy, link); stacked raw they read as a wall of pictures,
    and prose extraction walked straight past them. Heading level is kept as
    the source wrote it so the outline does not shift."""
    out = []
    rows = grid.find_all("div", class_=lambda c: c and (
        "industry-equipment-row" in c or "industry-equipment-card" in c))
    for i, row in enumerate(rows):
        img = row.find("picture") or row.find("img")
        body = (row.find("div", class_="industry-equipment-body")
                or row.find("div", class_="industry-equipment-text"))
        if body is None:
            continue
        h = body.find(["h3", "h4", "h5"])
        title = h.get_text(" ", strip=True) if h is not None else ""
        rest = "".join(str(c) for c in body.find_all(recursive=False) if c is not h)
        media = '        <div class="card-media">%s</div>\n' % str(img) if img else ""
        out.append('      <article class="card" data-tone="%s">\n%s        <%s>%s</%s>\n%s\n      </article>'
                   % (TILE_TONES[i % len(TILE_TONES)], media,
                      h.name if h is not None else "h3", title,
                      h.name if h is not None else "h3", rest))
    if not out:
        return ""
    return '<div class="cards cards-left">\n%s\n      </div>' % "\n".join(out)


def card_head(el):
    """A card's heading is h3 on some pages and h4 on others; the h3-only
    filter silently dropped five of eight cards on working-capital-loans."""
    h = el.find(["h3", "h4", "h5"])
    return h.get_text(strip=True) if h else ""

def card_body(el):
    """All paragraphs, not just the first."""
    return "</p>\n      <p>".join(p.decode_contents().strip() for p in el.find_all("p")) or ""

def card(h3, body, tone=None, media="", eyebrow="", href=None, cta="", icon=""):
    t = ' data-tone="%s"' % tone if tone else ""
    head = ('      <p class="eyebrow">%s</p>\n' % eyebrow) if eyebrow else ""
    ic = ('      <span class="card-icon">%s</span>\n' % icon) if icon else ""
    inner = "%s%s%s      <h3>%s</h3>\n      <p>%s</p>\n%s" % (media, ic, head, h3, body, cta)
    if href:
        return '    <a class="card"%s href="%s">\n%s    </a>' % (t, href, inner)
    return '    <article class="card"%s>\n%s    </article>' % (t, inner)


KEEP_DECL = ("display", "visibility")


def _clean_styles(node):
    """Drop inline presentation, keep inline behaviour. A widget hidden with
    style="display:none" must stay hidden."""
    for el in node.find_all(style=True):
        keep = [d.strip() for d in el["style"].split(";")
                if d.strip() and d.split(":")[0].strip().lower().startswith(KEEP_DECL)]
        if keep:
            el["style"] = ";".join(keep)
        else:
            el.attrs.pop("style", None)
    return node


SUMMARY_LABEL = re.compile(r'^\s*(quick answer|in short|short answer|bottom line|tl;dr)\s*[:\u2014-]\s*', re.I)


def article_bands(s, shell, tone, slug):
    """The long-form guide template: a body column and one sticky rail.

    The source keeps two rails - a left one holding only a back link, a date
    and a CTA, and a right one holding the table of contents. Folding the left
    rail's contents into the article (breadcrumb, dateline) and the rail (quick
    facts, CTA) gives the body real measure instead of a narrow middle column.
    Heading ids are preserved exactly: the TOC and external anchors use them.
    """
    main_src = shell.find("main")
    if main_src is None:
        return []
    left = shell.find("aside", class_="blog-post-rail-left")
    toc_src = shell.find("div", class_="blog-rail-toc")
    cta_src = shell.find(class_="services-cta")
    # Work on a copy and lift the components out of it. Skipping them by
    # identity only worked while they were direct children of <main>; on some
    # pages the FAQ is nested inside a <p>, so the paragraph carried the whole
    # block along and every answer shipped twice.
    main = copy.copy(main_src)
    for sec_el in main.find_all("section"):
        sid = sec_el.get("id")
        if not sid:
            continue
        h = sec_el.find(["h2", "h3"])
        if h is not None and not h.get("id"):
            h["id"] = sid          # the anchor now lands on the heading itself
    faq_src = main.find(["div", "section"],
                        class_=lambda c: has_class(c, "article-faq", "article-faq__*", "faq-list"))
    rel_src = main.find("section", class_="related-resources")
    qa_node = main.find("div", class_="quick-answer")
    faq_head_html = ""
    if faq_src is None:
        # some pages write the FAQ as a <section> of h3/p pairs instead of the
        # .article-faq div. Detect it here, before the body is flattened, or
        # the questions ship twice - once as prose and once as accordions.
        for cand in main.find_all(["section", "div"]):
            h = cand.find(["h2", "h3"])
            head_txt = h.get_text(" ", strip=True).lower() if h is not None else ""
            if (cand.get("id") == "faqs" or "frequently asked" in head_txt
                    or head_txt.strip().endswith("faqs")) and len(faq_pairs(cand)) >= 2:
                faq_src = cand
                if h is not None:
                    faq_head_html = "        %s\n" % str(_clean_styles(copy.copy(h)))
                break
    for node in (faq_src, rel_src, qa_node):
        if node is not None:
            node.extract()

    # --- breadcrumb + dateline, lifted out of the left rail ---
    head_bits = ""
    if left is not None:
        blocks = left.find_all("div", class_="article-rail__block")
        if blocks:
            b0 = copy.copy(blocks[0])
            _clean_styles(b0)
            # the date is a text node sitting after a "Updated" label span, so
            # reading the label element alone gave the word with no date
            date = ""
            for el in b0.find_all(["div", "p", "time"]):
                txt = " ".join(el.get_text(" ").split())
                if txt.lower().startswith("updated") and len(txt.split()) > 1:
                    date = txt
                    break
            # the two links were separated by a bare "|" text node; joining the
            # anchors ran them together into one uppercase sentence
            links = [a for a in b0.find_all("a")]
            if links:
                crumbs = ""
                for n_a, a_el in enumerate(links):
                    a2 = _clean_styles(copy.copy(a_el))
                    a2["class"] = ["crumb"]
                    if n_a:
                        a2["data-tone"] = "bronze"
                    crumbs += "          %s\n" % str(a2)
                head_bits += '        <div class="crumb-row">\n%s        </div>\n' % crumbs
            if date:
                head_bits += '        <p class="dateline">%s</p>\n' % date
    # --- quick answer -> the navy callout used everywhere else ---
    qa = qa_node
    qa_html, qa_id = "", "quick-answer"
    if qa is None:
        # Many guides open with their own labelled summary - "Quick Answer:" or
        # "In short:" - as the first paragraph. That IS the quick answer; it
        # belongs in the callout, with the label dropped (the callout says it).
        first_p = None
        for cand in main.find_all("p"):
            if cand.get_text(strip=True):
                first_p = cand
                break
        if first_p is not None:
            txt = " ".join(first_p.get_text(" ").split())
            mt = SUMMARY_LABEL.match(txt)
            if mt and len(txt.split()) >= 12:
                lifted = copy.copy(first_p)
                inner = lifted.decode_contents()
                inner = re.sub(r'^\s*(<(?:b|strong|span)[^>]*>\s*)?' + mt.group(1) +
                               r'\s*[:\u2014-]\s*(</(?:b|strong|span)>)?\s*', '', inner,
                               count=1, flags=re.I)
                lifted.clear()
                lifted.append(BeautifulSoup(inner, "html.parser"))
                qa = lifted
                first_p.extract()
    if qa is not None:
        q = _clean_styles(copy.copy(qa))
        label = q.find("strong")
        eyebrow = ""
        if label is not None and len(label.get_text(strip=True).split()) <= 3:
            eyebrow = '          <p class="eyebrow">%s</p>\n' % label.get_text(" ", strip=True)
            label.decompose()
        qa_id = qa.get("id") or "quick-answer"
        qa_html = (
            '      <div class="callout" id="{id}">\n{eyebrow}'
            '        <div class="prose">\n          {inner}\n'
            '        </div>\n      </div>\n'
        ).format(id=qa_id, eyebrow=eyebrow, inner=q.decode_contents().strip())

    # --- body ---
    body, first_para = "", True
    demoted = []                 # ids of headings that turned out to be labels

    def flatten(node, acc):
        for el in node.find_all(recursive=False):
            if getattr(el, "name", None) is None:
                continue
            if el.name in ("script", "style"):
                continue
            # wrappers left empty once a component was lifted out
            if not el.get_text(strip=True) and not el.find(["img", "picture", "table", "iframe", "input"]):
                continue
            cls = " ".join(el.get("class") or [])
            if "services-cta" in cls or is_button_row(el):
                continue
            if el.name == "section":
                flatten(el, acc)     # nested sections are just more article flow
                continue
            acc.append(el)
        return acc

    flat = flatten(main, [])
    for n_el, el in enumerate(flat):
        # a heading with nothing under it before the next heading is a divider
        # the writer used as a group label, not a section of its own. Rendered
        # as an <h2> it reads as a heading someone forgot to write copy for.
        if el.name == "h2":
            nxt = flat[n_el + 1] if n_el + 1 < len(flat) else None
            if nxt is not None and nxt.name in ("h2", "h3"):
                lab = _clean_styles(copy.copy(el))
                if lab.get("id"):
                    demoted.append(lab["id"])
                lab.name = "p"
                lab["class"] = ["section-label"]
                body += "        %s\n" % str(lab)
                continue
            e = _clean_styles(copy.copy(el))
        else:
            e = _clean_styles(copy.copy(el))
        if e.name == "table":
            body += '        <div class="table-wrap">%s</div>\n' % str(e)
        elif e.name == "figure":
            e["class"] = ["article-figure"]
            body += "        %s\n" % str(e)
        elif e.name == "p" and first_para and e.get_text(strip=True):
            e["class"] = (e.get("class") or []) + ["lede-para"]
            body += "        %s\n" % str(e)
            first_para = False
        else:
            body += "        %s\n" % str(e)

    # --- FAQ -> accordions ---
    if faq_src is not None:
        pairs = faq_pairs(faq_src)
        if pairs:
            body += faq_head_html
            body += ('        <div class="faq">\n%s\n        </div>\n' %
                     "\n".join('          <details>\n            <summary>%s</summary>\n'
                                '            <div class="answer">%s</div>\n          </details>' % pr
                                for pr in pairs))

    # --- rail ---
    rail = ""
    if toc_src is not None:
        nav = copy.copy(toc_src)
        _clean_styles(nav)
        h = nav.find(["h2", "h3", "h4"])
        heading = h.get_text(" ", strip=True) if h is not None else "On this page"
        lst = nav.find(["ul", "ol"])
        if lst is not None:
            for li in lst.find_all("li"):
                a_el = li.find("a", href=True)
                if a_el is not None and a_el["href"].lstrip("#") in demoted:
                    li.decompose()
            lst.attrs.pop("class", None)
            rail += ('        <nav class="toc" aria-label="%s">\n          <h3>%s</h3>\n'
                     '          %s\n        </nav>\n' % (heading, heading, str(lst)))
    rail_cta = None
    if left is not None:
        for blk in left.find_all("div", class_="article-rail__block")[1:]:
            if blk.find("a", class_=lambda c: c and "btn" in " ".join(
                    c if isinstance(c, list) else [c])) is not None:
                rail_cta = blk
    actions = ""
    if qa_html:
        actions += ('          <a class="btn btn-quiet" href="#%s">Quick answer</a>\n' % qa_id)
    if rail_cta is not None:
        a_btn = rail_cta.find("a", class_=lambda c: c and "btn" in " ".join(
            c if isinstance(c, list) else [c]))
        if a_btn is not None:
            actions += ('          <a class="btn btn-primary" href="%s">%s</a>\n'
                        % (a_btn.get("href", "/match.html"),
                           a_btn.get_text(" ", strip=True)))
    if actions:
        rail = '        <div class="rail-actions">\n%s        </div>\n' % actions + rail
    if False:
        for blk in left.find_all("div", class_="article-rail__block")[1:]:
            b = _clean_styles(copy.copy(blk))
            b.attrs.pop("class", None)
            for hx in b.find_all(["h2", "h4"]):
                hx.name = "h3"
            is_cta = bool(b.find("a", class_=lambda c: c and "btn" in " ".join(c if isinstance(c, list) else [c])))
            for a_el in b.find_all("a"):
                acl = " ".join(a_el.get("class") or [])
                if "btn" in acl:
                    a_el["class"] = ["btn"]
            rail += '        <div class="rail-card%s">\n          %s\n        </div>\n' % (
                " rail-cta" if is_cta else "", b.decode_contents().strip())

    grid = ('    <div class="article-grid">\n'
            '      <div class="article-body">\n%s%s%s      </div>\n'
            '      <aside class="article-rail">\n%s      </aside>\n'
            '    </div>' % (head_bits, qa_html, body, rail))
    out = ['<section class="section section-tight">\n  <div class="container article-container">\n'
           '%s\n  </div>\n</section>' % grid]

    if rail_cta is not None:
        h = rail_cta.find(["h2", "h3", "h4"])
        body_p = "".join(str(_clean_styles(copy.copy(c)))
                         for c in rail_cta.find_all("p")
                         if c.get_text(strip=True) and not is_button_row(c)
                         and not is_button(c.find("a")) if True)
        out.append(band(h.get_text(" ", strip=True) if h is not None else "Ready to get funded?",
                        '      <div class="prose">\n        %s\n      </div>' % body_p,
                        False, cta_html(rail_cta), tone))

    # --- related resources as tiles ---
    if rel_src is not None:
        links = [a for a in rel_src.find_all("a") if a.get("href") and not is_button(a)]
        if links:
            tiles = "\n".join(
                '      <a class="tile" data-tone="%s" href="%s">\n'
                '        <span class="tile-icon">%s</span>\n        <span>%s</span>\n      </a>'
                % (TILE_TONES[i % 5], a["href"], product_icon(a.get_text(" ", strip=True)),
                   a.get_text(" ", strip=True))
                for i, a in enumerate(links))
            h = rel_src.find(["h2", "h3"])
            rid = rel_src.get("id") or (h.get("id") if h is not None else None)
            out.append((band(h.get_text(" ", strip=True) if h else "Related Resources",
                            '      <div class="tiles">\n%s\n      </div>' % tiles,
                            False, "", tone)
                        # keep the anchor the contents list points at
                        .replace('<section class="section"',
                                 '<section id="%s" class="section"' % rid, 1)
                        if rid else band(h.get_text(" ", strip=True) if h else "Related Resources",
                            '      <div class="tiles">\n%s\n      </div>' % tiles, False, "", tone)))

    # --- closing CTA ---
    if cta_src is not None and not cta_src.find(["h2", "h3", "h4"]) and not [
            c for c in cta_src.find_all("p", recursive=False) if c.get_text(strip=True)]:
        row = cta_html(cta_src).strip()
        if row:
            out[0] = out[0].replace('      </div>\n      <aside class="article-rail">',
                                    '  %s\n      </div>\n      <aside class="article-rail">' % row, 1)
        cta_src = None
    if cta_src is not None:
        h = cta_src.find(["h2", "h3", "h4"])
        copy_p = "".join(str(_clean_styles(copy.copy(c)))
                         for c in cta_src.find_all(["p"], recursive=False)
                         if c.get_text(strip=True) and not is_button_row(c))
        out.append(band(h.get_text(" ", strip=True) if h is not None else "Get Started",
                        '      <div class="prose">\n        %s\n      </div>' % (copy_p or ""),
                        False, cta_html(cta_src), tone))
    return out


def article_pages():
    """Every long-form guide, wherever it lives: */articles/<slug>/,
    articles/<slug>/ and the industry article folders. Identified by the
    template's own shell class, in the live file or in its backup, so the list
    is the same before and after a conversion."""
    out = []
    for f in sorted(ROOT.rglob("index.html")):
        if any(part.startswith("_") for part in f.relative_to(ROOT).parts):
            continue
        key = BACKUP / (page_key(f) + ".html")
        src = key if key.exists() else f
        try:
            head = src.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if "blog-post-shell" in head:
            out.append(f.relative_to(ROOT).as_posix())
    return out


def inject_quick_answer_schema(html):
    """Put the page's quick answer into its FAQPage block as the first Q&A.

    The callout is the passage an answer engine wants, but it was only prose in
    a div - present in the structured data on 16 of 284 pages sampled. The
    answer text stays exactly what is visible on the page, which is what the
    FAQPage markup requires.
    """
    soup = BeautifulSoup(html, "html.parser")
    callout = soup.select_one(".callout")
    if callout is None:
        return html
    body = copy.copy(callout)
    for lbl in body.select(".eyebrow"):
        lbl.decompose()
    answer = " ".join(body.get_text(" ").split())
    if len(answer.split()) < 20:
        return html

    question = ""
    for h2 in soup.select("section.section h2"):
        txt = " ".join(h2.get_text(" ").split())
        if txt.lower().startswith("quick answer"):
            rest = re.sub(r"^quick answer\s*[:\u2014-]\s*", "", txt, flags=re.I).strip()
            if len(rest.split()) >= 3:
                question = rest
            break
    if not question and soup.h1 is not None:
        question = " ".join(soup.h1.get_text(" ").split())
    question = re.split(r"\s+[|\u2014]\s+", question)[0].strip()
    # Only mark it up when it is genuinely a question. Google restricted FAQ
    # rich results to authoritative sites in 2023, so the upside is small and
    # the downside - a structured-data action for FAQPage entries that are not
    # questions - is real. A statement headline gets no markup.
    # Only genuine questions. Appending "?" to a statement heading produced
    # entries like "What a Business Line of Credit Is?" - markup that reads as
    # manipulated, which is the risk worth avoiding since Google restricted FAQ
    # rich results to authoritative sites anyway.
    if not question.rstrip().endswith("?"):
        return html

    changed = False
    for sc in soup.find_all("script", type="application/ld+json"):
        raw = sc.string or ""
        if "FAQPage" not in raw:
            continue
        try:
            data = json.loads(raw)
        except Exception:
            continue
        nodes = data if isinstance(data, list) else [data] + list(
            data.get("@graph") or []) if isinstance(data, dict) else []
        for node in nodes:
            if not isinstance(node, dict) or "FAQPage" not in str(node.get("@type", "")):
                continue
            main = node.get("mainEntity")
            if isinstance(main, dict):
                main = [main]
            if not isinstance(main, list):
                main = []
            names = {" ".join(str(q.get("name", "")).split()).lower()
                     for q in main if isinstance(q, dict)}
            if question.lower() in names:
                continue
            main.insert(0, {"@type": "Question", "name": question,
                            "acceptedAnswer": {"@type": "Answer", "text": answer}})
            node["mainEntity"] = main
            changed = True
        if changed:
            sc.string = json.dumps(data, ensure_ascii=False)
            break
    return str(soup) if changed else html


def convert(path: Path, dry=False):
    slug = path.parent.name if path.stem == "index" else path.stem
    src = BACKUP / (page_key(path) + ".html")
    raw = (src if src.exists() else path).read_text(encoding="utf-8")
    s = BeautifulSoup(raw, "html.parser")
    tone = TONE.get(slug) or (equip_tone(slug) if path.parent.parent.name == "equipment" else "blue")

    # ---------- head ----------
    title = s.title.get_text(strip=True)
    desc = s.find("meta", attrs={"name": "description"})
    canon = s.find("link", rel="canonical")
    ogs = [str(t) for t in s.head.find_all("meta", property=True)]
    tws = [str(t) for t in s.head.find_all("meta", attrs={"name": re.compile("^twitter")})]
    icons = [str(t) for t in s.head.find_all("link", rel=lambda r: r and any("icon" in x for x in r))]
    ld = [str(t) for t in s.head.find_all("script", type="application/ld+json")]
    gtm = [str(t) for t in s.head.find_all("script") if "googletagmanager" in str(t) or "dataLayer" in str(t)]

    # ---------- hero ----------
    h1 = s.h1
    hero = h1.find_parent(["div", "section", "header"]) if h1 is not None else None
    if hero is None:
        hero = BeautifulSoup("<div></div>", "html.parser").div   # nothing to lift
    sub = hero.find("p")
    bullets = hero.find("ul")
    eyebrow_src = hero.find(class_=lambda c: has_class(c, "eyebrow", "kicker", "hero-eyebrow"))
    hero_eyebrow = eyebrow_src.get_text(" ", strip=True) if eyebrow_src is not None else ""
    # a hero often carries a stat strip in a second wrapper; it is content, and
    # the v2 hero has nowhere to put it, so it becomes the first band
    hero_extra = ""
    if h1 is not None:
        for sib in hero.find_all(recursive=False):
            if sib is None or sib.find("h1") is not None:
                continue
            txt = " ".join(sib.get_text(" ").split())
            if 6 <= len(txt.split()) <= 80 and not is_button_row(sib):
                he = _clean_styles(copy.copy(sib))
                inner = he.decode_contents().strip()
                hero_extra = ('<section class="section section-tight">\n  <div class="container">\n'
                              '    <div class="group" data-tone="%s">\n'
                              '      <div class="prose">\n        %s\n      </div>\n'
                              '    </div>\n  </div>\n</section>' % (tone, inner))
                break
    ctas = [a for a in hero.select("a") if a.get("href")]
    heroimg = None
    m = re.findall(r"url\((?:&quot;|[\"']?)(/assets/[^)\"';]+)", raw)
    if m:
        heroimg = m[0]
    if not heroimg and slug in HERO_FALLBACK:
        heroimg = HERO_FALLBACK[slug]
    bullet_html = ""
    if bullets:
        lis = "".join("\n        <li><span class=\"tick\">&#10003;</span><span>%s</span></li>"
                      % li.get_text(" ", strip=True) for li in bullets.find_all("li"))
        bullet_html = '\n      <ul class="hero-checks">%s\n      </ul>' % lis
    # Heroes often carry two calls to action - "See if you qualify" plus a
    # calculator. Taking only the first quietly dropped the second, losing the
    # page's only link to /dscr-calculator.html and /mca-calculator.html.
    act = ""
    btns = []
    for a in ctas:
        href = a.get("href") or ""
        if href.startswith(("tel:", "mailto:")):
            continue
        cls = " ".join(a.get("class") or [])
        if "btn" not in cls:
            continue
        if href and not href.startswith(("/", "http", "#")):
            href = "/" + href
        kind = "btn-secondary" if "secondary" in cls else "btn-primary"
        btns.append('<a class="btn %s btn-lg" href="%s">%s</a>' % (kind, href, a.get_text(strip=True)))
    if btns:
        act = ('\n      <div class="actions">\n        %s'
               '\n        <span class="call">Or call <a href="tel:+15612680465">(561)&nbsp;268-0465</a></span>'
               '\n      </div>' % "\n        ".join(btns))
    hero_media = ('\n  <div class="hero-media">\n    <img src="%s" alt="" width="1920" height="1071" '
                  'fetchpriority="high" decoding="async">\n  </div>' % heroimg) if heroimg else ""

    # ---------- body bands ----------
    bands, kinds, band_srcs = [], [], []
    shell = s.find("div", class_="blog-post-shell")
    if shell is not None:
        bands = article_bands(s, shell, tone, slug)
        kinds = ["body"] * len(bands)
    for i, sec in enumerate([] if shell is not None
                            else split_multi_heading(content_blocks(s))):
        h2 = sec.find("h2")
        if not h2:
            continue
        head = " ".join(h2.get_text().split())
        # the generic trust band ("The Axiant Advantage": 20+ / $0 / 1 / U.S.)
        # is dropped on the owner's instruction
        if "axiant advantage" in head.lower() or "trust-band" in " ".join(sec.get("class") or []):
            continue
        alt = False
        pr = prose_html(sec)
        pr_raw = pr
        pr = cards_from_feature_list(tiles_from_list(table_from_amount_list(pr))) if pr else pr
        pr_block = render_prose(pr)
        extra = cta_html(sec)

        stats = sec.select(".trust-stat")
        tband = sec.select(".trust-band-item")
        bens = sec.select(".benefit-card")
        svcs = sec.select(".service-card")
        steps = sec.select(".step-card")
        posts = sec.select(".relevant-post-card")
        calc = sec.select_one(".ic-wrap, .calc-grid, .calc-out")
        h4s = sec.find_all("h4", recursive=False)

        if "quick answer" in head.lower():
            # the quick answer stays a compact list: it is the block an answer
            # engine lifts, and breaking it into cards defeats that
            band_srcs.append(sec); kinds.append('quick'); inner_all = "".join(str(c) for c in sec.find_all(recursive=False)
                                if getattr(c, "name", None) not in ("h2", "script")
                                and not is_button_row(c))
            bands.append(band(head, '      <div class="callout">\n        <div class="prose">\n          %s\n        </div>\n      </div>' % inner_all, alt, extra, tone))
        elif tband:
            tiles = []
            for n, b in enumerate(tband):
                k = b.select_one(".trust-band-num"); l = b.select_one(".trust-band-label")
                kt = k.get_text(strip=True) if k else ""
                lt = l.get_text(strip=True) if l else ""
                tiles.append('        <div class="stat" data-tone="%s"><span class="stat-icon">%s</span>'
                             '<span class="stat-body"><span class="stat-key">%s</span>'
                             '<span class="stat-label">%s</span></span></div>'
                             % (TILE_TONES[n % 5], pick_icon(kt + " " + lt), kt, lt))
            band_srcs.append(sec); kinds.append('body'); bands.append(band(head, pr_block + '      <div class="stats">\n%s\n      </div>' % "\n".join(tiles), alt, extra, tone))
        elif stats:
            tiles = []
            for n, t_ in enumerate(stats):
                k = t_.select_one(".trust-stat-number"); l = t_.select_one(".trust-stat-label")
                kt = k.get_text(strip=True) if k else ""
                lt = l.get_text(strip=True) if l else ""
                tiles.append('        <div class="stat" data-tone="%s"><span class="stat-icon">%s</span>'
                             '<span class="stat-body"><span class="stat-key">%s</span>'
                             '<span class="stat-label">%s</span></span></div>'
                             % (TILE_TONES[n % 5], pick_icon(kt + " " + lt), kt, lt))
            band_srcs.append(sec); kinds.append('body'); bands.append(band(head, pr_block + '      <div class="stats">\n%s\n      </div>' % "\n".join(tiles), alt, extra, tone))
        elif bens:
            cs = []
            for b in bens:
                pic = b.find("picture") or b.find("img")
                media = ('        <div class="card-media">%s</div>\n' % str(pic)) if pic else ""
                h3 = b.find("h3"); p = b.find("p")
                cs.append(card(card_head(b), card_body(b), media=media,
                               tone=TILE_TONES[len(cs) % 5]))
            band_srcs.append(sec); kinds.append('body'); bands.append(band(head, pr_block + '      <div class="cards cards-left">\n%s\n      </div>' % "\n".join(cs), alt, extra, tone))
        elif svcs:
            cs = [card(card_head(c), card_body(c), tone=TILE_TONES[n % 5],
                       icon=product_icon(card_head(c) + " " + card_body(c)[:120]))
                  for n, c in enumerate(svcs)]
            band_srcs.append(sec); kinds.append('body'); bands.append(band(head, pr_block + '      <div class="cards cards-left">\n%s\n      </div>' % "\n".join(cs), alt, extra, tone))
        elif steps:
            cs = []
            for n, c in enumerate(steps):
                num = c.select_one(".step-number"); h3 = c.find("h3"); p = c.find("p")
                cs.append(card(card_head(c), card_body(c), tone=STEP_TONES[n % 4],
                               eyebrow=num.get_text(strip=True) if num else str(n + 1)))
            band_srcs.append(sec); kinds.append('body'); bands.append(band(head, pr_block + '      <div class="cards cards-left">\n%s\n      </div>' % "\n".join(cs), alt, extra, tone))
        elif posts:
            cs = []
            for a in posts:
                link = a.select_one("h3 a") or a.find("a")
                p = a.find("p")
                href = link.get("href") if link else "#"
                if href and not href.startswith(("/", "http")):
                    href = "/" + href
                cs.append(card(link.get_text(strip=True) if link else "",
                               p.decode_contents().strip() if p else "", href=href,
                               tone=TILE_TONES[len(cs) % 5],
                               cta='      <span class="card-cta">Read &rarr;</span>\n'))
            band_srcs.append(sec); kinds.append('body'); bands.append(band(head, pr_block + '      <div class="cards">\n%s\n      </div>' % "\n".join(cs), alt, extra, tone))
        elif (("faq" in head.lower() or "frequently asked" in head.lower()
               or sec.find("div", class_=lambda c: c and "faq-list" in c))
              and len(faq_pairs(sec)) >= 3):
            faq = "\n".join('        <details>\n          <summary>%s</summary>\n'
                            '          <div class="answer">%s</div>\n        </details>' % pr
                            for pr in faq_pairs(sec))
            band_srcs.append(sec); kinds.append('faq')
            bands.append(band(head, '      <div class="faq">\n%s\n      </div>' % faq, alt, extra, tone))
        elif h4s and len(h4s) >= 3:
            pairs, cur = [], None
            for ch in sec.find_all(recursive=False):
                if ch.name == "h4":
                    cur = ch.get_text(strip=True)
                elif ch.name == "p" and cur:
                    pairs.append((cur, ch.decode_contents().strip())); cur = None
            faq = "\n".join('        <details>\n          <summary>%s</summary>\n'
                            '          <div class="answer"><p>%s</p></div>\n        </details>' % p for p in pairs)
            band_srcs.append(sec); kinds.append('faq'); bands.append(band(head, '      <div class="faq">\n%s\n      </div>' % faq, alt, extra, tone))
        elif calc:
            # keep the widget exactly as it is - it is driven by an inline
            # script and rebuilding it would break the numbers
            # The explanatory sentence belongs above the instrument, on the
            # light band, not inside the navy console - it reads better there
            # and it stops one caption fighting the generic .card > p colour.
            intro = ""
            keep_nodes = []
            for c in sec.find_all(recursive=False):
                nm = getattr(c, "name", None)
                cls = c.get("class") or []
                if nm in ("h2", "script") or "section-cta" in cls:
                    continue
                if nm == "p" and "sub" in cls and not intro:
                    intro = '      <div class="prose">\n        <p>%s</p>\n      </div>\n' % c.decode_contents().strip()
                    continue
                keep_nodes.append(c)
            keep = "".join(str(c) for c in keep_nodes)
            # The inline script wires itself with querySelectorAll('.inline-calc')
            # (and '.calc' elsewhere), so the widget's own wrapper classes have to
            # survive or the estimator silently renders $0 forever.
            hooks = " ".join(c for c in (sec.get("class") or [])
                             if c not in ("about-section",))
            band_srcs.append(sec); kinds.append('calc'); bands.append(band(head, intro + '      <div class="card %s">%s</div>' % (hooks, keep), alt, extra, tone))
        else:
            pic = next((x for x in sec.find_all(["picture", "img"]) if usable_pic(x)), None)
            egrid = sec.find("div", class_="industry-equipment-grid")
            has_grid = ('class="cards' in pr) or ('class="tiles"' in pr)
            if egrid is not None and equip_cards(egrid):
                lead = "".join("<p>%s</p>" % c.decode_contents().strip()
                               for c in sec.find_all("p", recursive=False)
                               if c.get_text(strip=True) and not is_button_row(c))
                inner = (('      <div class="prose">\n        %s\n      </div>\n' % lead) if lead else "") \
                        + "      " + equip_cards(egrid)
            elif pic and not in_component(pic) and has_grid:
                inner = ('      <div class="split split-media">\n'
                         '        <div class="prose-figure">%s</div>\n'
                         '        <div class="media-col">\n%s        </div>\n'
                         '      </div>' % (str(pic), pr_block))
            elif pic and not in_component(pic) and pr and not has_grid:
                inner = ('      <div class="split">\n        <div class="prose">\n          %s\n        </div>\n'
                         '        <div class="prose-figure">%s</div>\n      </div>' % (pr, str(pic)))
            else:
                fig = ('      <div class="prose-figure">%s</div>\n' % str(pic)) if pic and not in_component(pic) else ""
                inner = fig + pr_block.rstrip()
            band_srcs.append(sec); kinds.append('body'); bands.append(band(head, inner, alt, extra, tone))

    # --- article hub --------------------------------------------------------
    # The /articles/ hubs are a hero, an intro line and a grid of 47 cards -
    # not one <h2> on the page, so the block walk above finds nothing at all.
    # Bands here carry no heading of their own: the hero already names the page
    # and inventing section titles would be writing copy.
    hub_used = []
    grid = s.find("div", class_="blog-grid")
    if grid is not None and not bands:
        def plain(inner_html):
            return ('<section class="section">\n  <div class="container">\n'
                    '    <div class="group" data-tone="%s">\n%s\n    </div>\n'
                    '  </div>\n</section>' % (tone, inner_html))
        lead, lead_srcs = "", []
        hub_wrap = grid.parent
        for el in hub_wrap.find_all(recursive=False):
            if el is grid or getattr(el, "name", None) is None:
                continue
            cls = " ".join(el.get("class") or [])
            if "services-cta" in cls or not el.get_text(strip=True):
                continue
            if el.name == "p":
                if "blog-back" in cls:
                    # drop the legacy btn classes: as an outlined button over
                    # body copy it reads as a stray control, not a breadcrumb
                    back = BeautifulSoup(el.decode_contents().strip(), "html.parser")
                    for a_el in back.find_all("a"):
                        a_el.attrs.pop("class", None)
                    lead += '        <p class="hub-back">%s</p>\n' % str(back)
                else:
                    lead += '        <p class="lead">%s</p>\n' % el.decode_contents().strip()
            else:
                inner = el.decode_contents().strip()
                lead += "        %s\n" % (inner if inner.lstrip().startswith("<")
                                           else "<p>%s</p>" % inner)
            lead_srcs.append(el)
        hub_used.extend(lead_srcs)
        if lead:
            band_srcs.append(lead_srcs[0]); kinds.append("body")
            bands.append(plain('      <div class="prose">\n%s      </div>' % lead)
                         .replace('<section class="section">',
                                  '<section class="section section-tight">', 1))
        cs = []
        for n, art in enumerate(grid.find_all("article", class_="blog-card")):
            # NB: local names here must not collide with convert()'s own
            # `title`/`desc`/`canon` - shadowing the page title wrote a card's
            # markup into <title> on the first run.
            c_link = art.find("a", href=True)
            c_head = art.find(["h3", "h4"])
            c_body = art.find("p")
            c_more = art.find("a", class_="blog-card-link")
            c_img = art.find("img")
            cs.append(card(c_head.get_text(" ", strip=True) if c_head else "",
                           c_body.decode_contents().strip() if c_body else "",
                           tone=TILE_TONES[n % 5],
                           media=('      <div class="card-media">%s</div>\n' % str(c_img))
                                 if c_img is not None else "",
                           href=c_link["href"] if c_link else "#",
                           cta='      <span class="card-cta">%s</span>\n'
                               % (c_more.get_text(" ", strip=True) if c_more else "Read more")))
        if cs:
            band_srcs.append(grid); kinds.append("body")
            bands.append(plain('      <div class="cards cards-left">\n%s\n      </div>'
                               % "\n".join(cs)))

    # --- content guard --------------------------------------------------
    # Unknown component markup (contractor-financing's .industry-equipment-grid,
    # for one) is invisible to the extractors above: its copy lives in divs and
    # bare anchors, so prose_html walks past it and the band ships nearly empty.
    # Where a band captured much less than its source block, fall back to that
    # block's own markup. Plainer, but nothing is lost.
    def _words(html):
        return len(" ".join(BeautifulSoup(html, "html.parser").get_text(" ").split()).split())

    for n, sec in enumerate(band_srcs):
        want = _words(str(sec))
        got = _words(bands[n])
        if want >= 40 and got < want * 0.85:
            kept = BeautifulSoup("<div id='__k'></div>", "html.parser")
            holder = kept.find(id="__k")
            for c in sec.find_all(recursive=False):
                if getattr(c, "name", None) in ("h2", "script") or is_button_row(c):
                    continue
                holder.append(copy.copy(c))
            # buttons are emitted as the CTA row; leaving them in the verbatim
            # fallback puts a loose button in the middle of a paragraph block
            for a in holder.find_all("a"):
                if is_button(a):
                    a.decompose()
            for d in holder.find_all(["div", "p"]):
                if not d.get_text(strip=True) and not d.find(["img", "picture", "iframe", "input"]):
                    d.decompose()
            keep = holder.decode_contents()
            head = " ".join(sec.find("h2").get_text().split()) if sec.find("h2") else ""
            bands[n] = band(head, '      <div class="prose">\n        %s\n      </div>' % keep,
                            False, cta_html(sec), tone)

    # --- style every table -------------------------------------------------
    # A table nested inside a div or a paragraph never reached the wrapper, so
    # it shipped as unstyled text columns: no navy header, no rules, no zebra.
    # Any table that is not already wrapped gets wrapped, at any depth.
    for n, b in enumerate(bands):
        if "<table" not in b:
            continue
        bs = BeautifulSoup(b, "html.parser")
        wrapped = False
        for tbl in bs.find_all("table"):
            if tbl.find_parent(class_="table-wrap"):
                continue
            holder = bs.new_tag("div")
            holder["class"] = ["table-wrap"]
            tbl.wrap(holder)
            wrapped = True
        if wrapped:
            bands[n] = str(bs)

    # --- label table cells for the phone -----------------------------------
    # A three-column table cannot fit a 360px screen, so on phones each row
    # stacks and every cell shows its column name. That needs the name on the
    # cell itself; it changes no text, only adds an attribute.
    for n, b in enumerate(bands):
        if "<table" not in b:
            continue
        bs = BeautifulSoup(b, "html.parser")
        changed = False
        for tbl in bs.find_all("table"):
            head = tbl.find("thead")
            names = [" ".join(c.get_text(" ").split())
                     for c in (head.find_all(["th", "td"]) if head else [])]
            if not names:
                first = tbl.find("tr")
                names = [" ".join(c.get_text(" ").split())
                         for c in (first.find_all("th") if first else [])]
            if not names:
                continue
            for row in tbl.find_all("tr"):
                cells = row.find_all(["td", "th"])
                for i, cell in enumerate(cells):
                    if cell.name == "td" and i < len(names) and names[i]:
                        cell["data-label"] = names[i]
                        changed = True
        if changed:
            bands[n] = str(bs)

    # --- strip legacy inline presentation ---------------------------------
    # The old pages styled odd lines by hand (text-align:center, font-weight,
    # hand-set margins). Carried into a v2 band those fight the stylesheet -
    # a centred bold line above left-aligned cards, wrapping mid-link. The
    # widget markup keeps its own styles: its script positions by them.
    # NB: display and visibility are behaviour, not decoration. Stripping
    # style="display:none" un-hid contact.html's "Thank you for contacting us"
    # panel, which then showed above the form on every visit.
    PRESO = ("text-align", "font-weight", "font-size", "font-family", "color",
             "background", "margin", "padding", "border", "letter-spacing",
             "line-height", "text-transform", "text-decoration")
    for n, b in enumerate(bands):
        if "style=" not in b:
            continue
        bs = BeautifulSoup(b, "html.parser")
        touched = False
        for el in bs.find_all(style=True):
            if el.find_parent(class_=lambda c: c and ("calc" in c or "inline-calc" in c)):
                continue
            keep = [d for d in el["style"].split(";")
                    if d.strip() and not d.split(":")[0].strip().lower().startswith(PRESO)]
            if len(keep) != len(el["style"].split(";")):
                touched = True
            if keep:
                el["style"] = ";".join(x.strip() for x in keep)
            else:
                del el["style"]
        if touched:
            bands[n] = str(bs)

    # --- drop dead images -------------------------------------------------
    # A zero-byte asset renders as a broken-image icon. Remove the element so
    # the band reads as prose (and picks up the placeholder panel below).
    for n, b in enumerate(bands):
        if "<img" not in b:
            continue
        bs = BeautifulSoup(b, "html.parser")
        gone = False
        for el in bs.find_all(["picture", "img"]):
            if el.parent is None or el.find_parent("picture"):
                continue
            if not usable_pic(el):
                holder = el.find_parent(class_="prose-figure") or el
                holder.decompose(); gone = True
        if gone:
            for sp in bs.find_all("div", class_="split"):
                kids = [c for c in sp.find_all(recursive=False)]
                if len(kids) == 1 and "prose" in (kids[0].get("class") or []):
                    sp.replace_with(kids[0])
            bands[n] = str(bs)

    # --- decorative aside ------------------------------------------------
    # A long prose-only band leaves the right half of its row empty. Give it
    # the section's own symbol on a hatched panel. This runs after the guard
    # so bands that fell back to verbatim markup are decorated too.
    CTA_CLS = {"section-cta", "cta-actions", "cta-actions-left"}
    eligible = []
    for n, b in enumerate(bands):
        bs = BeautifulSoup(b, "html.parser")
        grp = bs.find("div", class_="group")
        if not grp:
            continue
        body = [c for c in grp.find_all(recursive=False)
                if getattr(c, "name", None)
                and "group-head" not in (c.get("class") or [])
                and not CTA_CLS & set(c.get("class") or [])]
        if len(body) != 1:
            continue
        only = body[0]
        if "prose" not in (only.get("class") or []):
            continue
        if only.find(["img", "picture", "table", "details", "iframe", "input"]):
            continue
        if only.find(class_=["cards", "tiles", "callout", "faq", "split",
                             "card", "aside-mark", "prose-figure"]):
            continue
        if len(only.get_text(" ").split()) < 110:
            continue
        eligible.append((len(only.get_text(" ").split()), n))
        continue

    # Six identical panels down one page reads as a template, not a design.
    # Keep the two longest - the bands with the most empty column to fill.
    for _, n in sorted(eligible, reverse=True)[:2]:
        bs = BeautifulSoup(bands[n], "html.parser")
        grp = bs.find("div", class_="group")
        only = [c for c in grp.find_all(recursive=False)
                if getattr(c, "name", None)
                and "group-head" not in (c.get("class") or [])
                and not CTA_CLS & set(c.get("class") or [])][0]
        h2 = grp.find("h2")
        wrap = BeautifulSoup(
            '<div class="split"><div class="aside-mark" aria-hidden="true">%s</div></div>'
            % product_icon(h2.get_text(" ", strip=True) if h2 else ""), "html.parser")
        sp = wrap.find("div", class_="split")
        only.insert_before(sp)
        sp.insert(0, only.extract())
        bands[n] = str(bs)

    # --- stray quick answer ---------------------------------------------
    # Some pages carry a .quick-answer box that belongs to no h2 block, so the
    # block walk above never sees it. Promote it to the page's quick answer.
    if shell is None and not any(k == "quick" for k in kinds):
        qa = s.find("div", class_="quick-answer")
        if qa is not None and not any(qa in b.descendants for b in band_srcs):
            qc = copy.copy(qa)
            label = qc.find("strong")
            if label is not None:
                label.decompose()
            for el in qc.find_all(True):
                el.attrs.pop("style", None)
            inner = qc.decode_contents().strip()
            if len(" ".join(qc.get_text(" ").split()).split()) >= 25:
                band_srcs.append(qa); kinds.append("quick")
                bands.append(band("Quick Answer",
                                  '      <div class="callout">\n        <div class="prose">\n'
                                  '          %s\n        </div>\n      </div>' % inner,
                                  False, "", TONE.get(slug, "blue")))

    # --- stray closing cta ------------------------------------------------
    # The equipment guides end with a .services-cta block: an h3, a sentence
    # and a button, owned by no h2. The block walk never saw it, so every one
    # of those pages was quietly dropping its closing pitch.
    for node in ([] if shell is not None else
                 s.find_all(class_=lambda c: c and "services-cta" in c)):
        if any(node in b.descendants for b in band_srcs if hasattr(b, "descendants")):
            continue
        h3 = node.find(["h2", "h3", "h4"])
        body = "".join(str(c) for c in node.find_all(["p", "ul"], recursive=False)
                       if c.get_text(strip=True) and not is_button_row(c))
        if not body:
            continue
        band_srcs.append(node); kinds.append("body")
        bands.append(band(" ".join(h3.get_text(" ").split()) if h3 else "Get Started",
                          '      <div class="prose">\n        %s\n      </div>' % body,
                          False, cta_html(node), TONE.get(slug) or "blue"))

    # --- orphan note --------------------------------------------------------
    # medical-imaging keeps a two-link disambiguation note in a bare div that
    # no <h2> owns, so the block walk dropped it. It ships as a heading-less
    # band at its own place in the page: inventing an <h2> for it would be
    # writing copy, and appending it to the end would read as an afterthought.
    wrap = s.find("div", class_="form-container") or s.find("div", class_="ef-page-wrap")
    if wrap is not None:
        for node in wrap.find_all("div", recursive=False):
            if in_component(node) or node.find(["h1", "h2", "h3", "h4", "section", "table"]):
                continue
            if any(node is b or b in node.descendants for b in band_srcs
                   if hasattr(b, "descendants")):
                continue
            if any(node is x for x in hub_used):
                continue
            txt = " ".join(node.get_text(" ").split())
            if not (15 <= len(txt.split()) <= 90) or len(node.find_all("a")) < 2:
                continue
            body = node.decode_contents().strip()
            if not body.lstrip().startswith("<"):
                body = "<p>%s</p>" % body
            at = sum(1 for b in band_srcs
                     if hasattr(b, "parent") and b in node.find_all_previous())
            band_srcs.insert(at, node); kinds.insert(at, "body")
            bands.insert(at,
                '<section class="section">\n  <div class="container">\n'
                '    <div class="group" data-tone="%s">\n'
                '      <div class="prose">\n        %s\n      </div>\n'
                '    </div>\n  </div>\n</section>' % (TONE.get(slug) or "blue", body))

    # --- orphan blocks ------------------------------------------------------
    # Content that belongs to no <h2> is invisible to the block walk: the
    # article template's <div class="answer"> lead and its closing disclaimer,
    # for two. Emit each as a heading-less band at its own place in the page -
    # inventing a heading would be writing copy. Deliberately narrow: only
    # direct children of the content wrap, never something already banded.
    if shell is None and bands:
        wrap = (s.find("main") or s.find("div", class_="form-container")
                or s.find("div", class_="wrap"))
        picked = [b for b in band_srcs if hasattr(b, "descendants")]
        picked += [n for n in hub_used if hasattr(n, "descendants")]
        if grid is not None:
            picked.append(grid)
        if wrap is not None:
            extra_bands = []
            for node in wrap.find_all(recursive=False):
                if getattr(node, "name", None) is None or node.name in ("script", "style"):
                    continue
                if _is_chrome(node) or in_component(node) or is_button_row(node):
                    continue
                if any(node is b or b in node.descendants or node in b.descendants
                       for b in picked):
                    continue
                txt = " ".join(node.get_text(" ").split())
                if len(txt.split()) < 12:
                    continue
                if node.find(["h2"]):
                    continue
                nd = _clean_styles(copy.copy(node))
                inner = nd.decode_contents().strip() if nd.name in ("div", "section") else str(nd)
                if not inner.lstrip().startswith("<"):
                    inner = "<p>%s</p>" % inner
                at = sum(1 for b in picked if b in node.find_all_previous())
                extra_bands.append((at, node,
                    '<section class="section">\n  <div class="container">\n'
                    '    <div class="group" data-tone="%s">\n'
                    '      <div class="prose">\n        %s\n      </div>\n'
                    '    </div>\n  </div>\n</section>' % (tone, inner)))
            for offset, (at, node, html) in enumerate(extra_bands):
                idx = min(at + offset, len(bands))
                bands.insert(idx, html); kinds.insert(idx, "body"); band_srcs.insert(idx, node)

    # --- document fallback --------------------------------------------------
    # privacy-policy, terms and vendors have no section blocks to band up. They
    # are documents: give them the chrome, one prose column at a readable
    # measure, and leave the copy exactly as written.
    if not bands:
        wrap = (s.find("div", class_="form-container") or s.find("div", class_="wrap")
                or s.find("main") or s.find("div", class_="container"))
        if wrap is not None:
            doc = copy.copy(wrap)
            for junk in doc.find_all(["nav", "footer", "script", "style"]):
                junk.decompose()
            for el in doc.find_all(class_=lambda c: has_class(
                    c, "main-nav", "site-footer", "mobile-cta-bar", "mobile-nav-overlay",
                    "nav-links", "breadcrumb")):
                el.decompose()
            for hx in doc.find_all("h1"):
                hx.decompose()                      # the hero already carries it
            _clean_styles(doc)
            # map the legacy grid/card classes onto the v2 vocabulary so a
            # document page's cards are styled rather than bare divs
            for grid in doc.find_all(class_=lambda c: has_class(
                    c, "lenders-grid", "cards-grid", "vendor-grid")):
                for kid in grid.find_all(recursive=False):
                    kid["class"] = ["card"]
                grid["class"] = ["cards", "cards-left"]
            for a_el in doc.find_all("a"):
                if is_button(a_el) or has_class(a_el.get("class"), "btn-primary", "btn-secondary"):
                    a_el["class"] = ["btn"]
            inner = doc.decode_contents().strip()
            if len(" ".join(doc.get_text(" ").split()).split()) >= 3:
                bands.append(
                    '<section class="section">\n  <div class="container">\n'
                    '    <div class="group" data-tone="%s">\n'
                    '      <div class="prose prose-doc">\n        %s\n      </div>\n'
                    '    </div>\n  </div>\n</section>' % (tone, inner))
                kinds.append("body")

    # --- order ---------------------------------------------------------
    # The quick answer opens the page: it is the summary a reader and an
    # answer engine both want first. The estimator is a tool, not an
    # introduction - it belongs after the explanation, just ahead of the FAQ.
    order = list(range(len(bands)))
    def move(idx, to):
        order.remove(idx); order.insert(to, idx)
    q = next((i for i, k in enumerate(kinds) if k == "quick"), None)
    if q is not None:
        move(q, 0)
    c = next((i for i, k in enumerate(kinds) if k == "calc"), None)
    if c is not None:
        f = next((i for i, k in enumerate(kinds) if k == "faq"), None)
        dest = order.index(f) if f is not None else max(len(order) - 2, 0)
        if order.index(c) < dest:
            dest -= 1
        move(c, dest)
    bands = [bands[i] for i in order]

    # stripe after ordering, so the bands still alternate
    # the hero strip is a band like any other: outside the sequence it left two
    # untinted sections stacked at the top of every page
    if hero_extra:
        bands.insert(0, hero_extra)
        hero_extra = ""
    bands = [re.sub(r'<section class="section((?: [^"]*)?)"',
                    r'<section class="section section-alt\1"', b, count=1)
             if n % 2 == 1 else b for n, b in enumerate(bands)]

    # Keep any inline script that drives the preserved widget. Matching only
    # "ic-" missed the other calculator family entirely (it binds by id -
    # feAmt/fePay), which shipped a widget showing a static number that never
    # updated. Collect the hooks the kept markup actually contains, then keep
    # every source script that references one.
    kept_markup = "".join(b for b in bands if "inline-calc" in b or 'class="card calc' in b)
    hooks = set(re.findall(r'id="([A-Za-z][\w-]*)"', kept_markup))
    hooks |= {c for c in re.findall(r'class="([^"]+)"', kept_markup)
              for c in c.split() if c.startswith(("ic-", "calc-"))}
    inline_calc = []
    for sc in s.find_all("script"):
        if sc.get("src"):
            continue
        body = sc.get_text()
        if any(h in body for h in hooks) or "ic-amount" in body:
            inline_calc.append(str(sc))

    header = (ROOT / "_components" / "header-v2.html").read_text(encoding="utf-8").strip()
    # "Financing program" is right for a program, industry or equipment page and
    # wrong on contact, vendors or a policy page. Use the page's own eyebrow when
    # it has one, "Guide" for an article, and nothing at all otherwise.
    if hero_eyebrow:
        _eyebrow = hero_eyebrow
    elif shell is not None:
        _eyebrow = "Guide"
    elif slug in PROGRAMS or slug in INDUSTRIES or path.parent.parent.name == "equipment":
        _eyebrow = "Financing program"
    else:
        _eyebrow = ""
    eyebrow_html = ('<p class="eyebrow">%s</p>' % _eyebrow) if _eyebrow else ""
    footer = (ROOT / "_components" / "footer-v2.html").read_text(encoding="utf-8").strip()
    nl = "\n"
    preload = ('<link rel="preload" href="%s" as="image" type="image/webp">\n' % heroimg) if heroimg else ""

    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="dns-prefetch" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="theme-color" content="#0d1f3c">
{nl.join(gtm)}
{str(desc) if desc else ''}
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
{str(canon) if canon else ''}
{nl.join(ogs)}
{nl.join(tws)}
<title>{title}</title>
{nl.join(icons)}
{preload}{nl.join(ld)}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/axiant-v2.css?v={VERSION}">
</head>
<body>
{header}

<section class="hero-compact">{hero_media}
  <div class="container">
    <div class="inner">
      {eyebrow_html}
      <h1>{h1.get_text(strip=True)}</h1>
      <p class="lede">{sub.get_text(" ", strip=True) if sub else ""}</p>{bullet_html}{act}
    </div>
  </div>
</section>

{hero_extra}
{nl.join(bands)}

{footer}
{nl.join(inline_calc)}
{'<script src="/article-toc.js?v=%s" defer></script>' % VERSION if shell is not None else ""}
<script src="/language-switcher.js?v={VERSION}" defer></script>
<script src="/script.js?v={VERSION}" defer></script>
</body>
</html>
"""
    out = fix_broken_apostrophes(out)
    out = inject_quick_answer_schema(out)
    if dry:
        print("  [dry] %s -> %d bands, %d bytes" % (path.name, len(bands), len(out)))
        return
    BACKUP.mkdir(exist_ok=True)
    if not (BACKUP / (page_key(path) + ".html")).exists():
        shutil.copy2(path, BACKUP / (page_key(path) + ".html"))
    path.write_text(out, encoding="utf-8")
    print("  %-34s %d bands  %d->%d bytes  tone=%s" % (path.name, len(bands), len(raw), len(out), tone))


def main():
    dry = "--dry-run" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--articles" in sys.argv:
        names = article_pages()
    elif "--equipment" in sys.argv:
        names = ["equipment/%s/index.html" % e for e in EQUIPMENT]
    elif "--industries" in sys.argv:
        names = [n + ".html" for n in INDUSTRIES]
    elif "--all" in sys.argv:
        names = ([n + ".html" for n in PROGRAMS + INDUSTRIES]
                 + ["equipment/%s/index.html" % e for e in EQUIPMENT])
    else:
        names = args
    if not names:
        print(__doc__); return 1
    for n in names:
        p = ROOT / n
        if not p.exists():
            print("  MISSING (not built yet): %s" % n); continue
        try:
            convert(p, dry)
        except Exception as e:
            print("  !! %-40s %s: %s" % (p, type(e).__name__, e))
    print("\nnow run:  python scripts/audit-page-parity.py " + " ".join(names))
    return 0


if __name__ == "__main__":
    sys.exit(main())
