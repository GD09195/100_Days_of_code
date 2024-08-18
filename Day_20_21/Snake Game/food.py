from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos: int = 0
        self.y_pos: int = 0
