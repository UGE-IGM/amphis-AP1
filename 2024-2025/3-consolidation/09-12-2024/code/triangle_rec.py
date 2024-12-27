def triangle(hauteur):
    if hauteur == 1:
        print('*')
    else:
        triangle(hauteur - 1)
        print('*' * hauteur)


triangle(15)
