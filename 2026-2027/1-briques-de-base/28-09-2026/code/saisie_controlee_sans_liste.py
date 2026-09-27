parfum = input("Choisissez un parfum de glace")

while parfum != "chocolat" and parfum != "vanille" and parfum != "fraise":
    print("Nous n'avons pas ça en stock...")
    parfum = input("Choisissez un parfum de glace")

print("Bien sûr, voici votre glace parfum " + parfum + " !")
