# /codex/DEBATS.md — registre des décisions débattues

**Tenu par `conciliateur`.** Append-only : on ajoute une fiche, on n'en réécrit jamais une.

---

## POURQUOI CE FICHIER

Le dispositif avait tout pour bien décider — un avocat, un contradicteur, un simulateur de
scénarios, un arbitre — et **personne pour les convoquer**. L'arbitre tranche un débat ; il ne le
provoque pas.

Constat fondateur, **2026-09-14** : une journée entière de décisions réelles — créer un dépôt,
choisir une palette, arrêter une architecture, trancher un positionnement, fixer un ordre de
démarches — **sans qu'une seule ait été soumise à un contradicteur**. Personne n'avait mal
travaillé. Personne n'avait le mandat de convoquer.

## CE QU'EST UNE DÉCISION

Pas seulement « je choisis A plutôt que B ». Aussi :

- un choix technique qui **ferme une porte** (un format, une dépendance, une architecture) ;
- un texte **publié** ou rendu public ;
- une **dépense**, ou un engagement qui en créera une ;
- un **ordre de démarches** — parce que l'ordre peut faire perdre un droit ;
- un **rôle ajouté**, une **règle posée**, un **contrôle assoupli**.

**Le plus dangereux est celui qui ne se présente pas comme une décision.**

## SEUIL — quand on ne convoque PAS

Un débat systématique devient un rituel, et un rituel devient un tampon. On ne convoque pas sur ce
qui est **réversible et sans conséquence**.

La question qui tranche : **revenir en arrière coûtera-t-il du temps, de l'argent ou de la
crédibilité ?** Si non, on décide et on avance.

## FORME D'UNE FICHE

```
## D-xx — [la décision, en une ligne]
**Date** AAAA-MM-JJ · **Consigne n°1 en vigueur** [laquelle] · **Réversible ?** [oui/non, à quel coût]

**POUR** (avocat) — le meilleur argument, pas le plus long. Et le coût de NE PAS le faire.
**CONTRE** (contradicteur) — le scénario d'échec le plus PROBABLE, pas le plus spectaculaire.
**SCÉNARIOS** — optimiste / réaliste / pessimiste. Jamais de pourcentage.
**ARBITRAGE** — une phrase actionnable.
**CE QUE LE CAMP PERDANT A OBTENU** — le garde-fou concédé.
**DÉCIDÉ PAR** — Chaima, ou l'arbitre dans les limites du §10.
```

**La ligne qui compte le plus est l'avant-dernière.** Une objection écartée sans garde-fou qui la
reprenne signifie que la décision a été **gagnée**, pas **arbitrée** — et c'est une faute
d'arbitrage, pas une victoire.

## LIMITE CONNUE

Ce registre repose sur la **discipline**, pas sur une machine : aucun contrôle ne vérifie
aujourd'hui qu'une décision a eu son débat. Or la leçon du 2026-09-14 est qu'une règle sans
mécanisme cède — elle a cédé quatre fois pour la dérive de périmètre (fiche E-26).

Un contrôle bloquant est **proposé** à Chaima, non posé d'office : exiger que tout rapport annonçant
une décision cite sa fiche de débat. Tant qu'il n'existe pas, **ce registre est une promesse, pas
une garantie** — et il doit le dire.

---

## FICHES

## D-01 — Où rapatrier les 12 dossiers « transverse » qui n'existent qu'au Drive ?
**Date** 2026-09-16 · **Consigne n°1** la base unique répliquée Drive + GitHub + local ·
**Réversible ?** **NON** pour une partie : publier dans un dépôt public est **irréversible**
(art. 54 CBE, aucun délai de grâce ; et un dépôt public reste lisible dans l'historique git même
après suppression — c'est la limite honnête inscrite à la PR #15).

**Convoqué par** `conciliateur` — première saisine depuis sa création. La décision ne s'annonçait
pas comme telle : « rapatrier des dossiers » ressemble à une tâche de rangement. C'en est une
**de divulgation**.

### POUR (avocat)
L'inventaire du jour l'établit : ces douze dossiers — le CODEX, la source unique de vérité, la
structure de veille, la bibliothèque brevets par pays, Brevetabilité de nos projets, Financement
& Capitaux, le Coffre confidentiel — **n'existent qu'au Drive**. Deux projets ont déjà été perdus
pour exactement cette raison. Le protocole qui gouverne tout le dispositif est aujourd'hui à la
merci d'un accès Drive perdu, d'une suppression accidentelle, d'un compte suspendu.
**Le coût de NE PAS le faire est la perte des règles elles-mêmes.**
Et le dépôt contient déjà `CLAUDE.md` avec le CODEX §1 à §15 : une partie du protocole y est
donc **déjà**, sans que cela ait jamais posé de problème.

### CONTRE (contradicteur)
**`keywordmoneymaker` est PUBLIC.** Le scénario d'échec le plus probable n'est pas spectaculaire,
il est banal : on rapatrie douze dossiers « pour les sauvegarder », et l'un d'eux contient une
note sur une idée brevetable. **La nouveauté est détruite le jour du push, irréversiblement.**
Aucun correctif n'existe : ni suppression, ni dépôt privé après coup, car l'historique git garde
tout (fiche E-15, et la limite honnête de la PR #15 sur le CV).

Deux dossiers sont **nommément** dangereux : **« Brevetabilité de nos projets »** — dont le titre
dit qu'il contient précisément ce que `protecteur` a mandat de protéger — et le **« Coffre
confidentiel »**, dont le rôle déclaré est « ne sort jamais en dépôt public ».

Et la fiche **E-17** décrit l'accident déjà survenu : 77 fichiers internes publiés, parce que le
dépôt **mêle contenu public et documents internes**. Sa cause aggravante est notée comme
**toujours présente**. Rapatrier douze dossiers de plus, c'est l'aggraver encore.

### VETO — `protecteur`
**Opposé.** Rien de ce qui touche à la brevetabilité n'entre dans un dépôt public avant dépôt.
En Europe il n'y a pas de délai de grâce : un push public vaut divulgation et détruit la
nouveauté définitivement. **Seule Chaima peut lever ce veto**, et le lever ne réparerait rien —
il autoriserait seulement la perte.

### SCÉNARIOS (simulateur-scenarios)
- **Optimiste** — les douze dossiers ne contiennent aucune idée brevetable ; le rapatriement est
  une simple sauvegarde et tout va bien. *Mais personne ne l'a vérifié dossier par dossier.*
- **Réaliste** — l'essentiel est anodin, un ou deux documents ne le sont pas, et on ne le
  découvre qu'en les lisant un par un — travail qui n'a pas été fait.
- **Pessimiste** — une note d'idée part en public, et un droit qui n'existera jamais est perdu
  sans que personne ne s'en aperçoive. **Le pire des scénarios est silencieux.**

### ARBITRAGE (arbitre-expert)
**Le rapatriement a lieu, mais pas dans un dépôt public : il faut un dépôt PRIVÉ, et il n'existe
pas encore.**

Le besoin de sauvegarde est réel et urgent ; la destination proposée était fausse. On ne renonce
pas au rapatriement — on change d'adresse.

### CE QUE LE CAMP PERDANT A OBTENU
L'avocat perd sur le calendrier : **rien ne part maintenant**, et ce blocage tient à une action
que seule Chaima peut faire (créer le dépôt). Il obtient en échange que **tout soit prêt** — le
tri fait, l'ordre des lots arrêté, la commande écrite — pour que la sauvegarde parte **le jour
même** où le dépôt existe, et non des semaines plus tard.

### DÉCIDÉ PAR
**Chaima** — §10 : créer un dépôt, publier, lever un veto de divulgation lui appartiennent.

### CE QU'IL FAUT D'ELLE
Créer un dépôt **PRIVÉ** nommé `empire-codex` (l'intégration ne peut pas créer de dépôt : testé,
403). Ensuite seulement, et dans cet ordre :
1. Protocole et source de vérité — sans risque de brevet, mais internes ;
2. Structure de veille, Financement & Capitaux, Synergies inter-agents ;
3. **Brevetabilité de nos projets** et **Bibliothèque brevets** — après lecture pièce par pièce
   par `protecteur` ;
4. **Coffre confidentiel — JAMAIS, nulle part ailleurs qu'au Drive**, sauf décision explicite de
   Chaima sur un support chiffré.


---

## D-02 — Faut-il continuer à chercher des brevets à vendre dans le domaine du droit accessible ?

**Date** 2026-09-19 · **Consigne n°1 en vigueur** veille technologique et brevets sur le droit
accessible aux citoyens · **Réversible ?** Oui, mais chaque semaine passée dans un domaine saturé
est une semaine non passée ailleurs. Coût du retour en arrière : le temps déjà dépensé.

**Convoqué par** `conciliateur`, à la suite de trois recherches d'antériorité du 2026-09-19 qui ont
toutes ramené de l'art antérieur sur les idées visées.

**POUR — continuer ici** (`avocat`)
C'est le domaine que Chaima connaît, où elle a déjà un produit en construction et une motivation
personnelle. Un inventeur qui comprend le problème mieux que les déposants existants a un avantage
réel : Intuit optimise la fiscalité américaine, personne n'a travaillé la Belgique à trois régions
et deux communautés. Le coût de ne pas continuer : abandonner un terrain où elle est experte pour
un terrain où elle ne l'est pas, et où sa capacité à juger une invention s'effondre.

**CONTRE — chercher ailleurs** (`contradicteur`)
Le scénario d'échec le plus probable n'est pas spectaculaire, il est lent. Trois recherches, trois
murs :
- entrée par la situation en langage ordinaire → US6931394B2, priorité 2000 ;
- ordonnancement des questions d'éligibilité → US10872315B1, priorité 2016 ;
- extraction de règles exécutables depuis un texte de loi et resynchronisation quand la loi
  change → US12561629, US12536214, US10650190, US10885442, entre autres ;
- gestion du répondant qui ne peut pas répondre → US10095682, dont la revendication 2 porte
  littéralement sur le recalcul de l'arbre « to compensate for questions that a user may not be
  able to answer ».

Ce domaine est travaillé depuis vingt-cinq ans par Intuit, Thomson Reuters, LexisNexis et leurs
concurrents. Ce ne sont pas des trous, ce sont des zones déjà ratissées.

S'y ajoute un obstacle structurel, et c'est lui le vrai : art. 52 CBE et COMVIK T 641/00. Une
invention dont l'apport est de mieux orienter un citoyen vers ses droits produit un meilleur
résultat **administratif**, pas un effet **technique**. C'est exactement la catégorie où l'OEB
refuse. Autrement dit : même en trouvant une nouveauté ici, la probabilité de délivrance en Europe
reste basse, et un brevet non délivré ne se vend ni ne se loue.

**SCÉNARIOS**
- *Optimiste* — une niche étroite subsiste, formulée avec un effet technique défendable (par
  exemple un gain mesurable de ressources machine, pas un gain de confort pour l'usager). Dépôt
  possible, valeur de revente faible à modérée car le marché acheteur est composé des quelques
  acteurs qui détiennent déjà les brevets de base.
- *Réaliste* — plusieurs semaines de recherche d'antériorité aboutissent à des candidats tous
  antériorisés ou tous refusés à l'art. 52. Le produit La Loi Avec Moi avance, le portefeuille de
  brevets reste vide.
- *Pessimiste* — un dépôt est préparé, payé, puis refusé à l'examen sur un motif d'exclusion
  qu'on pouvait voir dès le départ. Perte sèche, et perte de confiance dans le dispositif.

**ARBITRAGE** — Séparer les deux objectifs qui ont été confondus : **La Loi Avec Moi reste un
produit** et continue, sans ambition de brevet ; **la chasse aux brevets change de domaine** pour
un domaine où l'effet technique est évident par nature et non à défendre. Le choix du domaine
revient à Chaima, pas à l'arbitre — c'est une décision de §10.

**CE QUE LE CAMP PERDANT A OBTENU** — La lecture du domaine juridique n'est pas jetée. Les deux
brevets tombés identifiés le 19/09 servent désormais de **preuve de liberté d'exploitation** pour
La Loi Avec Moi : ce que nous voulions construire est enseigné par des brevets tombés, donc utilisable.
Ce qui échoue comme invention réussit comme protection du produit. Et la méthode éprouvée ici —
trois recherches d'antériorité en une matinée, avec numéros et dates — est transposable telle
quelle au domaine suivant, quel qu'il soit.

**DÉCIDÉ PAR** — En attente de Chaima. Proposition soumise, rien n'est changé tant qu'elle n'a pas
répondu : changer de priorité en silence reste interdit.
