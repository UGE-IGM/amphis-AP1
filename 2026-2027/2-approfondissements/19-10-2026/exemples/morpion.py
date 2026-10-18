grille = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

print(grille[0])
print(grille[1])
print(grille[2])

fini = False
while not fini:
    nligne = int(input("Entrez un numéro de ligne : "))
    ncolonne = int(input("Entrez un numéro de colonne : "))
    
    grille[nligne][ncolonne] = "X"
    
    print(grille[0])
    print(grille[1])
    print(grille[2])

    fini = True
    for ligne in grille:
        for element in ligne:
            if element == " ":
                fini = False
