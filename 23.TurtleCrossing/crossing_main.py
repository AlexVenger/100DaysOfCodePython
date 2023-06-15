from turtle import Screen
from player_turtle import PlayerTurtle
from scoreboard import Scoreboard
from car import Car
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

difficulty_level = screen.numinput(title="Difficulty", prompt="Choose difficulty level. Type any integer: ")

player = PlayerTurtle()
scoreboard = Scoreboard(difficulty_level)
car_number = 2
cars_to_remove = []
cars = {1: Car()}

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

iteration = 0
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1 * 0.9 ** (scoreboard.level - 1))
    for i in cars:
        cars[i].forward(20)
        # Check if car crashed
        if cars[i].distance(player) < 20 and abs(player.ycor() - cars[i].ycor()) < 15:
            is_game_on = False
            scoreboard.game_over()
        # Remove car that left the board
        if cars[i].xcor() < -350:
            cars[i].hideturtle()
            cars_to_remove.append(i)
    # Go to next level
    if player.ycor() > 250:
        player.next_level()
        scoreboard.update_scoreboard()
    # Add new car
    if iteration >= scoreboard.car_timer:
        cars[car_number] = Car()
        car_number += 1
        iteration = 0
    else:
        iteration += 1
    # Remove cars that left the board
    for i in cars_to_remove:
        cars.pop(i)
    cars_to_remove = []

screen.exitonclick()
