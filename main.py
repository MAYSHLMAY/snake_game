import pygame
from game import Game
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    game = Game(screen, clock, FPS)
    game.main_game_loop()

    pygame.quit()

if __name__ == "__main__":
    main()