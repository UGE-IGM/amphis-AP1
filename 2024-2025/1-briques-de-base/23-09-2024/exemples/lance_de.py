from random import randint

def lance_de():
    """Renvoie le résultat d'un lancer d'un dé à six faces."""
    return randint(1,6)


compteur = 1
while lance_de() != 6:
    compteur = compteur + 1
print('Obtenu un 6 en', compteur, 'jets de dé.')