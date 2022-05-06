from turtle import Turtle
STARTING_POSITIONS = [(-20,0), (0,0),(20,0)]
MOVE_DISTANCE = 20
MOVE_LEFT= 90
MOVE_RIGHT = 90

class Snake:
    def __init__(self):
        self.all_snake =[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(position)
            self.all_snake.append(new_snake)

    def move(self):
        for seq_num in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[seq_num - 1].xcor()
            new_y = self.all_snake[seq_num - 1].ycor()
            self.all_snake[seq_num].goto(new_x, new_y)
        self.all_snake[0].forward(MOVE_DISTANCE)


    def up(self):
        self.all_snake[0].setheading(90)
        self.self.all_snake[0].move()

    def down(self):
        self.all_snake[0].setheading(270)
        self.self.all_snake[0].move()

    def left(self):
        self.all_snake[0].setheading(180)
        self.self.all_snake[0].move()

    def right(self):
        self.all_snake[0].setheading(0)
        self.self.all_snake[0].move()


