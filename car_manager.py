from random import choice, randint
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    cars = []

    def initialize_car(self):
        starting_y_point = randint(-28, 28) * 10
        color = choice(COLORS)
        car = Car(280, starting_y_point, color)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move(STARTING_MOVE_DISTANCE)
