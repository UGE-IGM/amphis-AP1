from random import randint
choix = input("pile ou face ? ")
if choix == "pile":
    nombre_choix = 1
else:
    nombre_choix = 0
tirage = randint(0,1)
if tirage == 1:
    print("Le résultat est pile !")
else:
    print("Le résultat est face !")
if nombre_choix == tirage:
    print("Gagné !")
else:
    print("Perdu !")
