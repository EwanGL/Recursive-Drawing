import turtle
import random

# réglage des paramètres du dessin
turtle.setup(width = 600, height = 600, startx = 100, starty= 100)
turtle.hideturtle()
turtle.colormode(255)
turtle.speed(0)
turtle.pensize(2)
turtle.bgcolor(0,0,0)

# position de départ du tracé
turtle.penup()
turtle.setposition(-150,-150)
turtle.pendown()

def choisir_couleur():
    turtle.color(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        
def escargot(n, longueur):
    choisir_couleur()
    if n >= 1:
        turtle.forward(longueur)
        turtle.left(45)
        escargot(n - 1, longueur*0.8)

escargot(20,200)