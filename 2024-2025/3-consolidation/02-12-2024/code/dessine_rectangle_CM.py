def dessine_ligne(n, caractere):
    for i in range(n):
        print(caractere, end=' ')
    print()  # Retour à la ligne


# On peut utiliser la multiplication de chaînes de caractères de Python
# pour faire une fonction plus compacte
def dessine_ligne_short(m, caractere):
    print(m * (caractere + ' '), end=' ')


def dessine_rectangle(m, n, caractere):
    for i in range(n):
        dessine_ligne(m, caractere)
        print()


def dessine_carre(n, caractere):
    dessine_rectangle(n, n, caractere)


# On définit un rectangle par récurrence
# (en informatique, on dit "récursivement") :
# Un rectangle de hauteur 0 est juste du vide
# Un rectangle de largeur m et de hauteur n+1 est
# une ligne de longueur m suivie d'un rectangle de hauteur n
def dessine_rectangle_rec(m, n, caractere):
    if m == 0:
        pass  # On ne fait rien
    else:
        dessine_ligne(n, caractere)
        dessine_rectangle(m-1, n, caractere)


# Remarque : on pourrait aussi dessiner une ligne de manière récursive
def dessine_ligne_rec(n, caractere):
    if n == 0:
        print()  # Retour à la ligne
    else:
        print(caractere, end=' ')
        dessine_ligne_rec(n-1, caractere)


dessine_ligne(10, '*')
dessine_rectangle_rec(3, 5, '*')
