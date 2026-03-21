"""Fix double picture wrappers and backslash paths from webp-first script."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def fix(content: str) -> str:
    content = content.replace("<picture><picture>", "<picture>")
    content = content.replace("</picture></picture>", "</picture>")
    # Fix Windows backslashes in URLs
    content = content.replace('srcset="\\assets', 'srcset="/assets')
    content = content.replace('href="\\assets', 'href="/assets')
    content = content.replace("url('\\assets", "url('/assets")
    content = content.replace('url("\\assets', 'url("/assets')
    content = content.replace("\\assets\\", "/assets/")
    content = content.replace("\\assets/", "/assets/")
    return content

total = 0
for path in ROOT.rglob("*.html"):
    if "node_modules" in str(path) or ".git" in str(path):
        continue
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    new_text = fix(text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        total += 1
        print(path.relative_to(ROOT))
print(f"Fixed {total} files")
