from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Setting up our screen
screen = Screen()
screen.bgcolor("dark blue")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

# Creating our game objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Getting player inputs
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# Game logic/loop
is_game_running = True
while is_game_running:
    time.sleep(ball.move_speed)  # Ball's move speed
    screen.update()
    ball.move()
    # If the ball hits Top/Bottom walls it will bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # If the ball hits the paddles it will bounce back
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # If the ball passes the paddles the ball will reset and scores will be added
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()