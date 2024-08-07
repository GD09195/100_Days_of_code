import colorgram
import turtle
import random


def rgb_from_image() -> list:
    colors = colorgram.extract('sample.jpg', 100)
    colors_rgb: list = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        colors_rgb.append((r, g, b))

    return colors_rgb


def get_randon_color() -> tuple:
    return random.choice(color_list)


def draw_dots():
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.speed("fastest")
    initial_x = -100
    initial_y = -200
    new_turtle.goto(initial_x, initial_y)

    for colum in range(10):
        for row in range(10):

            new_turtle.dot(20,get_randon_color())
            new_turtle.forward(50)
        initial_y += 50
        new_turtle.goto(initial_x, initial_y)


turtle.colormode(255)
new_turtle = turtle.Turtle()
new_screen = turtle.Screen()
color_list = rgb_from_image()
draw_dots()


new_screen.exitonclick()

