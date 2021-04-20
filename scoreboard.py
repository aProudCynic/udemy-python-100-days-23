from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.setposition(0, 270)
        self.score_left = 0
        self.score_right = 0
        self._write_score()

    def level_up(self):
        self.level += 1
        self._write_score()

    def _write_score(self):
        self.clear()
        self.write(f'Level: {self.level}', font=('Arial', 24))
