# Sources légales du site — contrôle quotidien

**Phrase de contrôle honnête.** Premier contrôle de sources depuis l'instauration de la règle
quotidienne par Chaima ce jour : aucun document antérieur comparable, donc aucun quasi-doublon
possible. Les quatre affirmations datées du site ont été recoupées une par une auprès de leur
source primaire, pas auprès d'un article de cabinet. Une imprécision réelle a été trouvée et
corrigée en PR séparée, sans attendre une demande de Chaima.

- **Projet** : Caelum Partners
- **Catégorie** : Vérification
- **Rédigé par** : session Claude Code `session_01BLc73LKqGJyvJaoqFP9hT4`
- **Destinataire** : Chaima

---

## Méthode

Extraction automatique de **toute** affirmation datée ou chiffrée des pages publiées
(`grep` sur dates, montants, seuils), puis recoupement de chacune auprès d'une source primaire.
Les blogs de cabinets et d'éditeurs de logiciels ont servi à *trouver* les textes, jamais à
*établir* un fait.

## 1. NIS2 — **VÉRIFIÉ** sur `ccb.belgium.be` : les trois dates du site sont exactes

Source primaire : Centre pour la Cybersécurité Belgique — https://ccb.belgium.be/fr/news/nis2-echeance-du-18-avril-2026-ce-que-les-entites-essentielles-doivent-avoir-mis-en-place — consulté le 2026-09-14.

| Affirmation du site | Vérification |
|---|---|
| « Transposée par la loi du 26 avril 2024 » | exact — l'arrêté royal du 9 juin 2024 exécute la loi du 26 avril 2024 |
| « en vigueur depuis le 18 octobre 2024 » | exact — le CCB écrit « la loi belge NIS2, entrée en vigueur le 18 octobre 2024 » |
| « Échéance clé : 18/04/2026 » | exact — le CCB titre « NIS2 : échéance du 18 avril 2026 » |

**Ce que le site ne dit pas et pourrait dire.** Le 18/04/2026 n'est pas la fin du parcours :
les entités essentielles doivent avoir obtenu une vérification CyFun® Basic ou Important à cette
date, et une **certification complète pour le 18/04/2027**. Ajout PROPOSÉ, non écrit.

## 2. CSRD / Omnibus — **VÉRIFIÉ** sur la directive `(UE) 2026/470` : date exacte, seuil imprécis

Source primaire : directive **(UE) 2026/470**, adoptée par le Conseil le **24 février 2026**,
publiée au Journal officiel de l'Union européenne le **26 février 2026**, entrée en vigueur le
**18 mars 2026**.

La date du site était exacte. **Le seuil ne l'était pas tout à fait.**

Le site écrivait « a fortement relevé les seuils de la CSRD (cible ~1 000 salariés) ». Or les
deux critères sont **cumulatifs** : plus de 1 000 salariés **ET** plus de 450 millions d'euros
de chiffre d'affaires net. Le critère de total de bilan a été supprimé.

**Pourquoi ce n'est pas un détail.** Énoncer le seul seuil d'effectif fait croire à une
entreprise de 1 200 salariés et 100 M€ de chiffre d'affaires qu'elle est concernée — alors
qu'elle ne l'est pas. L'erreur allait dans le sens de l'**inquiétude inutile**, exactement ce que
ce site existe pour éviter. Sur la page dont le titre est « Et la CSRD ? Probablement pas pour
vous — et c'est vérifié », l'imprécision était particulièrement mal placée.

**Corrigé** dans une PR séparée, avec la référence de la directive et sa date de publication
ajoutées en note de source — le motif graphique déjà utilisé par les quatre autres blocs.

## 3. E-facturation B2B (Peppol) — **VÉRIFIÉ** sur `efacture.belgium.be`

Source primaire : SPF Finances — https://efacture.belgium.be/fr/partner/spf-finances — consulté le 2026-09-14 — « à partir du
1er janvier 2026, la facture électronique structurée sera obligatoire pour toutes les opérations
entre des assujettis TVA belges. La modification de la loi a été publiée au Moniteur belge le
20 février 2024. »

| Affirmation du site | Vérification |
|---|---|
| obligatoire entre assujettis TVA établis en Belgique | exact |
| « Un PDF envoyé par e-mail ne suffit plus » | exact — format structuré via Peppol exigé |
| « La tolérance d'environ trois mois annoncée pour début 2026 est passée » | exact — tolérance du 1er trimestre, expirée le 31 mars 2026 |

**Ce que le site ne dit pas et pourrait dire.** Le régime d'amendes de l'arrêté royal du
8 juillet 2025 — 1 500 €, puis 3 000 €, puis 5 000 € par infraction — n'apparaît nulle part.
C'est l'information la plus concrète pour une PME, et elle manque. Ajout PROPOSÉ, non écrit :
ajouter un chiffre de sanction est une modification de texte public, donc une décision de Chaima.

## 4. Lanceurs d'alerte — **VÉRIFIÉ** sur `ejustice.just.fgov.be`, et une exception manquait

Source primaire : le **texte de la loi lui-même**, banque de données Justel —
https://ejustice.just.fgov.be/eli/loi/2022/11/28/2022042980/justel — consulté le 2026-09-14.
Pas un commentaire de cabinet : l'article de loi.

La loi du 28 novembre 2022 transpose la **directive (UE) 2019/1937** du 23 octobre 2019. Elle a
été publiée au Moniteur belge le 15 décembre 2022 et est entrée en vigueur le 15 février 2023.
Le seuil de 50 travailleurs est exact — **article 11, § 2, alinéa 1er** : « le paragraphe 1er ne
s'applique pas aux entités juridiques du secteur privé qui comptent moins de cinquante
travailleurs ».

**Mais l'alinéa suivant dit ceci, et le site l'ignorait :**

> « L'exception visée à l'alinéa 1er ne s'applique pas aux entités relevant du champ
> d'application des dispositions en matière de services, produits et marchés financiers »

Autrement dit : **une entité du secteur financier est tenue d'avoir le canal de signalement quel
que soit son effectif**, y compris à dix salariés.

**Pourquoi c'est plus grave que l'imprécision CSRD.** L'erreur CSRD allait dans le sens de
l'inquiétude inutile — désagréable, mais sans conséquence juridique. Celle-ci va dans le sens
inverse : un courtier en assurances ou un intermédiaire financier de dix personnes lisait
« Dès 50 travailleurs », en concluait qu'il n'était pas concerné, et **restait en infraction**.
Un site de conformité qui rassure à tort est pire qu'un site qui se tait.

**Corrigé** dans la même PR, avec la référence exacte de l'article et de la directive européenne
transposée.

## 4 ter. Contre-vérification en NÉERLANDAIS — elle confirme, et elle trouve autre chose

Sur remarque de Chaima : le droit belge est publié en français **et** en néerlandais, les deux
versions faisant également foi. Vérifier une seule langue, c'est vérifier à moitié.

**La version néerlandaise confirme la correction, mot pour mot** — `etaamb.openjustice.be/nl` :

> « De in het eerste lid bedoelde uitzondering geldt niet voor entiteiten die onder het
> toepassingsgebied vallen van de bepalingen op het gebied van **financiële diensten, producten
> en markten** »

Les deux textes authentiques disent la même chose. La correction tient dans les deux langues.

**Et le néerlandais a montré une phrase que l'extrait français n'avait pas rendue** — l'extrait
FR consulté s'arrêtait juste avant. Le texte précise **comment le seuil de 50 se calcule** : il
s'agit de la **moyenne** des travailleurs occupés, au sens de l'article 14 de la loi du
20 septembre 1948 et de l'article 7, § 1er de la loi du 4 décembre 2007 sur les élections
sociales.

**Conséquence pour le site.** La carte dit aujourd'hui « une obligation qui passe souvent
inaperçue jusqu'à l'embauche qui fait franchir le seuil ». Ce n'est pas faux, mais cela suggère
un déclenchement **instantané**. Le seuil est en réalité une **moyenne annuelle**, recalculée au
1er janvier sur les quatre trimestres de l'année précédente — cette dernière précision provient
d'un cabinet spécialisé commentant une clarification législative, donc **PLAUSIBLE**, pas
**VÉRIFIÉ** — absente du texte consulté sur `etaamb.openjustice.be/nl`.

Reformulation **PROPOSÉE**, non écrite : la phrase actuelle n'est pas erronée, et la corriger
relève d'un arbitrage de rédaction, pas d'un correctif juridique.

**Ce que cet épisode établit comme méthode.** Lire la seconde langue n'a pas servi qu'à confirmer :
elle a produit une information absente du premier extrait. À partir d'aujourd'hui, toute
affirmation juridique du site est recoupée en **français et en néerlandais** pour le droit belge,
et en **anglais** pour le droit européen (EUR-Lex publie souvent la version anglaise en premier,
et les documents de la Commission y sont plus détaillés).

## 4 bis. RGPD — non recontrôlé ce jour

Les plafonds de 20 M€ / 4 % (article 83 du RGPD) n'ont pas été recoupés à la source aujourd'hui.
**NON VÉRIFIÉ ce jour** — inscrit au prochain passage plutôt que présenté comme contrôlé.

## 5. L'e-reporting 2028 — **VÉRIFIÉ** sur `blogitaa.be` (ITAA) : ma suspicion était fausse

J'avais laissé cette affirmation en **NON VÉRIFIÉ**, et j'ai d'abord soupçonné une confusion avec
le calendrier européen. **Cette suspicion était fausse**, et la vérification l'a montrée avant que
je n'accuse le site à tort.

**Le cadre européen** — paquet ViDA, directive **(UE) 2025/516** adoptée le 11 mars 2025, publiée
au Journal officiel le 25 mars 2025, en vigueur le 14 avril 2025. Les exigences de déclaration
numérique transfrontalière s'y appliquent au **1er juillet 2030**, et les États disposant d'un
reporting national en temps réel doivent s'aligner pour le **1er janvier 2035**. Source :
Commission européenne — https://taxation-customs.ec.europa.eu/news/adoption-vat-digital-age-package-2025-03-11_en

**Le calendrier belge est distinct, et c'est lui que le site cite.** L'e-reporting belge est une
décision de l'accord de gouvernement, visant le **1er janvier 2028**, bâtie sur la même
infrastructure Peppol que l'e-facturation et sur le *ViDA Tax Data Document*. L'Institut des
Experts-comptables et Conseils fiscaux le confirme en mai 2026 : projet de loi en phase finale
pré-parlementaire, publication de la loi attendue à l'automne 2026, arrêté royal d'exécution
début 2027.

**La nuance qui manque au site.** Au 14 septembre 2026, cet e-reporting repose sur un **projet de
loi non encore publié**. Le mot « prévu » employé par le site est donc exact — mais dire
explicitement que la loi n'est pas encore publiée serait plus honnête encore. Ajout **PROPOSÉ**,
non écrit : c'est une modification de texte public.

**Ce que le site ne dit nulle part** : ViDA existe, et fixe l'horizon européen à 2030 puis 2035.
Pour une PME belge qui facture hors de Belgique, c'est une information réelle. Ajout **PROPOSÉ**.

---

    DE : session Claude Code                POUR : CHAIMA
    OBJET : Fusionner PR #23 — deux corrections juridiques, dont une qui rassurait à tort.
    VERDICT : VÉRIFIÉ — directive `(UE) 2026/470` au JOUE du 26/02/2026 : 1 000 salariés ET 450 M€.
    PARCE QUE : le site énonçait le seul seuil d'effectif, ce qui élargit à tort le périmètre.
    NON VÉRIFIÉ : les plafonds RGPD de l'article 83, non recontrôlés ce jour.
    CE QUI CHANGERAIT MON AVIS : la clause de revoyure de 2031 peut rouvrir ces seuils — ce contrôle
    est à refaire, il n'est pas acquis.
