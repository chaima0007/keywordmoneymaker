# Pourquoi rien n'a changé, et ce que la mémoire avait manqué

**Phrase de contrôle honnête.** Aucun rapport de cartographie n'avait été produit depuis celui du
14/09 sur *La Loi Avec Moi* — sujet différent, aucun quasi-doublon. La condition d'arrêt a bien
fonctionné au sens strict (aucun document produit les 15 et 16/09 alors que rien ne bougeait), mais
**elle a trop bien fonctionné** : le silence a masqué que le journal n'avait pas enregistré la
soirée du 14/09. Un problème est donc porté ici sans attendre une demande : le rituel de snapshot
du §5 n'a pas été tenu par moi.

- **Projet** : Empire Chaima (transverse) · **Catégorie** : Cartographie
- **Rédigé par** : session Claude Code `session_01BLc73LKqGJyvJaoqFP9hT4`
- **Destinataire** : Chaima

---

## 1. La réponse à « pourquoi rien n'a changé »

`main` = `4f206cf`, **inchangé depuis le 14/09 à 22h**. Vérifié par `git log origin/main`, pas de mémoire.

**Quatre PR sont ouvertes, vertes, fusionnables — et aucune n'est fusionnée.**

| PR | Ouverte | Ce qu'elle apporte |
|---|---|---|
| #18 | 11/09 | i-DEPOT : invérifiable par un tiers, règle d'échéance |
| #22 | 14/09 | refonte « Le Signal » — la direction C que tu as confirmée |
| #23 | 14/09 | quatre corrections juridiques + garde-fou de cohérence |
| #24 | 14/09 | contenu redevenu visible sans JavaScript |

**Il n'y a pas de panne, pas de blocage technique, pas de CI rouge.** Le travail existe et il est
vérifié. Il n'est pas en production parce que fusionner sur `main` est une décision humaine (§10),
et que tu as conditionné la fusion à l'accord préalable des agents. Cette condition n'était pas
décorative : les agents ont bloqué **trois fois de suite**, à chaque fois à raison.

**Conséquence concrète, à dire clairement** : le site en ligne porte encore le design que tu as
rejeté **et** les quatre imprécisions juridiques trouvées le 14/09 — dont celle qui dit à des
entreprises obligées qu'elles ne le sont pas.

## 2. Ce que la mémoire avait manqué — et c'est ma faute

**`📋 JOURNAL.md`** : dernier snapshot au 14/09 **18h30**, c'est-à-dire écrit **avant** toute la
soirée. Les quatre erreurs juridiques, la refonte codée, les quatre passages d'agents, le garde-fou
écrit puis démoli puis réécrit : **rien n'était au journal**. Deux jours sans snapshot, alors que le
§5 en impose un par session. Corrigé : un snapshot daté couvre l'écart et le nomme.

**`codex/EVOLUTION.md`** : dernière entrée au 11/09, alors que six jalons avaient eu lieu depuis —
identité déployée, fuite RGPD fermée, quatre erreurs juridiques trouvées, défaut d'affichage majeur
corrigé, dispositif d'agents ayant prouvé sa valeur. Corrigé.

**`codex/A-DECIDER.md`** : ne mentionnait **aucune** des quatre PR. Le fichier censé répondre à
« qu'est-ce qui bloque » ne portait pas le blocage principal. Corrigé, avec la cinquième question du
simulateur ajoutée.

**`.claude/BASE-ERREURS.md`** : deux motifs réels du 14/09 au soir n'avaient aucune fiche.
Ajoutés — **E-27** (la brochure corrigée et le produit laissé faux) et **E-28** (un garde-fou aveugle
à la faute exacte qu'il devait empêcher). 28 fiches, index régénéré et vérifié.

## 3. Ce qui, en revanche, était bien tenu

Pour être juste, et parce qu'un rapport qui ne dit que le négatif est aussi faux qu'un rapport qui
flatte :

- La **structure §12** est conforme, 11 éléments sur 11.
- Le **registre d'erreurs** et son index généré n'ont jamais divergé — le contrôle est vert.
- Les **quatre contrôles bloquants** tournent sur chaque PR et n'ont laissé passer aucun push rouge.
- Les **trois rapports** déposés sont tous recoupés par `verifier_rapports.py`, zéro violation.
- Le **contrôle des sources** a fait exactement ce pour quoi il a été instauré : quatre erreurs
  juridiques réelles trouvées en une soirée, dont une qui pouvait coûter une sanction à un lecteur.

## 4. La carte vivante, créée

`codex/CARTE.md`. Le CODEX §1 la confie au cartographe depuis le 06/09 ; **elle n'avait jamais
existé**. Elle dit où en est le projet, ce qui bloque, ce que chaque contrôle rend impossible **et ce
qu'il ne voit pas**, la frontière entre les deux substrats d'agents — et surtout **quel fait va dans
quel fichier**, parce que l'erreur la plus fréquente n'est pas d'oublier d'écrire : c'est d'écrire au
bon sujet dans le mauvais endroit.

## 5. Un fait de structure qui mérite d'être connu

`.github/workflows/deploy.yml` ne se déclenche que sur un **push vers `main`**. Ses quatre
garde-fous — fuite de fichier interne, CNAME, périmètre produit, appel externe — **n'ont jamais
évalué une seule PR**. Le vert d'une PR ne dit donc rien sur le fait que le site se déploiera.
Constat, pas correctif : le modifier est une décision d'architecture.

## 6. Ce qui RESTE

- **Fusionner, ou dire pourquoi on ne fusionne pas.** C'est le blocage n°1, il est inscrit en tête
  d'`A-DECIDER.md`.
- Le **rendu du site en production** reste NON VÉRIFIÉ et t'appartient (fiche E-21).
- Quatre points de droit explicitement NON VÉRIFIÉS, listés dans la carte, §7.

---

    DE : cartographe                        POUR : CHAIMA
    OBJET : Fusionner les 4 PR ouvertes, ou inscrire la raison de ne pas le faire.
    VERDICT : VÉRIFIÉ — `main` inchangé depuis le 14/09, quatre PR vertes et fusionnables.
    PARCE QUE : rien de ce qui a été produit depuis le 11/09 n'est en production, y compris les
    corrections juridiques dont l'une rassure à tort un lecteur obligé.
    NON VÉRIFIÉ : le rendu réel du site (fiche E-21) ; quatre points de droit listés dans la carte.
    CE QUI CHANGERAIT MON AVIS : une raison de ne pas fusionner que je n'aurais pas vue — c'est
    précisément ce que les agents ont trouvé trois fois, et pourquoi la condition posée tient.
