import csv
import mysql.connector as con 

# Connexion à la base de données MySQL
db = con.connect(host="localhost", user="root", password="", db="addcar") 


# Ouverture du fichier CSV--Voiture
with open('Voiture.csv', 'r') as file:
    # Lecture des données CSV
    reader = csv.reader(file,delimiter=';')
    

    # Création du curseur pour exécuter les requêtes SQL
    cursor = db.cursor()

    # Suppression de toutes les lignes de la table "voiture"
    cursor.execute("TRUNCATE TABLE voiture")

    # Parcours de chaque ligne du fichier CSV et insertion des données dans la table MySQL
    for row in reader:

        query = "INSERT IGNORE INTO voiture (matricule, marque, couleur, etat, date, prix) VALUES (%s, %s, %s,%s, %s, %s)"

        # Vérification que le nombre de colonnes dans le fichier CSV correspond au nombre de marqueurs de positionnement
        if len(row) == 6:
            # Conversion des valeurs de type str en type int si nécessaire
            row = [int(x) if x.isdigit() else x for x in row]
            cursor.execute(query, row)
            # Validation de la transaction
            db.commit()
        else:
            print("Erreur: le nombre de colonnes dans le fichier CSV ne correspond pas au nombre de colonnes dans la table MySQL")

        # Ouverture du fichier CSV--Client----------------------------------------------------------------------------------
with open('Client.csv', 'r') as file:
    # Lecture des données CSV
    reader = csv.reader(file,delimiter=';')
    # Ignorer l'en-tête du fichier CSV

    # Création du curseur pour exécuter les requêtes SQL
    cursor = db.cursor()

    # Suppression de toutes les lignes de la table "voiture"
    cursor.execute("TRUNCATE TABLE client")

    # Parcours de chaque ligne du fichier CSV et insertion des données dans la table MySQL
    for row in reader:
        query = "INSERT INTO client (cin,nom,prenom,age,adresse,mail,tel) VALUES (%s, %s, %s,%s, %s, %s, %s)"

        # Vérification que le nombre de colonnes dans le fichier CSV correspond au nombre de marqueurs de positionnement
        if len(row) == 7:
            # Conversion des valeurs de type str en type int si nécessaire
            row = [int(x) if x.isdigit() else x for x in row]
            cursor.execute(query, row)
            # Validation de la transaction
            db.commit()
        else:
            print("Erreur1: le nombre de colonnes dans le fichier CSV ne correspond pas au nombre de colonnes dans la table MySQL") 
     
     # Ouverture du fichier CSV--Location------------------------------------------------------------------------------------
with open('Location.csv', 'r') as file:
    # Lecture des données CSV
    reader = csv.reader(file,delimiter=';')
    
    # Création du curseur pour exécuter les requêtes SQL
    cursor = db.cursor()

    # Suppression de toutes les lignes de la table "voiture"
    cursor.execute("TRUNCATE TABLE location")

    # Parcours de chaque ligne du fichier CSV et insertion des données dans la table MySQL
    for row in reader:
        query = "INSERT INTO location (numero,cin,matricule,date,duree,montant) VALUES (%s, %s, %s,%s, %s, %s)"

        # Vérification que le nombre de colonnes dans le fichier CSV correspond au nombre de marqueurs de positionnement
        if len(row) == 6:
            # Conversion des valeurs de type str en type int si nécessaire
            row = [int(x) if x.isdigit() else x for x in row]
            cursor.execute(query, row)
            # Validation de la transaction
            db.commit()
        else:
            print("Erreur2: le nombre de colonnes dans le fichier CSV ne correspond pas au nombre de colonnes dans la table MySQL")           

    # Fermeture du curseur et de la connexion à la base de données MySQL
    cursor.close()
    db.close()
