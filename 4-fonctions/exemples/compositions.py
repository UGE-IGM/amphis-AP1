def minimum(a,b):
    temp = 0
    if a <= b:
        temp = a
    else:
        temp = b
    return temp

def addition(a,b):
    return a+b

def soustraction(a,b):
    return a - b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a // b
    
# m = minimum(5+12, 7*4)
m = minimum(addition(5,12), multiplication(7,4))
# m = minimum(5+12//4, 7*4-3)
m = minimum(addition(5,division(12,4)), soustraction(multiplication(7,4),3))