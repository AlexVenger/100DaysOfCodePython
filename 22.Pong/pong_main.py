from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

LEFT_PADDLE_X = -350
RIGHT_PADDLE_X = -LEFT_PADDLE_X

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.tracer(0)

l_paddle = Paddle(LEFT_PADDLE_X)
r_paddle = Paddle(RIGHT_PADDLE_X)
ball = Ball()

screen.listen()
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)

is_game_on = True
while is_game_on:
    screen.update()
    ball.forward(20)
    time.sleep(1)


screen.exitonclick()
