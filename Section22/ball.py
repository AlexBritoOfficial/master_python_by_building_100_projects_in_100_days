from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.goto(0,0)
        self.X_MOVE = 10
        self.Y_MOVE = 10
        self.penup()
        self.move_speed = 0.1

    def move(self):
        self.goto(x=self.xcor() + self.X_MOVE, y=self.ycor() + self.Y_MOVE)

    def bounce_y(self):
        self.Y_MOVE *= -1

    def bounce_x(self):
        self.X_MOVE *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase_speed(self):
        self.speed() + 10