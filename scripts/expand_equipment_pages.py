#!/usr/bin/env python3
"""Expand equipment pages under 2500 words with SEO-optimized content blocks."""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
EQUIPMENT_DIR = BASE / "equipment"

# Content blocks - uses {name} placeholder
EXPANSION_BLOCK = '''
            <section class="about-section">
                <h2>Choosing the Right {name} for Your Operation</h2>
                <p>Before applying for {name} financing, clarify your needs: capacity, throughput, and how the equipment fits your workflow. Get written quotes from reputable dealers or integrators. Compare new vs used—<a href="/equipment-financing/articles/can-you-finance-used-equipment/">many lenders finance used equipment</a> when condition is documented. Consider bundling with related equipment for larger deals that may secure better terms. Plan for installation lead times and training. Use our <a href="/calculator.html">financing calculator</a> to estimate payments.</p>
            </section>

            <section class="about-section">
                <h2>Application Checklist for {name} Financing</h2>
                <p>Gather these before applying: 3–6 months of business bank statements; prior-year tax returns; current-year P&amp;L; a detailed equipment quote with specs and pricing; business formation documents (LLC, Corp); and proof of time in business. Multi-location or franchise operations may need additional documentation. Complete applications receive faster decisions—typically 24–48 hours for equipment financing. <a href="/equipment-financing/articles/what-do-lenders-look-at-equipment-financing-approval/">What lenders look at</a>.</p>
            </section>

            <section class="about-section">
                <h2>Tax Benefits: Section 179 and Bonus Depreciation</h2>
                <p>{name} typically qualifies for <strong>Section 179</strong> (deduct full purchase price in year of purchase, subject to limits) and <strong>bonus depreciation</strong>. Lease payments are usually fully deductible as operating expenses. These benefits can significantly reduce the net cost of financing—consult your CPA for your situation.</p>
            </section>
'''

def count_words(html: str) -> int:
    """Count words in body content, stripping scripts/styles/tags."""
    text = re.sub(r'<script[^>]*>[\s\S]*?</script>', '', html, flags=re.IGNORECASE)
    text = re.sub(r'<style[^>]*>[\s\S]*?</style>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    words = [w for w in text.split() if len(w) > 1 or w.isalnum()]
    return len(words)

def get_display_name(slug: str) -> str:
    """Convert slug to display name (e.g. pallet-jacks -> Pallet Jacks)."""
    return slug.replace('-', ' ').title()

def has_expansion(html: str) -> bool:
    """Check if page already has our expansion block."""
    return "Application Checklist for" in html and "Choosing the Right" in html

def expand_page(path: Path, slug: str) -> bool:
    """Inject expansion block before Process section. Returns True if modified."""
    html = path.read_text(encoding='utf-8')
    if count_words(html) >= 2500:
        return False
    if has_expansion(html):
        return False

    name = get_display_name(slug)
    block = EXPANSION_BLOCK.strip().format(name=name)

    # Insert before "Process" section
    for marker in ['<h2>Process</h2>', '<h2>How the Process Works</h2>', '<h2>Financing Process</h2>']:
        pos = html.find(marker)
        if pos != -1:
            section_start = html.rfind('<section', 0, pos)
            if section_start >= 0:
                html = html[:section_start] + block.strip() + '\n            \n            ' + html[section_start:]
                path.write_text(html, encoding='utf-8')
                return True
    return False

def main():
    expanded = []
    for cat in sorted(EQUIPMENT_DIR.iterdir()):
        if not cat.is_dir():
            continue
        idx = cat / "index.html"
        if not idx.exists():
            continue
        slug = cat.name
        if expand_page(idx, slug):
            expanded.append(slug)
    print(f"Expanded {len(expanded)} pages: {', '.join(expanded)}")
    for slug in expanded:
        path = EQUIPMENT_DIR / slug / "index.html"
        wc = count_words(path.read_text(encoding='utf-8'))
        print(f"  {slug}: ~{wc} words")

if __name__ == "__main__":
    main()
