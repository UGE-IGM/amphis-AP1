first_names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia",
               "Jackson", "Mia", "Lucas", "Harper", "Evelyn", "Alexander",
               "Abigail", "Ella", "Michael", "Emily", "Benjamin", "Grace",
               "Daniel", "Mila", "Aiden", "Madison", "James", "Scarlett",
               "Elizabeth", "David", "Chloe", "Joseph", "Avery", "Henry",
               "Ella", "Samuel", "Lily", "Matthew", "Aria", "Jackson",
               "Hannah", "Sebastian", "Addison", "Avery", "Victoria", "Ethan",
               "Stella", "Elijah", "Layla", "Gabriel", "Paisley", "Carter",
               "Natalie", "Isaac", "Penelope", "Wyatt", "Riley", "Owen",
               "Nora", "Caleb", "Zoe", "Luke", "Leah", "Jack", "Sadie",
               "William", "Skylar", "Alexander", "Lillian", "James", "Zoe",
               "Oliver", "Brooklyn", "Connor", "Luna", "Eli", "Savannah",
               "Logan", "Lily", "Jayden", "Ellie", "Aiden", "Scarlett",
               "Muhammad", "Aubrey", "Mason", "Grace", "Lucas", "Hazel",
               "Ethan", "Lillian", "Olivia", "Anna", "Avery", "Ellie", "Levi",
               "Nora", "Asher", "Camila", "Leo", "Aurora", "Cameron", "Claire",
               "Samuel", "Emilia", "Henry", "Chloe", "David", "Isabelle",
               "Joseph", "Sofia", "Owen", "Lucy", "Dylan", "Mila", "Julian",
               "Layla", "Gabriel", "Eleanor", "Anthony", "Hannah", "Isaiah",
               "Victoria", "Daniel", "Amelia", "Matthew", "Peyton", "Carter",
               "Aria", "Wyatt", "Penelope", "Andrew", "Harper", "Joshua",
               "Bella", "Christopher", "Claire", "Grayson", "Ruby", "Mia",
               "Reagan", "Joseph", "Madeline", "Samuel", "Margaret", "Isaac",
               "Gianna", "Eli", "Skylar", "Landon", "Gabriella", "Luke",
               "Piper", "Avery", "Sadie", "Caleb", "Kinsley", "Christian",
               "Zoey", "Hunter", "Samantha", "Jonathan", "Aaliyah", "Adrian",
               "Madelyn", "Nathan", "Nevaeh", "Jackson", "Kennedy", "Nicholas",
               "Hailey", "Sebastian", "Stella", "Evan", "Kaylee", "Jaxon",
               "Lydia", "Levi", "Taylor", "Jordan", "Brielle", "Aaron",
               "Mackenzie", "Isaiah", "Kylie", "Thomas", "Maya", "Jeremiah",
               "Jasmine", "Charles", "Sydney", "Josiah", "Audrey", "Hudson",
               "Adeline", "Lincoln", "Alexa", "Ryan", "Ellie", "Nolan",
               "Molly", "Hunter", "Aubree", "Alex", "Harmony", "Easton",
               "Lila", "Robert", "Claudia", "Nicholas", "Ariana", "Caleb",
               "Eva", "Grayson", "Alaina"]


def valeurs_uniques(lst):
    """Renvoie la liste lst, où chaque valeur apparait une et une seule fois"""
    valeurs_uniques_lst = []
    for elt in lst:
        if elt not in valeurs_uniques_lst:
            valeurs_uniques_lst.append(elt)
    return valeurs_uniques_lst


def compter_occurrences(valeur, lst):
    """Renvoie le nombre de fois qu'element apparait dans lst)"""
    res = 0
    for elt in lst:
        if elt == valeur:
            res += 1
    return res


def liste_des_occurrences(lst):
    occurrences = []
    uniques = valeurs_uniques(lst)
    for valeur in uniques:
        occ = compter_occurrences(valeur, lst)
        occurrences.append((valeur, occ))
    return occurrences


def dico_des_occurrences(lst):
    dico_occurrences = {}
    for element in lst:
        if element in dico_occurrences:
            dico_occurrences[element] += 1
        else:
            dico_occurrences[element] = 1
    return dico_occurrences


def liste_vers_dictionnaire(lst):
    dico = {}
    for (cle, valeur) in lst:
        dico[cle] = valeur
    return dico


def main():
    liste_occurrences = liste_des_occurrences(first_names)
    dico_occurrences = dico_des_occurrences(first_names)
    dico_occurrences_bis = liste_vers_dictionnaire(liste_occurrences)
    print(liste_occurrences)
    print(dico_occurrences)
    print(dico_occurrences_bis)


if __name__ == "__main__":
    main()
