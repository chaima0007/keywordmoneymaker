> **Rapatrié le 2026-09-14 depuis `chaima0007/test`** (fiche E-15). Journal de la chaîne veille/brevets/capitaux.
> Distinct de `📋 JOURNAL.md` à la racine, qui porte les snapshots d'entrée de session du CODEX §5.

# 📋 JOURNAL — chaîne Veille, Brevets, Technologies & Capitaux

> Snapshot par session de travail sur cette chaîne. Ajout en haut, jamais d'écrasement.

## 2026-09-11-23h15 (Europe/Brussels) — Consolidation + registre unifié + dossier DÉPOSANT n°1

**Contrôle honnête (§11)** — Aucun document quasi identique, et un a été **évité** : je n'ai PAS recopié
la charte consolidée au Drive, précisément pour ne pas recréer la divergence d'E-18. Le Drive reçoit les
dossiers ; les normes vivent dans le dépôt, à un seul endroit. `croque-mort` non saisi, aucune boucle.

**Consolidation faite, et elle rétrécit.** `veille/CHARTE-CONSOLIDEE-2026-09-11.md` — **99 lignes** de
lecture à jour contre 319 d'historique conservé. Le point important est ce qu'elle **rend** : la condition
d'arrêt, les règles de vérité, l'audit de chaîne, les trois rôles et la subordination sont désormais
assurés par le CODEX et les agents, souvent plus strictement — le §5 du CODEX va plus loin que mon §7.1.
Ne restent définies que cinq règles que rien d'autre ne couvre : divulgation art. 54 CBE, nommage Drive et
son plafond, emplacements de sauvegarde et leur état réel, cadence des offices, structure Drive.
La charte d'origine garde ses 12 sections, avec une bannière disant à quoi elle sert : comprendre
**pourquoi** une décision a été prise, jamais savoir ce qui s'applique.

**TROUVÉ EN CONSOLIDANT — deux registres d'erreurs coexistaient.** En relisant le CODEX §12 j'ai vu qu'il
impose `/🔴 ERREURS.md` à la racine — qui existait, avec 3 entrées, en parallèle de ma base de 19 fiches,
contenus partiellement recoupés et rien pour les comparer. **C'est E-18 en version pure, commise par moi
dans le dispositif écrit pour l'empêcher.**
Corrigé sans choisir un camp : `.claude/BASE-ERREURS.md` fait foi, `🔴 ERREURS.md` devient son **index
généré**, et un contrôle **bloquant** en CI échoue si les deux divergent. Un index dérivé ne peut pas
dériver. Les 3 entrées du registre racine n'ont rien perdu : deux sont devenues des fiches complètes —
**E-20** (outil d'audit pointé sur la mauvaise cible : il produit des résultats vrais mais hors sujet) et
**E-21** (état du site déduit du dépôt, pas du live) — la troisième correspondait déjà à E-02.
**21 fiches.** Détection prouvée dans les deux sens par test piégé.

**Défaut trouvé dans mon propre générateur**, en relisant sa sortie : il ne lisait que la première ligne
de métadonnées, donc E-17 ressortait « DOCUMENTÉE » alors que sa fiche dit « corrigé ». Corrigé. Le statut
n'est jamais inventé : il se déduit du vocabulaire de la fiche, et vaut « DOCUMENTÉE » quand aucune
correction n'est revendiquée. Les deux seules **NON CORRIGÉE** sont les vrais points ouverts : E-08 et E-13.

**Dossier DÉPOSANT n°1 ouvert** (Drive, « Brevetabilité de nos projets ») sur E-08, la LICENSE absente.
Quatre options avec leurs conséquences, **aucune appliquée** : choisir une licence engage la
commercialisation, donc c'est une décision de Chaima (§10). Le constat qui compte : la licence est en aval
d'un autre problème — ce dépôt public contient la méthode interne, et **aucune licence ne répare ça**.
Recommandé : « tous droits réservés » explicite maintenant (quelques minutes, réversible, ne concède
rien), choix de fond après la séparation public/interne.

**Vérifié** — `main` = `47d50bf`, les deux workflows VERTS avec le nouveau contrôle bloquant du registre ·
cloisonnement code 0 · sécurité VERT · publication toujours **19 fichiers**, site inchangé.

**BLOQUÉ PAR L'ENVIRONNEMENT, pas par la méthode** — le rôle **SCANNER** reste à zéro. Testé ce soir :
Espacenet, WIPO Patentscope, USPTO, DPMA et EUIPO répondent **tous HTTP 000**, refus au gateway du proxy,
comme `caelumpartners.agency`. Les axes de recherche et les priorités d'offices sont posés ; c'est un accès
à ouvrir, ou un travail à faire depuis un navigateur. Je ne le contournerai pas en inventant des résultats.

**Chez Chaima** — `uv run python main.py` · `caelum-coffre` · TMview · rendu du site · libellé de la
LICENSE.

## 2026-09-11-22h10 (Europe/Brussels) — Réconciliation faite · 44 → 56 agents · 0 suppression

**Contrôle honnête (§11)** — Aucun document quasi identique. **Élagueur non saisi** — et il faut noter
que ce rôle n'existe plus sous ce nom : c'est `croque-mort` qui l'assume désormais.

**Arbitrages de Chaima appliqués, rôle par rôle**
- `croque-mort` gardé, ÉLAGUEUR abandonné. `verificateur-verite` gardé, GARANT **fusionné** dedans avec
  sa nuance (« sur quoi repose la confiance ? » + remontée des NON VÉRIFIÉ en tête).
- Redécoupage en trois rôles nets : `superviseur-vigie` (état interne) · `guetteur` (menaces externes) ·
  `passerelle` (circulation de l'info). Plus aucun chevauchement.
- `cartographe` + `boussole` conservés, mandats écrits : l'un tient un ÉTAT, l'autre pose un CONSTAT.
- `conservateur-secrets` + `protecteur` conservés : fuite technique réparable vs fuite juridique
  irréparable. Sur un push public, les deux passent.
- Les 8 sans équivalent créés. **Total 44 → 56 agents, aucune suppression, aucun renommage.**

**Décision de forme que j'ai prise seul, et qui compte** — les 12 nouveaux adoptent le **format CODEX**
de la flotte existante (socle repris verbatim, hachage identique aux 44 autres ; puis mission,
déclencheur, décision possédée, interdits). Écrire dans le format de ma charte aurait introduit une
**troisième norme concurrente** : les fiches E-06 et E-18 exactement. Le dépôt avait changé de
convention entre-temps ; s'y plier valait mieux que défendre la mienne.

**Frontières réciproques.** Les 4 agents existants concernés ont reçu la frontière **en ajout** :
50 insertions, **0 suppression**, socle intact dans les quatre. Une frontière connue d'un seul côté n'est
pas une frontière.

**Fiche E-19 ajoutée (19 fiches)** — mon erreur du jour : une manipulation git pendant une fusion en
cours détruit `MERGE_HEAD` **sans avertissement ni erreur**. La commande réussit, l'information
disparaît. Attrapée par un contrôle explicite avant tout push, pas par une alerte de git.

**Vérifié** — socle des 12 identique au bit près aux 44 existants · 0 ligne supprimée dans les 4 agents
modifiés · cloisonnement code 0 · contrôle sécurité VERT · le pont Python lit bien 19 fiches et
`pour_action("fusion git")` renvoie E-19 · **le site publié ne change pas** : aucun fichier de
`products/*/site/` touché, simulation toujours à 19 fichiers · `main` = `d21a3bf`.

**Reste chez Chaima** — `uv run python main.py`, `caelum-coffre`, TMview, et la vérification du rendu.

## 2026-09-11-20h35 (Europe/Brussels) — Infrastructure fusionnée sur main, déploiement vert

**Contrôle honnête (§11)** — Aucun document quasi identique. **ÉLAGUEUR non saisi**, motif : aucune
boucle. Une erreur de ma part en revanche, consignée plus bas.

**FUSION FAITE — main = `94d932b`.** Fusion en deux temps comme décidé : l'infrastructure part,
les 13 agents restent en réserve sur `claude/chaine-veille-13-agents`.

**Déploiement VERT, prouvé par le journal du runner** (run 34633563819, toutes étapes succès) :
- « ── Contenu réellement publié (**19 fichiers**) ── » suivi de la liste exacte — **identique à ma
  simulation locale**, fichier par fichier.
- « vérification de propriété publiée : googleab8fcc73e6abfbb0.html » → Search Console préservée.
- **Aucun `::warning::fichier attendu absent`** : tous les fichiers de la liste blanche ont été trouvés
  à leur nouvel emplacement `products/caelum/site/`.
- Artefact 17 519 octets, déploiement créé pour `94d932b`, « Reported success! ».

**Le contrôle de cloisonnement a tourné en CI réelle et il est BLOQUANT** : étape « Cloisonnement des
produits (BLOQUANT depuis la phase 5) » — succès sur le runner. Ce n'est plus une preuve de bac à sable.

**Delta réel en production** — mesuré en simulant les deux workflows avant la fusion : main publiait
**26** fichiers, il en publie **19**. Les 19 sont identiques. Les 7 disparus sont tous CompeteIQ ou
KeywordMoneyMaker (Option 0, voulue). Zéro fichier nouveau.

**Ce que main avait fait entre-temps, et que j'ai intégré plutôt que contourné**
- 44 agents (pas 29), protocole CODEX (`codex/`, dont `codex/agents-correspondance.md`), vérification
  Google Search Console, retrait de `linkedin_cv/` du dépôt public.
- `.gitignore` : les DEUX blocs conservés. `codex/` autorisé à la racine par le contrôle. Entrée
  `linkedin_cv` retirée du contrôle, devenue sans objet.
- Le fichier de vérification Google déplacé de la racine vers `products/caelum/site/` : il fonctionnait
  par accident (le motif du workflow se résolvait à la racine) mais était séparé du site qu'il certifie.
- **Vérifié : les 8 fichiers de site apportés par main sont IDENTIQUES à mes copies déplacées** — aucun
  contenu perdu au passage en `products/`.

**MON ERREUR, à ficher (candidate E-19)** — j'ai lancé `git stash` et `git checkout` **pendant une
fusion en cours** pour calculer le delta de production. Ces manipulations ont détruit `MERGE_HEAD` :
la fusion n'était plus enregistrée comme telle, et committer aurait produit un commit sans `main`
comme parent — donc un conflit garanti à la fusion suivante. Détecté par un contrôle explicite de
`MERGE_HEAD`, pas par chance. Reprise propre : `reset --hard`, fusion refaite, corrections réappliquées.
**Leçon : une fusion en cours est un état fragile ; on ne fait aucune manipulation d'index ou de branche
avant de l'avoir finalisée.** Fiche non encore ajoutée à la base : elle partira avec la réconciliation
des agents plutôt que de motiver un second push sur main aujourd'hui.

**Reste, et c'est pour Chaima**
- **Le rendu final dans un navigateur.** Je ne peux pas le vérifier : la politique réseau de cet
  environnement refuse `caelumpartners.agency` (403 au gateway, confirmé sur curl et sur le fetch).
  Ce que je prouve s'arrête à ce que le runner a publié.
- `uv run python main.py` — commande transmise, sortie brute attendue.
- Réconciliation des 13 agents : questions posées rôle par rôle, arbitrage à elle.
- `caelum-coffre` : à créer par elle (403 sur l'intégration). Résultat TMview attendu.

## 2026-09-11-18h50 (Europe/Brussels) — Option B exécutée, 5 phases · Caelum Partners

**Contrôle honnête (§11)** — Pas de document quasi identique : six commits, cinq phases distinctes,
chacune avec son propre objet. Condition d'arrêt respectée. **ÉLAGUEUR non saisi**, motif : aucune
boucle, aucune piste morte — la migration a avancé à chaque étape.

**Les 5 phases, dans l'ordre, phase 4 isolée comme demandé**
- **P1** `scripts/audit_cloisonnement.py` écrit AVANT tout déplacement, en mode avertissement.
  Choix payant immédiatement : il a mesuré au lieu de supposer.
- **P2** `shared/` extrait (14 modules en `git mv`, historique préservé) + `shared/attribution.py`
  comme source unique + **mémoire découpée par produit** (`.memory/{caelum,kmm,competeiq,shared}.json`).
  Lectures agrégées pour ne rien changer à l'affichage, écritures routées vers le propriétaire.
- **P3** 19 modules rangés en `products/{caelum,kmm,competeiq}/agents/`. `agents/` disparaît.
- **P4** sites en `products/*/site/`, `deploy.yml` recâblé. **Seule phase à risque, commit isolé.**
- **P5** bascule du contrôle en **bloquant**, détection prouvée par test piégé.

**Ce que la phase 1 a corrigé dans mon propre plan.** C1 passait, mais C3 échouait **12 fois** :
quatre modules que j'avais classés transverses d'après les catégories de `main.py` importent en
réalité des modules KMM. Ce sont des orchestrateurs du pipeline SEO, pas du transverse. Attribution
refaite **sur la preuve des imports**. Répartition réelle : caelum 5 · kmm 11 · competeiq 4 · shared 15
— loin des « 2 modules partagés » que mon plan annonçait.

**E-18 : une divergence trouvée dans ma propre machinerie anti-divergence.**
Le test piégé de la phase 5 a révélé qu'un piège **ne se déclenchait pas** : après migration, le
chemin suffisait à attribuer un module, mais `main.py` interrogeait encore la table pour router la
mémoire. Deux sources répondaient à la même question, sans que rien ne les compare — la faute d'E-01,
commise dans le module écrit pour l'empêcher. Une relecture n'aurait rien vu : les deux moitiés
étaient correctes séparément. Corrigé : le disque fait foi, la table devient un repli, et un contrôle
**C4** compare les deux. **Un piège qui ne se déclenche pas est une information, pas un succès.**

**Vérifié (avec preuve)**
- Simulation à blanc du déploiement après la phase 4 : **exactement les 18 mêmes fichiers** qu'avant.
  Le site publié est inchangé — c'était la contrainte qui gouvernait cette phase.
- Trois garde-fous de déploiement re-testés par pièges après réécriture : fichier interne → bloqué ·
  produit hors périmètre → bloqué · CNAME absent → bloqué · témoin légitime → passe.
- Cinq contrôles de cloisonnement testés par pièges en mode bloquant : tous bloquent, témoin passe.
- Résolution de chemin prouvée module par module (`importlib.find_spec`), sans exécuter le code.
- Routage de la mémoire testé : 4 lancements de 4 propriétaires atterrissent chacun au bon endroit.
- Compilation de `main.py` et des 35 modules. Contrôle sécurité du projet **VERT**. Push vérifié.

**Limite honnête** — `__import__` d'un module d'agent échoue dans ce bac à sable sur
`claude_agent_sdk`, dépendance déclarée au `pyproject.toml` mais non installée ici. Ce n'est pas un
défaut de la migration : `find_spec` prouve que Python trouve bien chaque fichier à sa nouvelle place.
La vérification d'exécution réelle reste à faire par Chaima avec `uv run python main.py`.

**Trois décisions laissées à Chaima, rien n'a été déplacé**
- `superviseur` : marqué PROVISOIRE dans le code. Il s'annonce « scan santé de la flotte », donc
  transverse, mais n'inspecte que des modules KMM. Le rendre réellement transverse est un refactor.
- `linkedin_cv/` : production personnelle, pas un produit. Toléré à la racine en attendant sa décision.
- `products/kmm/agents/__init__.py` : inutile puisque les imports sont à plat. Conservé, non supprimé.

**Reste** — vérification d'exécution de `main.py` par Chaima · création de `caelum-coffre` (403,
droit à accorder) · résultat TMview · aucune PR, aucun merge : la fusion vers `main` lui appartient.

## 2026-09-11-18h05 (Europe/Brussels) — Option 0 exécutée · Option B planifiée · Caelum Partners

**Contrôle honnête (§11)** — Pas de document quasi identique : l'Option B détaillée est un plan
d'exécution, pas une reformulation du plan à 3 options de 17h35 (qui comparait ; celui-ci exécute).
Condition d'arrêt respectée. **ÉLAGUEUR non saisi**, motif : aucune boucle, aucune piste morte.

**Option 0 — EXÉCUTÉE et poussée.** `caelumpartners.agency` ne sert plus que Caelum.
- Retirés de la liste blanche : `competeiq-landing.html`, `keywordmoneymaker-index.html`, et les
  dossiers `competeiq/`, `intelligence/`, `kmm/`, `keywordmoneymaker/`, `seo/`. Les fichiers **restent**
  au dépôt, ils ne sont plus servis.
- Conservés car tous Caelum : `caelum/`, `agence/`, `home/` (redirigent vers « / ») et `nl/`.
- **Fait aggravant trouvé en vérifiant :** `keywordmoneymaker-index.html` n'avait **pas** de `noindex`.
  La page « AI SEO Content Generator » était donc **indexable** sur le domaine d'un conseil en
  conformité. Ce n'était plus une hypothèse de positionnement, c'était mesurable.
- **Garde-fou 3 ajouté, bloquant** : le déploiement échoue si un fichier ou un dossier produit
  réapparaît dans le contenu public. La règle est vérifiée par la machine, pas par la mémoire (E-01).

**Vérifications avant modification (aucune supposition)**
- `grep` sur tout le contenu publié : **aucune** page Caelum ne liait ces produits → zéro lien mort.
- `sitemap.xml` : ne listait que des URL Caelum → aucune modification nécessaire.
- `robots.txt` : rien à changer.
- Cibles réelles des dossiers lues une par une : `caelum/`, `home/`, `agence/` → « / » ; les cinq
  autres → les deux pages produits. Tous en `noindex`.
- Simulation à blanc du script de publication : **18 fichiers, tous Caelum**.
- **Détection prouvée par deux tests piégés** (fichier produit réintroduit ; dossier produit
  réintroduit) : les deux sortent en code 1. Un garde-fou qui ne bloque pas pendant un essai n'est
  pas un garde-fou prouvé.
- `_redirects` : les règles pointant vers les cibles retirées sont **commentées, non supprimées**.
  Actives, elles renverraient 404 après une migration Cloudflare/Netlify — le piège que l'en-tête du
  fichier signale déjà dans l'autre sens.
- Contrôle sécurité du projet : **VERT sur les contrôles bloquants**.

**Option B — PLANIFIÉE, RIEN D'EXÉCUTÉ.** Plan à 5 phases au Drive (« Plans de mise en œuvre »).
Ordre imposé par les dépendances et le risque : (1) écrire le contrôle CI en mode avertissement
**avant** tout déplacement, pour mesurer l'état réel au lieu de le supposer · (2) extraire `shared/`
— le point dur, dont tout dépend · (3) déplacer les agents par produit en `git mv` (l'historique suit,
avantage décisif sur l'Option A) · (4) sites + `deploy.yml`, **seule phase à risque réel**, isolée dans
son propre commit · (5) basculer le contrôle CI en bloquant, détection prouvée par test piégé.
**ESTIMATION : 2 à 2,5 sessions.**

Point d'insertion du contrôle CI, en deux endroits volontairement distincts :
`securite-code.yml` pour le cloisonnement du code (tourne à chaque push et PR, donc un import croisé
devient impossible à merger), `deploy.yml` pour le périmètre de publication (déjà en place). Les
fusionner laisserait passer l'un des deux.

**Trois décisions signalées comme n'étant pas les miennes** : sort de `main.py` (lanceur unique
transverse ou un par produit), de `.caelum_memory.json` (unique ou par produit), et des sites non
publiés (rester sous `products/` ou sortir tout de suite, ce qui serait déjà l'Option A partielle).

**Reste / en attente de Chaima** — feu vert Option B · création de `caelum-coffre` (403, droit à
accorder) · résultat TMview · aucune PR, aucun merge.

## 2026-09-11-17h35 (Europe/Brussels) — Points 1, 4 exécutés · 3 bloqué · 5 proposé · Caelum Partners

**Contrôle honnête (§11)** — Aucun document quasi identique : un plan (neuf) et une fiche E-17 (ajout).
La condition d'arrêt a fonctionné, et mieux que ça : ce cycle a **réduit** la duplication au lieu d'en
créer. **ÉLAGUEUR non saisi**, motif : aucune boucle, aucune piste morte.

**Point 1 — FAIT.** Les 13 agents réduits à un pointeur de 2 lignes vers `CLAUDE.md` §2 ter + la base.
Le texte normatif vivait en 14 endroits : c'était reproduire la divergence d'E-01. 8 sections par agent
désormais, contre 9.

**Point 3 — BLOQUÉ, pas oublié.** `caelum-coffre` **n'a pas pu être créé** : l'API GitHub répond
**403 « Resource not accessible by integration »**. L'intégration de cette session n'a pas le droit de
créer un dépôt. Ce n'est pas un échec transitoire (E-16 : « non autorisé », pas « en échec ») — aucune
relance ne le résoudra. À créer par Chaima, ou en élargissant les droits de l'intégration.

**Point 4 — FAIT.**
- `agents/base_erreurs.py` : passerelle de la flotte Python vers la base. Conception clé — il **lit**
  `.claude/BASE-ERREURS.md` et `CLAUDE.md`, il ne recopie rien. Preuve que ça marche : l'ajout d'E-17
  a été repris par le module **sans aucune modification de code**.
  Échec bruyant volontaire : une base illisible lève une exception au lieu de retourner vide — ne jamais
  laisser croire « aucune erreur connue » quand la réponse est « je n'ai pas pu vérifier » (E-16).
  Greffé au démarrage de `main_loop()`. Testé : import OK, 17 fiches lues,
  `pour_action("je crée un dossier au Drive")` → E-01, E-03, E-12, E-14.
- `.claude/FRONTIERE-SUBSTRATS.md` : la frontière des deux substrats, avec qui possède quoi, la règle
  d'arbitrage, les interdits croisés, et la seule chose qui traverse (la base). Référencée au
  `CLAUDE.md` §2 ter, point 3.
- Couverture réelle corrigée : la règle atteint désormais les **75** agents (42 Markdown + 33 Python),
  contre 42 auparavant.

**Point 5 — PROPOSÉ, NON EXÉCUTÉ.** Plan à 3 options au Drive (« Plans de mise en œuvre »).
En établissant les faits, une **Option 0** est apparue, non envisagée dans la demande : retirer les
autres produits de la liste blanche de publication. Elle supprime le coût réel du mélange — la dilution
du positionnement de Caelum — en ~30 minutes, sans toucher à la production. Recommandé : Option 0
maintenant, Option B (mono-repo cloisonné + contrôle CI) ensuite si besoin, Option A (3 dépôts)
seulement quand un produit gagne domaine et revenus.

**Trouvé en chemin — E-17 ajoutée à la base (17 fiches).**
Le commentaire de `deploy.yml` documente l'incident d'exposition signalé par Chaima au départ : le
workflow publiait `path: '.'`, donc `CLAUDE.md`, `ETAT.md`, `reports/`, `.claude/`, `agents/` et un CV
étaient lisibles sur `caelumpartners.agency`. Il **manquait** à la base. Cause racine : liste noire
implicite — tout publié sauf ce qu'on pense à exclure. Corrigé de longue date par liste blanche + 2
garde-fous bloquants ; la fiche existe pour qu'ils ne soient jamais affaiblis.

**Autre fait établi, qui change le point 5 :** un seul domaine (`caelumpartners.agency`) sert les trois
produits sous des sous-chemins. Et la flotte Python n'est pas séparable proprement —
`decision_simulator.py` (Caelum + CompeteIQ) et `gdpr_garde.py` (Caelum + KMM) servent deux produits.

**Vérifié (avec preuve)** — 8 sections par agent après réduction · `py_compile` sur `main.py` et
`base_erreurs.py` · import et fonctions testés hors `main.py` · contrôle sécurité du projet **VERT sur
les contrôles bloquants** après chaque modification · push vérifié · read-back Drive.

**Reste / en attente de Chaima** — création de `caelum-coffre` (droits) · résultat du check TMview ·
feu vert Option 0 et choix Option A/B · aucune PR, aucun merge.

## 2026-09-11-16h55 (Europe/Brussels) — Base d'erreurs + contrôle avant rapport · Caelum Partners

**Contrôle honnête (nouvelle règle §11, appliquée dès cette entrée)**
- Documents quasi identiques produits récemment ? **Non.** Les 13 documents de rôle partagent une
  structure mais diffèrent en substance (mission, déclencheur et décision possédée distincts) — c'est
  la demande de Chaima, pas de la duplication. Le rectificatif de 16h40 recouvre la table de 16h20 sur
  le fond, mais il existe **parce que** l'écrasement est interdit : c'est la règle qui fonctionne.
- Condition d'arrêt fonctionnelle ? **Oui**, et vérifiable : aucun document neuf n'a été créé pour un
  état inchangé ; le `Calendrier des expirations` a été déposé à **0 entrée** plutôt que rempli de
  fiction ; aucune entrée de journal n'a été écrite sans changement d'état réel.
- **ÉLAGUEUR non saisi**, motif : aucune piste morte, aucune boucle. Un seul point de dérive signalé,
  de forme et non de fond — la charte a reçu 5 sections en un jour et devient longue (travers E-04).
  Consolidation datée à proposer par l'ARCHITECTE, inscrite en dette dans la charte §11.

**Fait — aux deux emplacements demandés**
- **Base d'erreurs : 16 fiches.** GitHub : `.claude/BASE-ERREURS.md` (dépôt Caelum, branche
  `claude/chaine-veille-13-agents`), placée à côté des agents pour qu'ils puissent la lire réellement.
  Drive : miroir dans « Synergies inter-agents ».
- Les 3 erreurs nommées par Chaima y sont : E-01 (règle anti-doublon de juillet ignorée un mois),
  E-02 (faux positif « PR#2 non mergée » répété ~30 fois), E-03 (`fileSize` trompeur → read-back).
- **13 autres erreurs ajoutées**, identifiées le même jour : titres de 300-400 caractères · index
  obsolète · deux conventions concurrentes · deux flottes d'agents dont une non documentée · dépôt
  public sans LICENSE · dépôt public inapte à sauvegarder du sensible · entité HTML littérale · clone
  superficiel pris pour l'historique · conversion Drive altérante · recherche web prise pour un
  registre · deux racines projet · contenu déposé dans le mauvais dépôt · service en échec pris pour
  inexistant.
- **6 des 16 fiches sont des fautes commises par un agent ce jour** (E-03, E-10, E-11, E-12, E-14,
  E-15). Une base qui ne contiendrait que les erreurs des autres serait fausse.
- **Règle de contrôle avant rapport** inscrite au `CLAUDE.md` **§2 ter** du dépôt Caelum — le seul
  document que les 42 agents appliquent. La charte seule n'aurait lié que les 13.
- Les 13 agents portent désormais 9 sections : + « AVANT D'AGIR — BASE D'ERREURS » et « AVANT TOUT
  RAPPORT — CONTRÔLE HONNÊTE ».

**Vérifié (avec preuve)**
- `.claude/BASE-ERREURS.md` : 19 417 octets, 16 fiches (comptage `grep`).
- 9 sections confirmées dans chacun des 13 agents.
- Contrôle sécurité du projet relancé après modification : **VERT sur les contrôles bloquants**.
- Push vérifié sur les deux dépôts. Read-back Drive effectué.

**Non fait, volontairement**
- **Les 29 agents préexistants n'ont pas été modifiés un par un.** La règle les lie via le
  `CLAUDE.md` §2 ter, ce qui suffit et évite 29 modifications dans un système qui n'est pas le mien.
- **Aucune PR, aucun merge.** `CLAUDE.md` est un fichier maître : sa modification attend l'accord de
  Chaima et reste sur la branche.

## 2026-09-11-16h40 (Europe/Brussels) — 13 agents créés sur décision de Chaima · Caelum Partners

**Décision reçue et exécutée**
- Chaima n'a pas retenu la recommandation de fusion : les 13 rôles restent **distincts et nommés**.
  Après explication du raisonnement, elle a confirmé et demandé de vrais fichiers, pas de la
  documentation. Exécuté. La recommandation de 16h20 est annulée par un rectificatif daté (le document
  d'origine n'a pas été écrasé).
- Position révisée honnêtement : deux de ses arguments implicites étaient plus forts que les miens —
  l'indépendance du CONTRÔLEUR est structurellement impossible à obtenir d'un agent unique, et
  l'asymétrie des coûts (faux GO brevet vs cycle gaspillé) justifie la redondance. Maintenu et non
  contesté : l'orchestration reste subordonnée à `meta-orchestrateur`.

**Fait — aux deux emplacements demandés**
- **GitHub** : 13 fichiers `.claude/agents/*.md` dans `chaima0007/keywordmoneymaker`, branche
  `claude/chaine-veille-13-agents`. Parc : **29 → 42 agents**. Accès en écriture obtenu en cours de
  session (le dépôt n'était accessible qu'en lecture jusque-là).
- **Drive** : 13 documents dans « Synergies inter-agents », un par rôle, + 1 rectificatif.
- Chaque agent porte 7 sections dont les 5 demandées : mission · déclencheur · décision possédée ·
  interdits · passation.
- Garde-fous inscrits dans chaque fichier : condition d'arrêt anti-boucle · rappel art. 54 CBE (ce
  dépôt est public) · subordination hors domaine · GUETTEUR strictement défensif.

**Vérifié (avec preuve)**
- Contrôle de forme des 13 : frontmatter valide, `name` conforme au nom de fichier, 7 sections
  présentes dans chacun — identique à la structure des 29 existants (comparaison faite sur
  `qa-verificateur.md`).
- **Contrôle sécurité du projet** (`scripts/audit_code_sur.py`, règle §2 bis du `CLAUDE.md`) exécuté :
  **VERT sur les contrôles bloquants** (secrets, code à risque). Les 2 avertissements — 4 actions CI
  non épinglées par SHA, 3 licences non vérifiées — sont **préexistants** et sans lien avec ces fichiers.
- Read-back Drive : les 14 documents listés avec une taille réelle de 2,5 à 6,8 Ko.
- Push vérifié sur les deux dépôts.

**Non fait, volontairement**
- **Aucune PR, aucun merge vers `main`.** La fusion est une décision de Chaima. Branche poussée, prête.
- Nommage de fichier choisi `gardien-controle-final` et non `gardien`, pour ne pas entrer en collision
  avec l'agent existant `gardien-juridique-verite`. Deux gardiens, deux périmètres.

## 2026-09-11-16h20 (Europe/Brussels) — Décisions de Chaima appliquées · projet : Caelum Partners

**Décisions reçues et exécutées**
- Les **3 rôles** (DÉPOSANT · HORLOGER · ÉLAGUEUR) et les **5 améliorations** sont ACCEPTÉS.
  Intégrés à la charte, §6 et §7. La chaîne passe à **38 rôles**.
- **Arbitrage des deux racines Caelum :** Chaima retient le dossier existant déjà structuré et actif,
  « 🗂️ Caelum — Journal d'Audit (Travaux techniques) ». Exécuté : `Veille & Opportunités` et ses
  32 sous-dossiers y ont été déplacés ; le conteneur `Caelum Partners` créé plus tôt aujourd'hui,
  vérifié **vide**, a été mis à la corbeille (récupérable, non supprimé définitivement).

**Fait**
- **Amélioration n°2 livrée** — table de correspondance des **29 agents en place vs 38 rôles**
  (Drive, « Synergies inter-agents »). Résultat : le recouvrement est concentré sur **deux couches
  seulement**, l'orchestration et la vérification. 13 rôles n'ont pas à être créés comme agents
  autonomes ; **17 sont réellement nouveaux** et s'activent sans conflit ; 8 voient leur périmètre
  restreint. Règle d'articulation retenue : la chaîne veille **se branche sous** `meta-orchestrateur`
  comme un domaine, elle ne se place pas à côté.
- Charte complétée : condition d'arrêt anti-boucle (§7.1), articulation (§7.2), dépôt privé (§7.3),
  plafond de nommage à 120/60 caractères (§7.4), première vague à 5 offices (§7.5).

**Vérifié (avec preuve)**
- Les 29 agents lus un par un dans `.claude/agents/*.md` — pas résumés, lus.
- `CLAUDE.md` §2 et §2 bis lus intégralement : la qualité en 3 couches et la chaîne de vérification
  du code tiers **existent déjà**. La chaîne veille s'y rattache au lieu de les dupliquer.
- Dossier `Caelum Partners` vérifié vide (requête Drive sur ses enfants) **avant** mise à la corbeille.
- Read-back des documents Drive après création.

**Trouvé — à arbitrer par Chaima (préexistant, hors périmètre)**
- Le dépôt Caelum contient **deux flottes distinctes** : 29 agents Markdown dans `.claude/agents/`
  et ~35 modules Python dans `agents/` (`avocat.py`, `fiscaliste.py`, `innovateur.py`,
  `superviseur.py`, `commandant.py`…). Le `CLAUDE.md` ne décrit que la première. Doublon structurel
  antérieur à cette chaîne. **Rien n'a été fusionné ni supprimé.**
- Angle mort dans les deux systèmes : `accessibilite` (WCAG) n'a aucun rôle correspondant dans la
  chaîne des 38.

**Contradiction de normes trouvée (consignée, non tranchée unilatéralement)**
- Le dossier Journal d'Audit contenait déjà un « LISEZ-MOI — Règles du journal » du **2026-07-13**
  portant une convention de nommage **différente** de celle donnée par Chaima ce jour. Les deux ne
  peuvent pas coexister. Retenu en attendant arbitrage : la convention du 2026-09-11 prévaut.
  **Le document existant n'a pas été modifié.** Détail : charte §8.
- Enseignement : la règle anti-doublon **existait déjà** au 2026-07-13 (« avant de créer un fichier, on
  vérifie qu'il n'existe pas déjà »). Elle a été enfreinte une trentaine de fois en juillet-août.
  L'amélioration §7.1 ne crée donc rien de neuf — elle **rétablit** une discipline abandonnée. Le
  manque n'était pas la règle, mais un rôle habilité à arrêter la boucle : c'est l'ÉLAGUEUR.
- L'« Index des entrées » du LISEZ-MOI est obsolète (1 ligne pour ≥ 9 documents). Non corrigé sans accord.

**Reste / bloqué (inchangé depuis 15h59)**
- **Marque « Caelum Partners » : NON VÉRIFIÉ** — registres EUIPO/BOIP non interrogeables d'ici.
  Premier dossier du DÉPOSANT dès que la vérification est faite. Risque commercial actif.
- Rôle 1 SCANNER : non commencé. Cadence désormais bornée à 5 offices en première vague.
- Dépôt privé pour le Coffre : non créé — il portera un nom sous le compte GitHub de Chaima,
  j'attends son accord sur ce point précis avant de créer quoi que ce soit.
- Dépôt Caelum sans `LICENSE` : à corriger par le DÉPOSANT (accès en écriture non disponible d'ici).

## 2026-09-11-15h59 (Europe/Brussels) — Session d'amorçage · projet : Caelum Partners

**Fait**
- Structure Drive créée : `Caelum Partners/Veille & Opportunités/` + 8 catégories + bibliothèque
  brevets à 22 juridictions + « Opportunités académiques non exploitées » = **33 dossiers**.
  Placée à la racine du Drive, pas dans le dossier transversal « COMPILATION & SYNOPSIS » (règle
  « par projet, jamais mélangé »).
- Projet identifié et lu : Caelum Partners = RegTech conformité PME belges (Peppol, NIS2, RGPD,
  lanceurs d'alerte, CSRD/DORA) + simulateur « Suis-je concerné ? » calculé côté client.
  Dépôt `chaima0007/keywordmoneymaker`, HEAD `c1de9a9`.
- **Rôle 0 INSPECTEUR** — verdict n°1 rendu sur le simulateur de conformité : **NO-GO brevet**,
  trois motifs indépendants (exclusion art. 52 CBE / nouveauté détruite art. 54 / absence
  d'activité inventive art. 56). Objection du CONTRADICTEUR intégrée et traitée.
  Titres alternatifs identifiés : droit d'auteur (acquis), droit *sui generis* des bases de données
  (l'actif le plus solide), marque (à vérifier), secret d'affaires (indisponible car dépôt public).
- Charte de chaîne + convention de nommage + règle de divulgation : ce dépôt, `veille/`.
- `Calendrier des expirations à venir` créé au Drive : **0 entrée**, honnêtement vide, avec les
  colonnes obligatoires et les 4 axes de recherche retenus pour le premier passage SCANNER.

**Vérifié (avec preuve)**
- Clone anonyme du dépôt Caelum réussi → dépôt **public** confirmé.
- Scan de secrets sur le dépôt Caelum : **0 correspondance réelle** (les seules occurrences sont les
  regex du scanner du projet lui-même). Bon point.
- Read-back du document INSPECTEUR après création au Drive : contenu complet et intègre.
- Base juridique COMVIK (T 641/00) et G 1/19 confirmée sur sources publiques datées.

**Reste / bloqué**
- **Marque « Caelum Partners » : NON VÉRIFIÉ** — EUIPO eSearch et BOIP sont des applications
  JavaScript non interrogeables depuis cet environnement. Aucun résultat inventé. À faire dans un
  navigateur. **Risque commercial actif** : le nom est déjà exploité publiquement.
- Rôle 1 SCANNER : non commencé (22 offices). Axes de recherche définis, priorités posées.
- Sauvegarde GitHub du contenu sensible : **impossible en l'état** — dépôt Caelum public, dépôt privé
  requis. Accès en écriture au dépôt Caelum non disponible depuis cette session (lecture seule).
- Dépôt Caelum **sans fichier LICENSE** → ambiguïté sur les droits des tiers. À corriger.
- Recouvrement à résoudre : 29 agents déjà en place dans le dépôt Caelum vs les 35 rôles de cette
  chaîne (voir charte §5).

**Dépend de Chaima**
- Accord sur les rôles et améliorations proposés (rien n'a été ajouté sans accord).
- Vérification de la marque au registre, ou mandat pour la faire faire.
- Décision sur le dépôt privé de sauvegarde.
