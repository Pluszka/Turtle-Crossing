from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_LEN = [2,3,4]

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.create()


    def create(self):
        self.shape('square')
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len= choice(CARS_LEN))

