from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)

ridiculous_racist = Turtle()
ridiculous_racist.color("red")

obnoxious_ouroboros = Turtle()
obnoxious_ouroboros.color("orange")

yankee_yeeter = Turtle()
yankee_yeeter.color("yellow")

ginormous_guerilla = Turtle()
ginormous_guerilla.color("green")

british_bombardier = Turtle()
british_bombardier.color("blue")

irresponsible_igniter = Turtle()
irresponsible_igniter.color("indigo")

vicious_vagabond = Turtle()
vicious_vagabond.color("violet")

turtles = [
    ridiculous_racist,
    obnoxious_ouroboros,
    yankee_yeeter,
    ginormous_guerilla,
    british_bombardier,
    irresponsible_igniter,
    vicious_vagabond
]

y = -180
for t in turtles:
    t.shape("turtle")
    t.penup()
    t.goto(x=-230, y=y)
    y += 60

user_bet = screen.textinput(title="Make your bet", prompt="Place your bet on one of the turtles (pick a color): ")

if user_bet:
    is_race_on = True

winner = ""
while is_race_on:
    for t in turtles:
        t.forward(random.randint(0, 10))
        if t.position()[0] >= 230:
            winner = t.color()[0]
            is_race_on = False
            break

if winner == user_bet:
    print(f"You've got that right! The {winner} turtle is the winner!")
else:
    print(f"You've lost. The winner is the {winner} turtle.")


screen.exitonclick()
