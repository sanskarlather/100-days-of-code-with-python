from turtle import Turtle, Screen
import time
import random
import car_manager
from player_turt import Players
scr=Screen()
scr.setup(600,600)
scr.colormode(255)
player=Players()
scr.listen()
scr.onkeypress(player.up,"Up")
scr.onkeypress(player.down,"Down")

scr.tracer(0)
car=car_manager.Cars()

gameOn=True
while gameOn:
    time.sleep(0.1)
    scr.update()
    car.create_car() 
    car.move_car()
    for i in car.cars_list:
       if player.distance(i)<20:
        gameOn=False
   
    
    
    










scr.exitonclick()