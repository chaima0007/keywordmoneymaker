# Les sources tier-1 ne sont pas atteignables depuis une session d'agent

**Phrase de contrôle honnête.** Aucun document comparable n'existe : c'est la première fois que la
contrainte réseau est **mesurée** au lieu d'être répétée. La condition d'arrêt a fonctionné — j'ai
arrêté la veille faute de cible désignée, et employé ce temps à vérifier une affirmation que je
répétais depuis ce matin sans l'avoir testée moi-même aujourd'hui. **ÉLAGUEUR saisi : non — rien à
élaguer, mais une correction de portée à faire sur des documents existants (§4).**

**Consigne n°1 servie : chaîne Veille, Brevets, Technologies & Capitaux.** La cible est en attente,
mais ce constat vaut pour tous les projets et conditionne le volet BREVETS de la mission.

- **Projet** : Empire Chaima (transverse) · **Catégorie** : Contrôle
- **Mesuré le** : 2026-09-14, entre 22h25 et 22h35 (Bruxelles)

---

## 1. CE QUI A ÉTÉ MESURÉ, ET COMMENT

Onze domaines ont été appelés depuis cette session, avec les deux outils réellement utilisés pour
la veille. Le proxy de sortie tient son propre journal, consultable par
`curl -sS "$HTTPS_PROXY/__agentproxy/status"` — **c'est lui la preuve, pas mon interprétation.**

Sa réponse, pour chacun des onze : `gateway answered 403 to CONNECT (policy denial)`.

| Domaine | Ce que c'est | État |
|---|---|---|
| `worldwide.espacenet.com` | recherche de brevets, OEB | **BLOQUÉ** |
| `register.epo.org` | registre européen des brevets | **BLOQUÉ** |
| `api.epo.org`, `data.epo.org` | interface machine de l'OEB (OPS) | **BLOQUÉ** |
| `patentscope.wipo.int` | base mondiale OMPI | **BLOQUÉ** |
| `patents.google.com` | copie Google des brevets | **BLOQUÉ** |
| `www.boip.int` | marques Benelux et i-DEPOT | **BLOQUÉ** |
| `www.tmdn.org` | TMview | **BLOQUÉ** |
| `euipo.europa.eu` | marques de l'Union | **BLOQUÉ** |
| **`www.ejustice.just.fgov.be`** | **Moniteur belge / Justel** | **BLOQUÉ** |
| **`economie.fgov.be`** | **SPF Économie** | **BLOQUÉ** |
| **`www.wallonie.be`** | **portail de la Wallonie** | **BLOQUÉ** |

Confirmé avec les deux outils : `curl` et l'outil de lecture de page renvoient tous deux
`EGRESS_BLOCKED`. Ce n'est **pas** un incident passager ni une limite de `curl` — c'est une
**décision de politique réseau**, et le manuel du proxy est explicite : *« do not retry organization
policy denials (403/407) — report them instead. »* C'est ce que fait ce document.

## 2. LE VOLET « BREVETS » DE LA MISSION EST STRUCTURELLEMENT IMPOSSIBLE ICI

Ta consigne nomme quatre objets : technologies, **brevets**, opportunités, capitaux.

**Aucune recherche d'antériorité, aucune liberté d'exploitation, aucune vérification de marque ne
peut être faite depuis cet environnement.** Ce n'est pas une question de compétence ou de méthode :
les registres sont fermés à la porte du réseau. Le rôle `analyste-brevets` créé aujourd'hui porte
cette limite dans sa mission — il ne peut produire, en l'état, que du **PLAUSIBLE**.

## 3. CE QUI MARCHE ENCORE — et pourquoi ce n'est PAS équivalent

Les **moteurs de recherche** fonctionnent, parce que la page n'est pas chargée par cette session :
elle est récupérée par les serveurs du moteur, qui m'en renvoient une copie.

**Conséquence, et elle est sérieuse :** quand un rapport dit « source vérifiée sur
ejustice.just.fgov.be », ce qui a réellement été lu est **la copie d'un tiers**, pas le texte à la
source. Le tiers peut être ancien, partiel, ou porter sur une version abrogée.

C'est exactement la fiche **E-13** — *une recherche web n'est pas un registre* — mais on en connaît
désormais le **mécanisme**, et non plus seulement le principe.

## 4. CE QUE CELA CHANGE POUR LES DOCUMENTS DÉJÀ PRODUITS

Il faut le dire sans dramatiser et sans l'escamoter.

- Les fiches juridiques produites depuis juillet portent la mention « sources tier-1 **vérifiées
  vivantes** ». **Cette mention est plus forte que ce qui a pu être fait** : aucune session d'agent
  ne pouvait ouvrir le Moniteur belge.
- **Cela ne rend pas ces fiches fausses.** Leur contenu peut être parfaitement exact, et il est
  recoupé entre plusieurs sources. Mais la **preuve** n'est pas celle qui est annoncée.
- Mon propre rapport de veille de 21h45 cite des portails officiels : il relève de la même réserve,
  et je la lui applique plutôt que de l'épargner parce qu'il est de moi.

**Correction de vocabulaire à appliquer partout** : tant que l'accès direct n'existe pas, le mot
juste est **CONFIRMÉ** (recoupé par deux sources indépendantes) — jamais **VÉRIFIÉ** (`CLAUDE.md` §13),
qui suppose d'avoir constaté soi-même à la source.

*(Note : le contrôle des rapports a signalé cette ligne, parce qu'elle contient le mot « VÉRIFIÉ » (`R7`)
sans trace. Il a raison de ne pas savoir distinguer le mot EMPLOYÉ du mot CITÉ — c'est le motif de
la fiche E-28, un contrôle qui se déclenche sur un texte parlant de lui-même. La ligne porte donc
maintenant sa référence, plutôt que d'assouplir la règle.)*

## 5. LE REMÈDE — il est entre les mains de Chaima, et seulement elles

La politique de sortie réseau est **choisie à la création de l'environnement** d'exécution. Ce n'est
pas un réglage d'agent : aucun agent ne peut l'élargir, et aucun ne doit essayer de la contourner.

Ce qu'il faut demander, c'est un environnement dont la politique autorise ces domaines :

```
worldwide.espacenet.com    register.epo.org    api.epo.org    data.epo.org
patentscope.wipo.int       www.boip.int        www.tmdn.org   euipo.europa.eu
www.ejustice.just.fgov.be  economie.fgov.be    www.wallonie.be
justice.belgium.be         www.mi-is.be        1890.be        economie-emploi.brussels
```

Documentation de référence : https://code.claude.com/docs/en/claude-code-on-the-web

**Sans cet accès, deux choses restent impossibles, quel que soit le projet choisi :** le volet
brevets de la mission, et l'affirmation « vérifié à la source » sur une norme juridique.

---

## Passation

- **Fait** : mesure réelle de onze domaines avec deux outils ; preuve tirée du journal du proxy et
  non d'une déduction ; correction de portée appliquée aux documents existants, y compris les miens.
- **Non fait** : rien de ce qui dépend des registres. Ce n'est pas un retard, c'est une impossibilité.
- **À qui** : Chaima — élargir la politique réseau de l'environnement est sa décision, et personne
  d'autre ne peut la prendre. `analyste-brevets` reste inopérant jusque-là.
- **Confiance** : **ÉLEVÉE**. Onze domaines, deux outils, journal du proxy à l'appui, et le manuel
  du proxy qui qualifie lui-même la réponse de « policy denial ».
