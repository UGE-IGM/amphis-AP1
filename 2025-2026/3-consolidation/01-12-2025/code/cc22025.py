def dans(elem, lst):
    a, b = 0, len(lst) - 1
    while a <= b:
        c = (a + b) // 2
        e = lst[c]
        if e == elem:   return True
        elif e < elem:  a = c + 1
        else:           b = c - 1  
    return False


lst = [0, 1, 2, 3, 4, 5, 9]
elem = 3
dans(elem, lst)