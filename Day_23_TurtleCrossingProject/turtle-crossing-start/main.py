import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player_turtle = Player()
car_admin = CarManager()
score = Scoreboard()

screen.setup(width=600, height=600)

screen.listen()
screen.onkey(player_turtle.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_admin.add_car()
    car_admin.move_cars()

    # Detect Collision with cars
    for car in car_admin.cars:
        if car.distance(player_turtle) < 20:
            game_is_on = False
            score.game_over()

    # Detect crossing
    if player_turtle.crossed_road():
        player_turtle.reset_position()
        car_admin.level_up()
        score.increase_lev()

screen.exitonclick()