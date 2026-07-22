def dessine_ligne(n, caractere):
    for j in range(n):
        print(caractere, end = '')
    print()
    
    
def dessine_rectangle(m, n, caractere):
    for i in range(m):
        dessine_ligne(n, caractere)
        
        
def dessine_rectangle_rec(m, n, caractere):
    if m == 0:
        pass
    else:
        dessine_ligne(n, caractere)
        dessine_rectangle_rec(m-1, n, caractere)
        

dessine_rectangle_rec(3, 5, '*')