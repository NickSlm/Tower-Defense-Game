from typing_extensions import runtime
import pygame
from game_engine import Game



# CONST VARIABLES
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1088

def main():
    # Initialize pygame
    pygame.init()

    # Set Screen size
    screen_size = (SCREEN_WIDTH,SCREEN_HEIGHT)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Nigga game")

    clock = pygame.time.Clock()
    game = Game(screen)


    running = True

    while running:
        running = game.events()
        game.run_logic()
        game.draw()
        clock.tick(60)
    pygame.quit()



if __name__ == "__main__":
    main()