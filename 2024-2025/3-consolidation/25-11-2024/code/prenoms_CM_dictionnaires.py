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


def dico_des_occurrences(lst):
    dico_occurrences = {}
    for valeur in lst:
        if valeur in dico_occurrences:
            dico_occurrences[valeur] += 1
        else:
            dico_occurrences[valeur] = 1
    return dico_occurrences


def main():
    occurrences = dico_des_occurrences(first_names)
    print(occurrences)
    print(occurrences)


if __name__ == "__main__":
    main()
