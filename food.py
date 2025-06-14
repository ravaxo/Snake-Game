"""This module handles the food re-appearing in different positions
    after every time snake hits the food."""
from turtle import Turtle
import random

class Food(Turtle):
    """food related things and its functions
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """New location for food particle
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
