#!/usr/bin/env python3
"""Insert missing cluster service-page links + cross-cluster links into article bodies.

Only operates on the <main class="blog-post-main"> region. Two passes:

1. Cluster service-page link: for each article whose body has no <a href>
   pointing at its own cluster's service page (/<cluster>.html), find the
   first naked text mention of the cluster's display phrase ("SBA loan",
   "equipment financing", etc.) and wrap it in a link.

2. Cross-cluster authority link: for each article still missing a link to
   another cluster's service or article surface, insert a contextual sentence
   referencing a relevant sibling cluster as the last paragraph of the body
   (before any closing CTA card or Related Resources block).

Run: python scripts/fix_internal_links.py [--dry-run]
"""
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent.parent

# Cluster -> primary display phrases (longest-first for greedy matching).
# Each entry is a list of phrases; the script tries them in order and uses
# the first one it finds in the article body.
CLUSTER_PHRASES = {
    "sba-loans": ["SBA 7(a) loan", "SBA 7(a)", "SBA loans", "SBA loan", "SBA"],
    "equipment-financing": ["equipment financing", "equipment loan", "equipment finance"],
    "business-line-of-credit": ["business line of credit", "line of credit"],
    "working-capital-loans": ["working capital loan", "working capital"],
    "business-term-loans": ["business term loan", "term loan"],
    "commercial-real-estate-loans": ["commercial real estate loan", "CRE loan", "commercial real estate"],
    "commercial-bridge-loans": ["commercial bridge loan", "bridge loan"],
    "fix-and-flip": ["fix-and-flip loan", "fix and flip loan", "fix-and-flip", "fix and flip"],
    "revenue-based-financing": ["revenue-based financing", "revenue based financing", "RBF"],
    "securities-based-lending": ["securities-based lending", "securities based lending", "SBL"],
    "merchant-cash-advance": ["merchant cash advance", "MCA"],
    "startup-financing": ["startup financing", "startup loan"],
}

CLUSTERS = set(CLUSTER_PHRASES.keys())

# Cross-cluster suggestion map: when an article has NO cross-cluster link,
# we add a contextual sentence referencing the sibling cluster (key) listed
# below. The link text uses the sibling cluster's first display phrase.
CROSS_CLUSTER_SIBLING = {
    "sba-loans": ("equipment-financing", "Equipment financing often closes faster than SBA when speed matters."),
    "equipment-financing": ("working-capital-loans", "Working capital loans cover soft costs equipment financing typically won't."),
    "business-line-of-credit": ("working-capital-loans", "Working capital loans suit one-time needs a line of credit can't carry."),
    "working-capital-loans": ("business-line-of-credit", "A business line of credit is the recurring counterpart for ongoing cash gaps."),
    "business-term-loans": ("sba-loans", "SBA loans often beat conventional term loans on rate when timing allows."),
    "commercial-real-estate-loans": ("sba-loans", "SBA 504 is often the cheapest commercial real estate path for owner-occupied properties."),
    "commercial-bridge-loans": ("commercial-real-estate-loans", "A permanent commercial real estate loan typically takes out the bridge once seasoning is met."),
    "fix-and-flip": ("commercial-bridge-loans", "A commercial bridge loan can replace fix-and-flip financing on larger deals."),
    "revenue-based-financing": ("merchant-cash-advance", "Merchant cash advances are RBF's closest cousin and often cheaper for short-term gaps."),
    "securities-based-lending": ("business-line-of-credit", "A business line of credit avoids the margin-call risk that comes with securities-based lending."),
    "merchant-cash-advance": ("revenue-based-financing", "Revenue-based financing is usually the cleaner alternative to an MCA for businesses with steady recurring revenue."),
    "startup-financing": ("sba-loans", "SBA 7(a) is one of the few startup-eligible loan products with reasonable rates."),
}

# Display phrase used for the cross-cluster link anchor.
CROSS_LINK_ANCHOR = {c: phrases[0] for c, phrases in CLUSTER_PHRASES.items()}

MAIN_RX = re.compile(r'(<main\b[^>]*class="[^"]*\bblog-post-main\b[^"]*"[^>]*>)(.*?)(</main>)', re.DOTALL | re.IGNORECASE)
A_OPEN_RX = re.compile(r'<a\b[^>]*>', re.IGNORECASE)
A_CLOSE_RX = re.compile(r'</a>', re.IGNORECASE)
HREF_RX = re.compile(r'<a\b[^>]*\bhref="([^"]+)"', re.IGNORECASE)
NAV_RX = re.compile(r'<nav\b[^>]*>.*?</nav>', re.DOTALL | re.IGNORECASE)
HEADER_RX = re.compile(r'<header\b[^>]*>.*?</header>', re.DOTALL | re.IGNORECASE)
FOOTER_RX = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL | re.IGNORECASE)

def cluster_for_path(rel_path: str):
    parts = rel_path.split("/")
    if len(parts) >= 3 and parts[1] == "articles" and parts[0] in CLUSTERS:
        return parts[0]
    return None

def normalize_href(href: str) -> str:
    h = href.strip()
    if h.startswith("https://axiantpartners.com"):
        h = h[len("https://axiantpartners.com"):]
    if h.startswith("http://axiantpartners.com"):
        h = h[len("http://axiantpartners.com"):]
    if not h.startswith("/"):
        h = "/" + h
    return h.split("#")[0].split("?")[0]

def link_target_cluster(href: str):
    h = normalize_href(href)
    if h.endswith(".html"):
        slug = h[1:-len(".html")]
        if slug in CLUSTERS:
            return slug
    parts = h.strip("/").split("/")
    if parts and parts[0] in CLUSTERS:
        return parts[0]
    return None

def has_link_to(body_for_link_check: str, target_path: str) -> bool:
    for href in HREF_RX.findall(body_for_link_check):
        if normalize_href(href) == target_path:
            return True
    return False

def has_cross_cluster_link(body_for_link_check: str, own_cluster: str) -> bool:
    for href in HREF_RX.findall(body_for_link_check):
        c = link_target_cluster(href)
        if c and c != own_cluster:
            return True
    return False

def find_anchor_open_close_ranges(body: str):
    """Return list of (start, end) byte ranges that are inside <a>...</a>."""
    ranges = []
    pos = 0
    while True:
        m_open = A_OPEN_RX.search(body, pos)
        if not m_open:
            break
        m_close = A_CLOSE_RX.search(body, m_open.end())
        if not m_close:
            break
        ranges.append((m_open.start(), m_close.end()))
        pos = m_close.end()
    return ranges

def position_inside_ranges(idx: int, ranges) -> bool:
    for s, e in ranges:
        if s <= idx < e:
            return True
    return False

def insert_cluster_service_link(body: str, own_cluster: str, dry: bool):
    """Wrap the first plain-text occurrence of a cluster phrase in an <a> link.
    Returns (new_body, changed: bool, info: str).
    """
    target = f"/{own_cluster}.html"
    a_ranges = find_anchor_open_close_ranges(body)

    for phrase in CLUSTER_PHRASES[own_cluster]:
        # Match phrase as whole word, case-sensitive for acronyms (SBA, MCA),
        # case-insensitive otherwise. Avoid matching inside HTML tags by
        # requiring a leading whitespace or punctuation, not '<'.
        is_acronym = phrase.isupper() or any(c.isupper() for c in phrase if c.isalpha())
        flags = 0 if is_acronym else re.IGNORECASE
        rx = re.compile(r'(?<![<>/\w])' + re.escape(phrase) + r'(?!\w)', flags)

        for m in rx.finditer(body):
            start = m.start()
            if position_inside_ranges(start, a_ranges):
                continue
            # Avoid wrapping if the phrase is inside an HTML attribute by
            # checking the nearest preceding '<' is closed by '>' before the match.
            prev_open = body.rfind("<", 0, start)
            prev_close = body.rfind(">", 0, start)
            if prev_open > prev_close:
                continue  # we're inside a tag

            matched = m.group(0)
            replacement = f'<a href="{target}">{matched}</a>'
            if dry:
                return body, True, f"WOULD wrap '{matched}' -> {target}"
            new_body = body[:start] + replacement + body[m.end():]
            return new_body, True, f"wrapped '{matched}' -> {target}"

    # Fallback: every plain-text mention is already inside another link.
    # Append a short contextual sentence after the last </p> linking to
    # the cluster service page so the article still hits the SEO rule.
    target = f"/{own_cluster}.html"
    anchor = CLUSTER_PHRASES[own_cluster][0]
    sentence = f'For the full overview, see <a href="{target}">{anchor}</a>.'
    paragraph = f'\n        <p class="ax-related-cluster-service" style="margin-top:1.25rem;">{sentence}</p>\n      '
    last_p_close = body.rfind("</p>")
    if last_p_close == -1:
        return body, False, "no phrase match and no </p> anchor"
    if dry:
        return body, True, f"WOULD append cluster service sentence -> {target}"
    insertion_point = last_p_close + len("</p>")
    new_body = body[:insertion_point] + paragraph + body[insertion_point:]
    return new_body, True, f"appended cluster service sentence -> {target}"

def insert_cross_cluster_paragraph(body: str, own_cluster: str, dry: bool):
    sibling_cluster, sentence_template = CROSS_CLUSTER_SIBLING[own_cluster]
    sibling_target = f"/{sibling_cluster}.html"
    sibling_anchor = CROSS_LINK_ANCHOR[sibling_cluster]
    # Inline-link the sibling anchor inside the sentence.
    sentence = sentence_template
    if sibling_anchor.lower() in sentence.lower():
        # Anchor naturally appears in the sentence — link the first occurrence.
        # Allow an optional trailing 's' to keep plural noun forms inside the
        # link (e.g. "working capital loans" instead of "working capital loan"s).
        rx = re.compile(re.escape(sibling_anchor) + r'(s\b)?', re.IGNORECASE)
        m = rx.search(sentence)
        if m:
            full = m.group(0)
            sentence = sentence[:m.start()] + f'<a href="{sibling_target}">{full}</a>' + sentence[m.end():]
    else:
        # Anchor not in sentence — append a "Learn more" style link.
        sentence = f'{sentence} <a href="{sibling_target}">More on {sibling_anchor}.</a>'

    paragraph = f'\n        <p class="ax-related-cross-cluster" style="margin-top:1.25rem;">{sentence}</p>\n      '

    # Insert paragraph just before the last </h2> ... </p> CTA block. Simplest
    # heuristic: insert before the first </main>'s closing or, if there's a
    # CTA card div near the end, just before it. Most reliable: find the LAST
    # </p> in the body and insert after it. That places it after the article's
    # final paragraph but before any trailing card / nav.
    last_p_close = body.rfind("</p>")
    if last_p_close == -1:
        return body, False, "no </p> anchor for insertion"

    insertion_point = last_p_close + len("</p>")
    if dry:
        return body, True, f"WOULD insert cross-cluster sentence -> {sibling_target}"
    new_body = body[:insertion_point] + paragraph + body[insertion_point:]
    return new_body, True, f"inserted cross-cluster sentence -> {sibling_target}"

def process_article(html_path: Path, dry: bool):
    rel = html_path.relative_to(BASE).as_posix()
    own_cluster = cluster_for_path(rel)
    if own_cluster is None:
        return None  # not a cluster article — skip cross-cluster step too

    text = html_path.read_text(encoding="utf-8", errors="ignore")
    main_m = MAIN_RX.search(text)
    if not main_m:
        return None

    body = main_m.group(2)
    body_for_audit = NAV_RX.sub("", body)
    body_for_audit = HEADER_RX.sub("", body_for_audit)
    body_for_audit = FOOTER_RX.sub("", body_for_audit)

    actions = []
    new_body = body

    needs_cluster_link = not has_link_to(body_for_audit, f"/{own_cluster}.html")
    if needs_cluster_link:
        new_body, changed, info = insert_cluster_service_link(new_body, own_cluster, dry)
        actions.append(("cluster_service", changed, info))

    body_for_audit_after = NAV_RX.sub("", new_body)
    body_for_audit_after = HEADER_RX.sub("", body_for_audit_after)
    body_for_audit_after = FOOTER_RX.sub("", body_for_audit_after)
    needs_cross = not has_cross_cluster_link(body_for_audit_after, own_cluster)
    if needs_cross:
        new_body, changed, info = insert_cross_cluster_paragraph(new_body, own_cluster, dry)
        actions.append(("cross_cluster", changed, info))

    if new_body == body:
        return {"path": rel, "actions": actions, "wrote": False}

    if not dry:
        new_text = text[:main_m.start(2)] + new_body + text[main_m.end(2):]
        html_path.write_text(new_text, encoding="utf-8")
    return {"path": rel, "actions": actions, "wrote": not dry}

def main():
    dry = "--dry-run" in sys.argv

    articles = []
    for cluster in sorted(CLUSTERS):
        articles_dir = BASE / cluster / "articles"
        if not articles_dir.exists():
            continue
        for sub in sorted(articles_dir.iterdir()):
            idx = sub / "index.html"
            if sub.is_dir() and idx.exists():
                articles.append(idx)

    changed = 0
    cluster_fixes = 0
    cross_fixes = 0
    for a in articles:
        r = process_article(a, dry)
        if not r:
            continue
        if r["actions"]:
            for kind, did_change, info in r["actions"]:
                if did_change:
                    if kind == "cluster_service":
                        cluster_fixes += 1
                    elif kind == "cross_cluster":
                        cross_fixes += 1
            if r["wrote"] or dry:
                changed += 1
                print(f"[{r['path']}]")
                for kind, did_change, info in r["actions"]:
                    print(f"  {kind}: {'+' if did_change else ' '} {info}")

    mode = "DRY RUN" if dry else "WROTE"
    print(f"\n{mode}: {changed} articles touched, +{cluster_fixes} cluster-service links, +{cross_fixes} cross-cluster sentences")

if __name__ == "__main__":
    main()
