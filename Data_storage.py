import json
import os

# --- Fonction de sauvegarde du dictionnaire ---
def sauvegarder(chemin, dictionnaire, compteur_consultation):
    """
    Sauvegarde le dictionnaire et le compteur de consultation dans un fichier JSON.
    
    Paramètres :
        chemin (str) : Chemin du fichier où sauvegarder les données.
        dictionnaire (dict) : Dictionnaire des mots et définitions.
        compteur_consultation (dict) : Compteur d'accès pour chaque mot.
    
    Retourne :
        bool : True si la sauvegarde a réussi, False en cas d'erreur.
    """
    try:
        with open(chemin, 'w', encoding='utf-8') as f:
            # On enregistre les deux dictionnaires dans un seul objet JSON
            json.dump({
                "dictionnaire": dictionnaire,
                "compteur": compteur_consultation
            }, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        # Affiche une erreur en cas d’échec de l’écriture
        print(f"Erreur lors de la sauvegarde : {e}")
        return False

# --- Fonction de chargement du dictionnaire ---
def charger(chemin):
    """
    Charge un dictionnaire et son compteur de consultation depuis un fichier JSON.
    
    Paramètre :
        chemin (str) : Chemin du fichier JSON à lire.
        
    Retourne :
        tuple : (dictionnaire, compteur_consultation)
                dictionnaire vide si le fichier n'existe pas ou en cas d'erreur.
    """
    if not os.path.exists(chemin):
        # Si le fichier n'existe pas, on retourne des dictionnaires vides
        return {}, {}
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            contenu = json.load(f)
            dictionnaire = contenu.get("dictionnaire", {})
            compteur = contenu.get("compteur", {})
            return dictionnaire, compteur
    except Exception as e:
        # En cas d’erreur de lecture ou de parsing JSON
        print(f"Erreur lors du chargement : {e}")
        return {}, {}
