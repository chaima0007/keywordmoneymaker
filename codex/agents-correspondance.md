# /codex/agents-correspondance.md — réconciliation des 21 rôles CODEX ↔ flotte existante

> Décision 2026-09-11 (TRANCHÉ PAR CHAIMA) : **MAPPER + COMPLÉTER, sans suppression.**
> On garde les agents existants (aucune suppression — §10), on AJOUTE les rôles CODEX réellement
> absents, et on MAPPE les autres vers l'agent existant qui les couvre déjà.
> Aucun agent n'a été supprimé. La consolidation éventuelle des doublons est une décision humaine ultérieure.

## Rôles CODEX AJOUTÉS (absents jusqu'ici) — récupérés de la PR #6 (vérifiée propre : 0 secret, 0 code malveillant, CI verte)
| Rôle CODEX (§1) | Raison de l'ajout |
|---|---|
| avocat | cœur délibératif parcours 2 — plaide POUR ; aucun équivalent |
| contradicteur | cœur délibératif parcours 2 — plaide CONTRE (permanent) ; aucun équivalent général |
| simulateur-scenarios | scénarios optimiste/réaliste/pessimiste ; aucun équivalent |
| arbitre-expert | UNE recommandation arbitrée ; aucun équivalent (≠ meta-orchestrateur qui arbitre les agents) |
| verificateur-verite | vérificateur transverse de vérité (référencé par la skill /debat) ; proche de gardien-juridique-verite mais distinct |
| superviseur-vigie | snapshot §5 d'entrée de session + hygiène ; aucun équivalent |
| cartographe | tient A-DECIDER.md + EVOLUTION.md + carte ; aucun équivalent |
| intendant-couts | dépenses récurrentes / plans gratuits / coûts dormants ; aucun équivalent |
| conservateur-secrets | fuite de secrets (.env, historique git, bundle client) ; distinct (cf. l'incident de fuite Pages) |
| avocat-du-client | voix de l'utilisateur payant ; aucun équivalent |
| croque-mort | déclarer mort / archiver / post-mortem ; aucun équivalent |
| responsable-continuite | sauvegardes / restauration / continuité ; aucun équivalent |
| archiviste-preuves | conserver la preuve, pas seulement le lien ; aucun équivalent |

## Rôles CODEX MAPPÉS vers un agent existant (pas de doublon créé)
| Rôle CODEX (§1) | Agent(s) existant(s) qui le couvre(nt) |
|---|---|
| scout | chercheur-code-libre |
| guardian-licences | auditeur-licences |
| sentinel-securite | architecte-securite (+ contre-verificateur-securite, auditeur-chaine-approvisionnement, verificateur-code-tiers) |
| architecte-integration | dev-backend-integrations (+ dev-frontend-ux) |
| gardien-donnees | rgpd-securite |
| scribe-empire | redacteur-contenu (+ content-marketing) |
| eclaireur-opportunites | analyste-marche |
| testeur-adverse | qa-verificateur |

## Note
- verificateur-verite (ajouté) et gardien-juridique-verite (existant) se recouvrent partiellement :
  le premier est le vérificateur de vérité transverse du CODEX, le second le gardien juridique+vérité du projet.
  Les deux sont conservés ; à consolider si Chaima le décide (décision humaine, §10).
- Les autres agents métier existants (marketing, SEO, design, dev, meta-orchestrateur…) n'ont pas d'équivalent
  CODEX : ils restent la flotte opérationnelle du projet, complémentaire des rôles de gouvernance du CODEX.

## Ajout du 2026-09-11 — rôles de patrimoine (hors des 21 rôles CODEX)
Créés à la demande de Chaima pour tenir `🔐 PATRIMOINE.md` (base unique de ce qu'elle possède).
Ils ne figurent pas dans les 21 rôles du §1 : ce sont des rôles **propres au projet**, ajoutés sans
rien retirer, conformément à la décision « mapper + compléter, sans suppression ».

| Rôle | Fichier | Périmètre |
|---|---|---|
| **DÉPOSANT** | `.claude/agents/deposant.md` | colonnes *statut* et *droits* : marques, dépôts, cessions. Ne dépose jamais rien lui-même (§10). |
| **HORLOGER** | `.claude/agents/horloger.md` | colonnes *date* et *preuve* : antériorité, dates de création (via git), **échéances** (i-DEPOT 5/10 ans, domaine, marque). |

Recouvrement assumé avec `archiviste-preuves` : celui-ci conserve la preuve de toute affirmation
publiée ; l'HORLOGER est spécialisé sur les dates et les échéances du patrimoine. Les deux coopèrent.
Total agents : 42 → **44**.
