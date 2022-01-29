from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TURTLE_COLOR = '#59C3C3'

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_spirit()

    def create_spirit(self):
        self.shape('turtle')
        self.penup()
        self.color(TURTLE_COLOR)
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def go_up(self):
        self.setheading(90)
        self.forward(10)

    def go_down(self):
        self.setheading(270)
        self.forward(10)

    def go_left(self):
        self.setheading(180)
        self.forward(10)

    def go_right(self):
        self.setheading(0)
        self.forward(10)

    def check_pos(self):
        if self.ycor() > FINISH_LINE_Y:
            self.setposition(STARTING_POSITION)
            return True
        elif self.ycor() < -300 or self.xcor() > 300 or self.xcor() < -300:
            self.setposition(STARTING_POSITION)
            return False
