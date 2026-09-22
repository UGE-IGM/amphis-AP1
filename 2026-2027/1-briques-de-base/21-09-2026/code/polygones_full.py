# Importer Turtle
import turtle

#Initialiser Turtle
t = turtle.Turtle()

# Demander le nombre de cotes a l'utilisateur
reponse = input("Combien de côtés ? ")
n = int(reponse)

# Décider de la couleur en fonction de la parité
# du nombre de côtés
if n % 2 == 0:
    couleur = "blue"
else:
    couleur = "red"
t.color(couleur)

#Dessiner le polygone

i = 0
while i != n:
    t.forward(100)
    t.left(360//n)
    i = i + 1
