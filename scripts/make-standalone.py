"""Flatten a converted page into ONE self-contained fragment (title + style +
body) so it can be viewed without a local server. Picks the smallest local
webp for every <picture>, inlines it as a data URI, drops external scripts."""
import base64, pathlib, re, sys
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAXK = 200

def local(p):
    p = p.split('?')[0]
    f = ROOT / p.lstrip('/')
    return f if f.exists() and f.is_file() else None

def data_uri(f):
    mt = {'.webp': 'image/webp', '.png': 'image/png', '.jpg': 'image/jpeg',
          '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml'}.get(f.suffix.lower())
    if not mt:
        return None
    return 'data:%s;base64,%s' % (mt, base64.b64encode(f.read_bytes()).decode())

def main(name):
    src = ROOT / name
    s = BeautifulSoup(src.read_text(encoding='utf-8'), 'html.parser')

    for pic in s.find_all('picture'):
        cands = []
        for so in pic.find_all('source'):
            u = (so.get('srcset') or '').split()[0] if so.get('srcset') else ''
            f = local(u)
            if f and f.suffix.lower() == '.webp':
                cands.append(f)
            so.decompose()
        img = pic.find('img')
        if img is not None:
            f2 = local(img.get('src') or '')
            if f2 and f2.suffix.lower() == '.webp':
                cands.append(f2)
            cands = [c for c in cands if c.stat().st_size <= MAXK * 1024] or cands
            if cands:
                best = min(cands, key=lambda c: c.stat().st_size)
                u = data_uri(best)
                if u:
                    img['src'] = u
                    img.attrs.pop('srcset', None)
                    img.attrs.pop('sizes', None)

    for img in s.find_all('img'):
        v = img.get('src') or ''
        if v.startswith('data:'):
            continue
        f = local(v)
        if f:
            u = data_uri(f)
            if u:
                img['src'] = u
        img.attrs.pop('srcset', None)

    css = ""
    for l in list(s.find_all('link')):
        h = l.get('href') or ''
        if h.endswith('.css') or '.css?' in h:
            f = local(h)
            if f:
                css += f.read_text(encoding='utf-8') + "\n"
            l.decompose()
        elif 'fonts.googleapis' not in h and 'fonts.gstatic' not in h:
            l.decompose()

    # inline any url(/assets/x) still left in css
    def sub(m):
        f = local(m.group(1).strip('\'"'))
        u = data_uri(f) if f else None
        return 'url(%s)' % u if u else m.group(0)
    css = re.sub(r'url\((["\']?/?[^)]+?["\']?)\)', sub, css)

    for sc in list(s.find_all('script')):
        src = sc.get('src') or ''
        f = local(src) if src else None
        # keep the page's own small scripts (the contents-rail highlighter),
        # inlined, so a preview behaves like the real page
        if f is not None and f.name in ('article-toc.js',):
            sc.attrs.pop('src', None)
            sc.string = f.read_text(encoding='utf-8')
            continue
        if src or 'googletagmanager' in str(sc) or 'dataLayer' in str(sc):
            sc.decompose()

    title = s.title.get_text(strip=True) if s.title else name
    fonts = "".join(str(l) for l in s.find_all('link') if 'fonts.google' in (l.get('href') or ''))
    body = s.body.decode_contents() if s.body else ""
    out = ROOT / ('_standalone-' + name.replace('/', '__').replace('__index.html', '.html'))
    out.write_text('<title>%s</title>\n%s\n<style>\n%s\n</style>\n%s'
                   % (title, fonts, css, body), encoding='utf-8')
    print(out.name, out.stat().st_size // 1024, 'KB')

for a in sys.argv[1:]:
    main(a)
