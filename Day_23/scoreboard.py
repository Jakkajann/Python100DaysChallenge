from turtle import Turtle
SCORE_POSITION = (-280, 260)
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)