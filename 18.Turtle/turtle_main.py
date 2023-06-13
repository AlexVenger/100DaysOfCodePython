from turtle import Turtle, Screen
import random

lenny = Turtle()
lenny.shape("turtle")


def draw_square():
    lenny.color("blue")
    for _ in range(4):
        lenny.forward(100)
        lenny.right(90)


def draw_dashed_line():
    lenny.left(180)
    for _ in range(10):
        lenny.penup()
        lenny.forward(10)
        lenny.pendown()
        lenny.forward(10)


def draw_polygons(n):
    for i in range(3, n):
        angle = 180 * (i - 2) / i
        print(angle)
        color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        lenny.color(color)
        for _ in range(i):
            lenny.forward(100)
            lenny.right(180 - angle)


def draw_random_walk(n, d):
    lenny.width(10)
    lenny.speed(20)
    directions = ["left", "right", "forward", "backward"]
    for _ in range(n):
        direction = random.choice(directions)
        color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        lenny.color(color)
        if direction == "left":
            lenny.left(90)
            lenny.forward(d)
        elif direction == "right":
            lenny.right(90)
            lenny.forward(d)
        elif direction == "forward":
            lenny.forward(d)
        else:
            lenny.backward(d)


def draw_spirograph(n):
    lenny.speed("fastest")
    for _ in range(n):
        color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        lenny.color(color)
        lenny.circle(100)
        lenny.left(360 / n)


draw_spirograph(50)

screen = Screen()
screen.exitonclick()
screen.colormode(255)
