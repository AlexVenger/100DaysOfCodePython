from turtle import Turtle
import random

STARTING_Y_COORDINATES = [i for i in range(-200, 200, 50)]
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "hot pink"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(x=350, y=random.choice(STARTING_Y_COORDINATES))
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.speed(1)
