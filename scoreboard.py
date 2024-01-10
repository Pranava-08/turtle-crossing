FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def score(self, lvl):
        self.reset()
        self.penup()
        self.hideturtle()
        self.goto(-330,250)
        self.write(f"level {lvl}", font=FONT, )

    def game_over(self):
        self.goto(0,20)
        self.write("Game Over!!!", align="center", font=FONT)