
from turtle import Turtle, Screen
MOVE_DISTANCE = 20


    

class Snake:
    def __init__(self,):
        
        
        self.snae = []
        
        self.snake_Creator()
        self.head = self.snae[0]
    def snake_Creator(self):
        for i in range(0,3):
            self.sneks = Turtle(shape="square")
            self.snae.append(self.sneks)
           
            self.snae[i].penup()
            self.snae[i].color("White")
            print(self.snae[i].color())
            self.snae[i].setx(i * (-20))
        
    def move(self):
        
            for i in range(len(self.snae) - 1,0,-1):
              self.snae[i].goto(self.snae[i - 1].pos())
            self.snae[0].forward(MOVE_DISTANCE)
            

    def up(self):
       if self.head.heading()!=190:
         self.head.setheading(90)
        
        
    def down(self):
       if self.head.heading()!=90:
        self.head.setheading(270)
        
    def left(self):
       if self.head.heading()!=0:
        self.head.setheading(180)
        
    def right(self):
        if self.head.heading()!=180:
         self.head.setheading(0)
        
         



















