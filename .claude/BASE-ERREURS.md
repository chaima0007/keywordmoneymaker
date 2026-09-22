# BASE D'ERREURS — chaîne Veille, Brevets, Technologies & Capitaux

> **À CONSULTER AVANT D'AGIR.** Obligatoire pour tout agent de la chaîne veille, à chaque entrée en
> action. Demande de Chaima du 2026-09-11 : « pour que les mêmes fautes ne soient jamais reproduites
> deux fois ».
>
> Créée le 2026-09-11-16h55 (Europe/Brussels). **Ajout uniquement, jamais d'écrasement.**
> Miroir Drive : « Synergies inter-agents ». Ce fichier est la copie de référence.

## COMMENT S'EN SERVIR (30 secondes, pas une lecture intégrale)
1. Lis l'**INDEX** ci-dessous et repère les erreurs dont le *déclencheur* ressemble à ce que tu vas faire.
2. Va lire ces fiches-là, pas les autres.
3. Si ton action correspond à un **signal de détection** listé, applique la contre-mesure AVANT d'agir.
4. Si tu commets ou découvres une erreur nouvelle : **ajoute une fiche**, ne modifie pas les existantes.

## INDEX

| ID | Erreur | Quand ça te menace | Rôle qui en répond |
|---|---|---|---|
| E-01 | Règle écrite puis ignorée pendant un mois | Tu crées un document | BOUSSOLE · GARDIEN |
| E-02 | Faux positif répété ~30 fois pendant 2 semaines | Tu reconduis un constat antérieur | GARANT |
| E-03 | Métadonnée trompeuse prise pour un échec/succès | Tu crées un fichier au Drive | tous |
| E-04 | Titre de document de 300-400 caractères | Tu nommes un document | BIBLIOTHÉCAIRE |
| E-05 | Index censé être tenu à jour, laissé obsolète | Tu ajoutes à une collection indexée | MONSIEUR PROPRE |
| E-06 | Deux conventions concurrentes coexistant | Tu appliques une règle de forme | ARCHITECTE |
| E-07 | Inventaire incomplet d'un système existant | Tu conclus sur « ce qui existe déjà » | GARDIEN |
| E-08 | Dépôt public sans LICENSE | Tu publies du code | DÉPOSANT |
| E-09 | Dépôt public utilisé comme sauvegarde de sensible | Tu sauvegardes une trouvaille | PROTECTEUR · REMPART |
| E-10 | Encodage d'entité HTML pris au littéral | Tu passes un titre à une API | tous |
| E-11 | Clone superficiel pris pour l'historique réel | Tu datures quoi que ce soit depuis git | HORLOGER |
| E-12 | Conversion Markdown → Google Docs qui altère | Tu déposes un document au Drive | PLUME · BIBLIOTHÉCAIRE |
| E-13 | Recherche web prise pour une recherche au registre | Tu conclus sur un brevet, une marque | SCANNER · DÉPOSANT · GARANT |
| E-14 | Deux racines créées pour un même projet | Tu crées un dossier | ARCHITECTE |
| E-15 | Contenu d'un projet déposé dans le dépôt d'un autre | Tu écris un fichier | BOUSSOLE |
| E-16 | Service en échec pris pour service inexistant | Un outil ne répond pas | tous |
| E-17 | Documents internes publiés avec le site | Tu configures une publication, un déploiement | PROTECTEUR · REMPART |
| E-18 | Deux sources de vérité pour la même question | Tu ajoutes une source d'information à côté d'une existante | ARCHITECTE · GARDIEN |
| E-19 | Manipulation git pendant une fusion en cours | Tu fais autre chose au milieu d'un merge non finalisé | tous |
| E-23 | Règle appliquée aux agents mais pas à l'ordonnanceur qui les déclenche | Tu poses une condition d'arrêt, ou une Routine tourne à vide | croque-mort · superviseur-vigie |
| E-24 | Un test a détruit le travail non commité | Tu écris un test qui touche à l'état du dépôt | tous |
| E-20 | Outil d'audit pointé sur la mauvaise cible | Tu lances un scan, un audit, un test de dépendances | tous |
| E-21 | État d'un site déduit du dépôt, pas du live | Tu conclus sur ce que voit un visiteur | GUETTEUR · verificateur-verite |
| E-22 | Défaut annoncé sans avoir été constaté | Tu rapportes un bug que tu n'as pas reproduit | GARANT · tous |

---

## E-01 — Une règle écrite le 13/07 a été ignorée pendant un mois
**Constaté le** 2026-09-11 · **Survenu** 2026-07-13 → 2026-08-11
**Ce qui s'est passé.** Le document « LISEZ-MOI — Règles du journal » (Drive, 2026-07-13) posait
explicitement : « avant de créer un fichier, on vérifie qu'il n'existe pas déjà », « on ne recopie pas ce
qui est déjà écrit ailleurs », « si on retravaille le même jour sur le même sujet → on complète l'entrée
existante ». Une trentaine de journaux « boucle-caelum » ont enfreint cette règle entre le 28/07 et le
11/08, tous porteurs du même message : « backlog SATURÉ → 0 nouvelle pièce · SILENCE · rien de neuf ».
**Cause racine.** Pas l'absence de règle — l'absence d'un rôle **habilité à arrêter** une boucle. Chaque
passage produisait consciencieusement son artefact parce que rien n'autorisait à ne rien produire.
**Signal de détection.** Tu es sur le point de créer un document dont le contenu dira « rien de nouveau ».
**Contre-mesure.** Condition d'arrêt (charte §7.1) : **aucun document neuf quand l'état est inchangé** ;
on met à jour un état courant unique. Trois cycles sans changement → saisir l'ÉLAGUEUR.
**Leçon transférable.** Une règle sans rôle qui la fait appliquer n'est pas une règle, c'est un vœu.

## E-02 — Un faux positif a survécu deux semaines et a été répété ~30 fois
**Constaté le** 2026-08-10 (corrigé) · **Survenu** 2026-07-28 → 2026-08-10
**Ce qui s'est passé.** Une trentaine de journaux ont affirmé « PR#2 NON mergée », alors que la PR était
fusionnée depuis le **17/07/2026 à 18h59** (API GitHub : state closed, merged true, merged_by chaima0007).
Conséquence : Chaima a reçu pendant deux semaines l'information qu'un merge l'attendait alors que non.
**Cause racine — technique.** `refs/pull/<n>/head` **persiste après la fusion**. Sa présence a été lue
comme « PR non mergée ». C'est un contresens sur la sémantique de la ref.
**Cause racine — organisationnelle.** Personne ne possédait la question « **est-ce que c'est encore
vrai ?** ». Chaque passage reconduisait le constat du précédent, qu'il prenait pour une preuve.
**Signal de détection.** Tu es sur le point d'écrire un constat que tu n'as pas vérifié toi-même ce run,
ou de reconduire une conclusion antérieure.
**Contre-mesure.** Rôle GARANT : « le contrôleur l'a validé » n'est **pas** une preuve. Pour un état de
PR, interroger l'API (`state`, `merged`, `merged_by`) — **jamais** déduire d'une ref. Et un constat
reconduit plus de deux cycles doit être re-prouvé à la source, pas recopié.
**Leçon transférable.** La répétition n'est pas une confirmation. Trente documents d'accord entre eux
peuvent avoir tort ensemble s'ils descendent tous de la même mesure non revérifiée.

## E-03 — Une métadonnée trompeuse a failli faire annoncer un échec
**Constaté le** 2026-09-11
**Ce qui s'est passé.** L'API Google Drive a renvoyé `fileSize: "1"` après la création d'un document de
~10 Ko. Lu tel quel, cela signifiait « document vide, création échouée ». Le read-back a montré que le
contenu était **complet et intègre** : la métadonnée était fausse, pas la création.
**Cause racine.** Confiance accordée au code de retour d'une API plutôt qu'à l'état réel de l'objet.
**Signal de détection.** Tu viens de créer, d'écrire ou de pousser quelque chose et tu vas l'annoncer.
**Contre-mesure.** **Read-back systématique avant d'annoncer** (déjà dans le `CLAUDE.md` §0, ici
confirmé par un cas réel). Vaut dans les deux sens : ne pas annoncer un succès non relu, et ne pas
annoncer un échec sur la seule foi d'une métadonnée.
**Leçon transférable.** Un accusé de réception n'est pas une preuve de contenu.

## E-04 — Titres de documents de 300 à 400 caractères
**Constaté le** 2026-09-11
**Ce qui s'est passé.** Les titres des journaux « boucle-caelum » embarquent le verdict complet, les
hashs de commit et l'état de la PR. Résultat : illisibles dans une liste, non triables, et le contenu du
titre devient obsolète alors que le titre, lui, ne change plus.
**Cause racine.** Confusion entre **nommer** un document et le **résumer**.
**Signal de détection.** Ton titre contient un verdict, un hash, un état, ou dépasse 120 caractères.
**Contre-mesure.** `AAAA-MM-JJ-HHhMM — [Projet] — [Catégorie] — [Sujet précis]`, titre ≤ 120 caractères,
sujet ≤ 60. Le verdict va **dans** le document.
**Leçon transférable.** Un titre est une adresse, pas un rapport.

## E-05 — Un index censé être tenu à jour est resté obsolète
**Constaté le** 2026-09-11
**Ce qui s'est passé.** Le LISEZ-MOI du 2026-07-13 contient un « Index des entrées » avec la mention
« *cet index est mis à jour à chaque nouvelle entrée* ». Il ne comporte **qu'une ligne**, du 13/07, alors
que le dossier compte au moins 9 documents postérieurs.
**Cause racine.** Un index tenu à la main, sans rôle qui en réponde, dérive silencieusement — et un index
faux est pire qu'une absence d'index, parce qu'on lui fait confiance.
**Signal de détection.** Tu ajoutes un élément à une collection qui possède un index ou un sommaire.
**Contre-mesure.** MONSIEUR PROPRE vérifie les index à chaque passage. Toute promesse de tenue à jour
dans un document est une dette : soit un rôle la porte, soit on retire la promesse.
**Leçon transférable.** Ne promets pas dans un document ce qu'aucun rôle n'est chargé de tenir.

## E-06 — Deux conventions de nommage concurrentes ont coexisté
**Constaté le** 2026-09-11
**Ce qui s'est passé.** Le LISEZ-MOI du 13/07 impose `AAAA-MM-JJ — Journal d'audit — [sujet court]`.
L'instruction de Chaima du 11/09 impose `AAAA-MM-JJ-HHhMM — [Projet] — [Catégorie] — [Sujet précis]`.
Les deux ont coexisté, alors que le `CLAUDE.md` §4 dit : « on ne laisse jamais deux chiffres différents
coexister : on tranche, on corrige, on date ».
**Cause racine.** Une nouvelle règle a été adoptée sans vérifier si une règle antérieure occupait la place.
**Signal de détection.** Tu appliques une convention de forme, ou tu en adoptes une nouvelle.
**Contre-mesure.** Avant d'adopter une règle : chercher celle qui existe déjà. En cas de conflit,
trancher explicitement, dater, et signaler la règle supplantée — sans modifier le document d'origine.
**Leçon transférable.** Une règle nouvelle doit nommer la règle qu'elle remplace, sinon les deux vivent.

## E-07 — Inventaire incomplet : deux flottes d'agents, une seule documentée
**Constaté le** 2026-09-11
**Ce qui s'est passé.** Le dépôt contient **deux** flottes distinctes : 29 agents Markdown dans
`.claude/agents/` et ~35 modules Python dans `agents/` (`avocat.py`, `fiscaliste.py`, `innovateur.py`,
`superviseur.py`, `commandant.py`, `resolveur.py`…). Le `CLAUDE.md` ne décrit que la première. Un agent
qui se fie au `CLAUDE.md` pour savoir « ce qui existe déjà » conclut faux.
**Cause racine.** La documentation d'un système a été prise pour l'inventaire du système.
**Signal de détection.** Tu vas affirmer « il n'existe pas déjà de X » ou « le parc compte N agents ».
**Contre-mesure.** Inventorier par le **système de fichiers**, pas par la documentation. Puis signaler
l'écart entre les deux.
**Leçon transférable.** La carte n'est pas le territoire. Compte les fichiers.

## E-08 — Dépôt public sans fichier LICENSE
**Constaté le** 2026-09-11 · **NON CORRIGÉ**
**Ce qui s'est passé.** `chaima0007/keywordmoneymaker` est public et ne contient aucun `LICENSE`. Sans
licence, les tiers n'ont **aucun droit d'usage** explicite — et le projet s'expose à l'ambiguïté inverse
de celle qu'il cherche. Le droit d'auteur est acquis (Code de droit économique, livre XI) mais les
permissions ne sont pas dites.
**Signal de détection.** Tu publies ou tu rends public du code.
**Contre-mesure.** DÉPOSANT : `LICENSE` explicite + en-têtes de copyright. Ironie à retenir : le dépôt
contient un agent `auditeur-licences` qui vérifie les licences **des tiers**, et pas la sienne.
**Leçon transférable.** Les contrôles qu'on applique aux autres, on se les applique aussi.

## E-09 — Un dépôt public a servi de sauvegarde à du contenu destiné à être protégé
**Constaté le** 2026-09-11
**Ce qui s'est passé.** La règle générale de Chaima dit « Drive + dépôt GitHub (**privé si sensible**) +
copie locale ». Or le seul dépôt disponible est **public**. Le « 🔒 Coffre confidentiel » ne peut donc
pas y être sauvegardé, et la règle était inapplicable sans qu'on l'ait remarqué.
**Cause racine.** Une règle de sauvegarde a été écrite sans vérifier que l'emplacement prévu satisfaisait
sa condition.
**Signal de détection.** Tu sauvegardes une trouvaille, ou tu appliques une règle « privé si sensible ».
**Contre-mesure.** PROTECTEUR / REMPART : vérifier la **visibilité réelle** du dépôt avant tout dépôt
sensible. En attendant un dépôt privé : Drive + copie locale uniquement. Rappel art. 54 CBE — en Europe
il n'y a pas de délai de grâce, un `git push` public est une divulgation irréversible.
**Leçon transférable.** Vérifie que l'emplacement satisfait la condition, pas seulement que la règle est écrite.

## E-10 — Une entité HTML a été prise au littéral dans un titre
**Constaté le** 2026-09-11 · corrigé immédiatement
**Ce qui s'est passé.** Un dossier Drive a été créé sous le nom « Veille &amp;amp; Opportunités » : la
séquence d'échappement a été transmise telle quelle à l'API au lieu du caractère `&`.
**Signal de détection.** Tu passes à une API un titre contenant `&`, `<`, `>`, une apostrophe ou un guillemet.
**Contre-mesure.** Passer le **caractère réel**, jamais son entité. Puis relire le nom créé dans la
réponse de l'API — la réponse contient le titre tel qu'il a été enregistré.
**Leçon transférable.** Relis ce que le système a enregistré, pas ce que tu croyais envoyer.

## E-11 — Un clone superficiel a failli produire une date de divulgation fausse
**Constaté le** 2026-09-11
**Ce qui s'est passé.** Sur un clone `--depth 1`, `git log --reverse` a renvoyé le **2026-09-11 14:33** —
la date du clone, pas celle du premier commit. Utilisée telle quelle, cette date aurait servi à établir
la date de première divulgation publique dans une analyse de brevetabilité : une erreur à conséquence
juridique directe.
**Cause racine.** Un artefact d'outil pris pour une donnée du dépôt.
**Signal de détection.** Tu dates quoi que ce soit à partir de git, sur un clone dont tu n'as pas vérifié
la profondeur.
**Contre-mesure.** HORLOGER : vérifier la profondeur (`git rev-parse --is-shallow-repository`) avant toute
datation. Sans historique complet, écrire « **NON VÉRIFIÉ** » — ce qui a été fait ici.
**Leçon transférable.** Une date qui sert de preuve se vérifie sur la source, pas sur la copie de travail.

## E-12 — La conversion Markdown → Google Docs altère silencieusement
**Constaté le** 2026-09-11
**Ce qui s'est passé.** Au dépôt d'un document au Drive : l'emoji `🔒` est devenu « ð », et le gras à
l'intérieur d'un tableau est ressorti en astérisques échappés. Le fond était intact, la forme non.
**Signal de détection.** Tu déposes au Drive un document contenant des emojis ou des tableaux formatés.
**Contre-mesure.** Read-back, et considérer le Drive comme une **surface de lecture** : la copie fidèle
de référence reste le fichier versionné. Éviter les emojis porteurs de sens dans un contenu converti.
**Leçon transférable.** Une conversion réussie n'est pas une conversion fidèle.

## E-13 — Une recherche web a failli être prise pour une recherche au registre
**Constaté le** 2026-09-11 · **NON RÉSOLU — marque « Caelum Partners » NON VÉRIFIÉE**
**Ce qui s'est passé.** Une recherche web généraliste sur la marque n'a rien renvoyé de pertinent. Lue
comme « aucune antériorité », elle aurait produit un faux feu vert sur un **risque commercial actif** :
le nom est déjà exploité publiquement sur un domaine et un site en ligne. Les registres faisant foi
(EUIPO eSearch, BOIP) sont des applications JavaScript non interrogeables depuis cet environnement.
**Cause racine.** Confusion entre « je n'ai pas trouvé » et « il n'y a pas ».
**Signal de détection.** Tu conclus sur l'existence ou le statut d'un brevet, d'une marque, d'un titre.
**Contre-mesure.** Seul le **registre** fait foi. Absence de résultat hors registre = « NON VÉRIFIÉ »,
jamais « aucune antériorité ». Ne jamais confondre brevet en instance et brevet délivré. Vaut aussi pour
le rôle SCANNER : jamais un numéro ni un statut sans registre consulté + date.
**Leçon transférable.** « Je n'ai pas trouvé » n'est pas un résultat négatif, c'est une absence de résultat.

## E-14 — Deux racines créées pour un même projet
**Constaté le** 2026-09-11 · corrigé le même jour sur décision de Chaima
**Ce qui s'est passé.** Un dossier `Caelum Partners` a été créé au Drive alors qu'il existait déjà
« 🗂️ Caelum — Journal d'Audit (Travaux techniques) », structuré et actif. Deux racines pour un projet.
**Cause racine.** Le protocole « DRIVE D'ABORD » du `CLAUDE.md` §0 n'a pas été appliqué assez loin :
l'existant a été cherché par **titre** plutôt que par **fonction**.
**Signal de détection.** Tu crées un dossier ou un conteneur.
**Contre-mesure.** Chercher l'existant par ce qu'il **fait**, pas par son nom. Un dossier qui ne porte
pas le nom attendu peut déjà remplir la fonction.
**Leçon transférable.** L'absence d'un nom ne prouve pas l'absence de la chose.

## E-15 — Contenu d'un projet déposé dans le dépôt d'un autre
**Constaté le** 2026-09-11 · corrigé dans la minute
**Ce qui s'est passé.** L'analyse de brevetabilité de Caelum a été copiée dans le dépôt `chaima0007/test`
(CompeteIQ), en violation de la règle « par projet, jamais mélangé » — énoncée par la même charte qui
venait d'être écrite.
**Cause racine.** Le réflexe « sauvegarder où je peux pousser » a primé sur la règle de rangement. Le
dépôt accessible n'est pas le dépôt correct.
**Signal de détection.** Tu écris un fichier dans un dépôt qui n'est pas celui du projet concerné.
**Contre-mesure.** BOUSSOLE : le contenu d'un projet va dans le dépôt de **ce** projet. Si on ne peut pas
y pousser, on le dit et on ne pousse pas ailleurs « en attendant ».
**Leçon transférable.** Écrire une règle ne suffit pas à s'y soumettre. Vérifie-toi contre ta propre charte.

## E-16 — Un service en échec pris pour un service inexistant
**Constaté le** 2026-09-11
**Ce qui s'est passé.** Deux cas le même jour. Le connecteur Drive s'est déconnecté en cours de travail
puis est revenu — une conclusion hâtive aurait été « le Drive n'est pas configuré ». Le serveur
`composio` renvoie une erreur 404 de connexion — ce qui signifie « échec de connexion », **pas**
« capacité absente ».
**Signal de détection.** Un outil ne répond pas, ou une capacité semble manquer.
**Contre-mesure.** Distinguer trois états et les nommer : **en échec** (réessayer, signaler) /
**non autorisé** (l'utilisateur doit agir) / **inexistant**. Ne jamais annoncer le troisième quand on
observe le premier.
**Leçon transférable.** « Ça ne répond pas » et « ça n'existe pas » appellent des réponses opposées.

---

## E-17 — Des documents internes ont été publiés avec le site
**Constaté le** 2026-09-11 (dans le code du workflow) · **Survenu** avant le durcissement de `deploy.yml`
· **État** corrigé, mécanisme en place

**Ce qui s'est passé.** Le workflow GitHub Pages publiait `path: '.'` — c'est-à-dire **le dépôt entier**.
Les documents internes devenaient donc lisibles sur `caelumpartners.agency` : `CLAUDE.md`, `ETAT.md`,
`reports/`, `.claude/`, `scripts/`, `agents/`, et un CV. Le commentaire de `.github/workflows/deploy.yml`
le documente explicitement. C'est l'incident d'exposition de fichiers internes déjà signalé par Chaima.

**Cause racine.** Le déploiement fonctionnait par **liste noire implicite** : tout était publié sauf ce
qu'on pensait à exclure. Or personne ne pense à tout, et chaque fichier ajouté au dépôt devenait public
par défaut, sans décision. Cause aggravante et toujours présente : le dépôt mêle contenu public de site
et documents internes de travail — l'adjacence rend l'accident possible.

**Signal de détection.** Tu configures ou modifies une publication, un déploiement, un `path`, une règle
de copie vers un répertoire servi. Ou tu ajoutes un fichier à un dépôt dont une partie est publiée.

**Contre-mesure — en place, à ne jamais affaiblir.** `deploy.yml` publie désormais une **liste blanche
explicite** : tout fichier non listé n'est pas mis en ligne. Deux garde-fous bloquants complètent le
dispositif, et doivent rester bloquants : un `find` qui échoue le déploiement si un `CLAUDE.md`, `ETAT.md`,
`*.py`, `uv.lock`, `pyproject.toml`, `.env*` ou `README.md` a traversé ; et un contrôle d'existence du
`CNAME`, sans lequel le domaine casserait. Le workflow liste aussi le contenu réellement publié — à lire,
pas à survoler.

**Leçon transférable.** Une publication se définit par ce qu'on autorise, jamais par ce qu'on interdit.
Une liste noire est fausse dès le fichier suivant.

## E-18 — Deux sources de vérité ont coexisté dans le dispositif censé l'empêcher
**Constaté le** 2026-09-11 (par test piégé) · **État** corrigé le jour même

**Ce qui s'est passé.** Le rattachement des modules à un produit était déclaré dans
`shared/attribution.py`, écrit précisément pour n'avoir qu'une seule table au lieu de deux.
Après la migration en `products/<produit>/agents/`, le contrôle CI a commencé à attribuer les modules
**par leur chemin** — c'était plus juste. Mais `main.py` continuait d'interroger la **table** pour
router la mémoire. Deux sources répondaient donc à la même question, et rien ne les comparait : un
module déplacé sur le disque aurait gardé son ancien propriétaire pour la mémoire, sans le moindre signal.

**Cause racine.** Une source d'information plus fiable (le disque) a été introduite **à côté** de
l'ancienne, sans que l'ancienne soit ni supprimée ni subordonnée. C'est la même faute que la fiche
E-01 — et elle a été commise dans le module écrit pour l'empêcher. La bonne intention ne protège pas :
seule la subordination explicite d'une source à l'autre protège.

**Comment elle a été trouvée.** Par **test piégé**, pas par relecture. Un piège a échoué à déclencher
(« module nouveau non déclaré » ne bloquait pas), et c'est ce silence inattendu qui a mis la divergence
au jour. Une relecture du code n'aurait rien vu : les deux moitiés étaient correctes séparément.

**Signal de détection.** Tu ajoutes une source d'information — table, fichier, index, cache, chemin —
là où une autre répond déjà à la même question. Ou un contrôle que tu attendais rouge reste vert.

**Contre-mesure.** Quand deux sources peuvent répondre à une même question : en désigner **une** comme
faisant foi, reléguer l'autre au rang de repli explicite, et **ajouter un contrôle qui compare les
deux** (ici le contrôle C4 de `scripts/audit_cloisonnement.py`). Sans ce troisième élément, la
hiérarchie se perd au premier refactor.

**Leçon transférable.** Une source de vérité nouvelle doit soit remplacer l'ancienne, soit la
subordonner explicitement — et quelque chose doit vérifier qu'elles s'accordent. Deux sources
d'accord aujourd'hui ne prouvent rien sur demain. Et un piège qui ne se déclenche pas est une
information, pas un succès.

## E-19 — Une manipulation git a détruit l'état d'une fusion en cours
**Constaté le** 2026-09-11 · **État** corrigé le jour même, avant tout push

**Ce qui s'est passé.** Au milieu d'un `git merge` non finalisé (conflit en cours de résolution), un
`git stash -u` puis un `git checkout` d'une autre référence ont été lancés — pour mesurer, légitimement, le
delta de publication entre les deux branches. Ces commandes ont **détruit `MERGE_HEAD`**. Les modifications
étaient toujours là, l'index paraissait normal : rien ne signalait le problème. Or committer aurait produit
un commit **ordinaire**, sans la branche fusionnée comme second parent — donc un historique faux et un
conflit garanti à la fusion suivante, sur les mêmes fichiers.

**Cause racine.** Une fusion en cours n'est pas un état de travail comme un autre : c'est un état
**transitoire** que git conserve dans des fichiers de contrôle (`MERGE_HEAD`, `MERGE_MSG`). Toute commande
qui réécrit l'index ou change de branche les efface, **sans avertissement et sans erreur**. La commande
réussit, l'information disparaît.

**Comment elle a été trouvée.** Par un contrôle explicite — `test -f .git/MERGE_HEAD` — ajouté par réflexe
avant de committer, pas par une alerte de git. Sans ce contrôle, l'erreur aurait été poussée.

**Signal de détection.** Tu es au milieu d'une fusion (conflits à résoudre, `MERGE_HEAD` présent) et tu
t'apprêtes à lancer autre chose que la résolution : `stash`, `checkout`, `reset`, `pull`, changement de
branche — ou n'importe quelle mesure sur un autre état du dépôt.

**Contre-mesure.** Une fusion se finalise **avant** toute autre opération. Ce qui doit être mesuré sur une
autre référence se mesure **avant** de lancer le merge, ou depuis un clone séparé, ou avec des commandes de
lecture seule qui ne touchent pas l'index (`git show ref:chemin`, `git ls-tree`). Et dans tous les cas :
vérifier `MERGE_HEAD` juste avant le commit de fusion.

**Leçon transférable.** Certains états d'outil sont transitoires et s'effacent en silence quand on fait
autre chose. Le succès d'une commande ne dit rien sur ce qu'elle a détruit au passage.

## E-20 — Un outil d'audit a inspecté la mauvaise cible pendant plusieurs runs
**Constaté le** 2026-09-06 · **État** CORRIGÉE (commit `bfe624f`) · *reprise du registre `🔴 ERREURS.md`*

**Ce qui s'est passé.** `pip-audit` était lancé sans `-r`, donc il auditait les paquets préinstallés de
l'environnement Ubuntu du runner — `cloud-init`, `ufw`, `twisted`… — et non les dépendances du projet.
Il remontait des CVE **réelles**, ce qui rendait le défaut d'autant plus difficile à voir : la sortie
avait l'air d'un audit qui travaille. Corrigé en ciblant `uv.lock` (635 dépendances réelles) ; le run
suivant affiche « Dépendances auditées : 635 » puis « No known vulnerabilities found ».

**Cause racine.** Un outil pointé sur la mauvaise cible ne se tait pas : il produit des résultats vrais
mais **hors sujet**. Rien dans sa sortie ne dit « je n'ai pas regardé ce que tu crois ».

**Signal de détection.** Tu lances un audit, un scan, un test de dépendances, un linter — et tu lis son
verdict sans avoir vérifié **ce qu'il a réellement inspecté**.

**Contre-mesure.** Exiger de tout outil de contrôle qu'il imprime sa **cible** et le **nombre d'éléments
inspectés**, et lire cette ligne avant le verdict. C'est pour cette raison que `audit_code_sur.py` affiche
« 3 dépendance(s) déclarée(s) » et `audit_cloisonnement.py` « Modules analysés : 35 » : un compte
inattendu est le seul indice qu'on regarde au mauvais endroit.

**Leçon transférable.** Un outil qui trouve quelque chose n'a pas forcément regardé le bon endroit. Vérifie
la cible avant le verdict.

## E-21 — L'état du site a été déduit du dépôt, pas de ce que voyait un visiteur
**Constaté le** 2026-08-10 · **État** CORRIGÉE · *reprise du registre `🔴 ERREURS.md`*

**Ce qui s'est passé.** La racine de `caelumpartners.agency` servait un placeholder `noindex`
« Redirection en cours » pendant des semaines, alors que la vraie page d'accueil conformité existait dans
le dépôt. Personne ne l'a vu parce que tout le monde vérifiait le **dépôt**, jamais le **live**. Corrigé :
`index.html` porte la vraie page, `caelum-index.html` devient une redirection `noindex`, ajout de `404.html`.

**Cause racine.** Le dépôt et le site servi sont deux états distincts, reliés par un déploiement qui peut
publier autre chose que ce qu'on croit — liste blanche, redirection, cache, configuration Pages. Lire le
dépôt et conclure sur le site est un saut logique, pas une vérification.

**Signal de détection.** Tu affirmes quelque chose sur ce qu'un visiteur voit — page en ligne, redirection,
indexation, certificat — en t'appuyant sur des fichiers.

**Contre-mesure.** Vérifier le **live**, ou écrire « NON VÉRIFIÉ » et nommer qui peut le faire. Deuxième
meilleure preuve quand le live est inaccessible : la liste des fichiers **réellement publiés** par le
déploiement, imprimée par le workflow. Elle prouve ce qui a été envoyé, pas ce qui est rendu — et il faut
le dire.

*Note du 2026-09-11 : la sortie réseau de l'environnement d'agent refuse `caelumpartners.agency` (403 au
gateway du proxy). Aucun agent ne peut donc vérifier le live d'ici. La vérification du rendu appartient
structurellement à Chaima, et tout rapport qui l'affirmerait sans elle serait faux.*

## E-22 — Un défaut a été annoncé à Chaima sans avoir jamais été constaté
**Constaté le** 2026-09-11 · **Survenu** 2026-09-11 · **État** corrigé le jour même

**Ce qui s'est passé.** Dans un état des lieux sur la typographie du site de Caelum, j'ai annoncé à
Chaima un défaut technique : « le CSS appelle Fraunces en 600/700 alors que seules les graisses 400 et
500 sont chargées ». Chaima a intégré ce défaut à ses priorités du jour et m'a demandé de le corriger.
Au moment d'écrire le correctif, la vérification règle par règle a montré qu'**il n'y avait aucun
défaut** : toutes les déclarations `font-weight:600` et `700` du fichier appartiennent à Inter, qui est
bien chargée en `400;500;600;700`. Fraunces n'est jamais appelée en 600 ni en 700.

**Cause racine.** Deux faits vrais ont été rapprochés sans être reliés : « le CSS contient des poids
600/700 » (vrai) et « Fraunces n'est chargée qu'en 400;500 » (vrai). La conclusion « donc Fraunces est
appelée en 600/700 » ne découlait ni de l'un ni de l'autre — il manquait la seule question qui
tranchait : *à quelle famille appartient chaque règle en 600/700 ?* Elle n'avait pas été posée.

**Le coût réel.** Il ne s'agit pas d'une erreur interne rattrapée avant sortie : l'affirmation avait
déjà atteint Chaima, qui a arbitré ses priorités dessus. Un défaut inventé consomme sa décision aussi
sûrement qu'un défaut réel — c'est la faute du §13 du CODEX sur les affirmations **à propos de nous**,
celles que personne ne pense à sourcer.

**Signal de détection.** Tu t'apprêtes à rapporter un défaut, un manque ou une régression que tu n'as
pas **reproduit**. Ou ton constat repose sur un décompte agrégé (`grep -c`, un total, une liste de
poids) et non sur l'examen de chaque occurrence.

**Contre-mesure.** Aucun défaut n'est annoncé sans la commande qui l'exhibe, jointe au constat. Pour
un décompte, descendre à l'occurrence : ce n'est pas « il y a N poids 600/700 », c'est « la règle
`fichier:ligne` applique 600 à la famille X ». Vocabulaire du §13 : sans exécution, c'est **PLAUSIBLE**,
jamais **VÉRIFIÉ**.

**Leçon transférable.** Un agrégat ne prouve rien sur ses éléments. Deux faits vrais côte à côte ne
font pas une conclusion vraie : il faut la question qui les relie, et elle doit être posée avant le
rapport, pas au moment du correctif. Et quand l'erreur est déjà partie chez Chaima, elle se corrige à
voix haute, dans le même canal, sans attendre qu'elle la découvre.


## E-23 — La condition d'arrêt visait les agents, pas l'horloge qui les réveille
**Constaté le** 2026-09-14 · **Survenu** 2026-09-12 → 2026-09-14 · **État** cause identifiée, correction en attente d'arbitrage

**Ce qui s'est passé.** La règle anti-bruit existe deux fois, et de façon explicite : CODEX §5
(« un rapport pour dire qu'il n'y a rien à dire est une faute contre le protocole ») et la condition
d'arrêt de la chaîne veille. Un rôle a même été créé le 2026-09-11 pour la faire appliquer —
`croque-mort`. Trois jours plus tard, le Drive contient une vingtaine de documents horodatés en 72 h,
dont au moins huit disent littéralement « INCHANGÉ · 0 nouvelle pièce · SILENCE ». Plusieurs répètent
depuis le 12/09 « code toujours bloqué (push authentifié requis) », c'est-à-dire qu'ils annoncent toutes
les deux heures l'attente d'une action humaine déjà signalée.

**Cause racine — et ce n'est pas la désobéissance d'un agent.** La règle s'adresse à celui qui *écrit
le rapport*. Or ce qui produit le bruit est en amont : **des Routines déclenchées par une horloge.**
Relevé au 2026-09-14 : deux Routines horaires, deux Routines toutes les deux heures — dont deux
programmées **à la même minute** (`22 */2 * * *`) sur le même dépôt — et six quotidiennes, soit de
l'ordre de soixante réveils par jour. Un agent réveillé n'a pas le pouvoir de décider qu'il n'aurait pas
dû l'être : au mieux il écrit « rien à signaler », et ce message *est* le bruit.

**Une condition d'arrêt posée sur l'agent et pas sur l'ordonnanceur ne s'applique jamais.**

**Signal de détection.** Tu poses une condition d'arrêt, une règle anti-doublon ou une règle anti-bruit.
Demande-toi : **qui décide que ce travail a lieu ?** Si c'est un `cron`, une Routine ou un planificateur,
la règle doit porter sur la fréquence, pas sur le contenu du rapport. Autre signal : une Routine dont les
derniers passages se ressemblent, ou qui attend depuis plus d'un cycle une action humaine.

**Contre-mesure.** Trois niveaux, du plus haut au plus bas :
1. **L'ordonnanceur d'abord.** Une boucle bloquée sur une décision humaine se met en pause ou passe en
   cadence longue — elle ne se rappelle pas toutes les deux heures. Une boucle dont le travail de fond
   est inaccessible (accès réseau fermé, par exemple) s'arrête : elle ne peut produire que du bruit.
2. **Jamais deux Routines à la même minute sur le même dépôt.** Deux sessions concurrentes sur le même
   `git` se gênent ; au minimum les décaler.
3. **L'agent ensuite**, comme aujourd'hui : état inchangé → une ligne dans l'état courant, pas un
   document neuf.

**Leçon transférable.** Une règle ne vaut que si elle s'adresse à celui qui a le pouvoir de l'appliquer.
Écrite pour un agent, une condition d'arrêt ne peut pas arrêter l'horloge qui le réveille — il faut la
poser là où la décision se prend.

## E-24 — Un test piégé a détruit le travail qu'il devait valider
**Constaté le** 2026-09-14 · **État** corrigé le jour même, travail refait

**Ce qui s'est passé.** Pour éprouver un nouveau garde-fou de déploiement, un test enchaînait plusieurs
pièges. Entre deux pièges, il remettait l'environnement à zéro avec `git checkout -q -- .` — commande qui
**écrase tout le travail non commité de l'arbre**. Une heure de modifications (quatre `@font-face`, six
pages nettoyées, le garde-fou lui-même) a disparu. Seuls les fichiers non suivis par git ont survécu, par
chance et non par conception.

Symptôme trompeur : le témoin du test, censé passer, a échoué. J'ai d'abord cru à un défaut du garde-fou.
Il était correct — c'est le monde autour de lui qui venait d'être réinitialisé.

**Cause racine.** Le test agissait sur **l'arbre de travail** alors qu'il n'avait besoin d'agir que sur
`_site`, un artefact de build reconstructible. Un test qui partage son état avec le travail qu'il valide
peut le détruire, et la commande de nettoyage la plus naturelle (`git checkout -- .`, `git reset --hard`,
`git clean -fd`) est précisément celle qui fait le plus de dégâts.

**Signal de détection.** Tu écris un test, un script de vérification ou une boucle de pièges qui contient
`git checkout`, `git reset`, `git clean`, `git stash` — ou qui écrit ailleurs que dans un répertoire
jetable.

**Contre-mesure — deux règles, dans cet ordre.**
1. **Commiter AVANT de tester.** Le travail devient inatteignable par un test mal isolé. C'est gratuit et
   ça aurait suffi ici.
2. **Un test n'agit que sur des artefacts jetables.** Ici : reconstruire `_site` entre chaque piège, ne
   jamais toucher aux fichiers sources. Aucune commande git de remise à zéro dans un test.

**Leçon transférable.** Un test doit pouvoir échouer sans rien casser. S'il partage son état avec le
travail qu'il valide, il n'est pas un test : c'est un risque de plus. Et deuxième leçon, née du
symptôme : quand un témoin échoue, soupçonner d'abord le banc d'essai, pas la pièce testée.

## E-25 — Un contrôle aveugle a accusé le rapport au lieu de s'accuser lui-même
**Constaté le** 2026-09-14 · **État** corrigé le jour même

**Ce qui s'est passé.** Le contrôle des rapports (`scripts/verifier_rapports.py`, règle R3) vérifie
que tout commit cité existe, via `git cat-file -e`. Il passait en local. À sa **première exécution
réelle en intégration continue**, il a échoué en annonçant : « le commit `45b2e4d` n'existe pas dans
ce dépôt ». Ce commit existe : c'est la tête de `main`, et le site en production en est issu.

Le workflow récupère le code avec `git fetch --depth 1`. Dans un dépôt **superficiel**, `cat-file`
répond non pour un commit parfaitement réel mais simplement non récupéré. Le contrôle n'a pas menti :
il a confondu **« je ne vois pas »** avec **« ça n'existe pas »**.

Circonstance aggravante : le même contrôle passait en local *par chance*. Le clone local était lui
aussi superficiel ; le commit cité se trouvait dans la profondeur récupérée. Un vert obtenu par
hasard est indistinguable d'un vert mérité — c'est ce qui rendait le défaut invisible.

**Cause racine.** Un outil de vérification a été écrit sans se demander ce qu'il fait quand **il ne
peut pas voir**. Deux états ont été fondus en un seul : « absent » et « hors de portée ». C'est la
fiche E-11 sous une autre forme : un historique tronqué pris pour l'historique réel.

**Signal de détection.** Tu écris un contrôle qui interroge l'historique git (`cat-file`, `log`,
`rev-list`, dates de commit) et qui s'exécutera dans une intégration continue — donc, par défaut,
dans un clone superficiel. Ou, plus généralement : ton contrôle possède une branche de code où il
répond « faux » alors que la réponse honnête serait « je ne sais pas ».

**Contre-mesure — deux règles, dans cet ordre.**
1. **Donner à voir.** L'historique complet est récupéré dans le workflow (`--depth 1` retiré) : 70
   commits, 3,5 Mo. Le coût était nul ; l'aveuglement ne l'était pas.
2. **Un contrôle qui ne peut pas voir échoue LUI-MÊME, il n'accuse personne.** Le script détecte
   désormais un dépôt superficiel et s'arrête en le disant, au lieu de rendre un verdict sur le
   rapport. « Je ne peux pas vérifier » n'est pas « c'est faux », et n'est surtout pas « c'est bon ».

**Leçon transférable.** Avant de faire confiance à un contrôle, demander : que répond-il quand il est
aveugle ? S'il répond « faux », il fabriquera des faux positifs (fiche E-02). S'il répond « vrai »,
il fabriquera de faux verts, ce qui est pire. La seule réponse acceptable est qu'il se déclare
incapable — bruyamment. Et un contrôle n'a pas prouvé sa valeur tant qu'il n'a pas tourné là où il
doit vivre : celui-ci a été pris en défaut par sa première exécution réelle, pas par ses sept pièges.

## E-26 — La dérive de périmètre : quatre fois détectée, jamais empêchée
**Constaté le** 2026-09-14 · **Survenu** depuis le 2026-07-17 au moins · **État** contre-mesure posée

**Ce qui s'est passé.** La consigne d'origine de Chaima est la **chaîne Veille, Brevets, Technologies
& Capitaux**. Le 14/09, une session entière a produit de l'infrastructure, un registre d'erreurs, des
garde-fous et un site web. **Zéro technologie trouvée, zéro brevet analysé, zéro piste de financement.**
C'est Chaima qui l'a relevé, pas le dispositif.

Et ce n'est pas un accident isolé. La méta-surveillance du soir a détecté exactement la même faute
**quatre fois**, et elle avait raison quatre fois :

| Date | Extrait de la méta-alerte (Drive) |
|---|---|
| 2026-07-17 | « DISPERSION FLOTTE (8 projets) vs décision *sites d'abord* » |
| 2026-07-25 | « DISPERSION : nouvelle piste *armoire à pharmacie* apparue à J-7, alors que les sites ne sont TOUJOURS pas en ligne » |
| 2026-09-11 | « DÉRIVE DE PRIORITÉ : flotte de vente construite APRÈS la consigne n°1 *le visuel d'abord, ne pas enchaîner* » |
| 2026-09-14 | la présente fiche |

**Cause racine — et elle n'est pas le manque d'attention.**
1. **Le dispositif détecte, il n'empêche pas.** La méta-surveillance passe à 22h30 : elle constate le
   soir une journée déjà perdue et n'a aucun pouvoir d'arrêter quoi que ce soit. Quatre constats
   justes, zéro correction structurelle. C'est la fiche E-01 : une règle écrite sans mécanisme cède.
2. **La dérive est faite de pas légitimes.** Aucun détour du 14/09 n'était absurde ; chacun a été
   demandé ou validé sur le moment. C'est le cumul qui est la faute, et le cumul ne se voit pas pas à pas.
3. **Rien n'obligeait à écrire au service de quoi on travaillait.** Tant que personne n'énonce la
   consigne servie, un travail hors mission est indistinguable d'un travail en mission.
4. **Un piège de langage :** « continue », « ok », « vas-y » **en réponse à un détour que l'agent a
   lui-même proposé** ont été pris pour un accord sur la priorité. Ce n'en est pas un.

**Signal de détection.** Tu es sur le point de commencer un travail et tu ne peux pas énoncer, en une
phrase, la consigne n°1 qu'il sert. Ou : tu enchaînes un troisième sujet sans que Chaima ait rien
redemandé. Ou : tu réponds à ta propre proposition de détour.

**Contre-mesure — trois pièces, dans l'ordre.**
1. **`codex/CONSIGNE-N1.md`** : la priorité en vigueur, datée, append-only. **Lue en premier par toute
   session**, redite avant d'agir. Seule Chaima l'y écrit.
2. **Règle R8 de `scripts/verifier_rapports.py`**, bloquante en intégration continue : tout rapport
   déposé doit **nommer la consigne qu'il sert**. Posée le 14/09, elle a immédiatement rejeté les deux
   rapports du jour — les deux étaient hors mission. Ils ont été annotés « détour assumé », pas maquillés.
3. **Un détour se nomme.** Travailler hors consigne n'est pas interdit ; le faire en silence l'est.
   Une phrase, puis l'accord explicite de Chaima.

**Leçon transférable.** Une surveillance qui arrive après coup n'est pas une surveillance, c'est une
archive. Pour empêcher une dérive, le contrôle doit se placer **à l'entrée** du travail, pas à sa
sortie. Et la dérive ne se combat pas par la vigilance : elle se combat en rendant **obligatoire
l'énoncé de ce qu'on sert** — parce qu'une phrase qu'on ne peut pas écrire est un travail qu'on ne
devrait pas commencer.

## E-27 — Un heredoc non cité a EXÉCUTÉ le texte qu'il devait écrire
**Constaté le** 2026-09-14 · **État** corrigé le jour même

**Ce qui s'est passé.** Écriture de deux définitions d'agents avec `cat > fichier <<AGENTEOF`.
Le délimiteur n'était **pas** entre apostrophes. Le shell a donc interprété le contenu avant de
l'écrire : chaque nom d'agent entre accents graves — `` `protecteur` ``, `` `deposant` ``,
`` `horloger` `` — a été traité comme une **commande à exécuter**. Résultat : sept
`command not found`, et un fichier livré avec un bloc « à qui tu passes la main » **vide** :

```
-  — dès qu'une divulgation est envisagée. Son veto prime sur ton analyse.
-  — si la trouvaille mérite un droit : c'est lui qui tient les droits, pas toi.
```

Un agent qui ne sait plus à qui passer la main. Le second fichier, dont les accents graves étaient
échappés, est sorti intact — ce qui rendait la panne **partielle**, donc facile à ne pas voir.

**Cause racine.** En shell, `<<FIN` interpole ; `<<'FIN'` n'interpole pas. Or le Markdown de ce
dépôt est **plein** d'accents graves : c'est ainsi qu'on y nomme les agents, les fichiers et les
commandes. Le format d'écriture le plus courant du dépôt est donc précisément celui qui déclenche
le piège.

**Signal de détection.** Des `command not found` portant des noms qui sont **du contenu** et non des
commandes. Ou un fichier écrit dont il manque justement les portions qui contenaient du code.

**Contre-mesure.** **Tout heredoc qui écrit du Markdown est cité** : `<<'FIN'`, sans exception.
La règle vaut même quand le contenu « n'a pas l'air » de contenir du code — un seul accent grave
suffit. Et la sortie d'écriture se relit : sept messages d'erreur défilaient à l'écran pendant que
le fichier se créait « avec succès ».

**Comment ça a été réglé.** Les sept renvois ont été réinsérés un par un, puis un contrôle a cherché
les motifs de dégât (`^-\s+—`, `au .**`) pour vérifier qu'il n'en restait aucun. Le fichier a été
relu avant commit, et la faute est écrite dans le message de commit plutôt que passée sous silence.

**Leçon transférable.** Une commande qui réussit n'a pas forcément fait ce qu'on croit. `cat` a
« réussi » : il a écrit un fichier. C'est son **contenu** qui était amputé. Vérifier le code de
sortie ne suffit jamais à vérifier le résultat.

## E-28 — Un contrôle qui se déclenche sur sa propre documentation
**Constaté le** 2026-09-14 · **État** corrigé le jour même

**Ce qui s'est passé.** Contrôle rapide des motifs RGPD interdits dans un script de recherche :
`grep localStorage`, `grep innerHTML`, `grep pushState`. Tous ont répondu **PRÉSENT**, alors que le
script ne les utilisait pas. Ils figuraient dans ses **commentaires**, qui expliquent précisément
pourquoi ces motifs sont interdits.

Le même piège a frappé une seconde fois dans la même journée, ailleurs : un contrôle de chemins
inexistants absolvait un fichier nommé `inexistant.html`, parce qu'il cherchait le mot « inexistant »
dans la ligne entière — nom de fichier compris.

**Cause racine.** Le contrôle analysait le fichier **brut**, sans distinguer le code de ce qui
l'entoure. Or un dépôt qui documente sérieusement ses interdits les **écrit en toutes lettres** dans
ses commentaires. Plus la documentation est bonne, plus le contrôle naïf produit de faux positifs.

**Signal de détection.** Un contrôle qui échoue sur un fichier dont tu sais qu'il est correct. Ou,
plus insidieux : un contrôle qui n'a **jamais** été vert depuis sa création.

**Contre-mesure.** Les commentaires (`/* */`, `//`, `<!-- -->`) sont retirés avant toute analyse de
motif, et les portions citées (entre accents graves) sont exclues des recherches de mots-clés.
Un contrôle doit lire ce que la machine exécute, pas ce que l'humain explique.

**Comment ça a été réglé.** `_sans_commentaires()` a été ajouté à `verifier_site.py` et appliqué
avant chaque test de motif ; la recherche d'aveu d'absence se fait hors des accents graves. Les deux
correctifs sont commentés dans le code avec le piège qui les a motivés, pour qu'on ne les
« simplifie » pas plus tard.

**Leçon transférable.** **Un contrôle qui crie au loup sur sa propre documentation apprend aux gens
à l'ignorer.** Un faux positif répété ne coûte pas seulement du temps : il détruit la crédibilité du
contrôle, et c'est ainsi qu'un vrai signal finit par passer inaperçu (fiche E-02).

## E-29 — Un lien mort écrit dans l'heure qui suivait l'écriture de la règle l'interdisant
**Constaté le** 2026-09-14 · **État** corrigé le jour même

**Ce qui s'est passé.** Le brief de construction du site La Loi Avec Moi consacre une section
entière aux 26 liens morts de l'ancien site et pose la règle : *aucune carte ne pointe vers le
vide*. **Moins d'une heure plus tard**, le gabarit de navigation que j'ai écrit pointait vers
`#recherche` — une ancre qui n'existe que sur la page d'accueil. Sur les quatre autres pages :
lien mort.

Ce n'est pas l'ignorance de la règle. Je venais de l'écrire.

**Cause racine.** Une ancre relative est valide **là où sa cible existe** et morte partout ailleurs ;
rien dans l'écriture ne le signale. Mais la cause profonde est ailleurs : **connaître une règle
n'empêche pas de l'enfreindre.** L'attention ne tient pas à l'échelle d'une journée de travail.

**Signal de détection.** Tu écris un lien relatif, une ancre ou un chemin dans un gabarit **partagé
entre plusieurs pages**. Ce qui est vrai depuis une page ne l'est pas depuis toutes.

**Contre-mesure.** Un contrôle automatique des liens internes, **bloquant**, qui résout chaque
référence depuis la page qui la contient — et qui vérifie l'existence de l'ancre, pas seulement du
fichier.

**Comment ça a été réglé.** `scripts/verifier_site.py` a été écrit **avant** la mise en ligne et a
détecté les quatre liens morts en trente secondes. Les gabarits pointent désormais vers
`index.html#recherche`, valide depuis n'importe quelle profondeur. Contrôle vert sur les sept pages.

**Leçon transférable.** C'est la démonstration la plus nette de la journée : **celui qui écrit la
règle l'enfreint aussi.** La discipline n'est pas un mécanisme. Un dispositif ne vaut que par ce qui
tourne sans qu'on y pense — et le meilleur moment pour l'écrire est juste avant d'avoir besoin de lui.

## E-30 — « Aucun accès aux brevets » était faux : je n'avais pas testé le contournement

**Constaté le** 2026-09-19 · **Survenu** du 2026-09-14 au 2026-09-19 (cinq jours) · **État** corrigé

**Ce qui s'est passé.** Le 14/09 j'ai mesuré que onze registres de brevets sont refusés par la
politique réseau. La mesure était juste, preuve par journal de proxy, re-confirmée le 19/09
(`connect_rejected` sur Espacenet et Google Patents). J'en ai tiré une conclusion beaucoup plus
large : « je ne peux lire aucun brevet ». Je l'ai répétée à Chaima pendant cinq jours, je l'ai
écrite en §0 de `codex/methodes/PIPELINE-BREVETS.md` comme « le blocage qui commande tout », et
j'ai décrit tout le pipeline comme tournant à vide.

Une heure après avoir écrit ce §0, j'ai testé `web_fetch_exa` sur une page Google Patents.
Le texte intégral est revenu : description, revendications, et surtout la section arrière-plan
avec la critique de l'art antérieur — exactement la matière première que je déclarais hors de
portée. Testé sur deux brevets (US9280603B2, EP2887236A1), les deux fois.

Le contournement fonctionne parce que la récupération a lieu sur les serveurs d'Exa, pas ici.
C'est le mécanisme que j'avais moi-même écrit le 14/09 pour expliquer pourquoi les API de
recherche répondent — et je ne l'ai pas appliqué à la lecture des brevets.

**Cause racine.** J'ai confondu **« cette route est fermée »** avec **« il n'y a pas de route »**.
Une mesure exacte sur un chemin unique a été généralisée en impossibilité. Aucun contrôle ne
surveille l'écart entre ce qui a été mesuré et ce qui en est conclu : la mesure est tracée et
datée, la généralisation ne l'est pas. Aggravant : un blocage est confortable. Il explique
l'absence de résultat sans qu'on ait à produire de résultat, donc il n'est pas réinterrogé.

**Signal de détection.** Tu t'apprêtes à écrire qu'une chose est impossible, et cette phrase
dispense la chaîne de travailler. Compte alors les voies testées. Une seule voie testée ne
démontre jamais une impossibilité — elle démontre qu'une voie est fermée.

**Contre-mesure.** Toute déclaration d'impossibilité doit porter la liste des voies éprouvées,
avec la date de chaque essai, et être réinterrogée à chaque fois qu'elle est citée. Rôle qui en
répond : `contradicteur`, dont c'est exactement le travail — un blocage est une affirmation, et
une affirmation se contredit. `verificateur-verite` rejette toute impossibilité à une seule voie.

**Ce qui reste vrai après correction.** Le blocage n'est pas nul, il est plus étroit :
Google Patents passe par Exa ; le Registre EPO et Espacenet ne passent pas (`CRAWL_UNKNOWN_ERROR`
et `CRAWL_LIVECRAWL_TIMEOUT`, testés le 19/09). Conséquence précise : **lire** un brevet est
possible, **vérifier son statut juridique** ne l'est pas. Google Patents l'écrit lui-même sur
chaque fiche : le statut affiché est une supposition, pas une conclusion juridique. Donc les
étapes 2 et 3 du pipeline sont débloquées, l'étape 1 reste suspendue au registre.

**Leçon transférable.** Une impossibilité annoncée est la plus rentable des erreurs : elle
justifie l'inaction. C'est pour ça qu'elle doit être la mieux contredite. **Mesurer une porte
fermée n'est pas mesurer le bâtiment.**

## E-31 — J'ai proposé trois domaines « éloignés » qui sont le même domaine

**Constaté le** 2026-09-19 · **Survenu** le 2026-09-19, quelques heures plus tôt · **État** corrigé

**Ce qui s'est passé.** Le matin du 19/09, après avoir établi que le domaine juridique était
ratissé, j'ai proposé à Chaima trois domaines de repli : capteurs et traitement du signal,
énergie et bâtiment, procédés et agroalimentaire. Elle a demandé de mener les trois de front pour
pouvoir les fusionner. J'ai fondé toute la méthode du transfert de domaine sur l'art. 56 CBE :
un enseignement venu d'un domaine **éloigné** est moins susceptible d'être jugé évident.

L'après-midi, deux croisements ouverts, deux croisements morts. X-01 transférait de
l'instrumentation de mesure vers l'instrumentation de procédé. X-02 transférait du chauffage
d'aliment en contenant fermé vers le chauffage d'aliment en contenant fermé. Dans les deux cas
l'antériorité était immédiate, et dans les deux cas pour la même raison : **les domaines n'étaient
pas éloignés.**

Les trois carnets portent tous sur la mesure et la conduite de processus thermiques et physiques.
Un seul super-domaine, une seule communauté d'ingénieurs, une seule littérature — donc un seul
homme du métier, et l'avantage que je prêtais au transfert n'a jamais existé.

**Cause racine.** J'ai choisi les trois domaines sur un critère juste mais unique : **l'effet
technique évident**, pour échapper à l'art. 52 CBE qui avait tué le domaine juridique. Optimiser
sur une seule contrainte a produit trois domaines qui se ressemblent, précisément parce qu'ils
partagent la propriété sur laquelle j'optimisais. Échapper à l'art. 52 m'a fait tomber sur
l'art. 56. Les deux articles tirent en sens contraire et je n'ai regardé qu'un seul des deux.

**Signal de détection.** Tu proposes plusieurs options en les qualifiant de différentes, et tu les
as choisies sur un même critère. Ce critère les rend semblables **par construction**. Demande-toi
ce qui les distingue, pas ce qui les qualifie.

**Contre-mesure.** Un ensemble de domaines n'est déclaré « éloigné » que si on peut nommer, pour
chaque paire, **ce qui empêche un ingénieur de l'un de lire la littérature de l'autre** : pas les
mêmes revues, pas les mêmes codes CPC, pas les mêmes salons, pas les mêmes formations. Tant que
cette phrase n'est pas écrite pour chaque paire, « éloigné » est une affirmation non vérifiée.
Rôle qui en répond : `contradicteur`, à convoquer sur la **proposition de domaines**, et pas
seulement sur les croisements qui en sortent.

**Leçon transférable.** Optimiser sur une seule contrainte produit un ensemble homogène, et
l'homogénéité est exactement ce qu'on voulait éviter. **Quand deux règles tirent en sens
contraire, choisir en ne regardant qu'une seule des deux donne l'illusion d'un bon choix.**

## E-33 — Le contrôle de licence a été pris en défaut à son premier usage réel

**Constaté le** 2026-09-20 · **Survenu** le 2026-09-20, dans l'heure suivant son écriture
· **État** corrigé, et le contrôle en sort plus capable qu'avant

**Ce qui s'est passé.** `scripts/sas_licence.py` a été écrit pour lire les FICHIERS de licence
plutôt que l'étiquette affichée par le dépôt — leçon du piège CodeGeeX4. Première exécution
réelle sur dix briques : **quatre refus dont trois étaient faux**.

Trois défauts distincts :
1. Il prenait les *sidecars* REUSE `*.license` et les scripts d'outillage
   (`resolve_licenses.py`, `update_license_headers.py`) pour des textes de licence, et déclarait
   NVIDIA/OpenShell multi-licencié — alors qu'il ne l'est pas.
2. Son motif SPDX avalait la fin du commentaire qui portait l'identifiant : `Apache-2.0 -->` en
   HTML devenait l'identifiant « Apache-2.0 -- », discordant avec « Apache-2.0 ». Le dépôt était
   déclaré en contradiction **avec lui-même**.
3. Il traitait `NOTICE` comme un texte de licence. Sous Apache-2.0, `NOTICE` est un fichier
   d'**attribution**. Trois briques refusées pour ça.

**Cause racine.** J'ai confondu « fichier qui EST une licence » et « fichier qui PARLE de
licences ». Les deux se ressemblent par le nom et ne se ressemblent en rien par la fonction. La
cause profonde est plus générale : **un contrôle écrit sans données réelles est une hypothèse sur
les données.** Celui-ci n'avait jamais vu un vrai dépôt quand il a été écrit.

**Signal de détection.** Tu écris un contrôle par filtrage de noms de fichiers, sans l'avoir fait
tourner sur au moins cinq cas réels. Le taux de faux positifs est alors inconnu, pas nul.

**Contre-mesure — et c'est le point.** La règle du projet interdit de desserrer un contrôle pris
en défaut : on le **durcit**. Desserrer aurait été d'ignorer les sidecars et les NOTICE. On a fait
l'inverse :
- les sidecars REUSE sont désormais **lus** et leurs identifiants SPDX comparés au texte principal
  — une déclaration discordante est précisément ce qu'on cherche ;
- `NOTICE` devient une catégorie propre, analysée pour les **noms de licences qu'elle cite**, et
  une attribution nommant une licence autre que celle du `LICENSE` lève un drapeau ;
- une licence **retypée à la main** — guillemets typographiques, deux-points pleine largeur — est
  reconnue et **signalée comme non canonique**, parce qu'un texte retypé peut différer sur le fond.

**Ce que le contrôle durci a trouvé le jour même.** Trois choses qu'aucune étiquette n'affichait :
`winsenlabs/platos` porte **treize** fichiers LICENSE aux licences **mixtes** Apache-2.0 et MIT
selon le paquet ; `alibaba/open-code-review` et `Huangruiteng/loopx` incorporent du code amont
sous MIT alors que leur LICENSE est Apache-2.0 ; `JoyAgent-JDGenie` publie un Apache-2.0 **retypé
à la main**. Aucune n'est bloquante — toutes ces licences sont permissives — mais aucune n'était
visible sur la fiche du dépôt.

**Leçon transférable.** Un contrôle pris en défaut est une information, pas une honte : il dit où
la réalité diffère du modèle qu'on s'en faisait. **Le durcir le rend plus capable ; le desserrer
le rend inutile.** Et un contrôle qui n'a jamais vu de données réelles n'a pas encore été écrit,
il a été imaginé.

## E-34 — E-27 s'est reproduite : le shell a exécuté les accents graves, une troisième fois

**Constaté le** 2026-09-20 · **Survenu** le 2026-09-20 · **État** corrigé
· **Cite** E-27 (2026-09-16) et E-29 (2026-09-16)

**Ce qui s'est passé.** Création de quatre rôles d'agent par une fonction shell prenant le texte
de la mission en paramètre, entre guillemets doubles. Le shell a fait deux dégâts distincts :

1. **Les accents graves ont été exécutés.** `scripts/sas_licence.py` entre accents graves a été
   lancé comme une commande — « No such file or directory ». Le fichier `gardien-du-sas.md` est
   sorti à 49 lignes au lieu de 83 : **toute sa section « Les six contrôles » avait disparu**.
2. **Les apostrophes ont été perdues.** Pour contourner le premier problème j'avais écrit
   « qu on », « l air », « ce qu elles » sans apostrophe. Trente et une élisions mutilées dans
   trois fichiers, restituées ensuite par expression régulière.

**Cause racine.** E-27 avait déjà établi la contre-mesure : **heredoc entre quotes**. Je le
savais, je l'avais écrit, et j'ai quand même construit le contenu dans une chaîne shell — parce
qu'une fonction paramétrée paraissait plus élégante pour créer quatre fichiers d'un coup.
L'élégance a coûté un fichier mutilé et une correction par expression régulière.

C'est exactement la leçon d'E-29 : **celui qui écrit la règle l'enfreint aussi.** Deuxième
démonstration, sur la même règle, en quatre jours.

**Signal de détection.** Tu t'apprêtes à mettre du texte destiné à un FICHIER dans une variable
shell, un paramètre de fonction, ou une chaîne entre guillemets doubles. Le contenu contient des
accents graves, des apostrophes, des `$`, ou du markdown. Arrête-toi là.

**Contre-mesure, et elle est plus dure que celle d'E-27.** E-27 disait « utilise un heredoc entre
quotes ». Insuffisant : la règle se contourne dès qu'on veut factoriser. La règle durcie est :
**le contenu d'un fichier ne transite JAMAIS par le shell.** On l'écrit avec Python — `Write`,
`pathlib.write_text` — ou avec un heredoc entre quotes écrit en toutes lettres, jamais paramétré.
Une fonction shell qui prend du contenu en paramètre est le signal d'alarme lui-même.

**Contrôle qui aurait attrapé ça.** Compter les accents graves et les lignes du fichier produit,
et comparer au contenu attendu. Fait après coup ici : 8 accents graves pour 49 lignes contre 32
pour 83 attendues. Un écart visible en une seconde, à condition de regarder.

**Leçon transférable.** Une contre-mesure qui repose sur la discipline est une contre-mesure qui
sera contournée le jour où elle gêne. **Une règle n'est tenue que si la manière commode de faire
est aussi la manière correcte.**

## E-35 — 29 fiches d'agent envoient l'agent sur un projet sorti du périmètre

**Constaté le** 2026-09-22 · **Survenu** depuis le 2026-09-19 · **État** SIGNALÉ, non corrigé —
rien n'est supprimé ni réécrit sans l'accord de Chaima

**Ce qui s'est passé.** Écriture d'un contrôle des fiches d'agent. À sa première exécution il
accuse trente fiches d'être mutilées. Vérification avant de conclure — c'est la leçon d'E-25 —
et le contrôle avait tort sur le motif : il exigeait le socle CODEX de toutes les fiches alors
que **deux familles cohabitent**, 43 au socle CODEX et 29 sous une charte antérieure.

Mais en corrigeant le contrôle, la vraie faute est apparue, et elle est plus grave que celle
qu'il annonçait. L'article 1 de cette charte antérieure dit :

> « PÉRIMÈTRE : Caelum Partners uniquement. Interdit de démarrer un autre projet. »

Caelum Partners est **sorti du périmètre le 2026-09-19**. Vingt-neuf agents sur soixante-douze
s'instruisent donc eux-mêmes de travailler sur un projet qui n'existe plus pour nous — et
d'interdire tout autre projet, dont celui-ci.

**Cause racine.** Un périmètre a été changé **en conversation** et jamais dans les fiches qui le
portent. Rien ne reliait la décision aux fichiers qui l'appliquent. La décision était datée, la
propagation n'existait pas.

**Signal de détection.** Tu changes le périmètre, la priorité ou le nom d'un projet. Demande
immédiatement : **quels fichiers répètent l'ancienne version ?** Une consigne dupliquée dans
soixante-douze fichiers ne se change pas en la disant une fois.

**Contre-mesure.** Contrôle A6 dans `scripts/verifier_agents.py`, bloquant en CI : toute fiche
nommant un projet hors périmètre échoue, avec la date de sortie. Le contrôle **signale et ne
supprime pas** — §10, rien n'est supprimé sans l'accord de Chaima.

**Ce qui reste à trancher, et c'est à elle.** Trois options sur les 29 fiches : les retirer, les
réécrire au périmètre du projet actuel, ou les archiver telles quelles pour le jour où Caelum
reprendra. Tant qu'elle n'a pas répondu, le contrôle reste rouge — et un contrôle rouge qu'on
laisse rouge est une dette visible, ce qui vaut mieux qu'une dette invisible.

**Leçon transférable.** Une décision prise en conversation ne se propage pas toute seule dans les
fichiers qui l'appliquent. **Changer une règle sans chercher ses copies, c'est créer une
contradiction, pas une mise à jour.**

## FICHE VIERGE (à copier pour toute erreur nouvelle)

```
## E-xx — [titre en une ligne : le fait, pas le jugement]
**Constaté le** AAAA-MM-JJ · **Survenu** [période] · **État** [corrigé / non corrigé]
**Ce qui s'est passé.** Les faits, avec preuve et source datée. Aucune reformulation flatteuse.
**Cause racine.** Pourquoi c'était possible — pas qui a fauté.
**Signal de détection.** La situation concrète dans laquelle un agent doit penser à cette fiche.
**Contre-mesure.** Ce qu'on fait à la place, et quel rôle en répond.
**Leçon transférable.** Une phrase réutilisable hors de ce cas précis.
```

## RÈGLES DE TENUE
- **Ajout uniquement.** Une fiche n'est jamais réécrite : on corrige par une fiche nouvelle qui cite l'ancienne.
- **Pas de blâme.** On documente des causes, pas des coupables. Une base qui accuse cesse d'être alimentée.
- **Les erreurs des agents y figurent aussi** — E-03, E-10, E-11, E-12, E-14 et E-15 sont des fautes
  commises par un agent le 2026-09-11, pas des fautes héritées. Une base qui ne contient que les erreurs
  des autres est fausse.
- **Rien n'est supprimé** sans l'accord explicite de Chaima.
