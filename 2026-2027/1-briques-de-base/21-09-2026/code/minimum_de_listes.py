# Paramètres : lst une liste d'entiers
# Valeur de retour : le minimum, un entier
# Parcours par indices
def minimum(lst):
    if lst == []:
        return None
    m = lst[0]
    for i in range(len(lst)):
        elem = lst[i]
        if m > elem:
            m = elem
    return m
# Parcours par éléments
def minimum_2(lst):
    if lst == []:
        return None
    m = lst[0]
    for elem in lst:
        if m > elem:
            m = elem
    return m
        
        
    
lst = [7, 5, 2, 3, 8, 10, 3]

mon_min = minimum(lst)
print(mon_min)

mon_min_2 = minimum_2(lst)
print(mon_min_2)
