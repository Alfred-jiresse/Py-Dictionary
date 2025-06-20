# Py-Dictionary

## Description du projet

Py-Dictionary est une application Python en ligne de commande permettant de gérer un dictionnaire personnel.
Elle offre les fonctionnalités suivantes :

* Ajouter, modifier, supprimer des mots et leurs définitions
* Rechercher des mots par mot-clé, lettre ou séquence
* Suggestions de mots similaires
* Statistiques de consultation des mots
* Sauvegarde et chargement des données au format JSON
* Export du dictionnaire en fichiers TXT et CSV
* Jeu de devinettes basé sur les définitions des mots
* Interface interactive en ligne de commande (CLI)

---

## Membres du projet

* Alfred Jiresse (Développeur principal)
* \[Ajouter les noms des autres membres s’il y en a]

---

## Répartition des tâches

| Tâche                           | Responsable            | Statut  |
| ------------------------------- | ---------------------- | ------- |
| Conception et architecture      | Mbala Biselela jiresse | Terminé |
| Expore\_Bonus                   | Masudi Tony Tony       | Terminé |
| Fonctionalité\_Avancer          | Mbaya Katende Djo      | Terminé |
| Interface CLI                   | Mauwa Zakwani Annick   | Terminé |
| Gestion des conflits Git        | Collaboration équipe   | Terminé |
| Documentation                   | Collaboration equipe   | Terminé |

---

## Installation

1. Cloner le dépôt GitHub :

   ```bash
   git clone https://github.com/Alfred-jiresse/Py-Dictionary.git
   cd Py-Dictionary
   ```
## Pour lancer l'application et 
python main_cli.py

## une fois l'application lancer
        ## menu principale
1. Rechercher un mot
2. Ajouter un mot
3. Modifier une définition
4. Supprimer un mot
5. Lister les mots
6. Statistiques
7. Rechercher par mot-clé
8. Rechercher par lettre
9. Rechercher par séquence
10. Suggestions de mots
11. Exporter
12. Jeu
0. Quitter

## Structure du Projet

Py-Dictionary/
│
├── Core_Dictionary.py        # Fonctions principales du dictionnaire
├── Data_storage.py           # Sauvegarde et chargement JSON
├── export_bonus.py           # Export et jeu de devinettes
├── advanced_features.py      # Fonctions avancées (mots aléatoires, stats)
├── main_cli.py               # Interface CLI principale
├── dictionnaire.json         # Fichier de données (créé après utilisation)
└── README.md                 # Documentation du projet


