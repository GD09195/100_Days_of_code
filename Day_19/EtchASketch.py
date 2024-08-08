import turtle as turtle_module

my_turtle = turtle_module.Turtle()
my_screen = turtle_module.Screen()


def move_forward() -> None:
    my_turtle.forward(10)


def move_backward() -> None:
    my_turtle.backward(10)


def rotate_clockwise() -> None:
    my_turtle.right(10)


def rotate_counterclockwise() -> None:
    my_turtle.left(10)


def clear_screen() -> None:
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_screen.listen()

my_screen.onkey(fun=move_forward, key='w')
my_screen.onkey(fun=move_backward, key='s')
my_screen.onkey(fun=rotate_clockwise, key='d')
my_screen.onkey(fun=rotate_counterclockwise, key='a')
my_screen.onkey(fun=clear_screen, key='c')

my_screen.exitonclick()