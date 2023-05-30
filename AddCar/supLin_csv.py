import csv

# Ouvrir le fichier CSV en mode lecture et lecture/écriture
with open('Location.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    lignes = list(reader)

with open('Location.csv', mode='w', newline='') as file:
    
    # Supprimer la deuxième ligne de la liste de lignes existantes
    ligne_supprimee = lignes.pop(0)
    
    # Réécrire toutes les lignes, sauf la ligne supprimée, dans le fichier
    writer = csv.writer(file)
    writer.writerows(lignes)

# Fermer le fichier
file.close()
