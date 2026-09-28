# La publication défensive : le domaine est rendu inbrevetable en temps réel

**Contrôle honnête d'entrée.** Ce rapport annonce un quatrième croisement mort, mais il ne
ressemble pas aux trois premiers et c'est tout son intérêt. X-01 et X-02 sont morts de ma faute
(domaines trop proches, `E-31`). X-03 est mort parce que l'idée était juste et faite depuis 1990.
X-04 meurt d'une cause nouvelle, qui change la stratégie et pas seulement le candidat. Aucun
document quasi identique dans `codex/rapports/`. Pas de croque-mort à convoquer.

**Au service de la consigne n°1** en vigueur (`codex/CONSIGNE-N1.md`). Réponse à la première des
trois questions ouvertes depuis le 2026-09-20 et jamais traitée : est-ce que quelqu'un a déjà fait
la couche de contradiction ?

---

## 1. La réponse est oui, et cinq fois

Le trou établi sur les douze briques — toutes vérifient que la tâche s'est **terminée**, aucune
que la conclusion est **juste** — est comblé par au moins cinq travaux publiés.

**US12676749**, publié le 2026-07-07, « Pre-inference execution compliance for artificial
intelligence systems ». Revendication 1 : porte d'exécution **fail-closed** avant inférence,
verdict d'autorisation **signé par un quorum**, registre d'arbitrage immuable, état de verrouillage
persistant, refus avant toute inférence ou action en aval. C'est la porte de contradiction, en
version cryptographique, et la revendication est large.

**draft-krausz-verification-state-01**, brouillon IETF. Spécifie une famille de contraintes
`verification.*` : porte pré-action fail-closed, reçu signé, et — décisif — un champ
`v_adversarial_result` avec une table de vérité où l'état `not_checked` donne **halt**. Le
brouillon écrit noir sur blanc : *« un état adverse non sondé n'est pas équivalent à résilient ;
l'incertitude DOIT arrêter »*. C'est exactement la règle que je croyais nôtre.

**Chauhan, « Ratification by Re-execution »**, janvier 2026. Protocole à deux agents où le
vérificateur **exécute lui-même** la chaîne de production et **publie son verdict avant de lire**
l'auto-vérification de l'implémenteur. Journaux d'écriture unidirectionnels, un seul auteur par
fichier, rétractation publique et permanente. C'est la propriété d'indépendance, formalisée.

**Surisetti, « DCTP »**, juillet 2026. Objets de contexte versionnés, verrouillage conditionné par
un graphe de dépendances, interface strictement propositionnelle, et **conservation du candidat
perdant** dans l'historique plutôt que son rejet. Cite lui-même **WO2021084510A1** (2021) pour le
gating par confiance.

**Et une discussion publique de praticiens** qui pose, en langage courant, le jeton de veto, la
dette de preuve avec délai, le registre de dissension qui survit à l'exécution, et le risque du
dissident de mauvaise foi qui gèle la synthèse.

## 2. Mais la cause de mort est nouvelle, et c'est elle qui compte

Le premier résultat de la recherche est un dépôt GitHub intitulé **`verdict-gated-merge-deploy-train`**
dont le fichier d'en-tête porte, en gras, la mention :

> **Public prior art.**

Il contient, de son propre aveu, *« une divulgation habilitante d'environ cinq mille mots avec des
revendications »*, plus un document de comparaison à l'art antérieur. Son mécanisme : une fusion
ne se fait que si un persona relecteur **et** un persona testeur ont écrit `verdict='pass'` dans un
registre, exécuté par un ordonnanceur **hors du bac à sable** des agents qui écrivent le code.

**Ce dépôt n'existe pas pour déposer un brevet. Il existe pour empêcher quiconque d'en déposer un.**
C'est une publication défensive, rédigée comme une demande de brevet et publiée gratuitement pour
détruire la nouveauté de tout dépôt ultérieur.

## 3. Ce que ça dit du domaine, et c'est stratégique

Dans les brevets, la nouveauté est détruite par toute divulgation antérieure — **y compris une
divulgation gratuite faite exprès pour ça**. Or dans l'espace des agents autonomes :

- les mécanismes sont publiés **en semaines**, pas en années ;
- une partie des acteurs publie **délibérément pour bloquer** ;
- les normalisateurs publient en brouillon IETF, ce qui est de l'art antérieur ;
- les articles font eux-mêmes leur propre examen de nouveauté — le DCTP conclut candidement qu'il
  est *« une synthèse plutôt qu'une percée »*.

**Conséquence :** chercher un brevet logiciel dans ce domaine depuis un bureau, sans laboratoire et
sans équipe, a un rendement proche de zéro. Ce n'est pas de la malchance sur quatre tirages. C'est
la structure du terrain.

## 4. Ce qui survit, et qui n'est pas une invention

Une chose n'apparaît dans aucun des cinq travaux : le **sas de provenance et de licence** tel que
construit ici. Lire les fichiers et non l'étiquette, attraper la licence scindée code/poids,
traiter `NOTICE` comme une attribution et non une licence, distinguer « ne conclut pas » de
« refusé », et rester **neutre en origine** tout en séparant le contrôle de sanctions.

Ce n'est **pas** le même domaine : c'est de la chaîne d'approvisionnement logicielle, pas de la
vérification d'agents. Codes CPC distincts, littérature distincte.

**Ce n'est pas pour autant un candidat.** L'espace SBOM, SPDX et analyse de licences est industriel
et ancien. Aucune recherche d'antériorité n'a été faite dessus, et l'annoncer comme piste sans
l'avoir testée serait exactement l'erreur que le registre des croisements interdit.

## 5. Ce qui n'est pas prouvé

Une antériorité trouvée suffit à tuer ; elle ne suffirait pas à valider. Aucune recherche par codes
CPC n'a été possible — les registres restent inatteignables. Aucune revendication lue mot à mot
hors des extraits cités. Aucune analyse ici n'est un conseil juridique.

Et une limite propre à ce rapport : je conclus à un **comportement de domaine** à partir d'un seul
dépôt explicitement défensif. Un seul cas ne fait pas une pratique. Est VÉRIFIÉ : `gusitllc/verdict-gated-merge-deploy-train` existe et porte en en-tête
« Public prior art ». Que ce soit une pratique répandue est PLAUSIBLE, confiance MODÉRÉE.

## 6. Ce qui attend Chaima

La décision n'est plus « quel domaine » mais **« est-ce qu'on continue à chercher des brevets
logiciels »**. Quatre croisements, quatre morts, et la quatrième cause est structurelle et ne
s'améliorera pas. Je propose et je ne tranche pas.
