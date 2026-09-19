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
| E-25 | Contrôle aveugle qui accuse au lieu de s'accuser | Tu écris un contrôle qui conclut sur ce qu'il ne voit pas | tous |
| E-26 | Livraison annoncée sans vérifier qu'elle existe | Tu dis « c'est poussé / la PR t'attend / c'est en ligne » | GARDIEN-CONTRÔLE-FINAL · tous |
| E-27 | Brochure corrigée, produit laissé faux | Tu corriges une affirmation présente à plusieurs endroits | tous |
| E-28 | Garde-fou aveugle à la faute qu'il devait empêcher | Tu écris un contrôle après une erreur | testeur-adverse · contre-verificateur-securite |

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

## E-26 — Une livraison a été annoncée à Chaima alors qu'elle n'existait pas

**Constaté le** 2026-09-11 · **Survenu** 2026-09-11 · **État** corrigé le soir même

**Ce qui s'est passé.** Après la fusion de la PR #19, la journalisation (registre, passation, rapport) a
été commitée et **poussée** sur la branche de travail. J'ai ensuite écrit à Chaima : « Je n'ai pas non plus
fusionné la PR du journal. Elle t'attend, c'est un clic. » **Cette PR n'avait jamais été créée.** La
branche était bien poussée — l'étape suivante, l'ouverture de la PR, n'avait pas été faite. Chaima s'est
endormie en croyant qu'un travail l'attendait au réveil ; il n'y avait rien à cliquer.

**Cause racine.** Le `git push` a réussi, et ce succès a été pris pour l'aboutissement de la chaîne. Une
chaîne de livraison a plusieurs maillons (commit → push → PR ouverte → CI verte → fusionnable) et le succès
d'un maillon ne dit rien des suivants. C'est la même racine que la fiche **E-22** — affirmer sans avoir
constaté — mais appliquée à **son propre travail**, qui est l'angle mort le plus difficile à voir : on sait
ce qu'on a voulu faire, et on le confond avec ce qu'on a fait.

**Le coût réel.** L'erreur est partie chez Chaima dans un message de fin de session, juste avant son départ.
Une affirmation fausse sur l'état d'une livraison est plus coûteuse qu'une affirmation fausse sur un fait
technique : elle organise le temps de quelqu'un d'autre.

**Signal de détection.** Tu écris « c'est poussé », « la PR t'attend », « c'est en ligne », « il n'y a plus
qu'à cliquer » — et tu t'appuies sur le succès de l'étape **précédente**, pas sur l'observation de l'état
que tu annonces.

**Contre-mesure.** Avant d'annoncer l'existence d'un livrable, l'**observer** : `list_pull_requests` pour
une PR, le listing du déploiement pour un fichier en ligne, `git log origin/<branche>` pour un push. Le
dernier maillon de la chaîne se vérifie explicitement, jamais par déduction depuis l'avant-dernier.

**Leçon transférable.** Le succès d'une étape ne prouve que cette étape. Une livraison n'est pas ce qu'on a
lancé, c'est ce qu'on a vu exister — et c'est sur son propre travail que l'on vérifie le moins.


## E-27 — La brochure a été corrigée et le produit laissé faux

**Constaté le** 2026-09-14 · **Survenu** 2026-09-14 · **État** corrigé le jour même

**Ce qui s'est passé.** Une affirmation juridique fausse a été corrigée dans `index.html` — l'exception
qui oblige les entités financières et anti-blanchiment à un canal de signalement sans seuil d'effectif.
La correction a été annoncée comme « le site est corrigé ». Le contradicteur a montré que
`assets/simulateur.js` portait **encore les deux formulations fautives**, et rendait un verdict **vert
« a priori non concerné »** à une entité que la loi oblige.

**Cause racine.** La même affirmation vivait à deux endroits — une carte de la page d'accueil et le
moteur du simulateur — et seul le premier a été cherché. La recherche s'est arrêtée au fichier où
l'erreur avait été *repérée*, au lieu de balayer tous les supports qui *portent* l'affirmation.

**Pourquoi c'est pire que ça n'en a l'air.** Le support oublié était le **produit**, pas la brochure.
Un visiteur fait davantage confiance à un simulateur qu'à une carte, parce qu'il lui répond
personnellement — et le verdict fautif était recopié dans le courriel de lead, donc archivé.
Corriger la page et pas l'outil, c'est corriger ce qui rassure et laisser ce qui engage.

**Signal de détection.** Tu corriges une affirmation — un seuil, une date, un chiffre, une exception —
et tu ne t'es pas demandé **combien de fichiers la portent**.

**Contre-mesure.** Avant de corriger, `grep` l'affirmation dans **tout** le périmètre publié, pas dans
le fichier où tu l'as trouvée. Puis poser un contrôle automatique qui exige la correction **dans chaque
support** — c'est ce que fait `scripts/verifier_coherence_juridique.py`, né de cette erreur.

**Leçon transférable.** Une correction n'est pas finie quand le fichier est juste : elle est finie quand
tous les supports qui portent l'affirmation sont justes. Et le support le plus important est celui qui
répond personnellement à l'utilisateur.

## E-28 — Un garde-fou était aveugle à la faute exacte qu'il devait empêcher

**Constaté le** 2026-09-14 · **Survenu** 2026-09-14 · **État** corrigé le jour même

**Ce qui s'est passé.** Après l'erreur E-27, un contrôle a été écrit pour empêcher qu'une correction
juridique soit appliquée à un support et pas à l'autre. Le contradicteur l'a attaqué, et les deux
pièges ont été **reproduits** : ils passaient au **vert**.

- « 1 000 salariés **OU** 450 millions » — le contrôle cherchait la chaîne « 450 M€ », jamais la
  conjonction. Or le OU mis pour le ET **était la faute d'origine**.
- « cette directive **est désormais** transposée » — l'empreinte cherchée, « transposée en droit
  belge », survivait à l'inversion complète du sens.

Le contrôle rendait donc impossible **une seule chose** : la suppression pure et simple de quatre
chaînes. Sous un intitulé — « cohérence juridique » — qui promettait bien davantage.

**Cause racine.** Un contrôle écrit en **motifs affirmatifs** ne peut pas détecter une négation ni une
substitution de conjonction : la sous-chaîne survit aux deux. Écrire ce qui doit être présent est
facile ; écrire ce qui doit être **absent** demande de se représenter la faute, pas la correction.

**Aggravant.** Le message de succès annonçait « la page et l'outil portent les mêmes corrections »,
puis « aucune des **5** affirmations » alors qu'il en contrôlait 7. Un contrôle qui exagère ce qu'il
prouve est pire que pas de contrôle : il crée une confiance qu'il ne mérite pas. C'est le §13 sur les
affirmations **à propos de nous**.

**Signal de détection.** Tu écris un contrôle après une erreur, et tu ne l'as pas éprouvé **sur cette
erreur-là**. Ou son message de sortie affirme plus que ce que son code teste.

**Contre-mesure.** Tout contrôle se pose avec ses **pièges** : on reproduit la faute d'origine, on
vérifie qu'il échoue, on la retire, on vérifie qu'il passe. Des motifs **interdits** en plus des motifs
exigés. Un compte, pas seulement une présence. Et un message de sortie qui ne promet que ce que le code
établit — les chiffres LUS, jamais écrits en dur.

**Leçon transférable.** Un contrôle jamais vu échouer n'est pas un contrôle. Et le premier piège à lui
poser est l'erreur pour laquelle il a été écrit.

## E-29 — Une liste de secteurs juridiques écrite de mémoire, puis annoncée « complète »

**Constaté le** 2026-09-19 · **Survenu** 2026-09-19 · **État** corrigé avant toute publication

**Ce qui s'est passé.** Pour rendre la question 3 du simulateur répondable, la liste des 18 secteurs
NIS2 a été écrite directement dans `products/caelum/site/simulateur.html`, de mémoire, sans ouvrir les
annexes de la directive (UE) 2022/2555 — puis présentée au visiteur comme « la liste complète ». Trois
lignes étaient fausses, vérification faite aux annexes le 2026-09-19 :
- « Transports : … routier » : l'annexe I, sous-secteur routier, vise les **autorités routières**
  chargées du contrôle de la gestion du trafic et les **opérateurs de systèmes de transport
  intelligents**. Le transport routier de marchandises n'y figure pas. Un transporteur belge se serait
  déclaré concerné à tort ;
- « Denrées alimentaires : … distribution » : l'annexe II vise les entreprises du secteur alimentaire
  « engaged in wholesale distribution and industrial production and processing ». Le commerce de détail
  en est exclu ;
- « Infrastructure numérique » : l'énumération omettait les points d'échange internet, les registres de
  noms de domaine de premier niveau et les réseaux de diffusion de contenu — omission du sens
  **rassurant**, donc la plus dangereuse.
Le nombre, lui, était exact : 11 secteurs à l'annexe I, 7 à l'annexe II.
Preuve : annexes I et II reproduites intégralement, consultées le 2026-09-19.

**Cause racine.** Le mot « complète » a été écrit pour un motif d'ergonomie — on ne peut pas exclure une
liste qu'on ne voit pas — sans que personne ne traite ce mot comme ce qu'il est : une affirmation
juridique **sur nous**, au sens du §13. Écrire « exemples de secteurs (~18) » n'engageait à rien ; écrire
« la liste complète » engage à l'avoir lue. Le passage de l'un à l'autre n'a déclenché aucune
vérification, parce que le contrôle `verifier_coherence_juridique.py` compare des chaînes qu'on lui a
données et ne sait pas qu'une liste neuve est apparue.

**Signal de détection.** Tu remplaces une formulation prudente et vague par une formulation ferme et
précise pour améliorer l'ergonomie. Le gain de confort du lecteur est exactement la mesure de ce que tu
viens de promettre. Mots déclencheurs : « complète », « tous les », « la liste des », « il suffit de ».

**Contre-mesure.** Toute énumération présentée comme exhaustive est recopiée depuis la source primaire
**pendant** qu'on l'écrit, pas relue après. `gardien-juridique-verite` est saisi avant le commit, pas
avant la fusion. Et quand l'accès réseau manque, on écrit « exemples » — jamais « complète ».

**Leçon transférable.** Rendre une question plus facile à répondre, c'est promettre davantage au
lecteur. L'ergonomie et l'exactitude ne sont pas deux sujets séparés : le confort qu'on offre est une
dette de preuve qu'on contracte.

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
