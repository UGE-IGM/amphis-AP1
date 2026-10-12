grille = [["X", " ", "O"],
          [" ", " ", " "],
          ["X", "O", " "]]

# Chercher un alignement gagnant
# -> Soit une liste est remplie seulement du même élément
# -> Soit il y a une diagonale
# -> Soit une colonne est remplie du même élément

# Tester si une case est remplie
# Et remplir une case

def est_une_ligne_gagnante(ligne):
    # Si la ligne est de taille 3 et qu'on le sait :
    # return ligne[0] == ligne[1] == ligne[2]
    # Sinon :
    for elem in ligne:
        if elem != elem[0] or elem == " ":
            return False
    return True

def contient_une_ligne_gagnante(matrice):
    for ligne in matrice:
        if est_une_ligne_gagnante(ligne):
            return True
    return False