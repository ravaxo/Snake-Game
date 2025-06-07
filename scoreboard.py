"""This module calculates and draw the score"""
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')
SCORE_POSITION = (0, 270)

class Score(Turtle):
    """calculates the score
    """
    def __init__(self):
        super().__init__()
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.score = 0
        self.update_score()

    def update_score(self):
        """Updates the current score
        """
        self.clear()
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def score_increment(self):
        """Increase the score if snake eats food
        """
        self.score += 1
        self.update_score()

    def game_over(self):
        """Game over after colliision with wall or it's own tail
        """
        self.home()
        self.write('GAME OVER!', move=False, align=ALIGNMENT, font=FONT)
