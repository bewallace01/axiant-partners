# -*- coding: utf-8 -*-
"""
Apply SEO/GEO/AEO optimization to all meta descriptions:
- SEO: keyword front, 140-160 chars, unique
- GEO: "for U.S. [audience]" or "nationwide" where relevant
- AEO: "How to", "Learn", "What is", "Compare", "When to" phrasing
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_LEN = 160
MIN_LEN = 135

# Path segment -> audience for GEO
AUDIENCE = {
    "backhoes": "contractors", "excavators": "contractors", "bulldozers": "contractors",
    "mini-excavators": "contractors", "skid-steers": "contractors", "wheel-loaders": "contractors",
    "dump-trucks": "contractors", "forklifts": "warehouses", "trailers": "haulers",
    "semi-trucks": "owner-operators", "flatbed-trucks": "haulers", "box-trucks": "delivery",
    "tanker-trucks": "carriers", "refrigerated-trucks": "fleets", "log-trucks": "operators",
    "combines": "farmers", "tractors": "farmers", "grain-equipment": "farmers",
    "hay-balers": "farmers", "sprayers": "farmers", "commercial-mowers": "landscapers",
    "zero-turn-mowers": "landscapers", "stump-grinders": "tree care",
    "dental-equipment": "practices", "medical-imaging": "practices", "surgical-equipment": "practices",
    "diagnostic-devices-medical": "healthcare practices", "exam-procedure-equipment": "practices",
    "alignment-racks": "auto shops", "brake-rotor-equipment": "auto shops",
    "commercial-kitchen": "restaurants", "restaurant-refrigeration": "restaurants",
    "bucket-trucks": "utility contractors", "scanning-wms": "warehouses",
    "lathes-milling-machines": "manufacturers", "press-brakes": "metal fabricators",
}

def topic_from_path(rel):
    """Derive topic from path for equipment and articles."""
    parts = rel.replace("\\", "/").split("/")
    if "equipment" in parts:
        idx = parts.index("equipment")
        if idx + 1 < len(parts) and parts[idx + 1] != "index.html":
            name = parts[idx + 1].replace("-", " ").title()
            if name in ("Semi Trucks", "Box Trucks", "Flatbed Trucks", "Tanker Trucks",
                       "Refrigerated Trucks", "Log Trucks", "Skid Steers", "Wheel Loaders",
                       "Mini Excavators", "Bucket Trucks", "Zero Turn Mowers", "Commercial Mowers",
                       "Stump Grinders", "Grain Equipment", "Hay Balers", "Press Brakes",
                       "Medical Imaging", "Dental Equipment", "Commercial Kitchen",
                       "Restaurant Refrigeration", "Diagnostic Devices Medical"):
                return name
            return name
    return None

def audience_from_path(rel):
    """Get GEO audience from path."""
    parts = rel.replace("\\", "/").lower().split("/")
    for p in parts:
        if p in AUDIENCE:
            return AUDIENCE[p]
    if "equipment" in parts:
        return "U.S. businesses"
    if "construction-business-financing" in rel or "trucking-business-financing" in rel:
        return "contractors" if "construction" in rel else "carriers"
    if "articles" in parts or "blog" in rel:
        return None
    return "U.S. businesses"

def optimize_description(rel, current, title, h1):
    """Produce SEO/GEO/AEO-optimized description (140-160 chars)."""
    plain = re.sub(r"&[a-z]+;", " ", current)
    plain = re.sub(r"\s+", " ", plain).strip()
    # Already good length and has GEO + verb
    has_geo = bool(re.search(r"\b(for U\.S\.|nationwide|for (contractors|farmers|restaurants|auto shops|practices|haulers))\b", plain, re.I))
    has_verb = bool(re.search(r"\b(How to|Learn|What is|Compare|When to|See|Get|Find)\b", plain, re.I))
    if MIN_LEN <= len(plain) <= MAX_LEN and has_geo and has_verb:
        return None  # no change

    topic = topic_from_path(rel)
    audience = audience_from_path(rel)
    base = rel.replace("\\", "/")

    # Equipment hub or subpage
    if "/equipment/" in base and "index.html" in base:
        t = topic or "Equipment"
        aud = audience or "U.S. businesses"
        return f"{t} financing for {aud}: how to get loans or leases. Fast approvals nationwide."[:MAX_LEN]

    # Industry landing pages
    if base.endswith("-business-financing.html") or base.endswith("-financing.html"):
        industry = base.split("/")[-1].replace("-business-financing.html", "").replace("-financing.html", "").replace("-", " ").title()
        return f"{industry} financing for U.S. businesses: equipment, SBA, working capital. Compare options and apply."[:MAX_LEN]

    # Service pages (root)
    if base in ("equipment-financing.html", "sba-loans.html", "working-capital-loans.html",
                "business-line-of-credit.html", "business-term-loans.html", "commercial-real-estate-loans.html",
                "commercial-bridge-loans.html", "fix-and-flip.html", "merchant-cash-advance.html",
                "securities-based-lending.html", "revenue-based-financing.html"):
        # Keep current if 130-160, else shorten with GEO
        if len(plain) >= 120:
            if "nationwide" not in plain and "U.S." not in plain:
                return (plain[:MAX_LEN - 15] + " nationwide.")[:MAX_LEN]
        return None

    # Articles and blog indexes
    if "/articles/" in base or "blog" in base:
        # Start with Learn/How to/What if missing
        if not re.match(r"^(How to|What is|What to|Learn|Compare|When to|Why|Discover)\b", plain, re.I):
            prefix = "Learn "
            if "how" in plain.lower() or "qualify" in plain.lower():
                prefix = "How to "
            elif "what" in plain.lower() or "requirements" in plain.lower():
                prefix = "What "
            new_ = prefix + plain[0].lower() + plain[1:] if plain else plain
            new_ = new_[:MAX_LEN]
            if audience:
                new_ = (new_.rstrip(".") + " for U.S. businesses.")[:MAX_LEN]
            return new_ if len(new_) >= MIN_LEN else new_ + " Apply now."[:MAX_LEN]
        if audience and "for U.S." not in plain and "nationwide" not in plain:
            return (plain.rstrip(".") + " Nationwide.")[:MAX_LEN]
        return None

    # Construction / trucking pain points
    if "construction-business-financing" in base or "trucking-business-financing" in base:
        if len(plain) < MIN_LEN or not has_geo:
            aud = "U.S. contractors" if "construction" in base else "U.S. carriers"
            return (plain[:120].rstrip(".") + f" How to fix it. Financing for {aud}.")[:MAX_LEN]
        return None

    # Default: ensure GEO and length
    if len(plain) > MAX_LEN:
        plain = plain[:MAX_LEN - 4].rsplit(" ", 1)[0] + "."
    if audience and not has_geo:
        plain = (plain.rstrip(".") + f" For {audience} nationwide.")[:MAX_LEN]
    return plain if 135 <= len(plain) <= 160 else None

def main():
    count = 0
    for dirpath, _, files in os.walk(ROOT):
        if "/.git" in dirpath.replace("\\", "/"):
            continue
        for f in files:
            if not f.lower().endswith(".html"):
                continue
            path = os.path.join(dirpath, f)
            rel = os.path.relpath(path, ROOT)
            try:
                text = open(path, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            m = re.search(r'<meta\s+name=["\']description["\'][^>]+content=(["\'])([^"\']*)\1', text, re.I)
            if not m:
                continue
            title_m = re.search(r"<title>([^<]+)</title>", text, re.I)
            h1_m = re.search(r"<h1[^>]*>([^<]+)</h1>", text, re.I)
            title = (title_m.group(1) if title_m else "").strip()
            h1 = re.sub(r"<[^>]+>", "", (h1_m.group(1) if h1_m else "")).strip()
            current = m.group(2)
            new_desc = optimize_description(rel, current, title, h1)
            if new_desc is None:
                continue
            new_content = m.group(0).replace(m.group(2), new_desc, 1)
            new_text = text.replace(m.group(0), new_content, 1)
            if new_text != text:
                open(path, "w", encoding="utf-8").write(new_text)
                count += 1
                print(rel[:70])
    print("DONE", count)

if __name__ == "__main__":
    main()
