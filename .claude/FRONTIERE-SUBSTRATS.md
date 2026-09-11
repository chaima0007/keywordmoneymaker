# FRONTIÈRE DES DEUX SUBSTRATS D'EXÉCUTION

> Établie le 2026-09-11-17h20 (Europe/Brussels), sur décision de Chaima : ni archivage, ni fusion —
> une frontière documentée. Constat d'origine : fiche **E-07** de `.claude/BASE-ERREURS.md`.

## LE CONSTAT
Ce dépôt contient **deux systèmes d'agents distincts qui s'ignoraient totalement.**
Vérifié le 2026-09-11 : `grep -rn "\.claude" main.py agents/` ne renvoie **rien**. Aucune référence
croisée, dans aucun sens.

| | Substrat A — Markdown | Substrat B — Python |
|---|---|---|
| Emplacement | `.claude/agents/*.md` | `agents/*.py` |
| Volume | **42** définitions (29 préexistantes + 13 de la chaîne veille) | **33** modules, ~5 300 lignes |
| Nature | **Prompts** — définitions de sous-agents | **Code exécutable** |
| Exécuté par | Claude Code (délégation à un sous-agent) | `main.py` — « Caelum Partners, Lanceur Central » |
| Socle technique | aucun (fichiers d'instructions) | `claude-agent-sdk`, `composio` |
| État | mémoire de conversation | `.caelum_memory.json` |
| Orchestrateurs | `meta-orchestrateur`, `orchestrateur-caelum`, `chef-orchestre-veille` | `commandant.py`, `superviseur.py`, `run_all.py`, `parallel_runner.py`, `competeiq_orchestrator.py` |
| Lit `CLAUDE.md` ? | **oui** | **non** — d'où le module `agents/base_erreurs.py` |

**Ce ne sont donc pas des doublons.** Ce sont deux manières différentes d'exécuter des agents. Les
fusionner n'aurait pas de sens ; en archiver une tuerait un système qui tourne.

## LA FRONTIÈRE — qui possède quoi

**Substrat A (Markdown) possède** le travail fait *dans une session Claude Code* : analyse, vérification,
rédaction, revue, décision documentée. Tout ce qui produit un jugement ou un document.

**Substrat B (Python) possède** le travail *exécutable et répétable hors session* : traitements par lots,
agents produits lancés depuis un menu, automatisations avec état persistant.

**Règle d'arbitrage.** Si une capacité existe des deux côtés, celui qui la possède est celui dont le
**mode d'exécution** correspond au besoin — pas celui qu'on a sous la main. Cas d'usage ponctuel et
raisonné → A. Traitement répétable et lançable par Chaima seule → B. En cas de doute,
`meta-orchestrateur` tranche.

**Interdit dans les deux sens.** Ne pas réimplémenter en Python un rôle de la chaîne veille, ni décrire
en Markdown un agent produit qui existe déjà en Python. Toute nouvelle capacité choisit **un** substrat,
et le déclare ici.

## CE QUI TRAVERSE LA FRONTIÈRE
Une seule chose, volontairement : **la base d'erreurs**. `.claude/BASE-ERREURS.md` est la source unique,
lue par les deux côtés — par le `CLAUDE.md` §2 ter pour le substrat A, et par `agents/base_erreurs.py`
pour le substrat B. Ce module **lit** la base, il ne la recopie pas : une règle qui vit à plusieurs
endroits finit par diverger (fiche E-01).

## LIMITE CONNUE, NON RÉSOLUE
Ce dépôt héberge **trois produits** — Caelum Partners, KeywordMoneyMaker, CompeteIQ — sites, agents et
code mêlés. Dans `agents/` seul : 8 modules mentionnent Caelum, 10 KeywordMoneyMaker, 4 CompeteIQ.
C'est la cause structurelle d'E-07 et une violation de « par projet, jamais mélangé » **à l'échelle du
dépôt**. Un plan de séparation est soumis à Chaima ; rien n'est exécuté sans son feu vert.
