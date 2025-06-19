import json
import os

def sauvegarder(chemin, dictionnaire, compteur_consultation):
    try:
        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump({"dictionnaire": dictionnaire, "compteur": compteur_consultation}, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")
        return False

def charger(chemin):
    if not os.path.exists(chemin):
        return {}, {}
    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            contenu = json.load(f)
            dictionnaire = contenu.get("dictionnaire", {})
            compteur = contenu.get("compteur", {})
            return dictionnaire, compteur
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return {}, {}