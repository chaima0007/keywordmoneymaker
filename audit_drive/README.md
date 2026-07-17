# audit_drive/

Sorties **runtime** du protocole d'audit partagé (voir `agents/drive_audit.py`).

- `manifest.jsonl` : une ligne JSON par audit (généré à l'exécution).
- `*.md` : un fichier lisible par audit (généré à l'exécution).

Ces fichiers sont **ignorés par git** : ils sont recréés à chaque exécution et
leur **copie de référence, partagée avec Chaima et les agents, vit sur le Google
Drive** (dossier « 🗂️ Caelum — Journal d'Audit »). Ce README garde le dossier
présent dans le dépôt.

Règle : aucun secret (mot de passe, clé, token) n'est jamais écrit ici.
