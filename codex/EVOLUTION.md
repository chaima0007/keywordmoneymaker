# /codex/EVOLUTION.md — APPEND-ONLY (CODEX §6.5)

> Une section par projet. UNIQUEMENT les événements significatifs (jalon, décision prise, lancement,
> problème résolu). Jamais « rien de neuf » — ça, c'est 📋 JOURNAL.md. On ajoute, on n'écrase jamais.

## Caelum Partners (dépôt keywordmoneymaker)
- 2026-06-18 — Domaine caelumpartners.agency rattaché à GitHub Pages (deploy Actions vert).
- 2026-07-17 — Positionnement tranché : RegTech conformité PME belges. Site refondu sur cet angle (accueil, simulateur, offres, mentions légales).
- 2026-07-17 — CompeteIQ (page hébergée dans ce dépôt) passée en « en développement — non disponible » (noindex, prix retirés, fausses preuves purgées) ; PR #2 mergée (60c241c).
- 2026-08-10 — Racine du site corrigée : index.html devient la vraie page d'accueil conformité (avant : placeholder noindex) ; ajout 404.html.
- 2026-09-06 — Flotte « code sûr » + workflow CI securite-code.yml ajoutés ; le contrôle a détecté puis corrigé 3 CVE réelles (cryptography, mcp, pydantic-settings). Boucle détection→correction→confirmation prouvée.
- 2026-09-06 — PROTOCOLE CODEX installé (bloc CLAUDE.md + structure /codex + skill debat). Agents non touchés (décision « protocole d'abord »).
- 2026-09-11 — Réconciliation des agents (« mapper + compléter, sans suppression ») : 13 rôles CODEX ajoutés (récupérés de la PR #6, auditée propre), 8 mappés aux agents existants, 0 suppression → 42 agents + table /codex/agents-correspondance.md.
- 2026-09-11 — **Identité de marque livrée et déployée** : marque « entonnoir » indigo #4338CA, favicon, icône iOS, image de partage 1200×630. Fusion `7163653`, déploiement en succès, les 5 fichiers lus dans l'archive publiée. Un lien Caelum partagé sur LinkedIn n'apparaît plus sans visuel.
- 2026-09-14 — **Fuite RGPD fermée** : Fraunces et Inter auto-hébergées (`b7082f4`), zéro appel externe, garde-fou en liste blanche au déploiement. Exécuté par une autre session sans passer par la file de décision — consigné comme tel, non attribué à Chaima.
- 2026-09-14 — **Quatre erreurs juridiques trouvées sur le site** par le premier contrôle quotidien des sources, recoupées en français, en néerlandais et au niveau européen : exception anti-blanchiment omise (rassurait à tort), seuils CSRD présentés comme alternatifs, règle du montant le plus élevé omise pour le RGPD puis pour NIS2. Corrigées en PR #23.
- 2026-09-14 — **Défaut d'affichage majeur découvert et corrigé** : `.reveal{opacity:0}` rendait 17 blocs sur 17 invisibles sans JavaScript, dont l'unique appel à l'action de la page d'accueil. Introduit par `312777f` en juillet, donc en production depuis. L'état au repos est désormais visible.
- 2026-09-14 — **Le dispositif d'agents a prouvé sa valeur** : gardien-juridique et contradicteur ont bloqué trois corrections successives, à chaque fois à raison — formulation plus étroite que l'article cité, brochure corrigée et produit laissé faux, garde-fou aveugle à la faute qu'il devait empêcher. Fiches E-27 et E-28.
- 2026-09-16 — **Carte vivante créée** (`codex/CARTE.md`), absente depuis l'installation du CODEX le 06/09.
