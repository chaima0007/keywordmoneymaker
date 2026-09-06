# 📋 JOURNAL.md — snapshots §5

> Règle anti-bruit : rien n'a changé → UNE ligne « SNAPSHOT [date] : aucun changement », puis silence.
> Quelque chose a changé → une entrée datée et précise. Un document / une entrée = un événement réel.

## SNAPSHOT 2026-09-06 23:11 CEST — installation du PROTOCOLE CODEX (premier snapshot)
- **État réel vérifié** (jamais de mémoire) : `git fetch` + `git log` sur le dépôt actif.
- **Branches** : `main` (site en ligne) · `design/caelum-premium-refonte` (2 commits, PR #3 OUVERTE)
  · `claude/humanizer-skill-setup-f963e3` · `chore/protocole-codex` (celle-ci).
- **Changements depuis le dernier état connu (ETAT.md, 2026-08-10)** :
  - Aucun nouveau commit sur `main` constaté à cette date.
  - PR #3 (refonte premium des 4 pages) toujours EN ATTENTE de fusion — 27 jours.
- **Installé ce jour** : bloc PROTOCOLE CODEX en tête de CLAUDE.md (382 lignes, les 83 lignes
  d'origine conservées à l'identique dessous) + structure §12 + A-DECIDER.md + EVOLUTION.md.
- **Audit de cohérence §5.5** : structure /codex/ désormais conforme au §12.
  **Écart SIGNALÉ, non corrigé** : `.claude/agents/` contient **29 agents** de l'ancienne flotte,
  là où le §12 prévoit **les 21 rôles** du protocole. Reporté dans A-DECIDER.md (§10 : supprimer
  un fichier est une décision humaine).
