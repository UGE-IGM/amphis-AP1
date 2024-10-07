def dessine_carre(n, caractere):
    """Dessine un carré de dimensions n x n
       constitué du caractère donné en paramètre."""
    i = 0
    # Dessine n fois une ligne
    while i < n:
        j = 0
        # Dessine une ligne
        while j < n:
            # Affiche caractere sans retourner à la ligne 
            print(caractere, end = '')
            j += 1
        # Retour à la ligne
        print('\n', end = '')
        i += 1
    return


dessine_carre(12,'*')