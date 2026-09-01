#!/usr/bin/env python3
"""Audit Quick Answer cards on every article body.

Per BLOG_POST_TEMPLATE.md a strong Quick Answer:
- Exists (.quick-answer div with a paragraph)
- 50-100 words in the answer paragraph
- 2-3 specific numbers in <strong> tags (rates, percentages, dollar amounts, time ranges)
- Leads with the direct answer (no "When considering..." preamble)
- Has a contextual CTA link (typically /match.html)

Outputs: counts + worst-offender list grouped by problem type.

Run: python scripts/audit_quick_answers.py [--json]
"""
from pathlib import Path
import re
import sys
import json

BASE = Path(__file__).resolve().parent.parent

CLUSTERS = [
    "sba-loans", "equipment-financing", "business-line-of-credit",
    "working-capital-loans", "business-term-loans", "commercial-real-estate-loans",
    "commercial-bridge-loans", "fix-and-flip", "revenue-based-financing",
    "securities-based-lending", "merchant-cash-advance", "startup-financing",
]

# Match <div class="quick-answer ..."> as an exact class token (not blog-rail-quick-answer).
# Then balance nested <div>...</div> by greedy-but-bounded scanning.
QA_DIV_OPEN_RX = re.compile(r'<div\b[^>]*\bclass="(?P<cls>[^"]*)"[^>]*>', re.IGNORECASE)
P_RX = re.compile(r'<p\b[^>]*>(.*?)</p>', re.DOTALL | re.IGNORECASE)
STRONG_RX = re.compile(r'<strong\b[^>]*>(.*?)</strong>', re.DOTALL | re.IGNORECASE)
A_HREF_RX = re.compile(r'<a\b[^>]*\bhref="([^"]+)"', re.IGNORECASE)
TAG_RX = re.compile(r'<[^>]+>')
NUMBER_RX = re.compile(r'(\$[\d,]+(?:\.\d+)?(?:[KMB]?\b|\s*million|\s*billion)?|[\d,]+%|\d+[–—\-]\d+(?:\s*days?| days| months?| weeks?| years?| hours?)?|FICO\s*\d+|\d+\s*FICO)', re.IGNORECASE)

# Bad opening phrases — preamble that signals weak answer-first structure
BAD_OPENERS = [
    r"^when ",
    r"^if you",
    r"^if your",
    r"^before ",
    r"^to ",
    r"^in today",
    r"^it.s important",
    r"^there are",
    r"^this article",
    r"^understanding ",
    r"^thinking about",
    r"^considering ",
    r"^navigating",
]
BAD_OPENER_RX = re.compile("|".join(BAD_OPENERS), re.IGNORECASE)

def strip_tags(s: str) -> str:
    return re.sub(r"\s+", " ", TAG_RX.sub("", s)).strip()

def first_p_in_qa(qa_html: str):
    """Return the first non-CTA paragraph (the answer body)."""
    ps = P_RX.findall(qa_html)
    for p in ps:
        plain = strip_tags(p)
        if not plain:
            continue
        # Skip obvious CTA paragraphs (just a link)
        if re.match(r'^\s*<a\b', p, re.IGNORECASE) and len(strip_tags(p)) < 60:
            continue
        return p, plain
    return None, ""

def find_quick_answer_block(text: str):
    """Locate the body's <div class="quick-answer">...</div>, balancing nested divs.
    Returns (start_offset_after_open_tag, end_offset_at_closing_lt) or None.
    """
    for m in QA_DIV_OPEN_RX.finditer(text):
        classes = m.group("cls").split()
        if "quick-answer" not in classes:
            continue
        # Now walk forward to find the matching </div>, balancing nested <div>s.
        depth = 1
        pos = m.end()
        scan_rx = re.compile(r'<(/?)div\b', re.IGNORECASE)
        while True:
            sm = scan_rx.search(text, pos)
            if not sm:
                return None
            if sm.group(1) == "/":
                depth -= 1
                if depth == 0:
                    return text[m.end():sm.start()]
                pos = sm.end()
            else:
                depth += 1
                pos = sm.end()
    return None

def audit_article(html_path: Path):
    rel = html_path.relative_to(BASE).as_posix()
    text = html_path.read_text(encoding="utf-8", errors="ignore")
    qa_html = find_quick_answer_block(text)
    if qa_html is None:
        return {"path": rel, "has_qa": False, "issues": ["missing"], "word_count": 0, "strong_count": 0, "number_count": 0, "has_cta": False, "weak_opener": False}
    p_html, p_plain = first_p_in_qa(qa_html)
    word_count = len(p_plain.split()) if p_plain else 0
    strong_count = len(STRONG_RX.findall(p_html or ""))
    # Count specific numbers (rates, dollar amounts, ranges, FICO)
    number_count = len(NUMBER_RX.findall(p_plain)) if p_plain else 0
    cta_links = [h for h in A_HREF_RX.findall(qa_html) if "/match.html" in h or "/equipment-financing-calculator" in h or "/sba-loans" in h]
    has_cta = len(cta_links) > 0
    weak_opener = bool(BAD_OPENER_RX.match(p_plain.strip())) if p_plain else False

    issues = []
    if word_count < 50:
        issues.append(f"too_short ({word_count}w)")
    elif word_count > 110:
        issues.append(f"too_long ({word_count}w)")
    if strong_count < 2:
        issues.append(f"weak_emphasis ({strong_count} strongs)")
    if number_count < 2:
        issues.append(f"few_numbers ({number_count})")
    if not has_cta:
        issues.append("no_cta")
    if weak_opener:
        issues.append("weak_opener")

    return {
        "path": rel,
        "has_qa": True,
        "word_count": word_count,
        "strong_count": strong_count,
        "number_count": number_count,
        "has_cta": has_cta,
        "weak_opener": weak_opener,
        "issues": issues,
    }

def gather_articles():
    out = []
    for cluster in CLUSTERS:
        d = BASE / cluster / "articles"
        if not d.exists():
            continue
        for sub in sorted(d.iterdir()):
            idx = sub / "index.html"
            if sub.is_dir() and idx.exists():
                out.append(idx)
    top = BASE / "articles"
    if top.exists():
        for sub in sorted(top.iterdir()):
            idx = sub / "index.html"
            if sub.is_dir() and idx.exists():
                out.append(idx)
    return out

def main():
    articles = gather_articles()
    results = [audit_article(a) for a in articles]

    if "--json" in sys.argv:
        print(json.dumps(results, indent=2))
        return

    total = len(results)
    has_qa = sum(1 for r in results if r["has_qa"])
    missing = total - has_qa
    too_short = sum(1 for r in results if r["has_qa"] and r["word_count"] < 50)
    too_long = sum(1 for r in results if r["has_qa"] and r["word_count"] > 110)
    weak_emphasis = sum(1 for r in results if r["has_qa"] and r["strong_count"] < 2)
    few_numbers = sum(1 for r in results if r["has_qa"] and r["number_count"] < 2)
    no_cta = sum(1 for r in results if r["has_qa"] and not r["has_cta"])
    weak_opener = sum(1 for r in results if r["has_qa"] and r["weak_opener"])
    no_issues = sum(1 for r in results if r["has_qa"] and not r["issues"])

    print(f"Articles scanned: {total}")
    print()
    print(f"  Quick Answer present:           {has_qa}/{total} ({has_qa/total*100:.0f}%)")
    print(f"  Quick Answer missing:           {missing}")
    print()
    print(f"  Of cards present ({has_qa}):")
    print(f"    Too short (<50 words):        {too_short} ({too_short/has_qa*100:.0f}% of cards)")
    print(f"    Too long (>110 words):        {too_long} ({too_long/has_qa*100:.0f}%)")
    print(f"    Weak emphasis (<2 <strong>):  {weak_emphasis} ({weak_emphasis/has_qa*100:.0f}%)")
    print(f"    Few specific numbers (<2):    {few_numbers} ({few_numbers/has_qa*100:.0f}%)")
    print(f"    No CTA link:                  {no_cta} ({no_cta/has_qa*100:.0f}%)")
    print(f"    Weak opener (preamble):       {weak_opener} ({weak_opener/has_qa*100:.0f}%)")
    print(f"    Clean (no issues):            {no_issues} ({no_issues/has_qa*100:.0f}%)")
    print()

    print("Word-count distribution (cards present):")
    buckets = {"<30": 0, "30-49": 0, "50-79": 0, "80-110": 0, "111-150": 0, ">150": 0}
    for r in results:
        if not r["has_qa"]:
            continue
        w = r["word_count"]
        if w < 30: buckets["<30"] += 1
        elif w < 50: buckets["30-49"] += 1
        elif w < 80: buckets["50-79"] += 1
        elif w <= 110: buckets["80-110"] += 1
        elif w <= 150: buckets["111-150"] += 1
        else: buckets[">150"] += 1
    for k in ["<30", "30-49", "50-79", "80-110", "111-150", ">150"]:
        print(f"    {k:>7}: {buckets[k]}")
    print()

    print("Worst offenders (3+ issues):")
    worst = [r for r in results if r["has_qa"] and len(r["issues"]) >= 3]
    for r in sorted(worst, key=lambda r: (-len(r["issues"]), r["path"]))[:25]:
        print(f"  [{len(r['issues'])} issues] {r['path']}")
        print(f"     {', '.join(r['issues'])}")
    if len(worst) > 25:
        print(f"  ... and {len(worst) - 25} more")
    print()
    print(f"Total worst-offender count (3+ issues): {len(worst)}")

if __name__ == "__main__":
    main()
