import pygame
from constants import SNAKE_SIZE, BLACK, RED, GREEN, DARK_GREEN, SCREEN_WIDTH, SCREEN_HEIGHT



class Snake:

    """
    The Snake class handles the snake's movement, growth,
    collision detection, and drawing on the screen.
    """

    def __init__(self, x, y):

        """Initialize snake with one segment at (x, y)."""
        self.segments = [(x, y)]
        self.direction = pygame.K_RIGHT 