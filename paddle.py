from turtle import Turtle


class Paddle(Turtle):  # Setting our paddles
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("cyan")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    # Our move functions for the paddles

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
