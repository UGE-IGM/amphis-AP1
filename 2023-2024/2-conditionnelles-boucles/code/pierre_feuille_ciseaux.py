from random import randint

coup_humain = int(input("Pierre (1), feuille (2) ou ciseaux (3) ? "))

coup_ordi = randint(1, 3)
if coup_ordi == 1:
    print("L'ordinateur a joué pierre.")
elif coup_ordi == 2:
    print("L'ordinateur a joué feuille.")
else:
    print("L'ordinateur a joué ciseaux.")

if coup_ordi == coup_humain:
    print("Égalité.")
elif coup_humain == (coup_ordi + 1) % 3:
    print("Vous avez gagné.")
else:
    print("Vous avez perdu.")