from turtle import Turtle
from random import choice, randint

COLORS = ["tomato", "chocolate", "goldenrod", "OliveDrab", "SteelBlue3", "SlateBlue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X_COR = 300


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.goto(STARTING_X_COR, randint(-230, 230))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
