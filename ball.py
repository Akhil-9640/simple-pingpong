from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(0,0)

    def move(self):
        new_x = self.xcor()+5
        new_y = self.ycor()+5
        self.setposition(new_x, new_y)
