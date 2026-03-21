/**
 * Applies mobile optimizations to all HTML files:
 * - Step 1: Inline critical-mobile.css as first stylesheet
 * - Step 5: Add lazy-load script before </body>
 * - Step 6: Ensure meta tags and dns-prefetch at top of head
 * - Step 2: Wrap /assets/ images in picture elements for mobile srcset
 * - Step 3: Defer language-switcher on mobile (wrap script load)
 */
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;

function findHtmlFiles(dir, files = []) {
  const items = fs.readdirSync(dir, { withFileTypes: true });
  for (const item of items) {
    const full = path.join(dir, item.name);
    if (item.isDirectory() && !['node_modules', '.git'].includes(item.name)) {
      findHtmlFiles(full, files);
    } else if (item.name.endsWith('.html')) {
      files.push(full);
    }
  }
  return files;
}

function getCriticalMobileCss() {
  const p = path.join(ROOT, 'critical-mobile.css');
  return fs.readFileSync(p, 'utf8').replace(/<\/style>/g, '').trim();
}

const LAZY_SCRIPT = `<script>
if(window.innerWidth<=768){var ls=document.querySelectorAll('.about-section,.testimonials-section,.global-bottom-cta,.site-footer-enhanced,.services-grid,.blog-grid,.steps-grid,.benefits-grid');var so=new IntersectionObserver(function(e){e.forEach(function(entry){if(entry.isIntersecting){entry.target.style.opacity='1';entry.target.style.transform='none';so.unobserve(entry.target);}});},{rootMargin:'100px'});ls.forEach(function(s){s.style.opacity='0';s.style.transition='opacity 0.3s ease';so.observe(s);});}
</script>`;

const META_BLOCK = `<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="theme-color" content="#0d1f3c">
<link rel="dns-prefetch" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">`;

function applyChanges(html, criticalCss) {
  let out = html;

  // Step 1: Add mobile-critical style before first stylesheet
  const mobileStyle = `<style id="mobile-critical">\n${criticalCss}\n</style>\n`;
  if (!out.includes('id="mobile-critical"')) {
    const stylesheetMatch = out.match(/<link[^>]+rel=["']stylesheet["'][^>]*>/i);
    if (stylesheetMatch) {
      out = out.replace(stylesheetMatch[0], mobileStyle + stylesheetMatch[0]);
    } else {
      const headEnd = out.indexOf('</head>');
      if (headEnd > -1) {
        out = out.slice(0, headEnd) + mobileStyle + out.slice(headEnd);
      }
    }
  }

  // Step 6: Ensure meta tags and dns-prefetch
  if (!out.includes('viewport-fit=cover') && out.includes('viewport')) {
    out = out.replace(/<meta\s+name=["']viewport["'][^>]*>/i, '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">');
  }
  if (!out.includes('theme-color')) {
    const headMatch = out.match(/<head[^>]*>/i);
    if (headMatch) {
      out = out.replace(headMatch[0], headMatch[0] + '\n<meta name="theme-color" content="#0d1f3c">');
    }
  }
  if (!out.includes('X-UA-Compatible')) {
    const headMatch = out.match(/<head[^>]*>/i);
    if (headMatch) {
      out = out.replace(headMatch[0], headMatch[0] + '\n<meta http-equiv="X-UA-Compatible" content="IE=edge">');
    }
  }
  if (!out.includes('dns-prefetch') && out.includes('googletagmanager')) {
    const firstLink = out.match(/<link\s+rel=/i);
    if (firstLink) {
      const hints = '\n<link rel="dns-prefetch" href="https://fonts.googleapis.com">\n<link rel="dns-prefetch" href="https://fonts.gstatic.com">\n<link rel="dns-prefetch" href="https://www.googletagmanager.com">';
      out = out.replace(/<head[^>]*>/i, (m) => m + hints);
    }
  }

  // Step 2: Wrap /assets/ images in picture (skip if already in picture)
  out = out.replace(
    /<img([^>]*?)src=["']([^"']*\/assets\/[^"']+)["']([^>]*)>/gi,
    (match, before, src, after, offset, fullString) => {
      const prev = fullString.slice(Math.max(0, offset - 150), offset);
      if (prev.includes('<source media=')) return match;
      const baseName = src.replace(/\.(png|jpg|jpeg|webp)(\?.*)?$/i, '');
      const mobileSrc = baseName + '-mobile.webp' + (src.includes('?') ? src.slice(src.indexOf('?')) : '');
      return `<picture><source media="(max-width: 768px)" srcset="${mobileSrc}"><img${before} src="${src}"${after}></picture>`;
    }
  );

  // Step 5: Add lazy script before </body> if not present
  if (!out.includes('ls=document.querySelectorAll') && !out.includes('lazySections')) {
    out = out.replace(/\s*<\/body>/i, '\n' + LAZY_SCRIPT + '\n</body>');
  }

  // Step 3: Defer language-switcher on mobile - replace static script with conditional load
  out = out.replace(
    /<script\s+src=["']([^"']*language-switcher\.js[^"']*)["']\s+defer\s*><\/script>/gi,
    '<script>if(window.innerWidth>768){var ls=document.createElement("script");ls.src="$1";ls.defer=true;document.body.appendChild(ls);}</script>'
  );

  return out;
}

const criticalCss = getCriticalMobileCss();
const files = findHtmlFiles(ROOT);
let count = 0;

for (const file of files) {
  try {
    const html = fs.readFileSync(file, 'utf8');
    const updated = applyChanges(html, criticalCss);
    if (updated !== html) {
      fs.writeFileSync(file, updated);
      count++;
    }
  } catch (err) {
    console.error('Error:', file, err.message);
  }
}

console.log('Updated', count, 'HTML files');
