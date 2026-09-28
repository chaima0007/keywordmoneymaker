# 2026-09-28-20h13 — Empire Chaima — Audit — Garde-fous, réparateurs, experts : ce qui tient et ce qui a dérivé

**SYNOPSIS.** Audit demandé par Chaima : où sont les garde-fous, les réparateurs, les experts, et où
sont les problèmes. Les cinq contrôles bloquants tiennent et rendent tous 0. Deux dérives réelles
trouvées : le rituel de snapshot avait douze jours de retard alors qu'une Routine tournait toutes les
six heures, et le paragraphe du CLAUDE.md que tout agent doit lire « avant d'affirmer ce qui existe
déjà » désignait un dossier qui n'existe pas. Les deux sont corrigés.

**Contrôle honnête avant rapport (§2 ter).** Aucun document quasi identique : le dernier rapport
porte sur les questions du simulateur (19/09), la dernière cartographie sur le 16/09. Celui-ci est un
audit du dispositif, demandé, et il constate une dérive qu'aucun des deux n'avait vue. L'ÉLAGUEUR
n'est pas saisi — au contraire, cet audit existe parce que la condition d'arrêt a trop bien
fonctionné (voir §2).

---

## 1. Les garde-fous — cinq, tous verts, et un angle mort connu

Cinq contrôles bloquants tournent dans `.github/workflows/securite-code.yml`. Exécutés localement ce
jour, chacun rend 0 :

| Contrôle | Ce qu'il rend impossible | Ce qu'il ne voit pas |
|---|---|---|
| `scripts/audit_code_sur.py` | motifs de code dangereux connus | une CVE ; un code sûr mais faux |
| `scripts/audit_cloisonnement.py` | qu'un produit importe le code d'un autre | un import dynamique (importlib) |
| `scripts/generer_registre_erreurs.py` | que l'index et la base d'erreurs divergent | qu'une fiche soit juste |
| `scripts/verifier_rapports.py` | une trace inventée ou périmée dans un rapport | que les conclusions soient justes |
| `scripts/verifier_coherence_juridique.py` | 8 affirmations juridiques contredites sur 7 fichiers | il compare des chaînes, il ne lit pas le droit |

**L'angle mort, connu et non corrigé.** Le second workflow, `deploy.yml`, publie en liste blanche et
porte quatre gardes — mais il ne se déclenche que sur un push vers `main`. Ses gardes ne s'exécutent
donc **jamais** sur une pull request. C'est consigné dans `codex/CARTE.md` ; ce n'est pas réparé.

VÉRIFIÉ — les cinq rendent 0, exécutés depuis `scripts/` : `scripts/audit_code_sur.py`,
`scripts/audit_cloisonnement.py`, `scripts/generer_registre_erreurs.py`, `scripts/verifier_rapports.py`,
`scripts/verifier_coherence_juridique.py`

## 2. La dérive principale : le contrôle automatique a remplacé le rituel

Une Routine de contrôle a réveillé la session **toutes les six heures pendant neuf jours** pour
surveiller la PR #26. Elle a bien travaillé : état réel relu à chaque fois, aucun rapport inutile,
aucun commentaire de bruit sur la PR. Pendant ce temps :

- `📋 JOURNAL.md` : dernier snapshot le **2026-09-16** — douze jours, alors que le §5 en impose un par
  session, et que **huit commits** ont été poussés dans l'intervalle ;
- `ETAT.md` : dernière modification le **2026-09-14** — quatorze jours, alors que le §4 du projet
  impose une passation à la fin de chaque tâche.

Le journal portait déjà, daté du 2026-09-14, le constat d'un écart de **huit jours** sur ce même
rituel. La faute s'est donc répétée à l'identique après avoir été documentée.

**La cause n'est pas la négligence, c'est le déplacement de l'attention.** La règle anti-bruit
(« si rien n'a changé, une seule ligne ») était juste pour la PR et fausse pour le dépôt : huit
commits ne sont pas « rien n'a changé ». Un réveil automatique donne le sentiment d'être à jour sur
tout, alors qu'il ne l'est que sur ce qu'il regarde.

Fiche **E-30** ajoutée, avec la commande qui tranche :
`git log --oneline --since=<date du dernier snapshot> | wc -l` — tout résultat supérieur à zéro
signifie qu'un snapshot est dû.

**Corrigé** : snapshot du 2026-09-28 écrit dans le journal, passation écrite dans `ETAT.md`,
`codex/A-DECIDER.md` redaté (il affichait encore le 20/09).

## 3. Le défaut que l'audit a trouvé dans la constitution elle-même

Le §2 ter.3 du `CLAUDE.md` — le paragraphe que tout agent doit lire **avant d'affirmer ce qui existe
déjà**, écrit précisément pour éviter la fiche E-07 — désignait « les **33 modules Python** de
`agents/` » et un fichier `agents/base_erreurs.py` qui n'existe pas (chemin cité ici pour mémoire,
délibérément absent du dépôt).

**Ce dossier n'existe pas à la racine du dépôt.** Les modules sont répartis dans `products/*/agents/`
(21) et `shared/` (15), soit 36, et la base d'erreurs est atteinte via `shared/base_erreurs.py`.

VÉRIFIÉ — `find . -name "*.py" -not -path "./.git/*"` regroupé par dossier : `shared` 15,
`products/kmm/agents` 12, `products/caelum/agents` 5, `products/competeiq/agents` 4, `scripts` 5,
racine 1 (`main.py`). Aucun dossier `agents/` à la racine.

VÉRIFIÉ — `codex/CARTE.md` ligne 68 portait déjà les bons chemins depuis le 2026-09-16 :
`products/*/agents/` + `shared/`, 36 modules. **La carte était juste et la constitution périmée.**

C'est exactement le mode de défaillance contre lequel ce paragraphe avait été écrit : une session a
réorganisé les modules par produit, la carte a suivi, le texte de référence non. Corrigé dans
`CLAUDE.md`.

## 4. Les réparateurs — un seul répare, les autres constatent

Sur les cinq contrôles, **un seul répare** : `generer_registre_erreurs.py`, qui régénère
`🔴 ERREURS.md` depuis `.claude/BASE-ERREURS.md` et fait échouer la CI si les deux ont divergé. Les
quatre autres bloquent sans corriger.

Le véritable dispositif de réparation est la **base d'erreurs** : 30 fiches, dont cinq nées d'erreurs
commises par un agent dans la quinzaine écoulée — E-26 (livraison annoncée sans vérifier qu'elle
existe), E-27 (brochure corrigée, produit laissé faux), E-28 (garde-fou aveugle à la faute qu'il
devait empêcher), E-29 (liste juridique écrite de mémoire puis annoncée complète), E-30 (celle-ci).

Ce n'est pas un bon score, c'est un bon signe : une base d'erreurs qui ne contient que les fautes des
autres est fausse.

## 5. Les experts — où ils sont, et ce qu'ils valent

VÉRIFIÉ — `ls .claude/agents/*.md | wc -l` → **56** définitions de rôles, lues par Claude Code.
VÉRIFIÉ — **36** modules Python exécutables, répartis comme au §3, socle `main.py`.
VÉRIFIÉ — **12** fiches d'expertise comptées dans `codex/expertise/droit-conformite-belgique.md`, domaine ouvert le 2026-09-21, maturité **CONFIRMÉ** (EXPERT exige aussi un deuxième
projet : le seuil de fiches est franchi, pas celui des projets).

**Ce que les experts ont réellement produit cette quinzaine**, et c'est le point à retenir : le
gardien juridique et le contradicteur ont bloqué **quatre** corrections successives, à chaque fois à
raison — formulation plus étroite que l'article cité, brochure corrigée avec produit laissé faux,
garde-fou aveugle, liste de secteurs écrite de mémoire. L'avocat du client a trouvé un dark pattern
dans un libellé que j'avais écrit une heure plus tôt. Le dispositif n'est pas décoratif.

## 6. Ce qui bloque, par ordre réel

1. **PR #26 en brouillon.** Verte, sans conflit, huit commits. Rien de ce qui a été fait depuis le
   19/09 n'est en production. Elle attend le feu vert de Chaima — c'est une page publique, parcours 3.
2. **Les quatre décisions de juillet**, toujours ouvertes : prix des trois offres, n° BCE / éditeur
   responsable, déclaration ONEM (débloque Stripe), compte Brevo. Les mentions légales affichent
   toujours « à compléter » en production.
3. **Cinq Routines sans condition d'arrêt déclarée**, inchangé depuis le 2026-09-14.
4. **`deploy.yml` sans garde sur PR** (§1).

## Ce qui reste NON VÉRIFIÉ

- Le rendu du site en production : le proxy refuse `caelumpartners.agency` (fiche E-21). Les captures
  de Chaima du 19/09 restent la seule preuve directe.
- Les trois points juridiques du rapport du 19/09 : sanctions de la loi lanceurs d'alerte, colonne
  « type d'entité » des annexes belges, décompte des intérimaires (NON TRANCHÉ, ambiguïté du texte).
