# Py-Dictionary
#  Py_Dictionary – Projet Collaboratif

Un dictionnaire de mots interactif en Python, avec stockage JSON, interface CLI et fonctionnalités avancées.

##  Objectif

Créer une application CLI permettant :
- de gérer un dictionnaire (ajout, suppression, modif, recherche),
- d’effectuer des recherches avancées (mot-clé, début/fin, suggestions…),
- de proposer un mini-jeu de devinettes,
- et de sauvegarder/exporter les données (.json, .txt, .csv).

##  Architecture du projet

| Module | Fichier | Rôle |
|--------|---------|------|
| 1 | `dictionary_core.py` | Logique en mémoire du dictionnaire |
| 2 | `data_storage.py` | Lecture/écriture JSON |
| 3 | `advanced_features.py` | Statistiques et recherches complexes |
| 4 | `export_bonus.py` | Exportation, catégories, mini-jeu |
| 5 | `main_cli.py` | Interface en ligne de commande (menu) |

## Comment contribuer ?

1. **Fork** ce dépôt (bouton en haut à droite)
2. **Clone** ton fork :
   ```bash
   git clone https://github.com/ton-pseudo/py_dictionary.git
