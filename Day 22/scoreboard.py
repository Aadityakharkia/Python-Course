from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.r_score = 0
        self.l_score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier",80,"normal"))

    def increase_r(self):
        self.r_score += 1
        self.update_score()

    def increase_l(self):
        self.l_score += 1
        self.update_score()