from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_LEN = [2,3,4]
LEFT = [-600, -10]
RIGHT = [10, 600]
ROAD = [-250, 250]

class CarManager(Turtle):

    def __init__(self, side):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create(side)

    def create(self, side):
        side = self.check_side(side)
        for car in range(10):
            car = Turtle()
            car.penup()
            car.shape('square')
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len= choice(CARS_LEN))
            car.setpos(x=randint(side[0], side[1]), y=randint(ROAD[0], ROAD[1]))
            self.cars.append(car)

    def go_left(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(10)
            if car.xcor() < -400:
                car.setpos(x=randint(350, 400), y=randint(ROAD[0], ROAD[1]))

    def go_right(self):
        for car in self.cars:
            car.setheading(0)
            car.forward(10)
            if car.xcor() > 400:
                car.setpos(x=randint(-400, -350), y=randint(-200, 200))

    def check_side(self, side):
        if side == 'r':
           return RIGHT
        elif side == 'l':
            return LEFT

    def knock(self, victim):
        for car in self.cars:
            if car.distance(victim) < 20:
                print('knock!')
                return 1
        return 0