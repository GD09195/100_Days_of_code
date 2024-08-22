from turtle import Turtle
WIDTH = 20
HEIGHT = 100
Y_MOVEMENT = 20
SHAPE = "square"


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=(HEIGHT/20), stretch_len=(WIDTH/20))
        self.penup()
        self.color("white")
        self.speed(speed="fastest")

    def position(self, x_cor: int, y_cor: int) -> None:
        self.setpos(x=x_cor, y=y_cor)

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor()+Y_MOVEMENT)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor()-Y_MOVEMENT)



