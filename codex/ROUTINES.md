# /codex/ROUTINES.md — registre des Routines (ordonnanceurs)

> **Pourquoi ce fichier existe.** Jusqu'au 2026-09-14, les Routines qui réveillent les agents
> n'existaient **nulle part** dans le dépôt. Les agents ignoraient ce qui les déclenchait, à quelle
> cadence, et sur quelles instructions. Conséquence directe : une vingtaine de documents Drive en 72 h
> pour dire « rien de neuf », et une Routine qui travaillait depuis des jours sur des instructions
> périmées sans que personne puisse le voir. C'est la fiche **E-23**, et sa cause profonde est la
> fiche **E-07** — un inventaire incomplet du système par lui-même.
>
> **Un ordonnanceur non inventorié est un angle mort par construction :** aucune règle écrite pour les
> agents ne peut l'atteindre.

## RÈGLES DE TENUE — les cinq qui comptent

1. **Toute Routine figure ici.** Une Routine créée sans ligne ici est un défaut, à signaler dans
   `A-DECIDER.md`. Le registre se relit avec `mcp__Claude_Code_Remote__list_triggers`.
2. **Chaque Routine déclare sa condition d'arrêt.** « Que doit-il se passer pour qu'elle se taise, ralentisse
   ou s'arrête ? » Sans réponse écrite, elle tournera indéfiniment — c'est exactement ce qui s'est produit.
3. **Jamais deux Routines à la même minute.** Deux sessions concurrentes sur le même dépôt se gênent.
   Constaté le 2026-09-14 : les deux seules Routines en état « EN ATTENTE » étaient les deux programmées
   à `22 */2 * * *`. Toutes les autres étaient « réussi ».
4. **Le prompt d'une Routine se périme.** Il cite des PR, des nombres d'agents, des étapes. Quand la
   réalité bouge, le prompt reste. Colonne « prompt relu le » obligatoire ; au-delà de 30 jours,
   `superviseur-vigie` le signale.
5. **Une boucle bloquée sur un humain passe en cadence longue ; une boucle dont le travail de fond est
   inaccessible s'arrête.** Elle ne peut produire que du bruit, et le bruit cache le signal.

## ÉTAT AU 2026-09-14 — 10 Routines actives

| Cadence (UTC) | Nom | Ce qu'elle fait | Condition d'arrêt | Prompt relu le |
|---|---|---|---|---|
| `52 */2 * * *` | La Loi Avec Moi — BOUCLE contenu | 1-2 fiches juridiques sourcées tier-1 par passage, déposées au Drive | corpus saturé sur les 12 domaines prioritaires | 2026-09-14 |
| `22 */8 * * *` | Caelum — BOUCLE de production | avance la checklist Caelum, prépare les diffs « À POUSSER » | checklist P0 vidée, ou site publié | 2026-09-14 |
| `35 9 * * *` | Caelum — Chaîne veille brevets & capitaux | veille brevets / technologies / capitaux | **accès aux registres rouvert** — sinon elle ne peut rien produire | 2026-09-14 |
| `40 * * * *` | Jeu Linux Empire Chaima — Amélioration continue | *(hors périmètre de cette session — non audité)* | **à déclarer** | **jamais** |
| `30 20 * * *` | Méta-surveillance — gardien du gardien | cohérence transverse | permanente (contrôle) | à déclarer |
| `0 16 * * *` | Surveillant Drive & Orchestrateur Caelum | surveillance Drive | permanente (contrôle) | à déclarer |
| `0 11 * * *` | Point de contrôle de midi | point quotidien | permanente (rituel) | à déclarer |
| `30 19 * * *` | Feedback quotidien honnête | feedback du soir | permanente (rituel) | à déclarer |
| `30 7 * * *` | Coach quotidien | coaching du matin | permanente (rituel) | à déclarer |
| une fois | Caelum — contrôle (cadence longue, 8 h) | contrôle ponctuel | s'éteint après son passage | — |

### Corrections appliquées le 2026-09-14 (Chaima : « arrange tous les problèmes »)
- **`La Loi — BOUCLE contenu`** : `22 */2` → **`52 */2`**. Supprime la collision de minute, qui est la
  cause la plus probable des deux Routines restées « EN ATTENTE ».
- **`Caelum — BOUCLE de production`** : `22 */2` → **`22 */8`**. Elle attend une action humaine (push
  authentifié, décisions de Chaima) : 12 réveils par jour pour redire la même attente, c'était la source
  principale du bruit. 3 suffisent.
- **`Chaîne veille brevets & capitaux`** : **horaire → quotidienne**. Son travail de fond est inaccessible
  (registres de brevets refusés par le proxy) ; 24 réveils quotidiens ne pouvaient produire que du vide.

Passé d'environ **60 réveils par jour à environ 20**.

### Défaut de fond corrigé le même jour
Le prompt de `Chaîne veille brevets & capitaux` demandait de « corriger les défauts restants de la PR #7 »
et d'« avancer la réconciliation des 21 vs 29 agents ». **Les deux étaient périmés** : la PR #7 est obsolète
depuis le 2026-09-12 et la réconciliation est faite depuis le 2026-09-11 (56 agents). La Routine partait donc,
chaque heure, sur une consigne sans objet. Une boucle qui ne produit rien n'est pas toujours une boucle
paresseuse : **regarder d'abord si sa consigne décrit encore le monde.**

## CE QUI RESTE À DÉCLARER
Cinq Routines n'ont ni condition d'arrêt écrite ni date de relecture de prompt, dont
`Jeu Linux Empire Chaima` qui tourne **toutes les heures** sans avoir été auditée ici. À faire par Chaima
ou par la session qui les a créées — pas devinable depuis ce dépôt.
