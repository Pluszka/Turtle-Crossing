from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_LEN = [2,3,4]

class CarManager(Turtle):

    def __init__(self, side):
        super().__init__()
        self.create()
        self.setpos(x=side, y=randint(-200, 200))

    def create(self):
        self.penup()
        self.shape('square')
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len= choice(CARS_LEN))

    def go_left(self):
        self.setheading(180)
        self.forward(100)

    def go_right(self):
        self.setheading(0)
        self.forward(100)