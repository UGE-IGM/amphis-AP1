from random import randint

NB_ESSAIS = 10000
total = 0
for i in range(NB_ESSAIS):
    gagne = False
    essais = 0
    successifs = 0
    while not gagne:
        essais+=1
        choix = randint(0,1)
        tirage = randint(0,1)
        print("Essai n°", essais)
        print("Choix : ", choix, "\nTirage : ", tirage)
        if choix == tirage:
            successifs+=1
            if successifs == 3:
                gagne = True
        else:
            successifs = 0
    total += essais
    print("\nNombre d'essais : ", essais, "\n\n")

print(total/NB_ESSAIS)


