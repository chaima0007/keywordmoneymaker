# Carnet 1 — Capteurs, mesure, traitement du signal

**Ce carnet ne contient que des problèmes, jamais de solutions.** Tenu par `recolteur-problemes`.
Ouvert le 2026-09-19. Ajout uniquement.

Tous les problèmes ci-dessous sont **extraits des sections arrière-plan de brevets publiés**,
c'est-à-dire décrits par les déposants eux-mêmes. Ils sont donc publics. Rappel de méthode : un
défaut décrit par un déposant sert son propre brevet — il est PLAUSIBLE, jamais VÉRIFIÉ, tant
qu'une source indépendante ne le confirme pas.

Statuts juridiques cités : tels qu'affichés par Google Patents, qui écrit lui-même qu'un statut
affiché est une supposition et non une conclusion juridique. Confiance MODÉRÉE. Registre non
atteignable depuis cette session.

---

## P-01 — La dérive de zéro survit à toute calibration d'usine

**Source** US6237394B1, Redwood Microsystems puis SMC, priorité 1999, affiché *Expired - Lifetime*.

Le déposant écrit que les techniques de calibration acceptées compensent bien les variations de
fabrication, mais **échouent quand les contraintes mécaniques du collage évoluent avec le temps**.
Le matériau de fixation flue, la membrane se déforme, le terme d'offset dérive. Chiffres donnés :
un décalage d'environ 0,5 psi, soit 1,25 % d'erreur à 40 psi mais **10 % d'erreur à 5 psi**.

Défaut nommé explicitement : *« It is not practical or acceptable for a customer to re-calibrate a
pressure sensor which has drifted. »* Le problème n'est pas de savoir corriger — c'est que la
correction suppose un retour en atelier que personne ne fera.

## P-02 — L'offset, pas le bruit, limite la dynamique du capteur

**Source** US5426969, priorité ~1993, affiché expiré.

Contre-intuitif et utile : *« additive drift tends to constitute the limiting factor in sensitivity
and dynamic range, rather than noise »*. Autrement dit, tout l'effort classique porté sur le bruit
s'attaque à la mauvaise limite. Et la réponse historique de l'industrie — *« ever more precise
manufacturing processes »*, ajustement laser — fait dépendre la performance finale de la qualité
du procédé de fabrication, donc du coût.

## P-03 — Le canal de référence coûte plus que le capteur

**Source** US5347474, capteur de gaz NDIR, priorité ~1993, affiché expiré.

Le déposant écrit que l'approche classique de la dérive long terme consiste à embarquer un canal
de référence qui mesure la dégradation — *« However, provision of this reference channel increases
the cost and complexity of the sensor. »* Et il précise où ça fait mal : détecteurs d'incendie et
sondes de ventilation, **attendus pour fonctionner des années sans intervention**, où une dérive
non compensée produit des fausses alarmes et une ventilation erratique.

## P-04 — La dérive initiale interdit l'usage juste après la mise en service

**Source** US4701253A, capteur ISFET, Sentron, priorité 1983, affiché *Expired - Fee Related*.

Deux défauts distincts, et le second est plus intéressant que le premier :
- dérive de 0,02 à 0,06 pH/heure en régime établi ;
- **dérive initiale bien plus forte, jusqu'à 0,1–0,2 pH/heure pendant la première heure**, ce qui
  impose une longue période d'attente avant toute mesure exploitable.

Le problème du démarrage est traité comme un sous-cas de la dérive. Il pourrait ne pas en être un.

## P-05 — Calibrer un grand système de capteurs en temps réel est instable ou trop lourd

**Source** US5506794, priorité ~1994, affiché expiré.

Le déposant décrit un choix imposé, sans troisième terme : soit le filtrage de Kalman optimal, dont
les conditions d'observabilité exigent de traiter des lots de mesures si grands qu'ils sont
impraticables en temps réel ; soit des variantes sous-optimales dont **la stabilité n'est pas
garantie** et dont les paramètres estimés peuvent diverger vers de fausses solutions. Il note aussi
que les paramètres de calibration sont **inobservables pendant de nombreux événements externes**.

---

## À chercher ensuite dans ce carnet

- Recherche par codes CPC — impossible d'ici, registres inatteignables. Chaima seule peut l'ouvrir.
- Les revendications n'ont pas été lues mot à mot. Description ≠ revendication.
