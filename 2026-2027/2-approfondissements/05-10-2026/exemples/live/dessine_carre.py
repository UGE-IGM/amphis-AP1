def dessine_ligne(longueur, carac):
    print(longueur * carac)
    

def dessine_carre(longueur, carac):
    for i in range(longueur):
        dessine_ligne(longueur, carac)
        
def dessine_rectangle(hauteur, largeur, carac):
    for i in range(hauteur):
        dessine_ligne(largeur, carac)
    
        
        
dessine_carre(12, '*')

print()

dessine_rectangle(5, 12, '*')