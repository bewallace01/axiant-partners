/* Axiant v2 - page behaviour.
   Single source of truth for every v2 page, the way axiant-v2.css is for
   styles. Loaded with `defer` from the header component, so it ships to every
   page sync-header-v2.py touches.

   Job one: the mobile menu. Job two, at the bottom: phone-click tracking.
   The desktop nav is display:none below
   1000px and .nav-toggle takes its place, so without this the hamburger is a
   dead button and a phone has no way to navigate. */
(function () {
  'use strict';

  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('mobileMenu');
  var close = document.getElementById('navClose');
  if (!toggle || !menu || !close) return;

  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    menu.hidden = false;
    menu.dataset.open = 'true';
    document.body.dataset.menuOpen = 'true';
    toggle.setAttribute('aria-expanded', 'true');
    close.focus();
  }

  function shut() {
    menu.dataset.open = 'false';
    menu.hidden = true;
    delete document.body.dataset.menuOpen;
    toggle.setAttribute('aria-expanded', 'false');
    if (lastFocus) lastFocus.focus();
  }

  toggle.addEventListener('click', open);
  close.addEventListener('click', shut);

  // Click the scrim (but not the panel) to dismiss.
  menu.addEventListener('click', function (e) {
    if (e.target === menu) shut();
  });

  // Any link closes the panel before it navigates.
  menu.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', shut);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && menu.dataset.open === 'true') shut();
  });

  // Rotating a phone to landscape can cross the 1000px breakpoint and bring
  // the desktop nav back; don't leave the body scroll-locked behind it.
  window.matchMedia('(min-width:1001px)').addEventListener('change', function (e) {
    if (e.matches && menu.dataset.open === 'true') shut();
  });

  // Mark the current page in both navs. Cheap, and it stops every v2 page
  // needing a hand-set "active" class the sync script would overwrite.
  // Pages preview as *-v2.html but ship at their original filename, and the
  // nav links to the shipped names - so normalise before comparing, or the
  // marking silently never matches while previewing.
  var here = window.location.pathname
    .replace(/-v2\.html$/, '.html')
    .replace(/\/index\.html$/, '/');
  document.querySelectorAll('.nav a, .mobile-menu nav a').forEach(function (a) {
    if (a.getAttribute('href') === here) a.setAttribute('aria-current', 'page');
  });
})();

/* Phone-click tracking, for every page that loads this file. Sends a GA4 event
   when someone taps a phone link, so GA4 shows which page drove it (the event's
   page path). Axiant's own line is phone_click. Numbers on equipment listings
   belong to the sellers, so they are listing_phone_click. No phone number or
   visitor detail is sent. A click means they tried to call, not that a call
   connected. */
(function () {
  'use strict';

  /* Some pages load this file twice, which would count every click twice. */
  if (window.axiantPhoneClicks) return;
  window.axiantPhoneClicks = true;

  var GA_ID = 'G-HZNSHH6NN0';
  var MAIN_LINE = '5612680465';

  /* Some pages have no Google tag in their head, and a click there would go
     nowhere. Load the same deferred tag those other pages use. */
  if (typeof window.gtag !== 'function') {
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    var loadTag = function () {
      var s = document.createElement('script');
      s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
      s.onload = function () {
        window.gtag('js', new Date());
        window.gtag('config', GA_ID);
      };
      document.head.appendChild(s);
    };
    if (document.readyState === 'complete') loadTag();
    else window.addEventListener('load', loadTag);
  }

  document.addEventListener('click', function (e) {
    var link = e.target && e.target.closest && e.target.closest('a[href^="tel:"]');
    if (!link) return;
    var digits = link.getAttribute('href').replace(/\D/g, '').slice(-10);
    var area = link.closest('.mobile-menu, nav') ? 'menu'
      : link.closest('header') ? 'header'
      : link.closest('footer') ? 'footer'
      : 'page';
    window.gtag('event', digits === MAIN_LINE ? 'phone_click' : 'listing_phone_click', {
      link_area: area,
      transport_type: 'beacon'
    });
  });
})();
