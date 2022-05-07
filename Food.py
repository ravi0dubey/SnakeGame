from turtle import Turtle
import random
CORD1 = -260
CORD2 = 260

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        pos_x = random.randint(CORD1, CORD2)
        pos_y = random.randint(CORD1, CORD2)
        self.goto(pos_x, pos_y)


