#!/usr/bin/env python3
"""Generate sitemap.xml with final URLs only (no redirect sources)."""
import sys
from pathlib import Path
from datetime import date

BASE = Path(__file__).resolve().parent.parent
BASE_URL = "https://axiantpartners.com"
TODAY = date.today().isoformat()

def _file_for_path(loc_path):
    """Map sitemap path to filesystem path for mtime lookup."""
    p = loc_path.rstrip("/")
    if not p:
        return BASE / "index.html"
    if p.endswith(".html"):
        return BASE / p.lstrip("/")
    return BASE / p.lstrip("/") / "index.html"

def _git_dates():
    """path -> date of the commit that last touched it, in one pass.

    Preferred over mtime: mtime is whenever the working tree was last written,
    so a fresh clone dates every page to the clone. Git knows when the content
    actually changed, and gives the same answer on every machine.
    """
    import subprocess
    try:
        out = subprocess.run(
            ["git", "log", "--name-only", "--date=short", "--format=%ad"],
            cwd=BASE, capture_output=True, text=True, timeout=120,
        ).stdout
    except (OSError, subprocess.SubprocessError):
        return {}
    dates, cur = {}, None
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        if len(line) == 10 and line[4] == "-" and line[7] == "-":
            cur = line
        elif cur and line not in dates:
            dates[line] = cur          # log is newest-first, so first wins
    return dates


_GIT_DATES = _git_dates()


def _lastmod(loc_path):
    """When the page actually last changed. W3C format YYYY-MM-DD.

    The committed sitemap had 400 of 764 entries reading 2026-04 while the files
    had been rewritten the week before, because this generator is not wired into
    any build step and had not been run since. A lastmod that lags the content
    tells Google there is nothing to re-look at.
    """
    f = _file_for_path(loc_path)
    rel = f.relative_to(BASE).as_posix() if f.is_relative_to(BASE) else None
    if rel and rel in _GIT_DATES:
        return _GIT_DATES[rel]
    if f.exists():
        try:
            from datetime import datetime
            return datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d")
        except OSError:
            pass
    return TODAY

def _escape_xml(s):
    """Escape XML special chars in URL for valid sitemap output."""
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )

def url_entry(loc_path, changefreq="monthly", priority="0.8"):
    loc = _escape_xml(BASE_URL + loc_path)
    lastmod = _lastmod(loc_path)
    return f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>'''

def main():
    urls = []
    seen = set()

    def add(loc_path, **kwargs):
        if loc_path in seen:
            return
        seen.add(loc_path)
        urls.append(url_entry(loc_path, **kwargs))

    # Core pages
    add("/", priority="1.0")
    add("/match.html", priority="0.9")
    add("/services.html", priority="0.9")
    add("/faq.html")
    add("/contact.html")
    add("/calculator.html")
    add("/equipment-financing-calculator.html", priority="0.9")
    add("/blog.html", changefreq="weekly")
    add("/referral.html", priority="0.7")

    # Service/topic pages
    for p in [
        "sba-loans", "equipment-financing", "equipment", "business-line-of-credit",
        "working-capital-loans", "business-term-loans", "commercial-real-estate-loans",
        "commercial-bridge-loans", "fix-and-flip", "revenue-based-financing",
        "securities-based-lending", "merchant-cash-advance", "startup-financing",
    ]:
        add(f"/{p}.html")

    # Article hubs
    for topic in [
        "sba-loans", "equipment-financing", "business-line-of-credit",
        "working-capital-loans", "business-term-loans", "commercial-real-estate-loans",
        "commercial-bridge-loans", "fix-and-flip", "revenue-based-financing",
        "securities-based-lending", "merchant-cash-advance", "startup-financing",
    ]:
        add(f"/{topic}/articles/", changefreq="weekly", priority="0.75")

    # Individual articles
    for d in (BASE / "sba-loans" / "articles").iterdir():
        if d.is_dir():
            add(f"/sba-loans/articles/{d.name}/", priority="0.7")
    for d in (BASE / "equipment-financing" / "articles").iterdir():
        if d.is_dir():
            add(f"/equipment-financing/articles/{d.name}/", priority="0.7")
    for d in (BASE / "business-line-of-credit" / "articles").iterdir():
        if d.is_dir():
            add(f"/business-line-of-credit/articles/{d.name}/", priority="0.7")
    for d in (BASE / "working-capital-loans" / "articles").iterdir():
        if d.is_dir():
            add(f"/working-capital-loans/articles/{d.name}/", priority="0.7")
    for d in (BASE / "business-term-loans" / "articles").iterdir():
        if d.is_dir() and d.name != "business-term-loan-vs-line-of-credit":  # 301 redirect
            add(f"/business-term-loans/articles/{d.name}/", priority="0.7")
    for d in (BASE / "commercial-real-estate-loans" / "articles").iterdir():
        if d.is_dir():
            add(f"/commercial-real-estate-loans/articles/{d.name}/", priority="0.7")
    for d in (BASE / "commercial-bridge-loans" / "articles").iterdir():
        if d.is_dir():
            add(f"/commercial-bridge-loans/articles/{d.name}/", priority="0.7")
    for d in (BASE / "fix-and-flip" / "articles").iterdir():
        if d.is_dir():
            add(f"/fix-and-flip/articles/{d.name}/", priority="0.7")
    for d in (BASE / "revenue-based-financing" / "articles").iterdir():
        if d.is_dir():
            add(f"/revenue-based-financing/articles/{d.name}/", priority="0.7")
    for d in (BASE / "securities-based-lending" / "articles").iterdir():
        if d.is_dir():
            add(f"/securities-based-lending/articles/{d.name}/", priority="0.7")
    for d in (BASE / "merchant-cash-advance" / "articles").iterdir():
        if d.is_dir():
            add(f"/merchant-cash-advance/articles/{d.name}/", priority="0.7")
    startup_articles = BASE / "startup-financing" / "articles"
    if startup_articles.exists():
        for d in startup_articles.iterdir():
            if d.is_dir():
                add(f"/startup-financing/articles/{d.name}/", priority="0.7")

    # General articles hub (root /articles/)
    articles_root = BASE / "articles"
    if articles_root.exists():
        add("/articles/", changefreq="weekly", priority="0.75")
        for d in articles_root.iterdir():
            if d.is_dir() and (d / "index.html").exists():
                add(f"/articles/{d.name}/", priority="0.7")

    # Get Matched product landers (noindex on-page; optional sitemap inclusion for GSC)
    for p in ("equipment", "line-of-credit", "working-capital", "merchant-cash-advance"):
        add(f"/get-matched/{p}/", priority="0.55")

    # Industries hub + individual industry pages
    add("/industries.html", priority="0.85")
    industries = [
        "construction-business-financing", "trucking-business-financing",
        "agriculture-business-financing", "forestry-business-financing",
        "landscaping-business-financing", "manufacturing-business-financing",
        "medical-practices-business-financing", "restaurants-business-financing",
        "auto-repair-business-financing", "logistics-warehousing-business-financing",
        "cleaning-business-financing",
    ]
    for p in industries:
        if (BASE / f"{p}.html").exists():
            add(f"/{p}.html")

    # Construction business financing subpages
    construction_dir = BASE / "construction-business-financing"
    if construction_dir.exists():
        for sub in construction_dir.iterdir():
            if sub.is_dir() and (sub / "index.html").exists():
                add(f"/construction-business-financing/{sub.name}/", priority="0.7")

    # Trucking business financing subpages (long-form industry articles)
    trucking_dir = BASE / "trucking-business-financing"
    if trucking_dir.exists():
        for sub in trucking_dir.iterdir():
            if sub.is_dir() and (sub / "index.html").exists():
                add(f"/trucking-business-financing/{sub.name}/", priority="0.7")

    # Equipment guides (equipment/[type]/index.html)
    equipment_dir = BASE / "equipment"
    if equipment_dir.exists():
        for cat in equipment_dir.iterdir():
            if cat.is_dir() and (cat / "index.html").exists():
                add(f"/equipment/{cat.name}/", priority="0.75")
                # Equipment subpages (e.g. semi-trucks/financing-owner-operators/)
                for sub in cat.iterdir():
                    if sub.is_dir() and (sub / "index.html").exists():
                        add(f"/equipment/{cat.name}/{sub.name}/", priority="0.7")

    # Legal/utility
    add("/vendors.html", priority="0.6")
    add("/rightmfgsystems.html", priority="0.6")
    add("/privacy-policy.html", changefreq="yearly", priority="0.4")
    add("/terms-and-conditions.html", changefreq="yearly", priority="0.4")

    urlset_attrs = (
        'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 '
        'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"'
    )
    out = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f"<urlset {urlset_attrs}>\n"
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    # This generator enumerates a hand-maintained list rather than discovering
    # pages, so it drifts behind the site. As of 2026-08-02 it emits 576 URLs
    # against 764 in the committed sitemap - running it would silently drop 198,
    # including all of business-debt-relief and equipment-for-sale. Refuse to
    # shrink the sitemap unless that is explicitly what the caller wants.
    existing = BASE / "sitemap.xml"
    if existing.exists():
        import re as _re
        have = len(_re.findall(r"<loc>", existing.read_text(encoding="utf-8")))
        if len(urls) < have and "--allow-shrink" not in sys.argv:
            sys.exit(
                f"refusing to write: would go from {have} URLs to {len(urls)}, "
                f"dropping {have - len(urls)}. The page list in this script is "
                f"behind the site. Update it, or pass --allow-shrink if the "
                f"removals are intended."
            )
    existing.write_text(out, encoding="utf-8")
    print(f"Generated sitemap with {len(urls)} URLs")

if __name__ == "__main__":
    main()
