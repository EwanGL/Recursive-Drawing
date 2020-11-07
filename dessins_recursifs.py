import turtle
import random
import time

# réglage des paramètres du dessin
turtle.setup(width = 600, height = 600, startx = 100, starty= 100)
turtle.hideturtle()
turtle.colormode(255)
turtle.speed(0)
turtle.pensize(2)
turtle.bgcolor(0,0,0)
#turtle.left(90) # if execute staires

# position de départ du tracé
turtle.penup()
turtle.setposition(-150,-150)
turtle.pendown()

def choisir_couleur():
    turtle.color(random.randint(1,255),random.randint(1,255),random.randint(1,255))

# Mission1:     
def escargot(n, longueur):
    choisir_couleur()
    if n >= 1:
        turtle.forward(longueur)
        turtle.left(45)
        escargot(n - 1, longueur*0.8)

def staires(n, length):
    choisir_couleur()
    if n>=1:
        turtle.right(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
    staires(n-1, length*0.8)

def triangles(n, length):
    choisir_couleur()
    if n>=1:
        for _ in range(3):
            turtle.forward(length)
            turtle.right(120)
        turtle.forward(length//2)
        turtle.right(60)
        triangles(n-1, length//2)

# escargot(20,200)
# staires(5,60)
# triangles(5, 200)

# Mission2:
def cote(n, length):
    choisir_couleur()
    if n ==1:
        turtle.forward(length)
    else:
        cote(n-1, length/3)
        turtle.left(60)
        cote(n-1, length/3)
        turtle.right(120)
        cote(n-1, length/3)
        turtle.left(60)
        cote(n-1, length/3)


cote(3,100)
turtle.penup()
time.sleep(1)