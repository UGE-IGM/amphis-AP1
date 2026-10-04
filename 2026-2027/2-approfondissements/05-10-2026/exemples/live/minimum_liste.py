def minimum_int(a, b):
    # À éviter : a = int(input()) # NON
    # À éviter : b = int(input()) # NON
    if a > b:
        m = b
        # À éviter : print(b)
    else:
        m = a
        # À éviter : print(a)
    return m

def minimum_liste_1(liste):
    """
Renvoie le minimum d'une liste.
    """
    m = liste[0]
    for elt in liste:
        if elt < m:
            m = elt
    return m

def minimum_liste_2(liste):
    m = liste[0]
    for elt in liste:
        m = minimum_int(m, elt)
    return m
    

lst = [5, 8, 12, 3, 7, 2, 13]
lst2 = [9, 5, 23]

# print(minimum_liste_1(lst))
print(minimum_liste_2(lst))
