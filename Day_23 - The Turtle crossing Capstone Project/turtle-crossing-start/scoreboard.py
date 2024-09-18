FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level: int = 1

        self.hideturtle()
        self.penup()
        self.goto(-280, 240)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_lev(self)-> None:
        self.level += 1
        self.update_scoreboard()

    def game_over(self)-> None:
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)


