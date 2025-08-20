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
        x = random.randint(0, (SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        return (x, y)  
    def spawn(self):
        """Respawn food at a new random position."""
        self.position = self.random_position()

    def check_collision(self, snake_head):
        """
        Check if the snake ate the food.
        Returns True if collision occurs.
        """
        if self.position == snake_head:
            self.spawn()  # respawn food immediately
            return True
        return False

    def draw(self, screen):
        """Draw the food on the screen."""
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))