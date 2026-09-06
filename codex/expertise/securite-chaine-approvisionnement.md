# EXPERTISE — Sécurité de la chaîne d'approvisionnement logicielle

**Maturité : DÉBUTANT** (2 fiches — seuil CONFIRMÉ à 3)

---

## EXP-001 — Un contrôle de sécurité doit prouver qu'il détecte

**Domaine :** sécurité / CI
**Principe appris :** un scanner qui ne trouve jamais rien est indiscernable d'un scanner cassé.
Avant d'accepter un verdict « vert », lui soumettre un cas piégé volontaire (faux secret, motif
dangereux) et vérifier qu'il vire au rouge, puis au vert après nettoyage. Sans cette preuve de
détection, « aucune anomalie trouvée » ne veut rien dire.
**Source liée :** contrôle mis en place sur le dépôt Caelum, test piégé exécuté le 2026-09-06 (CONFIRMÉ, reproduit).
**Projets où appliqué :** Caelum.
**Fiabilité :** ÉLEVÉE — reproduit localement.
**Dernière confirmation :** 2026-09-06.

---

## EXP-002 — Un audit de dépendances doit viser le projet, pas la machine

**Domaine :** sécurité / dépendances
**Principe appris :** lancé sans cible explicite, un auditeur de vulnérabilités analyse les paquets
préinstallés du serveur d'intégration (paquets système de la distribution) et non ceux du projet.
Le résultat est une longue liste de vulnérabilités réelles mais hors sujet — un bruit qui décrédibilise
le contrôle et masque les vraies alertes. Toujours pointer l'auditeur sur le fichier de verrouillage
du projet.
**Effet observé :** une fois recentré sur le verrou, 635 dépendances réelles analysées et
3 vulnérabilités effectives découvertes dans des dépendances *transitives* — invisibles à l'œil nu.
**Source liée :** journaux d'exécution du 2026-09-06 (runs 1 à 3), dépôt Caelum (CONFIRMÉ).
**Projets où appliqué :** Caelum.
**Fiabilité :** ÉLEVÉE.
**Dernière confirmation :** 2026-09-06.
