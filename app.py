# Object class fot the racket; used two times
# class for the scoreboard;
# class for the ball
# DONETODO 1: Create the screen
# DONETODO 2: Create and move a paddle
# DONETODO 3: Create another paddle
# DONETODO 4: Create the ball and make it move
# DONETODO 5: Detect collision with wall and bounce
# TODO 6: Detect Collision with the paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep Track of scores

from turtle import Screen, Turtle
import time
from racket import Racket
from ball import Ball

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_racket = Racket((-280, 0))
r_racket = Racket((275, 0))
ball = Ball()
screen.update()
screen.listen()
screen.onkey(r_racket.go_up, "Up")
screen.onkey(r_racket.go_down, "Down")
screen.onkey(l_racket.go_up, "w")
screen.onkey(l_racket.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
