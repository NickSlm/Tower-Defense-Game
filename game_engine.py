import pygame
from data.enemy.spawn_enemy import EnemyWave
from data.map.map import Map
from data.player.player import Player

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
        self.clock = pygame.time.Clock()

        # Create map and map objects/blockers
        self.map = Map(self.screen)
        self.blockers = self.map.blockers()
        self.enemy_path = self.map.checkpoints()
        
        # Delta time
        self.dt = 0
        # Fonts
        self.font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",24)

        # Game
        self.game_over = False
        self.round_running = False
        self.round = 1

        # Initialize Player
        self.player = Player(self.screen)

        # Create wave
        self.enemy_wave = EnemyWave(self.enemy_path)

    def events(self):
        # Handling player events
        for event in pygame.event.get():
            self.player.events(event,self.blockers)

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_p:
                    self.__init__(self.screen)

                if event.key == pygame.K_ESCAPE:
                    return False
                    
                if event.key == pygame.K_SPACE:
                    if self.round_running == False:
                        self.round_running = True
                        self.enemy_wave.enemy_spawn = True

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

            # Update player towers 
            self.player.towers.update(self.dt,self.enemy_wave.enemy_sprites)
            self.player.bullets.update()

            if self.round_running:
                # Enemy spawn
                if self.enemy_wave.enemy_spawn:
                    self.enemy_wave.generate_enemies(self.round)
                elif not self.enemy_wave.enemy_spawn:
                    if not self.enemy_wave.enemy_sprites:
                        self.round_running = False
                        self.round += 1
               
                # Update enemies
                for sprite in self.enemy_wave.enemy_sprites:
                    if sprite.update():
                        self.player.health -= sprite.damage
                    if sprite.hp <= 0:
                        self.player.money += sprite.money
                        for tower in self.player.towers:
                            tower.xp += sprite.xp
                        sprite.kill()

                # Check projectile collision
                for bullet in self.player.bullets:
                    if pygame.sprite.spritecollideany(bullet,self.enemy_wave.enemy_sprites):
                        pygame.sprite.spritecollideany(bullet,self.enemy_wave.enemy_sprites).hp -= bullet.DAMAGE
                        bullet.kill()

                # Game-over condition
                if self.player.health <= 0 or self.round == 100:
                    self.game_over = True
    def draw(self):
        """ Draw everything on the screen for the game. """
        # Draw map background
        self.map.background()

        if not self.game_over:
            # Draw towers
            self.player.towers.draw(self.screen)
            self.player.bullets.draw(self.screen)

            # Draw enemies
            self.enemy_wave.enemy_sprites.draw(self.screen)

        # Draw map foreground
        self.map.foreground()
        
        # Draw tower profile stats/talents
        for tower in self.player.towers:
            tower.draw_range(self.screen)

        # Draw game-over screen
        if self.game_over:
            text = self.font.render("Game Over, click to restart", 1, (0,0,0))
            center_x = (1920 // 2) - (text.get_width() // 2)
            center_y = (1088 // 4) - (text.get_height() // 2)
            self.screen.blit(text, [center_x, center_y])

        # Draw player's GUI
        self.player.draw_gui(self.round)

        pygame.display.flip()
        self.dt = self.clock.tick(60)