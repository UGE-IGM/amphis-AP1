lst = [5, 8, 12, 3, 7, 2, 13]

# Afficher le contenu de lst

## Méthode n°1
print("Méthode n°1")
for i in range(len(lst)):
    print(lst[i])

## Méthode n°2
print("Méthode n°2")
for element in lst:
    print(element)
    
## Méthode n°3
print("Méthode n°3")
for i, elt in enumerate(lst):
    print(i, elt)
    
## Méthode n°4 (un peu moins joli)
print("Méthode n°4")
i = 0
while i < len(lst):
    print(lst[i])
    i += 1
    

# On peut avoir des éléments de types différents dans une liste
lst2 = [True, False, 5, "zakjlejzalkfds", False]
