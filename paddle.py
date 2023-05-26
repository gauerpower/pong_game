from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_coordinate):
        super().__init__()
        self.hideturtle()
        self.speed(10)
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x = x_coordinate, y = 0)
        self.showturtle()

    def up(self):
        if self.ycor() <= 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
