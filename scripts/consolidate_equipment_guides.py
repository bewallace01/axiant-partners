"""
Consolidate equipment guides: move how-to-finance content into equipment/category/index.html
and delete how-to-finance-* subdirs. equipment/category/ becomes the single Excavator Financing Guide page.
"""
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EQUIPMENT_DIR = os.path.join(ROOT, "equipment")


def get_hub_to_guide():
    result = {}
    for d in os.listdir(EQUIPMENT_DIR):
        full = os.path.join(EQUIPMENT_DIR, d)
        if not os.path.isdir(full):
            continue
        for sub in os.listdir(full):
            if sub.startswith("how-to-finance"):
                result[d] = sub
                break
    return result


def consolidate_content(html: str, folder: str, how_to: str) -> str:
    """Transform guide HTML for consolidated URL equipment/folder/"""
    base = "https://axiantpartners.com"
    new_url = f"{base}/equipment/{folder}/"
    old_url = f"{base}/equipment/{folder}/{how_to}/"

    # Replace URLs
    html = html.replace(old_url, new_url)
    html = html.replace(f"/equipment/{folder}/{how_to}/", f"/equipment/{folder}/")

    # Related links: /equipment/any-folder/how-to-finance-anything/ -> /equipment/any-folder/
    html = re.sub(
        r'/equipment/([a-z0-9-]+)/how-to-finance-[^/"]+/',
        r'/equipment/\1/',
        html
    )

    # CSS/scripts: ../../../ -> ../  (guide is 3 levels deep, index is 2)
    html = html.replace("../../../critical.css", "../../critical.css")
    html = html.replace("../../../styles.css", "../../styles.css")
    html = html.replace("../../../language-switcher.js", "../../language-switcher.js")
    html = html.replace("../../../script.js", "../../script.js")
    html = html.replace("../../../logo-horizontal-transparent.png", "../../logo-horizontal-transparent.png")
    html = html.replace("../../../Axiant_light_logo.png", "../../Axiant_light_logo.png")

    # Breadcrumbs: remove 4th item (the how-to guide); keep Home > Equipment > Excavators
    # Pattern: {"@type":"ListItem","position":4,...} - remove that item
    bc_pattern = r',\s*\{[^}]*"@type":"ListItem"[^}]*"position":4[^}]*\}'
    html = re.sub(bc_pattern, "", html)

    # Fix breadcrumb position 3 to be last (no position 4)
    # Position 3's "item" should be the current page (equipment/folder/)
    # Already correct if we removed pos 4.

    # blog-back: Back to Excavator Financing -> Back to Equipment
    html = re.sub(
        r'<p class="blog-back"><a href="\.\./">&larr; Back to [^<]+</a></p>',
        '<p class="blog-back"><a href="/equipment.html">&larr; Back to Equipment</a></p>',
        html
    )

    return html


def main():
    mapping = get_hub_to_guide()

    for folder, how_to in mapping.items():
        guide_path = os.path.join(EQUIPMENT_DIR, folder, how_to, "index.html")
        hub_path = os.path.join(EQUIPMENT_DIR, folder, "index.html")

        if not os.path.exists(guide_path):
            print("Skip (no guide):", folder)
            continue

        with open(guide_path, encoding="utf-8") as f:
            content = f.read()

        content = consolidate_content(content, folder, how_to)
        with open(hub_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Consolidated:", folder, "->", hub_path)

        # Delete how-to-finance subdir
        guide_dir = os.path.join(EQUIPMENT_DIR, folder, how_to)
        shutil.rmtree(guide_dir)
        print("  Deleted:", guide_dir)

    print("\nDone. Now update equipment.html links and sitemap.")


if __name__ == "__main__":
    main()
