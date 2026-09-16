/* Caelum — micro-interactions partagées (fichier externe, conforme CSP script-src 'self').
   Révélation au défilement, respectueuse de prefers-reduced-motion. Aucune dépendance. */
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) return;  // rien à faire : le CSS laisse tout visible

  // Le drapeau est posé AVANT d'observer quoi que ce soit : tant qu'il n'est pas
  // là, le CSS n'a le droit de rien cacher. Si ce fichier ne se charge pas, la
  // page reste intégralement lisible — elle perd l'animation, pas le contenu.
  document.documentElement.classList.add("js-anim");
  var els = document.querySelectorAll(".reveal");
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
