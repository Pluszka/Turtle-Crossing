from turtle import Turtle
FONT = ("Courier", 15, "bold")
OVER_FONT = ("Courier", 25, "bold")
TEXT_COLOR = '#59C3C3'
DEAD = '#'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.penup()
        self.hideturtle()
        self.color(TEXT_COLOR)
        self.setposition(x=-200, y=260)
        self.prompt()

    def prompt(self):
        self.write(f'Level: {self.lvl}', align='center', font=FONT)

    def add_lvl(self):
        self.clear()
        self.lvl += 1
        self.prompt()

    def game_over(self):
        self.home()
        self.write('GAME OVER', align='center', font=OVER_FONT)
