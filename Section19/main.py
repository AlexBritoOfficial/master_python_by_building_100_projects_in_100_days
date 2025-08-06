import random
from turtle import Turtle, Screen

# This is used for the Etch-a-Sketch example
# def forwards():
#     turtle.forward(10)
#
# def backwards():
#     turtle.backward(10)
#
# def left():
#     newheading = turtle.heading() + 10
#     turtle.setheading(newheading)
#
# def right():
#     newheading = turtle.heading() - 10
#     turtle.setheading(newheading)
#
# def clear():
#     turtle.clear()
#     turtle.penup()
#     turtle.home() # turtle.setpos(0,0)
#     turtle.pendown()



if __name__ == "__main__":
    is_race_on = False
    screen = Screen()
    screen.setup(width=800, height=800)

    """
        400
    -400   400
        400
    """
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color")
    colors = ["red", "orange", "brown", "green", "blue", "purple"]
    all_turtles = []

    y_value = 250
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-380, y= y_value)
        y_value = y_value - 100
        all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 400:
            is_race_on = False
            print(f"Turtle {turtle.pencolor()} won")
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. The {winning_color} turtle won the race.")
            break


    # This is used for the Etch-a-Sketch example
    # screen.onkey(key="Up", fun=forwards)
    # screen.onkey(key="Down", fun=backwards)
    # screen.onkey(key="Left", fun=left)
    # screen.onkey(key="Right", fun=right)
    # screen.onkey(key="c", fun=clear)


screen.listen()
screen.exitonclick()