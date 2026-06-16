#!/usr/bin/env node
/* Axiant Partners full-site audit -> self-contained HTML dashboard.
 * Run: node scripts/site-audit.js   (or: npm run audit)
 * Output: _analysis/site-audit.html  (gitignored; never deployed)
 * Auto-runs via .git/hooks/post-commit after every commit. */
const fs = require('fs'), path = require('path');
const ROOT = process.cwd();
const OUT_DIR = path.join(ROOT, '_analysis');
const today = new Date().toISOString().slice(0, 10);

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
const veryThin = indexable.filter(p=>isContent(p)&&p.wc<500 && p.type!=='cluster-index');
const thin = indexable.filter(p=>isContent(p)&&p.wc>=500&&p.wc<800 && p.type!=='cluster-index');
const brokenList=[]; for(const p of arr) for(const b of p.broken) brokenList.push({from:p.key, href:b});
const notInSitemap = indexable.filter(p=>!p.inSitemap && !['core','fragment','ad-landing','cluster-index'].includes(p.type));
const noindexInSitemap = arr.filter(p=>p.noindex && p.inSitemap);
const deadSitemap=[...sitemapKeys].filter(k=>!pages[k]);
const noSchema = indexable.filter(p=>isContent(p)&&p.schema.length===0 && p.type!=='cluster-index');
const ldFails = arr.filter(p=>p.ldFail>0);
const stale = articles.filter(p=>!p.mod || p.mod < '2026-03-01');
const filler = arr.filter(p=>p.dataBatch);
const weak = indexable.filter(p=>isContent(p)&&p.inbound>0&&p.inbound<=2&&p.type!=='core'&&!CHROME.has(p.key));
const clusters={};
for(const p of arr){ const o=(clusters[p.cluster]=clusters[p.cluster]||{cluster:p.cluster,n:0,words:0,thin:0,orphan:0,noindex:0,inb:0,inSm:0,broken:0}); o.n++; o.words+=p.wc; if(p.wc<500&&isContent(p))o.thin++; if(p.inbound===0&&isContent(p)&&!CHROME.has(p.key))o.orphan++; if(p.noindex)o.noindex++; o.inb+=p.inbound; if(p.inSitemap)o.inSm++; o.broken+=p.broken.length; }
const clusterArr = Object.values(clusters).map(o=>({...o, avgw:Math.round(o.words/o.n), avgInb:(o.inb/o.n).toFixed(1)})).sort((a,b)=>b.n-a.n);
const typeDist={}; for(const p of arr) typeDist[p.type]=(typeDist[p.type]||0)+1;
const buckets=[[0,300],[300,600],[600,900],[900,1200],[1200,1600],[1600,99999]];
const hist=buckets.map(([a,b])=>({label:b>9000?(a+'+'):a+'-'+b, n: arr.filter(p=>isContent(p)&&p.wc>=a&&p.wc<b).length}));
const summary = {
  totalFiles: files.length, indexable: indexable.length, noindex: arr.length-indexable.length,
  inSitemap: arr.filter(p=>p.inSitemap).length, clusters: Object.keys(clusters).length,
  articles: articles.length, totalWords: arr.reduce((s,p)=>s+p.wc,0),
  avgArticleWords: Math.round(articles.reduce((s,p)=>s+p.wc,0)/(articles.length||1)),
  orphans: orphans.length, veryThin: veryThin.length, thin: thin.length, weak: weak.length,
  brokenLinks: brokenList.length, notInSitemap: notInSitemap.length, noindexInSitemap: noindexInSitemap.length,
  deadSitemap: deadSitemap.length, noSchema: noSchema.length, ldFails: ldFails.length, dupTitles: dupTitles.length,
  filler: filler.length, stale: stale.length, sitemapTotal: sitemapKeys.size, withTool: arr.filter(p=>p.hasTool).length,
};
const DATA = { summary, pages: arr, clusterArr, typeDist, hist, lists: {
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
.hd h1{font-size:1.9rem;font-weight:800;letter-spacing:-.02em}
.hd p{color:var(--tx2);margin-top:6px;font-size:.95rem}
.badge{display:inline-block;background:#0b1626;border:1px solid var(--line);color:var(--cy);border-radius:20px;padding:3px 12px;font-size:.78rem;margin-right:8px;margin-top:10px}
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
.good-li,.plan-li{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:13px 16px;margin-bottom:10px;font-size:.9rem}
.good-li b{color:var(--good)}.plan-li b{color:var(--cy)}
.plan-li .tag{font-size:.7rem;padding:2px 8px;border-radius:10px;margin-right:8px;font-weight:700}
.t-now{background:var(--bad);color:#fff}.t-soon{background:var(--warn);color:#0b1626}.t-later{background:var(--bl);color:#fff}
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
" kpi(S.brokenLinks,'Broken internal links',S.brokenLinks?'bad':'good'),kpi(S.veryThin,'Very thin (<500w)',S.veryThin>20?'bad':'warn'),",
" kpi(S.thin,'Thin (500-800w)',S.thin>50?'warn':'good'),kpi(S.weak,'Weak links (1-2 inb)','warn'),",
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
"var L=DATA.lists;",
"function listKW(a){return a.map(function(p){return row(p.k,'<span class=pill>'+p.t+'</span> <span class=pill>'+p.w+'w</span>');}).join('');}",
"function row(k,meta){return '<div style=\"display:flex;justify-content:space-between;gap:10px;padding:7px 12px;border-bottom:1px solid var(--line);font-size:.82rem\"><span>'+esc(k)+'</span><span style=flex:none>'+meta+'</span></div>';}",
"var TABS=[",
" {name:'Broken links',crit:1,n:L.broken.length,render:function(){var by={};L.broken.forEach(function(b){(by[b.from]=by[b.from]||[]).push(b.href);});return Object.keys(by).sort().map(function(f){return '<div style=\"padding:8px 12px;border-bottom:1px solid var(--line)\"><b>'+esc(f)+'</b> <span class=muted>('+by[f].length+')</span><br><span class=muted style=\"font-size:.8rem\">'+by[f].map(esc).join(' &middot; ')+'</span></div>';}).join('')||'<div style=padding:14px>None.</div>';}},",
" {name:'Very thin <500w',crit:1,n:L.veryThin.length,render:function(){return listKW(L.veryThin);}},",
" {name:'Thin 500-800w',warnc:1,n:L.thin.length,render:function(){return listKW(L.thin);}},",
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
"renderEx();"
].join("\n");

const S = summary;
const HTML =
'<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">'+
'<title>Axiant Partners &mdash; Site Audit</title><style>'+CSS+'</style></head><body>'+
'<header class=hd><div class=wrap><h1>Axiant Partners &mdash; Full Site Audit</h1>'+
'<p>Structural &amp; content-health breakdown of every page. Auto-generated '+today+' (rebuilds after each commit).</p>'+
'<div><span class=badge>'+S.totalFiles+' pages</span><span class=badge>'+S.articles+' articles</span><span class=badge>'+S.clusters+' clusters</span><span class=badge>avg '+S.avgArticleWords+'w/article</span></div>'+
'</div></header><div class=wrap>'+
'<div class=note><b>Top findings:</b> <b>'+S.brokenLinks+' broken internal links</b>, <b>'+S.filler+' pages with <code>data-batch</code> filler</b>, <b>'+S.noindexInSitemap+' noindex pages in the sitemap</b>, and <b>'+(S.veryThin+S.thin)+' thin pages</b>. Work through the Issues tabs below.</div>'+
'<h2 class=sec>1. Scorecard</h2><div class=sub>Green = healthy, amber = attention, red = fix.</div><div class=kpis id=kpis></div>'+
'<h2 class=sec>2. How the site is built</h2><div class=sub>Static, framework-free HTML on Netlify. Service clusters (equipment-financing, sba-loans, working-capital-loans) and industry hubs (*-business-financing.html), each with an /articles/ folder, plus amount/geo landing pages, calculators, and ad-landing variants.</div>'+
'<div class=grid2><div class=panel><h3 style="margin-bottom:10px;font-size:.95rem">Page types</h3><div id=typedist></div></div>'+
'<div class=panel><h3 style="margin-bottom:10px;font-size:.95rem">Content depth (words, content pages)</h3><div id=hist></div></div></div>'+
'<h2 class=sec>3. Clusters &mdash; depth &amp; health</h2><div class=sub>Click headers to sort.</div><div class=panel style="overflow:auto;max-height:540px" id=cltbl></div>'+
'<h2 class=sec>4. Issues &mdash; what needs work</h2><div class=sub>Each tab is a ready-to-action list. Red = highest priority.</div><div class=tabs id=tabs></div><div id=tabpanel></div>'+
'<h2 class=sec>5. What is good</h2>'+
'<div class="good-li"><b>Strong topical clustering.</b> '+S.clusters+' clusters, '+S.articles+' articles averaging '+S.avgArticleWords+' words.</div>'+
'<div class="good-li"><b>Almost no orphans ('+S.orphans+').</b> Nearly every article is reachable from its hub/siblings.</div>'+
'<div class="good-li"><b>'+S.dupTitles+' duplicate titles, '+S.ldFails+' JSON-LD parse failures.</b> Cannibalization + structured-data hygiene are solid.</div>'+
'<div class="good-li"><b>Schema near-universal</b> &mdash; only '+S.noSchema+' content pages lack JSON-LD.</div>'+
'<h2 class=sec>6. What is bad / risky</h2>'+
'<div class="good-li" style="border-left:3px solid var(--bad)"><b style="color:#fca5a5">'+S.brokenLinks+' broken internal links.</b> Wastes crawl budget and drops link equity.</div>'+
'<div class="good-li" style="border-left:3px solid var(--bad)"><b style="color:#fca5a5">'+(S.veryThin+S.thin)+' thin pages</b> ('+S.veryThin+' <500w, '+S.thin+' 500-800w). Expand, merge, or prune.</div>'+
'<div class="good-li" style="border-left:3px solid var(--warn)"><b style="color:#fcd34d">'+S.filler+' pages carry <code>data-batch</code> filler</b> and '+S.noindexInSitemap+' noindex pages are wrongly in the sitemap; '+S.notInSitemap+' indexable pages are missing from it.</div>'+
'<div class="good-li" style="border-left:3px solid var(--warn)"><b style="color:#fcd34d">'+S.weak+' pages have only 1-2 inbound links</b> and '+S.stale+' articles are stale. Both lift with light passes.</div>'+
'<h2 class=sec>7. Forward plan</h2><div class=sub>Sequenced by impact-to-effort.</div>'+
'<div class="plan-li"><span class="tag t-now">NOW</span><b>Clear the '+S.brokenLinks+' broken links + strip the '+S.filler+' filler pages + fix sitemap noindex.</b></div>'+
'<div class="plan-li"><span class="tag t-now">NOW</span><b>Triage the '+S.veryThin+' very-thin pages</b> &mdash; expand to 1,000w+, merge, or 301/prune.</div>'+
'<div class="plan-li"><span class="tag t-soon">SOON</span><b>Conversion capture:</b> inline calculators + tight apply CTAs on top-impression pages (only '+S.withTool+' have a tool today).</div>'+
'<div class="plan-li"><span class="tag t-soon">SOON</span><b>Internal-linking pass on the '+S.weak+' weak pages</b> + refresh the '+S.stale+' stale articles.</div>'+
'<div class="plan-li"><span class="tag t-later">LATER</span><b>Net-new only where it can\'t cannibalize</b> &mdash; new verticals + comparison/"best-X" pages, each with apply CTAs.</div>'+
'<h2 class=sec>8. Explore every page</h2><div class=sub>Search, filter by type, click headers to sort. Flags show each page\'s issues.</div>'+
'<div class=controls><input id=q placeholder="Search URL or title..."><select id=ft></select><span class=muted id=excount style="align-self:center"></span></div>'+
'<div class=panel style="overflow:auto;max-height:640px" id=extbl></div>'+
'<p class=muted style="margin-top:30px;font-size:.8rem">Auto-generated by scripts/site-audit.js from '+S.totalFiles+' HTML files. Word counts use the &lt;main&gt; region where present. Orphan = 0 resolved inbound links excluding global nav/footer.</p>'+
'</div><script>\nvar DATA='+JSON.stringify(DATA)+';\n'+JS+'\n</script></body></html>';

if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });
fs.writeFileSync(path.join(OUT_DIR, 'site-audit.html'), HTML);
console.log('[site-audit] '+S.totalFiles+' pages, '+S.articles+' articles | broken:'+S.brokenLinks+' thin:'+(S.veryThin+S.thin)+' filler:'+S.filler+' -> _analysis/site-audit.html');
