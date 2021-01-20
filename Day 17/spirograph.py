import turtle as t
import random
t.colormode(255)
turt=t.Turtle()
turt.speed("fastest")
def rand_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tup_c=(r,g,b)
    return tup_c
def draw_spirograph(gap):
    for i in range(int(360/gap)):
        
        t.circle(100)   
        head =t.heading()
        t.setheading(head+gap)
        t.color(rand_color())

draw_spirograph(10)
scr=t.Screen()
scr.exitonclick()