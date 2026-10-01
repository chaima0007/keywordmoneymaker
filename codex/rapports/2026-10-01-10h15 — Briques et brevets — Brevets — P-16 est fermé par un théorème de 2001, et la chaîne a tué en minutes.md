# P-16 est fermé par un théorème de 2001, et la chaîne a tué en minutes

**Contrôle honnête d'entrée.** Ce rapport annonce une septième mort, mais pour la première fois la
mort est bon marché et c'est le seul résultat qui compte ici. Aucun document quasi identique dans
`codex/rapports/` : les six précédents portent sur des croisements entre domaines, celui-ci sur la
première entrée du registre des solutions. Il corrige aussi trois choses que j'avais écrites
moi-même dans `codex/briques/CARNET-04-quantique-fusion-et-superposition.md`.

**Au service de la consigne n°1** en vigueur (`codex/CONSIGNE-N1.md`), route 1 : les problèmes à
effet technique physique. Réponse à l'autorisation « vasy » du 2026-10-01 : mettre la chaîne
physique au travail sur `P-16`.

---

## 1. Ce que j'ai fait, et dans quel ordre

La chaîne impose l'antériorité **avant** toute proposition. Appliqué : aucune hypothèse n'a été
formulée, aucun chiffre produit, aucun calcul lancé. J'ai pris la question telle qu'elle est écrite
dans la fiche de `physicien-fusion-et-boosting` — *existe-t-il un gain de probabilité de succès de
fusion qui ne se paie pas en photons exposés à la perte ?* — et je suis allé voir si elle était
ouverte.

Elle ne l'est pas. Entrée `S-01` au registre des solutions, état **MORTE**.

## 2. Ce n'est pas un trou, c'est un théorème — et les quatre portes sont occupées

**Le mur.** Calsamiglia et Lütkenhaus établissent que la discrimination non ambiguë de quatre états
de Bell équiprobables en optique linéaire ne dépasse pas **1/2** ; que des modes auxiliaires **dans
le vide** n'améliorent rien ; et qu'une mesure déterministe est **impossible avec n'importe quel
état auxiliaire**, même avec rétroaction conditionnelle. Relevé dans Schmidt & van Loock,
arXiv:2410.20261 (2024-10-26), qui les citent en références [3], [4] et [5].

**Les quatre sorties publiées :**

| sortie | coût | occupée par |
|---|---|---|
| photons auxiliaires | des photons exposés à la perte | Grice 2011 · Ewert & van Loock 2014, 3/4 avec quatre photons non intriqués · optimalité chez Olivo & Grosshans 2018 |
| redondance de code | des photons | le « code-boosting », déjà dans la proposition FBQC d'origine |
| **compression (gaussien actif)** | **des compresseurs, pas des photons** | **Zaidi & van Loock, PRL 110, 260501 (2013)** |
| changer la mesure elle-même | une architecture | Pankovich et coll., ORCA Computing, PRL 133, 050604 (2024) — projection en base GHZ |

**La troisième sortie est mot pour mot la question posée, et elle a treize ans.** Le titre de Zaidi
& van Loock est *« Beating the one-half limit of ancilla-free linear optics Bell measurements »*.

## 3. La ligne étroite meurt aussi, et par un chiffre

On pouvait espérer que la compression reste inexploitée **en rail double** — l'encodage qu'emploie
réellement la FBQC. Non, et c'est quantifié :

- **Phys. Rev. A 99, 032302 (2019)** : la valeur de 0,643 souvent citée est *« un résultat ponctuel
  expérimentalement inatteignable »*, qui tombe à 0,59 au moindre écart sur le paramètre de
  compression. Le maximum réellement atteignable est **0,596** à r ≈ 0,774.
- **arXiv:2412.07353** (2025) : *« pour les systèmes bidimensionnels, la procédure de compression ne
  bat même pas la mesure de Bell la plus simple avec photons auxiliaires »*.

**0,596 sans photons contre 0,625 avec deux photons auxiliaires.** En rail double, la porte sans
photons est la **moins bonne** des quatre. Elle ne devient avantageuse qu'en dimension supérieure —
et la dimension supérieure est occupée : arXiv:2505.16816 (2025), PRL 134, 200801 (2025), et surtout
**arXiv:2606.29432, *Squeezing-enhanced Pairwise Fusion of Photonic Qudits***, dont le résumé
annonce *« recycler des échecs de mesure structurés sans photons auxiliaires en entrée »* — 75 % à
79,62 % en d = 4, 83,33 % à 87,15 % en d = 6, au prix de 2d compresseurs. La question posée, plus la
seule variante qui restait, faites et publiées.

Et le terrain bouge encore : *Single-photon-boosted type-I fusion gates*, Phys. Rev. Applied, publié
le **2026-09-16** — douze jours avant l'ouverture de `S-01`.

## 4. Trois corrections à mon propre carnet

**Un.** Le carnet écrivait : *« on le contourne par l'encodage et l'adaptativité »*. Il y a
**quatre** sorties, pas deux, et celle que j'allais chercher est la troisième.

**Deux.** La question inscrite dans la fiche du physicien n'était pas une question de recherche :
elle est bornée par un résultat d'impossibilité. **Une question dont la réponse est un théorème
n'est pas une direction.**

**Trois, et la plus utile.** Le carnet cite *« booster […] n'a aucune tolérance intrinsèque à la
perte »* comme un constat de domaine. La citation est exacte, sa portée non : une **expérience**
publiée dans npj Quantum Information le 2025-03-08 mesure une mesure de Bell boostée à 69,3 ± 0,3 %
et rapporte un seuil de perte passant de 0,45 % à **1,4 %**, soit un triplement de la robustesse à
la perte.

Les deux énoncés ne se contredisent pas — booster n'apporte pas de tolérance *par lui-même*, c'est
l'encodage qui la donne — mais les modèles d'erreur diffèrent et **les chiffres ne s'additionnent
pas**. Ma faute est d'avoir cité la phrase pessimiste seule. C'est la famille de la fiche `E-36`, et
je n'ouvre pas de fiche nouvelle : `E-36` couvre déjà ce signal exact, et la dédoubler diluerait la
première.

## 5. Ce que le dispositif a bien fait, et c'est le vrai résultat

La contre-mesure d'`E-36`, écrite trois jours plus tôt, disait : *« quand un article dit qu'un outil
manque, lis les références de la phrase avant de la croire. »* Appliquée.

Conséquences mesurables :

- la piste est morte **en minutes**, contre des heures ou des jours pour chacun des six croisements ;
- **aucun secret n'a été créé**, donc `S-01` peut être écrite en clair dans un dépôt public sans rien
  divulguer — il n'y a pas de fond à mettre au coffre ;
- la chaîne engendrée hier a produit son premier résultat utile le jour suivant, et ce résultat est
  un refus.

**Le coût réel d'un dispositif de veille ne se mesure pas au nombre de candidats qu'il produit, mais
à la vitesse à laquelle il tue les mauvais.** C'est la première fois que cette vitesse se compte en
minutes.

## 6. Ce qui n'est pas prouvé

- Schmidt & van Loock **rapportent** qu'une étude récente, leur référence [20], démontre
  analytiquement la borne de 1/2 pour les fusions généralisées sans photon auxiliaire ni redondance
  de code. **Je n'ai pas lu [20] et je ne l'ai pas identifiée : NON VÉRIFIÉ.** Ce qui est établi par
  leur texte, c'est l'existence de ce résultat et les bornes de Calsamiglia–Lütkenhaus citées en [3]
  à [5] — lecture du 2026-10-01 à https://arxiv.org/abs/2410.20261
- **Aucune revendication de brevet lue sur ce sujet.** La mort est par **publication**, pas par
  dépôt. Cinquième fois sur sept — et cela affaiblit encore l'argument du virage quantique, déjà
  corrigé en fiche `E-36`.
- Toutes les probabilités citées sont **LUES** dans les articles nommés, aucune n'est SIMULÉE ni
  MESURÉE ici. PLAUSIBLE, confiance MODÉRÉE sur les valeurs ; confiance ÉLEVÉE sur le fait que la
  direction est occupée.
- Registres EPO et Espacenet toujours inatteignables depuis cette session.
- Ceci n'est pas un conseil juridique.

## 7. Ce que je propose ensuite, et je ne tranche pas

`P-16` est fermé comme piste de brevet. Deux cibles restent, et je les classe :

1. **`P-15`, à vérifier en premier et vite** — les *scraps* sont la piste que la littérature nomme
   sans l'épuiser, mais arXiv:2606.29432 recycle des « échecs de mesure structurés », ce qui en est
   voisin sans être identique. Si c'est la même chose, `P-15` tombe aussi, et il vaut mieux le savoir
   en une heure.
2. **`P-17`, volets dispositif** — une ligne à retard qui perd moins, et surtout un mécanisme qui
   **tolère** une visibilité HOM basse au lieu de l'exiger haute, là où l'erreur Z vaut exactement
   `(1 − V)/4`. C'est un **dispositif**, donc un effet physique, donc hors de l'exclusion de
   l'art. 52 CBE qui a tué `P-18`. Et rien de ce que j'ai lu aujourd'hui ne le touche.

Mon avis, demandé ou non : faire `P-15` d'abord parce qu'il coûte une heure, puis `P-17` parce que
c'est le seul endroit du carnet où nous aurions à la fois un effet physique et une question que
personne n'a encore refermée.

Et les quatre décisions en attente depuis le 2026-09-28 restent entières : `empire-codex`, les 29
fiches au périmètre Caelum (`E-35`), la règle R9 (`E-36`), et la question qui décide du reste —
l'accès à un banc de photonique quantique, que je prépare et ne solliciterai pas.
