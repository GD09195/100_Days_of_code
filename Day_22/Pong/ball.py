from turtle import Turtle
BALL_SPEED = 6

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed(1)

    def move(self) -> None:
        new_x = self.xcor() + BALL_SPEED
        new_y = self.ycor() + BALL_SPEED
        self.goto(x=new_x, y=new_y)
