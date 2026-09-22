# Domaine : droit de la conformité — Belgique

> **Maturité : CONFIRMÉ** (12 fiches, un seul projet à ce jour — Caelum Partners).
> Le seuil de 10 fiches est franchi, mais EXPERT exige **aussi** un deuxième projet (CODEX §4) :
> le domaine reste donc CONFIRMÉ. Une maturité qu'on s'accorde à soi-même ne vaut rien.
> Dernière passe : 2026-09-22.

Ce fichier est **transverse** : ce que Caelum apprend du droit belge, tout projet de l'Empire le sait.
On consigne le **principe** et la **source primaire**, jamais un avis. Chaque fiche porte sa date de
dernière confirmation ; une fiche non reconfirmée depuis plus de six mois doit être relue avant d'être
citée.

**Règle de lecture.** Une fiche dit ce qui est établi. Là où le texte est ambigu, elle le dit et
n'arbitre pas — un droit incertain présenté comme certain est plus dangereux qu'une lacune avouée.

---

## E-BE-01 — E-facturation : le numéro de TVA ne suffit pas à déterminer qui est concerné

**Domaine** : TVA / facturation électronique structurée (B2B, Peppol).

**Principe appris.** L'obligation vise les assujettis **établis en Belgique**, pour leurs factures à
d'autres assujettis établis en Belgique. Deux erreurs symétriques sont courantes :
- croire que le **régime de la franchise** (chiffre d'affaires sous 25 000 €) dispense — il ne
  dispense pas ;
- croire qu'un numéro de TVA belge suffit à rendre concerné — quatre situations en dispensent :
  réaliser **uniquement** des opérations exemptées par l'article 44 du Code TVA (soins de santé,
  enseignement, certains services financiers), relever du **régime forfaitaire** (article 56, en
  extinction au plus tard le 01/01/2028), être **en faillite**, ou être **identifié à la TVA en
  Belgique sans y être établi** (pas d'établissement stable).

**Pourquoi ça compte.** Un kinésithérapeute ou un dentiste a un numéro BE 0… et facture des
professionnels : un outil qui raisonne sur le seul numéro de TVA lui annonce une obligation qu'il n'a
pas. C'est le type d'erreur qu'un comptable détecte en une phrase, et qui coûte la crédibilité.

**Sources liées.** SPF Finances, efacture.belgium.be, « Pour qui la facturation électronique
deviendra-t-elle obligatoire ? » — https://efacture.belgium.be/fr/article/pour-qui-la-facturation-electronique-deviendra-t-elle-obligatoire
Base légale : article 53, § 2bis, du Code TVA, inséré par la loi du 6 février 2024 (M.B. 20/02/2024).

**Projets où appliqué** : Caelum Partners (simulateur, question 1 et carte de résultat).
**Fiabilité** : ÉLEVÉE. **Dernière confirmation** : 2026-09-19.

---

## E-BE-02 — E-facturation : facturer des particuliers dispense d'émettre, pas de recevoir

**Principe appris.** Les factures sortantes adressées à des particuliers échappent à l'obligation.
Mais une entreprise qui a un numéro de TVA belge doit **être en mesure de recevoir** les factures
électroniques structurées de ses fournisseurs. C'est la moitié qu'on oublie, et c'est celle qui
piège le commerce de détail, l'horeca et les métiers à clientèle privée.

**Corollaire opérationnel.** Être inscrit au réseau Peppol ne suffit pas : une entreprise qui reçoit
ses factures en PDF et les ressaisit à la main n'est pas conforme, puisque l'obligation porte sur la
**réception d'une facture structurée**, pas sur l'inscription.

**Sources liées.** Même page du SPF Finances que la fiche E-BE-01 : « vous devez être en mesure de
recevoir des factures électroniques structurées de la part de vos fournisseurs ».

**Projets où appliqué** : Caelum Partners (carte de résultat « e-facturation », branche « je ne
facture que des particuliers », passée de verte à ambre pour cette raison).
**Fiabilité** : ÉLEVÉE. **Dernière confirmation** : 2026-09-19.

---

## E-BE-03 — E-facturation, sanctions : ce qui est puni n'est pas ce que la presse spécialisée répète

**Principe appris — c'est la fiche la plus utile du fichier.** L'arrêté royal du 8 juillet 2025
(NUMAC 2025005169, en vigueur le 01/01/2026) insère un point C dans la rubrique I de la section 2 de
l'annexe à l'arrêté royal n° 44 du 9 juillet 2012. Son libellé exact :

> « **C. Non-disposition des moyens techniques permettant d'émettre et de recevoir une facture
> électronique structurée** — 1ère infraction : 1.500 EUR ; 2ème infraction : 3.000 EUR ; infractions
> suivantes : 5.000 EUR »

Deux conséquences que beaucoup de publications commerciales inversent :

1. **L'infraction sanctionnée est l'absence de moyens techniques, pas la facture non conforme.**
   L'affirmation « 1 500 € par facture », et les calculs du type « 200 factures = 300 000 € par
   mois » qui en découlent, ne correspondent pas au texte de l'arrêté. Ce sont des chiffres de peur.
2. **Le délai de trois mois joue en sens inverse de ce qu'on lit souvent.** Le texte dit : « une
   infraction ne peut être considérée comme une deuxième infraction ou une infraction suivante
   qu'après la constatation de cette infraction par l'administration, **au plus tôt trois mois
   après** que l'infraction précédente ayant donné lieu à une amende administrative ait été
   constatée ». Ce n'est pas « 3 000 € si vous récidivez dans les trois mois » : c'est un **délai de
   carence protecteur** avant que l'échelon supérieur puisse s'appliquer.

**Base légale de l'échelle** : article 70, § 4, alinéa 1er, du Code TVA — amende fiscale non
proportionnelle de 50 à 5 000 EUR par infraction, l'échelle étant fixée par le Roi.

**Sources liées.** Texte de l'arrêté royal du 08/07/2025 sur Justel —
https://www.ejustice.just.fgov.be/eli/arrete/2025/07/08/2025005169/justel

**Ce que ça vaut commercialement.** Un acteur de la conformité qui corrige une peur répandue en
citant le texte se distingue de ceux qui la propagent. À manier avec la retenue du §13 : nous
n'affirmons pas que les amendes sont anodines, nous disons ce que l'arrêté punit.

**Projets où appliqué** : aucun encore — candidat naturel pour un contenu public de Caelum.
**Fiabilité** : ÉLEVÉE (texte primaire lu). **Dernière confirmation** : 2026-09-21.

---

## E-BE-04 — NIS2 : c'est la colonne « type d'entité » qui décide, jamais le nom du secteur

**Principe appris.** Les annexes I (11 secteurs) et II (7 secteurs) de la directive (UE) 2022/2555
comportent trois colonnes : secteur, sous-secteur, **type d'entité**. Seule la troisième a une portée
juridique. Lire le nom du secteur conduit à des erreurs dans les deux sens :
- **sur-inclusion** : « Transports — routier » ne vise pas le transport routier de marchandises, mais
  les **autorités routières** chargées du contrôle de la gestion du trafic et les **exploitants de
  systèmes de transport intelligents** ; « Denrées alimentaires » ne vise que la production et la
  transformation **industrielles** et la **distribution en gros**, le commerce de détail en étant
  exclu ;
- **sous-inclusion** : « Infrastructure numérique » comprend aussi les **points d'échange internet**,
  les **registres de noms de domaine de premier niveau** et les **réseaux de diffusion de contenu**,
  qu'une énumération de mémoire oublie — et cette omission-là rassure à tort.

**Sources liées.** Annexes I et II reproduites intégralement —
https://www.nis2-info.eu/regulation/nis2/annex/0 et https://www.nis2-info.eu/regulation/nis2/annex/1

**Projets où appliqué** : Caelum Partners (question 3 du simulateur). Cette fiche est née d'une erreur
réelle : fiche **E-29** de `.claude/BASE-ERREURS.md`.
**Fiabilité** : ÉLEVÉE. **Dernière confirmation** : 2026-09-19.

---

## E-BE-05 — NIS2 : une activité accessoire fait entrer l'entité entière dans le champ

**Principe appris.** Le champ d'application porte sur **l'ensemble de l'entité**, pas seulement sur
ses activités listées. Sauf là où la définition du type d'entité retient elle-même le caractère
principal ou accessoire de l'activité — « gestion des déchets à titre d'activité principale »,
« autorités routières pour lesquelles la gestion du trafic n'est pas une part non essentielle » —
exercer une activité listée **même à titre secondaire** suffit.

**Pourquoi c'est le piège le plus coûteux.** Un dirigeant raisonne en métier principal. Il répond
« non » en toute bonne foi, et un outil mal conçu le conforte. C'est le défaut que ni l'avocat du
client ni le gardien juridique n'avaient vu : il n'est dans aucune liste, il est dans la manière de
la lire.

**Sources liées, dans les deux langues qui font foi.**
FR — FAQ NIS2 du CCB : « une entité tombe dans le champ d'application de la loi même si le service
concerné qu'elle fournit n'est qu'une partie accessoire ou non-essentielle de toutes ses activités »
— https://atwork.safeonweb.be/fr/media/780/download?inline=
NL — même FAQ : « valt een entiteit binnen het toepassingsgebied van de wet, zelfs als de betrokken
dienst die zij verleent alleen een bijkomstig of niet-essentieel onderdeel is van al haar
activiteiten » — https://ccb.belgium.be/nl/open-media/780/download?inline=

**Projets où appliqué** : Caelum Partners (question 3, paragraphe « le piège à connaître »).
**Fiabilité** : ÉLEVÉE. **Dernière confirmation** : 2026-09-21.

---

## E-BE-06 — NIS2 : le seuil de taille n'est pas un filtre étanche

**Principe appris.** Le critère de taille (moyenne entreprise au sens de la recommandation
2003/361/CE : au moins 50 personnes, ou plus de 10 millions d'euros de chiffre d'affaires ou de total
de bilan) connaît des entrées **sans seuil**, de trois origines différentes :
- **directive, article 2, § 2** : prestataires de services de confiance qualifiés, registres de noms
  de domaine de premier niveau, fournisseurs de services DNS, fournisseurs de réseaux et services de
  communications électroniques publics ;
- **loi belge du 26 avril 2024, article 3, § 4** : les entités identifiées comme critiques au sens de
  la loi du 19 décembre 2025 relative à la résilience des entités critiques ;
- **loi belge, article 11** : le CCB peut identifier une entité **quelle que soit sa taille**,
  notamment si elle est le seul prestataire en Belgique d'un service essentiel, ou si elle est
  critique par son importance nationale ou régionale.

Le droit belge élargit donc les entrées sans seuil au-delà de la directive. Et l'article 3, § 6,
autorise le Roi à **ajouter** des secteurs aux annexes par arrêté délibéré en Conseil des ministres —
faculté non exercée à ce jour, le CCB en parlant encore au conditionnel.

**Sources liées.** Texte français de la loi — https://refli.be/fr/lex/2024202344 · Texte néerlandais
authentique sur Justel — https://www.ejustice.just.fgov.be/eli/wet/2024/04/26/2024202344/justel ·
Article 2, § 2, de la directive — https://nis2compliant.org/fr/texte-integral-de-la-directive-nis2/

**Projets où appliqué** : Caelum Partners (question 3, mention des activités visées quelle que soit
la taille).
**Fiabilité** : ÉLEVÉE pour la directive et les articles 3 et 11 ; MODÉRÉE pour le fait qu'aucun
arrêté d'extension n'ait été pris (absence prouvée par une formulation au conditionnel du CCB, pas
par une recherche exhaustive au Moniteur). **Dernière confirmation** : 2026-09-21.

---

## E-BE-07 — NIS2, sanctions : le montant le plus élevé, jamais l'un ou l'autre

**Principe appris.** Entités **essentielles** : 10 000 000 EUR **ou** 2 % du chiffre d'affaires annuel
mondial total de l'exercice précédent — **le montant le plus élevé étant retenu**. Entités
**importantes** : 7 000 000 EUR **ou** 1,4 %, même règle.

L'erreur à ne jamais commettre est d'écrire « ou » sans la règle du plus élevé : elle transforme un
plafond en plancher pour les grandes entreprises, et inversement pour les petites. La même vigilance
vaut pour le RGPD (20 millions / 4 %).

**Sources liées.** CCB, « La directive NIS2 : que cela signifie-t-il pour mon organisation ? » —
https://ccb.belgium.be/nl/node/521 (l'autorité nationale, reprenant les montants de l'article 34 de
la directive). Les sanctions belges figurent au titre 4, chapitre 2, de la loi du 26 avril 2024.

**Où se trouve le barème — tranché le 2026-09-22 par la table des matières de Justel.** Le titre 4,
chapitre 2, de la loi se divise en deux sections : **articles 51 à 57, « Procédure »** ; **articles 58
à 61, « Mesures administratives et amendes »**. Le barème est donc dans les articles **58 à 61**. Le
site qui titre « Article 56 — Amendes administratives » se trompe : l'article 56 appartient à la
section Procédure — ce qui cadre d'ailleurs avec le fait qu'on lui prête ailleurs le recouvrement par
contrainte et l'opposition devant le juge des saisies.

**Méthode à retenir**, transférable : quand un document est trop long pour être lu en entier, sa
**table des matières** suffit souvent à départager deux commentateurs. Elle est en tête, donc
atteignable, et elle donne les bornes d'articles par section.

**Encore PLAUSIBLE, confiance MODÉRÉE** : l'attribution fine à l'intérieur de 58-61 (article 58 pour
l'outillage de mesures, 59 pour le barème, 60 pour l'escalade réservée aux entités essentielles). Un
seul commentateur la propose, mais elle est cohérente avec l'intitulé de la section.

**Sources liées.** Table des matières de la loi, texte néerlandais authentique —
https://www.ejustice.just.fgov.be/eli/wet/2024/04/26/2024202344/justel : « HOOFDSTUK 2. - De
administratieve maatregelen en geldboetes — Afdeling 1. Procedure Art. 51-57 — Afdeling 2.
Administratieve maatregelen en geldboetes Art. 58-61 ».

**Projets où appliqué** : Caelum Partners (cartes de sanction de la page d'accueil, contrôlées par
`scripts/verifier_coherence_juridique.py`, qui exige deux occurrences de la règle du plus élevé).
**Fiabilité** : ÉLEVÉE pour les montants et pour la section ; MODÉRÉE pour l'article exact.
**Dernière confirmation** : 2026-09-22.

---

## E-BE-08 — Lanceurs d'alerte : le seuil de 50 n'est pas un effectif, et il connaît deux exceptions sans seuil

**Principe appris, en trois temps.**

1. **Deux branches sans aucun seuil d'effectif.** L'obligation de canal interne s'applique quel que
   soit l'effectif aux entités juridiques relevant des dispositions en matière de services, produits
   et marchés financiers, **et** à celles soumises à la législation anti-blanchiment — ce qui englobe
   beaucoup de petites structures qui l'ignorent : fiduciaires, comptables, notaires, agents
   immobiliers.
2. **Le seuil est une moyenne, pas une photographie.** Article 11, § 2, de la loi du 28 novembre
   2022 : le seuil « est calculé au regard de la moyenne des travailleurs occupés dans l'entité
   juridique […] telle que calculée sur la base de l'**article 7, § 1er**, de la loi du 4 décembre
   2007 relative aux élections sociales ».
3. **Vérification annuelle depuis 2025.** Le calcul se refait chaque **1er janvier**, sur les quatre
   trimestres de l'année civile précédente (article 199 de la loi du 9 février 2024, M.B.
   21/03/2024).

**L'ambiguïté, et elle n'est pas levée.** L'article 7 de la loi du 4 décembre 2007 a quatre
paragraphes : § 1er le calcul de base (diviser par 365 le total des jours civils) ; § 2 la règle des
trois quarts (un temps partiel sous les trois quarts compte pour moitié) ; § 3 le transfert
d'entreprise ; § 4 les **intérimaires**, comptés chez l'utilisateur en divisant par 92 les jours d'un
seul trimestre de référence, à l'exclusion de ceux qui remplacent un permanent dont le contrat est
suspendu. La loi lanceurs d'alerte ne renvoie **qu'au § 1er**. Lu à la lettre, ni les intérimaires ni
la règle des trois quarts ne s'appliquent ; lu comme le font les secrétariats sociaux, c'est toute la
méthode qui s'applique ; un cabinet retient une troisième lecture et écrit lui-même « a priori ».

**Statut §13 : NON TRANCHÉ**, confiance FAIBLE dans chacune des trois lectures. Ce n'est pas un manque
de recherche, c'est une ambiguïté du texte. **Conséquence pratique** : ne jamais énoncer la règle de
comptage avec plus de précision que « une moyenne sur l'année civile précédente, selon les règles des
élections sociales » — et renvoyer au comptable pour une entreprise proche de 50.

**Sources liées.** Loi du 28/11/2022, article 11, § 2 —
https://etaamb.openjustice.be/fr/loi-du-28-novembre-2022_n2022042980 · Article 7 de la loi du
04/12/2007 sur Justel — https://www.ejustice.just.fgov.be/eli/loi/2007/12/04/2007012768/justel ·
Version coordonnée officieuse du SPF Emploi —
https://emploi.belgique.be/sites/default/files/content/documents/Concertation%20sociale/R%C3%A9glementation/Loi%20du%204%20d%C3%A9cembre%202007%20relative%20aux%20%C3%A9lections%20sociales%20%28version%20coordonn%C3%A9e%20officieuse%29.pdf ·
Période de référence annuelle —
https://www.securex.be/fr/lex4you/employeur/actualites/nouvelle-periode-de-reference-pour-le-calcul-du-seuil-pour-les-lanceurs-d-alerte

**Projets où appliqué** : Caelum Partners (carte « canal lanceurs d'alerte », maintenue en « à
vérifier » sous 50 travailleurs précisément à cause du point 1 ; question 2 et sa réserve).
**Fiabilité** : ÉLEVÉE pour les points 1 à 3, NON TRANCHÉ pour le décompte des intérimaires.
**Dernière confirmation** : 2026-09-21.

---

## E-BE-09 — CSRD : une directive européenne adoptée n'est pas un droit applicable

**Principe appris.** Le paquet Omnibus du 24/02/2026 (directive (UE) 2026/470) relève fortement les
seuils CSRD : il faudra dépasser **à la fois** 1 000 salariés **et** 450 millions d'euros de chiffre
d'affaires net. Deux pièges distincts :
- **le « et » cumulatif**, qu'une lecture rapide transforme en « ou » — ce qui ferait entrer dans le
  champ des entreprises qui n'y sont pas ;
- **la transposition**, qui n'est pas faite en droit belge. Jusque-là, ce sont les seuils nettement
  plus bas de la loi du 2 décembre 2024 qui s'appliquent. Écrire « désormais », « déjà » ou « est
  transposée » est faux tant que le Moniteur n'a rien publié.

**Principe transférable, et c'est le vrai apport de la fiche.** Une directive adoptée à Bruxelles ne
crée aucune obligation directe pour une PME belge tant qu'elle n'est pas transposée. Le réflexe
« c'est voté, donc ça s'applique » est la source d'erreur la plus fréquente dans la communication de
conformité — dans les deux sens, puisqu'il peut aussi rassurer à tort quand les nouveaux seuils sont
plus favorables que les anciens.

**Sources liées.** Le contrôle `scripts/verifier_coherence_juridique.py` du dépôt Caelum interdit
mécaniquement les formulations « 1 000 salariés OU », « désormais transposée en droit belge »,
« déjà transposée », « a été transposée » — motifs volontairement amputés de leur verbe, parce qu'un
interdit qui dépend d'une forme verbale se contourne sans le vouloir.

**Projets où appliqué** : Caelum Partners (carte « CSRD et DORA », page d'accueil, simulateur).
**Fiabilité** : ÉLEVÉE. **Dernière confirmation** : 2026-09-19.

---

## E-BE-10 — Méthode : comment vérifier une affirmation de droit belge

**Principe appris**, distillé de six erreurs réelles commises sur ce domaine.

1. **Les deux langues font foi.** Le texte néerlandais n'est pas une traduction : il a la même valeur
   que le français. Une nuance tombée d'une version se retrouve souvent dans l'autre — c'est ainsi
   qu'a été trouvée la règle de calcul par moyenne du seuil des 50, absente de l'extrait français
   consulté. Instruction de Chaima du 2026-09-18 : les sources néerlandaises et anglaises aident, il
   faut s'en servir.
2. **Hiérarchie des sources**, dans cet ordre et sans sauter d'échelon : le texte sur Justel ou au
   Moniteur → l'**autorité compétente** (CCB pour NIS2, SPF Finances pour la TVA, APD pour le RGPD) →
   un ordre professionnel ou un secrétariat social → un cabinet d'avocats → tout le reste. Un
   commentaire qui écrit « a priori » signale honnêtement qu'il n'a pas tranché : le reprendre sans
   ce mot est une falsification.
3. **Un renvoi à un paragraphe précis se lit à la lettre.** « L'article 7, § 1er » n'est pas
   « l'article 7 ». Vérifier ce que contiennent les autres paragraphes avant de conclure : c'est là
   que se cache l'ambiguïté de la fiche E-BE-08.
4. **Une liste annoncée « complète » se recopie depuis la source pendant qu'on l'écrit**, jamais de
   mémoire avec relecture après coup (fiche E-29 de la base d'erreurs).
5. **Les chiffres circulent plus vite que les textes.** « 1 500 € par facture » (fiche E-BE-03) est
   repris par des sites sérieux et ne correspond pas à l'arrêté. Devant un chiffre frappant, remonter
   à l'arrêté ou à la loi avant de le relayer — surtout s'il fait peur, car la peur circule mieux.
6. **Un document long ne se lit pas par le début.** Les annexes sont à la fin, et les outils tronquent
   depuis le début : chercher une formule distinctive de l'annexe plutôt que d'essayer de lire tout
   le texte.

**Projets où appliqué** : Caelum Partners. **Fiabilité** : ÉLEVÉE — chaque point vient d'une erreur
datée, pas d'un principe général. **Dernière confirmation** : 2026-09-21.

---

## E-BE-11 — Lanceurs d'alerte : les deux délais que tout canal interne doit tenir

**Principe appris.** Un canal de signalement interne n'est pas une boîte mail. L'article 12, § 1er, de
la loi du 28 novembre 2022 énumère ce qu'il doit comporter, et deux délais y sont chiffrés :

- **7 jours** pour l'accusé de réception adressé à l'auteur du signalement (art. 12, § 1er, 2°) ;
- **3 mois maximum** pour le retour d'informations, comptés depuis l'accusé de réception — ou, si
  aucun accusé n'a été envoyé, depuis l'expiration du délai de sept jours (art. 12, § 1er, 5°).

Le reste de l'article est tout aussi contraignant et se vend mal en une ligne : des canaux **sécurisés
garantissant la confidentialité** de l'auteur et des tiers cités, empêchant l'accès du personnel non
autorisé ; la possibilité de signaler **par écrit ou oralement**, par téléphone ou messagerie vocale,
et **en personne sur demande** dans un délai raisonnable ; la désignation d'un **gestionnaire de
signalement** nommé ; un **suivi diligent, y compris des signalements anonymes** ; et la mise à
disposition d'informations sur les canaux **externes** (coordinateur fédéral, autorités compétentes).

**Deux points pratiques pour une PME.** Les entités de 50 à 249 travailleurs peuvent **mutualiser**
les ressources de réception et d'investigation — utile pour une petite structure. Et l'échéance de
mise en conformité est passée depuis longtemps : 250 travailleurs et plus dès l'entrée en vigueur en
décembre 2022, 50 à 249 au plus tard le **17 décembre 2023**.

**Le défaut subtil du délai de retour.** Ne pas accuser réception ne repousse pas l'échéance : le
délai de trois mois court alors depuis l'expiration des sept jours. Le silence ne fait pas gagner de
temps, il en fait perdre.

**Sources liées.** Texte de l'article 12 —
https://etaamb.openjustice.be/fr/loi-du-28-novembre-2022_n2022042980.html · Guide de l'Institut
fédéral pour la protection et la promotion des droits humains —
https://institutfederaldroitshumains.be/sites/default/files/2024-12/Guide%20lanceurs%20d%27alerte.pdf

**NON VÉRIFIÉ** : la **nature exacte des sanctions** encourues par l'employeur qui n'instaure pas de
canal, entrave un signalement ou exerce des représailles. Les commentaires parlent de « sanctions
pénales et administratives » sans citer d'article ; le Code pénal social prévoit quatre niveaux, dont
le niveau 4 (emprisonnement de 6 mois à 3 ans et/ou amende pénale de 600 à 7 000 EUR), mais **rien
dans ce que j'ai lu ne rattache la loi lanceurs d'alerte à un niveau précis**. Ne pas citer de montant
tant que l'article n'est pas lu.

**Projets où appliqué** : aucun encore — matière première pour la carte « canal lanceurs d'alerte » et
pour une offre d'accompagnement.
**Fiabilité** : ÉLEVÉE pour les délais et le contenu de l'article 12 ; NON VÉRIFIÉ pour les sanctions.
**Dernière confirmation** : 2026-09-22.

---

## E-BE-12 — Un chiffre qui circule sans son texte est un chiffre en sursis

**Principe appris**, tiré de trois cas rencontrés le même mois et qui se ressemblent trop pour être
des accidents.

1. **« 1 500 € par facture »** (e-facturation). L'arrêté punit la non-disposition des moyens
   techniques ; le « par facture » n'y est pas. Des calculs à six chiffres en ont été tirés.
2. **« 3 000 € si vous récidivez dans les trois mois »** (même arrêté). Le texte dit l'inverse : trois
   mois est un délai **minimum** avant que l'échelon supérieur puisse s'appliquer.
3. **« Article 56 — Amendes administratives »** (NIS2 belge). La table des matières de la loi place
   l'article 56 dans la section « Procédure » ; le barème est aux articles 58 à 61.

**Ce que les trois ont en commun** : le chiffre est exact, c'est son **rattachement** qui est faux —
à quoi il s'applique, à partir de quand, dans quel article. Un chiffre juste mal rattaché est plus
trompeur qu'un chiffre faux, parce qu'il résiste à la vérification paresseuse : on retrouve bien
« 1 500 € » dans l'arrêté, donc on cesse de chercher.

**Contre-mesure.** Pour tout chiffre repris d'un tiers, vérifier trois choses avant de l'écrire :
**à quoi** il se rattache (l'infraction exacte), **quand** il s'applique (le déclencheur, le délai),
et **où** il se trouve (l'article). Si l'une des trois manque, écrire le chiffre avec sa réserve, ou
ne pas l'écrire.

**Pourquoi c'est un actif commercial.** Ces trois erreurs circulent chez des éditeurs de logiciels et
des consultants qui les reprennent les uns aux autres. Un acteur de la conformité qui cite le texte
là où les autres citent un confrère se distingue sans rien dénigrer.

**Projets où appliqué** : Caelum Partners. **Fiabilité** : ÉLEVÉE — chaque cas est daté et sourcé
dans les fiches E-BE-03 et E-BE-07. **Dernière confirmation** : 2026-09-22.

---

## Ce qui reste ouvert dans ce domaine

| Question | Pourquoi elle n'est pas tranchée | Prochain pas |
|---|---|---|
| Décompte des intérimaires pour le seuil de 50 (lanceurs d'alerte) | Ambiguïté du renvoi au seul § 1er de l'article 7 | Une circulaire ou une décision de justice ; sinon, rester au niveau de précision de la fiche E-BE-08 |
| ~~Numéro d'article du barème de sanctions NIS2~~ | **Fermé le 2026-09-22** : section « Mesures administratives et amendes » = articles 58 à 61 (table des matières de Justel) | Reste à confirmer l'article exact dans cette fourchette |
| Sanctions encourues par l'employeur — loi lanceurs d'alerte | Aucun commentaire consulté ne cite l'article ; le rattachement à un niveau du Code pénal social n'est pas établi | Lire les articles de sanction de la loi du 28/11/2022 |
| Colonne « type d'entité » des annexes de la loi belge NIS2, lue ligne à ligne | Les tableaux sont à la fin du Moniteur ; les outils tronquent depuis le début | Chercher les formules distinctives une par une, ou obtenir le PDF paginé |
| ~~Délais de la loi lanceurs d'alerte~~ | **Fermé le 2026-09-22** : 7 jours pour l'accusé de réception, 3 mois pour le retour (fiche E-BE-11) | — |
| RGPD : durées de conservation et DPA sous-traitants, pour un usage opérationnel | Hors du périmètre des passes faites jusqu'ici | À ouvrir si un contenu ou une offre le demande |
