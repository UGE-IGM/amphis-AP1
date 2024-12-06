# Ce programme itératif :
n = 0
while n < 10:
    print(n)
    n += 1


# Est équivalent à cette fonction récursive :
def f(n):
    if n == 10:
        pass
    else:
        print(n)
        f(n+1)


# Appelée sur n = 0
f(0)
