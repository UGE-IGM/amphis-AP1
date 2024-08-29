# Observer comment s'empilent les appels de fonctions.
def minimum(a,b):
    """
    Renvoie le minimum de a et de b.
    """
    temp = 0
    if a <= b:
        temp = a
    else:
        temp = b
    return temp

def addition(a,b):
    """
    Renvoie la somme de a et de b.
    """
    return a+b

def soustraction(a,b):
    """
    Renvoie la différence de a et de b.
    """
    return a - b

def multiplication(a,b):
    """
    Renvoie le produit de a et de b.
    """
    return a*b

def division(a,b):
    """
    Renvoie le quotient de a et de b.
    """
    return a // b
    
# m = minimum(5+12, 7*4)
m = minimum(addition(5,12), multiplication(7,4))
# m = minimum(5+12//4, 7*4-3)
m = minimum(addition(5,division(12,4)), soustraction(multiplication(7,4),3))
