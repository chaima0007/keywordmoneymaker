# 2026-09-11-20h45 — Claude Code — Identité de marque Caelum (marque, favicons, image de partage) + licences des polices

**SYNOPSIS** — Le site de Caelum Partners n'avait ni favicon, ni icône iOS, ni image de partage : un lien posté sur LinkedIn s'affichait sans visuel. Les licences des deux polices n'étaient documentées nulle part, en manquement au CLAUDE.md §2 bis. Les deux trous sont comblés dans la PR #19, qui ne modifie **aucun texte, aucun prix, aucun disclaimer, aucune ligne du simulateur**. État : livré, CI corrigée, **en attente de fusion par Chaima**.

Heure de référence : `TZ="Europe/Brussels" date` → **2026-09-11 20h45**.

---

## FAIT

### La marque
Trois barres décroissantes **centrées**, sur cartouche indigo `#4338CA` — direction C « Le Signal », confirmée par Chaima. La forme dit ce que fait le produit : un entonnoir, du corpus réglementaire vers ce qui concerne réellement l'entreprise. Rien de céleste, rien de mystique.

| Fichier | Usage |
|---|---|
| `products/caelum/site/assets/marque.svg` | la marque, vectorielle |
| `products/caelum/site/favicon.svg` | onglet, navigateurs modernes |
| `products/caelum/site/favicon-32.png` | onglet, repli |
| `products/caelum/site/apple-touch-icon.png` | écran d'accueil iOS, 180 px |
| `products/caelum/site/assets/og-caelum.png` | image de partage, 1200×630 |

### L'image de partage — zéro texte inventé
- Titre « Suis-je concerné ? » = le nom exact du simulateur (`simulateur.html:44`).
- Sous-titre = la `og:description` d'`index.html`, mot pour mot.
- Composée avec les **vraies** Fraunces et Inter.

### Câblage
Icônes sur les 6 pages réelles ; `og:image` sur les 4 pages françaises seulement (`/nl/` ne la reçoit pas : l'image est en français). Stubs de redirection laissés intacts. `deploy.yml` : les 3 fichiers de racine ajoutés à la liste blanche.

### Licences des polices — `codex/candidates/C-01`
Fraunces et Inter sont sous **SIL Open Font License 1.1**, texte lu à la source le 2026-09-11.

### Récupération de la flotte de juillet
La branche avait divergé le 2026-07-17 et portait 2 commits jamais fusionnés (`protocole.py`, `drive_audit.py`). **Conservés**, pas écrasés : push en fast-forward, aucun force.

---

## VÉRIFIÉ (exécuté, avec preuve)

| Contrôle | Preuve | Résultat |
|---|---|---|
| `assets/simulateur.js` intact | `git diff --stat origin/main..HEAD` | sortie vide |
| `assets/caelum.css` intact | idem | sortie vide |
| Aucun texte visible modifié | diff HTML filtré hors `icon`/`og:image` | sortie vide |
| Build de déploiement | liste blanche rejouée en local | 24 fichiers, les 5 nouveaux présents |
| Garde-fous 1, 2, 3 du deploy | rejoués en local | PASSE, PASSE, PASSE |
| Chemins référencés | résolution dans `_site` | 4/4 OK |
| CSP | `img-src 'self' data:` | tout auto-hébergé, rien à changer |
| Import de la flotte de juillet | `import drive_audit` + `from protocole import with_protocole` exécutés | OK |
| `audit_cloisonnement.py --bloquant` | rejoué en local | C1 C2 C3 C4 + RATTACHEMENT verts, exit 0 |
| `audit_code_sur.py` | rejoué en local | VERT sur les contrôles bloquants |
| Push | `7d36555..52ee273` | fast-forward, aucun force |

### Deux défauts trouvés et corrigés en cours de route
1. **La marque se lisait « F »** — barres alignées à gauche, mauvaise initiale. Corrigée en centré.
2. **« concerné » se lisait « conccrné »** — Fraunces à `opsz=144` amincit la traverse du « e » jusqu'à la faire disparaître. Ramené à `opsz=40`, `wght=600`.

### Une CI rouge, diagnostiquée et réparée
Le contrôle « Sécurité du code » a échoué sur 2 points, **tous deux dus au travail de juillet récupéré, aucun aux visuels** : `audit_drive/` à la racine, et les 2 modules absents de la table d'attribution. Réparé en rangeant le dossier là où le code écrit réellement (`products/kmm/audit_drive/`) et en déclarant les modules sur preuve d'imports. Les deux contrôles rejoués en local avant le second push.

---

## RESTE

- **Je n'ai pas vu le site rendu.** Le proxy de sortie bloque `caelumpartners.agency` : ma preuve est le listing du build, jamais un HTTP 200. À confirmer par Chaima après fusion.
- **PR #19 en attente de fusion** — décision de Chaima (CLAUDE.md §10).
- **Point RGPD des polices, OUVERT et non tranché** : servies par `fonts.gstatic.com`, donc l'IP de chaque visiteur part chez Google sans consentement. Ce n'est **pas** un défaut de licence. Remède connu et de notre côté : auto-héberger les deux fichiers, l'OFL l'autorise. Consigné comme objection du Contradicteur dans C-01.
- **La refonte « Le Signal » n'est pas faite** : le corps du site est toujours en « Le Greffe ». Cette PR pose l'identité, pas la mise en page.

## CORRECTION D'UNE DE MES AFFIRMATIONS

J'avais affirmé que le CSS appelait Fraunces en 600/700 alors que seules 400 et 500 sont chargées, et Chaima m'a demandé de corriger ce bug. **Vérification règle par règle : c'était faux, il n'y a pas de bug.** Toutes les graisses 600/700 du CSS appartiennent à Inter, chargée en 400;500;600;700. Fraunces n'est jamais appelée en 600/700. Rien à corriger, CSS non touché. Le besoin réel existe pour la suite : le contraste typographique de « Le Signal » exigera d'**ajouter** Fraunces 600/700 au chargement — ce sera dans la PR de refonte.

## DÉPEND DE CHAIMA

1. Fusionner ou non la PR #19.
2. Trancher le point RGPD des polices (auto-hébergement ou statu quo).
3. Son verdict sur le spécimen « Le Signal », toujours en attente.
