from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

screen.update()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.grow()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        is_game_on = False
        scoreboard.game_over()

    for piece in snake.snake_pieces[1:]:
        if snake.head.distance(piece) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
