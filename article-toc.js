/* Contents rail: lights the section you are reading, in the rail and in the
   article. Progressive enhancement - without it the list is still a list. */
(function () {
  var toc = document.querySelector('.toc');
  if (!toc) return;

  var pairs = [];                         // [heading, link], document order
  toc.querySelectorAll('a[href^="#"]').forEach(function (a) {
    var el = document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
    if (el) pairs.push([el, a]);
  });
  if (!pairs.length) return;

  var current = null;
  function light(pair) {
    var link = pair ? pair[1] : null;
    if (link === current) return;
    if (current) {
      current.classList.remove('is-current');
      var old = document.getElementById(
        decodeURIComponent(current.getAttribute('href').slice(1)));
      if (old) old.classList.remove('is-reading');
    }
    current = link;
    if (!pair) return;
    link.classList.add('is-current');
    pair[0].classList.add('is-reading');
    var rail = document.querySelector('.article-rail');
    if (!rail || rail.scrollHeight <= rail.clientHeight + 2) return;
    var a = link.getBoundingClientRect(), r = rail.getBoundingClientRect();
    if (a.top < r.top + 8 || a.bottom > r.bottom - 8) {
      rail.scrollTop += (a.top - r.top) - r.height / 3;
    }
  }

  /* The reading line sits 40% down the viewport: a section lights up as its
     heading rises into the upper part of the screen, not after it has left.
     Waiting for the heading to reach the top made the rail lag a section
     behind everything you were actually reading. */
  function update() {
    var line = window.innerHeight * 0.4;
    var pick = null;
    for (var i = 0; i < pairs.length; i++) {
      if (pairs[i][0].getBoundingClientRect().top <= line) pick = pairs[i];
    }
    if (!pick) pick = pairs[0];
    light(pick);
  }

  var queued = false;
  function onScroll() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(function () { queued = false; update(); });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  toc.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    for (var i = 0; i < pairs.length; i++) if (pairs[i][1] === a) light(pairs[i]);
  });
  update();
})();
