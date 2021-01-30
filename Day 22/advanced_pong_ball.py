from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0,0)
        self.move_x=10
        self.move_y=10
        self.move_speed=0.1
        
    def move(self):
        self.goto(self.xcor()+self.move_x,self.ycor()+self.move_y)
    def bounce_xaxis(self):
        self.move_x*=-1
    def bounce_yaxis(self):
        self.move_y*=-1
