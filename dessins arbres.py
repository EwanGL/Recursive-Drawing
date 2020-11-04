import turtle
import random

# réglage des paramètres du dessin
turtle.setup(width = 600, height = 600, startx = 100, starty= 100)
turtle.hideturtle()
turtle.colormode(255)
turtle.speed(0)
turtle.pensize(2)
turtle.bgcolor(80,40,0)

# position de départ du tracé
turtle.penup()
turtle.setposition(0,-100)
turtle.pendown()

def choisir_couleur():
    turtle.color(0,random.randint(130,255),0)


def arbre(n, longueur) :
    choisir_couleur()
    angle_gauche = 30
    angle_droite = 45
    if n == 0:
        turtle.forward(longueur)
        turtle.backward(longueur)
    else :
        turtle.forward(longueur)
        turtle.left(angle_gauche)
        arbre(n-1, longueur)
        turtle.right (angle_gauche + angle_droite)
        arbre(n-1, longueur)
        turtle.left(angle_droite)
        turtle.backward(longueur)
        
        
turtle.left(90)
arbre(5,40)