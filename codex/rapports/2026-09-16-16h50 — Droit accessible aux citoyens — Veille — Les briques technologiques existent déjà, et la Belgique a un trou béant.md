# Les briques technologiques existent déjà — et la Belgique a un trou béant

**Phrase de contrôle honnête.** Aucun doublon : première veille technologique sur ce domaine.
La condition d'arrêt a fonctionné — recherche arrêtée dès que la question décisive (« existe-t-il
l'équivalent belge de l'open data juridique français ? ») avait sa réponse, sans empiler des
acteurs pour faire nombre. **Et je dois dire ceci : c'est Chaima qui m'a remis sur la mission,
pour la deuxième fois. Le dispositif anti-dérive que j'ai construit ce matin ne m'a pas arrêté.**

**Consigne n°1 servie : veille technologies & brevets, cible « le droit accessible aux citoyens »**
(`codex/CONSIGNE-N1.md`, recentrée le 2026-09-16 à 16h50).

- **Catégorie** : Veille · **Sources lues et datées le** : 2026-09-16

---

## 1. LA DÉCOUVERTE QUI COMMANDE TOUT LE RESTE

**La Belgique a un identifiant officiel, stable et adressable par machine, pour chaque loi.**

```
https://www.ejustice.just.fgov.be/eli/{type}/{aaaa}/{mm}/{jj}/{numac}/justel
```

C'est l'**ELI** (European Legislation Identifier), en service depuis juin 1997 pour le Moniteur
belge. `type` vaut `loi`, `decret`, `ordonnance`, `arrete`, `constitution`. On peut donc pointer
une loi, un article, une version — de façon stable et citable.

**MAIS — et c'est là que tout se joue :**

> **Il n'existe AUCUNE recherche plein texte.** Le Moniteur belge n'expose aucune interface de
> recherche par mot-clé. On ne peut atteindre un texte que si **on connaît déjà ses coordonnées**.

Autrement dit : **le droit belge est accessible à qui sait déjà où il est.** C'est exactement
l'inverse de ce dont a besoin quelqu'un qui vient d'être licencié.

**C'est le trou. Et c'est précisément celui que « La Loi Avec Moi » comble.** Le positionnement
n'est pas un pari marketing : il répond à une lacune technique documentée.

## 2. CE QUI EXISTE DÉJÀ — et il y en a plus qu'attendu

### Pour la Belgique

| Projet | Ce qu'il fait | Licence / état |
|---|---|---|
| **`matematicsolutions/be-eli-mcp`** | serveur MCP : métadonnées et texte intégral d'une loi belge par coordonnées ELI, avec citation vérifiable ; FR / NL / DE | **Apache-2.0**, sur PyPI |
| **`Ansvar-Systems/Belgium-law-mcp`** | **5 775 lois, 142 743 dispositions**, recherche plein texte FTS5, vérification « toujours en vigueur ? », liens vers le droit UE | code ouvert, **mais le corpus pré-construit n'est PAS redistribué** |
| **`openjusticebe`** (ASBL belge) | API ECLI d'accès à la jurisprudence belge : Conseil d'État, Cour constitutionnelle, cours du travail | ASBL, legaltech à but non lucratif |
| **`rafjaf/juportal_crawler` + BetterJustel** | extrait les sommaires de la Cour de cassation depuis Juportal, les rattache à chaque article de loi via ELI | extension navigateur |
| **SPF Économie — jurisprudence PI** | base gratuite de décisions belges en propriété intellectuelle (droit d'auteur, brevets, marques) | publique, gratuite |

### Pour la France — l'écosystème est bien plus riche
`librejustice`, `juridix`, `berryer`, `openlegi`, `droit-francais-mcp` : moteurs de recherche en
langage naturel, graphes de citations, accès MCP. **Tous reposent sur Légifrance/DILA et Judilibre,
qui sont en open data.** La Belgique n'a pas cet équivalent — d'où l'écart.

## 3. LA QUESTION QUI N'EST PAS TRANCHÉE, ET QUI PEUT TOUT BLOQUER

**A-t-on le droit de redistribuer le texte de la loi belge ?**

`be-eli-mcp` écrit, honnêtement, que le statut de licence des données du Moniteur est
« **largement décrit comme CC0 par des catalogues tiers, mais non revérifié de façon indépendante**
auprès des conditions d'utilisation d'ejustice ».

Et `Ansvar-Systems` va plus loin : il **refuse de redistribuer son corpus**, invoquant des
contraintes de fouille de textes et de licence sur les sources amont — alors même que son code est
ouvert.

> **Deux projets sérieux, deux réserves convergentes.** Ce n'est pas un détail juridique : c'est la
> condition de possibilité d'une base de droit belge réutilisable. **NON VÉRIFIÉ** — et non
> vérifiable depuis cet environnement, `ejustice.just.fgov.be` étant bloqué par la politique réseau.

## 4. CE QUE ÇA CHANGE POUR LE PROJET

- **Ne pas reconstruire le socle.** Deux serveurs MCP belges existent, dont un sous Apache-2.0.
  Le travail utile n'est pas d'aller chercher les textes : c'est **la couche que personne ne fait —
  traduire une situation vécue en articles applicables**.
- **`openjustice.be` n'est pas un concurrent, c'est un allié possible.** ASBL belge, même mission
  d'ouverture de l'accès au droit. À approcher avant de dupliquer son travail.
- **Le contradicteur objecte, et c'est fondé :** ces projets sont jeunes, peu maintenus pour
  certains, et dépendent tous du **parsing HTML** d'un site officiel qui peut changer sans préavis.
  Bâtir dessus, c'est hériter de leur fragilité. Un changement de gabarit sur ejustice casse la
  chaîne entière, sans avertissement.

## 5. VOLET BREVETS — ce qui a avancé, et ce qui reste bloqué

**Avancé** : le SPF Économie publie une base gratuite de la **jurisprudence belge en propriété
intellectuelle** — brevets, marques, droit d'auteur, dessins et modèles. C'est une source utilisable
pour comprendre comment les juges belges appliquent ces droits.

**Toujours bloqué** : aucune recherche d'antériorité possible. Espacenet, registre OEB, BOIP,
TMview, EUIPO sont refusés par la politique réseau — mesuré le 2026-09-14, onze domaines, preuve au
journal du proxy. `analyste-brevets` reste **inopérant**.

---

## Passation

- **Fait** : cartographie des technologies d'accès au droit, belges et françaises ; identification
  du trou structurel belge (ELI sans recherche) ; repérage d'un allié potentiel ; découverte de la
  question de licence non tranchée.
- **Non fait** : la vérification du statut de licence des données du Moniteur — impossible d'ici,
  domaine bloqué. Aucune recherche d'antériorité brevets.
- **À qui** : Chaima — décider si l'on bâtit sur l'existant ou non, et si l'on approche
  `openjustice.be`. `analyste-financements` — les projets d'accès au droit relèvent souvent de
  subsides « numérique d'intérêt général ».
- **Confiance** : **ÉLEVÉE** sur l'existence des projets et sur l'absence de recherche plein texte
  (affirmée par deux projets indépendants et cohérente avec la documentation ELI officielle) ;
  **FAIBLE** sur le statut de licence des données, explicitement non revérifié par ses propres
  sources.

### Sources (lues le 2026-09-16)
- [be-eli-mcp](https://github.com/matematicsolutions/be-eli-mcp) · [sur PyPI](https://pypi.org/project/be-eli-mcp/)
- [Ansvar-Systems/Belgium-law-mcp](https://github.com/Ansvar-Systems/Belgium-law-mcp)
- [openjusticebe/ecli](https://github.com/openjusticebe/ecli) · [openjusticebe/data_api](https://github.com/openjusticebe/data_api)
- [rafjaf/juportal_crawler](https://github.com/rafjaf/juportal_crawler)
- [ELI — Belgique, documentation officielle](https://www.ejustice.just.fgov.be/eli/)
- [SPF Économie — jurisprudence belge en propriété intellectuelle](https://economie.fgov.be/fr/themes/propriete-intellectuelle/outils-de-recherche/base-de-donnees-de-la)
- [librejustice](https://github.com/librejustice/librejustice) · [juridix](https://github.com/Ktulu-Analog/juridix) · [berryer](https://github.com/demerys/berryer)
