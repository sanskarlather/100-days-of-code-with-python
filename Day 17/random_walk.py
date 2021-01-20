from turtle import Turtle,Screen
import random
turt=Turtle()
color=["red","green","salmon","medium purple","wheat","medium spring green","pale turquoise","dark goldenrod"]
turt.speed(10000)
turt.width(10)
movemnet=[0,90,180,270]
test=1
while test!=0:
    turt.forward(30)
    turt.color(random.choice(color))
    turt.setheading(random.choice(movemnet))

scr=Screen()