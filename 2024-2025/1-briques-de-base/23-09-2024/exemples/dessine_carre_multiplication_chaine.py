def dessine_ligne(n, caractere):
    """Dessine une ligne de longueur n
       constituée du caractère donné en paramètre."""
    # Pas besoin de mettre "end = ''"
    # car on affiche toute la ligne d'un coup
    print(caractere * n)
    

def dessine_carre(n, caractere):
    """Dessine un carré de dimensions n x n
       constitué du caractère donné en paramètre."""
    for i in range(n):
        dessine_ligne(n, caractere)
        # Pas besoin d'ajouter "print()"
        # car c'est dessine_ligne qui le fait


dessine_carre(12,'*')
