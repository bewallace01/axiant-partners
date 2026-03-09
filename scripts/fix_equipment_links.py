import re
with open("equipment.html", "r", encoding="utf-8") as f:
    t = f.read()
t = re.sub(r'(href="equipment/[^/]+)/how-to-finance-[^"]+/"', r'\1/"', t)
with open("equipment.html", "w", encoding="utf-8") as f:
    f.write(t)
print("Updated equipment.html links")
