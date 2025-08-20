import pygame
from snake import Snake
from food import Food
from score import Score
from constants import PLAYER_CONTROLS

class Game:
    """Manages the main game logic and state.

    Args:
        screen: pygame.Surface object for rendering the game.
        clock: pygame.time.Clock object to control the game loop timing.
        fps (int): Frames per second for the game loop.
    """

    def __init__(self, screen, clock, fps):

        """Initializes the game with screen, clock, and FPS settings.

        Args:
            screen: pygame.Surface object for rendering the game.
            clock: pygame.time.Clock object to control the game loop timing.
            fps (int): Frames per second for the game loop.
        """

        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.state = "main_game"
        self.snake1 = Snake(PLAYER_CONTROLS["snake1"], (100, 100))
        self.snakes = [self.snake1]
        self.food = Food()
        self.score = Score()

    def main_game_loop(self):

        """Runs the main game loop, handling events, updates, and rendering.

        Handles user input, updates game objects, and renders the game state
        to the screen.
        """

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    for snake in self.snakes:
                        snake.handle_key(event.key)

            self.screen.fill((0, 0, 0))
            self.score.draw_score(self.screen)
            for snake in self.snakes:
                snake.move()
                if snake.check_wall_collision() or snake.check_self_collision():
                    snake.die()
                if self.food.check_collision(snake.segments[0]):
                    snake.grow()
                    self.score.increase_score(self.screen)
                if snake.alive:
                    snake.draw(self.screen)
                else:
                    running = False

            self.food.draw(self.screen)
            pygame.display.update()
            self.clock.tick(self.fps)