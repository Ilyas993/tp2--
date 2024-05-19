import csv
import json
import math

# Classe pour représenter les données géographiques
class DonneesGeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return f"Ville: {self.ville}, Pays: {self.pays}, Latitude: {self.latitude}, Longitude: {self.longitude}"

# Fonction pour lire les données d'un fichier CSV et les retourner sous forme de liste d'objets DonneesGeo
def lireDonneesCsv(nomFichier):
    donnees = []
    with open(nomFichier, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            donnees.append(DonneesGeo(row['Ville'], row['Pays'], row['Latitude'], row['Longitude']))
    return donnees

# Fonction pour afficher les données géographiques à l'écran
def afficherDonnees(donnees_geo):
    print("Ville, Pays, Latitude, Longitude")
    for donnee in donnees_geo:
        print(donnee)
    input("Appuyez sur une touche pour continuer...")

# Fonction pour sauvegarder les données géographiques dans un fichier JSON
def ecrireDonneesJson(nomFichier, listeObjDonneesGeo):
    liste_dictionnaires = [obj.__dict__ for obj in listeObjDonneesGeo]
    with open(nomFichier, mode='w', encoding='utf-8') as file:
        json.dump(liste_dictionnaires, file, indent=4)
    print("Données sauvegardées dans", nomFichier)

# Fonction pour calculer la distance entre deux points géographiques en utilisant la formule de Haversine
def calculer_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon de la Terre en kilomètres
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# Fonction pour trouver la distance minimale entre deux villes à partir d'un fichier JSON et sauvegarder les distances calculées dans un fichier CSV
def trouverDistanceMin(nomFichier):
    with open(nomFichier, mode='r', encoding='utf-8') as file:
        donnees = json.load(file)
        objets_geo = [DonneesGeo(**data) for data in donnees]

    min_distance = float('inf')
    ville1, ville2 = None, None

    distances = []

    # Calculer toutes les distances et trouver la distance minimale
    for i in range(len(objets_geo)):
        for j in range(i + 1, len(objets_geo)):
            distance = calculer_distance(objets_geo[i].latitude, objets_geo[i].longitude, objets_geo[j].latitude,
                                         objets_geo[j].longitude)
            distances.append((objets_geo[i], objets_geo[j], distance))
            if distance < min_distance:
                min_distance = distance
                ville1, ville2 = objets_geo[i], objets_geo[j]

    # Afficher la distance minimale
    if ville1 and ville2:
        print(
            f"Distance minimale en kilomètres entre 2 villes : Ville 1 : {ville1.ville} {ville1.pays} {ville1.latitude} {ville1.longitude} et Ville 2 : {ville2.ville} {ville2.pays} {ville2.latitude} {ville2.longitude} Distance en kilomètres : {min_distance:.2f}")

    # Sauvegarder les distances dans un fichier CSV
    with open('distances.csv', mode='w', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(
            ['Ville1', 'Pays1', 'Latitude1', 'Longitude1', 'Ville2', 'Pays2', 'Latitude2', 'Longitude2', 'Distance'])
        for ville1, ville2, distance in distances:
            csv_writer.writerow(
                [ville1.ville, ville1.pays, ville1.latitude, ville1.longitude, ville2.ville, ville2.pays,
                 ville2.latitude, ville2.longitude, distance])
    print("Distances sauvegardées dans distances.csv")

# Fonction pour afficher le menu principal
def afficher_menu():
    print("\nMenu:")
    print("1- Lire les données du fichier csv, créer les objets et afficher les données.")
    print("2- Sauvegarder les données dans un fichier .json.")
    print(
        "3- Lire les données du fichier .json, déterminer et afficher les données associées à la distance minimale entre deux villes et sauvegarder les calculs dans distances.csv.")
    print("Entrez un numéro pour choisir une option ou appuyez sur 'q' pour quitter :")

# Fonction principale pour exécuter le programme
def main():
    donnees_geo = []
    choix1_fait = False  # Variable pour vérifier si le choix 1 a été fait
    choix2_fait = False  # Variable pour vérifier si le choix 2 a été fait
    continuer = True
    while continuer:
        afficher_menu()
        choix = input("Votre choix : ")
        if choix == '1':
            # Lire les données du fichier CSV et les afficher
            donnees_geo = lireDonneesCsv('Donnees.csv')
            afficherDonnees(donnees_geo)
            choix1_fait = True
        elif choix == '2':
            if not choix1_fait:
                # Vérifier si le choix 1 a été fait avant d'exécuter le choix 2
                print("Veuillez lire les données du fichier CSV (choix 1) avant de sauvegarder dans un fichier JSON.")
            else:
                # Sauvegarder les données dans un fichier JSON
                ecrireDonneesJson('donnees.json', donnees_geo)
                choix2_fait = True
        elif choix == '3':
            if not choix2_fait:
                # Vérifier si le choix 2 a été fait avant d'exécuter le choix 3
                print("Veuillez sauvegarder les données dans un fichier JSON (choix 2) avant de calculer la distance minimale.")
            else:
                # Trouver la distance minimale entre deux villes et sauvegarder les calculs dans un fichier CSV
                trouverDistanceMin('donnees.json')
        elif choix.lower() == 'q':
            # Quitter le programme
            continuer = False
        else:
            print("Choix invalide, veuillez réessayer.")

# Point d'entrée du programme
if __name__ == "__main__":
    main()
