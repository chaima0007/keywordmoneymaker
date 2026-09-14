# 📋 JOURNAL.md — snapshots d'entrée de session (CODEX §5)

> Rituel d'entrée : état réel vérifié (jamais de mémoire), comparé au dernier snapshot.
> Rien n'a changé → une seule ligne « SNAPSHOT [date] : aucun changement ». Un changement → entrée datée et précise.
> Un rapport pour dire qu'il n'y a rien à dire est une faute contre le protocole. Le plus récent en haut.

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
