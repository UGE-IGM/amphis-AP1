def sauvegarde(pseudos, nom_fichier):
    with open(nom_fichier, "w") as f:
        for pseudo in pseudos:
            f.write(pseudo)
            f.write("\n")


liste_pseudos = ["Johnny86", "f332", "louri_briffiant", "draco"]
sauvegarde(liste_pseudos, "save/pseudos.txt")