def sauvegarde(notes, nom_fichier):
    """
    Paramètres :
    - notes (int list) : la liste des notes
    - nom_fichier (str) : le nom du fichier
    Sauvegarde les notes données dans le fichier,
    séparées par des espaces.
    """
    f = open(nom_fichier, 'w')
    for note in notes:
        f.write(str(note))
        f.write(' ')
    f.close()


def recupere_sauvegarde(nom_fichier):
    """
    Paramètres :
    - nom_fichier (str) : le nom du fichier
    Récupère les notes sauvegardées dans le fichier donné.
    Les notes doivent être séparées par des espaces.
    """
    f = open(nom_fichier, 'r')
    text = f.read()
    liste_notes_str = text.split(' ')
    print(liste_notes_str)
    liste_notes = []
    for note_str in liste_notes_str:
        if not note_str.isdigit():
            print("Il y a un problème avec cette note : ", note_str)
        else:
            liste_notes.append(int(note_str))
    return liste_notes


def main():
    mes_notes = [12, 18, 15, 9, 8]
    mon_nom_fichier = "notes.txt"
    sauvegarde(mes_notes, mon_nom_fichier)
    liste_notes = recupere_sauvegarde(mon_nom_fichier)
    print(liste_notes)


if __name__ == "__main__":
    main()
