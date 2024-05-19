def afficher_menu():
    print("\nMenu:")
    print("1- Lire les données du fichier csv, créer les objets et afficher les données.")
    print("2- Sauvegarder les données dans un fichier .json.")
    print("3- Lire les données du fichier .json, déterminer et afficher les données associées à la distance minimale entre deux villes et sauvegarder les calculs dans distances.csv.")
    print("Entrez un numéro pour choisir une option ou appuyez sur 'q' pour quitter :")

def main():
    donnees_geo = []
    while True:
        afficher_menu()
        choix = input("Votre choix : ")
        if choix == '1':
            donnees_geo = lireDonneesCsv('Donnees.csv')
            afficherDonnees(donnees_geo)
        elif choix == '2':
            if not donnees_geo:
                print("Veuillez lire les données du fichier CSV avant de sauvegarder dans un fichier JSON.")
            else:
                ecrireDonneesJson('donnees.json', donnees_geo)
        elif choix == '3':
            trouverDistanceMin('donnees.json')
        elif choix.lower() == 'q':
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()