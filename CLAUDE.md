# CLAUDE.md — RÈGLES MAÎTRES DU PROJET (CAELUM PARTNERS)

## 0. AVANT TOUTE ACTION — PROTOCOLE « DRIVE D'ABORD » (P-DRIVE-D-ABORD, doc 19)
1. **DRIVE D'ABORD** : ouvre le dossier Drive concerné (Caelum/KMM/CompeteIQ → « 🗂️ Caelum — Journal
   d'Audit », ID 1npTlFufVU03luocJIw365Sd3evziZGg_ ; transversal → « 🗂️ COMPILATION & SYNOPSIS — Empire
   Chaima », ID 1qXUj9D9r7HSmIMzMcsScz4Ynlv4auP4G) et lis le DERNIER rapport de session + les titres
   existants + les décisions en attente. Ne refais JAMAIS un travail déjà fait ; ne crée JAMAIS de doublon ;
   repars toujours des versions déjà critiquées/corrigées, pas des originales.
2. Puis lis : ce fichier, « ETAT.md », et la dernière PASSATION. Ne relis pas tout le code : va droit aux
   fichiers concernés par ta tâche. Si ETAT.md n'existe pas, crée-le. Contradiction entre deux infos →
   trancher, corriger, dater ; deux versions ne coexistent jamais.
3. **JOURNALISATION — PROTOCOLE DE LIVRAISON (obligatoire à chaque livraison, directive Chaima 17-07-2026)** :
   - DATE/HEURE réelles via `TZ="Europe/Brussels" date` — utilisées PARTOUT (titres, en-têtes, passations).
   - Chaque document/rapport COMMENCE par un SYNOPSIS (2-3 lignes : quoi, pourquoi, état).
   - Titre horodaté : « AAAA-MM-JJ-HHhMM — [auteur] — [sujet] ».
   - AUDIT honnête : FAIT / VÉRIFIÉ (avec preuve : test, capture, commande) / RESTE. Ne JAMAIS dire
     qu'une chose est finie si elle ne tourne pas.
   - Copie du rapport dans le Drive, dossier « COMPILATION & SYNOPSIS — Empire Chaima »
     (ID 1qXUj9D9r7HSmIMzMcsScz4Ynlv4auP4G) ; SANS accès Drive : le dire et déposer dans `reports/` du dépôt.
   - Mettre à jour la passation (ETAT.md ici ; 00-LIRE-D-ABORD.md dans les dépôts qui l'utilisent).
   - Un document = un événement ; AJOUT, jamais d'écrasement. Vérité totale, zéro invention, sources datées.
   - Read-back après création avant d'annoncer.

## 1. MISSION & PÉRIMÈTRE
- UN seul projet : Caelum Partners. Interdit de démarrer un autre projet ou d'écrire un document de stratégie.
- Objectif : un MVP réellement déployable (simulateur « Suis-je concerné ? » → capture de lead → page /offres →
  paiement Stripe en test → pages légales).

## 2. TRAVAILLER AVEC L'ÉQUIPE D'AGENTS (obligatoire)
- Démarre toujours via l'agent « meta-orchestrateur », qui planifie et délègue aux agents spécialisés
  (orchestrateur-caelum, dev-frontend-ux, dev-backend-integrations, gardien-juridique-verite, rgpd-securite,
  qa-verificateur, architecte-securite, reponse-incident — et la flotte du doc 14 : designer-brand,
  redacteur-contenu, seo-technique, cro-conversion, accessibilite, strategiste-marketing, content-marketing,
  social-linkedin, ads-sea, email-marketing, partenariats-fiduciaires, analytics-mesure,
  completeur-angles-morts, analyste-marche, reformulateur-demandes).
- Une responsabilité = un agent (pas de doublon). En cas de recouvrement, le meta-orchestrateur tranche.
- Chaque tâche terminée passe par la **qualité en 3 couches** (doc 19) : production (agent spécialisé) →
  critique adversariale (« qa-verificateur »/« gardien-juridique-verite » : vérité, droit, RGPD, langue) →
  **critique de la critique** (un second vérificateur juge la critique : corrections fondées ? défaut raté ?
  sur-correction ?). Validé seulement ≥ 90/100, sinon retour en couche 1 avec la liste exacte.
  Action mineure (typo, commit technique) : auto-contrôle documenté (tests/grep/read-back) — le dire honnêtement.
- Avant tout déploiement : audit de « architecte-securite » + « rgpd-securite ».

## 3. RÈGLE DE VÉRIFICATION (À CHAQUE GESTE — le cœur)
- VÉRIFIER, PAS SUPPOSER : lance réellement le build ET les tests ; vérifie que le push distant a réussi.
- VÉRITÉ : aucun chiffre inventé ; chaque affirmation légale = loi réelle + source officielle + date, sinon supprimée.
- SÉCURITÉ : secrets en variables d'environnement uniquement ; validation stricte des entrées ; rate limiting.
- DEFINITION OF DONE : ne coche « fait » qu'avec preuve ; sépare toujours « vérifié » de « à finir ».

## 4. COMMUNICATION & SOURCE UNIQUE DE VÉRITÉ
- Source de vérité = le dossier Google Drive « 🗂️ COMPILATION & SYNOPSIS — Empire Chaima » + le fichier ETAT.md.
- En cas de contradiction entre deux informations, le document de compilation vérifié PRIME. On ne laisse jamais
  deux chiffres différents coexister : on tranche, on corrige, on date.
- MODÈLE DE PASSATION (à écrire en finissant chaque tâche, dans ETAT.md) :
  Tâche · Ce que j'ai fait · Fichiers touchés · Vérifié (build/test/push) + preuve · Ce qui reste/risques · Besoin du suivant.
- À la fin de CHAQUE session : écris un RAPPORT honnête DANS LE DRIVE (dossier compilation) : fait / vérifié / reste /
  dépend de Chaima. Objectif : que l'assistant qui suit Chaima puisse le lire et poursuivre avec elle.

## 5. LOIS À JOUR (refléter EXACTEMENT sur le site — ni plus, ni moins)
- E-facturation B2B : obligatoire depuis 01/01/2026 (Peppol), assujettis TVA établis en Belgique ; tolérance ~3 mois ; e-reporting 2028.
- NIS2 : en vigueur depuis 18/10/2024 ; échéance entités essentielles 18/04/2026 ; secteurs critiques.
- RGPD : toutes entreprises. Lanceurs d'alerte : ≥50 travailleurs. DORA : depuis 17/01/2025 (financier).
- CSRD : Omnibus 2026 → seuils relevés (~1000 salariés), échéances décalées → NE PAS la présenter comme obligation PME.
- Disclaimer obligatoire : « Caelum fournit information et outils, pas un conseil juridique ; Caelum n'est pas un cabinet d'avocats. »

## 6. DÉCISIONS RÉSERVÉES À CHAIMA (s'arrêter, demander, mais continuer le reste)
Prix des 3 offres · n° BCE / éditeur responsable · compte Stripe (clés) · accès DNS du domaine · email de réception des leads.

## 7. ESPRIT
Du côté de Chaima, pour sa réussite. Vérité sur les chiffres, jamais d'invention, jamais de flatterie.
Un rapport honnête vaut mieux qu'un rapport qui fait plaisir.
