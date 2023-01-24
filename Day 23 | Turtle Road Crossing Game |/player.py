from turtle import Turtle
#------------------------------- Setting Values --------------------
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
#------------------------------- Creating Class --------------------
class Player(Turtle): # Turtle is the parent class for this class

    def __init__(self):
        super().__init__() # Subclass
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False