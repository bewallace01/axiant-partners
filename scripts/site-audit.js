#!/usr/bin/env node
/* Axiant Partners full-site audit -> self-contained HTML dashboard.
 * Run: node scripts/site-audit.js   (or: npm run audit)
 * Output: _analysis/site-audit.html      (gitignored; never deployed)
 * History: _analysis/site-audit-history.json (gitignored; one snapshot/run, dedup by day)
 * Auto-runs via .git/hooks/post-commit after every commit. */
const fs = require('fs'), path = require('path');
const ROOT = process.cwd();
const OUT_DIR = path.join(ROOT, '_analysis');
const today = new Date().toISOString().slice(0, 10);
const _now = new Date();
const _mon = ['January','February','March','April','May','June','July','August','September','October','November','December'][_now.getMonth()];
let _h = _now.getHours(); const _ap = _h >= 12 ? 'PM' : 'AM'; _h = _h % 12 || 12;
const stamp = _mon + ' ' + _now.getDate() + ', ' + _now.getFullYear() + ' at ' + _h + ':' + String(_now.getMinutes()).padStart(2,'0') + ' ' + _ap;

// ---------- crawl ----------
function walk(dir, out) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    const rel = path.relative(ROOT, p).split(path.sep).join('/');
    if (e.isDirectory()) {
      if (/^(\.git|node_modules|fonts|assets|docs|__pycache__)$/.test(e.name)) continue;
      if (rel.startsWith('_')) continue;
      walk(p, out);
    } else if (e.name.endsWith('.html')) {
      if (rel.startsWith('_')) continue;
      out.push(rel);
    }
  }
  return out;
}
const files = walk(ROOT, []).sort();

// ---------- helpers ----------
const norm = s => s.replace(/&amp;/g,'&').replace(/&[a-z]+;/g,' ').replace(/&#\d+;/g,' ').replace(/\s+/g,' ').trim();
const keyOf = rel => ('/' + rel).replace(/index\.html$/,'');
function resolveLink(fromRel, href) {
  href = href.split('#')[0].split('?')[0];
  if (!href) return null;
  let target = href.startsWith('/') ? href.slice(1)
    : path.posix.normalize(path.posix.join(path.posix.dirname(fromRel), href));
  const cands = [target, target.replace(/\/$/,'') + '/index.html', target + (target.endsWith('.html')?'':'.html'), target + '/index.html'];
  for (const c of cands) {
    const clean = c.replace(/^\//,'');
    if (fs.existsSync(path.join(ROOT, clean)) && fs.statSync(path.join(ROOT, clean)).isFile()) return clean;
  }
  return null;
}
function classify(rel) {
  const parts = rel.split('/'), base = parts[parts.length-1];
  if (/^get-matched\//.test(rel)) return 'ad-landing';
  if (/(^|\/)(tools|fragments)\//.test(rel) || /digital-marketing\/fragments/.test(rel)) return 'fragment';
  if (/articles\/index\.html$/.test(rel)) return 'article-index';
  if (/^[^/]+\/articles\/[^/]+\/index\.html$/.test(rel)) return 'article';
  if (/^equipment\/[^/]+\/[^/]+\/index\.html$/.test(rel)) return 'article';
  if (/^equipment\/[^/]+\/index\.html$/.test(rel)) return 'equipment-hub';
  if (parts.length>1 && base==='index.html') return 'cluster-index';
  if (parts.length===1) {
    if (/-business-financing\.html$/.test(base)) return 'industry-hub';
    if (/-guide\.html$/.test(base)) return 'guide';
    if (/^business-loans-[a-z-]+\.html$/.test(base)) return 'geo-landing';
    if (/(\d+|business-loan)\.html$/.test(base) && /loan|financing/.test(base)) return 'landing';
    const svc = new Set(['equipment-financing.html','sba-loans.html','business-line-of-credit.html','working-capital-loans.html','commercial-real-estate-loans.html','business-term-loans.html','merchant-cash-advance.html','invoice-factoring.html','commercial-bridge-loans.html','accounts-receivable-financing.html','revenue-based-financing.html','securities-based-lending.html','inventory-financing.html']);
    if (svc.has(base)) return 'service-hub';
    const util = new Set(['index.html','match.html','calculator.html','calculator-embed.html','contact.html','services.html','industries.html','about.html','blog.html','faq.html','referral.html','privacy-policy.html','terms-and-conditions.html','vendors.html','thank-you.html','business-growth.html']);
    if (util.has(base)) return 'core';
    return 'root-page';
  }
  return 'page';
}
const CHROME = new Set(['/','/match.html','/index.html','/services.html','/industries.html','/calculator.html','/contact.html','/about.html','/privacy-policy.html','/terms-and-conditions.html','/vendors.html','/blog.html','/faq.html','/referral.html','/business-growth.html','/calculator-embed.html','/thank-you.html']);

// ---------- sitemap ----------
let sitemapKeys = new Set();
try {
  const sm = fs.readFileSync(path.join(ROOT,'sitemap.xml'),'utf8');
  for (const m of sm.matchAll(/<loc>\s*([^<]+?)\s*<\/loc>/g)) sitemapKeys.add(m[1].replace(/^https?:\/\/[^/]+/,''));
} catch(e){}

// ---------- parse ----------
const pages = {}, inbound = {};
for (const rel of files) {
  const html = fs.readFileSync(path.join(ROOT, rel), 'utf8');
  const key = keyOf(rel);
  const titleM = html.match(/<title>([^<]*)<\/title>/i);
  const descM = html.match(/<meta name="description" content="([^"]*)"/i);
  const robotsM = html.match(/<meta name="robots" content="([^"]*)"/i);
  const noindex = robotsM ? /noindex/i.test(robotsM[1]) : false;
  const h1 = (html.match(/<h1[\s>]/gi)||[]).length;
  const ldBlocks = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/gi)];
  let ldFail = 0; const types = new Set();
  for (const b of ldBlocks) {
    try { JSON.parse(b[1].replace(/&amp;/g,'&')); } catch(e){ ldFail++; }
    for (const t of b[1].matchAll(/"@type"\s*:\s*"([^"]+)"/g)) types.add(t[1]);
  }
  let wc=0, src='body';
  const mainM = html.match(/<main[\s\S]*?<\/main>/i);
  if (mainM){ wc = norm(mainM[0].replace(/<[^>]+>/g,' ')).split(' ').filter(Boolean).length; src='main'; }
  else {
    const secs=[...html.matchAll(/<section class="about-section[^"]*">([\s\S]*?)<\/section>/gi)];
    if (secs.length){ wc = norm(secs.map(s=>s[1]).join(' ').replace(/<[^>]+>/g,' ')).split(' ').filter(Boolean).length; src='about'; }
    else { const bodyM=html.match(/<body[\s\S]*<\/body>/i); wc = norm((bodyM?bodyM[0]:html).replace(/<(script|style)[\s\S]*?<\/\1>/gi,' ').replace(/<[^>]+>/g,' ')).split(' ').filter(Boolean).length; }
  }
  const imgs=[...html.matchAll(/<img\b[^>]*>/gi)].map(m=>m[0]);
  const imgNoAlt = imgs.filter(t=>!/\balt\s*=/.test(t)).length;
  const hrefs=[...html.matchAll(/href="([^"]+)"/gi)].map(m=>m[1])
    .filter(h=>!/^(https?:|mailto:|tel:|\/\/|data:|#)/.test(h))
    .filter(h=>!/\.(css|js|json|xml|txt|webp|png|jpg|jpeg|svg|gif|ico|pdf|webmanifest)(\?|$)/i.test(h.split('#')[0]));
  const outKeys=new Set(); const broken=[];
  for (const h of hrefs){
    const r = resolveLink(rel, h);
    if (r===null){ if(!h.includes("'+")&&!h.includes('${')) broken.push(h); }
    else outKeys.add(keyOf(r));
  }
  const modM = html.match(/(?:article:modified_time|dateModified)["']?\s*[:=]\s*["']?(\d{4}-\d{2}-\d{2})/);
  const dataBatch = /data-batch/.test(html);
  const hasTool = /<iframe[^>]*calculator|<input\b|id="[^"]*[Cc]alc/.test(html);
  let na=0; for(const b of Buffer.from(html)){ if(b>127) na++; }
  pages[key] = { key, rel, type: classify(rel), cluster: rel.includes('/')?rel.split('/')[0]:'(root)',
    title: titleM?norm(titleM[1]):'', desc: descM?descM[1].length:0, h1, noindex,
    schema:[...types], ldFail, wc, wcSrc:src, imgs:imgs.length, imgNoAlt,
    out:[...outKeys], broken, inSitemap: sitemapKeys.has(key), mod: modM?modM[1]:null, dataBatch, hasTool, nonascii:na };
  for (const ok of outKeys) inbound[ok]=(inbound[ok]||0)+1;
}
for (const k in pages) pages[k].inbound = inbound[k]||0;

// ---------- aggregates ----------
const arr = Object.values(pages);
const indexable = arr.filter(p=>!p.noindex);
const contentTypes = new Set(['article','industry-hub','service-hub','guide','article-index','equipment-hub','cluster-index','landing','geo-landing','root-page','page']);
const isContent = p => contentTypes.has(p.type);
const titleMap={};
for(const p of indexable){ if(p.type==='fragment'||p.type==='ad-landing')continue; const t=p.title.replace(/\s*\|\s*Axiant.*/i,'').trim().toLowerCase(); if(!t)continue; (titleMap[t]=titleMap[t]||[]).push(p.key); }
const dupTitles = Object.entries(titleMap).filter(([t,v])=>v.length>1);
const orphans = indexable.filter(p=>p.inbound===0 && !CHROME.has(p.key) && isContent(p) && p.type!=='core');
const articles = arr.filter(p=>p.type==='article');
// Thin = genuine ARTICLES only. Calculators/embeds, article-index card grids, hubs,
// print brochures, and vendor pages are legitimately short and are NOT thin content.
const isArticleType = p => p.type==='article' && !/calculator|embed|brochure/.test(p.rel);
const veryThin = indexable.filter(p=>isArticleType(p)&&p.wc<500);
const thin = indexable.filter(p=>isArticleType(p)&&p.wc>=500&&p.wc<800);
const brokenList=[]; for(const p of arr) for(const b of p.broken) brokenList.push({from:p.key, href:b});
const notInSitemap = indexable.filter(p=>!p.inSitemap && !['core','fragment','ad-landing','cluster-index'].includes(p.type));
const noindexInSitemap = arr.filter(p=>p.noindex && p.inSitemap);
const deadSitemap=[...sitemapKeys].filter(k=>!pages[k]);
const noSchema = indexable.filter(p=>isContent(p)&&p.schema.length===0 && p.type!=='cluster-index');
const ldFails = arr.filter(p=>p.ldFail>0);
const stale = articles.filter(p=>!p.mod || p.mod < '2026-03-01');
const filler = arr.filter(p=>p.dataBatch);
const weak = indexable.filter(p=>isContent(p)&&p.inbound>0&&p.inbound<=2&&p.type!=='core'&&!CHROME.has(p.key));
const noToolHubs = arr.filter(p=>['industry-hub','service-hub','landing','geo-landing'].includes(p.type)&&!p.hasTool);
const clusters={};
for(const p of arr){ const o=(clusters[p.cluster]=clusters[p.cluster]||{cluster:p.cluster,n:0,words:0,thin:0,orphan:0,noindex:0,inb:0,inSm:0,broken:0}); o.n++; o.words+=p.wc; if(p.wc<500&&isArticleType(p))o.thin++; if(p.inbound===0&&isContent(p)&&!CHROME.has(p.key))o.orphan++; if(p.noindex)o.noindex++; o.inb+=p.inbound; if(p.inSitemap)o.inSm++; o.broken+=p.broken.length; }
const clusterArr = Object.values(clusters).map(o=>({...o, avgw:Math.round(o.words/o.n), avgInb:(o.inb/o.n).toFixed(1)})).sort((a,b)=>b.n-a.n);
const typeDist={}; for(const p of arr) typeDist[p.type]=(typeDist[p.type]||0)+1;
const buckets=[[0,300],[300,600],[600,900],[900,1200],[1200,1600],[1600,99999]];
const hist=buckets.map(([a,b])=>({label:b>9000?(a+'+'):a+'-'+b, n: arr.filter(p=>isContent(p)&&p.wc>=a&&p.wc<b).length}));
const artByCluster={}; arr.forEach(p=>{ if(p.type==='article') artByCluster[p.cluster]=(artByCluster[p.cluster]||0)+1; });
const hubGaps = arr.filter(p=>p.type==='industry-hub').map(p=>{const base=p.rel.replace(/\.html$/,'');return {k:p.key,arts:artByCluster[base]||0};}).filter(h=>h.arts<3).sort((a,b)=>a.arts-b.arts);
const summary = {
  totalFiles: files.length, indexable: indexable.length, noindex: arr.length-indexable.length,
  inSitemap: arr.filter(p=>p.inSitemap).length, clusters: Object.keys(clusters).length,
  articles: articles.length, totalWords: arr.reduce((s,p)=>s+p.wc,0),
  avgArticleWords: Math.round(articles.reduce((s,p)=>s+p.wc,0)/(articles.length||1)),
  orphans: orphans.length, veryThin: veryThin.length, thin: thin.length, weak: weak.length,
  brokenLinks: brokenList.length, notInSitemap: notInSitemap.length, noindexInSitemap: noindexInSitemap.length,
  deadSitemap: deadSitemap.length, noSchema: noSchema.length, ldFails: ldFails.length, dupTitles: dupTitles.length,
  filler: filler.length, stale: stale.length, sitemapTotal: sitemapKeys.size, withTool: arr.filter(p=>p.hasTool).length,
  noToolHubs: noToolHubs.length,
};

// ---------- history (append one snapshot/day, dedup by date) ----------
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });
const HIST_FILE = path.join(OUT_DIR, 'site-audit-history.json');
let history = [];
try { history = JSON.parse(fs.readFileSync(HIST_FILE,'utf8')); } catch(e){}
const snap = { date: today, files: summary.totalFiles, indexable: summary.indexable, articles: summary.articles,
  avgw: summary.avgArticleWords, broken: summary.brokenLinks, veryThin: summary.veryThin, thin: summary.thin,
  weak: summary.weak, filler: summary.filler, noidxSm: summary.noindexInSitemap, notInSm: summary.notInSitemap,
  stale: summary.stale, orphans: summary.orphans, tools: summary.withTool };
history = history.filter(h => h.date !== today);
history.push(snap);
history = history.slice(-180);
fs.writeFileSync(HIST_FILE, JSON.stringify(history));

// ---------- suggested fixes (data-driven) ----------
const brokenBy={}; brokenList.forEach(b=>{brokenBy[b.from]=(brokenBy[b.from]||0)+1;});
const brokenTop = Object.entries(brokenBy).sort((a,b)=>b[1]-a[1]).slice(0,10).map(e=>e[0]+'  ('+e[1]+' broken)');
const samp = (list,n) => list.slice(0,n||8).map(x=>x.k + (x.w!=null?'  ('+x.w+'w)':''));
const fixes=[];
if(summary.brokenLinks) fixes.push({pri:'NOW',effort:'Low',title:'Fix '+summary.brokenLinks+' broken internal links',how:'Largely resolved in PRs #49/#50 — merge them, then re-run this audit to confirm it drops to ~0. Worst offenders below.',sample:brokenTop});
if(summary.veryThin) fixes.push({pri:'NOW',effort:'Med',title:'Expand, merge, or prune '+summary.veryThin+' very-thin articles (<500w)',how:'Genuine articles only (calculators, index/card-grid, hubs and brochures are excluded). For each: expand to 1,000w+, merge into a stronger sibling, or 301/prune. Start by pruning the dated "wartime/inflation" set.',sample:samp(veryThin.map(p=>({k:p.key,w:p.wc})),12)});
if(summary.filler) fixes.push({pri:'NOW',effort:'Low',title:'Strip data-batch filler from '+summary.filler+' pages',how:'Empty/boilerplate H2 blocks that read as over-optimization. A deterministic strip pass exists; PR #49 covers most.',sample:samp(filler.map(p=>({k:p.key,w:p.wc})),10)});
if(summary.orphans) fixes.push({pri:'NOW',effort:'Low',title:'Reconnect '+summary.orphans+' orphan pages (0 inbound)',how:'Add a contextual link from the relevant hub/sibling so they are discoverable.',sample:samp(orphans.map(p=>({k:p.key})),10)});
if(summary.noindexInSitemap+summary.notInSitemap) fixes.push({pri:'SOON',effort:'Low',title:'Fix sitemap drift ('+summary.noindexInSitemap+' noindex in, '+summary.notInSitemap+' indexable missing)',how:'Remove noindex URLs from sitemap.xml and add the missing indexable pages. Keeps crawl signals clean.',sample:noindexInSitemap.map(p=>'(noindex-in) '+p.key).concat(notInSitemap.map(p=>'(missing) '+p.key)).slice(0,12)});
if(summary.thin) fixes.push({pri:'SOON',effort:'Med',title:'Deepen '+summary.thin+' lean articles (500-800w)',how:'Genuine articles only. Add a worked example, FAQ, or comparison table to push toward the 1,000w+ house standard.',sample:samp(thin.map(p=>({k:p.key,w:p.wc})),10)});
if(summary.weak) fixes.push({pri:'SOON',effort:'Med',title:'Strengthen internal links to '+summary.weak+' weak pages (1-2 inbound)',how:'Add 1-2 contextual links each from stronger cluster pages. Do not over-optimize past ~3.',sample:samp(weak.map(p=>({k:p.key,w:p.wc})),10)});
if(summary.stale) fixes.push({pri:'SOON',effort:'Low',title:'Refresh '+summary.stale+' stale articles',how:'Update figures, bump dateModified, add a tool/FAQ where it fits. Freshness helps both ranking and trust.',sample:samp(stale.map(p=>({k:p.key,w:p.wc})),10)});
if(summary.noToolHubs) fixes.push({pri:'SOON',effort:'Med',title:'Add conversion tools to '+summary.noToolHubs+' hubs/landing pages',how:'Only '+summary.withTool+' pages have an interactive tool today. Inline calculators + prefilled apply CTAs are the AIO-proof lever that actually converts.',sample:samp(noToolHubs.map(p=>({k:p.key})),12)});
if(summary.noSchema) fixes.push({pri:'LATER',effort:'Low',title:'Add JSON-LD schema to '+summary.noSchema+' content pages',how:'Add BreadcrumbList + Article/FinancialService + FAQPage for AEO/GEO eligibility.',sample:samp(noSchema.map(p=>({k:p.key})),10)});

// ---------- opportunities ("things to go after") ----------
const opps=[];
if(hubGaps.length) opps.push({title:'Build article clusters for '+hubGaps.length+' shallow industry hubs',impact:hubGaps.length+' hubs',detail:'These industry hubs have fewer than 3 supporting articles. Add a 3-problem cluster each (same proven pattern as septic/towing) to build topical depth.',sample:hubGaps.slice(0,12).map(h=>h.k+'  ('+h.arts+' articles)')});
opps.push({title:'Net-new verticals (zero cannibalization by construction)',impact:'~9 clean gaps',detail:'Industries with no page yet — safe, additive ranking surface. Each = a hub + 3 problem-articles with apply CTAs.',sample:['welding & metal fabrication','catering','sign company','masonry','flooring','pool service & construction','demolition','pressure washing','IT / MSP','auto detailing']});
opps.push({title:'Commercial comparison / "best-X" pages',impact:'highest click-intent',detail:'"X vs Y" and "best X for [audience]" earn the few clicks AI Overviews leave on the table. Dedup hard against the existing Best-X set first.',sample:['best equipment financing for [trade]','term loan vs SBA for [use]','more lender-type head-to-heads','best working capital for [industry]']});
opps.push({title:'Factoring cluster Tier-2',impact:'depth + intent',detail:'Round out the invoice-factoring set (4 Tier-1 articles in flight) with vertical/specialty pieces.',sample:['medical / healthcare receivables factoring','government-contractor factoring (Assignment of Claims Act)','dedicated trucking/freight factoring (fuel advances, quick-pay)','staffing-agency factoring (dedicated)']});
opps.push({title:'Local geo + industry landing pages',impact:'least AIO-suppressed',detail:'City + service combos (e.g. "HVAC financing in Atlanta") capture high-intent local traffic. Extends the metro work already shipped.',sample:['metro x service combinations','more city pages where Atlanta validates','state hub deepening']});
opps.push({title:'Conversion funnel upgrades',impact:'revenue, not just traffic',detail:'Reorder the match form to ask loan details before contact info, add inline email micro-capture under calculators, and prefill from each page.',sample:['match.html step reorder (global — propose first)','email micro-capture under calc results','prefill ?type=&amount= on every calc CTA']});

// ---------- visual architecture (route-prefix breakdown into categories) ----------
const PRODUCTS = new Set(['equipment-financing','sba-loans','working-capital-loans','business-line-of-credit','commercial-real-estate-loans','business-term-loans','merchant-cash-advance','invoice-factoring','commercial-bridge-loans','revenue-based-financing','securities-based-lending','fix-and-flip','accounts-receivable-financing','inventory-financing','business-debt-relief','startup-financing']);
function archCat(c){
  if(/-business-financing$/.test(c)) return 'Industries (hubs + clusters)';
  if(PRODUCTS.has(c)) return 'Financing products';
  if(c==='equipment') return 'Equipment by type';
  if(/glossary|comparison|guide|^articles$|blog/.test(c)) return 'Guides & reference';
  if(c==='(root)') return 'Root pages';
  return 'Other sections';
}
const archMap={};
for(const o of clusterArr){ const cat=archCat(o.cluster); (archMap[cat]=archMap[cat]||[]).push({label:o.cluster==='(root)'?'/':('/'+o.cluster), n:o.n}); }
// root pages: break into type pills instead of one giant "(root)"
const rootByType={}; for(const p of arr){ if(p.cluster==='(root)') rootByType[p.type]=(rootByType[p.type]||0)+1; }
archMap['Root pages']=Object.entries(rootByType).map(([t,n])=>({label:t,n})).sort((a,b)=>b.n-a.n);
const ARCH_ORDER=['Financing products','Industries (hubs + clusters)','Equipment by type','Guides & reference','Root pages','Other sections'];
const arch=ARCH_ORDER.filter(c=>archMap[c]).map(cat=>({cat, items: archMap[cat].sort((a,b)=>b.n-a.n)}));

const DATA = { summary, stamp, pages: arr, clusterArr, typeDist, hist, history, fixes, opps, arch, lists: {
  orphans: orphans.map(p=>({k:p.key,t:p.type,w:p.wc})).sort((a,b)=>a.k.localeCompare(b.k)),
  veryThin: veryThin.map(p=>({k:p.key,t:p.type,w:p.wc})).sort((a,b)=>a.w-b.w),
  thin: thin.map(p=>({k:p.key,t:p.type,w:p.wc})).sort((a,b)=>a.w-b.w),
  weak: weak.map(p=>({k:p.key,t:p.type,w:p.wc,i:p.inbound})),
  broken: brokenList,
  notInSitemap: notInSitemap.map(p=>({k:p.key,t:p.type})),
  noindexInSitemap: noindexInSitemap.map(p=>({k:p.key})),
  deadSitemap,
  noSchema: noSchema.map(p=>({k:p.key,t:p.type})),
  ldFails: ldFails.map(p=>({k:p.key,n:p.ldFail})),
  dupTitles: dupTitles.map(([t,v])=>({t,v})),
  filler: filler.map(p=>({k:p.key,w:p.wc})),
  stale: stale.map(p=>({k:p.key,m:p.mod||'none',w:p.wc})).sort((a,b)=>(a.m||'').localeCompare(b.m||'')),
}};

// ---------- render ----------
const CSS = `
:root{--bg:#0b1626;--bg2:#101f33;--card:#13243b;--card2:#172b46;--line:#22405f;--tx:#e6eef7;--tx2:#9fb3c8;--cy:#7dd3fc;--bl:#2d7fb8;--good:#22c55e;--warn:#f59e0b;--bad:#ef4444}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,-apple-system,Segoe UI,sans-serif;background:var(--bg);color:var(--tx);line-height:1.5;padding:0 0 80px}
a{color:var(--cy);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1200px;margin:0 auto;padding:0 20px}
header.hd{background:linear-gradient(135deg,#0d1f3c,#1e3a5f);padding:34px 0 28px;border-bottom:1px solid var(--line);margin-bottom:26px}
.hd h1{font-size:2.1rem;font-weight:800;letter-spacing:-.02em;margin-top:14px}
.hd .lede{color:var(--tx2);margin-top:12px;font-size:.98rem;max-width:780px;line-height:1.6}
.hd .lede b{color:var(--tx)}
.badge{display:inline-block;background:#0b1626;border:1px solid var(--line);color:var(--cy);border-radius:20px;padding:3px 12px;font-size:.78rem;margin-right:8px;margin-top:10px}
.pillbadge{display:inline-flex;align-items:center;gap:7px;border-radius:20px;padding:5px 13px;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;margin-right:10px}
.pb-green{background:rgba(34,197,94,.12);border:1px solid rgba(34,197,94,.4);color:#86efac}
.pb-gen{background:rgba(125,211,252,.08);border:1px solid var(--line);color:var(--tx2)}
.pb-gen .dot{width:8px;height:8px;border-radius:50%;background:var(--good);box-shadow:0 0 8px var(--good)}
.toptabs{display:flex;gap:6px;border-bottom:1px solid var(--line);margin:22px 0 6px}
.toptab{padding:11px 18px;cursor:pointer;font-size:.95rem;font-weight:600;color:var(--tx2);border-bottom:2px solid transparent;margin-bottom:-1px}
.toptab.on{color:var(--cy);border-bottom-color:var(--cy)}
.tabpane{display:none}.tabpane.on{display:block}
.arch-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}@media(max-width:820px){.arch-grid{grid-template-columns:1fr}}
.arch-card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}
.arch-card h3{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:var(--tx2);margin-bottom:12px}
.routepill{display:inline-flex;align-items:center;gap:6px;background:#0b1626;border:1px solid var(--line);border-radius:8px;padding:5px 10px;margin:0 7px 8px 0;font-size:.82rem;font-family:ui-monospace,Menlo,monospace}
.routepill .ct{background:rgba(125,211,252,.14);color:var(--cy);border-radius:6px;padding:0 6px;font-weight:700;font-family:Inter,sans-serif}
h2.sec{font-size:1.25rem;font-weight:700;margin:38px 0 6px;padding-top:10px}
.sub{color:var(--tx2);font-size:.9rem;margin-bottom:16px;max-width:900px}
.kpis{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.kpi{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.kpi .v{font-size:1.7rem;font-weight:800}.kpi .l{color:var(--tx2);font-size:.78rem;margin-top:3px}
.kpi.good .v{color:var(--good)}.kpi.warn .v{color:var(--warn)}.kpi.bad .v{color:var(--bad)}.kpi.neu .v{color:var(--cy)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:24px}@media(max-width:820px){.grid2{grid-template-columns:1fr}}
.panel{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px}
table{width:100%;border-collapse:collapse;font-size:.85rem}
th,td{text-align:left;padding:7px 9px;border-bottom:1px solid var(--line)}
th{color:var(--tx2);font-weight:600;cursor:pointer;user-select:none;position:sticky;top:0;background:var(--card2)}
th:hover{color:var(--cy)}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
tr:hover td{background:rgba(125,211,252,.05)}
.bar{height:20px;background:linear-gradient(90deg,var(--bl),var(--cy));border-radius:4px}
.barrow{display:flex;align-items:center;gap:10px;margin:5px 0;font-size:.82rem}
.barrow .lab{width:130px;color:var(--tx2);flex:none;text-align:right}
.barrow .n{width:46px;flex:none;font-variant-numeric:tabular-nums}
.barwrap{flex:1;background:#0b1626;border-radius:4px}
.tabs{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px}
.tab{background:var(--card);border:1px solid var(--line);color:var(--tx2);border-radius:8px;padding:7px 12px;cursor:pointer;font-size:.83rem}
.tab.on{background:var(--bl);color:#fff;border-color:var(--bl)}
.tab .c{display:inline-block;background:rgba(0,0,0,.25);border-radius:10px;padding:0 7px;margin-left:6px;font-size:.75rem}
.tab.crit .c{background:var(--bad);color:#fff}.tab.warnc .c{background:var(--warn);color:#0b1626}
.list{max-height:430px;overflow:auto;border:1px solid var(--line);border-radius:8px}
.pill{display:inline-block;font-size:.7rem;padding:1px 7px;border-radius:10px;background:#0b1626;border:1px solid var(--line);color:var(--tx2)}
.flag{font-size:.68rem;padding:1px 6px;border-radius:6px;margin-right:3px}
.f-bad{background:rgba(239,68,68,.16);color:#fca5a5}.f-warn{background:rgba(245,158,11,.16);color:#fcd34d}.f-good{background:rgba(34,197,94,.16);color:#86efac}
.controls{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:12px}
input,select{background:#0b1626;border:1px solid var(--line);color:var(--tx);border-radius:8px;padding:8px 11px;font-size:.85rem}
input{min-width:240px}
.note{background:rgba(245,158,11,.1);border-left:3px solid var(--warn);padding:12px 16px;border-radius:8px;margin:14px 0;font-size:.9rem;color:#fcd34d}
.good-li{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:13px 16px;margin-bottom:10px;font-size:.9rem}
.good-li b{color:var(--good)}
.fixcard{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin-bottom:10px}
.fixhead{display:flex;align-items:center;gap:10px;flex-wrap:wrap}.fixhead b{font-size:.95rem}
.eff{margin-left:auto;font-size:.72rem;color:var(--tx2);background:#0b1626;border:1px solid var(--line);border-radius:10px;padding:2px 8px}
.tag{font-size:.7rem;padding:2px 8px;border-radius:10px;font-weight:700}
.t-now{background:var(--bad);color:#fff}.t-soon{background:var(--warn);color:#0b1626}.t-later{background:var(--bl);color:#fff}
.trendgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(195px,1fr));gap:12px}
details summary{cursor:pointer}
.muted{color:var(--tx2)}
code{background:#0b1626;padding:1px 6px;border-radius:5px;color:var(--cy);font-size:.85em}
`;

const JS = [
"var P=DATA.pages, S=DATA.summary;",
"function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;');}",
"function kpi(v,l,cls){return '<div class=\"kpi '+(cls||'')+'\"><div class=\"v\">'+v+'</div><div class=\"l\">'+l+'</div></div>';}",
"document.getElementById('kpis').innerHTML=[",
" kpi(S.totalFiles,'HTML pages','neu'),kpi(S.indexable,'Indexable','neu'),kpi(S.inSitemap+' / '+S.sitemapTotal,'In sitemap','neu'),",
" kpi(S.clusters,'Clusters/sections','neu'),kpi(S.articles,'Articles','neu'),kpi(S.avgArticleWords,'Avg article words',S.avgArticleWords>=1000?'good':'warn'),",
" kpi(S.dupTitles,'Duplicate titles',S.dupTitles?'bad':'good'),kpi(S.orphans,'Orphans (0 inbound)',S.orphans>5?'bad':'good'),",
" kpi(S.brokenLinks,'Broken internal links',S.brokenLinks?'bad':'good'),kpi(S.veryThin,'Very thin articles',S.veryThin>20?'bad':'warn'),",
" kpi(S.thin,'Thin articles',S.thin>50?'warn':'good'),kpi(S.weak,'Weak links (1-2 inb)','warn'),",
" kpi(S.notInSitemap,'Not in sitemap',S.notInSitemap?'warn':'good'),kpi(S.noindexInSitemap,'Noindex in sitemap',S.noindexInSitemap?'warn':'good'),",
" kpi(S.filler,'data-batch filler',S.filler?'warn':'good'),kpi(S.stale,'Stale articles',S.stale?'warn':'good'),",
" kpi(S.noSchema,'Missing schema',S.noSchema?'warn':'good'),kpi(S.withTool,'Pages w/ tool','neu')",
"].join('');",
"var cl=DATA.clusterArr, cSort={k:'n',d:-1};",
"function renderCl(){var rows=cl.slice().sort(function(a,b){var x=a[cSort.k],y=b[cSort.k];if(typeof x==='string'){return cSort.d*x.localeCompare(y);}return cSort.d*(x-y);});",
" var h='<table><thead><tr>'+['cluster|Cluster','n|Pages','avgw|Avg words','thin|Thin','orphan|Orphans','avgInb|Avg inbound','inSm|In sitemap','broken|Broken'].map(function(c){var p=c.split('|');return '<th data-k=\"'+p[0]+'\" class=\"'+(p[0]==='cluster'?'':'num')+'\">'+p[1]+'</th>';}).join('')+'</tr></thead><tbody>';",
" rows.forEach(function(o){h+='<tr><td>'+esc(o.cluster)+'</td><td class=num>'+o.n+'</td><td class=num>'+o.avgw+'</td><td class=num>'+(o.thin||'')+'</td><td class=num>'+(o.orphan||'')+'</td><td class=num>'+o.avgInb+'</td><td class=num>'+o.inSm+'</td><td class=num>'+(o.broken||'')+'</td></tr>';});",
" document.getElementById('cltbl').innerHTML=h+'</tbody></table>';",
" document.querySelectorAll('#cltbl th').forEach(function(t){t.onclick=function(){var k=t.getAttribute('data-k');cSort.d=(cSort.k===k?-cSort.d:-1);cSort.k=k;renderCl();};});}",
"renderCl();",
"function bars(id,items){var m=Math.max.apply(null,items.map(function(i){return i.n;}));document.getElementById(id).innerHTML=items.map(function(i){var w=(i.n/m*100).toFixed(1);return '<div class=barrow><div class=lab>'+esc(i.label)+'</div><div class=barwrap><div class=bar style=\"width:'+w+'%\"></div></div><div class=n>'+i.n+'</div></div>';}).join('');}",
"bars('typedist',Object.keys(DATA.typeDist).map(function(k){return {label:k,n:DATA.typeDist[k]};}).sort(function(a,b){return b.n-a.n;}));",
"bars('hist',DATA.hist.map(function(b){return {label:b.label+' w',n:b.n};}));",
// fixes + opps
"function fcard(f){var s=f.sample&&f.sample.length?'<details style=\"margin-top:8px\"><summary class=muted style=\"font-size:.8rem\">'+f.sample.length+' example pages</summary><div style=\"font-size:.78rem;color:var(--tx2);margin-top:6px;line-height:1.8;font-family:monospace\">'+f.sample.map(esc).join('<br>')+'</div></details>':'';return '<div class=fixcard><div class=fixhead><span class=\"tag t-'+f.pri.toLowerCase()+'\">'+f.pri+'</span><b>'+esc(f.title)+'</b><span class=eff>'+f.effort+' effort</span></div><div class=muted style=\"font-size:.85rem;margin-top:6px\">'+esc(f.how)+'</div>'+s+'</div>';}",
"document.getElementById('fixes').innerHTML=DATA.fixes.map(fcard).join('')||'<div class=good-li>No open issues — clean.</div>';",
"document.getElementById('opps').innerHTML=DATA.opps.map(function(o){var s=o.sample&&o.sample.length?'<div style=\"font-size:.8rem;color:var(--tx2);margin-top:8px;line-height:1.8\">'+o.sample.map(function(x){return '&bull; '+esc(x);}).join('<br>')+'</div>':'';return '<div class=fixcard><div class=fixhead><b>'+esc(o.title)+'</b><span class=eff>'+esc(o.impact)+'</span></div><div class=muted style=\"font-size:.85rem;margin-top:6px\">'+esc(o.detail)+'</div>'+s+'</div>';}).join('');",
// trends
"var H=DATA.history;",
"function spark(vals){if(!vals||vals.length<2)return '<span class=muted style=\"font-size:.72rem\">collecting&hellip; (need 2+ runs)</span>';var mn=Math.min.apply(null,vals),mx=Math.max.apply(null,vals),r=(mx-mn)||1,w=170,h=34;var pts=vals.map(function(v,i){return (i/(vals.length-1)*w).toFixed(1)+','+(h-((v-mn)/r)*h).toFixed(1);}).join(' ');return '<svg width='+w+' height='+h+' style=\"display:block\"><polyline points=\"'+pts+'\" fill=none stroke=\"#7dd3fc\" stroke-width=2 stroke-linejoin=round stroke-linecap=round /></svg>';}",
"var METR=[['broken','Broken links',1],['thin','Thin 500-800',1],['veryThin','Very thin',1],['filler','Filler',1],['weak','Weak inbound',1],['stale','Stale',1],['articles','Articles',0],['tools','Pages w/ tool',0]];",
"document.getElementById('trendcards').innerHTML=METR.map(function(m){var vals=H.map(function(h){return h[m[0]];}).filter(function(v){return v!=null;});var last=vals.length?vals[vals.length-1]:0,prev=vals.length>1?vals[vals.length-2]:null;var d=prev==null?'':last-prev;var col=d===''?'var(--tx2)':((m[2]?(d<0):(d>0))?'var(--good)':(d===0?'var(--tx2)':'var(--bad)'));var dt=d===''?'&middot;':(d>0?'\\u25b2'+d:(d<0?'\\u25bc'+Math.abs(d):'\\u2014'));return '<div class=kpi><div style=\"display:flex;justify-content:space-between;align-items:baseline\"><div class=v style=\"font-size:1.3rem\">'+last+'</div><div style=\"font-size:.8rem;color:'+col+'\">'+dt+'</div></div><div class=l>'+m[1]+'</div><div style=\"margin-top:8px\">'+spark(vals)+'</div></div>';}).join('');",
"var hcols=[['date','Date'],['files','Pages'],['articles','Articles'],['broken','Broken'],['veryThin','VThin'],['thin','Thin'],['weak','Weak'],['filler','Filler'],['stale','Stale'],['tools','Tools']];",
"var hh='<table><thead><tr>'+hcols.map(function(c){return '<th'+(c[0]==='date'?'':' class=num')+'>'+c[1]+'</th>';}).join('')+'</tr></thead><tbody>';H.slice().reverse().forEach(function(r){hh+='<tr>'+hcols.map(function(c){return '<td'+(c[0]==='date'?'':' class=num')+'>'+(r[c[0]]==null?'':r[c[0]])+'</td>';}).join('')+'</tr>';});document.getElementById('histtbl').innerHTML=hh+'</tbody></table>';",
// issues tabs
"var L=DATA.lists;",
"function listKW(a){return a.map(function(p){return row(p.k,'<span class=pill>'+p.t+'</span> <span class=pill>'+p.w+'w</span>');}).join('');}",
"function row(k,meta){return '<div style=\"display:flex;justify-content:space-between;gap:10px;padding:7px 12px;border-bottom:1px solid var(--line);font-size:.82rem\"><span>'+esc(k)+'</span><span style=flex:none>'+meta+'</span></div>';}",
"var TABS=[",
" {name:'Broken links',crit:1,n:L.broken.length,render:function(){var by={};L.broken.forEach(function(b){(by[b.from]=by[b.from]||[]).push(b.href);});return Object.keys(by).sort().map(function(f){return '<div style=\"padding:8px 12px;border-bottom:1px solid var(--line)\"><b>'+esc(f)+'</b> <span class=muted>('+by[f].length+')</span><br><span class=muted style=\"font-size:.8rem\">'+by[f].map(esc).join(' &middot; ')+'</span></div>';}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Very thin articles',crit:1,n:L.veryThin.length,render:function(){return listKW(L.veryThin);}},",
" {name:'Thin articles',warnc:1,n:L.thin.length,render:function(){return listKW(L.thin);}},",
" {name:'Weak (1-2 inbound)',warnc:1,n:L.weak.length,render:function(){return L.weak.map(function(p){return row(p.k,'<span class=pill>'+p.t+'</span> <span class=pill>'+p.w+'w</span> <span class=pill>'+p.i+' inbound</span>');}).join('');}},",
" {name:'Orphans',crit:1,n:L.orphans.length,render:function(){return listKW(L.orphans)||'<div style=padding:14px>None.</div>';}},",
" {name:'Not in sitemap',warnc:1,n:L.notInSitemap.length,render:function(){return L.notInSitemap.map(function(p){return row(p.k,'<span class=pill>'+p.t+'</span>');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Noindex in sitemap',warnc:1,n:L.noindexInSitemap.length,render:function(){return L.noindexInSitemap.map(function(p){return row(p.k,'');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'data-batch filler',warnc:1,n:L.filler.length,render:function(){return L.filler.map(function(p){return row(p.k,'<span class=pill>'+p.w+'w</span>');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Stale articles',warnc:1,n:L.stale.length,render:function(){return L.stale.map(function(p){return row(p.k,'<span class=pill>mod '+p.m+'</span> <span class=pill>'+p.w+'w</span>');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Missing schema',warnc:1,n:L.noSchema.length,render:function(){return L.noSchema.map(function(p){return row(p.k,'<span class=pill>'+p.t+'</span>');}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Duplicate titles',n:L.dupTitles.length,render:function(){return L.dupTitles.length?L.dupTitles.map(function(d){return '<div style=\"padding:8px 12px;border-bottom:1px solid var(--line)\"><b>'+esc(d.t)+'</b><br>'+d.v.map(esc).join('<br>')+'</div>';}).join(''):'<div style=padding:14px>None &mdash; clean.</div>';}}",
"];",
"var panelEl=document.getElementById('tabpanel');",
"document.getElementById('tabs').innerHTML=TABS.map(function(t,i){return '<div class=\"tab'+(i===0?' on':'')+(t.crit?' crit':'')+(t.warnc?' warnc':'')+'\" data-i=\"'+i+'\">'+t.name+'<span class=c>'+t.n+'</span></div>';}).join('');",
"function showTab(i){panelEl.innerHTML='<div class=list>'+(TABS[i].render()||'<div style=padding:14px>None.</div>')+'</div>';document.querySelectorAll('#tabs .tab').forEach(function(t,j){t.classList.toggle('on',j==i);});}",
"document.querySelectorAll('#tabs .tab').forEach(function(t){t.onclick=function(){showTab(+t.getAttribute('data-i'));};});showTab(0);",
"var eSort={k:'wc',d:-1};",
"function flags(p){var f=[];if(p.inbound===0&&!/^\\/(index)?$/.test(p.key))f.push('<span class=\"flag f-bad\">orphan</span>');if(p.wc<500)f.push('<span class=\"flag f-bad\">thin</span>');else if(p.wc<800)f.push('<span class=\"flag f-warn\">lean</span>');if(p.broken.length)f.push('<span class=\"flag f-bad\">'+p.broken.length+' broken</span>');if(p.noindex)f.push('<span class=\"flag f-warn\">noindex</span>');if(!p.inSitemap)f.push('<span class=\"flag f-warn\">no-sitemap</span>');if(p.dataBatch)f.push('<span class=\"flag f-warn\">filler</span>');if(p.schema.length===0)f.push('<span class=\"flag f-warn\">no-schema</span>');if(p.hasTool)f.push('<span class=\"flag f-good\">tool</span>');return f.join('');}",
"function renderEx(){var q=document.getElementById('q').value.toLowerCase();var ft=document.getElementById('ft').value;",
" var rows=P.filter(function(p){return (!q||p.key.toLowerCase().indexOf(q)>=0||(p.title||'').toLowerCase().indexOf(q)>=0)&&(!ft||p.type===ft);});",
" rows.sort(function(a,b){var x=a[eSort.k],y=b[eSort.k];if(typeof x==='string')return eSort.d*x.localeCompare(y);return eSort.d*((x||0)-(y||0));});",
" document.getElementById('excount').textContent=rows.length+' pages';",
" var h='<table><thead><tr>'+['key|Page','type|Type','wc|Words','inbound|Inbound','schema|Schema','x|Flags'].map(function(c){var p=c.split('|');return '<th data-k=\"'+p[0]+'\" class=\"'+(/wc|inbound/.test(p[0])?'num':'')+'\">'+p[1]+'</th>';}).join('')+'</tr></thead><tbody>';",
" rows.slice(0,400).forEach(function(p){h+='<tr><td>'+esc(p.key)+'</td><td><span class=pill>'+p.type+'</span></td><td class=num>'+p.wc+'</td><td class=num>'+p.inbound+'</td><td class=num>'+p.schema.length+'</td><td>'+flags(p)+'</td></tr>';});",
" h+='</tbody></table>';if(rows.length>400)h+='<div class=muted style=padding:10px>Showing first 400 of '+rows.length+'.</div>';",
" document.getElementById('extbl').innerHTML=h;",
" document.querySelectorAll('#extbl th').forEach(function(t){t.onclick=function(){var k=t.getAttribute('data-k');eSort.d=(eSort.k===k?-eSort.d:-1);eSort.k=k;renderEx();};});}",
"document.getElementById('q').oninput=renderEx;document.getElementById('ft').onchange=renderEx;",
"document.getElementById('ft').innerHTML='<option value=\"\">All types</option>'+Object.keys(DATA.typeDist).sort().map(function(t){return '<option>'+t+'</option>';}).join('');",
"renderEx();",
// visual architecture pills
"document.getElementById('arch').innerHTML=DATA.arch.map(function(g){var pills=g.items.map(function(i){return '<span class=routepill>'+esc(i.label)+'<span class=ct>'+i.n+'</span></span>';}).join('');return '<div class=arch-card><h3>'+esc(g.cat)+'</h3>'+pills+'</div>';}).join('');",
// top-level tab switching
"document.querySelectorAll('.toptab').forEach(function(t){t.onclick=function(){var p=t.getAttribute('data-pane');document.querySelectorAll('.toptab').forEach(function(x){x.classList.toggle('on',x===t);});document.querySelectorAll('.tabpane').forEach(function(pane){pane.classList.toggle('on',pane.id==='pane-'+p);});window.scrollTo(0,0);};});"
].join("\n");

const Sx = summary;
const HTML =
'<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'+
'<title>Axiant Partners &mdash; Site Audit</title><style>'+CSS+'</style></head><body>'+
'<header class=hd><div class=wrap>'+
'<span class="pillbadge pb-green">Site Architecture &amp; SEO Audit</span>'+
'<span class="pillbadge pb-gen"><span class=dot></span>Auto-generated '+stamp+'</span>'+
'<h1>Axiant Partners &mdash; Full Site Breakdown</h1>'+
'<p class=lede>Every published page on axiantpartners.com, mapped by type, cluster, and content health. Page counts and structure are <b>auto-derived from the codebase on every commit</b> &mdash; this report regenerated <b>'+stamp+'</b>. The <b>Fixes &amp; Opportunities</b> tab is where the work is.</p>'+
'</div></header><div class=wrap>'+
'<div class=kpis id=kpis></div>'+
'<div class=note><b>Top findings:</b> <b>'+Sx.brokenLinks+' broken internal links</b>, <b>'+Sx.filler+' pages with <code>data-batch</code> filler</b>, <b>'+Sx.noindexInSitemap+' noindex pages in the sitemap</b>, and <b>'+(Sx.veryThin+Sx.thin)+' thin articles</b> &mdash; see the Fixes &amp; Opportunities tab.</div>'+
'<div class=toptabs><div class="toptab on" data-pane="overview">&#128202; Overview &amp; Audit</div><div class=toptab data-pane="fixes">&#128295; Fixes &amp; Opportunities</div></div>'+
'<div class="tabpane on" id="pane-overview">'+
'<h2 class=sec>Visual architecture</h2><div class=sub>Every section of the site by route prefix, with live page counts &mdash; auto-derived from the codebase. Financing products and industry clusters are the backbone; equipment subtypes, guides, and landing pages fill the long tail.</div><div class=arch-grid id=arch></div>'+
'<h2 class=sec>Page types &amp; content depth</h2><div class=sub>Static, framework-free HTML on Netlify: service hubs, industry hubs, per-cluster articles, amount/geo landing pages, calculators, and ad-landing variants.</div>'+
'<div class=grid2><div class=panel><h3 style="margin-bottom:10px;font-size:.95rem">Page types</h3><div id=typedist></div></div>'+
'<div class=panel><h3 style="margin-bottom:10px;font-size:.95rem">Content depth (words, content pages)</h3><div id=hist></div></div></div>'+
'<h2 class=sec>Clusters &mdash; depth &amp; health</h2><div class=sub>Click headers to sort.</div><div class=panel style="overflow:auto;max-height:540px" id=cltbl></div>'+
'<h2 class=sec>Issues &mdash; raw lists</h2><div class=sub>Each tab is a working list. Red = highest priority.</div><div class=tabs id=tabs></div><div id=tabpanel></div>'+
'<h2 class=sec>What is good</h2>'+
'<div class="good-li"><b>Strong topical clustering.</b> '+Sx.clusters+' clusters, '+Sx.articles+' articles averaging '+Sx.avgArticleWords+' words.</div>'+
'<div class="good-li"><b>Almost no orphans ('+Sx.orphans+') and '+Sx.dupTitles+' duplicate titles.</b> Interlinking + cannibalization work paid off.</div>'+
'<div class="good-li"><b>'+Sx.ldFails+' JSON-LD parse failures; schema near-universal</b> ('+Sx.noSchema+' content pages without it). Strong AEO/GEO base.</div>'+
'<h2 class=sec>Explore every page</h2><div class=sub>Search, filter by type, click headers to sort. Flags show each page\'s issues.</div>'+
'<div class=controls><input id=q placeholder="Search URL or title..."><select id=ft></select><span class=muted id=excount style="align-self:center"></span></div>'+
'<div class=panel style="overflow:auto;max-height:640px" id=extbl></div>'+
'</div>'+
'<div class=tabpane id="pane-fixes">'+
'<h2 class=sec>Suggested fixes</h2><div class=sub>Auto-derived from the data, prioritized NOW / SOON / LATER with effort and example pages. Expand any card for the affected URLs.</div><div id=fixes></div>'+
'<h2 class=sec>Things to go after</h2><div class=sub>Growth opportunities that won\'t cannibalize existing pages &mdash; sized by data where possible.</div><div id=opps></div>'+
'<h2 class=sec>Trends over time</h2><div class=sub>Each run appends a snapshot (deduped per day). Arrows compare to the previous run &mdash; green is the good direction. Sparklines fill in as history accumulates.</div><div class=trendgrid id=trendcards style="margin-bottom:18px"></div><div class=panel style="overflow:auto;max-height:340px" id=histtbl></div>'+
'</div>'+
'<p class=muted style="margin-top:30px;font-size:.8rem">Auto-generated '+stamp+' by scripts/site-audit.js from '+Sx.totalFiles+' HTML files. Word counts use the &lt;main&gt; region where present. Orphan = 0 resolved inbound links excluding global nav/footer.</p>'+
'</div><script>\nvar DATA='+JSON.stringify(DATA)+';\n'+JS+'\n</script></body></html>';

fs.writeFileSync(path.join(OUT_DIR, 'site-audit.html'), HTML);
console.log('[site-audit] '+Sx.totalFiles+' pages, '+Sx.articles+' articles | broken:'+Sx.brokenLinks+' thin:'+(Sx.veryThin+Sx.thin)+' filler:'+Sx.filler+' | history:'+history.length+' snapshot(s) -> _analysis/site-audit.html');
