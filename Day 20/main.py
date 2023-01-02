from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

is_on = True
while is_on == True:
    screen.update()
    time.sleep(0.3)

    snake.move()

screen.exitonclick()
