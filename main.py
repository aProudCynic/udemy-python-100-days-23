from random import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=600, height=SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

def player_is_at_top_edge_of_screen(player: Player):
    return player.ycor() >= SCREEN_HEIGHT / 2 - 10

def move_player_to_original_position(player: Player):
    player.set_to_starting_position()

def level_up():
    scoreboard.level_up()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    if random() <= 0.3:
       car_manager.initialize_car()
    car_manager.move_cars()
    if player_is_at_top_edge_of_screen(player):
        move_player_to_original_position(player)
        level_up()
    screen.update()
