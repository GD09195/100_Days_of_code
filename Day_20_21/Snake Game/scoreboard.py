from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score: int = 0
        self.high_score: int = 0
        self.display: str = "Score: "

    def increase_score(self, increment: int) -> None:
        self.score += increment
        self.display_score()

    def display_score(self) -> None:
        self.clear()
        self.write(f"{self.display}{self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def set_position(self, x_cor:int, y_cor: int) -> None:
        self.clear()
        self.goto(x_cor, y_cor)
        self.display_score()

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.display_score()
