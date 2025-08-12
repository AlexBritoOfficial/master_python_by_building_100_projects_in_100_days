from importlib.metadata import packages_distributions
from turtle import Turtle

X_POS = 350
Y_POS = 0


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def moveUp(self):

        print(self.ycor())
        if self.ycor() > 220:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + 20)

    def moveDown(self):
        if self.ycor() < -220:
            pass

        else:
            self.goto(self.xcor(), self.ycor() - 20)
