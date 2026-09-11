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
