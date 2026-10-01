# Carnet 4 — Quantique : fusion, superposition, correction d'erreurs

**Ce carnet ne contient que des problèmes, jamais de solutions.** Tenu par `recolteur-problemes`.
Ouvert le 2026-09-28 sur demande de Chaima. Ajout uniquement.

**Pourquoi ce domaine, et ce n'est pas un caprice.** Cinq croisements sont morts, et quatre fois
sur cinq ce qui bloquait n'était pas un brevet concurrent mais **du libre publié** — dans le
logiciel, les acteurs ne brevettent pas, ils publient, et publier détruit la nouveauté aussi
sûrement qu'un dépôt. En photonique quantique la logique du terrain est **inverse** : PsiQuantum,
Xanadu, Quandela, Photonic et les grands laboratoires déposent massivement. S'y ajoute que l'effet
technique y est **physique**, donc l'art. 52 CBE ne tue rien d'avance.

**Ce qu'il faut dire d'emblée, et sans le contourner.** Je n'ai aucune capacité expérimentale.
Les problèmes ci-dessous sont **lus dans la littérature**, avec leurs chiffres et leurs sources.
Les transposer en invention demandera un physicien — pas une recherche documentaire. Toute
prétention contraire serait la faute que ce projet documente depuis huit jours.

Chiffres relevés le 2026-09-28. Sources : littérature publiée, non les registres — ceux-ci restent
inatteignables depuis cette session.

---

## P-15 — La perte de photons est LE problème, et il n'est pas résolu

**Source** Bartolucci et coll., *Fusion-based quantum computation*, Nature Communications, 2023 ;
et la littérature qui en découle.

La perte de photons est nommée, dans chaque article lu, comme **le mode de défaillance dominant**
de la photonique. Un type-II fusion demande deux détections : si l'un des deux photons est perdu,
**les deux résultats de mesure sont effacés** — et l'effacement est signalé, mais on ne sait pas
lequel des deux qubits a été perdu, donc **les voisinages des deux** doivent être retirés du graphe.

Chiffres du seuil de perte par photon (LPPT), tels que publiés :

| Configuration | LPPT |
|---|---|
| Fusion boostée, sans encodage | **0,79 %** |
| État ressource 6-ring encodé {2,2} Shor, base d'échec randomisée | **2,7 %** |
| Avec adaptativité locale | **5,7 %** |
| Avec adaptativité par exposition | **7,5 %** |
| Réseau « loopy diamond », complexe cuboctaédrique encodé {2,2} | **9,0 %** |
| 6-ring encodé {7,4} | **17,4 %** |

Limites fondamentales publiées : **29,3 %** dans le cas non adaptatif classique, **38,2 %**
(≈ (3−√5)/2) en tenant compte de l'information non-stabilisatrice encore disponible sous perte —
les *scraps* —, et **50 %** dans le cas adaptatif avec mesures à un photon.

**Le défaut nommé :** les architectures exigeant une efficacité photonique supérieure à 97 %
sont décrites comme *« une perspective redoutable pour les dispositifs actuels »*.

## P-16 — Booster la fusion dégrade la tolérance à la perte : un compromis, pas un progrès

**Source** la même littérature, et c'est le défaut le plus intéressant du carnet.

Une fusion entre deux qubits en rail double échoue intrinsèquement une fois sur deux. On peut
abaisser cette probabilité en **boostant** avec des états auxiliaires : p_fail = 1/2ⁿ s'obtient
avec 2n−2 photons supplémentaires.

Mais chaque photon ajouté est un photon qui peut être perdu. Les auteurs l'écrivent sans détour :
*« booster la probabilité de succès avec des photons auxiliaires augmente le taux d'effacements et
finit par nuire à la tolérance à la perte »*. Et plus net encore : *« booster ajoute des photons
pour des améliorations modestes des probabilités de succès, et n'a aucune tolérance intrinsèque à
la perte »*.

**C'est un compromis dur, énoncé comme tel, et personne ne le résout — on le contourne** par
l'encodage et l'adaptativité, qui ont leurs propres coûts.

## P-17 — Les états ressources de grande taille sont difficiles à fabriquer

**Source** la littérature sur les émetteurs quantiques, dont arXiv:2410.06784 et arXiv:2304.03796.

Les seuils de perte élevés — au-delà de 10 % — s'obtiennent avec des états ressources décrits comme
*« complexes et difficiles à générer, exigeant plusieurs émetteurs quantiques et des portes
probabilistes »*. Les sources par conversion paramétrique descendante ne produisent des états à peu
de photons **qu'avec une faible probabilité**.

Autre défaut nommé : les photons voyagent à vitesse immense, ce qui **impose de longues lignes à
retard** pour implémenter la rétroaction conditionnelle.

Et la distinguabilité partielle des photons issus d'émetteurs différents limite l'interférence de
Hong-Ou-Mandel nécessaire à la fusion : pour une fusion {XX, ZZ}, elle induit une erreur Z au taux
**(1−V)/4**, où V est la visibilité du creux de HOM.

## P-18 — Six cents réseaux de fusion, et pas de bonne métrique pour les comparer

**Source** arXiv:2506.11975, *Comparison of schemes for highly loss tolerant photonic FBQC*.

Le nombre de réseaux de fusion possibles a **explosé** : les auteurs rapportent que la construction
par complexe de fusion a produit *« plus de six cents instances de réseaux de fusion identifiés »*,
et que tout réseau encodé Shor est automatiquement un complexe de fusion à géométrie modifiée.

Face à quoi ils écrivent un besoin **explicite et non satisfait** :

> *« Des métriques améliorées de coût en ressources seraient un outil précieux pour comparer les
> protocoles FBQC sans avoir à tenir compte des erreurs physiques dans toute leur complexité. »*

Et ils expliquent pourquoi compter les photons ne suffit pas : deux états ressources de même nombre
de qubits peuvent demander des nombres très différents d'états GHZ à trois photons pour être
préparés, et ces nombres dépendent fortement des méthodes de préparation supposées. Ils donnent un
cas concret : un état ressource à **32 qubits** est **moins coûteux** à préparer, et a un **seuil
plus élevé**, que l'état 6-ring encodé {2,2} à 24 qubits.

**C'est le seul problème de ce carnet qui soit de nature calculatoire et non expérimentale.** Il est
énoncé comme un besoin ouvert, par des auteurs de PsiQuantum, et il ne demande pas de laboratoire.

## P-19 — Les erreurs induites par les mesures de fusion n'avaient pas d'analyse formelle

**Source** arXiv:2409.13541.

Les conditions de *flow* — qui décrivent quand les corrections de Pauli rendent un calcul
déterministe — étaient bien comprises pour les **mesures à un qubit sur un état de graphe fixe**,
mais *« n'avaient pas été étudiées dans le cadre photonique fondé sur la fusion »*, où les mesures
sont à plusieurs qubits et où la préparation et la mesure de l'état de graphe sont **entremêlées**.

Les auteurs présentent ce travail comme *« la première analyse formelle des erreurs induites par
les mesures de fusion photoniques »*. Un domaine dont l'analyse formelle date de 2024 est un
domaine jeune.

---

## Ce qui n'est pas fait, et qu'il ne faut pas croire fait

- **Aucune recherche d'antériorité** sur aucun de ces cinq problèmes. Le registre des croisements
  interdit de parler de candidat avant.
- **Aucune recherche par codes CPC.** Le domaine relève principalement de **G06N 10/** (calcul
  quantique) et **H04B 10/70** (communication quantique). Registres inatteignables.
- **Aucune vérification des chiffres à la source primaire.** Ils sont lus dans les articles cités,
  qui se citent entre eux. PLAUSIBLE, confiance MODÉRÉE. Un seul chiffre faux invaliderait un
  raisonnement entier.
- **Aucune compétence expérimentale ici.** P-15, P-16, P-17 et P-19 demandent un physicien. P-18
  est le seul qui ne demande qu'un ordinateur — et c'est pour ça qu'il est le seul par lequel
  commencer.

## Les briques du domaine, et ce qu'elles permettent vraiment

Huit briques sont en sas, toutes permissives après lecture des fichiers. Trois comptent pour P-18 :

- `quantumlib/Stim` (Apache-2.0) — simulation de circuits stabilisateurs à haute performance, et
  conversion d'un circuit bruité en **modèle d'erreur de détecteurs**, qui sert à configurer les
  décodeurs. C'est l'outil de référence.
- `graphiq-dev/graphiq` (Apache-2.0) — conception **inverse** : trouver le circuit qui produit un
  état cible, avec modèles de bruit et de perte optique, qubits émetteurs et photoniques.
- `quantinuum-dev/optyx` (Apache-2.0) — architectures hybrides qubit-photon en ZX, canaux avec
  perte, mesures héraldées, et **il modélise explicitement la fusion de type II et la
  distinguabilité partielle** via des états internes.

**Ces trois briques permettent de travailler P-18 sans laboratoire.** C'est un fait, pas une
promesse : elles simulent, elles ne mesurent pas. Ce qu'on pourrait en tirer reste à chercher, et
la recherche d'antériorité passe avant.

---

*Un carnet ne contient jamais de solution. Dès qu'il propose, il contamine le croisement.*

---

## AJOUT DU 2026-09-28, 21h15 — P-18 : antériorité FAITE, et le problème est fermé

**Ajout, pas réécriture.** Ce qui est au-dessus reste tel qu'écrit à 16h30, y compris ce qui est
maintenant contredit — c'est la règle du carnet et elle vaut plus que mon confort.

### Ce qui est corrigé dans l'en-tête de ce carnet

L'en-tête dit, comme justification du domaine : « en photonique quantique la logique du terrain est
**inverse** : PsiQuantum, Xanadu, Quandela, Photonic et les grands laboratoires déposent
massivement ». **Faux par moitié.** Ils déposent *et* ils publient, et sur `P-18` précisément la
même équipe a fait les deux. Fiche `E-36`.

### Ce que la recherche a trouvé sur P-18

`X-06` au registre des croisements. Trois causes de mort, indépendantes :

1. **OptGraphState** — Lee & Jeong, Quantum 7, 1212 (2023), **MIT**, dépôt
   `seokhyung-lee/OptGraphState` : calcule le coût en ressources d'un état de graphe généré par
   fusions de type II, **quantifié par le nombre moyen d'états ressources de base à trois qubits
   requis**. C'est la métrique demandée, publiée en 2023. Et arXiv:2506.11975 — l'article qui énonce
   le besoin — **la cite en référence [22]** et écrit de son propre heuristique : « une optimisation
   similaire a été présentée dans [22] ».
2. **US12596949B2** (SNU R&DB Foundation, mêmes auteurs), délivré le **2026-04-07**, en vigueur
   jusqu'en 2044 : revendique « performing a resource optimization algorithm for the combination
   graph », avec un coût par arête `M_e = 2(1−η)^(−2)(M_v1 + M_v2)` où **η est le taux de perte**.
   La version « améliorée » que P-18 appelle est donc **déjà brevetée, en mieux** que ce que P-18
   demande.
3. **Art. 52(2) CBE.** Une métrique calculée sans effet physique est une méthode mathématique, donc
   exclue. Et c'est structurel : ce carnet dit que P-18 est **le seul problème qui ne demande qu'un
   ordinateur** — c'est pour cela qu'il est **le seul sur lequel l'art. 52 mord**.

### La tenaille, et il faut la regarder en face

|  | Effet physique (passe l'art. 52) | Faisable sans laboratoire |
|---|---|---|
| P-15 perte de photons | oui | **non** |
| P-16 compromis du boosting | oui | **non** |
| P-17 états ressources | oui | **non** |
| P-19 erreurs de mesure de fusion | oui | **non** |
| P-18 métrique de coût | **non** | oui |

**Aucune case du carnet n'a les deux.** Ce n'est pas un hasard de sélection : c'est la même tenaille
que dans le logiciel, déplacée d'un cran. Ce qu'on peut faire depuis un bureau, l'art. 52 l'exclut ;
ce que l'art. 52 admet demande un laboratoire.

US12596949B2 montre par où l'on sort : SNU a obtenu la délivrance parce que l'algorithme est
revendiqué **à l'intérieur** d'un procédé qui finit par « measuring at least one central qubit of
the RHG lattice ». La métrique passe l'art. 52 en étant attachée à un dispositif. **Pour breveter du
calcul, il faut de la matière.**

### Ce que le carnet garde, et ce qu'il perd

**Perdu :** P-18 comme piste de brevet, définitivement. Et la justification du virage quantique,
telle qu'écrite.

**Gardé :** les cinq problèmes restent des problèmes réels, décrits par leurs déposants, avec leurs
chiffres. P-15, P-16, P-17 et P-19 ne sont pas touchés par cette recherche — **leur antériorité n'a
pas été cherchée**, et ils restent hors de portée sans physicien. Les briques du domaine restent
utilisables, et deux se sont ajoutées le jour même : `B-21 OptGraphState` (MIT) et
`B-22 graphix` (Apache-2.0).

**À trancher par Chaima, et rien ne change sans elle.** Le carnet 4 avait été ouvert parce que P-18
était « le seul par lequel commencer ». Il est fermé. Les quatre autres demandent un physicien.
La question n'est donc plus quel problème, mais **avec qui** — ou bien s'il faut arrêter de chercher
des brevets et garder du dispositif ce qui rapporte vraiment, c'est-à-dire les briques vérifiées et
la liberté d'exploitation.

---

## AJOUT DU 2026-10-01, 10h15 — P-16 : antériorité faite, et trois corrections à ce carnet

**Ajout, pas réécriture.** Ce qui est écrit au-dessus de P-16 reste tel quel, y compris ce qui est
maintenant corrigé. Entrée `S-01` au registre des solutions.

### Correction 1 — il y a quatre portes, pas deux

Le carnet écrit : *« c'est un compromis dur, énoncé comme tel, et personne ne le résout — on le
contourne par l'encodage et l'adaptativité »*. **Incomplet, et c'est l'incomplétude qui comptait.**

Les sorties publiées du compromis sont **quatre** :

1. **les photons auxiliaires** — Grice 2011, Ewert & van Loock 2014 (3/4 avec quatre photons non
   intriqués), optimalité étudiée par Olivo & Grosshans 2018 ;
2. **la redondance de code** — le « code-boosting », déjà dans la proposition FBQC d'origine ;
3. **le traitement gaussien actif**, c'est-à-dire la **compression** — Zaidi & van Loock, PRL 110,
   260501 (2013), dont le titre est *« Beating the one-half limit of ancilla-free linear optics Bell
   measurements »*. Elle coûte des compresseurs et **pas des photons** ;
4. **changer la mesure elle-même** — Pankovich et coll., ORCA Computing, PRL 133, 050604 (2024) :
   projection en base GHZ au lieu de fusion à deux qubits, avec des seuils de perte par photon
   élevés.

Le carnet nommait les deux premières et présentait le reste comme absent. La troisième est
précisément la direction que j'allais chercher, et elle a **treize ans**.

### Correction 2 — la question n'était pas ouverte, elle était close par un théorème

La question que j'avais inscrite dans la fiche de `physicien-fusion-et-boosting` — *existe-t-il un
gain qui ne se paie pas en photons exposés ?* — n'est pas une question de recherche. Elle est
**bornée** : Calsamiglia et Lütkenhaus établissent que la discrimination non ambiguë de quatre états
de Bell en optique linéaire ne dépasse pas 1/2, que les modes auxiliaires **dans le vide**
n'améliorent rien, et qu'une mesure déterministe est **impossible avec n'importe quel état
auxiliaire**, même avec rétroaction.

**Une question dont la réponse est un théorème n'est pas une direction de recherche.** Et la seule
porte sans photons, en rail double — l'encodage qu'emploie réellement la FBQC —, est la **moins
bonne** des quatre : 0,596 par compression (Phys. Rev. A 99, 032302, qui établit que le 0,643
souvent cité est un point expérimentalement inatteignable) contre 0,625 avec deux photons
auxiliaires. arXiv:2412.07353 l'écrit : en dimension deux, la compression ne bat même pas la mesure
de Bell la plus simple avec photons auxiliaires.

### Correction 3 — une citation présentée comme générale, et c'est E-36 encore

Le carnet cite : *« booster ajoute des photons pour des améliorations modestes des probabilités de
succès, et n'a aucune tolérance intrinsèque à la perte »*. La citation est exacte. Sa portée, non.

Une **expérience** publiée dans npj Quantum Information le 2025-03-08 mesure une mesure de Bell
boostée par paire auxiliaire intriquée à 69,3 ± 0,3 %, et rapporte un seuil de perte par photon
passant de 0,45 % à **1,4 %** — *« un triplement de la robustesse à la perte »*, avec en plus des
taux d'erreur logique nettement réduits même pour de petits réseaux de fusion.

**Les deux énoncés ne se contredisent pas** : booster n'apporte pas de tolérance à la perte *par
lui-même* — c'est l'encodage qui la donne — tout en relevant le seuil dans le régime mesuré. Et les
deux chiffres ne se comparent pas : modèles d'erreur différents, réseaux différents. **Il ne faut
surtout pas les additionner.**

Ce qui est fautif, c'est de ma part : j'ai cité la phrase pessimiste seule, sans la mesure qui la
nuance, et je l'ai présentée comme un constat de domaine. C'est **la famille de la fiche `E-36`** —
une phrase lue, une portée non mesurée. Pas de fiche nouvelle : `E-36` couvre déjà exactement ce
signal, et en ouvrir une seconde pour le même motif diluerait la première.

### Ce que le dispositif a bien fait, et il faut le dire aussi

La contre-mesure d'`E-36` prescrivait : *« quand un article dit qu'un outil manque, lis les
références de la phrase avant de la croire »*. Appliquée. L'antériorité est passée **avant** toute
proposition, et la piste est morte **en minutes, sans qu'aucun secret soit créé** — donc l'entrée
`S-01` peut être écrite en clair, puisqu'il n'y a rien de nous à protéger.

C'est le premier cas où le dispositif tue une mauvaise direction avant qu'elle coûte quelque chose.
Les six croisements précédents coûtaient des heures ou des jours chacun.

### P-16 : état final

**Fermé comme piste de brevet.** Il reste un problème réel et correctement décrit — le compromis
existe, les auteurs l'énoncent — mais ses quatre sorties sont occupées, la plus récente depuis douze
jours (*Single-photon-boosted type-I fusion gates*, Phys. Rev. Applied, 2026-09-16).

**Deux problèmes du carnet restent intouchés par cette recherche :** `P-17` dans ses volets
**dispositif** — une ligne à retard qui perd moins, un mécanisme qui **tolère** une visibilité HOM
basse au lieu de l'exiger haute, où l'erreur Z vaut exactement `(1 − V)/4` — et `P-19`. `P-15` est à
vérifier en premier, parce que arXiv:2606.29432 recycle des « échecs de mesure structurés », ce qui
est voisin des *scraps* sans leur être identique.

---

## AJOUT DU 2026-10-01, 11h00 — P-15 : le volet *scraps* est pré-empté sans être divulgué

**Ajout, pas réécriture.** Entrée `S-02` au registre des solutions. Et `P-15` n'est **pas** clos en
entier : seul son volet scraps meurt ici.

### Ce que le carnet disait, et ce qu'il omettait

Le carnet écrit, à juste titre, que les scraps font passer la limite de 29,3 % à 38,2 % (≈ (3−√5)/2)
« en tenant compte de l'information non-stabilisatrice encore disponible sous perte ».

Il omettait **qui** l'a montré, et dans quoi. La phrase exacte d'arXiv:2506.11975 est :
*« **in [19] we show** even without adaptivity an LPPT of 38.2 % […] can be achieved by accounting
for the non-stabilizer information (known as scraps) »*. Et la référence [19] du même article est,
intégralement : **« PsiQuantum, Manuscript in preparation. »**

Les deux autres limites, elles, sont publiées et attribuées : **29,3 %** non adaptatif par Lee et
coll. (2015), Ewert et coll. (2016), Lee et coll. (2019) et Hilaire et coll. (2023) ; **50 %**
adaptatif à mesures mono-photon.

### La huitième cause de mort, et elle est pire que les sept précédentes

Ni « déjà publié », ni « déjà breveté » : **annoncé et non divulgué.**

- Pas d'enseignement habilitant public : on sait que le résultat existe, pas comment il s'obtient.
  Rien sur quoi construire.
- Et la partie qui le détient dépose massivement. Annoncer un résultat en réservant le détail
  habilitant à un manuscrit en préparation est la signature habituelle d'une demande déjà déposée.
  **NON VÉRIFIÉ** — aucun numéro de demande en main. PLAUSIBLE, confiance MODÉRÉE.

### Une suspicion levée, et il faut le dire

J'avais écrit ce matin, à 10h15, qu'arXiv:2606.29432 — qui « recycle des échecs de mesure
structurés » — pouvait recouvrir les scraps. **Non.** Ce papier recycle le secteur d'**échec de
fusion** d'une porte par paires en dimension d, par compression gaussienne. Les scraps concernent
l'information résiduelle après **perte de photon**. Secteurs différents, mécanismes différents.

C'était une suspicion, elle était signalée comme telle, et elle tombe. C'est le fonctionnement
normal : une suspicion vérifiée en une heure vaut mieux qu'une certitude non vérifiée.

### La leçon, et elle inverse celle du 2026-09-28

Le 2026-09-28, sur `P-18`, j'ai pris **un aveu de trou pour un trou** : les auteurs écrivaient qu'il
leur manquait une métrique, et l'outil était en référence [22] du même paragraphe.

Ici c'est l'inverse exact : les auteurs écrivent qu'ils **ont** le résultat, et la référence est un
manuscrit en préparation. **Dans les deux cas, la phrase du corps de texte ne dit pas ce qu'elle a
l'air de dire, et c'est la référence qui le dit.**

Règle qui en sort, et elle complète la contre-mesure d'`E-36` : **dans ce domaine, une référence est
un acte juridique autant qu'un renvoi bibliographique.** « Nous montrons dans [réf] » où [réf] est
un manuscrit en préparation se traite comme un dépôt, pas comme une lacune.

### Ce qui reste de P-15, et n'est pas enterré avec

Non attribué, non cherché : l'effacement qui retire les voisinages des **deux** qubits pour un seul
photon perdu, et l'exigence de plus de 97 % d'efficacité photonique que ses propres auteurs
qualifient de « perspective redoutable ». Aucune antériorité là-dessus.

### État du carnet 4 au 2026-10-01, 11h00

| problème | état | pourquoi |
|---|---|---|
| `P-15` scraps | **MORT** | pré-empté sans divulgation par PsiQuantum (`S-02`) |
| `P-15` reste | ouvert, non cherché | effacement double voisinage, seuil des 97 % |
| `P-16` | **FERMÉ** | borné par un théorème, quatre sorties occupées (`S-01`) |
| `P-17` métrique de coût | **MORT** | `X-06`, le 2026-09-28 |
| `P-17` dispositif | **ouvert, et c'est le meilleur restant** | ligne à retard, tolérance à une visibilité HOM basse où l'erreur Z vaut `(1 − V)/4` |
| `P-18` | **MORT** | libre publié MIT + brevet jusqu'en 2044 + art. 52 CBE |
| `P-19` | ouvert, non cherché | analyse formelle née en 2024 |

**Deux cibles restent, et une seule est bonne.** `P-17` volet dispositif : effet physique — donc
hors de l'exclusion de l'art. 52 CBE —, relation exacte publiée et donc calculable, et rien de ce
qui a été lu aujourd'hui ne la touche.
