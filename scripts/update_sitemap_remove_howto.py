"""Remove equipment/how-to-finance-* URLs from sitemap (consolidated into equipment/category/)"""
import re

with open("sitemap.xml", "r", encoding="utf-8") as f:
    content = f.read()

# Remove entire <url>...</url> blocks that contain how-to-finance in the loc
pattern = (
    r'  <url>\s*\n'
    r'    <loc>https://www\.axiantpartners\.com/equipment/[^/]+/how-to-finance-[^<]+</loc>\s*\n'
    r'    <lastmod>[^<]+</lastmod>\s*\n'
    r'    <changefreq>[^<]+</changefreq>\s*\n'
    r'    <priority>[^<]+</priority>\s*\n'
    r'  </url>\s*\n'
)
content = re.sub(pattern, "", content)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(content)

print("Removed how-to-finance URLs from sitemap")
