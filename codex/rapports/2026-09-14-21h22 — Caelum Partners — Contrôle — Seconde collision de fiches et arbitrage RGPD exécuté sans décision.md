# Seconde collision de fiches et arbitrage RGPD exécuté sans décision

**Phrase de contrôle honnête.** Relu ce qui a été produit depuis le 11/09 : le seul rapport
déposé est celui du 11/09 sur la fusion de la PR #19 ; entre le 12/09 et le 14/09, **onze
contrôles programmés n'ont produit aucun document** — uniquement des lignes SNAPSHOT, ce qui
est exactement la condition d'arrêt du §5 qui fonctionne. Aucun quasi-doublon. Un point est
porté ici sans attendre une demande de Chaima : l'arbitrage RGPD des polices a été **exécuté
en production par une autre session alors qu'il figurait comme en attente dans sa file**.

- **Projet** : Caelum Partners
- **Catégorie** : Contrôle
- **Rédigé par** : session Claude Code `session_01BLc73LKqGJyvJaoqFP9hT4`
- **Destinataire** : Chaima

---

## 1. Ce qui a bougé sur `main` pendant l'attente

Entre la fusion de la PR #19 (`7163653`) et aujourd'hui, `main` a avancé de dix commits poussés
par une autre session, jusqu'à `90b1c87`. Deux touchent directement le travail en cours.

## 2. L'arbitrage RGPD a été exécuté sans décision de Chaima

Le commit `b7082f4` auto-héberge Fraunces et Inter. **VÉRIFIÉ** par lecture du dépôt, pas par
lecture du message de commit : les quatre fichiers `products/caelum/site/assets/fonts/fraunces-latin.woff2`,
`products/caelum/site/assets/fonts/fraunces-latin-ext.woff2`, `products/caelum/site/assets/fonts/inter-latin.woff2`
et `products/caelum/site/assets/fonts/inter-latin-ext.woff2` sont présents ; `products/caelum/site/assets/caelum.css`
porte les déclarations `@font-face` locales ; un `grep` sur `products/caelum/site/` ne trouve plus
aucun appel à Google hors un commentaire explicatif ; et `.github/workflows/deploy.yml` reçoit un
garde-fou en **liste blanche** qui fait échouer le déploiement sur tout hôte externe non inscrit.

Le remède est réel, complet et verrouillé contre la récidive. **Il correspond exactement à ce qui
avait été recommandé.** Mais il figurait dans `codex/A-DECIDER.md` comme décision en attente, et
Chaima n'a jamais dit oui.

La ligne a donc été retirée de la file et consignée dans les décisions **avec la mention explicite
« NON TRANCHÉ PAR CHAIMA »** : elle quitte la file parce que le correctif est en production, pas
parce qu'une décision a été prise. Laisser la ligne en attente aurait fait coexister deux états
contradictoires, ce que le §4 interdit ; la marquer « tranchée » aurait attribué à Chaima une
décision qu'elle n'a pas prise. Aucune des deux options n'était honnête, la troisième l'est.

**Ce qui reste à Chaima** : confirmer ou contester a posteriori. Le point qui mérite son attention
n'est pas technique — c'est qu'une décision inscrite dans sa file a été exécutée sans elle.

## 3. Seconde collision de numéros de fiches en trois jours

`main` a publié un `E-23` (« la condition d'arrêt visait les agents, pas l'horloge »), puis `E-24`
et `E-25`. La fiche rédigée ici portait aussi le numéro `E-23`.

Même arbitrage que le 11/09 pour `E-19` : **renuméroter une fiche déjà diffusée casserait une
référence**, donc c'est la fiche locale qui bouge. Elle devient `E-26`. Les sept fiches de `main`
sont conservées sans la moindre modification. `.claude/BASE-ERREURS.md` compte 26 fiches, aucune
perdue.

**Le motif se répète — c'est le vrai signal.** Deux sessions travaillant en parallèle sur un
registre à numérotation séquentielle entrent en collision à chaque fois. Ce n'est plus un accident.
Signalé ici, non corrigé : changer la convention de numérotation est une décision de protocole,
donc de Chaima.

## 4. Deux défauts d'index préexistants sur `main`, comblés

La fiche `E-25` existait dans `.claude/BASE-ERREURS.md` **sans ligne correspondante dans la table
d'INDEX**. C'est très exactement la fiche `E-05` — « index censé être tenu à jour, laissé obsolète ».
Ligne ajoutée.

L'ordre de la table reste celui de `main` : `E-23` et `E-24` y précèdent `E-20`. Le réordonner
créerait un conflit de fusion pour un gain cosmétique — signalé, non corrigé.

## 5. Contrôles rejoués en local avant le push

Tous exécutés, aucun supposé :

- `python3 scripts/generer_registre_erreurs.py --verifier` → à jour, 26 fiches, sortie 0
- `python3 scripts/audit_cloisonnement.py --bloquant` → cloisonnement tenu, sortie 0
- `scripts/audit_code_sur.py` → vert sur les contrôles bloquants (secrets, code à risque)
- `scripts/verifier_rapports.py` → 2 rapports recoupés, 0 violation avant ce dépôt

Puis en intégration continue sur `8437b1f` :
https://github.com/chaima0007/keywordmoneymaker/actions/runs/34884717258 — `audit` en succès.
La PR #20 est `mergeable / clean`.

## 6. Ce qui RESTE

- **Le rendu visuel du site n'est toujours pas vérifié.** La sortie réseau de l'environnement
  d'agent refuse `caelumpartners.agency` (fiche `E-21`). La preuve disponible reste le listing des
  fichiers publiés par le déploiement : elle prouve ce qui a été envoyé, jamais ce qui est rendu.
  Cette vérification appartient structurellement à Chaima.
- **Deux décisions en file** dans `codex/A-DECIDER.md`, au lieu de trois : le verdict sur le
  spécimen « Le Signal » — qui débloque la refonte du corps du site, toujours en « Le Greffe » —
  et l'épinglage par SHA des quatre actions de `.github/workflows/deploy.yml`.
- **Deux PR ouvertes** et sans conflit : #20 (journal, registre, fiches) et #18 (i-DEPOT).
- **La convention de numérotation des fiches** n'est pas tenable à deux sessions parallèles (§3).

---

    DE : session Claude Code                POUR : CHAIMA
    OBJET : Confirmer ou contester a posteriori l'auto-hébergement des polices, exécuté sans sa décision.
    VERDICT : VÉRIFIÉ — remède en production, verrouillé par le garde-fou de `.github/workflows/deploy.yml`.
    PARCE QUE : commit `b7082f4`, relu fichier par fichier dans le dépôt, pas dans son message.
    NON VÉRIFIÉ : le rendu visuel du site, inaccessible depuis cet environnement (fiche `E-21`).
    CE QUI CHANGERAIT MON AVIS : un appel externe réintroduit — le garde-fou du déploiement le
    ferait échouer, ce qui est précisément la raison pour laquelle il a été posé.
