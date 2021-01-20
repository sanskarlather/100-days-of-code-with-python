from turtle import Turtle,Screen
import turtle
import random
turtle.colormode(255)
turt=Turtle()
movement=[0,90,180,270]
turt.width(10)
def rand_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tup_c=(r,g,b)
    return tup_c
for i in range(0,1000):
    turt.forward(30)
    turt.setheading(random.choice(movement))
    turt.pencolor(rand_color())