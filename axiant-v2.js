/* Axiant v2 - page behaviour.
   Single source of truth for every v2 page, the way axiant-v2.css is for
   styles. Loaded with `defer` from the header component, so it ships to every
   page sync-header-v2.py touches.

   Currently one job: the mobile menu. The desktop nav is display:none below
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
