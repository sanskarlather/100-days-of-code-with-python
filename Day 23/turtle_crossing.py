from turtle import Turtle, Screen
import time
import random
import car_manager
scr=Screen()
scr.setup(600,600)
scr.colormode(255)

scr.tracer(0)
car=car_manager.Cars()

gameOn=True
while gameOn:
    time.sleep(0.1)
    scr.update()
    car.create_car() 
    car.move_car()
   
    
    
    










scr.exitonclick()