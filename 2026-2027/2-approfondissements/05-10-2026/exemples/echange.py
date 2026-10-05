# Cette fonction échange-t-elle vraiment les valeurs de a et b ?
def echange(a, b):
    """
    Une tentative (échouée) pour échanger les variables données en argument.
    """
    temp = a
    a = b
    b = temp

t = 1
u = 2
echange(t, u)
print(t, u)
