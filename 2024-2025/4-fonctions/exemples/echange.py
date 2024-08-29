# Cette fonction échange-t-elle vraiment les valeurs de a et b ?
def echange(a, b):
    """
    Une tentative (échouée) pour échanger les variables données en argument.
    """
    temp = a
    a = b
    b = temp

x = 1
y = 2
echange(x, y)
print(x, y)
