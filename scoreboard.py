FONT = ("Courier", 24, "normal")

class Scoreboard:

    def __init__(self):
        super().__init__()
        self.level = 1

    def level_up(self):
        self.level += 1

