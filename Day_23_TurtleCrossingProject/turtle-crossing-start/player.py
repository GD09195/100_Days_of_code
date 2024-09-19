STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.reset_position()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")

    def move_up(self) -> None:
        self.forward(MOVE_DISTANCE)

    def crossed_road(self) -> bool:
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def reset_position(self) -> None:
        self.goto(STARTING_POSITION)
