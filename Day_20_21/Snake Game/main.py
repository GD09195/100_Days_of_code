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


def update_game(my_snake: Snake, my_screen: Screen, food: Food, score: Scoreboard) -> None:

    game_on = True
    game_speed = 0.1

    while game_on:
        my_screen.update()
        time.sleep(game_speed)
        my_snake.move()

        #Detect Collision with food
        if snake.head.distance(food) < 15:
            food.set_position()
            score.increase_score(1)
            snake.extend()

        #Detect Collision with wall
        if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
            game_on = False
            score.game_over()

        #Detect Collision with tail
        #if head collides with any segment in tail.

        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                game_on = False
                score.game_over()


def controls(my_screen: Screen) -> None:
    my_screen.listen()
    my_screen.onkey(snake.up, "Up")
    my_screen.onkey(snake.down, "Down")
    my_screen.onkey(snake.right, "Right")
    my_screen.onkey(snake.left, "Left")


screen = initialize_screen()

snake = Snake()
my_food =  Food(600, 600)

my_Score = Scoreboard()
my_Score.setposition(0,276)
my_Score.display_score()

controls(screen)
update_game(snake, screen, my_food, my_Score)

screen.exitonclick()