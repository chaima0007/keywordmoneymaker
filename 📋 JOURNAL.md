# 📋 JOURNAL.md — snapshots d'entrée de session (CODEX §5)

> Rituel d'entrée : état réel vérifié (jamais de mémoire), comparé au dernier snapshot.
> Rien n'a changé → une seule ligne « SNAPSHOT [date] : aucun changement ». Un changement → entrée datée et précise.
> Un rapport pour dire qu'il n'y a rien à dire est une faute contre le protocole. Le plus récent en haut.

## SNAPSHOT 2026-09-28 20h13 (Europe/Brussels) — audit demandé : garde-fous, réparateurs, experts

**Écart de rituel, le même qu'il y a quinze jours.** Dernier snapshot : 2026-09-16. Douze jours,
huit commits poussés dans l'intervalle (`git log --oneline --since=2026-09-16 | wc -l` → 8).
`ETAT.md` n'a pas bougé depuis le 2026-09-14. Une Routine de contrôle tournait toutes les six heures
et répondait « aucun changement » — vrai pour la PR surveillée, faux pour le dépôt. Fiche **E-30**.

**État réel vérifié, pas de mémoire.**
- `main` distant = `2a975ec`, inchangé depuis le 2026-09-16. Branche `ux/questions-simulateur`
  = `74b879f`, 8 commits d'avance, PR #26 **en brouillon**, CI verte, sans conflit.
- Rien de ce qui a été fait depuis le 19/09 n'est en production. C'est voulu : parcours 3, relecture
  humaine obligatoire.

**Les garde-fous — 5 contrôles bloquants, tous verts ce jour (code 0).**
`audit_code_sur.py` · `audit_cloisonnement.py --bloquant` · `generer_registre_erreurs.py --verifier` ·
`verifier_rapports.py` · `verifier_coherence_juridique.py`. Ils tournent dans
`.github/workflows/securite-code.yml`. Le second workflow, `deploy.yml`, publie en liste blanche et
ne se déclenche que sur `main` : ses quatre gardes ne s'exécutent donc **jamais** sur une PR — connu,
consigné dans la carte, non corrigé.

**Les réparateurs — un seul répare vraiment.** `generer_registre_erreurs.py` régénère
`🔴 ERREURS.md` depuis `.claude/BASE-ERREURS.md` et échoue en CI si les deux divergent. Les quatre
autres **constatent** et bloquent, ils ne corrigent rien. Le vrai réparateur du dispositif reste la
base d'erreurs elle-même : 30 fiches, dont 5 nées d'erreurs commises par un agent cette quinzaine
(E-26 à E-30).

**Les experts — 56 définitions Markdown, 36 modules Python, 12 fiches d'expertise.**
`/codex/expertise/` était vide jusqu'au 2026-09-21 : le domaine « droit de la conformité — Belgique »
y est désormais ouvert, maturité CONFIRMÉ (12 fiches, un seul projet — EXPERT exige un deuxième).

**Défaut trouvé par cet audit, et corrigé.** Le §2 ter.3 du CLAUDE.md — le paragraphe que tout agent
doit lire « avant d'affirmer ce qui existe déjà » — désignait « les 33 modules Python de `agents/` »
et « `agents/base_erreurs.py` ». **Ce dossier n'existe pas.** Les modules sont répartis dans
`products/*/agents/` (21) et `shared/` (15), soit 36, et la base d'erreurs est atteinte via
`shared/base_erreurs.py`. `codex/CARTE.md` portait, lui, les bons chemins depuis le 2026-09-16 : la
carte était juste et la constitution périmée. Corrigé dans CLAUDE.md.

**Audit de cohérence (§5.5).** CLAUDE.md porte le CODEX ✅ · structure /codex conforme §12 ✅ ·
A-DECIDER redaté (il affichait le 20/09) ✅ · ETAT.md remis à jour ✅ · `deploy.yml` sans garde sur PR ⚠️
(inchangé) · 5 Routines sans condition d'arrêt déclarée ⚠️ (inchangé depuis le 14/09).

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
