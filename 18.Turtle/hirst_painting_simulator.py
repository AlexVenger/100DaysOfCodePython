import colorgram
from turtle import Turtle, Screen
import random

colors = []
for color in colorgram.extract("hirst_painting.jpeg", 40):
    colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

screen = Screen()
screen.colormode(255)
screen.exitonclick()

jimmy = Turtle()
jimmy.shape("square")
jimmy.hideturtle()
jimmy.penup()
jimmy.goto(-200, -200)
jimmy.showturtle()
jimmy.pendown()
for _ in range(10):
    for _ in range(10):
        jimmy.color(random.choice(colors))
        jimmy.dot(20)
        jimmy.penup()
        jimmy.forward(50)
        jimmy.pendown()
    jimmy.penup()
    jimmy.left(90)
    jimmy.forward(50)
    jimmy.left(90)
    jimmy.forward(500)
    jimmy.left(180)
    jimmy.pendown()
