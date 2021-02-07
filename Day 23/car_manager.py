from turtle import Turtle
import random
START_POS=300

class Cars(Turtle):
    def __init__(self):
       
        self.cars_list=[]
        
        
        

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            newcar=Turtle("square")
            newcar.hideturtle()
        
            self.red=random.randint(1,255)
            self.blue=random.randint(1,255)
            self.green=random.randint(1,255)
            newcar.color(self.red,self.blue,self.green)
            newcar.shapesize(1.25,2.5)
            newcar.penup()
            newcar.sety(random.randint(-250,250))
            newcar.setx(START_POS)
            newcar.showturtle()
            self.cars_list.append(newcar)
    def move_car(self):
        for i in self.cars_list:
            i.forward(-5)
        
    def move_y(self,y):
        self.sety(y)
