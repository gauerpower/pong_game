from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

scr = Screen()
scr.bgcolor('black')
scr.setup(width=800, height=600)
scr.title('Pong')
scr.tracer()

left_paddle = Paddle(x_coordinate = -350)
right_paddle = Paddle(x_coordinate = 350)
ball = Ball()


scr.listen()
scr.onkey(fun = right_paddle.up, key = "Up")
scr.onkey(fun = right_paddle.down, key = "Down")
scr.onkey(fun = left_paddle.up, key = "w")
scr.onkey(fun = left_paddle.down, key = "s")

game_going = True

while game_going:
    time.sleep(0.1)
    scr.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if (ball.distance(right_paddle) <= 50 and ball.xcor() > 320) or (ball.distance(left_paddle) <= 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()

    if ball.xcor() < -380:
        ball.reset()

scr.exitonclick()