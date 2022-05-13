from turtle import Screen
from snake import Snake
from Food import Food
from scoreboard import Scoreboard
import time
CORD1 = 280
CORD2 = -280

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_continues = True
while game_continues:
    # with open("score.txt") as file:
    #     print(f"xyz:{file.read()}")
    #      # xyz= file.read()

    screen.update()
    time.sleep(0.2)
    snake.move()

# Detect collision with food, increase the score, extend the snake.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.add_points()


#Detect collision with wall. End the game
    if snake.head.xcor() > CORD1 or snake.head.xcor() < CORD2\
            or snake.head.ycor() > CORD1 or snake.head.ycor() < CORD2 :
        score.new_game()
        score.refresh_score()
        # score.game_over()
        # game_continues = False
        snake.refresh()

#Detect collision with Tail, end the game
    for seq in snake.all_snake[1:len(snake.all_snake)-1]:
        if seq == snake.head:
            pass
        elif snake.head.distance(seq) < 10:
            score.new_game()
            score.refresh_score()
            snake.refresh()
            # score.game_over()
            # game_continues = False




screen.exitonclick()
