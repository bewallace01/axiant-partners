"""Add Common Mistakes and Financing Timeline sections to equipment pages that have When to Apply but not Common Mistakes."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EQUIPMENT_DIR = os.path.join(ROOT, "equipment")
NAMES_PATH = os.path.join(ROOT, "scripts", "equipment_guide_names.json")
with open(NAMES_PATH, encoding="utf-8") as f:
    names = json.load(f)


def get_dirs():
    result = []
    for d in os.listdir(EQUIPMENT_DIR):
        full = os.path.join(EQUIPMENT_DIR, d)
        if not os.path.isdir(full):
            continue
        for sub in os.listdir(full):
            if sub.startswith("how-to-finance"):
                result.append({"folder": d, "how_to": sub})
                break
    return result


def extra_sections(name):
    return f'''

            <h2>Common Mistakes to Avoid</h2>
            <p>Avoid these when financing {name}: skipping the equipment quote (lenders need it to structure the loan), applying with incomplete financials (causes delays), focusing on rate alone (terms, fees, and flexibility matter), and waiting until the last minute (rush approvals may limit your options). Compare at least 2–3 offers. Read the full agreement before signing—watch for prepayment penalties, collateral requirements, and insurance obligations. <a href="/equipment-financing/articles/red-flags-equipment-finance-agreements/">See red flags in equipment finance agreements</a>.</p>

            <h2>Financing Timeline: What to Expect</h2>
            <p>Standard equipment financing approval takes <strong>1–5 business days</strong> from application to funding. Day 1: submit application and documents. Days 2–3: lender review, possible follow-up questions. Day 4–5: approval, documentation, and funding. Funds typically go directly to the seller; you take possession once the deal closes. SBA loans add 30–60+ days. Having everything ready upfront can compress the timeline. <a href="/match.html">Get matched</a> to start the process.</p>
'''


def main():
    dirs = get_dirs()
    for d in dirs:
        folder = d["folder"]
        how_to = d["how_to"]
        name = names.get(folder)
        if not name:
            continue
        path = os.path.join(EQUIPMENT_DIR, folder, how_to, "index.html")
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            html = f.read()
        if "Common Mistakes to Avoid" in html:
            continue
        if "When to Apply for" not in html:
            continue
        # Insert before Step-by-Step (after Why Businesses Finance paragraph)
        pattern = r'(</p>\s*\n)(\s*<h2>Step-by-Step)'
        if re.search(pattern, html):
            html = re.sub(pattern, r'\1' + extra_sections(name) + r'\n            \2', html, count=1)
            with open(path, "w", encoding="utf-8") as f:
                f.write(html)
            print("Added:", folder)


if __name__ == "__main__":
    main()
