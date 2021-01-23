import time
from snake import Snake
from turtle import Turtle, Screen
scr=Screen()
scr.setup(600,600)
scr.bgcolor("Black")
scr.title("snek game")
scr.tracer(0)

snek=Snake()
scr.listen()
scr.onkey(snek.up,"Up")
scr.onkey(snek.down,"Down")
scr.onkey(snek.left,"Left")
scr.onkey(snek.right,"Right")
gameOn=True
while gameOn:
    scr.update()
    time.sleep(0.1)
    snek.move()
        
    
    



















scr.exitonclick()