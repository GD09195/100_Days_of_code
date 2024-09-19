import turtle as turtle_module
import random


def set_starting_position(all_turtles: dict[str: turtle_module.Turtle]) -> None:
    number_of_turtles = len(all_turtles)
    width_gap = 20
    turtle_height_gap = screen_height/number_of_turtles
    height_intervals = []
    for index in range(int(-1*(screen_height/2))+20, int(screen_height/2), int(turtle_height_gap)):
        height_intervals.append(index)

    index = 0
    for color, turtle in all_turtles.items():
        turtle.penup()
        turtle.goto(x=(-1*(screen_width/2))+width_gap, y=height_intervals[index])
        index += 1


def set_colors(all_turtle: dict[dir: turtle_module.Turtle]) -> None:
    for key, turtle in all_turtle.items():
        turtle.color(key)


def race_turtles(all_turtles: dict[str: turtle_module.Turtle]) -> None:
    race_on = True
    while race_on:
        for key, turtle in all_turtles.items():
            randon_distance = random.randint(0, 12)
            turtle.dot(4, key)
            turtle.forward(randon_distance)
            if turtle.xcor() >= (screen_width/2)-20:
                race_on = False
                check_winner(key)
                break


def check_winner(color: str) -> None:
    if color == user_guess:
        print(f"You've won! The winner is {color}!")
    else:
        print(f"You've lost. The winner is {color}.")


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'grey', 'pink', 'brown']
screen_width = 500
screen_height = 400
screen = turtle_module.Screen()
turtles = {colour: turtle_module.Turtle(shape='turtle') for colour in colors}

screen.setup(width=screen_width, height=screen_height)
set_colors(turtles)
set_starting_position(turtles)
user_guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color?")
race_turtles(turtles)

screen.exitonclick()