from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LEN = 1
PADDLE_SPEED = 30

class Paddle(Turtle):
    def __init__(self, initial_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH,stretch_len=PADDLE_LEN)
        self.penup()
        self.goto(initial_position[0], initial_position[1])
    
    def go_up(self):
        new_y = self.ycor() + PADDLE_SPEED
        self.goto(x=self.xcor(), y=new_y)
    
    def go_down(self):
        new_y =  self.ycor() - PADDLE_SPEED
        self.goto(x=self.xcor(), y=new_y)