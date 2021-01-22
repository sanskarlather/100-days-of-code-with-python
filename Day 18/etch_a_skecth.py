import turtle as t
turt=t.Turtle()
scr=t.Screen()
scr.listen()
def fwd():
    turt.forward(10)
def bwd():
    turt.backward(10)
def clock():
    turt.setheading(turt.heading()-10)
def anticlock():
    turt.setheading(turt.heading()+10)

scr.onkeypress(fwd,"w")
scr.onkeypress(bwd,"s")
scr.onkeypress(clock,"d")
scr.onkeypress(anticlock,"a")
scr.onkey(scr.reset,"c")
scr.exitonclick()
