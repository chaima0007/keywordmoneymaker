# Chaîne physique — méthode

Engendrée le 2026-10-01 sur demande de Chaima : « crée des agents physiciens et agents qui
pourraient trouver des solutions ». Huit rôles, engendrés par
`scripts/engendrer_physiciens.py` — le socle est **extrait** de `.claude/agents/contradicteur.md`,
jamais recopié, parce qu'une copie diverge et qu'une extraction non.

**Au service de la consigne n°1** en vigueur (`codex/CONSIGNE-N1.md`), route 1 proposée le
2026-09-28 après la mort de `X-06`.

---

## 1. Ce que cette chaîne est, et ce qu'elle n'est pas

**Elle n'est pas un laboratoire.** Aucun des huit rôles ne mesure quoi que ce soit : pas de source
de photons, pas de détecteur, pas de cryostat. Ils lisent de la littérature publiée et ils font
tourner des simulateurs. Toute sortie porte **SIMULÉ** ou **LU**, jamais MESURÉ.

Ce n'est pas une précaution de style. La fiche `E-36`, écrite le 2026-09-28, documente une inférence
non mesurée présentée comme un constat : elle a coûté un virage de domaine entier. Un agent dont le
nom contient le mot « physicien » est précisément celui qui risque de l'oublier, et chaque fiche
porte donc l'avertissement **à l'endroit où l'agent décide**, pas en préambule.

**Ce qu'elle est.** Quatre lecteurs spécialisés, un proposeur, un calculateur, un réfuteur, et un
préparateur de dossier pour un humain qui, lui, mesurera.

---

## 2. Les huit rôles

### Les quatre physiciens — un par problème ouvert

| rôle | problème | ce qu'il tient |
|---|---|---|
| `physicien-pertes-photoniques` | `P-15` | seuils LPPT, effacements, scraps, les limites 29,3 % / 38,2 % / 50 % |
| `physicien-fusion-et-boosting` | `P-16` | le compromis `p_fail = 1/2^n` contre `2n − 2` photons exposés |
| `physicien-etats-ressources` | `P-17` | émetteurs, SPDC, lignes à retard, erreur Z au taux `(1 − V)/4` |
| `physicien-flow-et-erreurs-de-fusion` | `P-19` | conditions de flow, préparation et mesure entremêlées |

Ils n'écrivent que des problèmes et des lectures. **Aucun ne propose de solution** — c'est la règle
des carnets, appliquée aux agents : dès qu'un carnet propose, il contamine le croisement.

### Les quatre rôles de solution

| rôle | pouvoir exclusif | interdiction |
|---|---|---|
| `chercheur-de-solutions` | **le seul qui PROPOSE** | n'écrit jamais dans un carnet, ne produit aucun chiffre, ne se valide pas |
| `calculateur-quantique` | **le seul qui produit des CHIFFRES** | ne propose pas, ne juge pas si un résultat est bon |
| `refutateur-physique` | **le seul qui RÉFUTE** | ne propose jamais de variante qui sauverait l'idée |
| `liaison-physicien-humain` | prépare le dossier pour un humain | **ne contacte personne, jamais** (§10) |

---

## 3. La séparation des pouvoirs, et pourquoi elle tient tout

Celui qui propose n'est jamais celui qui vérifie. C'est la propriété d'indépendance que `X-04` a
trouvée **déjà formalisée** dans la littérature (Chauhan, *Ratification by Re-execution*, 2026 :
le vérificateur exécute lui-même et publie son verdict **avant** de lire l'auto-vérification de
l'autre). Nous l'appliquons parce qu'elle est juste, pas parce qu'elle serait nôtre — et c'est
précisément pour cela qu'elle n'est pas brevetable, ce qui est sans importance ici.

Trois conséquences pratiques :

- `chercheur-de-solutions` ne peut pas écrire « vérifié ». Le seul statut qu'un agent peut poser
  est **PROPOSÉ** (§13).
- `calculateur-quantique` ne peut pas écrire « donc ça marche ». Il dit ce que le chiffre vaut, et
  sous quel modèle de bruit — nommé.
- `refutateur-physique` ne peut pas écrire « validé ». Son meilleur résultat possible est : « je
  n'ai pas trouvé de réfutation, voici les trois endroits où j'ai cherché. »

---

## 4. Le passage de main, et son format

```
PROBLÈME (physicien)  →  HYPOTHÈSE (chercheur)  →  CHIFFRE (calculateur)  →  RÉFUTATION (réfuteur)
                                      ↑                                              │
                                      └──────────── retour si réfuté ────────────────┘
                                                              │
                                                    si mesure nécessaire
                                                              ↓
                                                  liaison-physicien-humain  →  CHAIMA
```

Une hypothèse transmise sans ces cinq champs est refusée, et le refus n'est pas négociable :

1. **le problème visé**, par son identifiant seul ;
2. **l'hypothèse** en une phrase disant ce qui change *physiquement* — pas « optimiser » ;
3. **le test de mort** : ce qui, s'il est vrai, la tue. Une hypothèse sans test de mort est un
   souhait ;
4. **le coût en photons** : ajoute, neutre, ou retire. S'il ajoute, au premier paragraphe ;
5. **pourquoi ce n'est pas déjà fait**, avec les références lues — **y compris les références de la
   phrase où l'on a cru voir un trou**. `X-06` est mort parce que l'outil réputé manquant était en
   référence [22] du paragraphe qui le réclamait.

---

## 5. Les quatre morts les plus fréquentes, que le réfuteur teste dans cet ordre

1. **Le compromis déguisé** — gain sur un axe, paiement sur un autre, et seul le gain est écrit.
   Test : compter les photons ajoutés.
2. **La limite fondamentale** — la proposition dépasse une borne publiée. Soit elle change de
   cadre et le dit, soit elle est fausse.
3. **Le report du problème** — résoudre `P-17` par une ligne à retard plus longue aggrave `P-15`.
   Les cinq problèmes sont **couplés** ; une solution qui ignore le couplage n'en est pas une.
4. **Le chiffre non recoupé** — les chiffres du carnet 4 sont lus dans des articles qui se citent
   entre eux, jamais à la source primaire. PLAUSIBLE, confiance MODÉRÉE.

---

## 6. Ce qui est déjà fermé, et qu'aucun rôle ne doit rouvrir

**`P-18` est mort le 2026-09-28**, et la chaîne doit le savoir pour ne pas y retourner :

- `OptGraphState` (Lee & Jeong, *Quantum* 7, 1212 (2023), **MIT**) calcule déjà le coût en
  ressources en nombre moyen d'états ressources de base ;
- **US12596949B2** (SNU R&DB Foundation, les mêmes auteurs, délivré le 2026-04-07, en vigueur
  jusqu'en 2044) revendique l'algorithme d'optimisation de ressources sur le graphe de combinaison,
  avec un coût par arête qui **intègre le taux de perte** ;
- **art. 52(2) CBE** exclut une métrique sans effet technique.

Ces deux outils sont **utilisables** — ils sont au sas sous `B-21` et `B-22`. Ils ne sont pas
brevetables par nous. Les deux faits cohabitent et aucun n'annule l'autre.

---

## 7. Le garde-fou qui compte le plus

Le dépôt est **public** et **il n'y a pas de délai de grâce en Europe**. Une solution écrite en
clair ici serait une solution dont nous aurions détruit la nouveauté nous-mêmes.

`codex/pistes/REGISTRE-SOLUTIONS.md` reçoit donc **la trace** : qu'une piste existe, quel problème
elle visait, où elle en est. **Jamais son contenu.** Le fond va au coffre Drive, un document par
trouvaille, horodaté, en ajout.

Rappel de l'incident réel du 11/09 : soixante-dix-sept fichiers internes de Caelum exposés pendant
des semaines. `liaison-physicien-humain` est le rôle le plus exposé de la chaîne, parce qu'un
dossier destiné à un tiers contient par construction ce qu'on a trouvé. Il écrit **la question**,
jamais la piste qui l'a suscitée.

---

## 8. Ce que cette chaîne ne résoudra pas

Elle ne trouvera pas de physicien. Elle ne mesurera pas. Elle ne décidera pas si la route 1 vaut son
coût — un accès à un banc de photonique quantique n'est ni gratuit ni rapide, et Chaima est seule.

Ce qu'elle peut faire, et c'est déjà quelque chose : **réduire à presque rien le coût de tuer une
mauvaise idée**, et formuler proprement les trois ou quatre questions qui vaudraient qu'on dérange
un expérimentateur. Le coût réel d'un dispositif de veille ne se mesure pas au nombre de candidats
qu'il produit, mais à la vitesse à laquelle il tue les mauvais.
