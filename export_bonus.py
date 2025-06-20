import csv
import random
from advanced_features import mot_aleatoire  # Importe la fonction de tirage aléatoire d'un mot depuis un module externe

# --- Exportation du dictionnaire dans un fichier texte ---
def exporter_vers_txt(dictionnaire, chemin):
    """
    Exporte le contenu du dictionnaire dans un fichier .txt.
    
    Paramètres :
        dictionnaire (dict) : Dictionnaire contenant les mots et définitions.
        chemin (str) : Chemin du fichier texte où écrire les données.
        
    Retourne :
        bool : True si l’export a réussi, False sinon.
    """
    try:
        with open(chemin, 'w', encoding='utf-8') as f:
            for mot, definition in dictionnaire.items():
                f.write(f"{mot} : {definition}\n")  # Écrit chaque mot suivi de sa définition
        return True
    except Exception as e:
        print(f"Erreur lors de l'export TXT : {e}")
        return False

# --- Exportation du dictionnaire dans un fichier CSV ---
def exporter_vers_csv(dictionnaire, chemin):
    """
    Exporte le contenu du dictionnaire dans un fichier .csv.
    
    Paramètres :
        dictionnaire (dict) : Dictionnaire contenant les mots et définitions.
        chemin (str) : Chemin du fichier CSV où enregistrer les données.
        
    Retourne :
        bool : True si l’export a réussi, False sinon.
    """
    try:
        with open(chemin, 'w', newline='', encoding='utf-8') as fichier_csv:
            writer = csv.writer(fichier_csv)
            writer.writerow(["Mot", "Définition"])  # En-tête du fichier CSV
            for mot, definition in dictionnaire.items():
                writer.writerow([mot, definition])  # Écrit chaque ligne avec mot et définition
        return True
    except Exception as e:
        print(f"Erreur lors de l'export CSV : {e}")
        return False

# --- Jeu de devinettes basé sur les définitions ---
def jouer_au_jeu(dictionnaire):
    """
    Lance un petit jeu où l'utilisateur doit deviner un mot à partir de sa définition.
    
    Paramètre :
        dictionnaire (dict) : Dictionnaire de mots pour jouer.
    """
    if not dictionnaire:
        print("Dictionnaire vide !")
        return
    
    mot, definition = mot_aleatoire(dictionnaire)  # Sélectionne un mot et sa définition au hasard
    print(f"Définition : {definition}")
    tentative = input("Quel est ce mot ? ")  # Demande à l'utilisateur de deviner le mot
    
    if tentative.lower() == mot.lower():
        print("Bravo !")  # Bonne réponse
    else:
        print(f"Raté. C’était : {mot}")  # Mauvaise réponse, on donne la bonne
