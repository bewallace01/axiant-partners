"""
1. Remove Related Equipment/Financing Guides + General Financing Resources from equipment guides
2. Add equipment-guide class to form-container for full-width styling
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EQUIPMENT_DIR = os.path.join(ROOT, "equipment")


def process_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # Add equipment-guide class to form-container blog-post-content
    content = content.replace(
        'class="form-container blog-post-content"',
        'class="form-container blog-post-content equipment-guide"'
    )

    # Remove: from <h2>Related...Guides</h2> through all uls until <h2>Apply for
    pattern = (
        r'\s*<h2>Related (?:Equipment )?Financing Guides?</h2>.*?'
        r'(?=<h2>Apply for )'
    )
    content = re.sub(pattern, "\n            \n", content, flags=re.DOTALL)

    if content != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    count = 0
    for folder in os.listdir(EQUIPMENT_DIR):
        path = os.path.join(EQUIPMENT_DIR, folder, "index.html")
        if os.path.isfile(path):
            if process_file(path):
                count += 1
                print("Updated:", folder)
    print("\nUpdated", count, "files")


if __name__ == "__main__":
    main()
