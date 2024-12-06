from turtle import *


# Pour représenter une feuille, on dessine un petit cercle vert
def dessine_feuille(rayon):
    width(1)
    fillcolor("green")
    begin_fill()
    circle(rayon)
    end_fill()


# Cette fonction implémente les étapes présentées à la slide 14
def dessine_arbre(longueur, ratio, angle, epaisseur):
    """
    Dessine un arbre de longueur donnée, avec le ratio tronc/branches donné,
    l'angle entre les branches donné, et l'épaisseur de tronc donnée.
    Ici, un arbre est un tronc, au-dessus duquel on dessine
    deux arbres plus petits pour symboliser les branches.
    Au bout des branches, lorsqu'elles sont suffisamment petites,
    on dessine des feuilles.
    Paramètres :
    - longueur (int) : la longueur du tronc
    - ratio (float) : le ratio longueur du tronc/ longueur des branches
    - angle (int) : l'angle entre la branche de gauche et l'axe du tronc
    - epaisseur (int) : la largeur du tronc, en pixels
    """
    # On considère qu'un arbre suffisamment petit est juste une feuille
    # Cela permet de terminer la récursion
    if longueur <= 10:
        dessine_feuille(5)
    else:
        color("brown")
        width(epaisseur)
        forward(longueur)
        left(angle)
        dessine_arbre(longueur * ratio, ratio, angle, epaisseur * ratio)
        right(angle)
        right(angle)
        dessine_arbre(longueur * ratio, ratio, angle, epaisseur * ratio)
        left(angle)
        backward(longueur)


if __name__ == '__main__':
    setup(800, 800) 	# <- ne pas modifier !!!
    up()
    goto(0, -350)  # On va en bas de l'image
    # Mettre la vitesse au maximum
    speed(0)
    # On pose le crayon
    down()
    # On le tourne vers le haut
    left(90)
    dessine_arbre(250, 2/3, 30, 10)
    exitonclick()		# <- ne pas modifier !!!
