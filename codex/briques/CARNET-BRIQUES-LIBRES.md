# Carnet des briques libres — matière première pour construire

**Ouvert le 2026-09-20.** Tenu par `chercheur-code-libre`. Ajout uniquement.

Ce carnet ne contient que des **briques réellement utilisables** : code publié, licence lue, et une
ligne disant ce que la brique **ne fait pas**. Une brique sans licence vérifiée n'entre pas.

**Règle de licence, appliquée sans exception.** MIT et Apache-2.0 : on construit dessus, on ferme
notre couche, on vend. GPL et AGPL : contamination, on ne vend plus en fermé — refusé ici sauf
décision explicite de Chaima. Apache-2.0 porte en plus une **concession de brevet** de ses
contributeurs, ce qui réduit le risque d'être attaqué sur la brique elle-même.

**Avertissement qui commande tout le reste.** Un code publié est de l'**art antérieur**, y compris
contre nous. On ne brevette jamais l'assemblage de ces briques : il est évident dès qu'on les voit.
On brevette **la couche qu'on ajoute** et que personne n'a faite.

Licences relevées le 2026-09-20 sur la fiche du dépôt. **À revérifier avant tout usage réel** — une
licence peut changer d'une version à l'autre, et `loopx` en est l'exemple : MIT jusqu'à v0.4.7,
Apache-2.0 à partir de v0.4.8.

---

## B-01 — NVIDIA/OpenShell · **Apache-2.0** · 8 282 étoiles

**Ce que ça donne.** Un bac à sable d'exécution pour agents autonomes. Chaque bac est isolé dans
son conteneur, et **chaque connexion sortante est interceptée par un moteur de politique** décrit en
YAML déclaratif. Les identifiants sont injectés en variables d'environnement à la création et **ne
touchent jamais le système de fichiers du bac**. Pilotes de calcul : Docker, Podman, MicroVM,
Kubernetes.

**Ce que ça ne fait pas.** Il contrôle ce que l'agent **peut atteindre**. Il ne dit rien de ce que
l'agent **conclut**.

## B-02 — winsenlabs/platos · **Apache-2.0**

**Ce que ça donne.** Un runtime d'agents complet, présenté comme le remplaçant libre des services
hébergés. Exécution durable sur trigger.dev — chaque appel long est une exécution reprenable avec
reprises, files et traces. Passerelle MCP universelle fédérant quatre familles d'outils derrière un
point d'entrée unique, avec portée OAuth et liste de contrôle par outil. Mémoire, compétences,
observabilité câblées au niveau du runtime : base vectorielle, graphe de connaissances, traces
OpenTelemetry, registre de coûts ClickHouse. Modèle multi-locataire par `(organisation, projet,
environnement)`.

**Ce que ça ne fait pas.** Il trace tout et ne juge rien.

## B-03 — adenhq/hive · **Apache-2.0**

**Ce que ça donne.** Des **colonies** d'agents plutôt qu'un graphe câblé à la main. Une seule
primitive d'exécution : la reine est une boucle d'agent, chaque ouvrier en est un clone. La
coordination passe par un **registre partagé** et un plan persistant. Reprise après incident,
plafond de coût, et intervention humaine hors bande.

**Ce que ça ne fait pas.** Les ouvriers sont des clones — même modèle, mêmes outils. **Un clone ne
contredit pas son original.**

## B-04 — HKUDS/OpenSpace · **MIT** · 7 496 étoiles

**Ce que ça donne.** Une couche de gestion des compétences : bibliothèque partagée entre agents,
import explicite avant réutilisation, et surtout **jugement des compétences sur les résultats
réels** — sélectionnée, appliquée, terminée, ou abandonnée — avec historique de versions et
lignée. Local d'abord, déployable en privé.

**Ce que ça ne fait pas.** Le signal de qualité est l'**exécution** : la tâche s'est-elle terminée.
Une compétence qui termine toujours en produisant une conclusion fausse sera jugée excellente.

## B-05 — alibaba/open-code-review · **Apache-2.0** · 6 135 étoiles

**Ce que ça donne.** Architecture hybride revendiquée : **pipelines déterministes + agent**, chacun
sur ce qu'il fait le mieux. Regroupement intelligent de fichiers en unités de revue, chaque paquet
traité par un sous-agent à contexte isolé. Appariement fin des règles au fichier. Éprouvé deux ans
en interne chez Alibaba avant publication.

**Ce que ça ne fait pas.** C'est de la revue de code. Le principe — déterministe pour ce qui peut
l'être, agent pour le reste, contextes isolés pour éviter la contagion — est transposable ; le
produit non.

## B-06 — Huangruiteng/loopx · **Apache-2.0 depuis v0.4.8** (MIT jusqu'à v0.4.7)

**Ce que ça donne.** Un noyau d'état pour agents à long horizon, **par-dessus** n'importe quel
harnais plutôt qu'à la place : objectifs, garde-barrières, tâches typées, preuves, quotas,
passages de main. Sans dépendance hors bibliothèque standard. Reprise entre tours.

**Ce que ça ne fait pas.** Les auteurs l'écrivent eux-mêmes : *« LoopX n'est pas un contrôleur de
production autonome. Les permissions dangereuses, la publication, les écritures en production et la
propriété finale restent à l'humain. »* C'est exactement la règle §10 de notre CODEX, écrite par
d'autres.

## B-07 — openai/symphony · **Apache-2.0**

**Ce que ça donne.** Transforme le travail de projet en exécutions autonomes isolées, avec
**preuve de travail** : état de l'intégration continue, retours de revue, analyse de complexité,
vidéos de parcours. L'humain gère le travail, pas l'agent.

**Ce que ça ne fait pas.** La preuve est une preuve d'**exécution réussie**, pas de justesse.

---

# LE TROU COMMUN AUX SEPT

Et il est net. Ces sept projets couvrent l'isolation, la mémoire, les compétences, les traces, les
coûts, la reprise après incident, l'intervention humaine, la preuve de travail. Aucun ne couvre
**la contradiction organisée**.

Tous vérifient la même chose : **la tâche s'est-elle terminée**. Aucun ne vérifie : **la conclusion
est-elle juste**. Un agent peut réussir parfaitement une tâche et se tromper — c'est même le mode de
défaillance le plus coûteux, parce qu'il ne déclenche aucune alarme.

Ce qui manque partout, et qui existe ici :
- un rôle dont l'unique fonction est d'**attaquer** la conclusion, jamais de la produire ;
- un **registre de débats** où une décision porte le camp perdant et ce qu'il a obtenu ;
- une **base d'erreurs en ajout seul**, qui documente les causes et jamais les coupables ;
- des **contrôles bloquants** qui refusent un commit, et qu'on durcit quand ils sont pris en défaut.

`hive` en est l'illustration la plus claire : ses ouvriers sont des **clones** de la reine. Même
modèle, mêmes outils, même angle mort. Un clone ne contredit pas son original.

**Ce que ça ne prouve pas.** Que personne ne l'a fait — aucune recherche d'antériorité n'a encore
été menée sur cette couche. Que c'est brevetable — l'effet technique reste à établir. Que ça se
vend. Ces trois questions sont ouvertes et se traitent dans cet ordre.

**Ce que ça établit.** Sept projets récents, dont deux d'NVIDIA et d'OpenAI, ont tous résolu les
mêmes problèmes et laissé le même trou. C'est un fait vérifiable, daté, avec les dépôts à l'appui.
