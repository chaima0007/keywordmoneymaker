# Registre des croisements

**Trace uniquement. Le fond est au coffre Drive.** Ce dépôt est public, et il n'y a pas de délai
de grâce en Europe : un croisement écrit ici serait un croisement perdu.

Chaque ligne dit qu'un croisement existe, d'où il vient, et où il en est. Jamais ce qu'il contient.

Tenu depuis le 2026-09-19. Ajout uniquement.

---

## X-01

| | |
|---|---|
| **Ouvert le** | 2026-09-19 |
| **Problèmes croisés** | `P-03` et `P-01` (carnet 1, capteurs) × `P-11` (carnet 3, procédés) |
| **Nature du transfert** | Un enseignement de métrologie transposé vers un procédé industriel d'un tout autre secteur |
| **Enseignements sources libres ?** | Affichés expirés côté carnet 1 — PLAUSIBLE, non confirmé, registre inatteignable. Côté carnet 3, statut **non établi du tout** |
| **Recherche d'antériorité** | **NON FAITE** |
| **Contredit par** | personne encore |
| **État** | HYPOTHÈSE. Ne vaut rien tant que la ligne précédente dit NON FAITE |
| **Où est le fond** | Coffre Drive, document daté du 2026-09-19 |

**Reste ouvert :** tout. L'antériorité, les statuts, la lecture des revendications, et la question
qui décidera — l'effet technique est-il défendable, ou le transfert est-il banal.

---

## Règle de tenue

Un croisement passe de HYPOTHÈSE à CANDIDAT quand, et seulement quand :
1. la recherche d'antériorité est faite et ne l'a pas tué ;
2. `contradicteur` a cherché pourquoi le transfert est banal, et a échoué ;
3. les enseignements sources sont confirmés libres sur registre, pas sur affichage.

Aucun croisement de ce registre n'a franchi ces trois portes. Écrire « candidat » avant serait
la faute la plus coûteuse du dispositif : on s'attache, puis on paie, puis on est refusé.

---

## VERDICT X-01 — MORT le 2026-09-19, quatre heures après son ouverture

**Tué par la recherche d'antériorité, exactement à l'étape où le registre disait qu'il pouvait
mourir.** Le croisement n'a jamais été traité comme un candidat, donc rien n'est perdu.

Ce qui le tue, par ordre de gravité :

- **US12607598**, publié 2026-04-21 — calibration d'un capteur en fonctionnement par analyse des
  valeurs brutes enregistrées : recherche des minima de charge, sélection de ces points comme
  valeurs de référence avec une concentration attendue, correction de la fonction de conversion.
  Le brevet donne l'exemple de la station d'épuration où l'analyte est quasi nul entre minuit et
  quatre heures. Et son contrôle de plausibilité cite explicitement le point où la concentration
  doit être nulle : *« during a cleaning phase of the sensor, for example, during CIP (cleaning in
  process) »*. C'est le transfert supposé, publié il y a cinq mois.
- **US6458213**, publié 2002 — après nettoyage, la cellule est rincée avec un liquide de référence ;
  si la mesure ne donne pas 0,0 %, *« the sensor system readjusts automatically to this value by
  offset correction »*. La même idée, il y a vingt-quatre ans.
- **US8970829**, publié 2015 — détection d'encrassement par écart à une valeur de référence mesurée
  **à l'état propre en début de cycle produit**, avec une variante à deux capteurs dont l'un est
  placé là où l'encrassement ne se forme pas, servant de référence continue.

**Ce que ça dit du croisement.** L'objection que `contradicteur` aurait soulevée — « utiliser un
état connu récurrent comme référence de zéro est ancien et général, un examinateur le jugera évident
dès qu'on constate que le CIP existe » — était écrite dans le document du coffre **avant** la
recherche. Elle était juste. L'antériorité n'a fait que la confirmer par des numéros.

**Ce que ça dit de la méthode.** Quatre heures entre l'ouverture et la mort. C'est le résultat
recherché : un croisement doit mourir vite et pas cher. Le coût réel d'un dispositif de veille ne
se mesure pas au nombre de candidats qu'il produit, mais à la vitesse à laquelle il tue les mauvais.

**Ce qui reste utilisable.** Les quatorze problèmes des trois carnets ne sont pas touchés : ils
restent des problèmes décrits par des déposants, indépendamment de ce croisement-ci. Et une leçon
transférable : dans les trois carnets, **la « référence connue récurrente » est un terrain déjà
dense**. Tout croisement futur qui repose dessus part avec un handicap, et doit être soumis à
l'antériorité en premier, pas en dernier.

---

## X-02 — ouvert et mort le 2026-09-19, dans la même recherche

**Ouvert** sur un principe du carnet 1, tiré de US5426969 : *« technological limitations are of
secondary importance »* — remplacer la précision de fabrication par un protocole qui annule
l'imperfection en prenant une différence entre deux états.

**Transfert supposé** vers `P-12` (carnet 3) : plutôt que de mesurer le produit à l'intérieur d'un
contenant scellé — ce que le déposant de US9241510 déclare virtuellement impossible, d'où le
sur-traitement de la majorité pour garantir le minimum — appliquer deux conditions connues
différentes et déduire la propriété thermique individuelle du contenant de l'écart entre ses
réponses observables.

**Mort immédiatement.**

- **US9927304**, Philips, publié 2018 — détermination de la température à cœur d'un aliment dans un
  contenant fermé : on **fait varier délibérément la puissance de chauffe** d'un niveau P1 à un
  niveau P2, on mesure la vitesse de variation de température qui en résulte, et on en déduit la
  température à cœur par des relations préétablies. C'est exactement le protocole supposé.
- **US9109960**, Philips, publié 2015 — détermination d'un paramètre d'inertie thermique par
  comparaison de la **vitesse de variation de la puissance fournie** à des valeurs connues, puis
  estimation de la température. Explicitement sans capteur au contact du contenu.
- **US4468135** (1984) et **US7213967** (2007) occupent la variante par objet simulateur calibré.

---

## CE QUE DEUX MORTS LE MÊME JOUR DISENT DE LA MÉTHODE

Et c'est plus important que les deux croisements réunis.

J'ai proposé trois domaines en les présentant comme éloignés : capteurs et signal, énergie et
bâtiment, procédés et agroalimentaire. **Ils ne sont pas éloignés.** Les trois portent sur la
mesure et la conduite de processus thermiques et physiques. C'est un seul super-domaine, avec une
seule communauté d'ingénieurs, une seule littérature, un seul homme du métier.

Conséquence directe, à l'art. 56 CBE : l'argument du domaine éloigné — qui était **toute** la
raison d'ouvrir trois chemins — ne tient pas entre ces trois-là. X-01 transférait de
l'instrumentation vers l'instrumentation. X-02 transférait du chauffage d'aliment vers le
chauffage d'aliment. Aucun des deux n'a jamais eu l'avantage que je lui prêtais.

Ce n'est pas une erreur de recherche, c'est une erreur dans la proposition que j'ai faite à Chaima
le matin même. Elle est inscrite en fiche `E-31`.

**Ce que ça ne remet pas en cause :** le principe du transfert de domaine reste juste, et les
quatorze problèmes des carnets restent valides. C'est le choix des trois domaines qui est à revoir,
pas la méthode.

---

## X-03 — paire VIVANT × STOCKAGE THERMIQUE — forme large MORTE, ligne étroite VIVANTE

**Ouverte le 2026-09-20.** Première paire à **passer le test de distance** : sections CPC distinctes
(A23/C12 contre F28/C09), revues sans recouvrement (cryobiologie contre physique du bâtiment),
formations sans recouvrement, vocabulaire non traduisible (« nucléation extracellulaire »,
« protéine InaZ » contre « surfusion », « capsule »).

**Problème visé** — `P-07` (carnet 2) : le matériau à changement de phase se dilate et fracture le
béton ; la surfusion figure dans la liste de défauts du déposant lui-même.

**Enseignement source** — le domaine du gel biologique ne subit pas la surfusion, il la **règle**.
US4978540 (1990) et US5194269 (1993), tous deux anciens : un agent nucléant permet de congeler à
−5/−30 °C au lieu de −20/−40 °C, en supprimant la surfusion. US11477981 va plus loin et donne une
**méthode de conception** : on choisit la température de nucléation voulue, puis on détermine le
nombre de particules, leur volume et la concentration locale d'agent à partir d'une courbe
d'étalonnage.

### Forme large : MORTE

Les quatre composantes de l'hypothèse sont déjà revendiquées, séparément :

- **US11378345** (2022) — contrôle actif de la cristallisation d'un PCM par **point froid maintenu**
  qui garde l'agent nucléant sous sa température de désactivation, pour une cristallisation
  *« consistent, predictive and selectable »*. Écrit noir sur blanc : *« The use of nucleating
  agents can be optimised by controlling where they are located and how they are contained, i.e.
  in a mesh or porous material. »* C'est le contrôle spatial supposé.
- **US10718573** (2020) — corps absorbant comprimable dans la capsule ; le PCM solidifie de la
  périphérie vers le centre et comprime ce corps. C'est diriger la dilatation vers un vide conçu.
  Cite FR2732453 comme antérieur pour la version sphérique.
- **US9046308** (2015) — volume de base plus volume de dilatation dimensionnés d'avance, et
  solidification en **microzones spatialement distribuées** par structure capillaire, pour éviter
  les poches de fondu emprisonnées qui endommagent le boîtier.
- **US11241733** (2022) — géométrie interne accordée qui pilote les chemins du front de
  solidification, avec vide interne pour la dilatation.

### Ligne étroite : VIVANTE, et non testée

Une chose est absente des quatre : **aucun n'emploie de nucléant biologique, et aucun n'emploie la
méthode de conception quantitative de la cryobiologie.** Le domaine PCM choisit ses nucléants
empiriquement — « un hydrate spécifique » — et les protège par un **point froid actif**, c'est-à-dire
un dispositif thermoélectrique alimenté en permanence. US11378345 décrit lui-même pourquoi :
*« If a PCM has no known sufficient method to ensure consistent nucleation, then that may prevent
its use. »* Toute son architecture existe **parce qu'il leur manque un nucléant fiable sans
protection active**.

La ligne : un stockage thermique à base aqueuse — la glace, précisément le domaine de `P-06` et de
US7827807B2 — dont la température de nucléation serait un **paramètre de conception du matériau**,
fixé par une population calibrée de particules nucléantes, et non un paramètre d'exploitation
maintenu par un appareil sous tension.

**État : HYPOTHÈSE. Recherche d'antériorité NON FAITE.** Le fond est au coffre.

**Ce qui la menace en premier** — et il faut le chercher avant tout le reste : la stabilité d'une
protéine sur des milliers de cycles thermiques. La cryobiologie congèle **une fois**. Un mur en
fait un par jour pendant trente ans. Si la protéine se dénature, la ligne meurt sur la physique et
non sur le droit.

---

## VERDICT X-03 LIGNE ÉTROITE — MORTE le 2026-09-20

Le document d'ouverture disait : vérifier **la physique avant le droit**, parce qu'il est inutile de
savoir si c'est brevetable si ça ne fonctionne pas. Fait dans cet ordre. Résultat inattendu : **la
physique répond oui, et c'est le droit qui tue.**

### La physique tient

- Une étude de durabilité au cyclage donne : *Erwinia ananas* stérilisée aux UV conserve sa capacité
  de rupture de surfusion à environ −1 °C sur **2000 cycles gel-dégel**. *P. syringae* et *E. ananas*
  tiennent une activité constante **jusqu'à environ 150 cycles**, puis dérivent.
- PNAS, octobre 2024 : le mécanisme de dégradation est compris. Les gros agrégats se désassemblent
  en dimères, ce qui abaisse la température de nucléation — mais **aucun nucléateur n'est perdu**, ils
  sont transformés. Et un tampon phosphate salin multiplie par deux cents la population de gros
  agrégats et **protège contre la perte d'activité au cyclage**.
- eLife, 2023 : les multimères résistent à 99 °C pendant dix minutes en ne perdant pas plus de 6 °C
  d'activité, et restent actifs de pH 2 à pH 11.

Autrement dit : le risque physique que je jugeais premier est réel mais **borné et pilotable**.
L'idée était bonne.

### Le droit tue

- **US5770102** (1998), « Ice nucleating-active materials and ice bank system ». Sa propre section
  d'arrière-plan cite les **bactéries à activité nucléante** pour les systèmes de stockage par glace,
  en renvoyant à la publication japonaise **JP 2-44133**, donc **1990**.
- **Yamamoto et coll., 1993** — protéine nucléante de *Xanthomonas campestris* employée dans un
  système de stockage de glace, remontant le point de rupture de surfusion de −5/−8 °C à −1/−3 °C,
  avec la conclusion explicite que la protéine est recommandée comme substance nucléante organique
  inoffensive et reproductible pour ce système. **C'est exactement la ligne étroite, publiée il y a
  trente-trois ans.**
- **US10487252** (2019) — gel de refroidissement aqueux revendiqué comme matériau à changement de
  phase, comprenant cellulose, **protéine nucléante** et biocide, avec les plages de concentration.
  C'est la revendication matériau moderne.

**X-03 est close.** Forme large morte, ligne étroite morte.

---

# CE QUE TROIS CROISEMENTS DISENT, ET IL FAUT L'ÉCRIRE

Trois hypothèses, trois morts, en deux jours. Mais les causes ne sont pas les mêmes, et c'est la
troisième qui est instructive :

| | Cause de la mort | Ce que ça révélait |
|---|---|---|
| X-01 | domaines trop proches | erreur de choix de domaines — `E-31` |
| X-02 | domaines trop proches | même erreur, même journée |
| X-03 | **domaines correctement éloignés, idée juste, déjà faite depuis 1990** | le test de distance fonctionne ; le problème est ailleurs |

**Le test de distance a marché.** X-03 était une vraie invention combinatoire, physiquement fondée,
dans une paire authentiquement éloignée. Elle est morte parce que **quelqu'un l'avait déjà faite,
il y a trente-trois ans**, dans une littérature japonaise que le domaine du bâtiment européen ne lit
pas plus que la cryobiologie.

C'est le constat qui compte : **quand l'idée est bonne, elle a déjà été faite.** Ce n'est pas de la
malchance, c'est la définition d'un domaine technique mûr. Un croisement qui survit à
l'antériorité est, presque par construction, un croisement que personne n'a voulu faire — donc
souvent un croisement sans marché, ou physiquement faux.

Ce que ça ne dit pas : que c'est impossible. Ce que ça dit : que le **taux de réussite est bas**,
que chaque tentative coûte des heures, et qu'il faut compter en dizaines de tentatives, pas en trois.

**À décider par Chaima**, et rien n'est changé sans elle : continuer à ce rythme en acceptant le
taux, ou réorienter le dispositif vers ce qu'il a produit de plus utile en deux jours — la liberté
d'exploitation. Les deux brevets tombés du 19/09 valent immédiatement quelque chose pour son
produit. Aucun croisement n'a rien valu.


---

## X-04 — la couche de contradiction — MORTE le 2026-09-28, et la cause est nouvelle

**Ouverte le 2026-09-20** sur le trou commun aux douze briques du registre : toutes vérifient que la
tâche s'est TERMINÉE, aucune que la conclusion est JUSTE. Trois questions avaient été posées dans
cet ordre — est-ce déjà fait, l'effet technique tient-il, est-ce que ça se vend — et **la première
est restée sans réponse pendant huit jours.** C'est ma faute : j'ai construit l'outillage du sas au
lieu de traiter la question que j'avais moi-même écrite.

**Réponse : c'est fait, cinq fois.**

- **US12676749** (2026-07-07) — porte d'exécution fail-closed avant inférence, verdict signé par
  quorum, registre d'arbitrage immuable, verrouillage persistant.
- **draft-krausz-verification-state-01** (IETF) — contraintes `verification.*`, champ
  `v_adversarial_result`, et table de vérité où `not_checked` donne **halt** : « un état adverse non
  sondé n'est pas équivalent à résilient ; l'incertitude DOIT arrêter ».
- **Chauhan, Ratification by Re-execution** (2026-01) — le vérificateur exécute lui-même et publie
  son verdict AVANT de lire l'auto-vérification de l'autre. Journaux unidirectionnels, un auteur
  par fichier.
- **Surisetti, DCTP** (2026-07) — verrouillage par graphe de dépendances, interface strictement
  propositionnelle, conservation du candidat perdant. Cite WO2021084510A1 (2021).
- Une discussion publique de praticiens posant le jeton de veto, la dette de preuve à délai et le
  registre de dissension qui survit à l'exécution.

### LA CAUSE NOUVELLE — la publication défensive

Le premier résultat n'est pas un brevet. C'est un dépôt GitHub, `verdict-gated-merge-deploy-train`,
dont l'en-tête porte en gras **« Public prior art »** et qui contient de son propre aveu « une
divulgation habilitante d'environ cinq mille mots avec des revendications ».

**Ce dépôt n'existe pas pour déposer. Il existe pour empêcher de déposer.**

C'est une publication défensive : rédigée comme une demande de brevet, publiée gratuitement, pour
détruire la nouveauté de tout dépôt ultérieur. La nouveauté est détruite par toute divulgation
antérieure — y compris une divulgation faite exprès pour ça.

### CE QUE QUATRE MORTS DISENT MAINTENANT

| | Cause | Ce que ça révélait |
|---|---|---|
| X-01 | domaines trop proches | erreur de choix — `E-31` |
| X-02 | domaines trop proches | même erreur, même journée |
| X-03 | idée juste, faite depuis 1990 | domaine mûr |
| X-04 | **domaine rendu inbrevetable en temps réel** | **structure du terrain, pas malchance** |

Les trois premières causes étaient corrigibles : mieux choisir les domaines, chercher plus tôt
l'antériorité. La quatrième ne l'est pas. Dans l'espace des agents autonomes, les mécanismes sont
publiés en semaines, les normalisateurs publient en brouillons qui font art antérieur, et une
partie des acteurs publie délibérément pour bloquer.

**Chercher un brevet logiciel dans ce domaine depuis un bureau a un rendement proche de zéro.**

### CE QUI SURVIT, ET QUI N'EST PAS UN CANDIDAT

Aucun des cinq travaux ne couvre le **sas de provenance et de licence** construit ici : lire les
fichiers et non l'étiquette, attraper la licence scindée code/poids, traiter `NOTICE` comme
attribution, distinguer « ne conclut pas » de « refusé », rester neutre en origine tout en séparant
le contrôle de sanctions. Autre domaine — chaîne d'approvisionnement logicielle, pas vérification
d'agents.

**État : PISTE NON OUVERTE.** L'espace SBOM, SPDX et analyse de licences est industriel et ancien.
Aucune antériorité cherchée. L'inscrire comme candidat sans l'avoir testée serait précisément la
faute que ce registre existe pour empêcher.


---

## X-05 — le sas de provenance et de licence — MORT le 2026-09-28

Chaima : « va tester ». Testé. La piste inscrite comme NON OUVERTE le 28/09 au matin est morte le
même jour, et il est bon qu'elle n'ait jamais été appelée candidate.

**Tout ce que le sas fait est publié, élément par élément :**

- **US11816190** (2023) — analyse des composants libres d'un produit, catégorisation en copyleft
  fort / faible / permissif, et un jeu de règles où un composant est **REJETÉ** sur copyleft fort,
  approuvé sous condition sinon, avec un attribut final par composant. C'est la porte d'admission
  avec règles de licence, revendiquée.
- **`osslili`** (2025, MIT) — lit les **fichiers** de licence, cascade à quatre niveaux, et écrit
  ceci : *« osslili n'affirme pas une licence qu'il ne peut pas étayer — une identification qu'il
  ne peut pas soutenir est abandonnée plutôt que devinée »*. C'est mot pour mot mon « ne conclut
  pas ». Et aussi : *« les licences trouvées dans des fichiers de notices tierces sont catégorisées
  séparément, pour qu'un THIRD_PARTY_NOTICES vendorisé ne fasse pas passer un projet permissif pour
  du copyleft »*. C'est mot pour mot mon traitement de `NOTICE`.
- **`audit-license-provenance.py`** (DeusData) — audit d'identité **octet par octet** de chaque
  licence vendorisée contre l'amont, **au commit épinglé**, avec verdicts IDENTICAL,
  IDENTICAL@PINNED, DIFFERS. C'est mon épinglage, en plus strict.
- **Une page publique sur les licences de synthèse vocale** documente le motif code/poids comme
  connaissance courante, en nommant les modèles concernés et en ajoutant des cas que je n'avais pas
  vus : licences qui portent sur la **sortie** générée, poids d'encodeur retenus, licences
  **empilées** à trois niveaux, et relicenciement (Piper, MIT vers GPL-3.0).

**Verdict : rien à breveter.** Et comme pour X-04, l'essentiel du corpus est **publié, pas
breveté** — deux des quatre sources sont du code libre et une page de documentation.

### CE QUE LE SAS A FAIT LE JOUR MÊME, ET QUI N'A RIEN À VOIR AVEC UN BREVET

Huit briques quantiques entrées au registre. Le contrôle de licence a trouvé, **dans le sens
favorable cette fois** :

- **Quandela/Perceval** — la fiche du dépôt affiche « Other ». Le fichier LICENSE dit **MIT**.
- **munich-quantum-toolkit/qecc** — la fiche n'affiche **aucune** licence. Le fichier dit **MIT**,
  avec 169 déclarations SPDX concordantes.

Lire les fichiers ne sert donc pas qu'à attraper des pièges : ça **débloque** des briques que
l'étiquette faisait éviter. Deux outils que la méfiance aurait écartés sont utilisables.

**C'est la vraie valeur du sas, et elle n'est pas brevetable : elle est opérationnelle.**

### CINQ MORTS, ET LE MOTIF EST STABLE

| | Cause |
|---|---|
| X-01, X-02 | domaines trop proches — ma faute, `E-31` |
| X-03 | idée juste, faite depuis 1990 |
| X-04 | domaine rendu inbrevetable **en temps réel** par publication défensive |
| X-05 | **outil déjà publié, en code libre et en documentation** |

Quatre fois sur cinq, ce qui nous bloque n'est pas un brevet concurrent : c'est du **libre publié**.
Dans le logiciel, les gens ne brevettent pas, ils publient — et publier détruit la nouveauté aussi
sûrement qu'un dépôt.

**C'est la raison qui rend le virage quantique sensé, et pas seulement différent.** En photonique
quantique, PsiQuantum, Xanadu, Quandela et Photonic déposent massivement : le domaine se protège
par brevet, pas par publication. La logique du terrain y est inverse.


---

## X-06 — la métrique de coût des réseaux de fusion — OUVERTE ET MORTE le 2026-09-28

Chaima : « vasy ». Ouverte sur `P-18`, le seul problème du carnet 4 qui ne demande qu'un ordinateur.

**Ce que X-06 n'est PAS, et il faut le dire avant de commencer.** Ce n'est pas un croisement de
domaines. Les cinq premiers transféraient un enseignement d'un domaine vers un autre, et le test de
distance d'`E-31` portait sur la **paire**. X-06 n'a pas de paire : c'est une attaque frontale sur un
besoin ouvert énoncé par les auteurs eux-mêmes. Le test de distance ne s'applique donc pas, et je ne
vais pas en fabriquer un pour faire joli.

En échange, X-06 partait avec un handicap que les cinq autres n'avaient pas, et je ne l'ai pas pesé :
**quand des auteurs écrivent publiquement qu'il leur manque un outil, ils ont déjà cherché — et ils
citent ce qu'ils ont trouvé.**

Ils citaient. Référence **[22]**.

### Mort n°1 — le besoin est comblé par du libre publié, que l'article du besoin cite lui-même

**OptGraphState** — Lee & Jeong, *Graph-theoretical optimization of fusion-based graph state
generation*, **Quantum 7, 1212 (2023)**, arXiv:2304.11988 (v1 24/04/2023). Dépôt
`seokhyung-lee/OptGraphState`, **MIT lue dans le fichier** au commit `4f7c563634cf`, créé le
2023-04-03. Le paquet fait, d'après sa propre documentation :

- trouver une méthode efficace en ressources pour générer un état de graphe donné **par fusions de
  type II à partir d'états ressources de base à trois qubits** ;
- **« calculer le coût en ressources correspondant, quantifié par le nombre moyen d'états ressources
  de base requis ou de tentatives de fusion »** ;
- calculer la probabilité de succès lorsque le nombre d'états ressources fournis est limité ;
- construire et visualiser le **réseau de fusion** et l'ordre des fusions.

C'est la métrique que `P-18` appelle, publiée il y a trois ans, en MIT. Et le détail qui tue : la
référence **[22]** de arXiv:2506.11975 — l'article de PsiQuantum qui énonce le besoin — **est ce
papier**, et à propos de son propre heuristique de coût l'article écrit : *« Une optimisation
similaire a été présentée dans [22]. »*

**Les auteurs du besoin ouvert citent l'outil qui le comble.** Le trou que j'ai lu dans leur phrase
n'était pas un trou dans l'état de l'art — c'était un trou dans *leur* annexe, qu'ils signalent
eux-mêmes en note.

### Mort n°2 — la version améliorée est BREVETÉE, par la même équipe, et le brevet est en vigueur

**US12596949B2** — *Method and apparatus for linear optical quantum computing*. Titulaire **SNU
R&DB Foundation** (Seoul National University). Inventeurs **Hyunseok Jeong, Seok-Hyung Lee, Yong
Siah Teo, Srikrishna Omkar** — les deux premiers sont les auteurs d'OptGraphState. Priorité KR
10-2022-0120561 du **2022-09-23**, demande US 18/075,327 du 2022-12-05, publication
US20240119334A1 du 2024-04-11, **délivré le 2026-04-07**, expiration ajustée affichée
**2044-12-16**. CPC : **G06N 10/00, G06N 10/20, G06N 10/40, B82Y 10/00**.

Revendication 13, sur le point qui nous concerne, verbatim :

> « determining a sequence of a plurality of single photon fusions and a plurality of single photon
> Bell-state measurements (BSMs) expressed by a shape of the combination graph and one or more lines
> between the vertices **by performing a resource optimization algorithm for the combination graph**
> consisting of a plurality of vertices representing an arbitrary microcluster and lines connecting
> the vertices ; configuring **at least two first Greenberger-Horne-Zeilinger (GHZ) states consisting
> of three photons** based on the shape of the combination graph ; […] defined by **(n, m)
> parity-state encoding** […] »

Et la description **donne la métrique** : un coût `M_v = 1` par sommet, un coût par arête

    M_e = 2 (1 − η)^(−2) (M_v1 + M_v2)

où **η est le taux de perte de photons**, puis contraction itérative de l'arête de coût minimal
jusqu'à ce qu'il ne reste qu'un sommet.

Ce coût-là est **plus** que ce que `P-18` demande, pas moins. Celui de PsiQuantum compte des états
3-GHZ « en faisant les hypothèses optimistes d'un multiplexage efficace et d'une fusion sans
perte ». Celui du brevet **intègre le taux de perte dans le coût**. La seule chose que je pouvais
ajouter — rendre la métrique consciente de la perte tout en la gardant indépendante du niveau
d'encodage — est la revendication délivrée d'un brevet qui court jusqu'en 2044.

**Et la combinaison des deux ne sauve rien**, au contraire : OptGraphState donne l'indépendance au
niveau d'encodage, le brevet donne la conscience de la perte, et **les deux sortent de la même
équipe de Séoul**. À l'art. 56 CBE, il n'existe pas de combinaison plus évidente pour l'homme du
métier que celle de deux travaux du même laboratoire qui se citent.

### Mort n°3 — art. 52 CBE, et c'est celle qui compte

Une métrique de coût calculée sur un ordinateur, qui ne commande aucun appareil et ne produit aucun
effet physique, est une méthode mathématique. L'art. 52(2) CBE l'exclut ; il faut un effet technique
pour en sortir (COMVIK T 641/00, G 1/19).

Or le carnet 4 écrit, noir sur blanc, que `P-18` est **le seul problème qui ne demande qu'un
ordinateur**. C'est exactement pour cela qu'il est **le seul problème du carnet sur lequel l'art. 52
mord**. `P-15`, `P-16`, `P-17`, `P-19` ont un effet physique et pas de laboratoire chez nous.
`P-18` n'a pas besoin de laboratoire et n'a pas d'effet physique.

**C'est une tenaille, et ce n'est pas une tenaille propre au quantique : c'est la même que dans le
logiciel.** Ce que je peux faire seule, l'art. 52 l'exclut. Ce que l'art. 52 admet, je ne peux pas
le faire seule. Le virage quantique n'a pas supprimé cette géométrie, il l'a déplacée d'un cran —
et je ne l'avais pas vu en ouvrant le carnet.

La preuve est dans le brevet lui-même, et elle est instructive : SNU a obtenu la délivrance parce
que l'algorithme d'optimisation est revendiqué **à l'intérieur** d'une méthode qui finit par
« measuring at least one central qubit of the RHG lattice ». La métrique passe l'art. 52 en étant
attachée à un procédé physique. **Pour breveter une métrique, il faut un dispositif — donc un
laboratoire.**

### Antériorité secondaire, relevée au passage et non exhaustive

Libre publié, en plus d'OptGraphState :

- **`TeamGraphix/graphix`** (Apache-2.0, lue au commit `2b30fdf18c09`) — `extraction.graph_to_fusion_network`
  décompose un état de graphe cible en états ressources GHZ et cluster linéaires, avec contrainte de
  taille maximale disponible (`max_ghz`, `max_lin`) pour un ordonnancement réaliste.
- **arXiv:2606.02880** — *Cost-aware Fusion-based Decomposition* : surcoût en ressources défini comme
  le nombre total de photons consommés, équivalence Clifford locale comme proxy, −84,6 % de surcoût.
- **arXiv:2509.14794** — coût photonique moyen par état GHZ-like, optimisation sur les séquences de
  fusion.
- **`benchq`**, **Rigetti RRE**, **Azure QRE**, **`qlass` ResourceAwareCompiler** (celui-ci modélise
  perte par composant, probabilité de succès de fusion et visibilité HOM) — l'estimation de
  ressources pour calcul tolérant aux fautes est un marché d'outils, pas un trou.

Brevets voisins, non lus en entier :

- **US11681845** — *Quantum circuit valuation* : score d'un circuit quantique avec un « resource
  factor » fonction du pré-traitement et de la correction d'erreurs requis. Revendication large sur
  l'idée même de **valoriser** un circuit par ses ressources.
- **US11501198** (PsiQuantum) — génération d'un état photonique intriqué à partir de « primates »,
  présentée comme « une réduction spectaculaire du nombre de ressources requises ».
- **US12468970**, **US12694322**, **US11341428** — architectures photoniques à états ressources,
  lignes à retard, multiplexage.

### Ce qui n'est pas prouvé, et ne doit pas être cru prouvé

- Registres **EPO et Espacenet toujours inatteignables** depuis cette session. US12596949B2 lu sur
  Google Patents via `mcp__Exa__web_fetch_exa` le 2026-09-28. Est VÉRIFIÉ, par cette lecture à
  `https://patents.google.com/patent/US12596949B2/en` : l'existence, le titre, le titulaire, les
  inventeurs, les dates, les codes CPC, et le texte cité de la revendication 13 et de la
  description.
- **NON VÉRIFIÉ** : l'étendue réelle de la famille (continuations, équivalents EP / CN / JP), la
  validité, et la portée exacte des revendications indépendantes 1 et 7 que je n'ai pas lues mot à
  mot.
- Le statut « actif, expire 2044-12-16 » est un **affichage** Google Patents, qui écrit lui-même que
  c'est une hypothèse et non une conclusion juridique.
- **Aucune recherche CPC exhaustive.** G06N 10/ compte des milliers de documents. Ce verdict tue le
  croisement ; il ne prouverait pas l'inverse.
- Ceci n'est **pas un conseil juridique**. Un conseil en PI humain est requis avant tout dépôt réel.

---

# SIX MORTS — ET LE MOTIF A CHANGÉ DE NATURE

| | Cause de la mort |
|---|---|
| X-01, X-02 | domaines trop proches — ma faute, `E-31` |
| X-03 | idée juste, faite depuis 1990 |
| X-04 | domaine rendu inbrevetable **en temps réel** par publication défensive |
| X-05 | outil déjà publié, en code libre et en documentation |
| X-06 | **libre publié MIT *et* brevet délivré en vigueur — par la MÊME équipe** |

**Pour la première fois, les deux barrières sont debout en même temps.** Dans le logiciel (X-04,
X-05), le libre publié détruisait la nouveauté mais laissait la liberté d'exploitation : on ne
pouvait pas breveter, on pouvait utiliser. Ici l'équipe de Séoul a fait les deux — elle a **publié
en MIT** ce qui détruit la nouveauté, et **breveté** la version améliorée jusqu'en 2044. On ne peut
ni déposer, ni progresser librement dans la direction évidente.

**Et cela corrige une affirmation que j'ai écrite le matin même.** Le carnet 4 et le verdict X-05
disent : « en photonique quantique la logique du terrain est **inverse**, les acteurs déposent
massivement au lieu de publier ». C'est **faux par moitié**, et la moitié fausse est précisément
celle qui servait d'argument au virage. Ils déposent **et** ils publient. Fiche `E-36`.

### Ce qui reste, et qui n'est pas un brevet

Les deux antériorités sont des **briques utilisables**, entrées au sas le jour même :
`B-21 seokhyung-lee/OptGraphState` (MIT, `4f7c563634cf`) et `B-22 TeamGraphix/graphix` (Apache-2.0,
`2b30fdf18c09`). C'est la troisième fois que la recherche d'antériorité rapporte un outil plutôt
qu'un candidat — et c'est, à ce stade, le seul rendement mesurable du dispositif.

**X-06 est close.** Aucune ligne étroite ne survit : celle qui survivrait est la revendication 13 de
US12596949B2.
