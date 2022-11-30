from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
POSITION_L = (-100, 200)
POSITION_R = (100, 200)

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(x=POSITION_L[0], y= POSITION_L[1])
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(x=POSITION_R[0], y=POSITION_R[1])
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()
    
    def r_point(self):
        self.r_score += 1
        self.update_score()