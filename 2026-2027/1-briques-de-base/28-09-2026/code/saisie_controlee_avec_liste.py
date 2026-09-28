parfums = ["chocolat", "vanille", "fraise"]
parfum = input("Choisissez un parfum de glace")

while parfum not in parfums:
    print("Nous n'avons pas ça en stock...")
    parfum = input("Choisissez un parfum de glace")

print("Bien sûr, voici votre glace parfum " + parfum + " !")
