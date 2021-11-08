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
    game_icon = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\game_icon.png')

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Nigga game")
    pygame.display.set_icon(game_icon)

    game = Game(screen)

    running = True
    while running:
        running = game.events()
        game.run_logic()
        game.draw()
    pygame.quit()



if __name__ == "__main__":
    main()