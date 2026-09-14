m = int(input("?"))
n = 0
l = []
while n < m:
    x = float(input("?"))
    if x < 0 or x > 20:
        print("!")
    else:
        l.append(x)
        n = n + 1

def f(a, b):
    s = 0
    for c in a:
        s = s + c
    r = s / b
    return r

r = f(l, m)

print(r)
