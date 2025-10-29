def minimum_int(a, b):
    """
    Renvoie le minimum de a et de b, où a et b sont des entiers.
    >>> minimum_int(5, 10)
    5
    >>> minimum_int(10, 12)
    10
    """
    if a > b:
        m = b
    else:
        m = a
    return m

x = 58
y = 78
m = 78
mon_min = minimum_int(x, y)
print(mon_min)
import doctest
doctest.testmod()