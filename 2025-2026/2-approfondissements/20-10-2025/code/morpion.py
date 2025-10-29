# On peut représenter une grille de morpion
# comme une liste de liste.
# Chaque liste représente une ligne.


grille = [["X", " ", "X"],
          [" ", "X", " "],
          ["O", "O", "O"]]


# grille_initiale = [[" ", " ", " "],
#                    [" ", " ", " "],
#                    [" ", " ", " "]]


# Chercher un alignement gagnant
# -> Soit une liste est remplie seulement du même élément
# -> Soit il y a une diagonale
# -> Soit une colonne est remplie du même élément

# Tester si une case est remplie
# Et remplir une case

# À un moment, on aura besoin de savoir qui est le gagnant.
# Plusieurs possibilités :
# Compter les tours (un joueur ne peut gagner qu'à son tour)
# Faire en sorte qu'une fonction renvoie le joueur gagnant
# Ajouter un paramètre "joueur" et l'on teste si tel joueur gagne

def est_une_ligne_gagnante(ligne, joueur):
    """Teste si `ligne` est gagnante pour `joueur`"""
    # Si la ligne est de taille 3 et qu'on le sait :
    # return ligne[0] == ligne[1] == ligne[2] == joueur
    # Sinon :
    for elem in ligne:
        if elem != joueur:
            return False
    return True


def contient_une_ligne_gagnante(grille, joueur):
    """Teste si `grille` contient une ligne gagnante pour `joueur`"""
    for ligne in grille:
        if est_une_ligne_gagnante(ligne, joueur):
            return True
    return False


def contient_une_colonne_gagnante(grille, joueur):
    """Teste si `grille` contient une colonne gagnante pour `joueur`"""
    for j in range(len(grille[0])):
        est_colonne_gagnante = True
        for i in range(len(grille)):
            if grille[i][j] != joueur:
                est_colonne_gagnante = False
        if est_colonne_gagnante:
            return True
    return False


def diagonale_gagnante(grille, joueur):
    """Teste si la diagonale haut-gauche bas-droite de `grille` est gagnante pour `joueur`"""
    for i in range(len(grille)):
        if grille[i][i] != joueur:
            return False
    return True


def anti_diagonale_gagnante(grille, joueur):
    """Teste si la diagonale haut-droite bas-gauche de `grille` est gagnante pour `joueur`"""
    for i in range(len(grille)):
        if grille[i][len(grille) - i - 1] != joueur:
            return False
    return True
                    

def est_grille_gagnante(grille, joueur):
    """Teste si `grille` est gagnante pour joueur`"""
    return (contient_une_ligne_gagnante(grille, joueur) or
            contient_une_colonne_gagnante(grille, joueur) or
            diagonale_gagnante(grille, joueur) or
            anti_diagonale_gagnante(grille, joueur))


# Créer la grille initiale

def est_pleine(grille):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == " ":
                return False
    return True


def jouer_coup(grille, i, j, joueur):
    grille[i][j] = joueur
    
    
def affiche_grille(grille):
    for i in range(len(grille)):
        print("|", end="")
        for j in range(len(grille[0])):
            print(grille[i][j], end = "|")
        print()
    
    
grille_initiale = [[" ", " ", " "],
                   [" ", " ", " "],
                   [" ", " ", " "]]


ligne = [" ", " ", " "]
grille = [ligne, ligne, ligne]
grille[0][1] = "X"

