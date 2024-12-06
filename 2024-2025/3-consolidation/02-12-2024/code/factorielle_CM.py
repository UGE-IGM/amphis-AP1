# factorielle(n) : si n = 0, factorielle(0) = 1,
#                  sinon c'est n * factorielle(n-1)
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)


# factorielle_iter(n) = 1 * 2 * 3 * 4 *... * (n-1) * n
def factorielle_iter(n):
    f = n
    for i in range(2, n):
        f *= i
    return f


print(factorielle(5))
print(factorielle_iter(5))
