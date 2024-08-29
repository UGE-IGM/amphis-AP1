def dessine_carre(n, caractere):
    i = 0
    while i < n:
        j = 0
        while j < n:
            print(caractere, end = '')
            j += 1
        print('\n', end = '')
        i += 1
    return

dessine_carre(5,'0')