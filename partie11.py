import csv


class DonneesGeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return f"Ville: {self.ville}, Pays: {self.pays}, Latitude: {self.latitude}, Longitude: {self.longitude}"


def lireDonneesCsv(nomFichier):
    donnees = []
    with open(nomFichier, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            donnees.append(DonneesGeo(row['Ville'], row['Pays'], row['Latitude'], row['Longitude']))
    return donnees


def afficherDonnees(donnees_geo):
    print("Ville, Pays, Latitude, Longitude")
    for donnee in donnees_geo:
        print(donnee)
    input("Appuyez sur une touche pour continuer...")
