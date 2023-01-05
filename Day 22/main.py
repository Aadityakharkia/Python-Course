from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor > 280 or ball.ycor < -280:
        ball.bounce()

screen.exitonclick()