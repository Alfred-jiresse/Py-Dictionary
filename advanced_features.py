import random

# Tirage aléatoire d’un mot dans le dictionnaire
def mot_aleatoire(dictionnaire):
    """
    Sélectionne un mot et sa définition au hasard depuis le dictionnaire.
    
    Paramètre :
        dictionnaire (dict) : Dictionnaire contenant les mots et définitions.
        
    Retourne :
        tuple : (mot, définition) choisis aléatoirement.
                Si le dictionnaire est vide, retourne (None, None).
    """
    if not dictionnaire:
        return None, None  # Si le dictionnaire est vide, on retourne rien
    mot = random.choice(list(dictionnaire.keys()))  # Choisit un mot au hasard
    return mot, dictionnaire[mot]  # Retourne le mot et sa définition

# Tri des mots les plus consultés 
def mots_les_plus_consultes(compteur):
    """
    Trie les mots selon le nombre de consultations décroissant.
    
    Paramètre :
        compteur (dict) : Dictionnaire contenant les mots et leur nombre de consultations.
        
    Retourne :
        list : Liste de tuples (mot, nombre) triée par nombre décroissant.
    """
    return sorted(compteur.items(), key=lambda x: x[1], reverse=True)  # Tri du plus consulté au moins consulté
