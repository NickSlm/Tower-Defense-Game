import pygame
import json
from data.enemy.enemy import Enemy, Enemy2, Enemy3
from data.enemy.spawn_enemy import EnemyWave
from data.game.player import Player
from data.map.map import Map
from data.player.tower import Tower

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
        
        # Fonts
        self.font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",24)

        # Game
        self.game_over = False
        self.round_running = False
        self.enemy_spawn = False
        self.round = 1

        # Initialize Player
        self.player = Player(self.screen)

        # Create player sprites
        self.towers = pygame.sprite.Group()

        # Create wave
        self.enemy_wave = EnemyWave()
        with open(r"D:\Games\Tower-Defense-Game\data\game\round.json") as json_file:
            self.data = json.load(json_file)
        self.enemy_index = 0 
        self.enemy_summoned = 0
        self.enemy_sprites = pygame.sprite.Group()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN: 
                mouse_x,mouse_y = pygame.mouse.get_pos()
                if event.key == pygame.K_r:
                    if not pygame.sprite.spritecollideany(Tower(mouse_x,mouse_y),self.blockers):
                        if not pygame.sprite.spritecollideany(Tower(mouse_x,mouse_y),self.towers):
                            self.towers.add(Tower(mouse_x,mouse_y))   

                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_SPACE:
                    if self.round_running == False:
                        self.round_running = True
                        self.enemies_spawn = True

            if event.type == pygame.KEYUP:
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
        print("a")
        if not self.game_over:
            if self.round_running:
                if self.enemies_spawn:
                    # 
                    self.enemy_type = self.data[str(self.round)]["enemy_order_type"][self.enemy_index]
                    amount = self.data[str(self.round)]["enemy_amount"][self.enemy_index]
                    # Render Enemy
                    if self.enemy_summoned < amount:
                        if self.enemy_type == "red":
                            if not pygame.sprite.spritecollideany(Enemy(self.enemy_path),self.enemy_sprites):
                                self.enemy_sprites.add(Enemy(self.enemy_path))
                                self.enemy_summoned += 1
                        if self.enemy_type == "blue":
                            if not pygame.sprite.spritecollideany(Enemy2(self.enemy_path),self.enemy_sprites):
                                self.enemy_sprites.add(Enemy2(self.enemy_path))
                                self.enemy_summoned += 1
                        if self.enemy_type == "green":
                            if not pygame.sprite.spritecollideany(Enemy3(self.enemy_path),self.enemy_sprites):
                                self.enemy_sprites.add(Enemy3(self.enemy_path))
                                self.enemy_summoned += 1
                    # 
                    if self.enemy_summoned == amount:
                        self.enemy_summoned = 0 
                        self.enemy_index +=1

                    if len(self.enemy_sprites) == sum(self.data[str(self.round)]["enemy_amount"]):
                        self.enemy_index = 0
                        self.enemies_spawn = False
                    # 
                elif not self.enemies_spawn:
                    if not self.enemy_sprites:
                        self.round_running = False
                        self.round += 1

                # Update player towers
                self.towers.update()

                # Update enemies
                for sprite in self.enemy_sprites:
                    if sprite.update():
                        self.player.health -= sprite.damage
                
                # Game-over condition
                if self.player.health <= 0 or self.round == 100:
                    self.game_over = True

    def draw(self):
        """ Draw everything on the screen for the game. """
        # Draw map background
        self.map.background()

        if not self.game_over:
            # Draw towers
            self.towers.draw(self.screen)
            # Draw enemies
            self.enemy_sprites.draw(self.screen)

        # Draw map foreground
        self.map.foreground()
        

        # Draw game-over screen
        if self.game_over:
            text = self.font.render("Game Over, click to restart", 1, (0,0,0))
            center_x = (1920 // 2) - (text.get_width() // 2)
            center_y = (1088 // 4) - (text.get_height() // 2)
            self.screen.blit(text, [center_x, center_y])

        # Draw player's resources
        self.player.draw_player_resources(self.round)

        pygame.display.flip()
        self.clock.tick(60)


