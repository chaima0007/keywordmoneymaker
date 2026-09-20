# 2026-09-19-16h08 — Caelum Partners — Correction — Les questions du simulateur, et trois lignes de droit écrites de mémoire

**SYNOPSIS.** Chaima a fait son propre simulateur et a répondu « Je ne sais pas » à deux questions
sur quatre. Les quatre questions ont été réécrites pour qu'un dirigeant puisse y répondre sans
appeler son comptable. Deux relectures adversariales ont trouvé six défauts, dont trois affirmations
juridiques fausses que j'avais écrites de mémoire. Tout est corrigé sur la branche
`ux/questions-simulateur`, rien n'est publié : aucune PR n'est ouverte et le déploiement ne se
déclenche que sur `main`.

**Contrôle honnête avant rapport (§2 ter).** Aucun document quasi identique produit récemment : le
dernier rapport porte sur la cartographie du 2026-09-16, et la vérification des sources légales du
2026-09-14 portait sur les cartes de la page d'accueil, pas sur les questions. La condition d'arrêt a
fonctionné : ce rapport existe parce que l'état a réellement changé — deux commits, une fiche
d'erreur, trois corrections de droit. L'ÉLAGUEUR n'est pas saisi.

## Ce qui a été fait

Fichiers touchés :
- `products/caelum/site/simulateur.html`
- `products/caelum/site/assets/simulateur.js`
- `products/caelum/site/assets/caelum.css`
- `.claude/BASE-ERREURS.md` et `🔴 ERREURS.md` (index régénéré)
- `codex/A-DECIDER.md`

Deux commits sur la branche `ux/questions-simulateur` : `9a35d96` puis `b3f9f05`.

### 1. Les questions, rendues répondables

Le jargon a disparu là où il empêchait de répondre. « Assujettie à la TVA » et « B2B » sont devenus
un numéro au format BE 0123.456.789 sur une facture qu'on a sous la main. La question sur l'effectif
dit le cas majoritaire : si personne n'est salarié, c'est « moins de 50 ». La liste des secteurs NIS2
est affichée en entier — on ne peut pas exclure une liste qu'on ne voit pas — et chaque question
s'annonce « Question N sur 4 », la barre de progression étant dans le bandeau, donc hors écran au
moment où elle servirait.

### 2. Ce que l'avocat du client a trouvé, et que j'ai corrigé

Mon libellé « Non — aucun nom, aucune adresse, aucun numéro de téléphone, nulle part » opposait une
clause en quatre membres à un « Oui » d'un mot. La réponse vers laquelle il poussait est exactement
celle qui justifie notre offre : le design était indistinguable d'une pression vers la réponse qui
vend. Remplacé par « Non — je ne conserve aucune donnée nominative ». Dans le moteur, la carte qui
répondait « Réponse rare… Revérifiez » — un reproche adressé à qui venait d'être dissuadé — est
devenue un constat.

Sa proposition de faire absorber par la question 2 le cas des entreprises soumises sans seuil
d'effectif a été ÉCARTÉE : elle ferait cocher « 50 travailleurs ou plus » à une fiduciaire de douze
personnes, réponse fausse qui alimente aussi le critère de taille NIS2. Ce cas appelle la cinquième
question, déjà en attente de Chaima.

### 3. Ce que le gardien juridique a trouvé, et qui était le plus grave

Trois lignes de ma liste « complète » étaient fausses. Elles ne l'auraient pas été si je l'avais
recopiée depuis les annexes au lieu de l'écrire de mémoire. Fiche `E-29` de la base d'erreurs.

## Vérifié

Chaque affirmation ci-dessous porte sa trace sur la ligne même, comme l'exige la règle R7 du contrôle.

VÉRIFIÉ le 2026-09-19 sur https://www.nis2-info.eu/regulation/nis2/annex/0 (annexe I reproduite
intégralement) — le sous-secteur routier vise les autorités routières chargées du contrôle de la
gestion du trafic et les opérateurs de systèmes de transport intelligents. Le transport routier de
marchandises n'y figure pas. Ma ligne disait « Transports : … routier », sans plus.

VÉRIFIÉ le 2026-09-19 sur https://www.nis2-info.eu/regulation/nis2/annex/1 (annexe II reproduite
intégralement) — le secteur alimentaire ne vise que les entreprises « engaged in wholesale
distribution and industrial production and processing ». Le commerce de détail en est exclu ; ma
ligne disait « distribution », sans le mot « en gros ».

VÉRIFIÉ le 2026-09-19 sur https://www.nis2-info.eu/regulation/nis2/annex/0 — l'infrastructure
numérique comprend aussi les points d'échange internet, les registres de noms de domaine de premier
niveau et les réseaux de diffusion de contenu, que mon énumération omettait. Omission du sens
rassurant, donc la plus dangereuse des trois.

VÉRIFIÉ le 2026-09-19 sur https://www.nis2-info.eu/regulation/nis2/annex/0 — le compte de 18 secteurs
tient : 11 à l'annexe I, 7 à l'annexe II. Le chiffre « 18 » n'est pas écrit dans la directive ; la
page dit donc « les 11 de l'annexe I et les 7 de l'annexe II ».

VÉRIFIÉ le 2026-09-19 sur https://efacture.belgium.be/fr/article/pour-qui-la-facturation-electronique-deviendra-t-elle-obligatoire
(SPF Finances) — le régime de la franchise TVA ne dispense PAS de l'e-facturation : « L'obligation
s'applique donc également si vous utilisez le régime de la franchise de taxe pour les petites
entreprises ». Les dispenses d'émission se limitent aux faillis, aux assujettis ne réalisant que des
opérations exemptées par l'article 44 du Code TVA, aux forfaitaires (article 56, jusqu'au 01/01/2028
au plus tard) et aux assujettis non établis en Belgique sans établissement stable.

VÉRIFIÉ le 2026-09-19 sur https://efacture.belgium.be/fr/article/pour-qui-la-facturation-electronique-deviendra-t-elle-obligatoire
— facturer uniquement des particuliers dispense d'ÉMETTRE, pas de RECEVOIR : « vous devez être en
mesure de recevoir des factures électroniques structurées de la part de vos fournisseurs ». Le
simulateur affichait là une carte verte « a priori non applicable ». Elle passe à « à vérifier » et
dit la moitié qu'on oublie.

VÉRIFIÉ le 2026-09-19 sur https://nis2compliant.org/fr/texte-integral-de-la-directive-nis2/
(article 2, § 2) — certaines entités relèvent de NIS2 quelle que soit leur taille : prestataires de
services de confiance qualifiés, registres de noms de domaine de premier niveau, fournisseurs de
services DNS, fournisseurs de réseaux et services de communications électroniques publics. La
question 3 le dit désormais, puisque la question 2 présente le seuil de 50 comme un filtre.

VÉRIFIÉ — les cinq contrôles bloquants passent, exécutés localement depuis `scripts/`, chacun rendant 0 :
`scripts/audit_code_sur.py`, `scripts/audit_cloisonnement.py` avec --bloquant,
`scripts/generer_registre_erreurs.py` avec --verifier, `scripts/verifier_rapports.py`,
`scripts/verifier_coherence_juridique.py`

VÉRIFIÉ — dix-huit entrées après réécriture, comptées dans `products/caelum/site/simulateur.html`
par grep -c sur la balise d'élément de liste.

VÉRIFIÉ — rendu et logique éprouvés dans Chromium sur trois profils, sur `products/caelum/site/simulateur.html`,
et pas seulement lus. Le script de test est volontairement hors du dépôt, dans le répertoire de
travail temporaire de la session. Résultats : plombier de 8 personnes → 2 « s'applique », 1 « non
concerné », 2 « à vérifier » ; commerce B2C → l'e-facturation passe de vert à ambre ; les réponses
de Chaima, deux « je ne sais pas » → 4 « à vérifier ».

## NON VÉRIFIÉ

- La comparaison des annexes belges est **faite au niveau des secteurs** depuis l'addendum du
  2026-09-19 17h05, et elle est concordante. Ce qui reste non fait : le diff **mot pour mot de la
  colonne « type d'entité »** des tableaux annexés au Moniteur, que je n'ai pas pu ouvrir
  directement. La page dit donc ce qui est établi, et rien de plus.
- Le décompte des **intérimaires** pour le seuil de 50 travailleurs de la loi du 28 novembre 2022 : la
  loi ne renvoie qu'au § 1er de l'article 7 de la loi du 4 décembre 2007.
- La **règle de comptage** annoncée par la question 2 (« sous contrat de travail, temps partiel
  compris ») ne correspond exactement ni au seuil des lanceurs d'alerte, qui se calcule en moyenne
  selon les règles des élections sociales, ni au critère de taille NIS2, qui se compte en unités de
  travail par année. Le défaut est identifié, la correction n'est pas faite : elle demande un arbitrage
  entre exactitude et lisibilité que je ne veux pas rendre seul.

## Ce qui reste, et ce qui dépend de Chaima

Rien n'est publié. La branche attend son feu vert pour la PR — c'est une page publique, donc le
parcours 3 du CODEX s'applique et la relecture humaine est obligatoire.

Inchangé et toujours à elle : les prix des trois offres, le numéro BCE et l'éditeur responsable, la
déclaration ONEM qui débloque Stripe, le compte Brevo, l'épinglage par SHA, et la cinquième question
du simulateur — la seule qui rendrait tranchante la carte « lanceurs d'alerte » pour une PME de moins
de 50 travailleurs.

Signalé sans être traité, parce que ce n'est pas mon mandat : le seul contact du site est une adresse
Gmail sur un domaine `.agency` payant. Pour un dirigeant méfiant, c'est un signal plus fort que
n'importe quelle maladresse de formulation.

---

# Addendum — 2026-09-19, 17h10 : la comparaison des annexes belges

Demandée par Chaima. Elle portait sur le premier des trois points laissés NON VÉRIFIÉS ce matin.
Addendum daté, pas réécriture : le corps du rapport reste tel qu'il a été déposé.

**Correction d'un fait du synopsis, périmé depuis :** le synopsis dit « aucune PR n'est ouverte ».
C'était vrai à 16h08. La PR https://github.com/chaima0007/keywordmoneymaker/pull/26 a été ouverte
depuis, **en brouillon**, sur demande de Chaima. Rien n'est déployé pour autant : le déploiement ne
se déclenche que sur `main`.

## Résultat de la comparaison

Les annexes de la loi belge du 26 avril 2024 portent **les mêmes 11 + 7 secteurs** que celles de la
directive (UE) 2022/2555. Aucun secteur ajouté, aucun retiré. La liste affichée sur la page vaut donc
pour un lecteur belge — ce que je ne pouvais pas affirmer ce matin.

VÉRIFIÉ le 2026-09-19 sur https://www.ejustice.just.fgov.be/eli/wet/2024/04/26/2024202344/justel
(Justel, texte néerlandais authentique, mis à jour au 19-01-2026) — l'article 3, § 1er, vise les
entités « van een in bijlage I of II bedoelde soort » et renvoie au critère de taille de la
recommandation 2003/361/CE, comme la directive.

VÉRIFIÉ le 2026-09-19 sur https://atwork.safeonweb.be/sites/default/files/2024-10/NIS2%20Brochure%20FR.pdf
(brochure du CCB, autorité nationale de cybersécurité) — l'énumération des annexes I et II de la
**loi belge** reprend les onze secteurs hautement critiques et les sept autres secteurs critiques,
dans le même ordre et sous les mêmes intitulés que la directive.

VÉRIFIÉ le 2026-09-19 sur https://atwork.safeonweb.be/fr/media/780/download?inline= (FAQ NIS2 du
CCB) — l'article 3, § 6, permet au Roi d'ajouter des secteurs par arrêté délibéré en Conseil des
ministres. Le CCB en parle au **conditionnel** : « Le Roi pourrait ajouter des secteurs ou
sous-secteurs aux annexes I et II ». Aucun arrêté d'extension pris à ce jour. La page le dit.

## Ce que la comparaison a trouvé en plus — et que personne n'avait vu

VÉRIFIÉ le 2026-09-19 sur https://atwork.safeonweb.be/fr/media/780/download?inline= (FAQ NIS2 du
CCB) — « le champ d'application de la loi NIS2 porte sur l'ensemble de l'entité concernée et non
uniquement sur ses activités reprises dans les annexes de la loi. Sauf si la définition du type
d'entité (service) repris dans les annexes prend en considération le caractère accessoire ou
non-essentiel de l'activité concernée, une entité tombe dans le champ d'application de la loi même
si le service concerné qu'elle fournit n'est qu'une partie accessoire ou non-essentielle de toutes
ses activités. »

C'est le défaut que ni l'avocat du client ni le gardien juridique n'avaient relevé, et il est plus
conséquent que les trois lignes corrigées ce matin : un dirigeant qui exerce une activité listée à
titre secondaire répondait « non » en toute bonne foi, et le simulateur le confortait en vert. La
question 3 porte désormais ce piège en toutes lettres, avec sa source.

VÉRIFIÉ le 2026-09-19 sur https://refli.be/fr/lex/2024202344 (texte français de la loi) — l'article
11 permet à l'autorité nationale de cybersécurité d'identifier une entité **quelle que soit sa
taille**, notamment lorsqu'elle est la seule en Belgique à fournir un service essentiel. Le droit
belge élargit donc les entrées sans seuil au-delà de l'article 2, § 2, de la directive. Porté sur la
page.

VÉRIFIÉ le 2026-09-19 sur https://refli.be/fr/lex/2024202344 — l'article 3, § 4, fait entrer dans le
champ, quelle que soit leur taille, les entités identifiées comme critiques au sens de la loi du
19 décembre 2025 relative à la résilience des entités critiques. **Non** porté sur la page : c'est
une désignation individuelle, qu'une entreprise connaît si elle la reçoit.

## Contrôle honnête

VÉRIFIÉ — les cinq contrôles bloquants passent après modification depuis `scripts/`, chacun rendant 0 : `scripts/audit_code_sur.py`, `scripts/audit_cloisonnement.py`,
`scripts/generer_registre_erreurs.py`, `scripts/verifier_rapports.py`,
`scripts/verifier_coherence_juridique.py`

VÉRIFIÉ — dans `products/caelum/site/simulateur.html`, les trois profils de test rendent les mêmes
verdicts qu'avant cette modification : le texte d'aide a changé, le moteur n'a pas bougé.

Ce que cet addendum ne lève pas : le diff mot pour mot de la colonne « type d'entité » des tableaux
annexés au Moniteur, et les deux autres points NON VÉRIFIÉS du rapport.


---

# Addendum — 2026-09-20 : la question 2, tranchée

TRANCHÉ PAR CHAIMA le 2026-09-20. Le troisième point NON VÉRIFIÉ du rapport n'était pas une
vérification manquante mais un arbitrage en attente : la question 2 annonce une règle de comptage
plus simple que la loi.

**Décision : formulation simple conservée, avec une réserve pour le cas limite.** L'aide de la
question 2 ajoute : « Si vous êtes proche de 50, le calcul légal est plus fin (moyenne annuelle,
temps partiels comptés autrement) : votre comptable tranchera. »

**Le fait qui a emporté la décision.** Sous 40 travailleurs ou au-dessus de 60, toutes les règles de
calcul — moyenne des élections sociales, équivalents temps plein de la recommandation 2003/361/CE —
donnent la même réponse. L'écart ne se manifeste qu'autour du seuil. Écrire les deux règles en
entier aurait alourdi la page pour tous les visiteurs afin de servir la minorité qui, de toute
façon, doit faire vérifier son décompte.

Ce que cela ne règle pas, et qui est dit sur la page : le simulateur ne calcule pas l'effectif légal
et ne prétend pas le faire.

VÉRIFIÉ — les cinq contrôles bloquants passent après modification depuis `scripts/`, chacun rendant 0.

VÉRIFIÉ — dans `products/caelum/site/simulateur.html`, les trois profils de test rendent les mêmes
verdicts qu'avant : seule l'aide a changé, le moteur n'a pas bougé.

Restent NON VÉRIFIÉS, inchangés : le décompte des intérimaires pour le seuil de 50 (la loi du
28/11/2022 ne renvoie qu'au § 1er de l'article 7 de la loi du 04/12/2007), et le diff mot pour mot
de la colonne « type d'entité » des tableaux annexés au Moniteur.
