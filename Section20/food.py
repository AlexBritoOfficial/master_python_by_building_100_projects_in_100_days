import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def generateRandomNumber(self):
        return random.randint(-280,280)

    def refresh(self):
        self.goto(x=self.generateRandomNumber(), y=self.generateRandomNumber())
