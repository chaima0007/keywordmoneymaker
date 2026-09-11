/* Caelum — micro-interactions partagées (fichier externe, conforme CSP script-src 'self').
   Révélation au défilement, respectueuse de prefers-reduced-motion. Aucune dépendance. */
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var els = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    // Pas d'animation : tout est visible immédiatement.
    for (var i = 0; i < els.length; i++) els[i].classList.add("is-visible");
    return;
  }
  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add("is-visible");
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
  els.forEach(function (el) { obs.observe(el); });
})();
