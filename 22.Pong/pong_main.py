from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=l_paddle.go_up)
screen.onkeypress(key="s", fun=l_paddle.go_down)
screen.onkeypress(key="Up", fun=r_paddle.go_up)
screen.onkeypress(key="Down", fun=r_paddle.go_down)
screen.onkey(key="space", fun=ball.start_move)

is_game_on = True
while is_game_on:
    screen.update()
    # Bounce on wall touch
    if abs(ball.ycor()) > 280:
        ball.bounce()
    # Bounce on paddle touch
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -320) or (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.paddle_bounce()
    # Restart if ball is beyond the board border
    if ball.xcor() > 350:
        ball.l_off_the_board()
        scoreboard.l_point()
    if ball.xcor() < -350:
        ball.r_off_the_board()
        scoreboard.r_point()
    # Condition to move the ball
    if ball.is_moving:
        ball.forward(20)
    time.sleep(ball.move_speed)


screen.exitonclick()
