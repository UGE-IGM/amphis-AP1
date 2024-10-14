grille = [[ " " , " ", " "],
          [ " " , " ", " "],
          [ " " , " ", " "]]

print(grille[0])
print(grille[1])
print(grille[2])


grille[1][1] = "X"
resultat = grille[1][1]
print("-------------")

print(grille[0])
print(grille[1])
print(grille[2])

grille[2][2] = "0"

print("-------------")

print(grille[0])
print(grille[1])
print(grille[2])

grille[0][2] = "X"

print("-------------")

print(grille[0])
print(grille[1])
print(grille[2])