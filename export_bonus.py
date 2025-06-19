import csv
import random
from advanced_features import mot_aleatoire

def exporter_vers_txt(dictionnaire, chemin):
    try:
        with open(chemin, 'w', encoding='utf-8') as f:
            for mot, definition in dictionnaire.items():
                f.write(f"{mot} : {definition}\n")
        return True
    except Exception as e:
        print(f"Erreur lors de l'export TXT : {e}")
        return False

def exporter_vers_csv(dictionnaire, chemin):
    try:
        with open(chemin, 'w', newline='', encoding='utf-8') as fichier_csv:
            writer = csv.writer(fichier_csv)
            writer.writerow(["Mot", "Définition"])
            for mot, definition in dictionnaire.items():
                writer.writerow([mot, definition])
        return True
    except Exception as e:
        print(f"Erreur lors de l'export CSV : {e}")
        return False

# --- Jeu de devinettes ---
def jouer_au_jeu(dictionnaire):
    if not dictionnaire:
        print("Dictionnaire vide !")
        return
    mot, definition = mot_aleatoire(dictionnaire)
    print(f"Définition : {definition}")
    tentative = input("Quel est ce mot ? ")
    if tentative.lower() == mot.lower():
        print("Bravo !")
    else:
        print(f"Raté. C’était : {mot}")