# /codex/A-DECIDER.md — décisions en attente de Chaima

> Le seul fichier à ouvrir pour savoir ce qui bloque (CODEX §6). Trié par ancienneté, le plus vieux en haut.
> ⚠️ = en attente depuis plus de 14 jours (mis en évidence). Une ligne ne disparaît que lorsque Chaima a
> tranché (→ consignée avec sa date), jamais parce qu'elle a vieilli. Aujourd'hui : 2026-09-06.

| Quoi | Projet | Type | En attente depuis | Résumé en 1 ligne |
|---|---|---|---|---|
| ⚠️ Prix des 3 offres (Essentiel / Sérénité / Sur-mesure) | Caelum | Produit / prix | 2026-07-17 | offres.html affiche « à confirmer » ; aucun prix validé |
| ⚠️ N° BCE / TVA / éditeur responsable | Caelum | Légal / admin | 2026-07-17 | mentions-legales.html dit « à compléter » ; société pas immatriculée |
| ⚠️ Déclaration C1/C1C ONEM → débloque Stripe | Caelum | Admin / paiement | 2026-07-17 | aucun encaissement possible avant |
| ⚠️ Compte Brevo + LEADS_WEBHOOK_URL | Caelum | Marketing / tech | 2026-07-17 | capture de lead = mailto en attendant l'endpoint |
| Épingler par SHA les 4 actions de deploy.yml | Caelum | Sécurité | 2026-09-06 | SHA non récupérables depuis le sandbox ; risque supply chain signalé |

---
## Décisions tranchées (consignées, ne pas supprimer)
- 2026-07-17 — **POSITIONNEMENT (Étape 0)** : RegTech conformité PME belges (comparatif Drive doc 17). TRANCHÉ PAR CHAIMA.
- 2026-09-06 — **Installation CODEX** : « protocole + structure d'abord », agents non touchés pour l'instant. TRANCHÉ PAR CHAIMA.
- 2026-09-06 — **PR #4 (passation CompeteIQ)** : à refaire sur main à jour. TRANCHÉ PAR CHAIMA.
- 2026-09-11 — **Réconciliation des agents** : « mapper + compléter, sans suppression » — 13 rôles CODEX ajoutés (cœur parcours 2 + angles morts), 8 mappés aux agents existants, les 29 d'origine conservés (table : /codex/agents-correspondance.md). TRANCHÉ PAR CHAIMA.
