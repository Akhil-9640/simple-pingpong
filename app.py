# Object class fot the racket; used two times
# class for the scoreboard;
# class for the ball
# DONE-TODO 1: Create the screen
# TODO 2: Create and move a paddle
# TODO 3: Create another paddle
# TODO 4: Create the ball and make it move
# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect Collision with the paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep Track of scores

from turtle import Screen, Turtle
import time
from racket import Racket

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_racket = Racket((-280, 0))
r_racket = Racket((275, 0))

screen.listen()
screen.onkey(r_racket.go_up, "Up")
screen.onkey(r_racket.go_down, "Down")
screen.onkey(l_racket.go_up, "w")
screen.onkey(l_racket.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
