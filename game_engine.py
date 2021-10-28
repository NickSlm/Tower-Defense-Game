import pygame
from data.enemy.enemy import Enemy, Enemy2
from data.game.ui import Health
from data.game.wave import Wave
from data.map.map import Map
from time import sleep

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
        self.myFont = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",24)

        # Game
        self.game_over = False
        self.round_running = False
        self.enemies_spawn = False

        self.round = 1

        self.health= 100
        self.money = 0

        # create sprite groups
        self.towers = pygame.sprite.Group()

        # Create wave instance
        self.enemies = pygame.sprite.Group()
        self.wave = Wave(self.enemy_path)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:              
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_r:
                    if self.round_running == False:
                        self.round_running = True
                        self.enemies_spawn = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__(self.screen)
                
        return True

    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """        
        if not self.game_over:
            if self.round_running:
                if self.enemies_spawn:
                    self.wave.generate_wave(self.round,self.enemies)
                    self.enemies_spawn = False
                elif self.enemies_spawn == False:
                    if not self.enemies:
                        self.round_running = False
                        self.round += 1
                

        print(self.enemies)

    def draw(self):
        """ Draw everything on the screen for the game. """
        # draw map background
        self.map.background()
        if not self.game_over:
            # draw towers
            self.towers.update()
            self.towers.draw(self.screen)
            # draw enemies
            self.enemies.update()
            self.enemies.draw(self.screen)


        # draw map foreground
        self.map.foreground()
        
        if self.game_over:
            text = self.myFont.render("Game Over, click to restart", 1, (0,0,0))
            center_x = (1920 // 2) - (text.get_width() // 2)
            center_y = (1088 // 4) - (text.get_height() // 2)
            self.screen.blit(text, [center_x, center_y])

        # draw player's resources
        self.health_text = self.myFont.render("Health: "+str(self.health), 1, (0,0,0))
        self.money_text = self.myFont.render("Money: "+str(self.money), 1, (0,0,0))
        self.round_text = self.myFont.render("Round: "+str(self.round), 1, (0,0,0))
        self.screen.blit(self.health_text,(10,10))
        self.screen.blit(self.money_text,(10,40))
        self.screen.blit(self.round_text,(960 - (self.round_text.get_width()// 2),10))

        pygame.display.flip()

