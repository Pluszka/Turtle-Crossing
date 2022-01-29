from turtle import Turtle
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.penup()
        self.hideturtle()
        self.setposition(x=-200, y=260)
        self.prompt()

    def prompt(self):
        self.write(f'Level: {self.lvl}', align='center', font=FONT)

    def add_lvl(self):
        self.clear()
        self.lvl += 1
        self.prompt()