from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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


def missed_ball(game_ball: Ball, player_missed: str, current_score: Scoreboard) -> None:
    if player_missed == "right":
        current_score.left_scored()

    if player_missed == "left":
        current_score.right_scored()

    game_ball.reset()

def update_game(screen: Screen, r_paddle: Paddle, l_paddle: Paddle, ball: Ball, score: Scoreboard) -> None:
    game_on = True

    while game_on:
        time.sleep(ball.ball_speed)
        screen.update()
        ball.move()

        # Detect collision with top wall & bottom wall
        if ball.ycor() >= 288 or ball.ycor() <= -288:
            ball.bounce_y()

        # Detect collision with the right paddle
        if ball.distance(right_paddle) < 50 and ball.xcor()>328:
            ball.bounce_x()

        # Detect collision with the left paddle
        if ball.distance(left_paddle) < 50 and ball.xcor()<-328:
            ball.bounce_x()

        # Detect if ball is missed by right player
        if ball.xcor() > 400:
            missed_ball(ball, "right", score)

        # Detect if ball is missed by left player
        if ball.xcor() < -400:
            missed_ball(ball, "left", score)



# Initialize the Screen
pong_screen = setup_pong_screen()


# Set Screen tracer to 0 to initialize all elements
pong_screen.tracer(0)

#Initialize the Scoreboard
scoreboard = Scoreboard()

# Initialize Paddles
right_paddle = Paddle()
right_paddle.position(x_cor=350, y_cor=0)
left_paddle = Paddle()
left_paddle.position(x_cor=-350, y_cor=0)
pong_ball = Ball()

# Set Controls
pong_screen = controls(pong_screen, right_paddle, left_paddle)

# Update game's frames
update_game(screen=pong_screen, r_paddle=right_paddle, l_paddle=left_paddle, ball=pong_ball, score=scoreboard)


pong_screen.exitonclick()

