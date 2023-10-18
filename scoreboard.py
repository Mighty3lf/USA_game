from turtle import Turtle

FONT = ("Arial", 10, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")

    def write_state(self, name, x, y):
        self.write(name,  font=FONT)
        self.goto(x,y)