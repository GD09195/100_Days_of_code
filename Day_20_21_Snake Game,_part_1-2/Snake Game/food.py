from operator import length_hint
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, width, length):
        super().__init__()
        self.x_pos: int = 0
        self.y_pos: int = 0
        self.x_limit: int = 0
        self.y_limit: int = 0

        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed("fastest")

        self.set_window_limit(width, length)
        self.set_position()

    def set_window_limit(self, wid: int, leng: int)-> None:
        edge_gap = 10
        self.x_limit = int(wid/2)-edge_gap
        self.y_limit = int(leng/2)-edge_gap

    def set_position(self)-> None:
        self.x_pos = random.randint(-self.x_limit, self.x_limit)
        self.y_pos = random.randint(-self.y_limit, self.y_limit)
        self.goto(self.x_pos,self.y_pos)
