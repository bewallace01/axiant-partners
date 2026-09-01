#!/usr/bin/env node
/**
 * apply-v2-shell.mjs - the per-page head and structured data for v2 pages.
 *
 * Scope note: this used to inject CSS, markup and JS too, back when
 * index-v2.html was one self-contained file. Those now have real homes and
 * this script deliberately does NOT touch them:
 *
 *   styles     -> axiant-v2.css
 *   header +   -> _components/header-v2.html  (run scripts/sync-header-v2.py)
 *   mobile menu
 *   behaviour  -> axiant-v2.js
 *
 * What's left is the one thing that genuinely differs per page - the head
 * (canonical, robots, OG/Twitter, GA4, favicons) and the JSON-LD graph. The
 * site has no build step, so this is the include mechanism for that.
 *
 * Everything is written between ax:head / ax:ld markers and stripped before
 * being rewritten, so running it repeatedly is a no-op.
 *
 *   node scripts/apply-v2-shell.mjs            # every *-v2.html
 *   node scripts/apply-v2-shell.mjs index-v2.html
 */
import fs from 'fs';
import path from 'path';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname).replace(/^\/([A-Za-z]:)/, '$1'), '..');
const GA4 = 'G-HZNSHH6NN0';
const ADS = 'AW-18021105450';
const SITE = 'https://axiantpartners.com';
const OG_IMAGE = SITE + '/assets/axiant-hero-branded.webp';

/* Pages ship back at their ORIGINAL filename, so the canonical drops the -v2
   suffix. index is the site root, not /index.html. */
const canonicalFor = (file) => {
  const base = path.basename(file).replace(/-v2\.html$/, '.html');
  return base === 'index.html' ? SITE + '/' : SITE + '/' + base;
};

const decode = (t) => t
  .replace(/&mdash;/g, '—').replace(/&ndash;/g, '–')
  .replace(/&nbsp;/g, ' ').replace(/&middot;/g, '·')
  .replace(/&rsquo;/g, '’').replace(/&quot;/g, '"')
  .replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>')
  .replace(/&amp;/g, '&').replace(/<[^>]*>/g, '')
  .replace(/\s+/g, ' ').trim();

const ORG = {
  '@type': 'Organization',
  '@id': SITE + '/#organization',
  name: 'Axiant Partners',
  url: SITE,
  logo: { '@type': 'ImageObject', url: SITE + '/logo.jpg' },
  image: SITE + '/logo.jpg',
  description: 'Commercial financing brokerage matching U.S. businesses with the lender programs most likely to approve them.',
  contactPoint: {
    '@type': 'ContactPoint',
    telephone: '+1-561-268-0465',
    contactType: 'customer service',
    areaServed: 'US',
    availableLanguage: 'English, Spanish',
  },
  sameAs: [
    'https://www.linkedin.com/company/axiantpartners/',
    'https://www.facebook.com/axiantpartners',
    'https://www.instagram.com/axiantpartners',
    'https://www.youtube.com/@axeltheloanlion',
  ],
  areaServed: { '@type': 'Country', name: 'United States' },
  serviceType: 'Business financing matchmaking and loan advisory',
  knowsAbout: [
    'SBA loans', 'Business lines of credit', 'Working capital loans',
    'Business term loans', 'Equipment financing', 'Commercial real estate loans',
    'Commercial bridge loans', 'Revenue-based financing', 'Merchant cash advances',
    'Invoice factoring', 'Startup financing', 'Securities-based lending',
    'Fix and flip loans', 'Business debt relief', 'Small business lending',
  ],
};

function processFile(file) {
  const abs = path.join(ROOT, file);
  let s = fs.readFileSync(abs, 'utf8');

  /* ---- strip what a previous run wrote --------------------------------- */
  // Match the marker PREFIX, not the whole opening comment - the start marker
  // carries a "do not edit" note, and matching it literally meant a reworded
  // note silently stopped the strip and the block got appended twice.
  const strip = (name) => {
    s = s.split(new RegExp('\\n?<!-- ax:' + name + ':start[\\s\\S]*?<!-- ax:' + name + ':end -->\\n?', 'g')).join('\n');
  };
  strip('head');
  strip('ld');
  s = s.replace(/\n{3,}/g, '\n\n');

  /* Injected text contains "$10,000" and "$5,000,000+". Handed to
     String.replace as a replacement STRING, "$1"/"$&" are read as
     BACKREFERENCES and expand into the surrounding markup - which silently
     corrupted the og:/twitter: descriptions and dumped raw HTML onto the page.
     A function replacer makes every "$" literal. Always insert through these. */
  const insertAfter = (re, text) => { s = s.replace(re, (m) => m + '\n' + text); };
  const insertBefore = (re, text) => { s = s.replace(re, (m) => text + '\n' + m); };

  /* ---- read what the page is telling us -------------------------------- */
  const pick = (re, what) => {
    const m = s.match(re);
    if (!m) throw new Error(`${file}: could not find ${what}`);
    return m;
  };
  const title = pick(/<title>([\s\S]*?)<\/title>/, '<title>')[1].trim();
  const desc = pick(/<meta name="description" content="([^"]*)"/, 'meta description')[1];
  const canonical = (s.match(/<link rel="canonical" href="([^"]*)"/) || [])[1] || canonicalFor(file);
  // A page may already declare its own canonical/robots; don't emit a second.
  const hasCanonical = /<link rel="canonical"/.test(s);
  const hasRobots = /<meta name="robots"/.test(s);

  /* ---- the head -------------------------------------------------------- */
  const head = [
    '<!-- ax:head:start - generated by scripts/apply-v2-shell.mjs; do not edit inside -->',
    '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
    '<meta name="theme-color" content="#0d1f3c">',
    '<meta name="google-site-verification" content="r6yyqb6FxWxmJGmr4GBVwPzRZ9flVFuz8Vt6CUkbarc">',
    ...(hasRobots ? [] : ['<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">']),
    ...(hasCanonical ? [] : ['<link rel="canonical" href="' + canonical + '">']),
    '',
    '<!-- Google tag (gtag.js) - deferred for faster initial load -->',
    '<script>',
    '  window.dataLayer = window.dataLayer || [];',
    '  function gtag(){dataLayer.push(arguments);}',
    "  window.addEventListener('load', function() {",
    "    var s = document.createElement('script');",
    '    s.async = true;',
    "    s.src = 'https://www.googletagmanager.com/gtag/js?id=" + GA4 + "';",
    '    document.head.appendChild(s);',
    "    s.onload = function() { gtag('js', new Date()); gtag('config', '" + GA4 + "'); gtag('config', '" + ADS + "'); };",
    '  });',
    '</' + 'script>',
    '',
    '<meta property="og:title" content="' + title + '">',
    '<meta property="og:description" content="' + desc + '">',
    '<meta property="og:type" content="website">',
    '<meta property="og:url" content="' + canonical + '">',
    '<meta property="og:image" content="' + OG_IMAGE + '">',
    '<meta property="og:image:width" content="1200">',
    '<meta property="og:image:height" content="630">',
    '<meta property="og:site_name" content="Axiant Partners">',
    '<meta property="og:locale" content="en_US">',
    '<meta name="twitter:card" content="summary_large_image">',
    '<meta name="twitter:title" content="' + title + '">',
    '<meta name="twitter:description" content="' + desc + '">',
    '<meta name="twitter:image" content="' + OG_IMAGE + '">',
    '',
    '<link rel="icon" type="image/webp" sizes="48x48" href="/favicon.webp">',
    '<link rel="icon" type="image/png" sizes="48x48" href="/favicon.png">',
    '<link rel="apple-touch-icon" href="/favicon.png">',
    '<!-- ax:head:end -->',
  ].join('\n');
  insertAfter(/<meta name="description" content="[^"]*">/, head);

  /* ---- the structured data --------------------------------------------- */
  // FAQPage is generated from the VISIBLE FAQ, so schema and page text can
  // never disagree. Pages without a FAQ simply don't get the block.
  const faqHtml = (s.match(/<div class="faq">([\s\S]*?)<\/div>\s*<\/div>\s*<\/section>/) || [, ''])[1];
  const faqs = [...faqHtml.matchAll(
    /<summary>([\s\S]*?)<\/summary>\s*<div class="answer">([\s\S]*?)<\/div>/g
  )].map((m) => ({ q: decode(m[1]), a: decode(m[2]) }));

  const graph = [
    ORG,
    {
      '@type': 'WebSite',
      name: 'Axiant Partners',
      url: SITE,
      publisher: { '@id': SITE + '/#organization' },
      mainEntity: { '@id': SITE + '/#organization' },
    },
    {
      '@type': 'WebPage',
      name: decode(title),
      description: decode(desc),
      url: canonical,
      isPartOf: { '@id': SITE + '/#organization' },
      publisher: { '@id': SITE + '/#organization' },
    },
  ];
  if (faqs.length) {
    graph.push({
      '@type': 'FAQPage',
      mainEntity: faqs.map((f) => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: { '@type': 'Answer', text: f.a },
      })),
    });
  }
  const ld = [
    '<!-- ax:ld:start -->',
    '<script type="application/ld+json">',
    JSON.stringify({ '@context': 'https://schema.org', '@graph': graph }, null, 2),
    '</' + 'script>',
    '<!-- ax:ld:end -->',
  ].join('\n');
  insertBefore(/<\/head>/, ld);

  /* ---- self-check: catch a mangled injection BEFORE writing ------------- */
  const descTags = (s.match(/<meta name="description"/g) || []).length;
  if (descTags !== 1) throw new Error(`${file}: expected 1 meta description, found ${descTags} - injection mangled`);
  const canonicals = (s.match(/<link rel="canonical"/g) || []).length;
  if (canonicals !== 1) throw new Error(`${file}: expected 1 canonical, found ${canonicals}`);
  for (const [prop, want] of [['og:description', desc], ['twitter:description', desc], ['og:title', title]]) {
    const got = (s.match(new RegExp('(?:property|name)="' + prop + '" content="([^"]*)"')) || [])[1];
    if (got !== want) throw new Error(`${file}: ${prop} does not match its source value - injection mangled`);
  }
  if (/<meta[^>]*content="[^"]*<meta/.test(s)) throw new Error(`${file}: a meta tag is nested inside another`);
  // A failed strip appends rather than replaces, so count the singletons too.
  for (const [what, re, want] of [
    ['og:title', /property="og:title"/g, 1],
    ['ld+json blocks', /application\/ld\+json/g, 1],
    ['gtag snippets', /googletagmanager\.com\/gtag/g, 1],
  ]) {
    const n = (s.match(re) || []).length;
    if (n !== want) throw new Error(`${file}: expected ${want} ${what}, found ${n} - a previous block was not stripped`);
  }
  JSON.parse((s.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/) || [, '{}'])[1]);

  fs.writeFileSync(abs, s, 'utf8');
  return { file, canonical, faqQuestions: faqs.length, addedCanonical: !hasCanonical };
}

const args = process.argv.slice(2);
const files = args.length
  ? args
  : fs.readdirSync(ROOT).filter((f) => f.endsWith('-v2.html')).sort();
if (!files.length) { console.error('no *-v2.html pages found'); process.exit(1); }

const report = files.map(processFile);
console.log(JSON.stringify(report, null, 1));
console.log('\nReminder: header/menu changes go in _components/header-v2.html');
console.log('then `python scripts/sync-header-v2.py`. Styles: axiant-v2.css. JS: axiant-v2.js.');
