import random
from Core_Dictionary import ajouter_mot, lister_mots, modifier_definition, mots_commencant_par, obtenir_definition, mots_contenant, rechercher_dans_definitions, statistiques_consultation, suggerer_mots_similaires, supprimer_mot
from export_bonus import exporter_vers_csv, exporter_vers_txt, jouer_au_jeu, mot_aleatoire
from Data_storage import charger, sauvegarder
from advanced_features import mot_aleatoire, mots_les_plus_consultes


def principal():
    fichier_dictionnaire = 'dictionnaire.json'
    dictionnaire, compteur = charger(fichier_dictionnaire)

    mot, definition = mot_aleatoire(dictionnaire)
    if mot:
        print(f"Mot du jour : {mot} → {definition}\n")

    while True:
        print("\n1. Rechercher un mot\n2. Ajouter un mot\n3. Modifier une définition")
        print("4. Supprimer un mot\n5. Lister les mots\n6. Statistiques")
        print("7. Rechercher par mot-clé\n8. Rechercher par lettre\n9. Rechercher par séquence")
        print("10. Suggestions de mots\n11. Exporter\n12. Jeu\n0. Quitter")
        choix = input("Votre choix : ")

        if choix == '1':
            mot = input("Mot à rechercher : ")
            definition = obtenir_definition(dictionnaire, compteur, mot)
            print(definition if definition else "Mot non trouvé.")

        elif choix == '2':
            mot = input("Nouveau mot : ")
            definition = input("Définition : ")
            if ajouter_mot(dictionnaire, compteur, mot, definition):
                print("Mot ajouté avec succès.")
                sauvegarder(fichier_dictionnaire, dictionnaire, compteur)
            else:
                print("Mot déjà présent.")

        elif choix == '3':
            mot = input("Mot à modifier : ")
            definition = input("Nouvelle définition : ")
            if modifier_definition(dictionnaire, mot, definition):
                print("Définition mise à jour.")
                sauvegarder(fichier_dictionnaire, dictionnaire, compteur)
            else:
                print("Mot introuvable.")

        elif choix == '4':
            mot = input("Mot à supprimer : ")
            if supprimer_mot(dictionnaire, compteur, mot):
                print("Mot supprimé.")
                sauvegarder(fichier_dictionnaire, dictionnaire, compteur)
            else:
                print("Mot introuvable.")

        elif choix == '5':
            for mot in lister_mots(dictionnaire):
                print(mot)

        elif choix == '6':
            stats = statistiques_consultation(dictionnaire, compteur)
            print(stats)

        elif choix == '7':
            mot_cle = input("Mot-clé à rechercher : ")
            print(rechercher_dans_definitions(dictionnaire, mot_cle))

        elif choix == '8':
            lettre = input("Lettre initiale : ")
            print(mots_commencant_par(dictionnaire, lettre))

        elif choix == '9':
            sequence = input("Séquence à chercher : ")
            print(mots_contenant(dictionnaire, sequence))

        elif choix == '10':
            mot = input("Mot mal orthographié : ")
            print(suggerer_mots_similaires(dictionnaire, mot))

        elif choix == '11':
            if exporter_vers_txt(dictionnaire, 'dictionnaire.txt'):
                print("Export TXT réussi.")
            if exporter_vers_csv(dictionnaire, 'dictionnaire.csv'):
                print("Export CSV réussi.")

        elif choix == '12':
            jouer_au_jeu(dictionnaire)

        elif choix == '0':
            break


if __name__ == '__main__':
    principal()
