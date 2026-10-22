/* attribution.js: the first-touch lead attribution block, standalone.
 *
 * A VERBATIM COPY of the block at the top of script.js (lines 1 to the first
 * "})();"). It exists for pages that do not load script.js: the homepage and the
 * generated equipment-for-sale pages. Without it, a visitor who lands on one of
 * those pages and then opens /match.html is recorded as landing on /match.html
 * with an axiantpartners.com referrer, i.e. channel "internal", and the real
 * source (ChatGPT, Google, a utm tag) is lost.
 *
 * Keep the two copies identical. If you change the block in script.js, copy it
 * here and bump ?v= on the pages that load this file.
 * Running both on one page is harmless: capture() is first-touch and returns the
 * saved record on every later call.
 */
/* ─── Lead attribution ──────────────────────────────────────────────────────
 * Records WHERE a lead came from. Nothing on this site did before, which is
 * why 50+ applications a month couldn't be traced to a channel — Search
 * Console only sees Google Search clicks, so AI-assistant referrals, direct,
 * Bing and partner traffic were all invisible.
 *
 * Captured on the FIRST page of the session and kept in sessionStorage: by the
 * time someone reaches the form, document.referrer is the previous page of
 * this site and the UTM tags are long gone from the URL. Reading either at
 * submit time would attribute every lead to "internal".
 */
(function(){
  var KEY='ax_attr';
  function readParams(){
    try{ return new URLSearchParams(location.search); }catch(e){ return null; }
  }
  /** Group a referrer host into something a human can act on. */
  function classify(ref, p){
    if(p&&(p.get('gclid')||p.get('gbraid')||p.get('wbraid')||p.get('utm_medium')==='cpc'||p.get('utm_medium')==='ppc')) return 'paid';
    /* AI assistants tag their own outbound links and several strip the referrer,
     * so the referrer alone under-counts them badly: ChatGPT sends
     * ?utm_source=chatgpt.com and Copilot ?utm_source=copilot.com. Reading only
     * document.referrer filed 9 of 28 AI-assistant leads as "direct", including
     * the one web application that has actually funded. Checked before the
     * referrer because when both are present the tag is the more specific signal. */
    var src='';
    try{ src=((p&&p.get('utm_source'))||'').toLowerCase(); }catch(e){ src=''; }
    if(src&&/(chatgpt|openai|copilot|perplexity|claude\.ai|anthropic|gemini|bard|you\.com|poe\.com|phind)/.test(src)) return 'ai_assistant';
    var h='';
    try{ h=ref?new URL(ref).hostname.replace(/^www\./,'').toLowerCase():''; }catch(e){ h=''; }
    if(!h) return 'direct';
    if(h.indexOf('axiantpartners.com')>-1) return 'internal';
    // AI assistants — the channel we most suspect and could least see.
    if(/(^|\.)(chatgpt\.com|chat\.openai\.com|openai\.com|perplexity\.ai|claude\.ai|anthropic\.com|gemini\.google\.com|bard\.google\.com|copilot\.microsoft\.com|you\.com|poe\.com|phind\.com|arc\.net)$/.test(h)) return 'ai_assistant';
    if(/(^|\.)(google\.[a-z.]+|bing\.com|duckduckgo\.com|search\.yahoo\.com|yahoo\.com|ecosia\.org|brave\.com|startpage\.com|baidu\.com|yandex\.[a-z]+)$/.test(h)) return 'organic_search';
    if(/(^|\.)(facebook\.com|instagram\.com|linkedin\.com|lnkd\.in|t\.co|twitter\.com|x\.com|reddit\.com|youtube\.com|tiktok\.com|pinterest\.com)$/.test(h)) return 'social';
    return 'referral';
  }
  function capture(){
    var saved=null;
    try{ saved=JSON.parse(sessionStorage.getItem(KEY)||'null'); }catch(e){}
    if(saved&&saved.channel) return saved;
    var p=readParams(), ref=document.referrer||'';
    var a={
      channel:classify(ref,p),
      referrer:ref||'(none)',
      landing_page:location.pathname+(location.search||''),
      captured_at:new Date().toISOString()
    };
    if(p){
      ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','gbraid','wbraid','fbclid','msclkid'].forEach(function(k){
        var v=p.get(k); if(v) a[k]=v;
      });
    }
    try{ sessionStorage.setItem(KEY,JSON.stringify(a)); }catch(e){}
    return a;
  }
  var attr=capture();
  /* Ad click ids, kept for 90 days (Google's click-through conversion window).
   * capture() is first-touch and per-tab, so a visitor who clicks an ad, leaves and
   * comes back later to apply would otherwise submit with no click id - and a
   * conversion Google cannot tie to its click. Newest click wins here, because the
   * ad platforms attribute to the last ad click. gbraid/wbraid are what Google sends
   * instead of gclid for many iOS clicks. */
  var CLICK_KEY='ax_click_ids', CLICK_IDS=['gclid','gbraid','wbraid','msclkid'];
  (function(){
    var p=readParams(); if(!p) return;
    var ids={}, any=false;
    CLICK_IDS.forEach(function(k){ var v=p.get(k); if(v){ ids[k]=v; any=true; } });
    if(!any) return;
    ids.at=Date.now();
    try{ localStorage.setItem(CLICK_KEY,JSON.stringify(ids)); }catch(e){}
  })();
  function storedClickIds(){
    try{
      var c=JSON.parse(localStorage.getItem(CLICK_KEY)||'null');
      if(c&&c.at&&Date.now()-c.at<90*864e5) return c;
    }catch(e){}
    return null;
  }
  /**
   * The referral partner token from /page?ref=TOKEN, held for the whole session.
   *
   * Nothing about a submission says which partner sent it except this token, and
   * it lives only in the URL — so a visitor who lands on a partner link, reads a
   * page or two and comes back to apply would otherwise submit with the token
   * gone and the attribution silently lost. That failure passes every hand test
   * (you apply straight away) and fails for real partners, so it is stored.
   *
   * Two sources, because either alone has a hole: the current URL catches a land
   * directly on /match.html?ref=..., and `attr.landing_page` — first-touch and
   * never overwritten, see capture() above — catches a land on /?ref=... followed
   * by navigation to the form.
   */
  var REF_KEY='axp_ref';
  (function(){
    var p=readParams();
    var token=(p&&p.get('ref')||'').trim();
    if(!token&&attr&&attr.landing_page){
      try{ token=(new URL(attr.landing_page,location.origin).searchParams.get('ref')||'').trim(); }catch(e){}
    }
    if(token){ try{ sessionStorage.setItem(REF_KEY,token); }catch(e){} }
  })();
  /** The stored token, or null. The CRM treats an unknown token as no referral. */
  window.__axRef=function(){
    try{ return sessionStorage.getItem(REF_KEY)||null; }catch(e){ return null; }
  };
  /** Flat params for EmailJS / Netlify. `lead_source` is the one-line summary. */
  window.__axAttr=function(){
    var a=attr||{}, bits=[];
    bits.push('Channel: '+(a.channel||'unknown'));
    bits.push('Landed on: '+(a.landing_page||'?'));
    bits.push('Referrer: '+(a.referrer||'(none)'));
    if(a.utm_source) bits.push('Campaign: '+a.utm_source+' / '+(a.utm_medium||'?')+(a.utm_campaign?' / '+a.utm_campaign:''));
    var out={
      lead_source:bits.join(' | '),
      lead_channel:a.channel||'unknown',
      lead_referrer:a.referrer||'(none)',
      lead_landing_page:a.landing_page||'',
      lead_submitted_from:location.pathname
    };
    ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid','gbraid','wbraid','fbclid','msclkid'].forEach(function(k){
      if(a[k]) out[k]=a[k];
    });
    var c=storedClickIds();
    if(c){ CLICK_IDS.forEach(function(k){ if(!out[k]&&c[k]) out[k]=c[k]; }); }
    return out;
  };
})();
