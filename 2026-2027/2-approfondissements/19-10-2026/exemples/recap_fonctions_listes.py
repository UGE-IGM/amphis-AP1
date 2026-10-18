def chercher(lst, x):
    """Renvoie l'indice de la première occurrence de x,
    et None si x n'apparaît pas dans la liste."""
    # On itère par indices car on a besoin de l'indice
    for i in range(len(lst)):
        if lst[i] == x:
            # pas la peine d'aller plus loin
            return i
    # élément non trouvé
    return None

def chercher(L, x):
    """Renvoie l'indice de la première occurrence de x,
    et None si x n'apparaît pas dans la liste."""
    i = 0
    while i < len(L):
        if L[i] == x:
            # pas la peine d'aller plus loin
            return i
        i += 1
    # élément non trouvé
    return None


def compter(lst, x):
    """Renvoie le nombre d'occurrences de x dans lst."""
    cpt = 0
    for elem in lst:
        if elem == x:
            cpt += 1
    return cpt

def compter(lst, x):
    """Renvoie le nombre d'occurrences de x dans lst."""
    i = 0
    cpt = 0
    while i < len(lst):
        if lst[i] == x:
            cpt += 1
        i += 1
    return cpt


def vider(lst):
    """Vide la liste donnée en argument."""
    # cette fonction n'est pas vraiment
    # implémentée comme ça en principe...
    while len(lst) > 0:
        lst.pop()

# Pas d'implémentation avec `for`
# C'est possible d'en faire une mais on préfère ne pas.


def copier(lst):
    """Renvoie une copie de lst."""
    copie = []
    for elem in lst:
        copie.append(elem)
    return copie

def copier(lst):
    """Renvoie une copie de lst."""
    copie = []
    i = 0
    while i < len(lst):
        copie.append(lst[i])
        i += 1
    return copie


def renverser(lst):
    """Renverse la liste donnée en argument."""
    i = 0
    while i < len(lst) // 2:
        # chaque élément de la première moitié
        # est interverti avec l'élément symétrique
        temp = lst[i]
        lst[i] = lst[len(lst) - i - 1]
        lst[len(lst) - i - 1] = temp
        i += 1

# Pas d'implémentation avec `for`
# C'est possible d'en faire une mais on préfère ne pas.


def retirer(lst, x):
    """Retire la première occurrence de x dans lst."""
    i = chercher(lst, x)
    if i is not None:
        # décaler tous les éléments
        # suivants d'un cran à gauche
        while i < len(lst) - 1:
            lst[i] = lst[i + 1]
            i += 1
        # supprimer la dernière case
        lst.pop()

# Pas d'implémentation avec `for`
# C'est possible d'en faire une mais on préfère ne pas.


def inserer(lst, i, x):
    """Insère l'élément x à l'indice i dans lst."""
    if i >= len(lst):
        # le nouvel élément va à la fin
        lst.append(x)
    else:
        # décaler le dernier élément d'un cran à droite (nouvelle case)
        lst.append(lst[len(lst) - 1])
        # décaler tous les éléments d'indices i à len(lst)-2 vers la droite
        # (en partant de l'ancienne fin)
        j = len(lst) - 2
        while j > i:
            lst[j] = lst[j - 1]
            j -= 1
        # placer le nouvel élément
        lst[i] = x

# Pas d'implémentation avec `for`
# C'est possible d'en faire une mais on préfère ne pas.
