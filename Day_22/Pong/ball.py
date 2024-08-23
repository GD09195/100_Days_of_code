from turtle import Turtle
STARTING_BALL_SPEED = 6

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed(1)

        self.ball_speed = 0.05
        self.x_direction: int = STARTING_BALL_SPEED
        self.y_direction: int = STARTING_BALL_SPEED

    def move(self) -> None:

        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction

        self.goto(x=new_x, y=new_y)

    def bounce_y(self) -> None:
        self.y_direction *= -1

    def bounce_x(self) -> None:
        self.x_direction *= -1
        self.ball_speed *= 0.8

    def reset(self):

        self.goto((0,0))
        self.bounce_x()
        self.ball_speed = 0.05