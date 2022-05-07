from turtle import Turtle
CORD1 = 0
CORD2 = 270
POINTS = 0
INCR = 1
FONT = ('Courier', 18, "normal")
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = POINTS
        self.penup()
        self.ht()
        self.color("white")
        self.goto(CORD1, CORD2)
        self.refresh()

    def refresh(self):
        self.write(f"Score : {self.points}",  align = ALIGNMENT, font= FONT)


    def add_points(self):
        self.clear()
        self.points += INCR
        self.refresh()

    def game_over(self):
        self.goto(CORD1, CORD1)
        self.write("Game Over",  align = ALIGNMENT, font= FONT)
