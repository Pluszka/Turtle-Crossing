from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_LEN = [2,3,4]
LEFT = [-300, -100]
RIGHT = [100, 300]

class CarManager(Turtle):

    def __init__(self, side):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create(side)

    def create(self, side):
        side = self.check_side(side)
        for car in range(20):
            car = Turtle()
            car.penup()
            car.shape('square')
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len= choice(CARS_LEN))
            car.setpos(x=randint(side[0], side[1]), y=randint(-200, 200))
            self.cars.append(car)

    def go_left(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(100)

    def go_right(self):
        for car in self.cars:
            car.setheading(0)
            car.forward(100)

    def check_side(self, side):
        if side == 'r':
           return RIGHT
        else:
            return LEFT