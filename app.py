#Object class fot the racket; used two times
#class for the scoreboard;
#class for the ball
#DONE-TODO 1: Create the screen
#TODO 2: Create and move a paddle
#TODO 3: Create another paddle
#TODO 4: Create the ball and make it move
#TODO 5: Detect collision with wall and bounce
#TODO 6: Detect Collision with the paddle
#TODO 7: Detect when paddle misses
#TODO 8: Keep Track of scores

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.up()
paddle.goto(-280, 0)


def go_up():
    new_y = paddle.ycor()+20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor()-20
    paddle.goto(paddle.xcor(),new_y)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()







screen.exitonclick()

