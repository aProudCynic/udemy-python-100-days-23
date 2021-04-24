from random import choice, randint
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

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

    def detect_collisions_with(self, player):
        player_position_x, player_position_y = player.pos()
        for car in self.cars:
            car_position_x, car_position_y = car.pos()
            distance_x = car_position_x - player_position_x
            distance_y = car_position_y - player_position_y
            if distance_x <= 20 and distance_x >= -20 and distance_y <= 10 and distance_y >= -10:
                return True
        return False
