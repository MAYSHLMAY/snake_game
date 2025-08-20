import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Score:
    """
    Manages the scoring system of the game
    """
    def __init__(self):
        """
        Initializes the class instance(score, font)
        """
        self.score = 0
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
