from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
import time


def initialize_screen() -> Screen:
    new_screen = Screen()
    new_screen.setup(width=600, height=600)
    new_screen.bgcolor('black')
    new_screen.title("Snake")
    new_screen.tracer(0)

    return new_screen


def update_game(my_snake: Snake, my_screen: Screen) -> None:

    game_on = True
    game_speed = 0.1

    while game_on:
        my_screen.update()
        time.sleep(game_speed)
        my_snake.move()


def controls(my_screen: Screen) -> None:
    my_screen.listen()
    my_screen.onkey(snake.up, "Up")
    my_screen.onkey(snake.down, "Down")
    my_screen.onkey(snake.right, "Right")
    my_screen.onkey(snake.left, "Left")


screen = initialize_screen()
snake = Snake()
controls(screen)
update_game(snake, screen)

screen.exitonclick()