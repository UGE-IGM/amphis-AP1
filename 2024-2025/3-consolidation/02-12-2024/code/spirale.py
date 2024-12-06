from turtle import *
from random import randint

def spirale(longueur, angle, increment):
    """
    Paramètres :
    - longueur : int
    - angle : int
    - increment : int
    Dessine une spirale dont le côté vaut initialement longueur,
    et qui tourne de angle à chaque étape,
    en raccourcissant de increment à chaque fois
    """
    if longueur <= 0:
        return  # On met "return" pour s'assurer que
                # la fonction ne fait rien d'autre
    else:
        forward(longueur)
        right(angle)
        spirale(longueur - increment, angle, increment)


#########################################################
##### Zone du programme qui dessine vos fractales #######
#########################################################

if __name__ == '__main__':
    setup(800, 800) 	# <- ne pas modifier !!!
    # Mettre la vitesse au maximum
    # speed(0)
    down()
    spirale(200, 90, 5)
    arbre()
    exitonclick()		# <- ne pas modifier !!!
