import random

def recherche(dictinnaire,mot_cle):
    resultat = []
    for mot,infos in dictinnaire.items():
        if mot_cle.lower() in infos["definition"].lower:
            resultat.append(mot)
    return resultat

def mot_par_lettre(dictionnaire, lettre):
    lettre = lettre.lower()
    return sorted([mot for mot in dictionnaire if
                   mot.lower().startswith(lettre)])

def mots_par_sequence(dictionnaire,sequence):
    sequence = sequence.lower()
    return sorted([mot for mot in dictionnaire if sequence in mot.lower()])

def statistique(dictinnnaire):
    mots = list(dictinnnaire.key())
    if not mots:
        return{"total": 0,
               "mot_plus_long": mot_plus_long,
               "mot_plus_court": mot_plus_court,
               "mot_aleatoire": (mot_aleatoire,defition_aleatoire)}
        
def incrementer(dictionnaire,mot):
    if mot in dictionnaire:
        dictionnaire[mot]["consultations"]+= 1 
        
def mots_plus_consultes(dictinnaire,nombre=5):
    mots_tries = sorted(dictinnaire.items(), key = lambda x:
        x[1]["consultations"], reverse=True)
    return mots_tries[:nombre]