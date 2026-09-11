# /codex/A-DECIDER.md — décisions en attente de Chaima

> Le seul fichier à ouvrir pour savoir ce qui bloque (CODEX §6). Trié par ancienneté, le plus vieux en haut.
> ⚠️ = en attente depuis plus de 14 jours (mis en évidence). Une ligne ne disparaît que lorsque Chaima a
> tranché (→ consignée avec sa date), jamais parce qu'elle a vieilli. Aujourd'hui : 2026-09-11.

| Quoi | Projet | Type | En attente depuis | Résumé en 1 ligne |
|---|---|---|---|---|
| ⚠️ Prix des 3 offres (Essentiel / Sérénité / Sur-mesure) | Caelum | Produit / prix | 2026-07-17 | offres.html affiche « à confirmer » ; aucun prix validé |
| ⚠️ N° BCE / TVA / éditeur responsable | Caelum | Légal / admin | 2026-07-17 | mentions-legales.html dit « à compléter » ; société pas immatriculée |
| ⚠️ Déclaration C1/C1C ONEM → débloque Stripe | Caelum | Admin / paiement | 2026-07-17 | aucun encaissement possible avant |
| ⚠️ Compte Brevo + LEADS_WEBHOOK_URL | Caelum | Marketing / tech | 2026-07-17 | capture de lead = mailto en attendant l'endpoint |
| Épingler par SHA les 4 actions de deploy.yml | Caelum | Sécurité | 2026-09-06 | **Blocage levé le 2026-09-11** : les 4 SHA sont en main (voir sous le tableau). Arbitrage réel à trancher, pas un simple correctif |
| Auto-héberger Fraunces et Inter (RGPD) | Caelum | Données personnelles | 2026-09-11 | Servies par fonts.gstatic.com → l'IP de chaque visiteur part chez Google sans consentement. Pas un défaut de licence. Remède autorisé par l'OFL |
| Verdict sur le spécimen « Le Signal » | Caelum | Design | 2026-09-11 | Consultable : https://claude.ai/code/artifact/8413c51c-4b28-44fc-ba24-cd76d5619392 — débloque la refonte du corps du site, toujours en « Le Greffe » |

---
## Épinglage par SHA — les faits, pour trancher

**Ce qui a changé le 2026-09-11.** Le motif d'attente inscrit le 2026-09-06 (« SHA non récupérables
depuis le sandbox ») ne tient plus : l'API GitHub reste bien fermée aux dépôts hors session (HTTP 403),
mais `git ls-remote` passe par le proxy git et les résout. **VÉRIFIÉ**, le 2026-09-11 :

    actions/checkout@v4                11d5960a326750d5838078e36cf38b85af677262
    actions/configure-pages@v4         1f0c5cde4bc74cd7e1254d0cb4de8d49e9068c7d
    actions/upload-pages-artifact@v3   56afc609e74202658d3ffba0e8f6dda462b719fa
    actions/deploy-pages@v4            d6db90164ac5ed86f2b6aed7e0febac5b3c0c03e

**POUR (Avocat).** Une étiquette `v4` est une référence mobile : le code exécuté dans le pipeline qui
publie le site peut changer sans notre accord. C'est le vecteur « repo hijacking » du CODEX §3, et
`scripts/audit_code_sur.py` le signale à chaque exécution. Un SHA fige exactement ce qui tourne.

**CONTRE (Contradicteur).** Épingler coupe aussi les **correctifs de sécurité** publiés sur l'étiquette :
une faille corrigée dans `checkout@v4` ne nous atteindrait plus. On échange un risque (code modifié à
notre insu) contre un autre (code figé et vulnérable). Sans une routine de mise à jour réelle, l'épinglage
dégrade la sécurité au lieu de l'améliorer. De plus ces 4 actions sont publiées par **GitHub lui-même**
(`actions/`) : c'est le profil de mainteneur le moins à risque de la grille.

**Ce que je n'ai pas pu établir. NON VÉRIFIÉ** : que le pipeline déploie encore correctement une fois
épinglé. Je ne peux pas exécuter GitHub Actions en local ; la seule preuve serait un déploiement réel
après fusion. C'est le vrai risque de ce changement — il touche la chaîne qui publie le site.

**Ce qui trancherait.** Si tu veux l'épinglage, il vient avec sa contrepartie : une relecture périodique
des 4 SHA, sinon on fige des failles. Dis-le et je le prépare en PR séparée — jamais mélangée à une PR
de contenu, pour que le déploiement soit vérifiable isolément.

---
## Décisions tranchées (consignées, ne pas supprimer)
- 2026-07-17 — **POSITIONNEMENT (Étape 0)** : RegTech conformité PME belges (comparatif Drive doc 17). TRANCHÉ PAR CHAIMA.
- 2026-09-06 — **Installation CODEX** : « protocole + structure d'abord », agents non touchés pour l'instant. TRANCHÉ PAR CHAIMA.
- 2026-09-06 — **PR #4 (passation CompeteIQ)** : à refaire sur main à jour. TRANCHÉ PAR CHAIMA.
- 2026-09-11 — **Réconciliation des agents** : « mapper + compléter, sans suppression » — 13 rôles CODEX ajoutés (cœur parcours 2 + angles morts), 8 mappés aux agents existants, les 29 d'origine conservés (table : /codex/agents-correspondance.md). TRANCHÉ PAR CHAIMA.
- 2026-09-11 — **Direction artistique** : « Le Greffe » (direction A) REJETÉ (« un vieux site des années 2000 »,
  trop vide, sans texture). **Direction C « Le Signal » retenue, indigo `#4338CA` confirmé.** L'ancienne palette
  navy/vert/or est rejetée et n'est pas rouverte. Non négociables reconduits : Fraunces + Inter, contenu légal,
  prix et disclaimers strictement inchangés, simulateur identique au caractère près, sélecteur FR/NL en entrée,
  bloc « expert nommé » en réserve et vide. TRANCHÉ PAR CHAIMA.
- 2026-09-11 — **Périmètre de publication (« Option 0 »)** : caelumpartners.agency ne sert plus que Caelum.
  CompeteIQ et KeywordMoneyMaker restent dans le dépôt mais ne sont plus publiés. TRANCHÉ PAR CHAIMA.
- 2026-09-11 — **Purge de l'historique git du CV** : NON, coût supérieur au bénéfice (ce n'est qu'un CV).
  Le risque résiduel réel est le cache Google et la Wayback Machine → demande de retrait via Search Console.
  TRANCHÉ PAR CHAIMA.
- 2026-09-11 — **Visibilité du dépôt, dépôt de marque et dates i-DEPOT** : administratif, Chaima s'en charge
  elle-même. Hors périmètre des agents. TRANCHÉ PAR CHAIMA.
- 2026-09-11 — **PR #19 — identité de marque** : FUSIONNÉE (merge `7163653`), sur autorisation explicite
  de Chaima (« Merge PR #19 maintenant — aucune décision requise, elle est verte »). Déploiement GitHub
  Pages en succès ; les 5 fichiers d'identité figurent dans l'archive publiée. TRANCHÉ PAR CHAIMA.
