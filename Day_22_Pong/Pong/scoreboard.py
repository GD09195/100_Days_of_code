from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.color("white")
        self.hideturtle()

        self.right_score: int = 0
        self.left_score: int = 0
        self.display_score()


    def draw_mid_line(self) -> None:
        self.goto(0,300)
        self.showturtle()
        self.pendown()
        self.setheading(270)

        while self.ycor() > -300:

            if self.ycor() == 0:
                self.color("white")
                self.dot(10)
            if self.ycor() % 6 == 0:
                self.color("white")
            else:
                self.color("black")
            self.forward(1)

        self.color("white")
        self.penup()
        self.hideturtle()


    def display_score(self):
        self.clear()
        self.draw_mid_line()
        self.goto(-100, 200)
        self.write(self.left_score, align="Center", font=("Consolas", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="Center", font=("Consolas", 80, "normal"))


    def right_scored(self) -> None:
        self.right_score += 1
        self.display_score()

    def left_scored(self) -> None:
        self.left_score += 1
        self.display_score()

