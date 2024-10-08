# fonction à deux paramètres produisant un résultat
def minimum(a, b):
    """
    Renvoie le minimum de a et b
    """
    if a <= b:
        print(a)
    else:
        print(b)

nb1 = 14
nb2 = 31

minimum(nb1, nb2)  # ne sert à rien !!

# On appelle la fonction et on garde le résultat dans c :
c = minimum(nb1, nb2)
# print("le min de", nb1, "et", nb2, "est", c)

# On peut aussi utiliser directement le résultat :
# print("le min de", nb1, "et", nb2, "est", minimum(nb1, nb2))

nb1 = 25
nb2 = 50
nb3 = 12

c = minimum(minimum(nb1, nb2), nb3)
print(c)