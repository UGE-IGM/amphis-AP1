nb_notes = int(input("Combien de notes ?"))
notes_entrees = 0
listes_notes = []
while notes_entrees < nb_notes:
    nouvelle_note = float(input("Entrez une note ?"))
    if nouvelle_note < 0 or nouvelle_note > 20:
        print("Note invalide")
    else:
        listes_notes.append(nouvelle_note)
        notes_entrees = notes_entrees + 1

def calcul_moyenne(liste_notes, nbre_notes):
    somme_notes = 0
    for note in liste_notes:
        somme_notes = somme_notes + note
    moyenne = somme_notes / nbre_notes
    return moyenne

moyenne = calcul_moyenne(listes_notes, nb_notes)

print("La moyenne est ", moyenne)
