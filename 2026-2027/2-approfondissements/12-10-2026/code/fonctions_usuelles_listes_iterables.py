def contient(iterable, cible):
    """
    Teste si `iterable` contient l'élément `cible`.
    Paramètres :
    - `iterable` : un itérable (de n'importe quel type)
    - `cible` : un élément (de n'importe quel type)
    Valeur de retour :
    Un booléen indiquant si `iterable` contient `cible`.
    """
    for elem in iterable:
        if elem == cible:
            return True
    return False


def contient_avec_indices(liste, cible):
    """
    Teste si `iterable` contient l'élément `cible`.
    Paramètres :
    - `iterable` : un itérable (de n'importe quel type)
    - `cible` : un élément (de n'importe quel type)
    Valeur de retour :
    Un booléen indiquant si `iterable` contient `cible`.
    """
    # Remarque : c'est la même docstring, car la fonction fait la même chose !
    for i in range(len(liste)):
        if liste[i] == cible:
            return True
    return False


def trouver_indice(liste, cible):
    """
    Cherche l'indice de l'élément `cible` dans `liste`.
    Paramètres :
    - `liste` : une liste (de n'importe quel type)
    - `cible` : un élément (de n'importe quel type)
    Valeur de retour :
    Un entier représentant l'indice de l'élément s'il existe,
    `None` sinon.
    """
    for i, elem in enumerate(liste):
        if elem == cible:
            return i
    return None


def maximum_liste(liste):
    """
    Renvoie le maximum de `liste`
    Paramètres :
    - `liste` : une liste (de n'importe quel type comparable)
    Valeur de retour :
    Le maximum de la liste
    Erreurs :
    Renvoie une erreur si la liste est vide.
    """
    maximum = liste[0]
    for elem in liste:
        if elem > maximum:
            maximum = elem
    return maximum


def maximum_liste_avec_indices(liste):
    """
    Renvoie le maximum de `liste`
    Paramètres :
    - `liste` : une liste (de n'importe quel type comparable)
    Valeur de retour :
    Le maximum de la liste
    Erreurs :
    Renvoie une erreur si la liste est vide.
    """
    # Remarque : c'est la même docstring, car la fonction fait la même chose !
    maximum = liste[0]
    for i in range(len(liste)):
        if liste[i] > maximum:
            maximum = liste[i]
    return maximum


def minimum_liste(liste):
    """
    Renvoie le minimum de `liste`
    Paramètres :
    - `liste` : une liste (de n'importe quel type comparable)
    Valeur de retour :
    Le minimum de la liste
    Erreurs :
    Renvoie une erreur si la liste est vide.
    """
    minimum = liste[0]
    for elem in liste:
        if elem < minimum:
            minimum = elem
    return minimum


def tous_pairs(liste):
    """
    Teste si `liste` contient seulement des éléments pairs.
    Paramètres :
    - `liste` : une liste d'entiers
    Valeur de retour :
    Un booléen indiquant si `iterable` contient seulement des entiers pairs.
    """
    # Remarque : cette fonction marche aussi pour n'importe quel itérable.
    for elem in liste:
        if elem % 2 != 0:
            return False
    return True



if __name__ == "__main__":
    ## Recherche
    print("Test de la recherche :")
    print(contient(['a', 'b', 'c'], 'b'))
    print(contient_avec_indices(['a', 'b', 'c'], 'b'))

    ## Calcul du maximum
    print("Test du calcul du maximum :")
    print(maximum_liste([-1, -5, -2, -3]))

    ## Tous pairs
    print("Test de tous pairs :")
    print(tous_pairs([2, 4, 10, 8]))
    print(tous_pairs([2, 4, 11, 8]))
