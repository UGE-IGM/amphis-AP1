def f(x):
    return g(x) + 1

def g(y):
    return h(y) + 2

def h(z):
    return z * 2

print(f(10))