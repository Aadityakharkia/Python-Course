from turtle import Turtle, Screen
import time
import Snake

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
    for i in range(len(segment)-1,0,-1):
        x= segment[i - 1].xcor()
        y=segment[i - 1].ycor()
        segment[i].goto(x,y)
    segment[0].forward(10)
    segment[0].left(90)

screen.exitonclick()
