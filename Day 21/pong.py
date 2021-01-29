from turtle import Turtle, Screen
import paddle
import ball
import time
import scoreboard

scr=Screen()
scr.setup(800,600)
scr.bgcolor("Black")
dash=Turtle()
dash.penup()
dash.ht()
dash.speed(0)
dash.color("white")
dash.sety(300)
dash.seth(270)
dash.pendown()
dash.forward(10)
scr.listen()
scr.tracer(0)
t=-1
l_socre=scoreboard.Score(-20)
r_socre=scoreboard.Score(20)

balls=ball.Ball()

paddle_l=paddle.Paddle(350,0)
paddle_r=paddle.Paddle(-350,0)
scr.onkeypress(paddle_l.up,"Up")
scr.onkeypress(paddle_l.down,"Down")
scr.onkeypress(paddle_r.up,"w")
scr.onkeypress(paddle_r.down,"s")

for i in range(300,-300,-10):
    if (t==1):
        dash.pendown()
        dash.forward(10)
    else:
        dash.penup()
        dash.forward(10)
    t*=-1


gameOn=True
while gameOn:
    time.sleep(balls.move_speed)
    scr.update()
    balls.move()
    if balls.ycor()>280 or balls.ycor()<-280:
            balls.bounce()
    if balls.distance(paddle_l.pos())<40 and balls.xcor()>320 or balls.distance(paddle_r.pos())<40 and balls.xcor()<-320:
        balls.move_speed*=.9
        balls.bounce_pad()

    if balls.xcor()>380:
        l_socre.inc_score()
        balls.reset_ball()
    if balls.xcor()<-380:
        r_socre.inc_score()
        balls.reset_ball()
















scr.exitonclick()