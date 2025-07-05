import math
from idlelib.search import find_again
import random
from turtle import Turtle, Screen



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

if __name__ == "__main__":
    turtle = Turtle()
    turtle.shape("circle")
    screen = Screen()
    screen.colormode(255)



    for y in range(10):
        for x in range (10):
            turtle.dot(20, random_color())
            turtle.setx(x * 40)
            turtle.sety(y * 40)
            print(turtle.pos())
            turtle.penup()

screen.exitonclick()
