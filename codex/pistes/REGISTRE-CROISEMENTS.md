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
