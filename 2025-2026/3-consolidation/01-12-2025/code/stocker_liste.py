liste = [True, "abc", 123, "tst", "etc"]


# On écrit la liste
with open("save/ma_liste.txt", "w") as f:
    f.write(str(liste))
    f.write("\n")


# On lit la liste
with open("save/ma_liste.txt", "r") as f:
    contenu = f.read()
    print(contenu)

# Mais comment récupérer la liste d'origine ?
# C'est possible mais très pénible :

def recupere_liste(texte_liste):
    # On enlève les crochets
    texte_sans_guillemets = texte_liste[1:-2]
    # On sépare en découpant à l'aide des virgules
    elements = texte_sans_guillemets.split(", ")
    # Problème : les éléments sont tous considérés comme
    # des chaînes de caractère...
    return elements


# On est bien embêtés !
print(recupere_liste(contenu))


# Solution : utiliser JSON
# Cf https://docs.python.org/3.14/library/json.html#basic-usage (en anglais)