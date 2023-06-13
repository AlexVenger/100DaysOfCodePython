from turtle import Turtle
import random

RANDOM_ANGLE_LEFT = random.randint(135, 225)
RANDOM_ANGLE_RIGHT = random.choice([i for i in range(0, 46)] + [i for i in range(315, 360)])
START_SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.setheading(RANDOM_ANGLE_RIGHT)
        self.move_speed = START_SPEED
        self.is_moving = False

    def bounce(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.setheading(180 - self.heading())
        self.move_speed *= 0.9

    def l_off_the_board(self):
        self.goto(0, 0)
        self.setheading(RANDOM_ANGLE_LEFT)
        self.move_speed = START_SPEED

    def r_off_the_board(self):
        self.goto(0, 0)
        self.setheading(RANDOM_ANGLE_RIGHT)
        self.move_speed = START_SPEED

    def start_move(self):
        self.is_moving = not self.is_moving
