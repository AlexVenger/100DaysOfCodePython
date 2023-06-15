from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super(Scoreboard, self).__init__()
        self.car_timer = 5
        self.level = int(level) - 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.car_timer /= self.level
        self.clear()
        self.goto(x=-260, y=260)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
