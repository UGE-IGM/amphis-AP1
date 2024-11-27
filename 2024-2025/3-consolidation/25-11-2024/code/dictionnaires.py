# Définition de dictionnaires
dict_vide = {}
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 2, 'd': 12}
dict3 = {'a': [1, 2], 'd': 12}

# Ajouter une valeur
dict3['z'] = 25
# On peut avoir des clés d'un type différent
# Même si ce n'est généralement pas recommandé
dict3[True] = 13
# Idem pour les valeurs
dict3[False] = [1, "Coucou"]

print(dict3)

# Fusionne deux dictionnaires
dict1.update(dict2)
print(dict1)

# Accéder à une clé qui n'existe pas provoque une erreur
dict3['c']  # KeyError
