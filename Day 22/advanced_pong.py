from turtle import Turtle, Screen
from advanceg_pong_paddle import Paddle
import time
from advanced_pong_ball import Ball
scr=Screen()
scr.setup(800,600)
scr.bgcolor("Black")
scr.tracer(0)
ball=Ball()
l_pad=Paddle(90,-380,0)
r_pad=Paddle(90,380,0)
b_pad_l=Paddle(0,-170,-280)
t_pad_l=Paddle(0,-170,280)
t_pad_r=Paddle(0,170,280)
b_pad_r=Paddle(0,170,-280)
scr.listen()
#left pad
scr.onkeypress(l_pad.up,"w")
scr.onkeypress(l_pad.down,"s")
#right pad
scr.onkeypress(r_pad.up,"Up")
scr.onkeypress(r_pad.down,"Down")
#left bottom pad
scr.onkeypress(b_pad_l.left,"a")
scr.onkeypress(b_pad_l.right,"d")
#left top pad
scr.onkeypress(t_pad_l.left,"q")
scr.onkeypress(t_pad_l.right,"e")
#lright bottom pad
scr.onkeypress(b_pad_r.left,"Left")
scr.onkeypress(b_pad_r.right,"Right")
#left top pad
scr.onkeypress(t_pad_r.left,".")
scr.onkeypress(t_pad_r.right,"/")
gameOn=True
while gameOn:
    scr.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.distance(t_pad_r)<40 or ball.distance(b_pad_r)<40 or ball.distance(t_pad_l)<40 or ball.distance(b_pad_l)<40:
            ball.bounce_yaxis()
    if ball.distance(l_pad.pos())<40 and ball.xcor()>320 or ball.distance(r_pad.pos())<40 and ball.xcor()<-320:
        ball.move_speed*=.9
        ball.bounce_xaxis()

    











scr.exitonclick()