from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def left_gets_a_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_gets_a_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align = 'center', font = ('Courier', 60, 'bold'))
        self.goto(100, 200)
        self.write(self.right_score, align = 'center', font = ('Courier', 60, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.\n{'Player 1' if self.left_score > self.right_score else 'Player 2'} wins.", align = 'center', font = ('Courier', 60, 'bold'))