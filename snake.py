import pygame
import sys
from itertools import islice
import deque
from constants import SNAKE_SIZE, BLACK, RED, GREEN, DARK_GREEN, SCREEN_WIDTH, SCREEN_HEIGHT



class Snake:

    """
    The Snake class handles the snake's movement, growth,
    collision detection, and drawing on the screen.
    """

    def __init__(self, controls, start_pos):

        """Initialize snake with one segment at (x, y)."""
        self.segments = deque([start_pos]) 
        self.direction = "RIGHT"
        self.controls = controls
        self.grow_pending = False
        self.alive = True 

    def move(self):
        pass