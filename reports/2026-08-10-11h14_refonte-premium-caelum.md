# 2026-08-10-11h14 — Claude Code (design) — Refonte premium du site Caelum (PR #3)

## SYNOPSIS
Refonte **purement visuelle** des 4 pages du site Caelum (accueil, simulateur, offres, mentions légales) au niveau premium (Fraunces + Inter, héros sombre & doré, œuvre SVG originale, icônes cohérentes, micro-interactions). **Contenu honnête et logique du simulateur inchangés** ; CSP conservée et durcie. Livré sur une **branche + PR #3** (aucun push direct sur le site). **État : construit et vérifié techniquement ; reste la revue visuelle humaine avant fusion.**

---

## FAIT
- **Système de design partagé** `assets/caelum.css` : typographie Fraunces (titres) + Inter (texte) via Google Fonts ; palette raffinée crème / or / bleu-nuit dérivée de l'existante ; cartes en relief (ombres + filet doré) ; états hover ; classes de révélation au défilement.
- **Héros sombre & doré** avec **œuvre SVG originale** : dôme céleste (arcs concentriques — « Caelum » = le ciel), constellation reliée, et arc de 12 étoiles dorées évoquant le cadre européen. Dégradés et halo, 100 % vectoriel.
- **Icônes SVG cohérentes** (même style de trait) par obligation : e-facturation Peppol, NIS2, RGPD, lanceurs d'alerte.
- **Micro-interactions** : hover cartes/CTA, révélation au scroll via `IntersectionObserver` (fichier externe `assets/caelum.js`), **`prefers-reduced-motion` respecté** (tout s'affiche sans animation si l'utilisateur le demande).
- **JS externalisé** pour respecter la CSP `script-src 'self'` : `assets/caelum.js` (interactions) et `assets/simulateur.js` (logique du simulateur **déplacée telle quelle**, aucune modification de logique).
- **Aucune photo stock ni faux client** : tous les visuels sont des SVG inline sur-mesure.
- **Livraison** : branche `design/caelum-premium-refonte`, **PR #3** vers `main` — https://github.com/chaima0007/keywordmoneymaker/pull/3

## VÉRIFIÉ (avec preuve)
- ✅ **Logique du simulateur identique au caractère près** — commande : `diff` de la zone `var res = [];` → `var lib =` entre l'original (`origin/main:simulateur.html`) et `assets/simulateur.js` → **44 lignes, 0 différence**.
- ✅ **Les 4 fichiers HTML parsent** sans balise orpheline — parseur Python (`html.parser`), pile finale vide sur les 4.
- ✅ **CSP correcte et durcie** sur les 4 pages : `script-src 'self'` (plus aucun inline), + `fonts.googleapis.com` (style-src) et `fonts.gstatic.com` (font-src). **0 `<script>` inline** dans les 4 fichiers.
- ✅ **Assets présents** : `assets/caelum.css`, `assets/caelum.js`, `assets/simulateur.js`.
- ✅ **Contenu honnête préservé** — grep des chaînes critiques : « Prix à confirmer », « Sur devis », « en cours de finalisation », « inscription en cours » (BCE), « n'est pas un cabinet d'avocats », démystification CSRD, « tout se calcule dans votre navigateur ». Toutes présentes.
- ✅ **Aucune image externe / photo stock** — grep `<img src="http...">` = 0.

## RESTE (honnête)
- ⚠️ **Revue visuelle humaine** dans un navigateur (rendu réel des Google Fonts + responsive mobile/desktop) : **non réalisable depuis cet environnement** (sortie réseau restreinte — l'accès aux domaines externes renvoie un blocage `host_not_allowed` du pare-feu du sandbox, ce n'est pas un défaut du site). → À faire par Chaima sur la préversion de la PR avant fusion.
- ⏳ **Fusion de la PR #3** = décision de Chaima. La fusion sur `main` déclenche le déploiement GitHub Pages.
- ℹ️ Hors périmètre (inchangé) : prix réels, BCE/TVA, branchement Brevo — restent « à compléter » comme avant.

## SÉCURITÉ
Aucun secret dans le code. CSP maintenue et resserrée (script-src 'self'). Aucune donnée envoyée par le simulateur (calcul navigateur). Aucun traceur ajouté.
