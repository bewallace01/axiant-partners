#!/usr/bin/env python3
"""AEO plan 1d: a Person must be a person.

48 articles named "Axiant Partners Editorial Team" as a schema.org Person. Until a named
reviewer is chosen, their author becomes the site's Organization entity (the same @id the
rest of the site uses), which is what those pages truthfully are. Idempotent.

Once the reviewer is decided, add reviewedBy (Person) and a visible "Reviewed by" line
on money pages and the top-25 cited pages instead of reintroducing a team-as-Person.

    python scripts/aeo/editorial_team_to_org.py [--dry]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ORG = ('{"@type":"Organization","@id":"https://axiantpartners.com/#organization",'
       '"name":"Axiant Partners","url":"https://axiantpartners.com"}')
# author: [ Person "Editorial Team" (worksFor Axiant), Organization Axiant ]  ->  author: ORG
PATTERN = re.compile(
    r'"author"\s*:\s*\[\s*\{\s*"@type"\s*:\s*"Person"\s*,\s*"name"\s*:\s*"Axiant Partners Editorial Team"'
    r'[^{}]*\{[^{}]*\}\s*\}\s*,\s*\{\s*"@type"\s*:\s*"Organization"\s*,\s*"name"\s*:\s*"Axiant Partners"'
    r'\s*,\s*"url"\s*:\s*"https://axiantpartners\.com"\s*\}\s*\]')
LDJSON = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def main(dry):
    changed = bad = 0
    for f in ROOT.glob("**/*.html"):
        if "node_modules" in f.parts or any(p.startswith("_backup") for p in f.parts):
            continue
        s = f.read_bytes().decode("utf-8", errors="strict") if b"Editorial Team" in f.read_bytes() else None
        if s is None:
            continue
        new, n = PATTERN.subn('"author":' + ORG, s)
        if n != 1 or "Editorial Team" in new:
            print(f"  UNMATCHED ({n}): {f.relative_to(ROOT)}")
            bad += 1
            continue
        for block in LDJSON.findall(new):
            json.loads(block)  # raises on a broken block
        if not dry:
            f.write_bytes(new.encode("utf-8"))
        changed += 1
    print(f"{changed} pages {'would change' if dry else 'changed'}, {bad} unmatched")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main("--dry" in sys.argv))
