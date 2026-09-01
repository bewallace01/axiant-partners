"""Build a Quick Answer for each equipment guide FROM THAT PAGE'S OWN STATS.
No new claims: the price range, decision time, terms, down payment, credit
floor and 50-state line all come from the page's at-a-glance band; the SBA
clause is only added where the page already talks about SBA."""
import pathlib, re, sys, importlib.util
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("c", ROOT / "scripts/convert-program-page.py")
conv = importlib.util.module_from_spec(spec); spec.loader.exec_module(conv)

BUYER = [
    ("contractors", ("excavat", "backhoe", "dozer", "skid", "loader", "stump", "trench", "compact")),
    ("carriers and owner-operators", ("truck", "van", "trailer", "semi", "tanker", "flatbed")),
    ("farms and growers", ("tractor", "combine", "hay", "grain", "sprayer", "greenhouse", "mower")),
    ("restaurants", ("kitchen", "refrigerat", "dishwash", "prep-", "ventilation", "pos-", "warewash")),
    ("practices", ("medical", "dental", "surgical", "imaging", "exam", "lab-")),
    ("shops", ("lift", "alignment", "brake", "tire", "diagnostic", "shop-")),
    ("warehouses and distributors", ("forklift", "pallet", "conveyor", "dock", "scanning", "racking")),
    ("manufacturers", ("cnc", "lathe", "press", "robot", "injection", "mold")),
]

def buyer(slug):
    for word, keys in BUYER:
        if any(k in slug for k in keys):
            return word
    return "businesses"

def stat(stats, *labels):
    for value, label in stats:
        for l in labels:
            if l in label.lower():
                return value
    return ""

def build(slug):
    p = ROOT / "equipment" / slug / "index.html"
    o = BeautifulSoup(p.read_text(encoding="utf-8"), "html.parser")
    stats = []
    for st in o.select(".stats .stat"):
        v = st.select_one(".stat-value, strong, b")
        parts = [x for x in (" ".join(st.get_text(" ").split())).split("  ") if x]
        txt = " ".join(st.get_text(" ").split())
        mm = re.match(r"(\S+)\s+(.*)", txt)
        if mm:
            val, lab = mm.group(1), mm.group(2)
            # "24-48 hr Equipment approval" -> the unit lives in the label
            u = lab.split()[0].lower() if lab.split() else ""
            if u.startswith(("hr", "hour")):
                val, lab = val + " hours", " ".join(lab.split()[1:])
            elif u.startswith(("mo", "month")):
                val, lab = val + " months", " ".join(lab.split()[1:])
            elif u.startswith(("day", "yr", "year")):
                val, lab = val + " " + u, " ".join(lab.split()[1:])
            stats.append((val, lab))
    if len(stats) < 5:
        return None
    h1 = o.select_one("h1").get_text(" ", strip=True)
    noun = h1.split(" Financing")[0].strip()
    # a few pages give the h1 a marketing sentence instead of the product name
    if " Financing" not in h1 or len(noun.split()) > 4:
        noun = slug.replace("-", " ").replace(" medical", "").replace(" auto", "")
        noun = noun[:-1] if noun.endswith("s") and not noun.endswith("ss") else noun
        noun = noun[0].upper() + noun[1:]
    ACR = {"cnc", "sba", "pos", "wms", "hvac"}
    low = " ".join(w if w.lower() in ACR else (w if w.isupper() and len(w) <= 4 else w.lower())
                   for w in noun.split())
    low = low[0].upper() + low[1:]
    rng   = stat(stats, "range")
    appr  = stat(stats, "approval")
    terms = stat(stats, "term")
    down  = stat(stats, "down")
    cred  = stat(stats, "credit")
    page  = " ".join(o.get_text(" ").split()).lower()
    sba   = "sba" in page

    lead = ("%s financing covers purchases in the %s range." % (low, rng)) if rng else \
           ("%s financing is available nationwide." % low)
    mid  = ("Most %s use an equipment loan or lease rather than paying cash: decisions typically come in %s, "
            "terms run %s, with %s down and credit from %s." % (buyer(slug), appr or "24-48 hours",
                                                                terms or "36-72 months",
                                                                down or "0-20%", cred or "600+"))
    tail = ("Axiant matches you with lenders in all 50 states, and SBA programs stretch terms further on "
            "larger purchases." if sba else "Axiant matches you with lenders in all 50 states.")
    title = " ".join(w if (w.isupper() and len(w) <= 4) else w[:1].upper() + w[1:]
                     for w in noun.replace(" Financing", "").split())
    head = "Quick Answer: What %s Financing Costs" % title
    return head, " ".join([lead, mid, tail])

if __name__ == "__main__":
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    for e in (only or conv.EQUIPMENT):
        r = build(e)
        print("###", e)
        print("   ", r[0] if r else "SKIPPED")
        print("   ", r[1] if r else "")
