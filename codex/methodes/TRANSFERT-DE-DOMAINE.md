# Le transfert de domaine — la méthode que Chaima a nommée sans trouver le mot

Document de méthode. Aucune invention, aucun croisement concret : ceux-là sont au coffre.
Ce dépôt est public.

---

## 1. Pourquoi c'est la bonne méthode, et pas seulement une méthode

Demande de Chaima, 2026-09-19 : mener les trois domaines en parallèle plutôt qu'un seul,
« car ça sera plus simple pour fusionner ». Elle a raison, et la raison est juridique avant
d'être pratique.

**Art. 56 CBE — l'activité inventive.** Une invention est brevetable si elle n'est pas évidente
**pour l'homme du métier**. Or l'homme du métier est défini par son domaine. Le spécialiste des
capteurs connaît la littérature des capteurs ; il ne lit pas les brevets de l'agroalimentaire.
Un enseignement transporté d'un domaine vers un autre domaine **éloigné** est donc, par
construction, moins susceptible d'être jugé évident qu'une amélioration interne à un domaine.

**Conséquence directe :** chercher dans un seul domaine, c'est se condamner à concurrencer les
spécialistes de ce domaine sur leur propre terrain, avec vingt ans de retard sur eux. Croiser
deux domaines, c'est occuper un espace que ni l'un ni l'autre ne surveille.

**Le piège symétrique, et il faut le dire :** « domaine éloigné » n'est pas une formule magique.
Si le transfert est banal — appliquer un filtre connu à un signal connu — l'OEB le jugera évident
quand même. Ce qui tient, c'est le transfert qui suppose d'avoir **reconnu que deux problèmes
décrits avec des mots différents sont le même problème**. C'est exactement le travail que fait
`recolteur-problemes` en classant par problème et non par brevet.

## 2. Les trois chemins ouverts

| Carnet | Domaine | Pourquoi ce domaine |
|---|---|---|
| `codex/pistes/CARNET-01-capteurs-et-signal.md` | Capteurs, mesure, traitement du signal | L'effet technique n'est pas à défendre : il est intrinsèque. C'est la voie la plus sûre pour passer l'art. 52 CBE. |
| `codex/pistes/CARNET-02-energie-et-batiment.md` | Thermique du bâtiment, stockage d'énergie | Effet technique évident. Financements régionaux belges, donc croisement avec le volet capitaux de la chaîne. |
| `codex/pistes/CARNET-03-procedes-et-agroalimentaire.md` | Procédés, transformation, agroalimentaire | Moins ratissé par les géants du logiciel. Tissu industriel belge réel, donc acheteurs ou licenciés de proximité. |

Chaque carnet ne contient que des **problèmes non résolus**, extraits des sections arrière-plan de
brevets publiés, avec numéro et date. Un carnet ne contient jamais de solution : dès qu'un carnet
propose, il contamine le croisement.

## 3. Le croisement, étape par étape

1. **Récolter séparément.** Trois carnets, trois lectures indépendantes. Ne jamais lire le carnet 3
   en cherchant à confirmer une idée née dans le carnet 1 — c'est ainsi qu'on fabrique une
   coïncidence.
2. **Chercher l'identité cachée.** Deux problèmes qui portent des noms différents dans deux
   domaines sont-ils le même problème ? C'est la seule question qui produit du transfert.
3. **Vérifier que l'enseignement source est libre.** Un enseignement tiré d'un brevet **en vigueur**
   n'est pas transférable sans licence. `eclaireur-brevets-libres` répond, et ne conclut jamais
   « libre » sans registre.
4. **Contredire avant d'espérer.** `contradicteur` cherche pourquoi le transfert est banal.
   `avocat` cherche l'antériorité qui le tue. Les deux passent **avant** qu'on s'attache à l'idée.
5. **Chercher l'antériorité, vraiment.** Un croisement non soumis à recherche d'antériorité ne vaut
   rien. C'est l'erreur la plus coûteuse possible : on s'attache, puis on paie, puis on est refusé.
6. **Inscrire au registre, garder le contenu au coffre.**
   `codex/pistes/REGISTRE-CROISEMENTS.md` porte la trace ; le coffre Drive porte le fond.

## 4. La règle qui protège tout le reste

Il n'y a **pas de délai de grâce en Europe**. Ce qui est publié avant le dépôt détruit la nouveauté
de ce qu'on déposerait ensuite. Un croisement écrit dans un dépôt public est un croisement perdu.

Les carnets sont publics parce qu'ils ne contiennent que des problèmes déjà publiés par leurs
propres déposants. Les croisements sont confidentiels parce qu'ils sont, eux, notre travail.

C'est `protecteur` qui tient cette frontière, avec droit de veto, et c'est la leçon de l'incident
du 11/09 : 77 fichiers internes exposés pendant des semaines.
