def obtenir_entree(fichier):
    liste = []
    with open(fichier, "r") as f:
        for line in f:
            liste.append(line.strip("\n"))
    return liste


def simuler_curseur(instructions):
    curseur = 50
    compteur = 0
    for instruction in instructions:
        valeur = int(instruction[1:])
        if instruction[0] == "L":
            curseur = curseur - valeur
        else:
            curseur = curseur + valeur
        curseur = curseur % 100
        if curseur == 0:
            compteur += 1
    return compteur
            
    
instructions = obtenir_entree("input.txt")
compteur = simuler_curseur(instructions)
print(compteur)