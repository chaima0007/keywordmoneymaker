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

## Tâches
| Tâche | État | Preuve |
|---|---|---|
| Flotte d'agents + CLAUDE.md + ETAT.md | vérifié | commit sur main, push vérifié |
| Étape 0 — positionnement | vérifié | décision de Chaima 2026-07-17 : RegTech conformité PME |
| Étape 1 — refonte site (accueil, simulateur, offres, mentions légales, robots+sitemap) | fait — déploiement à vérifier | commit + Actions deploy |
| Étape 2 — brouillons marketing | vérifié | Drive doc 15 (vérifié par binôme juridique+QA) |
| Étape 3 — audit La Loi Avec Moi | BLOQUÉ session | accès dépôt refusé (add_repo indisponible) — à relancer, rien inventé |
| Angles morts | vérifié | Drive doc 16 (25 points, triés par urgence) |

## PASSATION (dernière en date en haut)
### 2026-09-06 (23h11 CEST) — Installation du PROTOCOLE CODEX (session Claude Code, branche + PR #5)
- Tâche : installer le PROTOCOLE CODEX — EMPIRE CHAIMA (version consolidée 2026-09-06) dans le projet.
- Ce que j'ai fait : bloc collé EN TÊTE de CLAUDE.md intégralement (83 → 417 lignes, les 83 lignes d'origine conservées à l'identique dessous, diff vérifié) ; §15.4 ajouté (dépôt, stack, commandes de vérification avant push, pièges datés) ; structure §12 créée (codex/candidates, expertise, opportunites, licences-sortantes, A-DECIDER.md, EVOLUTION.md, « 📋 JOURNAL.md », « 🔴 ERREURS.md ») ; snapshot §5 écrit ; A-DECIDER.md rempli avec les 6 décisions réelles en attente (5 à plus de 14 jours, mises en évidence).
- Fichiers touchés : CLAUDE.md, codex/*, « 📋 JOURNAL.md », « 🔴 ERREURS.md », .claude/skills/debat/README.md, ETAT.md. AUCUN fichier du site.
- Vérifié : diff des 83 lignes d'origine = 0 différence ; git status = aucun fichier du site modifié ; structure conforme au §12.
- NON VÉRIFIÉ / RESTE : les 21 agents du §12 ne sont PAS installés — .claude/agents/ contient 29 agents de l'ancienne flotte ; le §15.3 dit de les COPIER depuis un projet existant, ils n'ont pas été fournis, donc rien n'a été inventé. Écart signalé (§5.5), jamais corrigé seul (§10). Porté dans A-DECIDER.md. La skill .claude/skills/debat/ est marquée NON INSTALLÉE.
- Rappel : PR #3 (refonte premium du site) toujours OUVERTE depuis 27 jours, attend la revue visuelle de Chaima.
- Besoin du suivant : lire /codex/A-DECIDER.md EN PREMIER. Ne rien supprimer dans .claude/agents/ sans décision de Chaima.

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
