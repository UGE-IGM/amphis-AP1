## Suite à une question posée en CM,
# voici quelques indications sur quand utiliser les différentes boucles

## Boucle while
# Quand il s'agit de modifier la liste.

## Exemple : enlever tous les zéros d'une liste
def enleve_zeros(liste):
    """Modifie la liste donnée en argument en retirant les zéros."""
    i = 0
    while i < len(liste):
        if liste[i] == 0:
            # Pop retire l'élément à l'indice i
            liste.pop(i)
        else:
            i += 1
# Cette fonction est difficile à faire avec un `for`, et c'est déconseillé
# car la boucle `for` n'est pas prévue pour cela, sauf exceptions.


print("Exemple d'utilisation de while : enlever les zéros")
liste = [1, 0, 5, 0, 6, 2, 3, 2, 0]
print(f"Liste : {liste}")
enleve_zeros(liste)
print(f"Liste après l'appel à enleve_zeros : {liste}")


## For par indices
# Quand on a besoin de connaître l'indice de l'élément

## Exemple : trouver l'indice de la première occurrence d'un élément
def premiere_occurrence(liste, element):
    """Renvoie la première occurrence de l'élément dans liste,
    ou None si l'élément est absent de la liste.
    Similaire à liste.index(element),
    mais ne renvoie pas d'erreur si element est absent de la liste."""
    for i in range(len(liste)):
        if element == liste[i]:
            return i
    return None

# Rappel : \n permet de passer à la ligne
print("\nExemple d'utilisation de for par indices : trouver la première occurrence")
liste = [1, 0, 5, 0, 6, 2, 3, 2, 0, 0]
print(f"Liste : {liste}")
cible = 2
occ = premiere_occurrence(liste, cible)
print(f"Première occurrence de {cible} : l'indice {occ}")

## For par enumerate (hors programme)
# Quand on a besoin de connaître l'indice de l'élément et l'élément lui-même

## Exemple : trouver l'indice de la première occurrence d'un élément
def premiere_occurrence_enum(liste, element):
    """Renvoie la première occurrence de l'élément dans liste,
    ou None si l'élément est absent de la liste.
    Similaire à liste.index(element),
    mais ne renvoie pas d'erreur si element est absent de la liste."""
    for i, e in enumerate(liste):
        if element == e:
            return i
    return None

print("\nExemple d'utilisation de for par enumerate (hors programme) : trouver la première occurrence")
liste = [1, 0, 5, 0, 6, 2, 3, 2, 0, 0]
print(f"Liste : {liste}")
cible = 2
occ = premiere_occurrence_enum(liste, cible)
print(f"Première occurrence de {cible} : l'indice {occ}")

## For par éléments
# Quand on a seulement besoin des éléments
# Typiquement, si la liste représente un ensemble

## Exemple : déterminer si un élément est présent dans une liste
def appartient(liste, element):
    """Renvoie True si element apparaît dans liste, False sinon.
    Équivalent au mot-clé `in`, ou encore à la méthode `__contains__`."""
    for e in liste:
        if element == e:
            return True
    return False

print("\nExemple d'utilisation de for par éléments : tester l'appartenance")
liste = [1, 0, 5, 0, 6, 2, 3, 2, 0, 0]
print(f"Liste : {liste}")
cible = 6
apparait = appartient(liste, cible)
if apparait:
    print("{cible} apparaît dans la liste.")
else:
    print("{cible} n'apparaît pas dans la liste.")

## Deuxième exemple : compter le nombre d'occurrences
# d'un élément dans une liste
def compte(liste, element):
    """Renvoie le nombre d'occurrences de l'élément dans la liste.
    Équivalent à la méthode `count`."""
    occurrences = 0
    for e in liste:
        if element == e:
            occurrences += 1
    return occurrences

print("\nExemple d'utilisation de for par éléments : compter les occurrences")
liste = [1, 0, 5, 0, 6, 2, 3, 2, 0, 0]
print(f"Liste : {liste}")
cible = 0
occurrences = compte(liste, cible)
print(f"Nombre d'occurrences de {cible} dans liste : {occurrences}")
