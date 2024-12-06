def affiche_entiers(n):
    i = n
    while i > 0:
        print(i)
        i -= 1


def affiche_entiers_rec(n):
    if n == 0:
        return
    else:
        print(n)
        affiche_entiers_rec(n-1)


affiche_entiers_rec(3)
