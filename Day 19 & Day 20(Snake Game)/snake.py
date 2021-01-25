
from turtle import Turtle, Screen
MOVE_DISTANCE = 20
STARTING_POINT=[(0,0),(-20,0),(-40,0)]

    

class Snake:
    def __init__(self,):
        
        
        self.snae = []
        
        self.snake_Creator()
        self.head = self.snae[0]
    def snake_Creator(self):
        for i in STARTING_POINT:
            self.extend_screator(i)
            
    def extend_screator(self,i):
         self.sneks = Turtle(shape="square")
         self.sneks.penup()
         self.sneks.color("White")
         self.sneks.goto(i)
         self.snae.append(self.sneks)
    def move(self):
        
            for i in range(len(self.snae) - 1,0,-1):
              self.snae[i].goto(self.snae[i - 1].pos())
            self.snae[0].forward(MOVE_DISTANCE)
            self.snae[0].color("red")
    
    def add(self):
          self.extend_screator(self.snae[-1].pos())
          

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
        
         



















