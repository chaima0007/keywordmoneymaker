# Pipeline brevets — comment la chaîne se parle à elle-même

Document de méthode. Aucune invention, aucun candidat, aucun nom de domaine
technique n'est écrit ici : ce fichier est dans un dépôt PUBLIC.
Le contenu des trouvailles va au Drive (coffre confidentiel), jamais ici.

Sert la consigne n°1 en vigueur : repérer des technologies, lire les brevets
existants, croiser leurs enseignements, concevoir des inventions que Chaima
pourra déposer, vendre ou louer.

---

## 0. Le blocage qui commande tout

**Je ne peux lire aucun brevet depuis cet environnement.**
Onze registres sont refusés par la politique réseau (relevé du 14/09, preuve
par journal de proxy) : Espacenet, Register EPO, api.epo.org, data.epo.org,
Patentscope, Google Patents, BOIP, TMview, EUIPO, ejustice, economie.fgov.be.

La méthode entière repose sur la lecture des sections « arrière-plan » des
brevets — c'est la matière première. Sans elle, les étapes 1 à 4 ci-dessous
tournent à vide.

**Contournement immédiat, sans attendre personne :** Chaima ouvre Espacenet,
cherche par code CPC, télécharge les PDF, les dépose dans le Drive. Le Drive
n'est pas bloqué. Je lis depuis là.

État : NON RÉSOLU au 2026-09-19.

---

## 1. Les huit étapes

Chaque étape dit : qui travaille, qui surveille, qui contredit, ce qui est
archivé. Aucune étape ne passe à la suivante sans son contradicteur.

### Étape 1 — Cartographier ce qui est libre
- **Travaille :** `eclaireur-brevets-libres`
- **Produit :** liste de brevets expirés, déchus pour annuités impayées, ou
  jamais étendus au territoire visé.
- **Contredit :** `verificateur-verite` — exige le registre pour chaque
  mention « libre ». Un brevet déchu peut être restauré ; un brevet expiré
  ne l'est pas. La confusion des deux est l'erreur qui coûte le plus cher.
- **Surveille :** `superviseur-vigie` prend l'instantané d'entrée (quelles
  sources, quelle date d'interrogation, quel périmètre territorial).
- **Archive :** `archiviste-preuves` — capture datée de chaque fiche registre.

### Étape 2 — Récolter les problèmes non résolus
- **Travaille :** `recolteur-problemes`
- **Produit :** problèmes extraits des sections « arrière-plan », classés par
  problème et non par brevet, avec signalement de ceux qui viennent d'un
  domaine éloigné.
- **Contredit :** `contradicteur` — un défaut décrit par un déposant sert son
  propre brevet ; il est PLAUSIBLE, jamais VÉRIFIÉ, tant qu'une seconde source
  indépendante ne le confirme pas.
- **Règle dure :** cet agent ne propose aucune solution. Dès qu'il propose,
  il contamine l'étape 4.

### Étape 3 — Lire pour de vrai
- **Travaille :** `dechiffreur`
- **Produit :** pour chaque brevet retenu, ce qui est réellement revendiqué
  (revendication indépendante) distingué de ce qui est seulement décrit.
  La description est libre d'usage ; la revendication ne l'est pas.
- **Contredit :** `controleur` — relit la revendication 1 mot à mot. Une
  lecture approximative d'une revendication est une conclusion fausse.
- **Archive :** `archiviste-preuves`.

### Étape 4 — Croiser
- **Travaille :** `analyste-brevets`, sur la table problèmes × enseignements.
- **Produit :** couples (problème récolté à l'étape 2 / enseignement libre
  repéré à l'étape 1) qui ne sont pas déjà rapprochés dans l'art antérieur.
- **Contredit :** `avocat` sur l'art. 56 CBE — si le rapprochement est évident
  pour l'homme du métier, il n'y a pas d'invention. C'est ici que meurent la
  plupart des candidats, et c'est normal.
- **Contredit aussi :** `contre-verificateur-securite` — vérifie qu'aucun
  élément du croisement n'a fuité hors du coffre pendant le travail.

### Étape 5 — Débat contradictoire obligatoire
- **Convoque :** `conciliateur`, qui ouvre une fiche dans `codex/DEBATS.md`.
- **S'opposent :** `avocat` (brevetabilité : art. 52, 54, 56 CBE, COMVIK
  T 641/00, G 1/19 si le candidat touche au logiciel) contre
  `analyste-marche` (est-ce que quelqu'un paierait pour ça ?).
- **Tranche :** `arbitre-expert`, qui écrit ce que le camp perdant a obtenu.
  Un débat sans cette ligne n'est pas clos.
- **Règle :** aucun candidat ne franchit l'étape 5 sans fiche de débat.

### Étape 6 — Éprouver
- **Travaille :** `simulateur-scenarios` et `testeur` — attaquent le candidat
  comme le ferait un examinateur puis un concurrent.
- **Cherchent :** l'antériorité qui tue, la divulgation qui a déjà eu lieu
  (pas de délai de grâce en Europe), le contournement trivial.
- **Contredit :** `avocat-du-client` — pourquoi un acheteur ou un licencié
  refuserait-il de payer.

### Étape 7 — Veto de divulgation
- **Travaille :** `protecteur`, seul, avec droit de veto.
- **Interdit :** toute écriture du candidat hors du coffre confidentiel Drive.
  Rien dans un dépôt public. Rien dans un rapport. Rien dans un message.
- **Rappel de l'incident du 11/09 :** 77 fichiers internes exposés pendant
  des semaines. Cette étape existe à cause de ça.

### Étape 8 — Clôture
- **Travaille :** `deposant` prépare le dossier ; `gardien-controle-final`
  refuse la clôture si une seule étape n'a pas son contradicteur.
- **Sauvegarde :** Drive + dépôt privé + copie locale. Trois emplacements ou
  la trouvaille n'est pas sauvegardée.
- **Humain requis :** aucune analyse ici n'est un conseil juridique. Un
  conseil en propriété intellectuelle humain valide avant tout dépôt réel.

---

## 2. Comment les agents se parlent

Un passage d'étape qui ne respecte pas ce format est refusé par `passerelle`.

```
DE      : <rôle qui passe la main>
VERS    : <rôle qui reprend>
ÉTAPE   : <numéro et nom>
OBJET   : <une ligne, sans contenu confidentiel>
ÉTAT    : VÉRIFIÉ | CONFIRMÉ | PLAUSIBLE | NON VÉRIFIÉ
SOURCE  : <registre, numéro de publication, date d'interrogation>
CONFIANCE : FAIBLE | MODÉRÉE | ÉLEVÉE
CONTREDIT PAR : <rôle> — <verdict> — <date>
RESTE OUVERT : <ce qui n'a pas pu être vérifié>
```

Trois règles sur ce format :

1. **`RESTE OUVERT` ne peut pas être vide.** S'il l'est, c'est que personne
   n'a cherché. `passerelle` renvoie le passage.
2. **`CONTREDIT PAR` rempli par le même rôle que `DE` est nul.** On ne se
   contredit pas soi-même.
3. **Jamais de pourcentage.** La confiance a trois valeurs, pas cent.

`passerelle` surveille les passages rompus : une étape dont personne ne
reprend la main pendant plus de sept jours est signalée à `pilote`.

---

## 3. Surveillance, audit, instantané

- **Instantané :** `superviseur-vigie` à l'entrée de chaque étape — quelles
  sources, quelle date, quel périmètre. Sans instantané d'entrée, une
  conclusion n'est pas rejouable six mois plus tard.
- **Audit de cloisonnement :** `scripts/audit_cloisonnement.py` vérifie
  qu'aucun contenu du coffre n'a migré vers le dépôt public.
- **Audit de la chaîne elle-même :** `conservateur-secrets` et
  `croque-mort` — le second est convoqué dès qu'apparaissent des documents
  quasi identiques ou une condition d'arrêt qui n'a pas fonctionné.
- **Contrôle bloquant :** `scripts/verifier_rapports.py`, règles R1 à R8.
  Si le contrôle est démontré faux, on le durcit ; on ne le desserre jamais.

---

## 4. Ce qui n'est pas résolu

| Sujet | État | Qui débloque |
|---|---|---|
| Accès aux registres de brevets | NON RÉSOLU | Chaima (PDF vers Drive, ou élargissement de la politique réseau) |
| Dépôt privé `empire-codex` | N'EXISTE PAS | Chaima (création — 403 pour moi) |
| Domaine technique à attaquer en premier | NON DÉCIDÉ | Chaima — je fournis les codes CPC exacts dès qu'il est nommé |
| Cinq groupes de projets en un seul emplacement | NON RÉSOLU | dépend de `empire-codex` |

---

*Un document = un événement. Ce fichier décrit une méthode, pas une trouvaille.
Les trouvailles vont au coffre, datées, une par document.*
