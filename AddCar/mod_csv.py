import csv

# Ouvrir le fichier CSV en mode lecture et lecture/écriture
with open('Location.csv', mode='r', newline='') as file:
    reader = csv.reader(file,delimiter=';')
    lignes_existantes = list(reader)

with open('Location.csv', mode='w', newline='') as file:
    
    
    # Créer une liste contenant les valeurs de la nouvelle ligne à insérer
    nouvelle_ligne = ['numero','cin','matricule','date','duree','montant']
    
    # Insérer la nouvelle ligne au début de la liste de lignes existantes
    lignes_existantes.insert(0, nouvelle_ligne)
    
    # Réécrire toutes les lignes, y compris la nouvelle ligne insérée, dans le fichier
    writer = csv.writer(file,delimiter=';')
    writer.writerows(lignes_existantes)

# Fermer le fichier
file.close()
