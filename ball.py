from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(0, 0)
        self.going_up = True

    def move(self):
        new_x = self.xcor()+5
        if self.going_up:
            new_y = self.ycor()+5
        else:
            new_y = self.ycor()-5

        if (new_y > 280 and self.going_up) or (new_y < -280 and not self.going_up):
            self.going_up = not self.going_up

        self.setposition(new_x, new_y)
