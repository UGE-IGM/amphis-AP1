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
            colonne.append(grille[i][j])
        if ligne_gagnante(colonne, joueur):
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
        if grille[len(grille) - i - 1][i] != joueur:
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


# Dans cette version du programme, les cases vides sont marquées d'un point.
def init_grille(taille):
    """Initialise une grille de la taille donnée."""
    grille = []
    for i in range(taille):
        grille.append(["."] * taille)
    return grille

def affiche_grille(grille):
    """Affiche la grille."""
    for ligne in grille:
        for element in ligne:
            print(element, end=" ")
        print()


def choix_case(grille):
    """Permet au joueur de choisir une case."""
    nr_ligne = int(input("Entrez un numéro de ligne : "))
    nr_colonne = int(input("Entrez un numéro de colonne : "))
    while grille[nr_ligne][nr_colonne] != ".":
        print("Cette case est déjà occupée ! Veuillez entrer une position valide : ")
        nr_ligne = int(input("Entrez un numéro de ligne : "))
        nr_colonne = int(input("Entrez un numéro de colonne : "))
    # On renvoie un tuple
    return (nr_ligne, nr_colonne)

def choix_entier(message):
    """Demande au joueur de choisir un nombre entier."""
    while True:
        reponse = input(message)
        if reponse.isnumeric():
            return int(reponse)
        else:
            print("Ceci n'est pas un nombre entier.")

def choix_case_verif(grille):
    """Permet au joueur de choisir une case,
    en vérifiant qu'il s'agit d'une case valide."""
    while True:
        nr_ligne = choix_entier("Entrez un numéro de ligne : ")
        nr_colonne = choix_entier("Entrez un numéro de colonne : ")
        if 0 <= nr_ligne < len(grille) and 0 <= nr_colonne < len(grille):
            if grille[nr_ligne][nr_colonne] == ".":
                return (nr_ligne, nr_colonne)
            else:
                print("Cette case est déjà occupée ! Veuillez entrer une position valide.")
        else:
            print("Cette case est hors de la grille ! Veuillez entrer une position valide.")


def complete(grille):
    """Teste si une grille est complète."""
    for ligne in grille:
        for element in ligne:
            if element == ".":
                return False
    return True


def adversaire(joueur):
    """Renvoie l'adversaire du joueur."""
    if joueur == "X":
        return "O"
    else:
        return "X"


### Programme principal amélioré ###

# La grille de jeu, initialement vide
# Le jeu de morpion se joue généralement sur une grille 3 x 3
grille = init_grille(3)

# Attention à la copie superficielle :
# Procéder comme suit ne fonctionne pas (testez)
# ligne = [ " ", " ", " "]
# grille = [ligne, ligne, ligne]

# Tient à jour le joueur courant
joueur_courant = "X"
# Vérifie s'il est encore possible de jouer

while not complete(grille):
    affiche_grille(grille)
    print(f"Joueur courant : {joueur_courant}")
    nr_ligne, nr_colonne = choix_case_verif(grille)
    grille[nr_ligne][nr_colonne] = joueur_courant
    if a_gagne(grille, joueur_courant):
        # On réaffiche la grille
        print(grille)
        print(f"Le joueur {joueur_courant} a gagné !")
        # `break` permet de sortir prématurément d'une boucle
        break
    # On passe au tour du joueur suivant
    joueur_courant = adversaire(joueur_courant)
# Si on sort de la boucle, c'est que la grille est complète
# Ici, `else` permet d'exécuter une instruction
# seulement si la boucle est allée au bout.
# Attention, c'est hors programme !
else:
    print("Ex aequo.")
