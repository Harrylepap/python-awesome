import turtle
import random

window = turtle.Screen()
window.setup(1000, 500, 260, 100)

def creation_fleur_get_position(x, y):
	creation_fleur(x, y, 
			random.randint(3, 10), 
			[random.random() for _ in range(3)], 
			[random.random() for _ in range(3)]
			)

def creation_fleur(x, y, nombre_de_petals, couleur_petal, couleur_central):
	fleur = turtle.Turtle()
	fleur.hideturtle()
	fleur.penup()
	fleur.setx(x)
	fleur.sety(y)
	fleur.color(couleur_petal)
	for taille in range(nombre_de_petals):
		fleur.forward(40)
		fleur.dot(200)
		fleur.forward(-40)
		fleur.right(360/nombre_de_petals)
	fleur.color(couleur_central)
	fleur.dot(75)
window.onclick(creation_fleur_get_position)
window.listen()

turtle.done()
print("Ok")
