# CLAUDE.md — RÈGLES MAÎTRES DU PROJET (CAELUM PARTNERS)

## 0. AVANT TOUTE ACTION
Lis d'abord : ce fichier, puis « ETAT.md » (état du projet), puis la dernière PASSATION. Ne relis pas tout le
code : va droit aux fichiers concernés par ta tâche. Si ETAT.md n'existe pas, crée-le.

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
- Chaque tâche terminée passe par le « qa-verificateur » : score qualité ≥ 90/100 sinon retour avec corrections.
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
