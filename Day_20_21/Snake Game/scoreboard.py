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
        self.display: str = "Score: "


    def increase_score(self, increment: int) -> None:
        self.score += increment
        self.display_score()

    def display_score(self) -> None:
        self.clear()
        self.write(f"{self.display}{self.score}", align=ALIGNMENT, font=FONT)

    def set_position(self, x_cor:int, y_cor: int) -> None:
        self.clear()
        self.goto(x_cor, y_cor)
        self.display_score()


    def game_over(self) -> None:
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
