import pygame
import sys
from itertools import islice
import deque
from constants import DIRECTIONS, SNAKE_SIZE, BLACK, RED, GREEN, DARK_GREEN, SCREEN_WIDTH, SCREEN_HEIGHT



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

        """Move snake to the specific direction"""

        head_x, head_y = self.segments[0]
        dx, dy = DIRECTIONS[self.direction]
        head_x += dx
        head_y += dy

        # adding new head for the snake

        self.segments.appendleft((head_x, head_y))

        # remove tail unless growing

        if not self.grow_pending:
            self.segments.pop()
        else:
            self.grow_pending = False

    def handle_key(self, key):

        """Update direction if key pressed matches this snake's controls"""
        if key in self.controls:
            new_dir = self.controls[key]
            opposite = {
                "UP": "DOWN",
                "DOWN": "UP",
                "LEFT": "RIGHT",
                "RIGHT": "LEFT",
            }
            if new_dir != opposite.get(self.direction):
                self.direction = new_dir
    def grow(self):
        """Mark snake to grow on next move."""
        self.grow_pending = True
    def check_wall_collision(self):
        """Return True if snake hits a wall."""
        head_x, head_y = self.segments[0]
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            print("collided")
            return True
        return False
    def die(self):
        self.alive = False

    def check_self_collision(self):
        """Return True if snake hits itself."""
        head = self.segments[0]
        if head in islice(self.segments, 1, len(self.segments)):
            return True
        return False

    def draw(self, screen):
        """Draw the snake on the screen."""
        for i, segment in enumerate(self.segments):
            color = DARK_GREEN if i == 0 else GREEN 
            pygame.draw.rect(screen, color, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    

    