from turtle import Turtle, Screen
from random import random


timmy = Turtle()
timmy.pensize(20)
k = -250
for i in range(10):
    k += 50

    timmy.teleport(-200, k)
    for j in range(10):
        timmy.pencolor(random(), random(), random())
        timmy.pendown()
        timmy.forward(1)
        timmy.penup()
        timmy.forward(50)

screen = Screen()
screen.exitonclick()
