from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

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

screen.onclick(r_paddle.go_up, "w")

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
        speed = speed/5

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r()
        
screen.exitonclick()