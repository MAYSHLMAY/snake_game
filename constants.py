import pygame

''' SCREEN AND GRID '''

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SNAKE_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // SNAKE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // SNAKE_SIZE

''' SNAKE SPEED '''

FPS = 10


''' SNAKE COLOR, FOOD, ENVIRONMENT '''

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)

''' DIRECTIONS '''

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

''' GAME SETTINGS '''

INITIAL_SNAKE_LENGTH = 3
FOOD_SIZE = SNAKE_SIZE
SCORE_PER_FOOD = 10
WALL_COLLISION = False
SELF_COLLISION = True

""" player controls and directions """

DIRECTIONS = {
    "UP": (0, -SNAKE_SIZE),
    "DOWN": (0, SNAKE_SIZE),
    "LEFT": (-SNAKE_SIZE, 0),
    "RIGHT": (SNAKE_SIZE, 0),
}


PLAYER_CONTROLS = {

    "snake1": {
        pygame.K_UP: "UP",
        pygame.K_DOWN: "DOWN",
        pygame.K_LEFT: "LEFT",
        pygame.K_RIGHT: "RIGHT",
    },

    """ Optional for the future """

    "snake2": {
        pygame.K_w: "UP",
        pygame.K_s: "DOWN",
        pygame.K_a: "LEFT",
        pygame.K_d: "RIGHT",
    },

}