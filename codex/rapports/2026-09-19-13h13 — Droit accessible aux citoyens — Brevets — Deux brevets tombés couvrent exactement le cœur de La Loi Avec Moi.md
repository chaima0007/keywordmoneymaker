# Deux brevets tombés couvrent exactement le cœur de La Loi Avec Moi

**Contrôle honnête d'entrée.** Deux choses à dire avant le contenu. D'abord, j'ai annoncé
pendant cinq jours ne pas pouvoir lire de brevets ; c'était faux et trop large, la fiche E-30
le documente — le blocage réel est plus étroit. Ensuite, ce rapport contredit une hypothèse
que nous portions : l'entrée par situation plutôt que par barre de recherche n'est pas une idée
neuve, elle est enseignée dans un brevet dont la priorité remonte à 2000. Aucun document
quasi identique dans `codex/rapports/`. Pas de croque-mort à convoquer.

**Au service de la consigne n°1** en vigueur (`codex/CONSIGNE-N1.md`) : veille technologique et
brevets sur le droit accessible aux citoyens. Première exécution réelle du pipeline décrit dans
`codex/methodes/PIPELINE-BREVETS.md`, étapes 1 à 3.

---

## 1. Ce qui a débloqué ce rapport

L'accès direct aux registres reste refusé — re-testé le 19/09, `connect_rejected` sur
Espacenet et Google Patents, journal de proxy à l'appui. Mais Google Patents répond par
récupération sur serveurs tiers, qui ramène le texte intégral : description, revendications,
et la section arrière-plan où le déposant critique l'art antérieur.

Ce qui reste hors de portée : le Registre EPO (`CRAWL_UNKNOWN_ERROR`) et Espacenet
(`CRAWL_LIVECRAWL_TIMEOUT`), testés le 19/09. Donc lire un brevet, oui ; établir son statut
juridique, non.

## 2. Première trouvaille — US6931394B2, expiré

https://patents.google.com/patent/US6931394B2/en — « Law retrieval system, law retrieval
apparatus and law retrieval program », Tonfu Corporation, priorité 2000-10-31, délivré
2005-08-16. Statut affiché : *Expired - Lifetime, expires 2023-03-18*.

Ce que le brevet enseigne, dans ses propres termes : permettre de retrouver la disposition
applicable **« from a slang word and the like without knowledge of retrieval keywords such as
technical terms on law »**, et **« by a user answering in sequence by making a choice among
adequate choices without inputting many retrieval keywords by himself »**. Trois mécanismes :
une base de méta-mots-clés reliant le mot ordinaire au terme juridique, une base verbe+objet,
et une base de « flux d'aide » — des arbres de questions préconstruits par type de situation.

**C'est mot pour mot la demande de Chaima** : « je veux que chaque citoyen belge trouve ce
qu'il a besoin sans chercher ». Un brevet japonais de 2000 décrit le mécanisme.

## 3. Seconde trouvaille — US10872315B1, déchu pour annuités

https://patents.google.com/patent/US10872315B1/en — « Methods, systems and computer program
products for prioritization of benefit qualification questions », **Intuit Inc.**, priorité
2016-07-27, délivré 2020-12-22. Statut affiché : *Expired - Fee Related, expires 2037-12-12*.

Lire ce statut correctement : l'expiration normale serait 2037. Il est tombé avant, pour
annuités impayées. Ce n'est **pas** la même chose qu'un brevet expiré — un brevet déchu pour
annuités peut être restauré. C'est exactement la distinction que porte le rôle
`eclaireur-brevets-libres`, et voici le premier cas réel qui l'illustre.

Ce que le brevet enseigne : chaque programme d'aide est représenté par un *completeness graph*,
le profil du citoyen est confronté à tous les graphes en parallèle, les graphes impossibles sont
éliminés, puis la question posée ensuite est celle qui **apparaît dans le plus de graphes
restants** — ou, variante revendiquée, celle qui maximise la somme des aides moyennes des
programmes où elle apparaît. Le classement est recalculé à chaque réponse.

C'est l'ossature algorithmique d'un parcours « je décris ma situation, on me dit à quoi j'ai
droit » — avec le nombre minimal de questions.

## 4. Conséquence, et elle n'est pas agréable

Pour **La Loi Avec Moi**, c'est une bonne nouvelle : le mécanisme que nous voulons construire
est enseigné par des brevets tombés, donc l'enseignement est dans le domaine public et ne nous
expose pas. Le risque résiduel pour un logiciel en Europe reste la licence, la marque et le
droit des bases de données — pas le brevet — comme déjà écrit dans
`codex/methodes/VEILLE-RAPIDE-15-JOURS.md`.

Pour l'objectif **offensif** — concevoir des brevets que Chaima pourra vendre ou louer — c'est
au contraire un coup dur, et il faut le dire net : **ce qui est enseigné par ces brevets est de
l'art antérieur**. On ne rebrevette pas un brevet tombé. Si l'invention visée est « entrée par
situation au lieu de barre de recherche », elle est morte à l'article 54 CBE. Si c'est
« ordonner les questions par couverture de programmes », elle est morte aussi.

L'invention, s'il y en a une, est ailleurs. Deux directions ouvertes par la lecture de ces deux
textes, et aucune n'est encore une invention :

1. Les deux brevets supposent le corpus juridique **déjà structuré** en règles exploitables.
   Aucun des deux ne traite l'obtention de cette structure à partir de textes publiés en langue
   naturelle et modifiés en continu. C'est précisément le trou belge relevé le 16/09.
2. Le brevet Intuit optimise le **nombre** de questions. Il ne traite pas le cas où le citoyen
   ne sait pas répondre, répond faux, ou refuse de répondre — alors que c'est le cas dominant
   chez la personne qui ne trouve pas ses droits.

Ces deux pistes vont au coffre Drive, pas ici. Ce dépôt est public.

## 5. Ce qui n'est pas prouvé

Les statuts juridiques cités viennent de Google Patents, qui écrit lui-même sur chaque fiche
que le statut affiché est une supposition et non une conclusion juridique. Ces deux statuts
sont donc PLAUSIBLE, confiance MODÉRÉE, et non CONFIRMÉ. La levée du doute demande le Registre
EPO ou l'USPTO, qui ne répondent pas d'ici.

Je n'ai pas lu les revendications elles-mêmes, seulement la description telle que restituée.
La description est libre d'usage ; la revendication ne l'est pas. Tant que la revendication 1
de chacun n'a pas été lue mot à mot, aucune conclusion de liberté d'exploitation n'est tenable.

Aucune analyse ici n'est un conseil juridique. Un conseil en propriété intellectuelle humain
est requis avant tout dépôt réel.

## 6. Ce que Chaima peut faire, et c'est court

Ouvrir ces deux numéros sur le registre américain et me dire ce qu'affiche le statut officiel :
US6931394 et US10872315. Deux recherches. C'est tout ce qui me manque pour passer ces deux
lignes de PLAUSIBLE à CONFIRMÉ.
