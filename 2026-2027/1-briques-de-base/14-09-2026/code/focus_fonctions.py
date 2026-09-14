










def calcul_moyenne(liste_notes, nbre_notes):
    somme_notes = 0
    for note in liste_notes:
        somme_notes = somme_notes + note
    moyenne = somme_notes / nbre_notes
    return moyenne

moyenne = calcul_moyenne(listes_notes, nb_notes)


