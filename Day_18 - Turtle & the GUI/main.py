import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)
tim = Turtle()
tim.color('black')
screen = Screen()
screen.bgcolor('white')

color = ["#c7ebec",
         "#075264",
         "#ffa8e3",
         "#bb3429",
         "#224d42",
         "#d63232",
         "#f7a583",
         "#a4a614",
         "#660066",
         "#992b27",
         "#73ced0",
         "#bb3429",
         "#73ced0",
         "#ffc525",
         "#c0bbf9"]


def draw_square():
    for face in range(4):
        tim.forward(200)
        tim.right(90)


def dashed_line():

    for dash in range(0, 50):
        dash_length: int = 1
        if dash % dash_length == 0:
            if tim.isdown():
                tim.penup()
            else:
                tim.pendown()

        tim.forward(10)


def draw_figures():

    for figure in range(3, 11):
        angle = 360 / figure
        tim_color = choice(color)
        color.remove(tim_color)
        tim.color(tim_color)

        for sides in range(figure):
            tim.forward(100)
            tim.right(angle)


def random_walk():

    tim.pensize(12)
    step_size = 24
    tim.speed(10)

    for step in range(500):

        new_color = (randint(0, 255), randint(0, 255), randint(0, 255) )
        tim.color(new_color)
        randon_direction = randint(0, 4)

        if randon_direction == 1:
            tim.setpos(tim.xcor()+step_size, tim.ycor())
            continue
        if randon_direction == 2:
            tim.setpos(tim.xcor()-step_size, tim.ycor())
            continue
        if randon_direction == 3:
            tim.setpos(tim.xcor(), tim.ycor()+step_size)
            continue
        if randon_direction == 4:
            tim.setpos(tim.xcor(), tim.ycor()-step_size)
            continue


def draw_circle():

    tim.speed(30)
    radius = 100
    number_of_circles = 80
    angle = 360/number_of_circles
    new_angle = 0
    for circles in range(0, number_of_circles):
        new_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        tim.color(new_color)
        tim.circle(radius)
        tim.left(angle)
        new_angle += angle

# draw_square()
# dashed_line()
# draw_figures()
# random_walk()
draw_circle()


screen.exitonclick()

