x = 12
y = 20

def echange(a, b):
    tmp = b
    b = a
    a = tmp
    return a, b
    
echange(x, y)
print(x, y)

