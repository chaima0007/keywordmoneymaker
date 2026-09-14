> **Rapatrié le 2026-09-14 depuis `chaima0007/test`.** Ces documents vivaient dans le dépôt de CompeteIQ
> parce que c'était le seul où j'avais un accès en écriture — ce qui est exactement la faute décrite par la
> fiche **E-15** (contenu d'un projet déposé dans le dépôt d'un autre). L'accès au dépôt Caelum ayant été
> obtenu depuis, la faute est corrigée à sa source plutôt que tolérée.
> L'historique complet du raisonnement reste sur la branche `claude/adoring-albattani-ue4vtz` du dépôt test.

# Charte consolidée — chaîne Veille, Brevets, Technologies & Capitaux
**2026-09-11-22h50 (Europe/Brussels) · remplace la LECTURE de `CHARTE-CHAINE-VEILLE.md`, sans le supprimer**

## SYNOPSIS
Consolidation demandée par Chaima. La charte d'origine a reçu douze sections en une journée : elle est
devenue illisible, ce qui est exactement le travers de sa propre fiche E-04. Ce document est **la seule
lecture à jour**. Il est court par construction : entre-temps, le PROTOCOLE CODEX a repris à son compte
une bonne partie de ce que la charte définissait, et le reste vit dans le dépôt. **Un document qui
consolide doit rétrécir.**

`CHARTE-CHAINE-VEILLE.md` est conservé comme historique du raisonnement — rien n'est supprimé.

---

## 1. OÙ EST LA VÉRITÉ — à lire avant tout
| Question | Fichier qui fait foi |
|---|---|
| Que doit faire tel agent ? | `.claude/agents/<nom>.md` (dépôt Caelum) |
| Qui couvre quoi, et avec quoi ne pas le confondre ? | `codex/agents-correspondance.md` |
| Quelles fautes ne pas reproduire ? | `.claude/BASE-ERREURS.md` — **21 fiches, fait foi** |
| Registre d'erreurs du §12 | `🔴 ERREURS.md` — **index généré**, ne s'édite pas à la main |
| Markdown ou Python : qui possède quoi ? | `.claude/FRONTIERE-SUBSTRATS.md` |
| Règles communes à tous les agents | `CLAUDE.md` — PROTOCOLE CODEX §1-§15, puis §0-§7 du projet |

Cette charte ne redéfinit **rien** de ce qui figure ci-dessus.

## 2. CE QUE LE CODEX A REPRIS — et que cette charte ne dit plus
Honnêteté de consolidation : ces règles étaient dans la charte, le CODEX les fait mieux ou plus
strictement. **Elles ne se lisent plus ici.**

| Ancienne section | Reprise par | Remarque |
|---|---|---|
| §7.1 condition d'arrêt (anti-boucle) | CODEX §5 + `superviseur-vigie` | Plus strict que ma version : « un rapport pour dire qu'il n'y a rien à dire est une faute contre le protocole » |
| §2 vérité, sources datées, « NON VÉRIFIÉ » | CODEX §13 + `verificateur-verite` | Le §13 impose en plus l'interdiction des pourcentages |
| §5 audit de la chaîne | `gardien-controle-final` + auto-audit CODEX | |
| §6 les trois rôles (DÉPOSANT, HORLOGER, ÉLAGUEUR) | `deposant`, `horloger`, `croque-mort` | ÉLAGUEUR abandonné, `croque-mort` a la même mission |
| §7.2 articulation sous `meta-orchestrateur` | inscrit dans `chef-orchestre-veille` | |
| Aucun merge, aucun engagement sans accord | CODEX §10 | Liste complète de ce qui reste strictement humain |

## 3. CE QUI RESTE PROPRE À CETTE CHAÎNE — les seules règles encore définies ici

### 3.1 Divulgation — la règle la plus coûteuse à enfreindre
En Europe, **pas de délai de grâce** (art. 54 CBE ; l'art. 55 ne couvre que la divulgation abusive et les
expositions officielles reconnues, 6 mois). Un `git push` vers un dépôt **public**, une mise en ligne, un
post, une démo : chacun est une divulgation qui détruit la nouveauté **irréversiblement**.

`keywordmoneymaker` est **public**. Rien de brevetable potentiel n'y entre avant dépôt.
Agent responsable : `protecteur` — droit de veto, que lui seul oppose et que seule Chaima lève.
À ne pas confondre avec `conservateur-secrets` : sa fuite est technique et réparable par rotation ;
celle-ci est juridique et sans correctif.

### 3.2 Nommage des documents Drive
Le CODEX ne définit pas de convention de titre. Celle-ci reste en vigueur :
```
AAAA-MM-JJ-HHhMM — [Projet] — [Catégorie] — [Sujet précis]
```
`TZ="Europe/Brussels" date '+%Y-%m-%d-%Hh%M'` · **titre ≤ 120 caractères, sujet ≤ 60.**
Le verdict va **dans** le document, jamais dans le titre : un titre est une adresse, pas un rapport
(fiche E-04, née de titres de 300 à 400 caractères).

### 3.3 Sauvegarde — état réel, pas intention
Règle : Drive + dépôt GitHub **privé si sensible** + copie locale.
**État au 2026-09-11 :** le dépôt disponible est public, `caelum-coffre` n'existe pas encore (droit de
création refusé à l'intégration, 403). Donc pour tout contenu sensible : **Drive + copie locale
uniquement**. La règle n'est pas applicable en entier, et le dire fait partie de la règle (fiche E-09).

### 3.4 Couverture des offices de brevets — première vague bornée
Documenter 22 offices par trouvaille n'est pas soutenable, et c'est redondant : Espacenet et WIPO
Patentscope donnent déjà les familles internationales, donc les équivalents nationaux.
- **Première vague (5) :** OEB/Espacenet · WIPO Patentscope · USPTO · DPMA · CNIPA.
- Descente au registre national **seulement** quand une famille précise le justifie.
- Les 22 dossiers Drive restent créés : c'est la cadence qui est bornée, pas la couverture.
- **Seul le registre fait foi.** Une recherche web sans résultat s'écrit « NON VÉRIFIÉ », jamais
  « aucune antériorité » (fiche E-13).

### 3.5 Structure Drive du projet
`🗂️ Caelum — Journal d'Audit` → `Veille & Opportunités` → 8 catégories + bibliothèque à 22 juridictions
+ `Opportunités académiques non exploitées` + `Calendrier des expirations à venir`. Par projet, jamais
mélangé (fiche E-15).

## 4. ÉTAT DU TRAVAIL AU 2026-09-11
**Fait** — structure Drive (33 dossiers) · verdict de brevetabilité n°1 (NO-GO brevet, motifs art. 52/54/56
CBE ; valeur réelle dans le droit *sui generis* des bases de données et la marque) · base d'erreurs
21 fiches, lue par les deux substrats · frontière des substrats · Option 0 (le domaine ne sert plus que
Caelum) · Option B (cloisonnement bloquant en CI) · 56 agents réconciliés, 0 suppression.

**Non commencé, et bloqué par l'environnement** — le rôle **SCANNER** (recherche d'antériorité réelle).
Les registres sont inaccessibles depuis l'environnement d'agent : Espacenet, Patentscope, USPTO, DPMA et
EUIPO répondent tous HTTP 000, refus au gateway du proxy. Ce n'est pas un manque de méthode : les axes de
recherche et les priorités d'offices sont posés (§3.4 et le `Calendrier` au Drive, honnêtement à 0 entrée).
C'est un accès à ouvrir, ou un travail à faire depuis un navigateur.

**Chez Chaima** — `uv run python main.py` · création de `caelum-coffre` · vérification de la marque au
registre (TMview/BOIP/EUIPO) · vérification du rendu du site dans un navigateur · `LICENSE` du dépôt
(fiche E-08, toujours ouverte).

---
*Un document = un événement. Cette consolidation est un ajout : `CHARTE-CHAINE-VEILLE.md` reste lisible
comme historique, et aucune de ses sections n'a été supprimée.*
