import turtle

t = turtle.Turtle()

reponse = input("Combien de côtés ?")
n = int(reponse)

if n % 2 == 0:
    couleur = "blue"
else:
    couleur = "red"
    
t.color(couleur)

for i in range(n):
    t.forward(50)
    t.left(360 / n)
