from turtle import Turtle, Screen

turt=Turtle()
color=[1,2,3,"red","green","salmon","medium purple","wheat","medium spring green","pale turquoise","dark goldenrod"]
for i in range(3,11):
    angle=360/i
    turt.color(color[i])
    for j in range(0,i):
        turt.right(angle)
        turt.forward(100)
scr=Screen()