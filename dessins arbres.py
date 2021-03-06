import turtle
import random
import time

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

def tree(n, longueur) :
    choisir_couleur()
    angle_gauche = 30
    angle_droite = 45
    if n == 0:
        turtle.forward(longueur)
        turtle.backward(longueur)
    else :
        turtle.forward(longueur)
        turtle.left(angle_gauche)
        tree(n-1, longueur)
        turtle.right (angle_gauche + angle_droite)
        tree(n-1, longueur)
        turtle.left(angle_droite)
        turtle.backward(longueur)

def my_tree(n, length=50):
    choisir_couleur()
    left = 30
    right = 45
    if n == 0:
        turtle.forward(length)
        turtle.backward(length)
    else:
        turtle.forward(length)
        turtle.backward(length/4)
        turtle.left(left)
        my_tree(n-1)
        turtle.right(left)
        turtle.backward(length/4)
        turtle.right(right)
        my_tree(n-1)
        turtle.left(right)
        turtle.backward(length/2)

turtle.left(90)
# tree(3,40)
my_tree(2)
time.sleep(1)