from turtle import Turtle
STARTING_POSITIONS = [(-20,0), (0,0),(20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_snake =[]
        self.create_snake()
        self.head= self.all_snake[0]

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
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)



