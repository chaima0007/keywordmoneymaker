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

## 4. Lanceurs d'alerte et RGPD — non recontrôlés ce jour

La loi du 28 novembre 2022 et le seuil de 50 travailleurs, ainsi que les plafonds RGPD
(20 M€ / 4 %), n'ont pas été recoupés à la source aujourd'hui. Ils sont stables depuis leur
publication et ne figuraient pas parmi les affirmations à risque de dérive. **NON VÉRIFIÉ ce
jour** — à inscrire au prochain passage plutôt qu'à présenter comme contrôlé.

## 5. Une affirmation que je n'ai pas pu établir

« Un e-reporting est prévu pour 2028 » (carte e-facturation). Aucune des sources primaires
consultées aujourd'hui ne l'établit. C'est cohérent avec le calendrier ViDA de la Commission,
mais **cohérent n'est pas vérifié**. Statut : **NON VÉRIFIÉ**. À trancher au prochain contrôle :
sourcer ou retirer.

---

    DE : session Claude Code                POUR : CHAIMA
    OBJET : Fusionner la correction du seuil CSRD — deux critères cumulatifs, pas un seul.
    VERDICT : VÉRIFIÉ — directive `(UE) 2026/470` au JOUE du 26/02/2026 : 1 000 salariés ET 450 M€.
    PARCE QUE : le site énonçait le seul seuil d'effectif, ce qui élargit à tort le périmètre.
    NON VÉRIFIÉ : l'e-reporting 2028, et les affirmations lanceurs d'alerte / RGPD non recontrôlées ce jour.
    CE QUI CHANGERAIT MON AVIS : la clause de revoyure de 2031 peut rouvrir ces seuils — ce contrôle
    est à refaire, il n'est pas acquis.
