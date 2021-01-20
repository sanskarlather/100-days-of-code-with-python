import turtle as t
import random
colors=[ (141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199), (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142), (181, 95, 111), (188, 182, 211)]
t.colormode(255)
turt=t.Turtle()
l=1
turt.setheading(225)
turt.penup()
turt.forward(250)
turt.setheading(0)
turt.hideturtle()
for i in range(0,10):
    
    for j in range(0,10):
        turt.pendown()
        turt.dot(20,random.choice(colors))
        turt.penup()
        turt.setx(turt.xcor()+50*l)
    turt.sety(turt.ycor()+50)
    l*=-1
    turt.setx(turt.xcor()+50*l)
    
scr=t.Screen()
scr.exitonclick()





