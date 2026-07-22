def recupere_sauvegarde(nom_fichier):
    with open(nom_fichier, "r") as f:
        return f.read()
    

contenu = recupere_sauvegarde("save/ecrire_fichier.txt")
print(contenu)
