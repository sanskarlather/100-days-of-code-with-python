from turtle import Turtle
class Score(Turtle):
    def __init__(self,xpos):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.ht()
        self.setpos(xpos,280)
        self.inc_score()
    def inc_score(self):
        self.clear()
        self.write(self.score,align="center",font=('Arial',14))
        self.score+=1