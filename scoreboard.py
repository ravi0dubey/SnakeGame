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
        self.path = "/users/ravi0dubey/OneDrive/desktop"
        # self.path = "../../OneDrive/Desktop"
        with open(f"{self.path}/score.txt") as rfile:
            self.high_score = int(rfile.read())
        self.color("white")
        self.goto(CORD1, CORD2)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.points}, High_score : {self.high_score}",  align = ALIGNMENT, font= FONT)

    def refresh_score(self):
        self.goto(CORD1, CORD2)
        self.clear()
        with open(f"{self.path}/score.txt") as rfile:
            self.high_score = int(rfile.read())
            print(f"open {self.high_score}")
        if self.points > self.high_score:
            self.high_score= self.points
            print(f"self.points > {self.points}")
            with open("score.txt",mode= "w") as wfile:
                print(f"update.points {self.high_score}")
                wfile.write(f"{self.high_score}")

        self.points = 0
        self.update_score()

    def add_points(self):
        self.clear()
        self.points += INCR
        self.update_score()

    def game_over(self):
        self.goto(CORD1, CORD1)
        self.write("Game Over",  align = ALIGNMENT, font= FONT)

    def new_game(self):
        self.goto(-200, -200)
        self.write("New Game",  align = ALIGNMENT, font= FONT)
