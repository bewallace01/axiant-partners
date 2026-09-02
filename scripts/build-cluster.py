#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a v2 article cluster: the articles, then the hub, from one data module.

    python scripts/build-cluster.py truck_title
    python scripts/build-cluster.py truck_title --apply
    python scripts/build-cluster.py --all --apply

A cluster module lives at scripts/cluster_<name>.py and exports CLUSTER (the
pillar, hub path and copy) plus ARTICLES. The renderer is article_v2.py, shared
with every other cluster so the shape cannot drift between them.

The hub is generated from what is on disk rather than from ARTICLES, so its
cards cannot fall behind the articles - the failure that left
generate_sitemap.py 188 URLs behind the site.
"""
import argparse, html, importlib, io, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import article_v2 as A

ROOT = A.ROOT
CLUSTERS = ["truck_title", "res_business_loan", "heloc", "equip_appraisal", "security_guard",
             "aircraft", "marine", "drone", "datacenter"]


def words(s):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S | re.I)
    return len(re.sub(r"<[^>]+>", " ", t).split())


def build(name, apply_changes):
    mod = importlib.import_module(f"cluster_{name}")
    c, arts = mod.CLUSTER, mod.ARTICLES
    v, header, footer = A.chrome()
    hub_dir = os.path.join(ROOT, c["hub"].replace("/", os.sep))

    print(f"\n=== {name}  ->  {c['hub']} ===")
    seen = set()
    for a in arts:
        if a["slug"] in seen:
            raise SystemExit(f"duplicate slug in {name}: {a['slug']}")
        seen.add(a["slug"])
        out = A.render(a, c, v, header, footer)
        w = words(out)
        # a title past ~60 characters is truncated in the SERP, and the tail
        # that gets cut is the part the reader was meant to act on
        tl = len(html.unescape(a["title"]))
        flag = "  " if 1200 <= w <= 1800 and tl <= 60 else "!!"
        if tl > 60:
            print(f"  !! {a['slug']:46} title is {tl} chars, cut at ~60")
        if apply_changes:
            d = os.path.join(hub_dir, a["slug"])
            os.makedirs(d, exist_ok=True)
            io.open(os.path.join(d, "index.html"), "w",
                    encoding="utf-8", newline="").write(out)
        print(f"  {flag} {a['slug']:46} {w:5} words  {len(a['faqs'])} faqs  "
              f"{len(a['sections'])} sections")

    n, hub = A.build_hub(c, v, header, footer)
    if apply_changes:
        os.makedirs(hub_dir, exist_ok=True)
        io.open(os.path.join(hub_dir, "index.html"), "w",
                encoding="utf-8", newline="").write(hub)
    print(f"     hub: {n} article(s) indexed")
    return len(arts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cluster", nargs="?", default="")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    names = CLUSTERS if a.all else ([a.cluster] if a.cluster else [])
    if not names:
        print(__doc__)
        return 1
    print("APPLIED" if a.apply else "DRY RUN")
    total = 0
    for n in names:
        try:
            total += build(n, a.apply)
        except ModuleNotFoundError:
            print(f"\n=== {n} === not written yet (scripts/cluster_{n}.py)")
    print(f"\n  {total} article(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
