#!/usr/bin/env python3
"""Repoint the FTC source on every page and generator module.

https://www.ftc.gov/business-guidance/credit-finance-trade now renders an empty
"Business Guidance" listing ("No results found"), so 113 pages cited a page with no
content. The replacement is the FTC Bureau of Consumer Protection's own guidance to
small-business financing providers (business blog, 2020-08-03): misrepresented costs,
unlawful servicing and collection, false government affiliation, policing brokers and
marketers. Checked to load with full content on 2026-10-22.

Rewrites the whole <li> entry (URL, name and description) in HTML, and the source tuple
in the generator modules, so a rebuild cannot bring the dead link back.

    python scripts/aeo/fix_ftc_source.py [--apply]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OLD_URL = "https://www.ftc.gov/business-guidance/credit-finance-trade"
NEW_URL = "https://www.ftc.gov/business-guidance/blog/2020/08/protecting-small-businesses-seeking-financing-during-pandemic"
NEW_NAME = "FTC: Protecting Small Businesses Seeking Financing"
NEW_DESC = ("The FTC's guidance to lenders, brokers and merchant cash advance providers on "
            "misrepresented costs, unlawful collection and false claims of government affiliation.")

HTML_ENTRY = re.compile(
    r'<a href="' + re.escape(OLD_URL) + r'"( rel="noopener nofollow" target="_blank")>[^<]*</a>( &mdash; | — )[^<]*(</li>)')
PY_TUPLE = re.compile(r'\(\s*"' + re.escape(OLD_URL) + r'",\s*"[^"]*",\s*(?:"[^"]*"\s*)+\)', re.S)


def main(apply):
    pages = mods = 0
    for f in ROOT.glob("**/*.html"):
        if "node_modules" in f.parts or any(p.startswith("_backup") for p in f.parts):
            continue
        s = f.read_bytes().decode("utf-8")
        if OLD_URL not in s:
            continue
        new = HTML_ENTRY.sub(lambda m: f'<a href="{NEW_URL}"{m.group(1)}>{NEW_NAME}</a>{m.group(2)}{NEW_DESC}{m.group(3)}', s)
        if OLD_URL in new:
            print(f"  UNHANDLED shape: {f.relative_to(ROOT)}")
            continue
        pages += 1
        if apply:
            f.write_bytes(new.encode("utf-8"))
    for f in list((ROOT / "scripts").glob("*.py")) + list((ROOT / "scripts" / "aeo").glob("*.py")):
        if f.name == Path(__file__).name:
            continue
        s = f.read_text(encoding="utf-8")
        if OLD_URL not in s:
            continue
        new = PY_TUPLE.sub(lambda m: f'("{NEW_URL}",\n       "{NEW_NAME}",\n       "{NEW_DESC}")', s)
        # add_sources_by_claim.py builds entries with S(url, name, desc, trigger)
        new = re.sub(r'S\("' + re.escape(OLD_URL) + r'", "[^"]*",\s*"[^"]*",',
                     f'S("{NEW_URL}",\n      "{NEW_NAME}",\n      "{NEW_DESC}",', new)
        if OLD_URL in new:
            print(f"  UNHANDLED module: {f.relative_to(ROOT)}")
            continue
        mods += 1
        if apply:
            f.write_text(new, encoding="utf-8", newline="\n")
        print(f"  module: {f.relative_to(ROOT)}")
    print(f"{'fixed' if apply else 'would fix'}: {pages} pages, {mods} modules")
    return 0


if __name__ == "__main__":
    sys.exit(main("--apply" in sys.argv))
