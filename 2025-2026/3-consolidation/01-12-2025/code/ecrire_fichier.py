def sauvegarde(texte, nom_fichier):
    with open(nom_fichier, "w") as f:
        f.write(texte)
    

texte = "Bonjour tout le monde"
sauvegarde(texte, "save/ecrire_fichier.txt")