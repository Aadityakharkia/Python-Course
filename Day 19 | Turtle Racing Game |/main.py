# Turtle Race Game

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
answer = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter the color")
colors = ["red","orange","yellow","green","blue","purple"]

is_race_on = False

y = 200
all_turtle = []

for turtle in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    all_turtle.append(new_turtle)
    for i in range (0,6):
        new_turtle.goto(-230,y)
        y -= 10

if answer:
    is_race_on = True

while is_race_on == True:
    for turtle in all_turtle:
        if turtle.xcor()>220:
            winner = turtle.pencolor()
            if answer == winner:
                print("You Won")
            else:
                print(f"Sorry you lost: The winner is {winner}")
            is_race_on = False
        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()