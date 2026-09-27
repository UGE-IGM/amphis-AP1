from random import randint

win_L, win_T = 0, 0
courses = 0  # indice de boucle 1

while courses < 1000:  # condition de continuation (boucle 1)
    pos_L = 0
    pos_T = 0
    winner = "Tortue"
    while pos_T < 6 and pos_L < 6:  # condition de continuation (boucle 2)
        lancer = randint(1, 6)
        if lancer == 6:
            pos_L = 6
            win_L += 1
        else:
            pos_T += lancer
            if pos_T >= 6:
                win_T += 1
    
