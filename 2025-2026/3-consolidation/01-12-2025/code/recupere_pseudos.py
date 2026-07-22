def recupere_pseudos(nom_fichier):
    pseudos = []
    with open(nom_fichier, "r") as f:
        for ligne in f:
            pseudo = ligne.strip("\n")
            pseudos.append(pseudo)
    return pseudos


pseudos = recupere_pseudos("save/pseudos.txt")
print(pseudos)
            