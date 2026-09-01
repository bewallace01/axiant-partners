"""One-shot — strip <a> wrappers pointing to a list of dead URL slugs.
Run from repo root: python scripts/strip_dead_links.py
"""
from __future__ import annotations

import re
import pathlib

DEAD_SLUGS = [
    # Phase 3 — industry-child pages
    "avoid-payroll-to-draw-timing-mistakes",
    "avoid-supplier-cod-traps-material-prices-spike",
    "contractor-cash-flow-red-flags-before-applying-financing",
    "contractor-financing-mistakes-kill-approvals",
    "defense-contracts-equipment-financing-bid-axiant",
    "documentation-mistakes-delay-contractor-funding",
    "how-to-cover-materials-and-payroll-before-the-first-draw",
    "how-to-finance-used-equipment-without-overpaying",
    "mistakes-financing-used-equipment-contractors",
    "steel-lumber-prices-finance-job",
    "why-contractors-get-stuck-in-underwriting",
    "win-more-bids-by-financing-equipment-instead-of-draining-working-capital",
    "working-capital-vs-equipment-financing-contractors",
    "bridge-net-30-net-45-gap-without-missing-fuel-and-payroll",
    "detention-layover-pay-cash-crunch",
    "pre-peak-freight-capacity-financing-plan",
    "truck-note-lease-payment-slow-freight-weeks",
    # Phase 4 — thin article pages
    "arkansas-trucking-owner-operator-financing",
    "colorado-craft-brewery-financing",
    "florida-hurricane-contractor-financing",
    "michigan-auto-tier-1-supplier-financing",
    "north-dakota-bakken-oilfield-financing",
    "washington-apple-orchard-financing",
    "sba-loan-manufacturing-lost-supplier-overseas-conflict-pivot",
    "sba-pre-approval-how-long-valid",
    "veterinary-practice-loan-vs-small-business-loan",
    "why-term-loan-funding-keeps-getting-pushed-back",
    "open-line-of-credit-now-before-wartime-inflation-rates-higher",
    "reasons-cre-loan-approval-taking-forever",
    "why-cre-loan-keeps-coming-back-for-more-documents",
    "why-bridge-loan-keeps-coming-back-for-more-documents",
    "war-fuel-material-costs-cash-flow-squeezed-options",
    "whats-keeping-you-from-refinancing-business-debt",
    "reasons-working-capital-loan-keeps-denied",
    "revenue-based-financing-professional-services",
    "finance-inventory-new-ecommerce-startup",
    "why-lender-keeps-asking-for-more-documents",
]

REPO = pathlib.Path(__file__).resolve().parent.parent
total_fixes = 0

for f in REPO.rglob("*.html"):
    try:
        text = f.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    if not any(s in text for s in DEAD_SLUGS):
        continue
    new_text = text
    for slug in DEAD_SLUGS:
        # Match <a href="...slug..."> OR <a href='...slug...'> with optional attrs
        # Capture inner text and replace with just inner text.
        pattern = re.compile(
            r"<a\s+href=([\"'])([^\"']*?" + re.escape(slug) + r"[^\"']*?)\1(?:\s[^>]*)?>([^<]*)</a>",
            re.IGNORECASE,
        )
        new_text, n = pattern.subn(r"\3", new_text)
        if n:
            total_fixes += n
    if new_text != text:
        f.write_text(new_text, encoding="utf-8")
        rel = f.relative_to(REPO)
        print(f"fixed: {rel}")

print(f"\nTotal additional <a> wrappers stripped: {total_fixes}")

# Verify remaining
remaining = []
for f in REPO.rglob("*.html"):
    try:
        text = f.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for slug in DEAD_SLUGS:
        if slug in text:
            remaining.append((str(f.relative_to(REPO)), slug))

if remaining:
    print(f"\n{len(remaining)} reference(s) still in HTML (likely in plain text, not links):")
    for f, s in remaining:
        print(f"  {f} :: {s}")
else:
    print("\nClean — zero remaining references.")
