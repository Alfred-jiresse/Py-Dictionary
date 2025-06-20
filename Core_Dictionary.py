import re

'''--- fonction pour ajouter un mots---
cette fonction prend en paramettre 4 elements dont entries qui est du type liste
qui va recevoir une listes mot, lookup_counter qui est un contaire qui va nous servir
tout au long de ce projet pour compter les mots, word qui est le mot lui meme et definition qui va stocker sa defnition'''

def ajouter_mot(dictionnaire, compteur_consultation, mot, definition):
    if mot in dictionnaire:
        return False
    dictionnaire[mot] = definition
    compteur_consultation[mot] = 0
    return True

'''fonction pour avoir la definition du mot
cette fonction prend 3 paramettre pour mieux comprendre ce paramettre 
voir le commentaire sur le fonction add_Word'''

def obtenir_definition(dictionnaire, compteur_consultation, mot):
    if mot in dictionnaire:
        compteur_consultation[mot] += 1
        return dictionnaire[mot]
    return None


'''onction pour mettre a jour une definition
elle prend aussi 3 paramettre dont un nouveau que nous n'avons pas encore expliquer 
new_definition comme sont nom l'indique va permettre de recuprere une nouvelle definition du mot'''

def modifier_definition(dictionnaire, mot, nouvelle_definition):
    if mot not in dictionnaire:
        return False
    dictionnaire[mot] = nouvelle_definition
    return True

# fonction permettant de supprimer un mot du dictionnaire

def supprimer_mot(dictionnaire, compteur_consultation, mot):
    if mot in dictionnaire:
        del dictionnaire[mot]
        del compteur_consultation[mot]
        return True
    return False

# fonction pour afficher la liste de mots 

def lister_mots(dictionnaire):
    return sorted(dictionnaire.keys())


# fonction pour chercher une definition dans le dictionnaire

def rechercher_dans_definitions(dictionnaire, mot_cle):
    return [mot for mot, definition in dictionnaire.items()
            if mot_cle.lower() in definition.lower()]

# fonction pour suggerer des motss similaire a l'utilisateur

def suggerer_mots_similaires(dictionnaire, mot, n=3):
    motif = rf".*{re.escape(mot)}.*"
    correspondances = [m for m in dictionnaire.keys() if re.match(motif, m)]
    return correspondances[:n]

# foncttion pour voir le mot le plus consulter

def statistiques_consultation(dictionnaire, compteur_consultation):
    if not compteur_consultation:
        return None
    mot_plus_consulte = max(compteur_consultation, key=compteur_consultation.get)
    return {
        'nombre_total': len(dictionnaire),
        'mot_plus_consulte': mot_plus_consulte,
        'nombre_consultations': compteur_consultation[mot_plus_consulte],
        'mot_le_plus_long': max(dictionnaire, key=len),
        'mot_le_plus_court': min(dictionnaire, key=len),
    }

# fonction pour rechercher le mot commençant par une  (x) lettre

def mots_commencant_par(dictionnaire, lettre):
    return sorted([mot for mot in dictionnaire if mot.startswith(lettre)])

# fonction pour avoir le mot qui contienne une sequence des mots

def mots_contenant(dictionnaire, sequence):
    return sorted([mot for mot in dictionnaire if sequence in mot])
