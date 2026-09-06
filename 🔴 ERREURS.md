# 🔴 ERREURS.md — registre des erreurs (réelles, datées, avec correction)

> Une erreur = une ligne datée. On ne supprime pas une erreur corrigée : on la marque CORRIGÉE (traçabilité).
> Vérité totale : une erreur cachée est une erreur qui reviendra. Le plus récent en haut.

| Date | Erreur | Statut | Preuve / correction |
|---|---|---|---|
| 2026-09-06 | pip-audit auditait l'environnement Ubuntu du runner au lieu du projet | ✅ CORRIGÉE | cible = uv.lock (635 dépendances) ; run n°3 vert (commit bfe624f) |
| 2026-08-10 | Racine du site servait un placeholder noindex « Redirection en cours » | ✅ CORRIGÉE | index.html = vraie page d'accueil conformité ; caelum-index.html → redirection ; +404.html |
| ≤2026-08-10 | Journaux « boucle-caelum » affirmaient à tort « PR #2 non mergée » | ✅ CORRIGÉE | API GitHub : PR #2 closed+merged le 17/07 ; refs/pull/2/head persiste après fusion (normal) |
