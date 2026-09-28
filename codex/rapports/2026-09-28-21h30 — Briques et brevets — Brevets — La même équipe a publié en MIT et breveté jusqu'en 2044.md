# La même équipe a publié en MIT et breveté jusqu'en 2044

**Contrôle honnête d'entrée.** Ce rapport annonce le sixième croisement mort, et je dois dire d'abord
ce qui le rend différent : il ne tue pas seulement `X-06`, il **corrige l'argument qui a justifié le
virage quantique**, écrit par moi le matin même. Aucun document quasi identique dans
`codex/rapports/` — les cinq précédents portent sur des croisements dont aucun ne touche la
photonique. Le seul document voisin est
`codex/rapports/2026-09-28-11h00 — Transversal — Brevets — La publication défensive : le domaine est rendu inbrevetable en temps réel.md`,
qui traite du logiciel et conclut l'inverse de celui-ci.

**Au service de la consigne n°1** en vigueur (`codex/CONSIGNE-N1.md`) : trouver du code libre, le
fusionner, construire, puis protéger la couche ajoutée. Réponse à l'autorisation « vasy » du
2026-09-28 : chercher l'antériorité de `P-18` avant tout attachement.

---

## 1. Ce que j'ai cherché, et pourquoi c'était le bon endroit

`P-18` est le seul problème du carnet 4 qui ne demande pas de laboratoire. Des auteurs de PsiQuantum
écrivent, dans arXiv:2506.11975 : *« Des métriques améliorées de coût en ressources seraient un
outil précieux pour comparer les protocoles FBQC sans avoir à tenir compte des erreurs physiques
dans toute leur complexité. »* Un besoin énoncé par ceux qui en souffrent, dans un domaine où plus
de six cents réseaux de fusion existent et où rien ne permet de les classer.

C'était le bon endroit. Ce n'était pas un endroit libre.

## 2. Trois morts indépendantes, et chacune suffirait

### Le libre publié — et l'article du besoin le cite lui-même

**OptGraphState**, Lee & Jeong, *Quantum* 7, 1212 (2023), arXiv:2304.11988, dépôt
github.com/seokhyung-lee/OptGraphState, **licence MIT**. Le paquet calcule *« le coût en ressources,
quantifié par le nombre moyen d'états ressources de base requis ou de tentatives de fusion »* pour
générer un état de graphe par fusions de type II à partir d'états à trois qubits.

C'est la métrique demandée, publiée en 2023, réutilisable gratuitement.

Et la référence **[22]** de arXiv:2506.11975 **est ce papier**. À propos de son propre heuristique de
coût, l'article de PsiQuantum écrit : *« une optimisation similaire a été présentée dans [22] »*.

**Les auteurs du besoin ouvert citent, dans le même paragraphe, l'outil qui le comble.** Ce que j'ai
lu comme un trou dans l'état de l'art était un trou dans leur annexe, qu'ils signalent eux-mêmes.
C'est une faute de lecture, et elle a un signal de détection maintenant : quand un article dit qu'un
outil manque, **lire les références de la phrase avant de la croire**.

### Le brevet — et il est plus fort que ce que P-18 demande

**US12596949B2**, *Method and apparatus for linear optical quantum computing*, titulaire **SNU R&DB
Foundation**, inventeurs **Hyunseok Jeong, Seok-Hyung Lee, Yong Siah Teo, Srikrishna Omkar**. Les
deux premiers sont les auteurs d'OptGraphState. Priorité KR du 2022-09-23, **délivré le 2026-04-07**,
expiration affichée 2044-12-16. CPC G06N 10/00, G06N 10/20, G06N 10/40, B82Y 10/00.

Sa revendication 13 revendique « performing a **resource optimization algorithm** for the combination
graph » de microclusters, avec des états GHZ à trois photons et un encodage de parité (n, m). Et sa
description donne la métrique : coût 1 par sommet, coût par arête égal à deux fois l'inverse du carré
de (1 moins le taux de perte), multiplié par la somme des coûts des deux sommets — puis contraction
itérative de l'arête la moins chère.

**Ce coût intègre le taux de perte de photons. Celui de PsiQuantum ne l'intègre pas** : il suppose
explicitement une fusion sans perte. Autrement dit, la seule amélioration que j'avais identifiée —
une métrique consciente de la perte et indépendante du niveau d'encodage — est la revendication
délivrée d'un brevet qui court vingt ans.

Et combiner les deux ne sauve rien : OptGraphState donne l'indépendance à l'encodage, le brevet donne
la conscience de la perte, et **les deux sortent du même laboratoire**. À l'art. 56 CBE, aucune
combinaison n'est plus évidente pour l'homme du métier que celle de deux travaux du même groupe qui
se citent.

### L'art. 52 CBE — et c'est la mort structurelle

Une métrique calculée sur un ordinateur, qui ne commande aucun appareil, est une méthode
mathématique : exclue par l'art. 52(2) CBE sauf effet technique (COMVIK T 641/00, G 1/19).

Or `P-18` est **le seul problème du carnet qui ne demande qu'un ordinateur**. C'est précisément pour
ça qu'il est **le seul sur lequel l'art. 52 mord**. Les quatre autres ont un effet physique et
exigent un laboratoire que nous n'avons pas.

| | Effet physique | Faisable sans laboratoire |
|---|---|---|
| P-15, P-16, P-17, P-19 | oui | non |
| P-18 | non | oui |

**Aucune case n'a les deux.** Et ce n'est pas propre au quantique : c'est la tenaille du logiciel,
déplacée d'un cran. Ce que je peux faire seule, le droit l'exclut ; ce que le droit admet, je ne peux
pas le faire seule.

Le brevet de Séoul montre par où l'on sort, et c'est instructif : l'algorithme y est revendiqué **à
l'intérieur** d'un procédé qui finit par mesurer un qubit central du réseau RHG. La métrique passe
l'art. 52 en étant attachée à un dispositif physique. **Pour breveter du calcul, il faut de la
matière.**

## 3. Ce que ça change, et ce n'est pas rien

Six croisements, six morts. Mais la sixième cause n'existait pas encore :

| | Cause |
|---|---|
| X-01, X-02 | domaines trop proches — ma faute, fiche `E-31` |
| X-03 | idée juste, faite depuis 1990 |
| X-04 | domaine rendu inbrevetable en temps réel par publication défensive |
| X-05 | outil déjà publié, en libre et en documentation |
| X-06 | **libre publié MIT *et* brevet en vigueur, par la même équipe** |

Jusqu'ici les deux barrières étaient alternatives. Dans le logiciel, le libre publié tuait la
nouveauté mais laissait la liberté d'exploitation : on ne pouvait pas déposer, on pouvait utiliser.
**Ici les deux sont debout en même temps** : la publication MIT détruit la nouveauté, le brevet
bloque l'amélioration évidente jusqu'en 2044. C'est la situation la plus fermée rencontrée en dix
jours.

## 4. Ce que je corrige, parce que je l'ai écrit ce matin

Le carnet 4 et le verdict X-05 justifiaient le virage par cette phrase : « en photonique quantique la
logique du terrain est **inverse**, les acteurs déposent massivement au lieu de publier ».

**Faux par moitié, et la moitié fausse portait tout l'argument.** Ils déposent — c'est vrai et
mesuré. Qu'ils ne publient pas, je ne l'avais pas mesuré. C'est la fiche `E-30` retournée : j'avais
alors conclu d'une porte fermée à un bâtiment fermé ; j'ai cette fois conclu d'un dépôt observé à une
absence de publication non observée.

Fiche `E-36` ouverte dans `.claude/BASE-ERREURS.md`, avec son signal de détection : **toute phrase de
la forme « dans ce domaine ils font X plutôt que Y » exige deux traces, une pour X et une pour Y.**
Une mesure plus un contraste rhétorique n'est pas une comparaison.

Corrections faites **par ajout daté** dans les deux documents concernés, jamais par réécriture.

En passant, une dette ancienne réparée dans le même fichier : l'index de `.claude/BASE-ERREURS.md`
s'était arrêté à E-24 alors que onze fiches avaient été écrites après — la fiche `E-05` commise dans
le fichier qui la décrit. Les onze lignes manquantes sont ajoutées, et l'absence de fiche E-32 est
signalée plutôt que comblée.

## 5. Ce qui reste, et qui n'est pas un brevet

Les deux antériorités sont des outils utilisables, entrés au sas le jour même et enregistrés dans
`codex/briques/registre.json` :

- **B-21 seokhyung-lee/OptGraphState** — MIT lue dans LICENSE, commit épinglé 4f7c563634cffd632438ba516dfafece941643aa
- **B-22 TeamGraphix/graphix** — Apache-2.0 lue dans LICENSE, commit épinglé 2b30fdf18c097a8c81eb1cb661bb794262d529ac

Vingt-deux briques au registre, aucune violation des six contrôles consignés — vérifiable par
`python3 scripts/briques.py --verifier`.

C'est la troisième fois que la recherche d'antériorité rapporte un outil plutôt qu'un candidat. À ce
stade c'est le seul rendement mesurable du dispositif, et il faut le dire comme tel plutôt que de le
présenter comme un lot de consolation.

## 6. Ce qui n'est pas prouvé

- Les registres **EPO et Espacenet restent inatteignables** depuis cette session. US12596949B2 a été
  lu sur Google Patents le 2026-09-28. Sont VÉRIFIÉS par cette lecture — existence, titre, titulaire, inventeurs, dates, codes CPC, extraits cités — à https://patents.google.com/patent/US12596949B2/en
  et rien au-delà de ce que cette page affiche.
- **NON VÉRIFIÉ** : l'étendue de la famille (continuations, équivalents EP, CN, JP), la validité, et
  les revendications indépendantes 1 et 7, que je n'ai pas lues mot à mot.
- Le statut « actif jusqu'en 2044 » est un affichage de Google Patents, qui écrit lui-même que ce
  n'est pas une conclusion juridique.
- Aucune recherche CPC exhaustive : G06N 10/ compte des milliers de documents. Ce verdict tue le
  croisement ; il ne prouverait pas l'inverse.
- Les chiffres du carnet 4 n'ont toujours pas été recoupés à la source primaire. PLAUSIBLE, confiance
  MODÉRÉE.
- Rien ici n'est un conseil juridique. Un conseil en PI humain reste requis avant tout dépôt réel.

## 7. Ce qui attend Chaima, et je propose sans trancher

Le carnet 4 a été ouvert parce que `P-18` était « le seul par lequel commencer ». Il est fermé. Les
quatre autres problèmes du carnet demandent un physicien et un laboratoire.

Trois routes, et le choix lui revient :

1. **Chercher un physicien** — P-15, P-16, P-17, P-19 sont des problèmes réels, non résolus, avec
   effet technique. Leur antériorité n'a jamais été cherchée. C'est la seule route qui garde
   l'objectif « brevets à vendre ».
2. **Arrêter de chercher des brevets** et garder du dispositif ce qui rapporte : vingt-deux briques
   vérifiées ligne par ligne, un sas qui débloque des outils que l'étiquette faisait éviter, et la
   liberté d'exploitation — six recherches d'antériorité qui disent ce qu'on peut utiliser sans
   risque.
3. **Changer de terrain une troisième fois** — je le mentionne pour être complet, et je le
   déconseille : deux virages en dix jours ont coûté plus que les six croisements réunis, et rien ne
   dit que le troisième terrain serait mieux mesuré que le second.

Trois décisions restent aussi en attente depuis plusieurs jours, et elles bloquent : créer le dépôt
privé `empire-codex` (je reçois un refus), trancher les vingt-neuf fiches d'agent au périmètre
obsolète (fiche `E-35`), et dire si la règle R9 proposée dans `E-36` entre au dispositif.
