# ETAT.md — État du projet Caelum Partners (source de vérité locale)

> Règle : chaque agent lit ce fichier + la dernière passation AVANT d'agir, et écrit sa passation en finissant.
> Référence globale : dossier Drive « 🗂️ COMPILATION & SYNOPSIS — Empire Chaima » (docs 00-14).

## Décisions EN ATTENTE de Chaima (bloquantes pour certaines tâches)
- [ ] **POSITIONNEMENT (Étape 0 — BLOQUANT refonte)** : agence d'automatisation IA **ou** RegTech conformité PME ? → question posée le 2026-07-17.
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
| Étape 0 — question positionnement à Chaima | en cours | posée le 2026-07-17 |
| Étape 1 — refonte site (contenu, simulateur, /offres, légal) | à faire — BLOQUÉE par Étape 0 | — |
| Étape 2 — brouillons marketing (plan 90j, LinkedIn, SEO, Brevo, ITAA) | en cours | brouillons dans le Drive (doc 15) |
| Étape 3 — audit La Loi Avec Moi (droit-citoyen-app, GELÉ, vérification seule) | en cours | rapport dans le Drive |
| Angles morts | en cours | rapport dans le Drive |

## PASSATION (dernière en date en haut)
### 2026-07-17 — Installation de la flotte (session Claude Code)
- Tâche : installer la flotte complète (doc 14) + prompt maître (doc 10) + ETAT.md.
- Ce que j'ai fait : 24 fichiers .claude/agents/*.md (charte commune embarquée), CLAUDE.md, ETAT.md.
- Fichiers touchés : .claude/agents/*, CLAUDE.md, ETAT.md.
- Vérifié : commit + push sur main (voir git log).
- Ce qui reste / risques : refonte gelée tant que le positionnement n'est pas tranché ; site actuel affiche encore « agence IA / 9 agents ».
- Besoin du suivant : lire la décision de Chaima sur le positionnement dans ce fichier avant toute refonte.
