import random

resultat = random.randint(0, 1)

if resultat == 0:
    # J'ai tiré un premier pile
    # Je retire une pièce
    nouveau_resultat = random.randint(0, 1)
    # Si j'ai refait pile:
    if nouveau_resultat == 0:
        # J'ai gagné
        print("gagné")
    else:
        # Sinon j'ai perdu
        print("perdu !")
else:
    # J'ai tiré un premier face
    # Je retire une pièce
    nouveau_resultat = random.randint(0, 1)
    # Si j'ai refait face:
    if nouveau_resultat == 1:
        # J'ai gagné
        print("gagné")
    else:
        # J'ai perdu
        print("perdu !")