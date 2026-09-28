def est_un_nombre(entree):
    chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    valide = True
    for element in entree:
        if element not in chiffres:
            valide = False  # Ce n'est pas un chiffre le nombre est invalide !
    return valide


def saisie_nombre():
    entree = input("Saisissez un nombre")
    nombre_valide = est_un_nombre(entree)
    while not nombre_valide:
        print("Ce n'est pas un nombre !")
        entree = input("Saisissez un nombre")
        nombre_valide = est_un_nombre(entree)
    return int(nombre)


# On commence par demander le nombre de notes à saisir
nbre_notes = saisie_nombre()

# Maintenant on rentre les notes une par une
liste_nombre = []
for i in range(nbre_notes):
    nombre = saisie_nombre()
    liste_nombre.append(nombre)

print(liste_nombre)
