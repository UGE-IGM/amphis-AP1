def ligne_gagnante(ligne, joueur):
    """
    Teste si la ligne donnée est gagnante pour le joueur.
    """
    for element in ligne:
        if element != joueur:
            return False
    return True

def a_gagne_horizontal(grille, joueur):
    """Teste si le joueur a gagné
via une ligne horizontale."""
    for ligne in grille:
        if ligne_gagnante(ligne, joueur):
            return True
    return False

# Une autre possibilité
def a_gagne_horizontal_2(grille, joueur):
    """Teste si le joueur a gagné
via une ligne horizontale."""
    for ligne in grille:
        gagne = True
        for element in ligne:
            if element != joueur:
                gagne = False
        if gagne:
            return True
    return False

def a_gagne_vertical(grille, joueur):
    """Teste si le joueur a gagné
via une ligne verticale."""
    for j in range(len(grille)):
        colonne = []
        for i in range(len(grille)):
            colonne.append(grille[j][i])
        if ligne_gagnante(ligne, joueur):
            return True
    return False

def a_gagne_vertical_2(grille, joueur):
    """Teste si le joueur a gagné
via une ligne verticale."""
    for j in range(len(grille)):
        gagne = True
        for i in range(len(grille)):
            if grille[i][j] != joueur:
                gagne = False
        if gagne:
            return True
    return False

def a_gagne_diagonal(grille, joueur):
    """Teste si le joueur a gagné
via une diagonale."""
    gagne = True
    # Première diagonale
    for i in range(len(grille)):
        if grille[i][i] != joueur:
            gagne = False
    if gagne:
        return True
    # Deuxième diagonale
    for i in range(len(grille)):
        if grille[len(grille) - i][i] != joueur:
            gagne = False
    if gagne:
        return True

def a_gagne_diagonal_2(grille, joueur):
    """Teste si le joueur a gagné
via une diagonale."""
    diag_1 = [grille[0][0], grille[1][1], grille[2][2]]
    diag_2 = [grille[0][2], grille[1][1], grille[2][0]]
    return ligne_gagnante(diag_1, joueur) or ligne_gagnante(diag_2, joueur)


def a_gagne(grille, joueur):
    """Teste si le joueur a gagné."""
    return (a_gagne_horizontal(grille, joueur)
            or a_gagne_vertical(grille, joueur)
            or a_gagne_diagonal(grille, joueur))


### Programme principal

# La grille de jeu, initialement vide
grille = [[ " " , " ", " "],
          [ " " , " ", " "],
          [ " " , " ", " "]]

# Attention à la copie superficielle :
# Procéder comme suit ne fonctionne pas (testez)
# ligne = [ " ", " ", " "]
# grille = [ligne, ligne, ligne]

# Affichage initial de la grille
print(grille[0])
print(grille[1])
print(grille[2])

# Tient à jour le joueur courant
joueur_courant = "X"
# Vérifie s'il est encore possible de jouer
termine = False

while not termine:
    nr_ligne = int(input("Entrez un numéro de ligne : "))
    nr_colonne = int(input("Entrez un numéro de colonne : "))
    while grille[nr_ligne][nr_colonne] != " ":
        print("Cette case est déjà occupée ! Veuillez entrer une position valide : ")
        nr_ligne = int(input("Entrez un numéro de ligne : "))
        nr_colonne = int(input("Entrez un numéro de colonne : "))
    grille[nr_ligne][nr_colonne] = joueur_courant
    
    print(grille[0])
    print(grille[1])
    print(grille[2])
    
    termine = True
    for ligne in grille:
        for element in ligne:
            if element == " ":
                termine = False
                
    if a_gagne(grille, joueur_courant):
        termine = True
        gagnant = joueur_courant
                
    if joueur_courant == "X":
        joueur_courant = "O"
    else:
        joueur_courant = "X"
