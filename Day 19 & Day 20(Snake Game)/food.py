from turtle import Turtle
import snake

import random

class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(.5,.5)
		self.color("white")
		self.refresh()

	def refresh(self):
		
		self.goto(random.randint(-280,280),random.randint(-280,280))