#!/usr/bin/env python3
"""Generate sitemap.xml with final URLs only (no redirect sources)."""
from pathlib import Path
from datetime import date

BASE = Path(__file__).resolve().parent.parent
BASE_URL = "https://www.axiantpartners.com"
LASTMOD = date.today().isoformat()

def url_entry(loc_path, changefreq="monthly", priority="0.8"):
    loc = BASE_URL + loc_path
    return f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{LASTMOD}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>'''

def main():
    urls = []

    # Core pages
    urls.append(url_entry("/", priority="1.0"))
    urls.append(url_entry("/match.html", priority="0.9"))
    urls.append(url_entry("/services.html", priority="0.9"))
    urls.append(url_entry("/faq.html"))
    urls.append(url_entry("/contact.html"))
    urls.append(url_entry("/calculator.html"))
    urls.append(url_entry("/blog.html", changefreq="weekly"))
    urls.append(url_entry("/referral.html", priority="0.7"))

    # Service/topic pages
    for p in [
        "sba-loans", "equipment-financing", "equipment", "business-line-of-credit",
        "working-capital-loans", "business-term-loans", "commercial-real-estate-loans",
        "commercial-bridge-loans", "fix-and-flip", "revenue-based-financing",
        "securities-based-lending", "merchant-cash-advance"
    ]:
        urls.append(url_entry(f"/{p}.html"))

    # Article hubs
    for topic in [
        "sba-loans", "equipment-financing", "business-line-of-credit",
        "working-capital-loans", "business-term-loans", "commercial-real-estate-loans",
        "commercial-bridge-loans", "fix-and-flip", "revenue-based-financing",
        "securities-based-lending", "merchant-cash-advance"
    ]:
        urls.append(url_entry(f"/{topic}/articles/", changefreq="weekly", priority="0.75"))

    # Individual articles
    for d in (BASE / "sba-loans" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/sba-loans/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "equipment-financing" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/equipment-financing/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "business-line-of-credit" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/business-line-of-credit/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "working-capital-loans" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/working-capital-loans/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "business-term-loans" / "articles").iterdir():
        if d.is_dir() and d.name != "business-term-loan-vs-line-of-credit":  # 301 redirect to business-line-of-credit
            urls.append(url_entry(f"/business-term-loans/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "commercial-real-estate-loans" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/commercial-real-estate-loans/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "commercial-bridge-loans" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/commercial-bridge-loans/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "fix-and-flip" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/fix-and-flip/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "revenue-based-financing" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/revenue-based-financing/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "securities-based-lending" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/securities-based-lending/articles/{d.name}/", priority="0.7"))
    for d in (BASE / "merchant-cash-advance" / "articles").iterdir():
        if d.is_dir():
            urls.append(url_entry(f"/merchant-cash-advance/articles/{d.name}/", priority="0.7"))

    # Industries hub + individual industry pages
    urls.append(url_entry("/industries.html", priority="0.85"))
    industries = [
        "construction-business-financing", "trucking-business-financing",
        "agriculture-business-financing", "forestry-business-financing",
        "landscaping-business-financing", "manufacturing-business-financing",
        "medical-practices-business-financing", "restaurants-business-financing",
        "auto-repair-business-financing", "logistics-warehousing-business-financing"
    ]
    for p in industries:
        if (BASE / f"{p}.html").exists():
            urls.append(url_entry(f"/{p}.html"))

    # Legacy equipment landing pages removed - structure uses /equipment/[type]/ now

    # Equipment by type (equipment/[type]/how-to-finance-*)
    equipment_dir = BASE / "equipment"
    if equipment_dir.exists():
        for cat in equipment_dir.iterdir():
            if cat.is_dir():
                urls.append(url_entry(f"/equipment/{cat.name}/", priority="0.75"))
                for sub in cat.iterdir():
                    if sub.is_dir() and (sub / "index.html").exists():
                        urls.append(url_entry(f"/equipment/{cat.name}/{sub.name}/", priority="0.75"))

    # Legal/utility
    urls.append(url_entry("/vendors.html", priority="0.6"))
    urls.append(url_entry("/rightmfgsystems.html", priority="0.6"))
    urls.append(url_entry("/privacy-policy.html", changefreq="yearly", priority="0.4"))
    urls.append(url_entry("/terms-and-conditions.html", changefreq="yearly", priority="0.4"))

    out = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
    (BASE / "sitemap.xml").write_text(out, encoding="utf-8")
    print(f"Generated sitemap with {len(urls)} URLs")

if __name__ == "__main__":
    main()
