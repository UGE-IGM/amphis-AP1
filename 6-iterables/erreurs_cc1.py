from doctest import testmod


# ATTENTION !
# Ce fichier contient un grand nombre d'erreurs et de maladresses.
# À utiliser avec prudence !!

# Objectif : corriger toutes les fonctions ci-dessous
# et relever les erreurs rencontrées.
# Attention, les tests fournis ne sont pas suffisants
# pour détecter toutes les erreurs.


# Q11 : préfixe croissant d'une liste

def prefixe_croissant(lst):
    """
    >>> prefixe_croissant([])
    []
    >>> prefixe_croissant([3, 1, 2])
    [3]
    >>> prefixe_croissant([1, 4])
    [1, 4]
    >>> prefixe_croissant([3, 4, 6, 1, 2])
    [3, 4, 6]
    """
    res = []
    i = 0
    while lst[i] < lst[i+1]:
        res.append(lst[i])
        i += 1
    return res

# Liste des erreurs repérées :
# - ...


def prefixe_croissant_bis(lst):
    """
    >>> prefixe_croissant_bis([])
    []
    >>> prefixe_croissant_bis([3, 1, 2])
    [3]
    >>> prefixe_croissant_bis([1, 4])
    [1, 4]
    >>> prefixe_croissant_bis([3, 4, 6, 1, 2])
    [3, 4, 6]
    """
    res = []
    i = 0
    while i < len(lst):
        if lst[i] < lst[i+1]:
            res.append(lst[i])
        i += 1
    return res

# Liste des erreurs repérées :
# - ...


# Q12 : liste des indices

def liste_indices(lst, elem):
    """
    >>> liste_indices([], 'test')
    []
    >>> liste_indices(['ce', 'test', 'est', 'un', 'très', 'bon', 'test'], 'test')
    [1, 6]
    >>> liste_indices([1, 0, 3, 3, 0, 1], 5)
    []
    >>> liste_indices([1, 0, 3, 3, 0, 1], 3)
    [2, 3]
    """
    if lst == []:
        return lst
    res = []
    i = 0
    while i <= len(lst):
        if lst[i] == elem:
            res.append(lst[i])
            i += 1
        print(res)

# Liste des erreurs repérées :
# - ...


# Q13 : conversion liste vers mot avec caractère ignoré

def liste_vers_mot_ignore(lst, a_ignorer):
    """
    >>> liste_vers_mot_ignore(['#', 'B', 'o', '#', 'n', 'j', 'o', '#', '#', 'u', 'r'], '#')
    'Bonjour'
    >>> liste_vers_mot_ignore(['x', 'x', 'x'], 'x')
    ''
    >>> liste_vers_mot_ignore([], '@')
    ''
    """
    res = []
    i = 0
    if a_ignorer in lst:
        lst.remove(a_ignorer)
    i = 0
    while i < len(lst):
        res.append(lst[i])
        i += 1
    print(str(res))

# Liste des erreurs repérées :
# - ...


def liste_vers_mot_ignore_bis(lst, a_ignorer):
    """
    >>> liste_vers_mot_ignore_bis(['#', 'B', 'o', '#', 'n', 'j', 'o', '#', '#', 'u', 'r'], '#')
    'Bonjour'
    >>> liste_vers_mot_ignore_bis(['x', 'x', 'x'], 'x')
    ''
    >>> liste_vers_mot_ignore_bis([], '@')
    ''
    """
    i = 0
    while i < len(lst):
        if lst[i] == a_ignorer:
            lst.pop(i)
        i += 1
    return lst

# Liste des erreurs repérées :
# - ...


# Q14 : saisir une liste de caractères

def saisir_liste_caracteres():
    lst = []
    saisie = 'a'
    while saisie != 'fin' or saisie != 'stop' or saisie != 'toto' or saisie != '':
        saisie = int(input())
        lst.append(saisie)
    return lst

# Liste des erreurs repérées :
# - ...


# Q15 : programme principal

def question_15():
    ign = int(input('Saisir un caractère à ignorer : '))
    print('Caractère à ignorer :', ign)
    saisir_liste_caracteres
    liste_vers_mot_ignore(lst, a_ignorer)
    print(res)
    

# Liste des erreurs repérées :
# - ...