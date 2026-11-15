# Un morpion VOLONTAIREMENT MAUVAIS : à ne surtout pas reproduire !

case_haut_gauche = None
case_haut_milieu = None
case_haut_droite = None
case_milieu_gauche = None
case_milieu_milieu = None
case_milieu_droite = None
case_bas_gauche = None
case_bas_milieu = None
case_bas_droite = None


def demander_case(joueur):
    print("C'est au tour de", joueur)
    ligne = input("Ou voulez vous jouer ? (haut, milieu, bas) ")
    colonne = input("Et dans quelle colonne ? (gauche, milieu, droite) ")
    return ligne + " " + colonne


def afficher(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 == None:
        print("_", end=" ")
    else:
        print(c1, end=" ")
    if c2 == None:
        print("_", end=" ")
    else:
        print(c2, end=" ")
    if c3 == None:
        print("_")
    else:
        print(c3)
    if c4 == None:
        print("_", end=" ")
    else:
        print(c4, end=" ")
    if c5 == None:
        print("_", end=" ")
    else:
        print(c5, end=" ")
    if c6 == None:
        print("_")
    else:
        print(c6)
    if c7 == None:
        print("_", end=" ")
    else:
        print(c7, end=" ")
    if c8 == None:
        print("_", end=" ")
    else:
        print(c8, end=" ")
    if c9 == None:
        print("_")
    else:
        print(c9)


def a_gagne(j, c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 == j and c2 == j and c3 == j:
        return True
    if c4 == j and c5 == j and c6 == j:
        return True
    if c7 == j and c8 == j and c9 == j:
        return True
    if c1 == j and c4 == j and c7 == j:
        return True
    if c2 == j and c5 == j and c8 == j:
        return True
    if c3 == j and c6 == j and c9 == j:
        return True
    if c1 == j and c5 == j and c9 == j:
        return True
    if c3 == j and c5 == j and c7 == j:
        return True
    return False


def plein(c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 != None and c2 != None and c3 != None and c4 != None and c5 != None and c6 != None and c7 != None and c8 != None and c9 != None:
        return True
    return False


joueur = "X"
fini = False
while not fini:
    afficher(case_haut_gauche, case_haut_milieu, case_haut_droite, case_milieu_gauche, case_milieu_milieu, case_milieu_droite, case_bas_gauche, case_bas_milieu, case_bas_droite)
    choix = demander_case(joueur)
    if choix == "haut gauche":
        case_haut_gauche = joueur
    if choix == "haut milieu":
        case_haut_milieu = joueur
    if choix == "haut droite":
        case_haut_droite = joueur
    if choix == "milieu gauche":
        case_milieu_gauche = joueur
    if choix == "milieu milieu":
        case_milieu_milieu = joueur
    if choix == "milieu droite":
        case_milieu_droite = joueur
    if choix == "bas gauche":
        case_bas_gauche = joueur
    if choix == "bas milieu":
        case_bas_milieu = joueur
    if choix == "bas droite":
        case_bas_droite = joueur
    if a_gagne(joueur, case_haut_gauche, case_haut_milieu, case_haut_droite, case_milieu_gauche, case_milieu_milieu, case_milieu_droite, case_bas_gauche, case_bas_milieu, case_bas_droite):
        afficher(case_haut_gauche, case_haut_milieu, case_haut_droite, case_milieu_gauche, case_milieu_milieu, case_milieu_droite, case_bas_gauche, case_bas_milieu, case_bas_droite)
        print(joueur, "a gagné")
        fini = True
    elif plein(case_haut_gauche, case_haut_milieu, case_haut_droite, case_milieu_gauche, case_milieu_milieu, case_milieu_droite, case_bas_gauche, case_bas_milieu, case_bas_droite):
        afficher(case_haut_gauche, case_haut_milieu, case_haut_droite, case_milieu_gauche, case_milieu_milieu, case_milieu_droite, case_bas_gauche, case_bas_milieu, case_bas_droite)
        print("Match nul")
        fini = True
    else:
        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"

if __name__ == "__main__":
    pass