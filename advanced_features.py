import random #mportation de la bibliotheque random pour choisir un mot aleatoire dans le dictinnaire

#definition de la fonction de recherche de mots-cles il retoune les mots dont la definiton contient le mot-cles donnee
def recherche(dictinnaire,mot_cle):
    resultat = []
    for mot,infos in dictinnaire.items(): #parcours chaque mot et ses informations
        if mot_cle.lower() in infos["definition"].lower: #recherche insensible a la casse
            resultat.append(mot)
    return resultat

def mot_par_lettre(dictionnaire, lettre):
    lettre = lettre.lower()
    return sorted([mot for mot in dictionnaire if
                   mot.lower().startswith(lettre)])
#definition de la fonction
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
#definiton  de la fontion de l'incrementation        
def incrementer(dictionnaire,mot):
    if  mot in dictionnaire:
        dictionnaire[mot]["consultations"]+= 1 
#definition de la fonction pour la recherche de mots le plus consultes      
def mots_plus_consultes(dictinnaire,nombre=5):
    mots_tries = sorted(dictinnaire.items(), key = lambda x:
        x[1]["consultations"], reverse=True)
    return mots_tries[:nombre]
'''------------------PARTIE_TESTE-------------------'''
