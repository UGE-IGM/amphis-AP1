# Utilisation du mot-clé global pour modifier des variables globales.
x = 12

def test(a):
    global x
    x = a

test(25)
print(x)
