from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.up()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,250)
        self.write(self.l_score,align="center",font=("Calibri",30,"normal"))
        self.color("red")
        self.goto(100,250)
        self.write(self.r_score,align="center",font=("Calibri",30,"normal"))

    def update_sb(self):
        self.clear()
        self.color("blue")
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Calibri", 30, "normal"))
        self.color("red")
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Calibri", 30, "normal"))

    def l_increase(self):
        self.l_score += 1
        self.update_sb()

    def r_increase(self):
        self.r_score += 1
        self.update_sb()