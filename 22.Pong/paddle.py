from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=x, y=0)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() < 250:
            self.goto(x=self.xcor(), y=self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(x=self.xcor(), y=self.ycor() - 20)
