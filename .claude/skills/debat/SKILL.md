---
name: debat
description: Orchestre le PARCOURS 2 du CODEX (une décision engageante — dépendance, fonctionnalité, prix, opportunité, protocole). À invoquer AVANT toute recommandation sur une décision qui engage. Lance POUR et CONTRE en parallèle, puis simulateur → arbitre → vérificateur → A-DECIDER, et laisse Chaima décider.
---

# Skill : debat (parcours 2 du CODEX)

Une décision engageante se présente (dépendance, fonctionnalité, prix, opportunité, changement de protocole).
Ce skill garantit qu'on ne « gagne » pas un débat, qu'on l'arbitre — le désaccord réel est la seule information utile.

## Séquence obligatoire (aucune étape sautée, surtout pour une idée « évidente »)

1. **POUR + CONTRE en parallèle, dans un seul message.** Lancer l'agent `avocat` (plaide POUR, sourcé) ET
   l'agent `contradicteur` (plaide CONTRE, permanent, non désactivable) EN MÊME TEMPS. Les lancer l'un après
   l'autre fait converger les positions et détruit le désaccord — précisément ce qu'on veut mesurer.
2. **simulateur-scenarios** — optimiste / réaliste / pessimiste. Jamais de pourcentage.
3. **arbitre-expert** — UNE recommandation claire. Doit dire ce que CHAQUE camp a gagné. Une objection écartée
   sans garde-fou qui la reprenne = décision non arbitrée, seulement gagnée. Recommande, n'exécute jamais.
4. **verificateur-verite** — s'applique à la sortie de tous : source datée, sinon « NON VÉRIFIÉ ».
5. **Consigner dans /codex/A-DECIDER.md** puis **Chaima décide** (§10 : un agent recommande, Chaima décide).

## Règle de désaccord (CODEX §14)
Quand deux agents se contredisent et que les faits ne départagent pas : **le verdict le plus prudent gagne par défaut.**
S'en écarter exige de dire pourquoi.

## Sortie — bloc de passation (CODEX §14)
    DE : arbitre-expert            POUR : CHAIMA
    OBJET : [une phrase décidable — action précise]
    VERDICT : [mot du §13]
    PARCE QUE : [le fait qui a emporté — fichier:ligne ou source datée]
    NON VÉRIFIÉ : [ce qui n'a pas pu être établi, ou « rien »]
    CE QUI CHANGERAIT MON AVIS : [le fait précis qui inverserait le verdict]

## NOTE D'INSTALLATION (2026-09-06)
Les agents référencés ici (`avocat`, `contradicteur`, `simulateur-scenarios`, `arbitre-expert`,
`verificateur-verite`) font partie des 21 rôles CODEX **pas encore créés** dans ce dépôt (décision Chaima
« protocole + structure d'abord »). Tant qu'ils ne sont pas créés/réconciliés (voir /codex/A-DECIDER.md),
appliquer la séquence ci-dessus manuellement, en une seule passe, sans sauter le CONTRE.
