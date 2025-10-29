from random import randint

# Génère une liste de nombres aléatoires
# C'est une compréhension de liste -> hors programme !
liste = [randint(0, 15) for i in range(20)]
# Une version sans compréhension de liste
# (ça fait la même chose que la ligne précédente)
liste = []
for i in range(20):
    liste.append(randint(0, 15))

#print(f"") permet de remplacer les noms de variable
# entre accolades par leur valeur.
print(f"Liste : {liste}")

chaine = "Je suis en CM d'AP1."
print(f"Chaine : {chaine}")

tup = (1, 2, 5, 6, 0, 10)
print(f"Tuple : {tup}")

# Impossible de modifier la valeur d'un tuple
# On dit que les tuples sont *immutables*
# tuple[1] = 13
# tuple.append(12)

# Impossible aussi de modifier la valeur d'une chaîne
# On dit que les chaînes sont aussi *immutables*
# chaine[0] = "A"

def affiche_elements(iterable):
    """Affiche les éléments d'un itérable,
    séparés par des espaces."""
    for element in iterable:
        print(element, end = " ")

def affiche_elements_indices_for(lst):
    """Affiche les éléments d'un itérable,
    séparés par des espaces.
    Implémentation en parcours par indices."""
    for i in range(len(lst)):
        print(lst[i], end = " ")

def affiche_elements_indices_while(lst):
    """Affiche les éléments d'un itérable,
    séparés par des espaces.
    Implémentation par une boucle while."""
    i = 0
    while i < len(lst):
        print(lst[i], end = " ")
        i += 1


print("Liste")
affiche_elements(liste)
# "\n" permet d'aller à la ligne
print("\nChaine")
affiche_elements(chaine)
print("\nTuple")
affiche_elements(tup)

# Vous pouvez expérimenter avec les autres versions de la fonction
# affiche_elements.
