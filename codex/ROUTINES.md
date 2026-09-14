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

## TROU DE COUVERTURE DE LA MÉTA-SURVEILLANCE (relevé le 2026-09-14)
La Routine « Méta-surveillance — gardien du gardien » est le seul dispositif qui contrôle les autres.
Sa consigne nomme **cinq** Routines à auditer : Coach 09h30 · Point de contrôle de midi 13h00 ·
Surveillant Drive 18h00 · Feedback honnête 21h30 · La Loi Avec Moi 08h00 (heures de Bruxelles).

Deux défauts, relevés en lisant la consigne elle-même et non sa description :

1. **Cinq Routines sur dix sont hors surveillance** — dont « Caelum — BOUCLE de production »,
   « Caelum — Chaîne veille brevets & capitaux », « Caelum — contrôle 8 h » et
   « Jeu Linux Empire Chaima », c'est-à-dire précisément celles qui produisent du code et des
   documents. Le gardien du gardien ne regarde pas là où le travail se fait.
2. **Une heure citée est devenue fausse par notre faute** — la consigne attend La Loi Avec Moi à
   08h00 ; depuis la correction de cadence du 2026-09-14 elle tourne toutes les deux heures.
   Le gardien auditera donc une Routine muette à 08h00 et conclura à une anomalie inexistante,
   pendant que douze exécutions réelles passeront inaperçues. C'est le motif de la fiche E-02
   (un faux positif qui survit parce que personne ne recoupe la consigne avec le monde).

**Ni l'un ni l'autre n'est corrigé ici** : réécrire la consigne d'une Routine, c'est modifier
l'automatisation de Chaima. Proposition déposée, décision à elle.

## VOIR AUSSI
- `codex/veille/CHARTE-CHAINE.md` — les 5 règles propres à la chaîne veille que rien d'autre ne couvre
  (divulgation art. 54 CBE, nommage Drive, sauvegarde, cadence des offices, structure Drive).
- `codex/veille/JOURNAL-CHAINE.md` — l'historique des sessions de la chaîne.

---

## OBJECTION DU CONTRADICTEUR — contre ce dispositif (2026-09-14)
Le protocole exige une objection sérieuse avant toute décision actée. En voici deux, contre ma propre
correction, et la seconde est la plus gênante.

### Objection 1 — « Ce registre est lui-même une seconde source de vérité »
`codex/ROUTINES.md` est un **fichier du dépôt**. Les Routines, elles, vivent **ailleurs** — dans le
service qui les déclenche. **Rien ne les synchronise.** Si Chaima change une cadence depuis son téléphone
demain matin, ce registre aura tort sans que rien ne le signale. C'est mot pour mot la fiche **E-18** :
deux sources qui répondent à la même question, sans contrôle qui les compare.

**Réponse honnête, et elle est partielle.** Pour la base d'erreurs, la contre-mesure était complète : une
source qui fait foi, un index **généré**, et un contrôle CI qui échoue si les deux divergent. **Ici je ne
peux pas faire pareil** — les Routines ne sont pas dans le dépôt, la CI n'y a aucun accès, le registre ne
peut donc pas être généré. Il reste écrit à la main.

Ce qui a été fait à la place : désigner la source qui fait foi (**les Routines réelles**, relues via
`list_triggers` — jamais ce fichier), et confier la comparaison à `superviseur-vigie` à chaque entrée de
session. C'est un contrôle **humain et agentique**, pas machine. **C'est plus faible que pour les
erreurs, et il faut le savoir** : ce registre est aussi fiable que la discipline de sa relecture. La
discipline seule a déjà perdu deux fois dans ce projet (E-01, E-07).

*Ce qui lèverait l'objection :* un accès en lecture aux Routines depuis la CI. Il n'existe pas aujourd'hui.

### Objection 2 — « Ralentir, c'est détecter plus tard »
La chaîne veille est passée d'horaire à quotidienne. Or sa consigne lui demandait aussi de vérifier
qu'aucune information sensible n'est exposée publiquement. Cette vérification passe donc de 24 fois par
jour à 1.

**Réponse.** Les contrôles qui protègent réellement n'ont pas bougé : le scan de secrets et le
cloisonnement tournent en **CI, à chaque push**, pas dans la Routine. Ce qui ralentit est la relecture
d'opportunité côté Drive. Le compromis est acceptable — mais il est réel, et le nier serait malhonnête.

### Ce qui a été retenu
Les deux objections sont **fondées** et ne sont pas écartées : elles sont inscrites ici pour que le
prochain qui lit ce fichier sache exactement ce qu'il protège et ce qu'il ne protège pas.

