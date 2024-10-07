def dessine_ligne(n, caractere):
    """Dessine une ligne de longueur n
       constituée du caractère donné en paramètre."""
    j = 0
    while j < n:
        print(caractere, end = '')
        j += 1
    print('\n', end = '')
    return


def dessine_carre(n, caractere):
    """Dessine un carré de dimensions n x n
       constitué du caractère donné en paramètre."""    
    i = 0
    while i < n:
        dessine_ligne(n,caractere)
        i += 1
    return


dessine_carre(12,'*')