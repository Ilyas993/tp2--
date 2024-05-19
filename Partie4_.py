def trouverDistanceMin(nomFichier):
    with open(nomFichier, mode='r', encoding='utf-8') as file:
        donnees = json.load(file)
        objets_geo = [DonneesGeo(**data) for data in donnees]

    min_distance = float('inf')
    ville1, ville2 = None, None

    distances = []

    for i in range(len(objets_geo)):
        for j in range(i + 1, len(objets_geo)):
            distance = calculer_distance(objets_geo[i].latitude, objets_geo[i].longitude, objets_geo[j].latitude,
                                         objets_geo[j].longitude)
            distances.append((objets_geo[i], objets_geo[j], distance))
            if distance < min_distance:
                min_distance = distance
                ville1, ville2 = objets_geo[i], objets_geo[j]

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