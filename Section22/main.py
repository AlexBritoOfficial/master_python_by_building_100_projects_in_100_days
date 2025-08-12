from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()

    screen.onkeypress(key="Up", fun=r_paddle.moveUp)
    screen.onkeypress(key="Down", fun=r_paddle.moveDown)
    screen.onkeypress(key="w", fun=l_paddle.moveUp)
    screen.onkeypress(key="s", fun=l_paddle.moveDown)

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
            ball.increase_speed()

        if ball.xcor() > 380:
            scoreboard.l_point()
            ball.reset()

        if ball.xcor() < -380:
            scoreboard.r_point()
            ball.reset()




    screen.exitonclick()
