# Object class fot the racket; used two times
# class for the scoreboard;
# class for the ball
# DONETODO 1: Create the screen
# DONETODO 2: Create and move a paddle
# DONETODO 3: Create another paddle
# DONETODO 4: Create the ball and make it move
# DONETODO 5: Detect collision with wall and bounce
# DONETODO 6: Detect Collision with the paddle
# DONETODO 7: Detect when paddle misses
# DONETODO 8: Keep Track of scores

from turtle import Screen
import time
from racket import Racket
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_racket = Racket((-350, 0))
r_racket = Racket((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()
screen.listen()
screen.onkeypress(r_racket.go_up, "Up")
screen.onkeypress(r_racket.go_down, "Down")
screen.onkeypress(l_racket.go_up, "w")
screen.onkeypress(l_racket.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.b_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_racket) < 50 and ball.xcor() > 320 or ball.distance(l_racket) < 50 and ball.xcor() < -320:
        print("made contact")
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_increase()
        time.sleep(1)

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_increase()
        time.sleep(1)

screen.exitonclick()
