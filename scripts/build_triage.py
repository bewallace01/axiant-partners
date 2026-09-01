"""One-shot script — builds _analysis/SEO_CLEANUP_TRIAGE_2026-05-27.md from
sitemap.xml + the GSC Pages.csv export. Safe to delete after the cleanup is
done; kept here so the recipe is reproducible from a future GSC export."""
from __future__ import annotations

import csv
import pathlib
import re
from collections import defaultdict

REPO = pathlib.Path(__file__).resolve().parent.parent
GSC_PAGES_CSV = pathlib.Path(r"C:\Users\alexr\AppData\Local\Temp\axiant-gsc-export\Pages.csv")
OUTPUT = REPO / "_analysis" / "SEO_CLEANUP_TRIAGE_2026-05-27.md"
ORIGIN = "https://axiantpartners.com"


def main() -> None:
    sitemap_xml = (REPO / "sitemap.xml").read_text(encoding="utf-8")
    sitemap_urls = [u.strip() for u in re.findall(r"<loc>([^<]+)</loc>", sitemap_xml)]

    # Best record per URL (max impressions wins if duplicate rows exist).
    gsc: dict[str, tuple[int, int, float]] = {}
    with GSC_PAGES_CSV.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            url = row["Top pages"].split("#")[0].strip()
            clicks = int(row["Clicks"])
            imp = int(row["Impressions"])
            pos = float(row["Position"])
            prev = gsc.get(url)
            if prev is None or imp > prev[1]:
                gsc[url] = (clicks, imp, pos)

    never_shown = sorted(set(sitemap_urls) - set(gsc.keys()))

    # ── bucket function ────────────────────────────────────────────────
    def bucket(url: str) -> str:
        path = url.replace(ORIGIN, "")
        rules = [
            ("/equipment-financing/states/", "1A. /equipment-financing/states/* (state pSEO)"),
            ("/equipment-financing/articles/", "1B. /equipment-financing/articles/*"),
            ("/construction-business-financing/", "1C. /construction-business-financing/* (industry child)"),
            ("/working-capital-loans/articles/", "1D. /working-capital-loans/articles/*"),
            ("/merchant-cash-advance/articles/", "1E. /merchant-cash-advance/articles/*"),
            ("/sba-loans/articles/", "1F. /sba-loans/articles/*"),
            ("/business-line-of-credit/articles/", "1G. /business-line-of-credit/articles/*"),
            ("/business-term-loans/articles/", "1H. /business-term-loans/articles/*"),
            ("/commercial-real-estate-loans/articles/", "1I. /commercial-real-estate-loans/articles/*"),
            ("/trucking-business-financing/", "1J. /trucking-business-financing/* (industry child)"),
            ("/fix-and-flip/articles/", "1K. /fix-and-flip/articles/*"),
            ("/get-matched/", "1Y. /get-matched/* (KEEP — lead capture)"),
        ]
        for needle, label in rules:
            if needle in path:
                return label
        if path.endswith(".html"):
            return "1Z. Root .html pages (KEEP — review individually)"
        return "1X. Other / misc"

    DEFAULT_ACTION = {
        "1A. /equipment-financing/states/* (state pSEO)": "**KILL or CONSOLIDATE** — these 33 state pages are the prime suspects for the May 18 quality demotion. Either 410-Gone them or 301 to /equipment-financing.html.",
        "1B. /equipment-financing/articles/*": "AUDIT first. Some have geo-specific intent (Arkansas trucking, FL hurricane); others read like generic AI long-tail.",
        "1C. /construction-business-financing/* (industry child)": "**CONSOLIDATE** into the /construction-business-financing.html hub. These are sub-topic articles with weak standalone search demand.",
        "1D. /working-capital-loans/articles/*": "AUDIT first.",
        "1E. /merchant-cash-advance/articles/*": "AUDIT first.",
        "1F. /sba-loans/articles/*": "AUDIT first.",
        "1G. /business-line-of-credit/articles/*": "AUDIT first.",
        "1H. /business-term-loans/articles/*": "AUDIT first.",
        "1I. /commercial-real-estate-loans/articles/*": "AUDIT first.",
        "1J. /trucking-business-financing/* (industry child)": "**CONSOLIDATE** into the /trucking-business-financing.html hub.",
        "1K. /fix-and-flip/articles/*": "AUDIT first.",
        "1Z. Root .html pages (KEEP — review individually)": "**KEEP** — these are likely load-bearing nav pages. Verify each.",
        "1Y. /get-matched/* (KEEP — lead capture)": "**KEEP** — conversion pages, not meant to rank organically.",
        "1X. Other / misc": "Audit individually.",
    }

    groups: dict[str, list[str]] = defaultdict(list)
    for u in never_shown:
        groups[bucket(u)].append(u.replace(ORIGIN, ""))

    # ── title-fix candidates ───────────────────────────────────────────
    title_fix = [
        (url, gsc[url][1], gsc[url][2])
        for url in gsc
        if gsc[url][0] == 0 and gsc[url][1] >= 100
    ]
    title_fix.sort(key=lambda r: -r[1])

    # ── render ─────────────────────────────────────────────────────────
    out: list[str] = []
    out.append("# SEO Cleanup Triage — May 2026 Drop Recovery")
    out.append("")
    out.append("**Generated:** 2026-05-27 from GSC export `2026-05-27`")
    out.append("**Diagnosis:** May 18 indexing-dilution event. Index count jumped 378 → 506 in one day. Impressions fell 65%. Average position slid from ~11 to ~27. Brand and high-intent commercial pages still rank fine — the problem is volume of thin pages pulling the domain-wide quality signal down.")
    out.append("**Strategy:** Cleanup BEFORE new pages. Kill / consolidate dead weight, fix title-meta on existing rankers, watch index count drop, then publish selectively.")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"## Section 1 — Never-shown pages ({len(never_shown)} URLs)")
    out.append("")
    out.append("These are in the sitemap but Google **has not shown them in any search result** over the last 28 days. They cost crawl budget, dilute quality signal, and contribute nothing.")
    out.append("")

    for grp in sorted(groups.keys()):
        urls = groups[grp]
        out.append(f"### {grp} — {len(urls)} URLs")
        out.append(f"**Default action:** {DEFAULT_ACTION.get(grp, 'AUDIT')}")
        out.append("")
        for u in urls:
            out.append(f"- `{u}`")
        out.append("")

    out.append("---")
    out.append("")
    out.append(f"## Section 2 — Title/meta fix candidates ({len(title_fix)} URLs)")
    out.append("")
    out.append("These pages ARE ranking but getting **zero clicks** despite >=100 impressions each. The title or meta isn't compelling the click. **Highest ROI work in the whole cleanup** — no content rewrite needed, just rewrite the `<title>` and `<meta name=\"description\">` per `.cursor/rules/seo-geo-aeo-meta.mdc`.")
    out.append("")
    out.append("| Impr | Pos | URL | Priority |")
    out.append("|-----:|----:|-----|----------|")
    for url, imp, pos in title_fix[:50]:
        path = url.replace(ORIGIN, "")
        if pos <= 5:
            prio = "**TOP** (page 1, just bad CTR)"
        elif pos <= 10:
            prio = "HIGH (page 1, position 6–10)"
        elif pos <= 20:
            prio = "MED (just below fold)"
        else:
            prio = "LOW (rewrite unlikely to lift to page 1)"
        out.append(f"| {imp} | {pos:.1f} | `{path}` | {prio} |")
    out.append("")

    out.append("---")
    out.append("")
    out.append("## Section 3 — Recommended order of operations")
    out.append("")
    out.append("1. **Week 1 — Quick wins.** Rewrite titles + metas on the top 10–15 entries from Section 2. No content edits required. Watch CTR climb week-over-week.")
    out.append("2. **Week 1 — Kill dead weight.** Drop the 33 state pSEO pages and 14 construction child pages. Either delete the files + add `410` redirects, or `301` each to the closest hub. Remove from `sitemap.xml`. This signals to Google we're pruning and should drop the indexed count from 506 toward ~420.")
    out.append("3. **Week 2 — Audit article batches.** For each Section-1 article group (1D–1K), sample 3 pages per template. If duplicate ratio >40% OR reads as generic AI long-tail with no real query intent, consolidate into hub. Otherwise rewrite for human intent.")
    out.append("4. **Week 3+ — Resubmit cleaned sitemap.** Use GSC URL Inspection to request reindexing of the rewritten pages. Rank recovery typically begins within 1–2 weeks of index count stabilizing at a lower number.")
    out.append("5. **NO new programmatic pages** until index count drops below ~420 AND average position recovers above 15. When we do publish: one batch of ~10 at a time, never 128 in a day.")
    out.append("")

    out.append("---")
    out.append("")
    out.append("## Section 4 — Data still needed from user")
    out.append("")
    out.append("Coverage.xlsx only has counts. To finish triage we need per-URL exports from GSC. Open **Search Console → Pages**, click each issue category, then **Export** to CSV:")
    out.append("")
    out.append("- **Crawled — currently not indexed** (17 URLs). Google crawled these and *explicitly rejected* them. Highest-priority audit — these are the worst-quality pages on the site by Google's own judgment.")
    out.append("- **Discovered — currently not indexed** (82 URLs). Google saw them but won't crawl yet. Often signals low link equity from the rest of the site.")
    out.append("- **Excluded by `noindex` tag** (6 URLs). Verify intentional vs accidental.")
    out.append("- **Alternate page with proper canonical** (6 URLs). Usually fine; spot-check canonical targets.")
    out.append("- **Not found (404)** (5 URLs). 301 to the closest relevant page or resurrect.")
    out.append("")

    out.append("---")
    out.append("")
    out.append("## Appendix — Pattern summary")
    out.append("")
    out.append(f"- Sitemap URLs: {len(sitemap_urls)}")
    out.append(f"- URLs with any impressions in last 28d: {len(gsc)}")
    out.append(f"- Never-shown URLs: {len(never_shown)}")
    out.append(f"- Title-fix candidates (≥100 imp, 0 clicks): {len(title_fix)}")
    out.append("")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {OUTPUT} ({len(out)} lines)")


if __name__ == "__main__":
    main()
