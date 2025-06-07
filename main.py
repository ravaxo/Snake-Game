"""This module create a Snake game"""
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.bgcolor("black")
SCREEN.title("My snake game")
SCREEN.listen()
SCREEN.tracer(0)

score = Score()
snake = Snake()
food = Food()

SCREEN.listen()
SCREEN.onkey(snake.up, "Up")
SCREEN.onkey(snake.down, "Down")
SCREEN.onkey(snake.left, "Left")
SCREEN.onkey(snake.right, "Right")

GAME_IS_ON = True
while GAME_IS_ON:
    SCREEN.update()
    time.sleep(0.1)
    snake.move()

    # Food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_length_increase()
        score.score_increment()

    #Detect collision with walls
    x, y = snake.head.position()
    if x > 280 or x < -280 or y > 280 or y < -280:
        GAME_IS_ON = False
        score.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            GAME_IS_ON = False
            score.game_over()

SCREEN.exitonclick()
