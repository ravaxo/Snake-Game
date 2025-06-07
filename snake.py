"""This module contains the Snake class, which defines the snake's attributes and behaviors for the game."""
from turtle import Turtle

# Constants for direction
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """A class to represent the snake in the Snake game."""

    def __init__(self, length=3, shape='square', color='white', distance=20):
        """Initialize a new snake."""
        self.length = length
        self.shape = shape
        self.color = color
        self.distance = distance
        self.segments = []
        self._create_snake()
        self.head = self.segments[0]

    def _add_segment(self, position):
        """Add a segment at a specific position."""
        segment = Turtle(shape=self.shape)
        segment.color(self.color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def _create_snake(self):
        """Create the initial snake body."""
        for i in range(self.length):
            position = (-self.distance * i, 0) #x, y coordinates
            self._add_segment(position)

    def move(self):
        """Move the snake forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.distance)

    def up(self):
        """Turn the snake upward."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn the snake downward."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn the snake left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn the snake right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_length_increase(self):
        """Increase the length of the snake by adding a segment at the tail."""
        tail_position = self.segments[-1].position()
        self._add_segment(tail_position)
