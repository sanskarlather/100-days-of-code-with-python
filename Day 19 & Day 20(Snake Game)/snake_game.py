import time
import random
from snake import Snake
from turtle import Turtle, Screen
import food
import score
scr=Screen()
scr.setup(600,600)
scr.bgcolor("Black")
scr.title("snek game")
scr.tracer(0)
scores=score.ScoreBoard()
foods=food.Food()
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
    
    if snek.head.distance(foods)<15:
        foods.refresh()
        scores.inc_score()
        snek.add()
    if snek.head.xcor()>280 or snek.head.xcor()<-280 or snek.head.ycor()>280 or snek.head.ycor()<-280:
        
        gameOn=False
        scores.game_over()
    for i in snek.snae:
        if i==snek.head:
            pass
        elif snek.head.distance(i)<1:
              gameOn=False
              scores.game_over()  
    


















scr.exitonclick()