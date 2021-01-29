from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.setpos(x_pos,0)
        self.speed(0)
        
    def up(self):
        self.sety(self.ycor()+10)
    def down(self):
        self.sety(self.ycor()-10)

