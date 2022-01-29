import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_r = CarManager('r')
car_l = CarManager('l')
turtle = Player()
scoreboard = Scoreboard()
nap_time = 0.4


def cars_moving(r_side, l_side):
    r_side.go_left()
    l_side.go_right()
    time.sleep(nap_time)
    screen.update()


screen.listen()
screen.onkey(key='Up', fun=turtle.go_up)
screen.onkey(key='Down', fun=turtle.go_down)
screen.onkey(key='Left', fun=turtle.go_left)
screen.onkey(key='Right', fun=turtle.go_right)

game_is_on = True
while game_is_on:
    if turtle.check_pos():
        nap_time *= 0.5
        scoreboard.add_lvl()
    cars_moving(car_r, car_l)
    knock = car_r.knock(turtle)
    knock += car_l.knock(turtle)
    if knock != 0:
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()
