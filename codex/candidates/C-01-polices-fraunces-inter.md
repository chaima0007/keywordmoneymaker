# C-01 — Polices Fraunces & Inter

**SYNOPSIS** — Les deux polices du site de Caelum Partners étaient utilisées depuis la refonte
sans qu'aucune licence ne soit documentée dans le dépôt (manquement au CLAUDE.md §2 bis).
Licences vérifiées à la source le 2026-09-11 : les deux sont sous **SIL Open Font License 1.1**,
qui autorise l'usage commercial, l'incorporation et la diffusion. Statut : **INTÉGRÉ**.
Un point RGPD réel reste ouvert (chargement depuis les serveurs de Google) — voir l'objection.

| | |
|---|---|
| **ID** | C-01 |
| **Statut** | **INTÉGRÉ** (les deux polices sont déjà en production) |
| **Date** | 2026-09-11 |

---

## Besoin couvert

Contraste typographique entre les titres et le texte courant (Fraunces, serif à contraste
variable) et lisibilité du corps de texte à l'écran (Inter, sans-serif à grande hauteur d'x).
Choix arrêté à la refonte et reconduit pour la direction C « Le Signal ».

## Source (identité canonique)

| Police | Dépôt d'origine | Miroir Google Fonts |
|---|---|---|
| Fraunces | `github.com/undercasetype/Fraunces` | `github.com/google/fonts` → `ofl/fraunces/` |
| Inter | `github.com/rsms/inter` | `github.com/google/fonts` → `ofl/inter/` |

Servies au visiteur depuis `fonts.googleapis.com` / `fonts.gstatic.com`.
**Aucun fichier de police n'est versionné dans ce dépôt.**

## Licence — verdict Guardian-Licences : **VÉRIFIÉ**

Les deux sont sous **SIL Open Font License, Version 1.1**. Texte lu à la source, pas déduit
d'une page de catalogue.

- `ofl/fraunces/OFL.txt` → « Copyright 2018 The Fraunces Project Authors
  (https://github.com/undercasetype/Fraunces) — This Font Software is licensed under the
  SIL Open Font License, Version 1.1. » *(consulté le 2026-09-11)*
- `ofl/inter/OFL.txt` → « Copyright 2020 The Inter Project Authors
  (https://github.com/rsms/inter) — This Font Software is licensed under the
  SIL Open Font License, Version 1.1. » *(consulté le 2026-09-11)*
- Également vérifié dans les dépôts d'origine : `undercasetype/Fraunces/OFL.txt`
  et `rsms/inter/LICENSE.txt`.

**Ce que l'OFL 1.1 autorise ici** : usage commercial, incorporation dans un produit,
redistribution. Clause décisive, citée : *« The requirement for fonts to remain under this
license does not apply to any document created using the fonts. »* — les visuels produits
avec ces polices (image de partage, favicon) ne sont donc **pas** contaminés par l'OFL.

**Ce que l'OFL 1.1 interdit** : vendre les fichiers de police seuls ; réserver le nom de la
police pour une version modifiée. Aucun des deux ne nous concerne : nous ne modifions ni ne
redistribuons les fichiers.

**Verdict : licence permissive, compatible avec un produit fermé. Pas de copyleft logiciel.**

## Sécurité — verdict Sentinel-Sécurité

Aucune exécution : une police n'embarque pas de script. Pas de chaîne de dépendances, pas de
script post-installation, pas de Zone 1 applicable (aucun binaire n'est installé dans le projet).

Fichiers téléchargés **au moment de la fabrication seulement** (génération de l'image de
partage), depuis `raw.githubusercontent.com/google/fonts`, non versionnés, empreintes relevées :

    177ff6c0f14e5550a3c624247cd1189611d4eb65d000b14944c63d967958abbb  Fraunces[SOFT,WONK,opsz,wght].ttf
    29160a80ff49ddcab2c97711247e08b1fab27a484a329ce8b813d820dc559031  Inter[opsz,wght].ttf

## Objection Contradicteur — **le vrai point ouvert**

Charger les polices depuis `fonts.gstatic.com` transmet l'**adresse IP du visiteur à Google**
à chaque affichage de page, sans consentement préalable. Ce point a déjà été jugé en Europe
(tribunal régional de Munich I, 20 janvier 2022, réf. 3 O 17493/20 — **NON VÉRIFIÉ** : je cite
cette décision de mémoire, je n'ai pas ouvert le jugement ; à confirmer avant toute
communication publique). Deux remèdes existent : héberger les fichiers sur notre propre
domaine (l'OFL l'autorise explicitement), ou renoncer aux polices web.

Ce n'est **pas** un défaut de licence, c'est un défaut de traitement de données. Il relève de
`gardien-donnees` et de `rgpd-securite`, pas de cette fiche. **Il n'est pas résolu à ce jour.**

## Argument Avocat

Le remède est connu, peu coûteux et entièrement de notre côté (auto-hébergement des deux
fichiers dans `assets/`, déjà autorisé par la licence). Rien n'oblige à changer de police :
le problème est *où* elles sont servies, pas *lesquelles*.

## Ce qui changerait le verdict

Une modification de la licence en amont (elle est irrévocable pour les versions déjà publiées
sous OFL, donc peu probable), ou la décision d'auto-héberger — qui ferait entrer les fichiers
dans le dépôt et rendrait alors l'attribution du copyright obligatoire à côté d'eux.

---

    DE : superviseur-vigie / guardian-licences      POUR : CHAIMA
    OBJET : Documenter l'auto-hébergement des polices comme décision à trancher (RGPD, pas licence).
    VERDICT : VÉRIFIÉ — SIL OFL 1.1 pour Fraunces et Inter, usage commercial autorisé.
    PARCE QUE : ofl/fraunces/OFL.txt et ofl/inter/OFL.txt, lus à la source le 2026-09-11.
    NON VÉRIFIÉ : la référence exacte du jugement de Munich I (citée de mémoire, non ouverte).
    CE QUI CHANGERAIT MON AVIS : la décision d'auto-héberger les fichiers — l'attribution
    du copyright deviendrait alors obligatoire dans le dépôt, à côté des .ttf.
