# 🔴 ERREURS.md — erreurs réelles, datées, et ce qu'on en a tiré

> Une entrée = une erreur réellement survenue. Pas de spéculation.
> Format : date · ce qui s'est passé · cause · correctif · comment on l'évite désormais.

## 2026-09-06 — Fausse alerte « fichier corrompu » (session Claude Code)
- **Ce qui s'est passé** : alerte émise sur `caelum-index.html` (« contenu banni : 9 agents / élite »).
- **Cause réelle** : la session était sur la branche `claude/humanizer-skill-setup-f963e3`, qui porte
  l'ANCIEN site. Aucune corruption, aucune perte.
- **Correctif** : vérification `git log`/`git show` sur `origin/design/caelum-premium-refonte` →
  refonte intacte (Fraunces présent, 0 occurrence bannie).
- **Règle qui en découle** : toujours afficher la branche courante (`git branch --show-current`)
  AVANT de qualifier un contenu d'anormal. Un fichier « faux » peut n'être qu'une autre branche.
