from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, car_color: str,y_position: int, current_speed: int):
        super().__init__()
        self.color(car_color)
        self.penup()
        self.goto(x=320, y=y_position)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed = current_speed

    def move(self):
        self.backward(self.speed)

    def speed_up(self, increase: int):
        self.speed += increase

class CarManager:
    def __init__(self):
        self.cars: list[Car] = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        random_chance = randint(0, 5)
        if random_chance == 1:
            random_color = COLORS[randint(0,len(COLORS)-1)]
            random_y_position = randint(-260, 260)
            new_car = Car(car_color=random_color, y_position= random_y_position, current_speed=self.cars_speed)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.move()

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT
        for car in self.cars:
            car.speed_up(MOVE_INCREMENT)





