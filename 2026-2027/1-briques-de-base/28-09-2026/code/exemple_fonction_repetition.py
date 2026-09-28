chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# On commence par demander le nombre de notes à saisir
nbre_notes = input("Combien de nombres voulez-vous saisir ?")


est_un_chiffre = False
while not est_un_chiffre: # On vérifie qu'on a bien rentré un nombre
    # Pour ce faire, on vérifie, que chaque élément est un chiffre
    valide = True
    for element in nbre_notes:
        if element not in chiffres:
            valide = False # Ce n'est pas un chiffre le nombre est invalide !
    # Si c'est incorrect, on recommence
    if not valide:
        print("Ce n'est pas un nombre!")
        nbre_notes = input("Combien de nombres voulez-vous saisir ?")

nbre_notes = int(input(nbre_notes)) # On oublie pas de convertir !

# Maintenant on rentre les notes une par une
liste_nombre = []
for i in range(nbre_notes):
    nombre = input("Saisissez une note")

    est_un_chiffre = False
    while not est_un_chiffre:  # On doit recommencer la vérification ...
        valide = True
        for element in nbre_notes:
            if element not in chiffres:
                valide = False
        if not valide:
            print("Ce n'est pas un nombre!")
            nombre = input("Combien de nombres voulez-vous saisir ?")
    nombre = int(nombre) # On oublie pas de convertir !

    liste_nombre.append(nombre)

print(liste_nombre)