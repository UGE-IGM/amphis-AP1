liste = [5, 8, 12, 3, 7, 2, 13]

somme = 0
nombre_elements = 0
for element in liste:
    somme = somme + element
    nombre_elements = nombre_elements + 1
moyenne = somme / nombre_elements
    
print("La somme de la liste est", somme)
print("La moyenne de la liste est", moyenne)
