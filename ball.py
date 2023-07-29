from turtle import Turtle
# Constants
MOVE = 10
CENTER = (0, 0)


class Ball(Turtle):
    def __init__(self):  # Setting up our ball
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.x_move = MOVE
        self.y_move = MOVE
        self.move_speed = 0.1

    # Ball's move function

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Ball's bouncing based on the scenarios set in main.py

    def bounce_y(self):
        self.y_move *= -1  # Changing the axis by 180 degrees

    def bounce_x(self):    # Same as above but the ball will also increase speed (it is tied to time.sleep in main.py)
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):  # Resetting positions after score, the ball will move center and move speed will be reset, changing axis too
        self.goto(CENTER)
        self.move_speed = 0.1
        self.bounce_x()