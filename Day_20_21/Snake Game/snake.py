from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.body: list[Turtle] = []
        self.generate_body(body_size=3)
        self.head = self.body[0]

    def generate_body(self, body_size: int) -> None:
        snake_body = []
        x_offset = -20
        x_pos = 0
        y_pos = 0

        for i in range(body_size):
            x_pos = i*x_offset
            self.add_segment((x_pos, y_pos))

    def move(self) -> None:

        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self) -> None:
        # Add new segment to the snake's body
        self.add_segment(self.body[-1].position())

    def add_segment(self, position):
        # Add a segment to the snake's body at a given position
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.goto(position)
        self.body.append(new_turtle)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
