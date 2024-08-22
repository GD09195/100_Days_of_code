from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


def setup_pong_screen() -> Screen:
    new_screen = Screen()
    new_screen.setup(width=800, height=600)
    new_screen.bgcolor("black")
    new_screen.title(titlestring="Pong")
    return new_screen


def controls(my_screen: Screen, right_p: Paddle, left_p: Paddle) -> Screen:
    my_screen.listen()
    my_screen.onkeypress(right_p.move_up, "Up")
    my_screen.onkeypress(right_p.move_down, "Down")
    my_screen.onkeypress(left_p.move_up, "w")
    my_screen.onkeypress(left_p.move_down, "s")
    return my_screen


def update_game(screen: Screen, r_paddle: Paddle, l_paddle: Paddle, ball: Ball) -> None:
    game_on = True
    while game_on:
        time.sleep(0.05)
        screen.update()
        ball.move()


# Initialize the Screen
pong_screen = setup_pong_screen()

# Set Screen tracer to 0 to initialize all elements
pong_screen.tracer(0)

# Initialize Paddles
right_paddle = Paddle()
right_paddle.position(x_cor=350, y_cor=0)
left_paddle = Paddle()
left_paddle.position(x_cor=-350, y_cor=0)
pong_ball = Ball()

# Set Controls
pong_screen = controls(pong_screen, right_paddle, left_paddle)

# Update game's frames
update_game(screen=pong_screen, r_paddle=right_paddle, l_paddle=left_paddle, ball=pong_ball)


pong_screen.exitonclick()

