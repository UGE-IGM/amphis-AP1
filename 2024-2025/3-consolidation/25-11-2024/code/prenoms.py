# La liste des prénoms
first_names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia", "Jackson", "Mia", "Lucas",
    "Harper", "Evelyn", "Alexander", "Abigail", "Ella", "Michael", "Emily", "Benjamin", "Grace", "Daniel",
    "Mila", "Aiden", "Madison", "James", "Scarlett", "Elizabeth", "David", "Chloe", "Joseph", "Avery",
    "Henry", "Ella", "Samuel", "Lily", "Matthew", "Aria", "Jackson", "Hannah", "Sebastian", "Addison",
    "Avery", "Victoria", "Ethan", "Stella", "Elijah", "Layla", "Gabriel", "Paisley", "Carter", "Natalie",
    "Isaac", "Penelope", "Wyatt", "Riley", "Owen", "Nora", "Caleb", "Zoe", "Luke", "Leah", "Jack", "Sadie",
    "William", "Skylar", "Alexander", "Lillian", "James", "Zoe", "Oliver", "Brooklyn", "Connor", "Luna",
    "Eli", "Savannah", "Logan", "Lily", "Jayden", "Ellie", "Aiden", "Scarlett", "Muhammad", "Aubrey",
    "Mason", "Grace", "Lucas", "Hazel", "Ethan", "Lillian", "Olivia", "Anna", "Avery", "Ellie", "Levi",
    "Nora", "Asher", "Camila", "Leo", "Aurora", "Cameron", "Claire", "Samuel", "Emilia", "Henry", "Chloe",
    "David", "Isabelle", "Joseph", "Sofia", "Owen", "Lucy", "Dylan", "Mila", "Julian", "Layla", "Gabriel",
    "Eleanor", "Anthony", "Hannah", "Isaiah", "Victoria", "Daniel", "Amelia", "Matthew", "Peyton",
    "Carter", "Aria", "Wyatt", "Penelope", "Andrew", "Harper", "Joshua", "Bella", "Christopher", "Claire",
    "Grayson", "Ruby", "Mia", "Reagan", "Joseph", "Madeline", "Samuel", "Margaret", "Isaac", "Gianna",
    "Eli", "Skylar", "Landon", "Gabriella", "Luke", "Piper", "Avery", "Sadie", "Caleb", "Kinsley",
    "Christian", "Zoey", "Hunter", "Samantha", "Jonathan", "Aaliyah", "Adrian", "Madelyn", "Nathan",
    "Nevaeh", "Jackson", "Kennedy", "Nicholas", "Hailey", "Sebastian", "Stella", "Evan", "Kaylee",
    "Jaxon", "Lydia", "Levi", "Taylor", "Jordan", "Brielle", "Aaron", "Mackenzie", "Isaiah", "Kylie",
    "Thomas", "Maya", "Jeremiah", "Jasmine", "Charles", "Sydney", "Josiah", "Audrey", "Hudson", "Adeline",
    "Lincoln", "Alexa", "Ryan", "Ellie", "Nolan", "Molly", "Hunter", "Aubree", "Alex", "Harmony",
    "Easton", "Lila", "Robert", "Claudia", "Nicholas", "Ariana", "Caleb", "Eva", "Grayson", "Alaina"
]

# La première approche (pas vue en CM)
def sans_doublons(liste):
    """
    Renvoie la liste des éléments de `liste` en ayant supprimé les doublons
    (c'est-à-dire que chaque élément apparaît une et une seule fois).
    """
    liste_sans_doublons = []
    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)
    return liste_sans_doublons


def nombre_occurrences(element, liste):
    """
    Compte le nombre de fois qu'un élément apparaît dans une liste.
    Équivalent à liste.count(element).
    """
    nb_occurrences = 0
    for e in liste:
        if e == element:
            nb_occurrences += 1
    return nb_occurrences


def liste_occurrences(liste):
    """
    Compte les occurrences de chaque prénom
    en suivant la première approche décrite dans les slides :
    - Déterminer la liste des prénoms sans doublons
    - Pour chaque prénom dans cette liste, compter combien de fois il apparaît
    """
    liste_sans_doublons = sans_doublons(liste)
    occurrences = []
    for element in liste_sans_doublons:
        nb_occurrences = nombre_occurrences(element, liste)
        occurrences.append([element, nb_occurrences])
    return occurrences


def compte_occurrences_2(liste_prenoms):
    """
    Compte les occurrences de chaque prénom
    en suivant la deuxième approche décrite dans les slides :
    - Créer une liste vide `occurrences`
    - Parcourir la liste des prénoms (avec doublons)
    - Pour chaque prénom `prenom` :
      - S'il n'apparaît pas dans `occurrences`,
        y ajouter une liste `[prenom, 1]`
      - S'il apparaît déjà dans `occurrences`,
        ajouter 1 au nombre d'occurrences correspondant
    """
    occurrences = []
    for prenom in liste_prenoms:
        trouve = False
        for decompte in occurrences:
            if decompte[0] == prenom:
                trouve = True
                decompte[1] += 1
        if not trouve:
            occurrences.append([prenom, 1])
    return occurrences


def compte_occurrences_dict(liste_prenoms):
    """
    Compte les occurrences de chaque prénom
    en suivant l'approche décrite dans les slides avec un dictionnaire :
    - Créer un dictionnaire vide `occurrences`
    - Parcourir la liste des prénoms (avec doublons)
    - Pour chaque prénom `prenom` :
      - S'il n'apparaît pas dans `occurrences`,
        y ajouter un clé `prenom` avec pour valeur `1`
      - S'il apparaît déjà dans `occurrences`,
        ajouter 1 au nombre d'occurrences correspondant
    """
    occurrences = {}
    for prenom in liste_prenoms:
        if prenom not in occurrences:
            occurrences[prenom] = 1
        else:
            occurrences[prenom] += 1
    return occurrences


def compte_occurrences_dict_2(liste_prenoms):
    """
    Compte les occurrences de chaque prénom
    en suivant l'approche décrite dans les slides avec un dictionnaire :
    - Créer un dictionnaire vide `occurrences`
    - Parcourir la liste des prénoms (avec doublons)
    - Pour chaque prénom `prenom` :
      - S'il n'apparaît pas dans `occurrences`,
        y ajouter un clé `prenom` avec pour valeur `1`
      - S'il apparaît déjà dans `occurrences`,
        ajouter 1 au nombre d'occurrences correspondant
    La méthode `dictionnaire.get(valeur, defaut)`
    permet de raccourcir considérablement le code.
    """
    occurrences = {}
    for prenom in liste_prenoms:
        occurrences[prenom] = occurrences.get(prenom, 0) + 1
        # Au lieu de :
        # occurrences[prenom] = occurrences[prenom] + 1 si prenom est déjà présent
        # occurrences[prenom] = 0 + 1 = 1 si prenom est absent (dans ce cas, occurrences.get(prenom, 0) renvoie 0, la valeur donnée par défaut)
    return occurrences


def affiche_prenoms(liste_prenoms):
    """
    Affiche les prénoms présents dans la liste, sans doublons.
    """
    occurrences = compte_occurrences_dict(liste_prenoms)
    print(occurrences.keys())
    

def affiche_prenoms_2(liste_prenoms):
    """
    Affiche les prénoms présents dans la liste, sans doublons,
    en parcourant explicitement les clés du dictionnaire.
    """
    occurrences = compte_occurrences_dict(liste_prenoms)
    for prenom in occurrences.keys():
        print(prenom)


def valeur_maximale(dictionnaire):
    """
    Renvoie la valeur maximale parmi les valeurs du dictionnaires.
    Attention !
    Si les valeurs sont de types différents, la fonction renverra une erreur.
    """
    vmax = 0
    for valeur in dictionnaire.values():
        if valeur > vmax:
            vmax = valeur
    return vmax


### NB : plusieurs clés peuvent être associées à une même valeur.
def trouve_cle_valeur(valeur, dictionnaire):
    """
    Retourne une des clé qui est associée à la valeur donnée,
    et renvoie None si aucune clé n'a cette valeur.
    """
    for (cle, v) in dictionnaire.items():
        if v == valeur:
            return cle


### NB : plusieurs clés peuvent être associées à la valeur maximale.
def trouve_cle_valeur_max(dictionnaire):
    """
    Retourne une des clé qui est associée à la valeur maximale du dictionnaire.
    """
    vmax = valeur_maximale(dictionnaire)
    return trouve_cle_valeur(vmax, dictionnaire)


def trouve_cle_valeur_max_2(dictionnaire):
    """
    Retourne une des clé qui est associée à la valeur maximale du dictionnaire,
    en parcourant le dictionnaire une seule fois.
    """
    cle_max = dictionnaire.keys()[0]
    vmax = dictionnaire[cle_max]
    for (cle, valeur) in dictionnaire.items():
        if valeur > vmax:
            cle_max = cle
            vmax = valeur
    return cle_max


# À comparer avec la fonction ci-dessus
def trouve_indice_max_liste(liste):
    """
    Retourne un indice d'une valeur maximale de la liste,
    en parcourant la liste une seule fois.
    """
    indice_max = 0
    vmax = liste[0]
    for i, valeur in enumerate(liste):
        if valeur > vmax:
            indice_max = i
            vmax = valeur
    return indice_max


# La solution à notre problème
def trouve_plus_courant(liste_prenoms):
    """
    Renvoie le prénom qui apparaît le plus de fois dans la liste,
    à l'aide des fonctions définies précédemment.
    """
    occurrences = compte_occurrences_dict(liste_prenoms)
    prenom_courant = trouve_cle_valeur_max(occurrences)
    return prenom_courant


print(trouve_plus_courant(first_names))
