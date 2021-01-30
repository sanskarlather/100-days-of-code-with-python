from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,face,xpos,ypos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1,5)
        self.color("white")
        self.seth(face)
        self.setpos(xpos,ypos)
    def up(self):
        self.sety(self.ycor()+10)
    def down(self):
        self.sety(self.ycor()-10)
    def left(self):
        self.setx(self.xcor()-10)
    def right(self):
        self.setx(self.xcor()+10)