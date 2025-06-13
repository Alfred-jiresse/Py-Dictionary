import random  # Pour choisir un mot aléatoire dans le dictionnaire

# 1. Recherche par mot-clé dans les définitions
def rechercher_par_mot_cle(dictionnaire, mot_cle):
    """
    Trouve et retourne les mots don't la définition contient le mot-clé donné.
    """
    resultat = []
    for mot, infos in dictionnaire.items():  # Parcours chaque mot et ses informations
        if mot_cle.lower() in infos["definition"].lower():  # Recherche insensible à la casse
            resultat.append(mot)  # Ajoute le mot si le mot-clé est trouvé dans la définition
    return resultat

# 2. Recherche de mots commençant par une lettre
def mots_par_lettre(dictionnaire, lettre):
    """
    Retourne la liste des mots qui commencent par une lettre donnée.
    """
    lettre = lettre.lower()  # Mise en minuscule pour comparaison
    return sorted([mot for mot in dictionnaire if mot.lower().startswith(lettre)])  # Trie alphabétique

# 3. Recherche de mots contenant une séquence de lettres
def mots_par_sequence(dictionnaire, sequence):
    """
    Retourne les mots contenant une séquence de lettres spécifique.
    """
    sequence = sequence.lower()
    return sorted([mot for mot in dictionnaire if sequence in mot.lower()])  # Cherche dans chaque mot

# 4. Statistiques sur le dictionnaire
def statistiques(dictionnaire):
    """
    Calcule et retourne :
    - le nombre total de mots
    - le mot le plus long
    - le mot le plus court
    - un mot aléatoire avec sa définition
    """
    mots = list(dictionnaire.keys())  # Liste de tous les mots

    if not mots:  # Si le dictionnaire est vide
        return {
            "total": 0,
            "mot_plus_long": "",
            "mot_plus_court": "",
            "mot_aleatoire": ("", "")
        }

    mot_plus_long = max(mots, key=len)  # Mot avec le plus grand nombre de caractères
    mot_plus_court = min(mots, key=len)  # Mot avec le moins de caractères
    mot_aleatoire = random.choice(mots)  # Sélectionne un mot au hasard
    definition_aleatoire = dictionnaire[mot_aleatoire]["definition"]  # Sa définition

    return {
        "total": len(mots),
        "mot_plus_long": mot_plus_long,
        "mot_plus_court": mot_plus_court,
        "mot_aleatoire": (mot_aleatoire, definition_aleatoire)
    }

# 5. Incrémenter les consultations d’un mot
def incrementer_consultation(dictionnaire, mot):
    """
    Incrémente le compteur de consultation d'un mot existant.
    """
    if mot in dictionnaire:
        dictionnaire[mot]["consultations"] += 1  # Augmente de 1 à chaque appel

# 6. Afficher les mots les plus consultés
def mots_plus_consultes(dictionnaire, nombre=5):
    """
    Retourne les mots les plus consultés (par défaut : 5 premiers).
    Trie les mots par le nombre de consultations décroissant.
    """
    mots_tries = sorted(
        dictionnaire.items(),
        key=lambda x: x[1]["consultations"],
        reverse=True
    )
    return mots_tries[:nombre]  # Retourne les ‘nombre’ premiers

'''------------------PARTIE_TESTE-------------------'''
# Ce bloc ne s’exécute que si le fichier est lancé directement (et pas importé dans un autre fichier)
if __name__ == "__main__":
    # Petit dictionnaire d’exemple pour tester
    dictionnaire = {
        "python": {
            "definition": "Langage de programmation moderne.",
            "consultations": 3
        },
        "algorithme": {
            "definition": "Suite d'instructions pour résoudre un problème.",
            "consultations": 7
        },
        "dictionnaire": {
            "definition": "Structure de données permettant de stocker des paires clé-valeur.",
            "consultations": 2
        }
    }