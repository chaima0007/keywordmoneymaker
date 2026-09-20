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
