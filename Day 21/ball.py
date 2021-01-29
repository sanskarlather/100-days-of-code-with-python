from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movex=10
        self.movey=10
        self.move_speed=0.1
    def move(self):
         self.goto(self.xcor()+self.movex,self.ycor()+self.movey)
    def bounce(self):
        self.movey*=-1
    def bounce_pad(self):
        
        self.movex*=-1
    def reset_ball(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.movex*=-1