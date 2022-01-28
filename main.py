import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager(350)
car1 = CarManager(-350)

game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()
    car.go_left()
    car1.go_right()
