import csv

# Dictionnaire de mots avec catégories
dictionnaire = {
    "animaux": ["serpent", "souris", "lion", "éléphant"],
    "fruits": ["pomme", "banane", "orange", "raisin"],
    "couleurs": ["rouge", "bleu", "vert", "jaune"]
}


def exporter_txt(nom_fichier="dictionnaire.txt"):
    with open(nom_fichier, "w", encoding="utf-8") as f:
        for categorie, mots in dictionnaire.items():
            f.write(f"{categorie}:\n")
            f.write(", ".join(mots) + "\n\n")
    print(f"Dictionnaire exporté en {nom_fichier}")


def exporter_csv(nom_fichier="dictionnaire.csv"):
    with open(nom_fichier, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Catégorie", "Mots"])
        for categorie, mots in dictionnaire.items():
            writer.writerow([categorie, ", ".join(mots)])
    print(f"Dictionnaire exporté en {nom_fichier}")


def filtrer_mots(categorie):
    return dictionnaire.get(categorie, [])


import random

def jeu_devinette():
    categorie = random.choice(list(dictionnaire.keys()))
    mot = random.choice(dictionnaire[categorie])
    print(f"Catégorie: {categorie}")
    essais = 3
    while essais > 0:
        devine = input("Devinez le mot: ")
        if devine.lower() == mot:
            print("Bravo, vous avez trouvé ! ")
            return
        else:
            essais -= 1
            print(f"Incorrect, il vous reste {essais} essai(s).")
    print(f"Dommage, le mot était '{mot}'.")


exporter_txt()
exporter_csv()
print(filtrer_mots("fruits"))
jeu_devinette()
