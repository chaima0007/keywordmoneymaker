# 🗺️ CARTE VIVANTE — Empire Chaima

> La « carte vivante » que le CODEX §1 confie au **cartographe**, et qui n'existait pas jusqu'au
> 2026-09-16. Elle répond à une seule question : **où en est-on réellement, et qu'est-ce qui bloque ?**
>
> Règle de tenue : **un état vérifié, jamais de mémoire.** Chaque chiffre porte la commande qui
> l'établit. Mise à jour à chaque session qui change quelque chose de structurel — pas à chaque session.
>
> Dernière vérification : **2026-09-16**.

---

## 1. Ce qui est EN LIGNE aujourd'hui

`main` = `4f206cf` · dernier déploiement réussi sur ce commit.

Le site publié à `caelumpartners.agency` porte :
- l'**identité de marque** (marque, favicons, icône iOS, image de partage) — fusionnée le 11/09 ;
- les **polices auto-hébergées**, aucune fuite RGPD vers Google ;
- le design **« Le Greffe »** — celui que Chaima a rejeté (« un vieux site des années 2000 ») ;
- **quatre affirmations juridiques imprécises**, identifiées le 14/09 et corrigées **dans une PR non fusionnée**.

**NON VÉRIFIÉ, et structurellement invérifiable d'ici** : le rendu réel du site. La sortie réseau
de l'environnement d'agent refuse `caelumpartners.agency` (fiche E-21). La preuve disponible est le
listing des fichiers publiés par le déploiement — jamais un HTTP 200.

## 2. Ce qui est ÉCRIT mais PAS en ligne — le vrai blocage

**Quatre PR ouvertes, toutes vertes, toutes fusionnables, aucune fusionnée.**

| PR | Ouverte le | Ce qu'elle apporte | Ce qui la retient |
|---|---|---|---|
| **#18** | 11/09 | i-DEPOT : pourquoi il est invérifiable par un tiers, règle d'échéance | rien — jamais contestée |
| **#22** | 14/09 | refonte « Le Signal » (direction C, indigo) | le contradicteur demande que Chaima l'ouvre dans un navigateur |
| **#23** | 14/09 | 4 corrections juridiques + garde-fou de cohérence | 4 passages d'agents ; aucun n'a revu l'état final |
| **#24** | 14/09 | contenu redevenu visible sans JavaScript (2 fichiers) | rien — jamais contestée |

**C'est l'explication du « rien n'a changé ».** Le travail existe, il est vérifié, il est vert.
Il n'est pas en production parce que la fusion sur `main` est une décision humaine (§10), et que
Chaima a conditionné la fusion à l'accord préalable des agents — condition qui s'est révélée tout
sauf décorative : les agents ont bloqué trois fois de suite, à chaque fois à raison.

## 3. Le dispositif de contrôle — ce qui tourne à chaque PR

Quatre contrôles **bloquants** dans `.github/workflows/securite-code.yml`, plus un cinquième dans
la PR #23 :

| Contrôle | Ce qu'il rend impossible | Ce qu'il ne voit pas |
|---|---|---|
| `scripts/audit_code_sur.py` | secrets en dur, code à risque, licences non vérifiées | une faille sans motif connu |
| `scripts/audit_cloisonnement.py` | imports croisés entre produits, racine polluée | un import dynamique (`importlib`) |
| `scripts/generer_registre_erreurs.py` | divergence entre la base d'erreurs et son index | la justesse d'une fiche |
| `scripts/verifier_rapports.py` | trace inventée ou périmée dans un rapport | la justesse d'une conclusion |
| `scripts/verifier_coherence_juridique.py` *(PR #23)* | une correction juridique appliquée à la page et pas à l'outil, inversée, ou « OU » mis pour « ET » | le droit lui-même — il compare des chaînes |

Et dans `deploy.yml`, quatre garde-fous qui s'exécutent **après** la fusion, sur `main` : fuite de
fichier interne, CNAME absent, produit hors périmètre, **appel externe** (liste blanche d'hôtes).

**Point à connaître, et qui n'est pas intuitif** : `deploy.yml` ne se déclenche que sur un push vers
`main`. Ses garde-fous **n'ont jamais évalué une seule PR**. Le vert d'une PR ne dit rien sur le fait
que le site se déploiera.

## 4. Les deux substrats d'agents

| | Où | Quoi | Qui les lit |
|---|---|---|---|
| **Markdown** | `.claude/agents/` | **56** définitions de rôles | Claude Code |
| **Python** | `products/*/agents/` + `shared/` | **36** modules exécutables | `main.py`, socle `claude-agent-sdk` |

Ce ne sont **pas** des doublons — frontière documentée dans `.claude/FRONTIERE-SUBSTRATS.md`,
à lire avant toute affirmation sur « ce qui existe déjà » (fiche E-07).

Répartition Python : caelum 5 · competeiq 4 · kmm 12 · shared 15.

## 5. La mémoire — quel fait va dans quel fichier

C'est la question qui revient, et l'erreur la plus fréquente est d'écrire au mauvais endroit.

| Fichier | Ce qu'on y met | Ce qu'on n'y met PAS |
|---|---|---|
| `📋 JOURNAL.md` | un **snapshot par session** (§5). Rien n'a changé → **une seule ligne** | un rapport pour dire qu'il n'y a rien à dire — c'est une faute |
| `codex/EVOLUTION.md` | **uniquement les jalons** : décision prise, lancement, problème résolu. Append-only | « rien de neuf » — ça, c'est le journal |
| `codex/A-DECIDER.md` | tout ce qui **attend une décision de Chaima**, trié par ancienneté | une ligne ne disparaît que si elle est **tranchée**, jamais parce qu'elle a vieilli |
| `.claude/BASE-ERREURS.md` | **une fiche par erreur**, avec cause racine, signal, contre-mesure. **Fait foi** | une réécriture — on ajoute, on n'écrase pas |
| `🔴 ERREURS.md` | **rien à la main** — c'est l'index **généré** de la base ci-dessus | toute édition manuelle : la CI la détecte |
| `codex/rapports/` | tout **rapport complet**, horodaté, recoupé par `verifier_rapports.py` | un rapport qui n'existe que dans une conversation — invérifiable par construction |
| `codex/candidates/` | une **fiche par composant externe** évalué, même rejeté | — |
| `codex/ROUTINES.md` | les **ordonnanceurs** : cadence, rôle, condition d'arrêt | — |
| `ETAT.md` | la **passation** de fin de tâche | — |

État de ces fichiers au 2026-09-16 : **26 fiches d'erreurs** · **3 rapports déposés** ·
**22 lignes de routines** · **11 décisions en attente**, dont 4 depuis le 17/07.

## 6. Les quatre erreurs juridiques trouvées le 14/09

Elles ne sont **pas** des fiches de la base d'erreurs : ce sont des défauts du **site**, pas des
fautes de méthode. Elles sont documentées dans
`codex/rapports/2026-09-14-21h40 — Caelum Partners — Vérification — Sources légales du site, contrôle quotidien.md`.

| Affirmation | Défaut | Sens de l'erreur |
|---|---|---|
| Lanceurs d'alerte | secteur financier **et anti-blanchiment** exonérés à tort du seuil de 50 | **rassurait à tort** — le plus grave |
| CSRD | seuils présentés comme alternatifs ; directive non transposée en droit belge | les deux sens |
| RGPD | « le montant le plus élevé étant retenu » omis | sous-estimait |
| NIS2 | même omission | sous-estimait |

Toutes corrigées dans la **PR #23**, non fusionnée.

## 7. Ce qui reste NON VÉRIFIÉ, et qui le restera jusqu'à décision

- Le **rendu du site en production** — appartient structurellement à Chaima (fiche E-21).
- Le **montant exact** retenu par la loi belge du 26/04/2024 pour les sanctions NIS2 : la directive
  fixe un plancher (« au moins 10 M€ »), c'est le droit national qui arrête le chiffre.
- La **partie II de l'annexe** de la directive (UE) 2019/1937 : elle étend l'exemption du seuil de 50
  à d'autres secteurs, jamais lue.
- Les **seuils chiffrés** de la loi belge du 02/12/2024 (CSRD) : deux jeux de valeurs incompatibles
  rencontrés en recherche. Aucun chiffre ne doit être publié avant relecture au Moniteur.
- Le **contenu juridique en néerlandais** : le garde-fou de cohérence ne porte que des motifs français.
  Sans objet aujourd'hui — la page NL n'affirme rien de juridique — mais bloquant le jour où elle le fera.
