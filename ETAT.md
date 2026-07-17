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
