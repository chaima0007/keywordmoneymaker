# /codex/rapports/ — les rapports complets, déposés pour être contredits

Directive de Chaima du 2026-09-14 : *« je veux que tu sois surveillé aussi pour être sûr ».*

## Pourquoi ce dossier existe

Jusqu'ici, les rapports complets n'existaient que dans une conversation. Conséquence exacte :
**aucune surveillance ne pouvait les atteindre.** Ni la méta-surveillance du soir, qui ne lit que
le Drive et le dépôt ; ni l'intégration continue, qui ne lit que des fichiers ; ni une relecture
trois semaines plus tard. Un rapport invérifiable par construction n'est pas un rapport, c'est
une affirmation.

Un rapport déposé ici peut être recoupé, cité, contredit, et vieillir mal au vu de tous.

## Les quatre niveaux de surveillance, du plus fort au plus faible

Nommés dans cet ordre parce que les confondre est la faute elle-même.

1. **Contrôle mécanique en intégration continue** — `scripts/verifier_rapports.py`, bloquant.
   Il s'exécute sans l'agent, ne se laisse pas convaincre, et refuse la fusion. Le plus fort.
2. **Session séparée** — la Routine « Méta-surveillance », qui relit avec un autre contexte et
   peut contredire. Forte, mais elle ne voit que ce qui est écrit : d'où ce dossier.
3. **Sous-agent appelé par l'agent lui-même** (CONTRADICTEUR, VÉRIFICATEUR-VÉRITÉ). Utile, mais
   c'est le même opérateur qui choisit de l'appeler et qui lit sa réponse. **Faible.**
4. **La phrase de contrôle honnête du §2 ter.** Écrite par la partie surveillée, sur elle-même.
   **Ne prouve rien seule.** Elle a de la valeur uniquement adossée aux trois niveaux au-dessus.

## Le défaut structurel, dit et non masqué

`scripts/verifier_rapports.py` est écrit par la partie qu'il surveille. Ses seules défenses :
il est mécanique, il est court, il est relisible par un humain en dix minutes, et il n'est pas
fusionné par son auteur. **Si un jour un rapport échoue à ce contrôle, la règle est : corriger
le rapport, jamais assouplir le contrôle.** Tout assouplissement de ce fichier doit être motivé
dans le message de commit et signalé à Chaima.

Premier usage, le 2026-09-14 : le contrôle a immédiatement pris son auteur en défaut sur deux
points — un « pas VÉRIFIÉ » au lieu du « NON VÉRIFIÉ » imposé par le §13, et un chemin cité de
façon ambiguë. Deux fautes réelles, deux corrections du rapport.

## L'exception à la règle — et elle est arrivée le premier jour

La règle « corriger le rapport, jamais le contrôle » vaut tant que le contrôle a raison. Le
2026-09-14, à sa **première exécution réelle en intégration continue**, il a eu tort : il a annoncé
qu'un commit n'existait pas alors qu'il s'agit de la tête de `main`. Le workflow clonait en
superficiel ; l'outil confondait « je ne vois pas » et « ça n'existe pas ».

La correction a donc porté sur le contrôle — mais dans le seul sens autorisé : **le durcir, jamais
l'assouplir.** L'historique complet est désormais récupéré, et le script détecte un dépôt superficiel
pour **s'arrêter en le disant** plutôt que de rendre un verdict qu'il n'a pas les moyens de rendre.
Un vert signifie maintenant qu'une vérification a réellement eu lieu.

La règle complète, telle qu'elle s'énonce après cet épisode :

> Quand le contrôle échoue, on corrige le rapport. Si le contrôle est **prouvé** faux, on le corrige
> en le rendant **plus strict ou plus honnête sur ses limites**, jamais plus permissif — et on le
> signale à Chaima avec la preuve. Un assouplissement non motivé est une régression de sécurité.

Fiche `E-25` de la base d'erreurs. Leçon annexe : le contrôle avait passé sept pièges et un témoin,
et c'est sa première exécution dans le monde réel qui l'a pris en défaut. Un dispositif n'a pas fait
ses preuves tant qu'il n'a pas tourné là où il doit vivre.

## Ce que le contrôle ne fait pas

Il prouve que les traces citées existent. **Il ne prouve pas que les conclusions sont justes.**
Un commit peut exister et ne rien valoir. Une URL peut être valide et pointer sur un échec.
La lecture humaine reste nécessaire, et c'est pour cela qu'elle reste au §10 du CODEX.

## Convention

`AAAA-MM-JJ-HHhMM — [Projet] — [Catégorie] — [Sujet précis].md`

Un document = un événement. **AJOUT, jamais d'écrasement.**
