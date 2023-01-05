from turtle import Turtle,Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onclick(r_paddle.go_up, 'Up')
screen.onclick(r_paddle.go_down,"Down")
screen.onclick(l_paddle.go_up, "w")
screen.onclick(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()