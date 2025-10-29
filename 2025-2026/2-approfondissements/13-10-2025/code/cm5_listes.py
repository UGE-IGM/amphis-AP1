lst = ["coucou", "les", "gens"]

def recherche_parcours_par_indice(element, liste):
    for indice in range(len(liste)):
        if element == liste[indice]:
            return True
    return False

def recherche_parcours_par_elements(element, liste):
    for elt_lst in liste:
        if element == elt_lst:
            return True
    return False

def recherche_indice(element, liste):
    for i, elt_lst in enumerate(liste):
        if element == elt_lst:
            return i
    return None

def recherche_indice_parcours_indice(element, liste):
    for i in range(len(liste)):
        if element == liste[i]:
            return i
    return None

def maximum(liste):
    # Au début, on suppose que le max est le premier élément
    max_l = liste[0]
    # On regarde chaque élément
    for elem in liste:
        # Si on en trouve un plus grand:
        if elem > max_l:
            # On met à jour le maximum
            max_l = elem
    # À la fin, on est forcément tombé sur la valeur max à un moment.
    # On renvoie donc max_l
    return max_l


def somme(liste):
    # Au début, la somme vaut 0 vu qu'on n'a vu personne
    s = 0
    # Pour chaque élément :
    for elem in liste:
        # On l'ajoute à la somme
        s += elem
    # À la fin, on renvoie la somme s
    return s

# On veut maintenant si une liste ne contient
# que des nombres pairs
def tous_pairs(liste):
    # On regarde chaque élément
    for elem in liste:
        # Si on en trouve un qui n'est pas pair :
        if elem % 2 != 0:
            # On peut d'emblée conclure que la liste
            # ne contient pas que des entiers pairs
            return False
    # Si on n'a vu aucun entier non pair, on renvoie True
    return True

# Enfin, on veut, à partir d'une liste,
# renvoyer la liste des entiers pairs qu'elle contient
def liste_pairs(liste):
    nouvelle_liste = []
    # On parcourt chaque élément
    for elem in liste:
        # Si on en trouve un pair
        if elem % 2 == 0:
            # On l'ajoute à la liste
            nouvelle_liste.append(elem)
    return nouvelle_liste
        

### Et les chaînes de caractères ?


ma_chaine = "salut tout le monde"

# Observation : c'est exactement la même fonction que
# recherche_parcours_par_indice !!!
def recherche_caractere(carac, chaine):
    for indice in range(len(chaine)):
        if carac == chaine[indice]:
            return True
    return False


ma_liste = [2, 4, 8, 2, 0, 1, 56, 32]

def tous_pairs_live_while(liste):
    i = 0
    while i < len(liste):
        if liste[i] % 2 != 0:
            return False
        i += 1
    return True

def tous_pairs_live_for(liste):
    for elem in liste:
        if elem % 2 != 0:
            return False
    return True

ma_liste_2 = [100, 210, 50, 60, 200]

def calcul_du_max_live(liste):
    max_pour_linstant = liste[0]
    for elem in liste:
        if elem > max_pour_linstant:
            max_pour_linstant = elem
    return max_pour_linstant

## On passe aux chaînes de caractères

def est_en_majuscules(chaine):
    for caractere in chaine:
        if not caractere.isupper():
            return False
    return True


ma_chaine = "salut tout le Monde"

def passer_en_majuscules(chaine):
    chaine = ""
    for caractere in chaine:
        chaine = chaine + caractere.upper()
    return chaine

def est_un_nombre(chaine):
    for caractere in chaine:
        if not caractere.isnumeric():
            return False
    return True

def inverser_minuscules_majuscules(phrase):
    nouvelle_phrase = ""
    for caractere in phrase:
        if caractere.islower():
            nouvelle_phrase = nouvelle_phrase + caractere.upper()
        elif caractere.isupper():
            nouvelle_phrase = nouvelle_phrase + caractere.lower()
        else:
            nouvelle_phrase = nouvelle_phrase + caractere
    return nouvelle_phrase
            
ma_phrase = "SaLuT tout le MONDE !!!§§§§§329342980484320924"
ma_phrase_inversee = inverser_minuscules_majuscules(ma_phrase)
print(ma_phrase_inversee)


# Les listes de listes

# Elles peuvent représenter des matrices
# Exemple
# 0  5  8  12
# 5  4  2  1
# 0 -1 25  2
# Peut être représentée par
ligne1 = [0, 5, 8, 12]
ligne2 = [5, 4, 2, 1]
ligne3 = [0, -1, 25, 2]
matrice = [ligne1, ligne2, ligne3]
# Ou, plus directement :
matrice = [[0,  5,  8, 12],
           [5,  4,  2,  1],
           [0, -1, 25,  2]]
           
# On veut savoir si un élément est dans la matrice :
# Rappel : on a la fonction recherche_parcours_par_elements(element, liste)
# qui recherche un élément dans *une seule* liste
def est_dans_la_matrice_explicite(element, matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if element == matrice[i][j]:
                return True
    return False

def est_dans_la_matrice(element, matrice):
    for i in range(len(matrice)):
        if recherche_parcours_par_elements(element, matrice[i]):
            return True
    return False
    