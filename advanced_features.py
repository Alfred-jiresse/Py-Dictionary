import random

def mot_aleatoire(dictionnaire):
    if not dictionnaire:
        return None, None
    mot = random.choice(list(dictionnaire.keys()))
    return mot, dictionnaire[mot]

def mots_les_plus_consultes(compteur):
    return sorted(compteur.items(), key=lambda x: x[1], reverse=True)
