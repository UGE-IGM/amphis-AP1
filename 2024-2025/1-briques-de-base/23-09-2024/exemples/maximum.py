# fonction à deux paramètres produisant un résultat
def maximum(a, b):
    """Renvoie le maximum de a et b."""
    if a >= b:
        return a
    else:
        return b


nb1 = 13
nb2 = 12

maximum(nb1, nb2)  # ne sert à rien car on ne stocke pas la valeur

# On appelle la fonction et on stocke le résultat dans c :
c = maximum(nb1, nb2)
print("le max de", nb1, "et", nb2, "est", c)

# On peut aussi utiliser directement le résultat :
print("le max de", nb1, "et", nb2, "est", maximum(nb1, nb2))