#!/usr/bin/env python3
"""Fix malformed left rail: close first blog-rail-card before second."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Pattern: meta item closing div, then immediately (no proper card close) another blog-rail-card
# We need to insert </div> between them
FIX_PATTERN = re.compile(
    r'(<div class="blog-rail-meta-item">.*?</div>)\s*'
    r'(<div class="blog-rail-card">\s*<div class="blog-rail-quick-answer">)',
    re.DOTALL,
)
FIX_REPLACEMENT = r'\1\n        </div>\n        \2'

# After the fix, we have an extra </div> - remove one before </aside> in left rail
# The left rail ends with </div></div></aside> and should end with </div></aside>
EXTRA_DIV_PATTERN = re.compile(
    r'(<aside class="blog-post-rail-left">.*?)'
    r'</div>\s*</div>\s*</aside>',
    re.DOTALL,
)


def fix_html(html: str) -> str:
    if "blog-rail-quick-answer" not in html or "blog-post-rail-left" not in html:
        return html
    # Apply fix
    new_html = FIX_PATTERN.sub(FIX_REPLACEMENT, html, count=1)
    if new_html == html:
        return html
    # Now we have one extra </div> - the original had two at end (inner card, outer card)
    # We added </div> to close outer, so we have outer closed, inner card, inner closed, and one extra
    # The structure: ...</div> (meta) </div> (outer - we added) <div class="blog-rail-card">...
    # ...</div> (inner card) </div> (extra - was closing outer)
    # So we need to remove the last </div> before </aside> in the left rail.
    # Match the left rail section and remove one </div>
    m = re.search(
        r'(<aside class="blog-post-rail-left">)(.*?)(</aside>)',
        new_html,
        re.DOTALL,
    )
    if not m:
        return new_html
    left_content = m.group(2)
    # Count: we should have first card, second card. First card: open, close (we added). Second: open, close.
    # So we have two </div>s for the two cards. But we might have more from nested divs.
    # The quick-answer has: <div class="blog-rail-quick-answer"><div class="blog-rail-quick-content">...
    # So we have blog-rail-card, blog-rail-quick-answer, blog-rail-quick-content. That's 3 divs in the second card.
    # Second card structure: <div class="blog-rail-card"> <div class="blog-rail-quick-answer"><div class="blog-rail-quick-content">...</div></div> </div>
    # So 3 closes for the inner content. The second card needs 1 close. So we have ...</div></div></div> for the second card's content.
    # Then we had </div> for the first card. So before fix we had: </div></div></div></div> - 4 divs. The last one closed the first card.
    # After our fix we have: </div>(meta) </div>(first card - new) <div...> </div></div></div> (second card) </div>(extra)
    # So we have one extra </div> at the end. We need to remove the last </div> before </aside>.
    # Replace </div>\s*</aside> at the end of left_content with </aside>? No - we need one </div> to close the second card.
    # The second card: <div class="blog-rail-card"> ... </div> (closes quick-answer or quick-content?) ... 
    # <div class="blog-rail-quick-answer"><div class="blog-rail-quick-content">...</div></div> - 2 closes for the inner divs
    # Then </div> for the card. So we need </div></div></div> to close second card (quick-content, quick-answer, card).
    # So the left rail ends with ...</div></div></div> (second card) </div> (was first card, now extra). So we remove the last one.
    # Pattern: </div>\s*</aside> - we need to remove one </div> before </aside>. So we replace (</div>)(\s*</aside>) with \2?
    # That would remove the last </div> before </aside>. So we'd have ...</div></div></div></aside> - the second card wouldn't be closed!
    # Let me count again. Second card contains: blog-rail-quick-answer which contains blog-rail-quick-content. So:
    # <div class="blog-rail-card">  open 1
    #   <div class="blog-rail-quick-answer">  open 2
    #     <div class="blog-rail-quick-content">  open 3
    #       ...
    #     </div>  close 3
    #   </div>  close 2
    # </div>  close 1
    # So we need 3 </div>s to close the second card. Then we had 1 </div> for the first card. Total 4 </div>s before </aside>.
    # After our fix we have: first card properly closed with our new </div>. So we have: first card content, </div>(close first), second card... </div></div></div>(close second), </div>(extra - was closing first, but first is already closed). So we have one extra </div>. We need to remove it. So we replace the last `</div>` before `</aside>` - but we need to remove only one. The last </div> before </aside> is the extra one. So we do:
    # Replace (.*)(</div>)(\s*</aside>) with \1\3 - that would remove the last </div> before </aside>. But that might be too greedy - .* could match a lot. Let me be more specific. We want to remove one </div> from the end of the left rail. The left content ends with newlines, spaces, </div>, maybe more </div>s, then </aside>. The structure is ...</div></div></div></div>\n      </aside>. We want ...</div></div></div>\n      </aside>. So we need to remove one </div>. The regex: r'(.*)(</div>)(\s*</aside>)$' - but the content is in the middle of the document. So we need to only affect the left rail. Let me do a replace within the left rail: the left rail inner content ends with multiple </div> and then we have the closing tags. Actually the aside structure is <aside> CONTENT </aside>. So CONTENT ends right before </aside>. So we need to replace CONTENT such that we remove one </div> from its end. So we could match (.*)</div>(\s*</aside>) and replace with \1\2 - that would remove the last </div> before </aside> in the entire document. That might be wrong if there are other asides. Let me be more careful - we only want to fix the blog-post-rail-left aside.
    inner = m.group(2)
    # Count the last few </div>s - we need to remove exactly one
    # Match from the end: optional whitespace, </div>, optional whitespace, and keep going until we've matched one </div> to remove
    # Simple: replace the pattern </div>(\s*)</aside> at the end of the aside content with \1</aside> - but only the last occurrence within the aside
    # So we need to find the position. The left_content ends with something like:
    # "...</div></div></div>\n        </div>\n      </aside>"
    # We want to remove one </div> - the one that's a duplicate. So we replace the LAST occurrence of "</div>" before "</aside>" in the left rail. We can do:
    # Reverse, replace first "</div>" with "", reverse. Or we can use a regex that matches the minimal amount. 
    # Pattern: (.*)</div>(\s*)(</aside>) - we'd match greedily from the start, so .* would match as much as possible, and we'd get the last </div>. Replace with \1\2\3. So we remove one </div>. Good.
    # But we need to restrict to the left rail. The m has the full match. So new_html has ...<aside>INNER</aside>... We're replacing INNER. So we need to fix INNER and then do the full replace. Let me do:
    fixed_inner = re.sub(r'(.*)</div>(\s*)$', r'\1\2', inner, count=1)
    if fixed_inner == inner:
        return new_html
    # Wait, that would remove the last </div> from inner. But inner doesn't include </aside> - it's the content between <aside> and </aside>. So inner ends with ...</div></div></div></div> and we want to remove one, so ...</div></div></div>. The regex (.*)</div>(\s*)$ - the $ is end of string. So we match (.*)(</div>)(\s*)$ and replace with \1\2. So we remove the last </div>. Good. But (.*) is greedy so we'd match everything up to the last </div>. So we'd get the right one. Good.
    result = new_html.replace(m.group(0), m.group(1) + fixed_inner + m.group(3))
    return result


def main():
    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        try:
            html = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"Skip {path}: {e}")
            continue
        if "blog-rail-quick-answer" not in html or "blog-post-rail-left" not in html:
            continue
        # Check if it has the malformed pattern (nested blog-rail-card)
        if '<div class="blog-rail-meta-item">' not in html:
            continue
        if 'blog-rail-meta-item">' in html and '<div class="blog-rail-card">' in html and 'blog-rail-quick-answer' in html:
            # Check for the specific malformed nesting: meta followed directly by another card
            if re.search(r'blog-rail-meta-item">.*?</div>\s*<div class="blog-rail-card">\s*<div class="blog-rail-quick-answer">', html, re.DOTALL):
                new_html = fix_html(html)
                if new_html != html:
                    path.write_text(new_html, encoding="utf-8")
                    print(f"Fixed: {path.relative_to(ROOT)}")
                    count += 1
    print(f"\nFixed {count} articles.")


if __name__ == "__main__":
    main()
