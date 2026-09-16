# 📋 JOURNAL.md — snapshots d'entrée de session (CODEX §5)

> Rituel d'entrée : état réel vérifié (jamais de mémoire), comparé au dernier snapshot.
> Rien n'a changé → une seule ligne « SNAPSHOT [date] : aucun changement ». Un changement → entrée datée et précise.
> Un rapport pour dire qu'il n'y a rien à dire est une faute contre le protocole. Le plus récent en haut.

## SNAPSHOT 2026-09-16 16h10 (Europe/Brussels) — pourquoi rien n'a changé, et ce que le journal avait manqué

- **État réel vérifié, pas de mémoire** : `main` = `4f206cf`, **inchangé depuis le 14/09 à 22h**.
  56 agents · 36 modules Python · 28 fiches d'erreurs · 3 rapports déposés · 11 décisions en attente.
- **LA RÉPONSE À « pourquoi rien n'a changé »** : quatre PR ouvertes, toutes vertes, toutes
  fusionnables, **aucune fusionnée** — #18 (i-DEPOT), #22 (refonte « Le Signal »), #23 (corrections
  juridiques), #24 (contenu visible sans JavaScript). Le travail existe et il est vérifié ; il n'est
  pas en production parce que la fusion est une décision humaine (§10) et que Chaima a conditionné
  celle-ci à l'accord préalable des agents. Le site en ligne porte donc encore le design rejeté ET
  les quatre imprécisions juridiques trouvées le 14/09.
- **Écart de rituel constaté, et il est à moi** : le dernier snapshot datait du 14/09 à 18h30 —
  écrit **avant** tout le travail de cette soirée-là. Les quatre erreurs juridiques, la refonte
  codée, les quatre passages d'agents, le garde-fou et sa réécriture : **rien n'était au journal**.
  Deux jours sans snapshot alors que le §5 en impose un par session.
- **Deux motifs d'erreur jamais consignés, ajoutés** : **E-27** (la brochure corrigée et le produit
  laissé faux) et **E-28** (un garde-fou aveugle à la faute exacte qu'il devait empêcher). Tous deux
  survenus le 14/09 au soir, tous deux trouvés par le contradicteur, aucun n'avait de fiche.
- **Carte vivante créée** : `codex/CARTE.md`. Le CODEX §1 la confie au cartographe depuis le 06/09 ;
  elle n'avait jamais existé. Elle répond à une question et une seule — où en est-on réellement, et
  qu'est-ce qui bloque — et dit quel fait va dans quel fichier, parce que l'erreur la plus fréquente
  est d'écrire au bon sujet dans le mauvais endroit.
- **Audit de cohérence (§5.5)** : CLAUDE.md porte le CODEX ✅ · structure §12 conforme, 11 éléments
  sur 11 ✅ · registre d'erreurs et son index concordants (28 fiches, contrôle vert) ✅ ·
  `codex/EVOLUTION.md` était resté au 11/09 alors que trois jalons avaient eu lieu depuis ⚠️ **corrigé** ·
  `codex/A-DECIDER.md` ne mentionnait aucune des quatre PR en attente ⚠️ **corrigé**.
- **Ce qui reste NON VÉRIFIÉ** : le rendu du site en production (fiche E-21, invérifiable d'ici) ;
  le montant exact des sanctions NIS2 en droit belge ; la partie II de l'annexe de la directive
  (UE) 2019/1937 ; les seuils chiffrés de la loi belge du 02/12/2024.

## SNAPSHOT 2026-09-14 18h30 (Europe/Brussels) — audit des ordonnanceurs
- **Écart de rituel constaté** : aucun snapshot entre le 2026-09-06 et aujourd'hui, soit **8 jours**,
  alors que le §5 en impose un par session. Les sessions ont tourné ; le journal n'a pas suivi.
- État réel vérifié (pas de mémoire) : `main` = 7163653 puis 0f0bb86 · 56 agents · 23 fiches d'erreurs ·
  registre `🔴 ERREURS.md` généré et vérifié en CI · cloisonnement bloquant vert · publication 19 fichiers.
- **Cause trouvée du bruit des 72 dernières heures** : les Routines n'étaient inventoriées nulle part.
  10 actives, ~60 réveils/jour, deux programmées à la même minute (les deux seules en « EN ATTENTE »).
  Une vingtaine de documents Drive en 3 jours, dont au moins 8 disant « INCHANGÉ · 0 pièce · SILENCE ».
- **Corrigé** : 3 cadences ajustées (~60 → ~20 réveils/jour), prompt périmé de la chaîne veille réécrit,
  `codex/ROUTINES.md` créé comme registre. Fiche **E-23** ajoutée : une condition d'arrêt écrite pour les
  agents ne peut pas arrêter l'horloge qui les réveille.
- Audit de cohérence (§5.5) : CLAUDE.md porte le CODEX ✅ · structure /codex conforme §12 ✅ ·
  A-DECIDER remis à jour (il datait du 11/09) ✅ · 5 Routines restent sans condition d'arrêt déclarée ⚠️.

## SNAPSHOT 2026-09-06 23h24 (Europe/Brussels) — installation CODEX
- État réel vérifié via l'API GitHub (main = b3dd3b2), pas de mémoire.
- Changements depuis la dernière session connue (juillet) : d'autres sessions ont poussé (10-08 racine + 404 ; 06-09 flotte « code sûr » + workflow CI + correction de 3 CVE).
- Constat anti-doublon (§9) : 29 agents déjà présents dans .claude/agents/, câblés à la CI → les 21 agents CODEX NON créés (décision Chaima « protocole d'abord »).
- Action de cette session : installation du bloc CODEX + structure /codex + skill debat (cette entrée). PR ouverte, non mergée.
- Audit de cohérence (§5.5) : CLAUDE.md porte désormais le CODEX en tête ✅ ; structure /codex conforme §12 ✅ ; agents = écart connu et consigné (A-DECIDER.md).
