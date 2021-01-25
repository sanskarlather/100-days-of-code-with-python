from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.setpos(0,280)
        self.hideturtle()
        self.color("White")
        self.inc_score()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",font=('Courier',"12"))
        
    def inc_score(self):
        self.clear()
        self.write(f"Scoreboard:{self.score}",font=('Courier',"12"))
        
        self.score+=1
        