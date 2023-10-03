def f(x):
    temp_f = 1
    return g(x) + temp_f

def g(x):
    temp_g = 2
    return h(x) + temp_g

def h(x):
    temp_h = 3
    return x + temp_h

print(f(8))