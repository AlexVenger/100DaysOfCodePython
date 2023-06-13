from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    snake_pieces = [Turtle(), Turtle(), Turtle()]
    head = snake_pieces[0]

    def __init__(self):
        x = 0
        for piece in self.snake_pieces:
            piece.penup()
            piece.shape("square")
            piece.color("white")
            piece.goto(x=x, y=0)
            x -= MOVE_DISTANCE

    def add_piece(self, position):
        piece = Turtle()
        piece.penup()
        piece.shape("square")
        piece.color("white")
        piece.goto(position)
        self.snake_pieces.append(piece)

    def move(self):
        for i in range(len(self.snake_pieces) - 1, 0, -1):
            self.snake_pieces[i].goto(self.snake_pieces[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def check_heading(self, heading):
        return self.head.heading() != heading

    def up(self):
        if self.check_heading(270):
            self.head.setheading(90)

    def down(self):
        if self.check_heading(90):
            self.head.setheading(270)

    def left(self):
        if self.check_heading(0):
            self.head.setheading(180)

    def right(self):
        if self.check_heading(180):
            self.head.setheading(0)

    def grow(self):
        self.add_piece(self.snake_pieces[-1].position())
