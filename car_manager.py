from random import choice, randint
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE

    cars = []

    def initialize_car(self):
        starting_y_point = randint(-28, 28) * 10
        color = choice(COLORS)
        car = Car(280, starting_y_point, color)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move(self.car_speed)

    def speed_up_cars(self):
        self.car_speed += MOVE_INCREMENT
