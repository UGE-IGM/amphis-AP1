def minimum(a,b):
    temp = 0
    if a <= b:
        temp = a
    else:
        temp = b
    return temp
    
m = minimum(5+12, 7*4)
m = minimum(5+12//4, 7*4-3)