def recherche(lst, element):
    
    for elem in lst :
        if elem == element :
            return True
    return False


def recherche_indice_variante(lst, element):
    """i = 0
    while i < len(lst):
        if lst[i] == element:
            return i
        i += 1
    return None"""
    liste_indice = []
    for i in range(len(lst)):
        if lst[i] == element:
            liste_indice.append( i)
    return liste_indice 


def calcul_max(liste):
    maxi = liste[0]
    for element in liste :
        if maxi < element :
            maxi = element
    return maxi


def somme(liste):
    somme = 0 # accumulateur
    for elem in liste:
        somme += elem
    return somme


def tous_pairs(liste):
    
    for elem in liste :
        if elem % 2 != 0:
            return False
    return True



liste = []
element_a_chercher = input("entrez l'élément à chercher")
print(recherche(liste, element_a_chercher))