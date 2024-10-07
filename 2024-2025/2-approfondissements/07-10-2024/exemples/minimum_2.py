def minimum_2(a, b):
    """
    Renvoie le minimum de a et b
    """
    if a <= b:
        m = a
    else:
        m = b
    return m

x = minimum_2(5, 10)
print(x)