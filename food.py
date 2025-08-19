import pygame
import random
from constants import SNAKE_SIZE, RED, SCREEN_WIDTH, SCREEN_HEIGHT

class Food:

    """
    Food class handles random placement, drawing, 
    and collision detection with the snake.
    """
    

    def __init__(self):

        """Initialize food at a random position."""
        self.position = self.random_position()

    def random_position(self):
        
        """Generate a random position aligned to the grid."""