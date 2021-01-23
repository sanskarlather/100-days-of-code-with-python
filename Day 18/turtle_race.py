from turtle import Turtle, Screen
import random

turt_lisy = []
for i in range(0,6):
    turt_lisy.append(Turtle(shape="turtle"))
color = ["red","green","yellow","blue","brown","orange"]
flag = 1
scr = Screen()
scr.setup(width=500,height=400)
bid = scr.textinput("BID","Who do you think will win")
flag = 0
ind = 0
for i in range(90,-90,-30):
    turt_lisy[ind].penup()
    turt_lisy[ind].goto(-230,i)
    turt_lisy[ind].color(color[ind])
    ind+=1

while flag == 0:
   
    for i in range(0,6):
        turt_lisy[i].forward(random.randint(1,10))
        if turt_lisy[i].xcor() > 230:
            flag = 1
            if turt_lisy[i].pencolor == bid:
                print("You won")
            else:
                print(turt_lisy[i].pencolor())
scr.exitonclick()