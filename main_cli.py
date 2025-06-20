import sys
import dictionnaire 
import statistiques

def afficher_menu():
    print("\n--- Menu Principal ---")
    print("1. Rechercher un mot")
    print("2. Voir les statistiques")
    print("3. Quitter")

def recherche_mot():
    mot = input("Entrez un mot à rechercher : ").strip()
    if not mot:
        print("Erreur : Aucun mot saisi.")
        return
    definition = dictionnaire.get_definition(mot)
    if definition:
        print(f"Définition de {mot} : {definition}")
    else:
        print(f"Aucune définition trouvée pour '{mot}'.")

def voir_statistiques():
    stats = statistiques.generer_stats()
    print("\n--- Statistiques ---")
    for cle, valeur in stats.items():
        print(f"{cle} : {valeur}")

def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()
        
        if choix == '1':
            recherche_mot()
        elif choix == '2':
            voir_statistiques()
        elif choix == '3':
            print("Fermeture du programme.")
            sys.exit(0)
        else:
            print("Entrée invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
