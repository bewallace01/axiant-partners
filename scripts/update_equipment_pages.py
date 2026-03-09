"""Add equipment-specific content and hub elements to all how-to-finance pages."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EQUIPMENT_DIR = os.path.join(ROOT, "equipment")
CONTENT_PATH = os.path.join(ROOT, "scripts", "equipment_specific_content.json")

with open(CONTENT_PATH, encoding="utf-8") as f:
    content = json.load(f)


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


def folder_to_title(folder):
    return " ".join(w.capitalize() for w in folder.split("-"))


def build_at_glance(glance):
    return f'''            <div class="at-a-glance-box" style="background:var(--bg-secondary); border:1px solid var(--border-color); border-radius:8px; padding:1rem 1.25rem; margin:1.5rem 0;">
                <h3 style="margin-top:0; font-size:1rem;">At a Glance</h3>
                <ul style="margin:0; padding-left:1.25rem; list-style:disc;">
                    <li><strong>Cost range:</strong> {glance["cost"]}</li>
                    <li><strong>Typical terms:</strong> {glance["terms"]}</li>
                    <li><strong>Typical approval:</strong> {glance["approval"]}</li>
                </ul>
            </div>

'''


def build_specific_section(folder, specific):
    title = folder_to_title(folder)
    return f'''            <h2>Why {title} Financing Is Different</h2>
            <p>{specific}</p>

'''


def main():
    dirs = get_how_to_dirs()
    how_to_map = {d["folder"]: d["how_to"] for d in dirs}
    updated = 0
    skipped = 0

    for d in dirs:
        folder = d["folder"]
        how_to = d["how_to"]
        data = content.get(folder)
        if not data or not data.get("glance") or not data.get("specific"):
            print("Skip (no content):", folder)
            skipped += 1
            continue

        html_path = os.path.join(EQUIPMENT_DIR, folder, how_to, "index.html")
        if not os.path.exists(html_path):
            print("Skip (no file):", folder)
            skipped += 1
            continue

        with open(html_path, encoding="utf-8") as f:
            html = f.read()

        changed = False

        # 1. Add At a Glance after </figure> if not present
        if "at-a-glance-box" not in html:
            if "</figure>\n\n            <h2>" in html:
                html = html.replace(
                    "</figure>\n\n            <h2>",
                    f"</figure>\n\n{build_at_glance(data['glance'])}            <h2>",
                )
                changed = True
            elif "</figure>\n" in html:
                # Insert before next tag
                html = re.sub(
                    r"(</figure>\s*\n)\s*(<h2>|<div)",
                    r"\1\n" + build_at_glance(data["glance"]) + r"            \2",
                    html,
                    count=1,
                )
                changed = True

        # 2. Add equipment-specific section if not present
        specific_title = f"Why {folder_to_title(folder)} Financing Is Different"
        if specific_title not in html:
            # Match h2 + paragraph (paragraph may contain <a>, <strong> etc.)
            pattern = r"(<h2>How Do You Finance[^<]+</h2>\s*<p>[\s\S]*?</p>)\s*(\n\s*<h2>)"

            def repl(m):
                return m.group(1) + "\n\n" + build_specific_section(folder, data["specific"]) + "            " + m.group(2)

            new_html, n = re.subn(pattern, repl, html, count=1)
            if n:
                html = new_html
                changed = True

        if changed:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)
            print("Updated:", folder)
            updated += 1
        else:
            skipped += 1

    print("\nDone. Updated:", updated, "Skipped:", skipped)


if __name__ == "__main__":
    main()
