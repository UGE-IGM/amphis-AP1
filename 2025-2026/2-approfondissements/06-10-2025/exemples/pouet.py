def pouet(x):
    if len(x) < 8:
      return False
    elif x == "00000000":
      return False
    elif x == "motdepasse":
      return False
    else:
      return True

solide = False
while (not solide):
  mdp = input("Veuillez entrer un mot de passe solide : ")
  solide = pouet(mdp)
print("Bravo !")
