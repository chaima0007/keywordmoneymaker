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

## Ajout du 2026-09-11 (soir) — rôles du domaine VEILLE / BREVETS / CAPITAUX (hors des 21 rôles CODEX)
Chaîne proposée par Chaima, réconciliée avec la flotte existante **rôle par rôle, par elle**. Même
principe que ci-dessus : mapper + compléter, **sans suppression** (§10).

### Ce qui NE crée PAS de rôle nouveau — arbitrages de Chaima
| Rôle proposé | Décision | Rôle qui l'assume |
|---|---|---|
| ÉLAGUEUR | **abandonné**, le nom existant est gardé | `croque-mort` — mission identique (« déclarer mort, archiver, post-mortem ») |
| GARANT | **fusionné** dans un rôle existant | `verificateur-verite`, complété de la nuance « sur quoi repose la confiance ? » (voir son fichier) |
| DÉPOSANT | déjà créé le 2026-09-11 (matin) | `deposant` |
| HORLOGER | déjà créé le 2026-09-11 (matin) | `horloger` |

### Rôles AJOUTÉS — aucun équivalent dans la flotte (8)
| Rôle | Périmètre | À ne pas confondre avec |
|---|---|---|
| `testeur` | viabilité réelle d'une trouvaille EXTERNE, itérations documentées, échecs compris | `testeur-adverse` (§1, couvert par `qa-verificateur`) qui teste la non-régression de NOTRE code |
| `controleur` | 2ᵉ vérification **indépendante**, jugement formé avant lecture du 1ᵉʳ rapport | `verificateur-verite`, qui contrôle le statut épistémique, pas la reproductibilité |
| `pilote` | ordre d'exécution du domaine + qualification des blocages | `meta-orchestrateur`, qui garde l'autorité hors domaine |
| `chef-orchestre-veille` | répartition dans le domaine + UNE synthèse unique ; **subordonné** | `meta-orchestrateur` — deux chefs d'orchestre = paralysie |
| `sentinelles` | trois passes nommées (légale, technique, divulgation) : ce que personne n'a soulevé | `sentinel-securite` (§1, mappé sur `architecte-securite`) |
| `gardien-controle-final` | droit de dire « ce n'est pas terminé » + audit de la chaîne | `gardien-juridique-verite` et `gardien-donnees`, autres périmètres |
| `prophete` | attaques anticipées sur CVE publiées et patterns documentés | `conservateur-secrets`, qui traite ce qui fuit déjà |
| `dechiffreur` | résumé opposable d'une source technique dense (brevet, thèse, norme) | `scribe-empire` (mappé), qui rédige pour publication |

### Rôles AJOUTÉS après REDÉCOUPAGE d'un recouvrement (4) — frontières écrites dans chaque fichier
| Rôle | Ce qui est à lui | Ce qui n'est PAS à lui |
|---|---|---|
| `guetteur` | menaces **externes** uniquement | l'état interne (`superviseur-vigie`), les passations (`passerelle`) |
| `passerelle` | circulation de l'info **entre agents** uniquement | l'état interne (`superviseur-vigie`), les menaces (`guetteur`) |
| `boussole` | **constat** de dérive de périmètre et de doublon | tenir un état ou un fichier de gouvernance (`cartographe`) |
| `protecteur` | fuite **juridique** : divulgation avant dépôt (art. 54 CBE), **irréparable** | fuite **technique** : clés, `.env`, historique git (`conservateur-secrets`), réparable par rotation |

`superviseur-vigie`, `cartographe` et `conservateur-secrets` ont reçu en retour la frontière réciproque,
écrite dans leur propre fichier : une frontière connue d'un seul côté n'est pas une frontière.

**Aucune suppression. Aucun agent renommé.** Total agents : 44 → **56**.

> Garde-fou assumé : 56 agents, c'est le régime où les doublons se multiplient sans que personne ne les
> voie. C'est précisément le mandat de `boussole`, et l'audit de chaîne de `gardien-controle-final`.

