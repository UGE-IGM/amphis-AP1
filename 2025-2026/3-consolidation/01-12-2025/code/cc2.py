lst1 = ["Alice", "Bob", "Charlie"]
lst2 = ["Alice", "Bob", "Charlie", "Bob", "Bob", "Alice"]


def decompte_votes(liste_votes):
    votes = {}
    for nom in liste_votes:
#         if nom in votes:
#             votes[nom] += 1
#         else:
#             votes[nom] = 1
        votes[nom] = 1 + votes.get(nom, 0)
    return votes


print(decompte_votes(lst1))
print(decompte_votes(lst2))



# Mini-problème
grille_ortho = [['s', 'a', 't', 'i', 'n'],
                ['e', 'c', 'r', 'i', 't'],
                ['b', 'o', 'a', 'n', 'z'],
                ['u', 't', 'i', 'l', 'e'],
                ['m', 'e', 'n', 'a', 'p']]


def demande_mot():
    mot = input("Entrez un mot de 5 lettres svp : ")
    while len(mot) != 5 and mot != "fin":
        mot = input("Entrez un mot de 5 lettres svp : ")
        if len(mot) != 5 and mot != "fin":
            print("Ce mot ne fait pas 5 lettres.")
    return mot


def demande_mot_2():
    mot = input("Entrez un mot de 5 lettres svp : ")
    while len(mot) != 5:
        if mot == "fin":
            return mot
        else:
            print("Ce mot ne fait pas 5 lettres.")
            mot = input("Entrez un mot de 5 lettres svp : ")
    return mot


def demande_mot_2():
    while True:
        mot = input("Entrez un mot de 5 lettres svp : ")
        if len(mot) == 5 or mot == "fin":
            return mot
        print("Ce mot ne fait pas 5 lettres.")


def demande_mot_rec():
    mot = input("Entrez un mot de 5 lettres svp : ")
    if len(mot) == 5 or mot == "fin":
        return mot
    else:
        print("Ce mot ne fait pas 5 lettres.")
        return demande_mot_rec()
    

def affiche_grille(grille):
    for ligne in grille:
        for elem in ligne:
            print(elem, end=" ")
        print()
        
    
def affiche_grille_join(grille):
    for ligne in grille:
        print(" ".join(ligne))
        
        
def verifie_horizontal(grille, mot):
    for ligne in grille:
        if "".join(ligne) == mot:
            return True
        
    
def verifie_vertical(grille, mot):
    for i in range(len(grille[0])):
        for j in range(len(grille)):
            if grille[j][i] != mot[j]:
                break
            if j == len(grille) - 1:
                return True
    return False


def verifie_vertical(grille, mot):
    for i in range(len(grille[0])):
        colonne_egal_mot = True
        for j in range(len(grille)):
            if grille[j][i] != mot[j]:
                colonne_egal_mot = False
            if colonne_egal_mot:
                return True
    return False
    
    
def verifie_diagonal(grille, mot):
    for i in range(len(grille)):
        if grille[i][i] != mot[i]:
            return False
    return True


def verifie(grille, mot):
    return (verifie_horizontal(grille, mot) or
            verifie_vertical(grille, mot) or
            verifie_diagonal(grille, mot))