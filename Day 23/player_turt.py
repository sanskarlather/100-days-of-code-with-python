from turtle import Turtle
class Players(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.sety(-280)
    def up(self):
        self.forward(10)
    def down(self):
        self.backward(10)