#!/usr/bin/env python3
"""Audit internal links inside <main class="blog-post-main"> on every article.

Outputs:
- Total articles scanned
- Per-article: in-body link count, has cluster service link, has cross-cluster link, has /match.html link
- Worst-offender lists for batch-fix triage

Run: python scripts/audit_internal_links.py [--json]
"""
from pathlib import Path
import re
import sys
import json

BASE = Path(__file__).resolve().parent.parent

CLUSTERS = {
    "sba-loans", "equipment-financing", "business-line-of-credit",
    "working-capital-loans", "business-term-loans", "commercial-real-estate-loans",
    "commercial-bridge-loans", "fix-and-flip", "revenue-based-financing",
    "securities-based-lending", "merchant-cash-advance", "startup-financing",
}

CLUSTER_SERVICE_PAGES = {f"/{c}.html" for c in CLUSTERS}

# Match the body-content container the BLOG_POST_TEMPLATE specifies.
MAIN_RX = re.compile(r'<main\b[^>]*class="[^"]*\bblog-post-main\b[^"]*"[^>]*>(.*?)</main>', re.DOTALL | re.IGNORECASE)
HREF_RX = re.compile(r'<a\b[^>]*\bhref="([^"]+)"', re.IGNORECASE)
NAV_RX = re.compile(r'<nav\b[^>]*>.*?</nav>', re.DOTALL | re.IGNORECASE)
HEADER_RX = re.compile(r'<header\b[^>]*>.*?</header>', re.DOTALL | re.IGNORECASE)
FOOTER_RX = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL | re.IGNORECASE)

def cluster_for_path(rel_path: str):
    """Return cluster name if article lives inside a cluster's /articles/, else None."""
    parts = rel_path.split("/")
    if len(parts) >= 3 and parts[1] == "articles" and parts[0] in CLUSTERS:
        return parts[0]
    return None

def is_internal(href: str) -> bool:
    if not href:
        return False
    h = href.strip()
    if h.startswith("#") or h.startswith("mailto:") or h.startswith("tel:"):
        return False
    if h.startswith("http://") or h.startswith("https://"):
        return "axiantpartners.com" in h
    return True  # relative or absolute path

def normalize_href(href: str) -> str:
    h = href.strip()
    if h.startswith("https://axiantpartners.com"):
        h = h[len("https://axiantpartners.com"):]
    if h.startswith("http://axiantpartners.com"):
        h = h[len("http://axiantpartners.com"):]
    if not h.startswith("/"):
        h = "/" + h
    # Strip trailing fragment / query
    h = h.split("#")[0].split("?")[0]
    return h

def link_target_cluster(href: str):
    """Identify which cluster (if any) a link points into."""
    h = normalize_href(href)
    # Service page like /sba-loans.html
    if h.endswith(".html"):
        slug = h[1:-len(".html")]
        if slug in CLUSTERS:
            return slug
        return None
    # Article-style /<cluster>/articles/...
    parts = h.strip("/").split("/")
    if parts and parts[0] in CLUSTERS:
        return parts[0]
    return None

def audit_article(html_path: Path):
    rel = html_path.relative_to(BASE).as_posix()
    text = html_path.read_text(encoding="utf-8", errors="ignore")
    main_m = MAIN_RX.search(text)
    if not main_m:
        return None  # not an article using this template
    body = main_m.group(1)
    # Strip nested nav/header/footer that may sit inside <main> (e.g. breadcrumbs)
    body = NAV_RX.sub("", body)
    body = HEADER_RX.sub("", body)
    body = FOOTER_RX.sub("", body)

    own_cluster = cluster_for_path(rel)

    in_body_links = []
    seen_targets = set()
    for href in HREF_RX.findall(body):
        if not is_internal(href):
            continue
        target = normalize_href(href)
        in_body_links.append(target)
        seen_targets.add(target)

    # Heuristics
    has_match = any(t == "/match.html" or t.startswith("/match.html") for t in seen_targets)
    has_cluster_service = own_cluster is not None and (f"/{own_cluster}.html" in seen_targets)
    cross_cluster_clusters = set()
    for t in seen_targets:
        c = link_target_cluster(t)
        if c and c != own_cluster:
            cross_cluster_clusters.add(c)

    return {
        "path": rel,
        "own_cluster": own_cluster,
        "in_body_links": len(in_body_links),
        "has_cluster_service_link": has_cluster_service,
        "has_match_link": has_match,
        "cross_cluster_link_count": len(cross_cluster_clusters),
        "cross_clusters": sorted(cross_cluster_clusters),
    }

def main():
    results = []

    # Scan cluster article pages
    for cluster in sorted(CLUSTERS):
        articles_dir = BASE / cluster / "articles"
        if not articles_dir.exists():
            continue
        for sub in sorted(articles_dir.iterdir()):
            idx = sub / "index.html"
            if sub.is_dir() and idx.exists():
                r = audit_article(idx)
                if r:
                    results.append(r)

    # Top-level /articles/<slug>/index.html (cross-cluster pieces)
    top_articles = BASE / "articles"
    if top_articles.exists():
        for sub in sorted(top_articles.iterdir()):
            idx = sub / "index.html"
            if sub.is_dir() and idx.exists():
                r = audit_article(idx)
                if r:
                    results.append(r)

    if "--json" in sys.argv:
        print(json.dumps(results, indent=2))
        return

    total = len(results)
    needs_3plus = sum(1 for r in results if r["in_body_links"] < 3)
    no_cluster_service = sum(1 for r in results if r["own_cluster"] and not r["has_cluster_service_link"])
    no_match = sum(1 for r in results if not r["has_match_link"])
    no_cross_cluster = sum(1 for r in results if r["cross_cluster_link_count"] == 0)

    print(f"Articles scanned: {total}")
    print()
    print(f"  Body links < 3:                       {needs_3plus} ({needs_3plus/total*100:.0f}%)")
    print(f"  Missing cluster service-page link:    {no_cluster_service} ({no_cluster_service/total*100:.0f}%)")
    print(f"  Missing /match.html link:             {no_match} ({no_match/total*100:.0f}%)")
    print(f"  No cross-cluster authority link:      {no_cross_cluster} ({no_cross_cluster/total*100:.0f}%)")
    print()
    print("Distribution of in-body link counts:")
    buckets = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for r in results:
        b = min(r["in_body_links"], 5)
        buckets[b] = buckets.get(b, 0) + 1
    for k in sorted(buckets):
        label = "5+" if k == 5 else str(k)
        print(f"  {label:>3} links: {buckets[k]} articles")
    print()
    print("Worst offenders (0-1 in-body links):")
    worst = sorted(
        (r for r in results if r["in_body_links"] <= 1),
        key=lambda r: (r["in_body_links"], r["path"]),
    )
    for r in worst[:30]:
        flags = []
        if not r["has_match_link"]:
            flags.append("no-match")
        if r["own_cluster"] and not r["has_cluster_service_link"]:
            flags.append("no-cluster-svc")
        if r["cross_cluster_link_count"] == 0:
            flags.append("no-xcluster")
        print(f"  [{r['in_body_links']}] {r['path']}  ({', '.join(flags) or 'ok'})")
    if len(worst) > 30:
        print(f"  ... and {len(worst) - 30} more")

if __name__ == "__main__":
    main()
