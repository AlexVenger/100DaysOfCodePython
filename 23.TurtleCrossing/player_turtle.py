from turtle import Turtle

START_POSITION = (0, -280)


class PlayerTurtle(Turtle):
    def __init__(self):
        super(PlayerTurtle, self).__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.next_level()

    def move(self):
        self.forward(20)

    def next_level(self):
        self.goto(START_POSITION)
