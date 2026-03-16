"""
Equipment Guide Update Script:
1. Rename "How to Finance X" -> "X Financing Guide" everywhere
2. Add expansion content to reach 2k+ words
3. Add high apply-intent CTAs
Run: python scripts/equipment_guide_expansion.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EQUIPMENT_DIR = os.path.join(ROOT, "equipment")
CONTENT_PATH = os.path.join(ROOT, "scripts", "equipment_specific_content.json")
NAMES_PATH = os.path.join(ROOT, "scripts", "equipment_guide_names.json")

with open(CONTENT_PATH, encoding="utf-8") as f:
    content = json.load(f)
with open(NAMES_PATH, encoding="utf-8") as f:
    names = json.load(f)


def get_how_to_dirs():
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


def build_cta_box(name):
    return f'''
            <div class="apply-cta-inline" style="background:linear-gradient(135deg, var(--bg-secondary) 0%, rgba(45,127,184,0.08) 100%); border:1px solid var(--border-color); border-radius:12px; padding:1.25rem 1.5rem; margin:1.5rem 0; text-align:center;">
                <p style="margin:0 0 0.75rem; font-weight:600;">Ready to apply for {name} financing?</p>
                <p style="margin:0 0 1rem; font-size:0.95rem;">Submit once—we match you with lenders. Same-day response.</p>
                <a href="/match.html" class="btn-primary">Get Matched for {name} Financing</a>
            </div>
'''


def build_expansion_sections(name):
    """Content to add ~500 words - When to Apply, What to Have Ready, Why Finance vs Cash"""
    return f'''
            <h2>When to Apply for {name} Financing</h2>
            <p>Apply when you have a clear equipment need, a written quote from your dealer or vendor, and financials that show your business can support the payment. The best time to apply is <strong>before</strong> you need the equipment—approval often takes 1–5 days, but having documents ready speeds the process. If you're replacing aging equipment, expanding capacity, or fulfilling a new contract, applying now gives you time to compare offers without pressure. Don't wait until equipment fails or a project starts; early application improves your leverage and terms. <a href="/match.html">Axiant Partners</a> matches businesses with lenders—submit once and hear from us the same day.</p>

            <h2>What to Have Ready Before You Apply</h2>
            <p>Gather these before starting your application: <strong>3–6 months of business bank statements</strong>, last year's tax returns (business and personal if required), a recent profit and loss statement, your <strong>equipment quote or proposal</strong>, and basic business information (EIN, formation date, ownership). Having these ready reduces back-and-forth and speeds approval. If you have existing equipment loans or leases, have those statements available. Lenders may also ask for a voided check for ACH. The more organized your documentation, the faster you'll get funded. Use our <a href="/calculator.html">financing calculator</a> to estimate payments before you apply.</p>

            <h2>Why Businesses Finance {name} Rather Than Pay Cash</h2>
            <p>Paying cash ties up working capital that could fund payroll, inventory, or growth. Financing spreads the cost over the equipment's useful life, matches expenses to revenue, and preserves liquidity. Equipment loans and leases also offer <strong>tax benefits</strong>—Section 179 and bonus depreciation for purchases, lease payments as operating expenses. Many businesses prefer to finance so they can keep reserves for emergencies or opportunities. If your cost of capital is lower than the return on that cash elsewhere, financing makes sense. Even strong businesses often finance equipment to optimize cash flow.</p>

            <h2>Common Mistakes to Avoid</h2>
            <p>Avoid these when financing {name}: skipping the equipment quote (lenders need it to structure the loan), applying with incomplete financials (causes delays), focusing on rate alone (terms, fees, and flexibility matter), and waiting until the last minute (rush approvals may limit your options). Compare at least 2–3 offers. Read the full agreement before signing—watch for prepayment penalties, collateral requirements, and insurance obligations. <a href="/equipment-financing/articles/red-flags-equipment-finance-agreements/">See red flags in equipment finance agreements</a>.</p>

            <h2>Financing Timeline: What to Expect</h2>
            <p>Standard equipment financing approval takes <strong>1–5 business days</strong> from application to funding. Day 1: submit application and documents. Days 2–3: lender review, possible follow-up questions. Day 4–5: approval, documentation, and funding. Funds typically go directly to the seller; you take possession once the deal closes. SBA loans add 30–60+ days. Having everything ready upfront can compress the timeline. <a href="/match.html">Get matched</a> to start the process.</p>
'''


def main():
    dirs = get_how_to_dirs()
    updated = 0
    for d in dirs:
        folder = d["folder"]
        how_to = d["how_to"]
        name = names.get(folder)
        if not name:
            print("Skip (no name):", folder)
            continue

        html_path = os.path.join(EQUIPMENT_DIR, folder, how_to, "index.html")
        if not os.path.exists(html_path):
            print("Skip (no file):", folder)
            continue

        with open(html_path, encoding="utf-8") as f:
            html = f.read()

        guide_name = f"{name} Financing Guide"
        # Replace all "How to Finance X" variations with "X Financing Guide"
        for old in [f"How to Finance an {name}", f"How to Finance a {name}", f"How to Finance {name}"]:
            html = html.replace(old, guide_name)
        # Fix Related links for all equipment types
        for n2 in names.values():
            html = html.replace(f"How to Finance an {n2}", f"{n2} Financing Guide")
            html = html.replace(f"How to Finance a {n2}", f"{n2} Financing Guide")
            html = html.replace(f"How to Finance {n2}", f"{n2} Financing Guide")

        # Add CTA after At a Glance
        if 'apply-cta-inline' not in html:
            cta = build_cta_box(name)
            # After at-a-glance box, before next h2
            m = re.search(r'(</ul>\s*</div>)\s*\n(\s*<h2>)', html)
            if m:
                html = html[:m.end(1)] + '\n' + cta + '\n            ' + html[m.start(2):]
            elif "</div>\n\n            <h2>What " in html:
                html = html.replace("</div>\n\n            <h2>What ", f"</div>\n{cta}\n            <h2>What ", 1)

        # Add expansion sections - insert after Rates/Financing paragraph (after its </p>), before Step-by-Step
        if "When to Apply for" not in html and "What to Have Ready" not in html:
            expansion = build_expansion_sections(name)
            # Insert expansion between </p> and <h2>Step-by-Step (keep </p> to close rates paragraph)
            pattern = r'(</p>\s*\n)(\s*<h2>Step-by-Step)'
            if re.search(pattern, html):
                html = re.sub(pattern, r'\1' + expansion + r'\n            \2', html, count=1)

        # Add second CTA before final "Apply for" section
        if html.count('apply-cta-inline') < 2:
            cta2 = build_cta_box(name)
            # Insert before "Related Equipment" or "Related Financing"
            html = re.sub(
                r'(<h2>Related (?:Equipment )?Financing Guides?)',
                cta2 + r'\n            \1',
                html,
                count=1
            )

        # Strengthen final CTA section
        html = re.sub(
            r'(<h2>Apply for [^<]+ Financing</h2>\s*<p>)',
            r'\1<strong>Applications are reviewed within 24–48 hours.</strong> ',
            html
        )

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Updated:", folder)
        updated += 1

    print("\nDone. Updated:", updated)


if __name__ == "__main__":
    main()
