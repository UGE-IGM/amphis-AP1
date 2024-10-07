def dessine_ligne(n, caractere):
    """Dessine une ligne de longueur n
       constituée du caractère donné en paramètre."""
    for j in range(n):
        print(caractere, end = '')


def dessine_carre(n, caractere):
    """Dessine un carré de dimensions n x n
       constitué du caractère donné en paramètre."""
    for i in range(n):
        dessine_ligne(n, caractere)
        print()


dessine_carre(12,'*')