import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

def cars_moving(r, l):
    r.go_left()
    l.go_right()
    time.sleep(0.4)
    screen.update()

car_r = CarManager('r')
car_l = CarManager('l')

game_is_on = True
while game_is_on:
    cars_moving(car_r, car_l)

