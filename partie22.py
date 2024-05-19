import json

def ecrireDonneesJson(nomFichier, listeObjDonneesGeo):
    liste_dictionnaires = [obj.__dict__ for obj in listeObjDonneesGeo]
    with open(nomFichier, mode='w', encoding='utf-8') as file:
        json.dump(liste_dictionnaires, file, indent=4)
    print("Données sauvegardées dans", nomFichier)
