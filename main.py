from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scr = Screen()
scr.bgcolor('black')
scr.setup(width=800, height=600)
scr.title('Pong')
scr.tracer()

left_paddle = Paddle(x_coordinate = -350)
right_paddle = Paddle(x_coordinate = 350)
ball = Ball()
scoreboard = Scoreboard()


scr.listen()
scr.onkey(fun = right_paddle.up, key = "Up")
scr.onkey(fun = right_paddle.down, key = "Down")
scr.onkey(fun = left_paddle.up, key = "w")
scr.onkey(fun = left_paddle.down, key = "s")

game_going = True

while game_going:
    time.sleep(0.05)
    scr.update()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    if (ball.distance(right_paddle) <= 50 and ball.xcor() > 320) or (ball.distance(left_paddle) <= 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_gets_a_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_gets_a_point()
    
    if scoreboard.left_score == 7 or scoreboard.right_score == 7:
        game_going = False
        scoreboard.game_over()

scr.exitonclick()