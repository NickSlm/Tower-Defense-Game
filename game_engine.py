import pygame
from data.enemy.enemy import Enemy

from data.map.map import Map


class Game:
    """
    This class represents an instance of the game. If we need to
    reset the game we'd just need to create a new instance of this class. 
    """
    def __init__(self,screen):
        """
        Constructor. Create all our attributes and initialize the game. 
        """
        self.screen = screen
        # Create map and map objects/blockers
        self.map = Map(self.screen)
        self.blockers = self.map.blockers()
        self.enemy_path = self.map.checkpoints()

        # create sprite groups
        self.towers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # create tower

        # create enemy
        self.enemy = Enemy(self.enemy_path)
        self.enemies.add(self.enemy)



    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:              
                if event.key == pygame.K_ESCAPE:
                    return False
        return True

    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """

    def draw(self):
        """ Draw everything on the screen for the game. """
        # draw map
        self.map.background()
        
        # draw enemies
        self.enemies.update()
        self.enemies.draw(self.screen)

        


        self.map.foreground()
        pygame.display.flip()

