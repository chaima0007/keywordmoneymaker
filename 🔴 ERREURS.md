# 🔴 ERREURS — ce qui a réellement cassé, et ce qu'on en a appris

> Une entrée = une erreur réelle, datée. Pas de « risque théorique » ici : ceux-là vont en
> A-DECIDER ou en fiche expertise. On écrit les erreurs pour ne pas les repayer.

## 2026-09-06 — Un audit de dépendances qui regardait la mauvaise cible
`pip-audit` lancé sans cible explicite a analysé les paquets préinstallés du serveur d'intégration
(cloud-init, ufw, twisted…) au lieu des dépendances du projet : des vulnérabilités réelles mais hors
sujet. Un contrôle vert qui ne regarde pas la bonne cible reste un contrôle faux.
**Correction :** audit pointé sur le verrou du projet → 635 dépendances réelles, 3 vulnérabilités
effectives trouvées et corrigées. **Leçon :** fiche EXP-002.

## 2026-08-10 — « PR #2 non mergée » affirmé pendant trois semaines
Des journaux automatiques déduisaient qu'une PR était ouverte de la seule présence de
`refs/pull/2/head` — or cette référence **persiste après la fusion**. La PR était fusionnée depuis le
17/07. Conséquence : un « verrou qui attendait Chaima » qui n'existait plus.
**Correction :** vérifier `merged: true` via l'API, jamais la seule présence d'une référence.
**Leçon :** une déduction n'est pas une observation ; le §13 impose VÉRIFIÉ + source, pas PLAUSIBLE.

## 2026-08-10 — La racine du site servait un placeholder
`index.html` contenait une redirection `noindex` « Redirection en cours » : le site refondu existait
mais n'était pas servi à l'adresse principale.
**Correction :** la vraie page d'accueil est passée à la racine, redirection inversée, page 404 ajoutée.
**Leçon :** « déployé » ne veut pas dire « visible » — vérifier ce que sert réellement l'URL publique.
