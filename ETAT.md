# ETAT.md — État du projet Caelum Partners (source de vérité locale)

> Règle : chaque agent lit ce fichier + la dernière passation AVANT d'agir, et écrit sa passation en finissant.
> Référence globale : dossier Drive « 🗂️ COMPILATION & SYNOPSIS — Empire Chaima » (docs 00-14).

## Décisions EN ATTENTE de Chaima (bloquantes pour certaines tâches)
- [x] **POSITIONNEMENT (Étape 0) : TRANCHÉ le 2026-07-17 par Chaima → RegTech conformité PME belges** (comparatif : doc 17 du Drive, scoring 6,75 vs 3,05). Le site est aligné sur cet angle.
- [ ] Prix des 3 offres (Essentiel / Sérénité / Sur-mesure).
- [ ] N° BCE / TVA / éditeur responsable (mentions légales).
- [ ] Déclaration C1/C1C ONEM → débloque Stripe.
- [ ] Création du compte Brevo (capture leads) + LEADS_WEBHOOK_URL.

## Décisions prises (datées)
- 2026-06-18 : domaine caelumpartners.agency rattaché à GitHub Pages (CNAME commité, deploy Actions vert).
- 2026-07-17 : DNS repointés parking Namecheap → GitHub Pages (A 185.199.108.153, www CNAME chaima0007.github.io), « DNS only », 525 résolu, site en HTTPS (autre session, doc 13). NE PAS réactiver le proxy Cloudflare tant que le certificat GitHub n'est pas confirmé stable.
- 2026-07-17 : flotte d'agents installée (.claude/agents/, 24 agents docs 08/09/12/14) + CLAUDE.md maître (doc 10) + ce fichier.
- 2026-07-17 : PROTOCOLE UNIVERSEL « DRIVE D'ABORD » adopté (doc 19 du Drive) : Drive lu avant toute action, critique des critiques (3 couches), journalisation datée+synopsis dans le dossier concerné. Intégré au §0 et §2 de CLAUDE.md.
- 2026-09-06 : PROTOCOLE CODEX installé (« protocole + structure d'abord ») — bloc CLAUDE.md + structure /codex + skill debat (PR #7). Agents non touchés (réconciliation en attente, voir /codex/A-DECIDER.md). TRANCHÉ PAR CHAIMA.

## Tâches
| Tâche | État | Preuve |
|---|---|---|
| Flotte d'agents + CLAUDE.md + ETAT.md | vérifié | commit sur main, push vérifié |
| Étape 0 — positionnement | vérifié | décision de Chaima 2026-07-17 : RegTech conformité PME |
| Étape 1 — refonte site (accueil, simulateur, offres, mentions légales, robots+sitemap) | fait — déploiement à vérifier | commit + Actions deploy |
| Étape 2 — brouillons marketing | vérifié | Drive doc 15 (vérifié par binôme juridique+QA) |
| Étape 3 — audit La Loi Avec Moi | BLOQUÉ session | accès dépôt refusé (add_repo indisponible) — à relancer, rien inventé |
| Angles morts | vérifié | Drive doc 16 (25 points, triés par urgence) |
| CompeteIQ — landing « en pause » (vérité rétablie) | vérifié | PR #2 mergée, commit 60c241c |

## PASSATION (dernière en date en haut)
### 2026-09-06 23h27 (Europe/Brussels) — Rétro-passation : clôture CompeteIQ + installation CODEX (session Claude Code CompeteIQ/TEST)
- Contexte : documenter la clôture CompeteIQ (non journalisée à l'époque dans ce fichier) + installer le CODEX. Remplace la PR #4 (basée sur un ETAT.md périmé, fermée).
- FAIT : (17-07) landing competeiq-landing.html passée en « en développement — non disponible » — noindex, prix → « Bientôt disponible », faux témoignages/ticker/métriques « Actif » supprimés, bandeau, CTA → mailto ; PR #2 mergée (60c241c). (06-09) CODEX installé (bloc CLAUDE.md + /codex + skill debat) via PR #7.
- VÉRIFIÉ (preuve) : PR #2 API {"merged":true} sha 60c241c ; PR #7 poussée (commit 0dbf613) ; ETAT.md/CLAUDE.md du main relus via API avant écriture (§5 état réel, pas de mémoire).
- NON VÉRIFIÉ : rendu de la page CompeteIQ déployée (proxy réseau 403 depuis le sandbox) ; à confirmer visuellement.
- RESTE : réconcilier les agents CODEX (21) vs flotte existante (29) — voir /codex/A-DECIDER.md ; merger PR #7 (CODEX) et cette PR après validation Chaima ; installer le CODEX sur chaima0007/test (priorité 2) ; décisions Chaima en attente (prix, BCE, ONEM, Brevo).
- Besoin du suivant : lire le bloc CODEX en tête de CLAUDE.md + /codex/A-DECIDER.md avant d'agir.

### 2026-09-06 21h30 (Europe/Brussels) — Le contrôle sécurité a trouvé et corrigé 3 CVE (session Claude Code)
- Boucle complète prouvée : le contrôle DÉTECTE → on CORRIGE → le contrôle CONFIRME.
- Défaut du run n°1 corrigé : pip-audit auditait l'environnement Ubuntu du runner (cloud-init, ufw, twisted…) au lieu du projet → cible désormais uv.lock (635 dépendances réelles).
- 3 vulnérabilités réelles trouvées puis corrigées dans le verrou : cryptography 49.0.0→50.0.1 (PYSEC-2026-3552) · mcp 1.28.0→1.29.1 (PYSEC-2026-3483) · pydantic-settings 2.14.1→2.15.0 (GHSA-4xgf-cpjx-pc3j).
- Vérifié : run n°3 du workflow « Sécurité du code » VERT, journal : « Dépendances auditées : 635 » puis « No known vulnerabilities found ». Commits 54cd359 (flotte) · bfe624f (correction cible) · b8cf719 (correction CVE).
- Reste : épingler par SHA les 4 actions de deploy.yml (SHA non récupérables depuis le sandbox — API GitHub bloquée pour actions/*) ; licences des dépendances non vérifiables ici (paquets non installés).

### 2026-09-06 21h24 (Europe/Brussels) — Flotte « code sûr » + contrôle automatique GitHub (session Claude Code)
- Tâche : agents pour trouver du code disponible et NON pollué + vérification multi-agents contre le risque de piratage (demande de Chaima).
- Fait : 5 agents ajoutés (.claude/agents/ : chercheur-code-libre, auditeur-licences, auditeur-chaine-approvisionnement, verificateur-code-tiers, contre-verificateur-securite → 29 au total) ; script `scripts/audit_code_sur.py` (5 contrôles : secrets, dépendances, actions CI, code à risque, licences) ; workflow `.github/workflows/securite-code.yml` (aucune action tierce, permissions lecture seule, + pip-audit) ; règle §2 bis dans CLAUDE.md.
- Vérifié : script exécuté sur le dépôt → VERT sur les contrôles bloquants ; DÉTECTION PROUVÉE par test piégé (faux secret + curl|bash + shell=True + exec distant → verdict ROUGE, puis VERT après nettoyage) ; workflow validé structurellement + zéro `uses:` (contrôle automatisé).
- Trouvé : 4 actions GitHub non épinglées par SHA dans deploy.yml (risque supply chain réel, signalé en avertissement). SHA réels NON récupérables depuis ce sandbox (API GitHub bloquée pour les dépôts actions/*) → aucun SHA inventé ; épinglage laissé à faire avec accès réseau.
- Reste : épingler les 4 actions de deploy.yml ; vérifier les licences des 3 dépendances (non installées ici, donc NON vérifiées).

### 2026-08-10 11h17 (Europe/Brussels) — Audit global + correction racine (session Claude Code)
- Tâche : re-vérification complète demandée par Chaima ; élimination des erreurs relevées par les audits Drive.
- CORRECTION D'AUDIT MAJEURE : la PR #2 est MERGÉE depuis le 17/07/2026 18h59 (API GitHub : state closed, merged true, merged_by chaima0007). Les journaux « boucle-caelum » (28/07→10/08) qui affirment « PR#2 NON mergée » se trompent : refs/pull/2/head persiste toujours après fusion. Aucun merge n'attend Chaima.
- ERREUR RÉELLE CORRIGÉE (E1) : la racine du site servait un placeholder noindex « Redirection en cours » → index.html contient désormais la vraie page d'accueil conformité (canonical /), caelum-index.html devient une redirection noindex vers /, ajout de 404.html.
- Vérifié : HTML parsé sans erreur ; disclaimer présent ; commit + push (voir git log) ; run Actions deploy à contrôler après push.
- Reste : vérification visuelle du live par Chaima (sandbox sans accès réseau au domaine).

### 2026-08-10 (11h14 CEST) — Refonte PREMIUM du design (session Claude Code, branche + PR)
- Tâche : élever le design des 4 pages (caelum-index, simulateur, offres, mentions-legales) au niveau premium, SANS toucher au contenu honnête ni à la logique du simulateur, CSP conservée.
- Ce que j'ai fait : système de design partagé (assets/caelum.css — Fraunces+Inter via Google Fonts, palette crème/or/bleu-nuit, cartes en relief, révélation au scroll) ; héros sombre & doré avec œuvre SVG originale (dôme céleste + constellation + arc de 12 étoiles = clin d'œil UE) ; icônes SVG cohérentes par obligation (Peppol/NIS2/RGPD/lanceurs d'alerte) ; JS externalisé (assets/caelum.js micro-interactions, assets/simulateur.js logique du simulateur DÉPLACÉE telle quelle) ; prefers-reduced-motion respecté ; 100% SVG inline (aucune photo stock).
- Fichiers touchés : caelum-index.html, simulateur.html, offres.html, mentions-legales.html, assets/caelum.css, assets/caelum.js, assets/simulateur.js.
- Vérifié (preuves) : logique du simulateur IDENTIQUE au caractère près (diff `var res=[]`→`var lib=` = 44 lignes, 0 diff) ; 4 HTML parsés sans balise orpheline (parseur Python) ; CSP durcie script-src 'self' + hôtes Google Fonts sur les 4 pages, 0 script inline ; assets présents ; chaînes honnêtes préservées (Prix à confirmer / Sur devis / BCE inscription en cours / disclaimers / sources) ; aucune image externe.
- Livré via : branche `design/caelum-premium-refonte` + PR #3 vers main (JAMAIS de push direct sur le site). Fusion = décision de Chaima.
- Limite honnête : le rendu visuel réel (chargement Google Fonts + responsive dans un navigateur) n'est PAS vérifiable depuis ce sandbox (sortie réseau restreinte) — RESTE : revue visuelle par Chaima avant fusion.
- Besoin du suivant : Chaima relit la PR #3, vérifie le rendu, fusionne si OK → déploiement GitHub Pages automatique.
### 2026-09-11 20h45 (Europe/Brussels) — Identité de marque Caelum + licences des polices (session Claude Code)
- Tâche : combler les deux derniers trous relevés à l'état des lieux — aucun logo/favicon/og:image sur le site, aucune licence de police documentée (manquement CLAUDE.md §2 bis).
- Ce que j'ai fait : marque « entonnoir » (3 barres décroissantes centrées, indigo #4338CA, direction C « Le Signal ») ; favicon.svg + favicon-32.png + apple-touch-icon.png (180, plein bord et opaque : iOS compose la transparence sur du noir) ; og-caelum.png 1200×630 composée avec les vraies Fraunces et Inter, texte repris MOT POUR MOT du site (titre = simulateur.html:44, sous-titre = og:description d'index.html) ; câblage sur les 6 pages réelles, og:image sur les 4 pages FR seulement (/nl/ exclue, l'image est en français) ; deploy.yml liste blanche étendue ; fiche codex/candidates/C-01 (Fraunces + Inter = SIL OFL 1.1, lu à la source).
- Fichiers touchés : products/caelum/site/{favicon.svg,favicon-32.png,apple-touch-icon.png,index.html,simulateur.html,offres.html,mentions-legales.html,404.html,nl/index.html,assets/marque.svg,assets/og-caelum.png}, .github/workflows/deploy.yml, codex/candidates/C-01-polices-fraunces-inter.md + README, shared/attribution.py, .gitignore, products/kmm/{agents/protocole.py,agents/drive_audit.py,audit_drive/README.md}.
- Vérifié (preuve) : simulateur.js et caelum.css → git diff VIDE ; diff HTML ne contient que icon/og:image ; build de déploiement rejoué en local (24 fichiers, les 5 nouveaux présents, 3 garde-fous PASSE, 4/4 chemins résolvent) ; audit_cloisonnement.py --bloquant → exit 0, tous verts ; audit_code_sur.py → VERT sur les bloquants ; push fast-forward 7d36555..52ee273, AUCUN force.
- Deux défauts trouvés et corrigés : la marque alignée à gauche se lisait « F » (recentrée) ; Fraunces à opsz=144 fait disparaître la traverse du « e », « concerné » se lisait « conccrné » (ramené à opsz=40/wght=600).
- Récupération : la branche avait divergé le 2026-07-17 et portait 2 commits JAMAIS fusionnés (protocole.py, drive_audit.py). Conservés, pas écrasés. Rangés dans products/kmm/agents/ à côté de leur unique consommateur commandant.py (git les plaçait dans shared/, l'import aurait été cassé). Imports vérifiés à l'exécution.
- CORRECTION : j'avais affirmé que Fraunces était appelée en 600/700 sans être chargée. VÉRIFIÉ RÈGLE PAR RÈGLE : c'était FAUX, il n'y a pas de bug — toutes les graisses 600/700 sont de l'Inter, chargée en 400;500;600;700. CSS non touché. Le besoin réel viendra avec « Le Signal », qui exigera d'AJOUTER Fraunces 600/700.
- Limite honnête : je n'ai PAS vu le site rendu. Le proxy de sortie bloque caelumpartners.agency — ma preuve est le listing du build, jamais un HTTP 200.
- Reste / risques : PR #19 en attente de fusion (décision de Chaima) ; point RGPD des polices OUVERT et non tranché (servies par fonts.gstatic.com → IP du visiteur chez Google ; ce n'est PAS un défaut de licence ; remède = auto-hébergement, autorisé par l'OFL) ; la refonte « Le Signal » n'est pas faite, le corps du site est toujours en « Le Greffe ».
- Besoin du suivant : Chaima relit et fusionne la PR #19, confirme le rendu réel, tranche le point RGPD des polices et rend son verdict sur le spécimen « Le Signal ».

### 2026-07-17 21h44 (Europe/Brussels) — Protocole de livraison v2 (session Claude Code)
- Tâche : intégrer le protocole de livraison obligatoire dicté par Chaima (date/heure Europe/Brussels partout, synopsis en tête, titre « AAAA-MM-JJ-HHhMM — [auteur] — [sujet] », audit FAIT/VÉRIFIÉ avec preuve/RESTE, copie Drive COMPILATION ou reports/ en secours, passation à jour, ajout jamais d'écrasement).
- Fichiers touchés : CLAUDE.md (§0.3 réécrit), ETAT.md.
- Vérifié : commit + push (voir git log) ; amendement déposé dans le Drive (doc « 2026-07-17-21h44 — Claude Code — Protocole de livraison v2 »), read-back effectué.
- Reste : les autres dépôts qui utilisent 00-LIRE-D-ABORD.md (hors de portée de cette session) doivent recopier ce bloc — signalé dans le doc Drive.
- Besoin du suivant : appliquer ce protocole à CHAQUE livraison, sans exception.

### 2026-07-17 (2) — Refonte Étape 1 (session Claude Code, décision Étape 0 obtenue)
- Tâche : refonte du site sur le positionnement RegTech conformité PME (décision de Chaima du jour).
- Ce que j'ai fait : caelum-index.html réécrit (accueil conformité : 4 obligations vérifiées doc 06 + démystification CSRD/DORA + bloc transparence sans chiffre inventé) ; simulateur.html créé (4 questions → logique réelle par obligation, résultat oui/à vérifier/non, capture par e-mail volontaire avec consentement, AUCUNE donnée transmise automatiquement) ; offres.html créé (3 niveaux, prix « à confirmer », aucun paiement possible) ; mentions-legales.html créé (éditeur/BCE « à compléter » en toute transparence, politique RGPD, cookies : aucun traceur) ; robots.txt + sitemap.xml.
- Fichiers touchés : caelum-index.html, simulateur.html, offres.html, mentions-legales.html, robots.txt, sitemap.xml, ETAT.md.
- Vérifié : grep gardien (zéro « 9 agents »/« élite »/témoignage inventé ; CSRD toujours accompagnée de l'Omnibus ; disclaimer sur les 4 pages ; zéro traceur) ; HTML parsé sans erreur ; push + run GitHub Actions deploy à contrôler après push.
- Limite honnête : le chargement du site en production (code 200 + cadenas) n'est PAS vérifiable depuis ce sandbox (politique réseau) — à confirmer par Chaima ou une session avec accès réseau. Le proxy Cloudflare reste désactivé (DNS only) conformément au doc 13.
- Besoin du suivant : quand BCE/TVA existent → compléter mentions-legales.html ; quand Brevo existe → brancher la capture (remplacer le mailto par le formulaire) ; prix → remplir offres.html.

### 2026-07-17 — Installation de la flotte (session Claude Code)
- Tâche : installer la flotte complète (doc 14) + prompt maître (doc 10) + ETAT.md.
- Ce que j'ai fait : 24 fichiers .claude/agents/*.md (charte commune embarquée), CLAUDE.md, ETAT.md.
- Fichiers touchés : .claude/agents/*, CLAUDE.md, ETAT.md.
- Vérifié : commit + push sur main (voir git log).
- Ce qui reste / risques : refonte gelée tant que le positionnement n'est pas tranché ; site actuel affiche encore « agence IA / 9 agents ».
- Besoin du suivant : lire la décision de Chaima sur le positionnement dans ce fichier avant toute refonte.
