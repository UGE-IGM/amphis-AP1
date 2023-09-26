def dessine_ligne(n, caractere):
    n = int(input())
    j = 0
    while j < n:
        print(caractere, end = '')
        j += 1
    print('\n', end = '')
    return

def dessine_carre(n, caractere):
    i = 0
    while i < n:
        dessine_ligne(n,caractere)
        i += 1
    return

dessine_carre(5,'0')