# MÉTHODES POUR ALLER VITE — veille technologies & brevets en 15 jours

**Écrit le 2026-09-19**, après que Chaima a signalé une confusion réelle de ma part :
j'avais présenté une base de **jurisprudence** comme une avancée sur les **brevets**.
Ce sont deux choses sans rapport, et la correction ouvre ce document (§0).

---

## §0. CE QU'ON CHERCHE, ET CE QU'ON NE CHERCHE PAS

| | C'est quoi | Où ça vit | Sert à quoi |
|---|---|---|---|
| **Brevet** | un titre sur une **invention technique** | registres : Espacenet, OEB, OMPI | savoir si une technique est prise |
| **Jurisprudence** | des **décisions de tribunaux** | Juportal, bases de justice | savoir comment un juge a tranché |

**On ne trouve pas de brevets dans la jurisprudence.** Un procès en contrefaçon cite un brevet,
mais il en cite un sur des milliers : c'est un échantillon biaisé par le conflit, pas un registre.

**Et le mot « technologie » ne veut pas dire « informatique ».** Un brevet protège un **procédé** :
une façon de faire qui produit un effet technique. Un site web n'est pas brevetable ; une méthode
de traitement local de données qui garantit par construction qu'elles ne sortent pas, peut l'être.

---

## §1. LA MÉTHODE QUI FAIT GAGNER LE PLUS DE TEMPS — produit d'abord, brevet ensuite

**Erreur classique : commencer par chercher des brevets.** C'est lent, le vocabulaire des brevets
n'est pas celui des gens, et on rate 90 % de ce qui compte.

**Méthode inverse, dix fois plus rapide :**

1. **Cherche le PRODUIT** qui fait déjà ce que tu veux faire. En langage normal.
2. **Trouve l'entreprise** derrière.
3. **Alors seulement**, cherche ses brevets — par nom de déposant, pas par mots-clés.

**Pourquoi c'est plus rapide :** un brevet qui compte est presque toujours attaché à un produit
vendu. Personne ne dépose et ne paie des annuités pendant vingt ans pour une technique que
personne n'exploite. **Le marché est un filtre gratuit sur la pertinence.**

Et un brevet sans produit est le plus souvent soit expiré, soit non payé, soit jamais délivré —
donc libre.

## §2. LA CLÉ D'ENTRÉE DES REGISTRES : le code de classification, jamais le mot-clé

Une recherche par mots-clés dans les brevets échoue presque toujours : les rédacteurs écrivent
« dispositif de retenue pour occupant de véhicule » là où tout le monde dit « ceinture ».

**La bonne clé, c'est la classification CPC.** Chaque brevet porte un ou plusieurs codes qui
disent de quoi il traite. Exemple utile ici : **G06F 21/62** — protection des données à caractère
personnel dans un système informatique.

**Méthode :** trouve **un seul** brevet proche de ton sujet, relève ses codes CPC, puis **explore
le code** au lieu de chercher des mots. Tu passes d'une recherche approximative à un rayon de
bibliothèque.

## §3. LE RACCOURCI QUI TRANCHE LA MOITIÉ DES CAS EN CINQ MINUTES

**Si c'est déjà publié, c'est déjà de l'état de la technique.**

Conséquence double, et elle règle beaucoup de situations :
- **Personne ne peut plus le breveter** — donc tu peux t'en servir sans craindre un brevet futur.
- **Toi non plus** — si tu l'as publié toi-même, ta nouveauté est détruite (art. 54 CBE, **aucun
  délai de grâce en Europe**).

**Application immédiate :** avant toute recherche, demande-toi *« est-ce que cette idée est déjà
sortie quelque part ? »* Un dépôt public, une démo, un post, un site en ligne. Si oui, le volet
« puis-je le breveter » est **clos**, et il ne reste que « puis-je l'utiliser » — beaucoup plus
simple.

## §4. POUR DU LOGICIEL EN EUROPE — le vrai risque n'est pas le brevet

En Europe, un programme d'ordinateur « en tant que tel » est **exclu** de la brevetabilité
(art. 52 CBE). Il faut un **effet technique** au-delà de l'exécution du code.

**Conséquence pratique, et elle fait gagner des semaines :** pour un site, une base de fiches, un
questionnaire d'orientation, **le risque brevet est faible**. Le temps est bien mieux investi sur
les trois risques qui, eux, sont réels :

| Risque réel | Comment on le lève, vite |
|---|---|
| **Licence** d'un composant réutilisé | lire le fichier `LICENSE` — 2 minutes |
| **Marque** déjà déposée sur le nom | recherche au registre — à faire dans un navigateur |
| **Droit des bases de données** sur un corpus repris | vérifier les conditions de réutilisation de la source |

## §5. CE QUI EST BLOQUÉ, ET COMMENT CONTOURNER SANS MENTIR

**Mesuré le 2026-09-14** : Espacenet, registre OEB, OPS, Patentscope, BOIP, TMview, EUIPO, Google
Patents — **onze domaines refusés** par la politique réseau, preuve au journal du proxy.

**Donc, honnêtement :** aucune recherche d'antériorité sérieuse ne peut être faite depuis une
session d'agent. **Une recherche web n'est pas un registre** (fiche E-13).

**Trois contournements légitimes :**
1. **Chaima fait la recherche dans son navigateur** — 20 minutes sur Espacenet valent mieux que
   trois jours de contournement.
2. **Élargir la politique réseau** de l'environnement — c'est un réglage, et il est entre ses mains.
3. **Partir des produits** (§1) : cette voie-là n'est pas bloquée, et elle donne l'essentiel.

---

## LE PLAN DE 15 JOURS

Trois blocs de cinq jours. Chaque jour produit **un document daté**, jamais un fourre-tout.

### Jours 1-5 — CARTOGRAPHIER (aucun registre nécessaire)
| Jour | Ce qu'on fait | Livrable |
|---|---|---|
| 1 | Lister tous les produits existants qui font ce qu'on veut faire | tableau des acteurs |
| 2 | Pour chacun : quel est son modèle, qui le paie, qu'est-ce qu'il ne fait pas | tableau des trous |
| 3 | Chercher le composant **libre** réutilisable pour chaque brique | tableau des briques + licences |
| 4 | Lire les licences une par une, vraiment | verdict par brique |
| 5 | **Décision : ce qu'on reprend, ce qu'on écrit** | fiche de débat `D-xx` |

### Jours 6-10 — PROTÉGER (Chaima au navigateur, une heure suffit)
| Jour | Ce qu'on fait | Livrable |
|---|---|---|
| 6 | Recherche **marque** : le nom est-il libre ? | verdict marque |
| 7 | Lister ce qui, dans le projet, pourrait avoir un effet technique | liste candidats |
| 8 | Pour chaque candidat : est-ce déjà publié ? (§3) | tri publié / non publié |
| 9 | Sur les non publiés : recherche CPC ciblée (§2) | état de l'art sommaire |
| 10 | **Décision : déposer, garder secret, ou publier** | fiche de débat `D-xx` |

### Jours 11-15 — FINANCER ET DÉCIDER
| Jour | Ce qu'on fait | Livrable |
|---|---|---|
| 11 | Aides accessibles **sans numéro d'entreprise** | tableau + **échéances d'abord** |
| 12 | Appels à projets « numérique d'intérêt général » | liste datée |
| 13 | Contact des alliés possibles (ex. `openjustice.be`) | brouillons, non envoyés |
| 14 | Tout recouper : le contradicteur passe sur l'ensemble | objections écrites |
| 15 | **Une seule synthèse**, pas quinze | rapport final + `A-DECIDER` |

---

## LES CINQ RÈGLES QUI FONT ALLER VITE

1. **Un jour = un livrable daté.** Pas de chantier qui traîne trois jours sans rien produire.
2. **Produit d'abord, brevet ensuite** (§1). C'est le gain de temps principal.
3. **Ce qui est bloqué se dit, ne se contourne pas.** Une recherche web présentée comme un
   registre fait perdre plus de temps qu'elle n'en gagne : il faut tout refaire quand on s'en
   aperçoit.
4. **Le contradicteur passe sur chaque décision** — pas à la fin, où il ne sert plus à rien.
5. **Une heure de Chaima au navigateur > trois jours d'agent bloqué.** Identifier ce qui n'est
   faisable que par elle, et le lui donner groupé, pas au compte-gouttes.

## CE QUE CE PLAN NE PROMET PAS

Il ne remplace pas un **conseil en propriété intellectuelle**. Une recherche d'antériorité
opposable, une rédaction de revendications, une stratégie de dépôt : c'est un métier, et un dépôt
raté coûte plus cher que le conseil. **Ce plan sert à décider s'il vaut la peine d'en payer un —
pas à s'en passer.**
