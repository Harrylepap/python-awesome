import turtle
import random

harry = turtle.Turtle()
harry.speed(0)

couleurs = ["gold", "red", "blue", "green", "pink", "turquoise", "purple", "orange", "white"]
longueur = 500
angle = 91
circonference = 10

for taille in range(longueur):
	couleur = random.choice(couleurs)
	harry.pencolor(couleur)
	harry.fillcolor(couleur)
	harry.penup()
	harry.forward(taille)
	harry.left(angle)
	harry.begin_fill()
	harry.circle(circonference)
	harry.end_fill()

turtle.exitonclick()
