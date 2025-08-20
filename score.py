import pygame

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

    def draw_score(self, screen ,x_cor=20, y_cor=20): # Used x_cor = 20 and y_cor = 20
        """
        Render the score on the given screen.
        Args:
            screen: pygame.Surface object where the score will be rendered.
            x_cor (int, optional): X coordinate for the score display. Defaults to 20.
            y_cor (int, optional): Y coordinate for the score display. Defaults to 20.
        """
        text_surface = self.font.render(str(self.score), False, (0,0,0))
        screen.blit(text_surface, (x_cor, y_cor))

    def increase_score(self, screen, x_cor=20, y_cor=20):
        """
        Increases the score by 1 and updates the display.
        Args:
            screen: pygame.Surface object where the score will be rendered.
            x_cor (int, optional): X coordinate for the score display. Defaults to 20.
            y_cor (int, optional): Y coordinate for the score display. Defaults to 20.
        """
        self.score += 1
        self.draw_score(screen=screen, x_cor=x_cor, y_cor=y_cor)

