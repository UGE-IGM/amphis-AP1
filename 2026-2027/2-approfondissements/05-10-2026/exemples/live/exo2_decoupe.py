def saisie_notes(nombre_notes):
    """Demande à l'utilisateur de saisir `nombre_notes` notes."""
    notes = []
    for i in range(nombre_notes):
        note = float(input(f"Note {i+1} : "))  # on convertit en flottant pour avoir les décimales
        notes.append(note)                     # on ajoute la note à la liste
    return notes


def calcule_moyenne(notes):
    """Calcule la moyenne de la liste de notes `notes`."""
    somme = 0
    for note in notes:
        somme += note              # on additionne toutes les notes
    moyenne = somme / len(notes)   # puis on divise par le nombre de notes
    return moyenne



def maximum_notes(notes):
    """Calcule la note maximum."""
    maximum = notes[0]             # on part de la première note comme valeur max provisoire
    for note in notes:
        if note > maximum:         # si on trouve une note plus grande
            maximum = note         # on met à jour la valeur max
    return maximum


def minimum_notes(notes):
    """Calcule la note minimum"""
    minimum = notes[0]             # même idée, mais pour le minimum
    for note in notes:
        if note < minimum:
            minimum = note
    return minimum


# On demande combien de notes l'utilisateur souhaite saisir
n = int(input("Combien de notes ? "))
# On lui demande ensuite de saisir les notes
mes_notes = saisie_notes(n)

# On calcule les résultats
moyenne = calcule_moyenne(mes_notes)
maximum = maximum_notes(mes_notes)
minimum = minimum_notes(mes_notes)

# On affiche les résultats
print("Moyenne :", moyenne)
print("Note la plus haute :", maximum)
print("Note la plus basse :", minimum)