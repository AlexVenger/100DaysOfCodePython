import turtle
from turtle import Turtle, Screen

tortilla = Turtle()
screen = Screen()
screen.listen()


def move_forwards():
    tortilla.forward(10)


def move_backwards():
    tortilla.backward(10)


def turn_left():
    tortilla.left(10)


def turn_right():
    tortilla.right(10)


def clear_screen():
    tortilla.clear()
    tortilla.penup()
    tortilla.home()
    tortilla.pendown()


screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
