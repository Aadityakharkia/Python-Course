# Pong Game

from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

# --------------------------- Setting up screen and calling for functions ------------------------

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()

screen.listen()

# ----------------------------------------- Defining Keys --------------------------------------

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# ---------------------------------------- Functioning the game --------------------------------

speed = 0.1
is_game_on = True
while is_game_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    if (ball.ycor() > 280) or (ball.ycor() < -280):
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320 :
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r()
        
screen.exitonclick()