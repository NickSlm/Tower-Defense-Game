import pygame
from data.player.tower import DwarfHunter, DwarfSlayer




class Player:
    def __init__(self,screen):
        self.screen = screen
        self.health = 100
        self.money = 125
        self.health_icon = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\heart.png')
        self.money_icon = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\gold-ingots.png')
        # self.inventory_img = pygame.image.load(r'')
        # Fonts
        self.font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",24)

        # Tower group
        self.towers = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def draw_player_resources(self,round):
        self.health_text = self.font.render("Health: "+str(self.health), 1, (0,0,0))
        self.money_text = self.font.render("Money: "+str(self.money), 1, (0,0,0))
        self.round_text = self.font.render("Round: "+str(round), 1, (0,0,0))
        self.screen.blit(self.health_text,(10,10))
        self.screen.blit(self.health_icon,(10 + self.health_text.get_width(),10))
        self.screen.blit(self.money_text,(10,40))
        self.screen.blit(self.money_icon,(10 + self.money_text.get_width(),40))
        self.screen.blit(self.round_text,(960 - (self.round_text.get_width()// 2),10))

    def events(self,event,blockers):
        if event.type == pygame.KEYDOWN:
            # Summon towers
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if event.key == pygame.K_q:
                tower = DwarfHunter(mouse_x,mouse_y,self.bullets)
                if not pygame.sprite.spritecollideany(tower,blockers):
                    if not pygame.sprite.spritecollideany(tower,self.towers):
                        if self.money >= 0 + tower.cost:
                            self.towers.add(tower)
                            self.money -= tower.cost
            if event.key == pygame.K_w:
                tower = DwarfSlayer(mouse_x,mouse_y,self.bullets)
                if not pygame.sprite.spritecollideany(tower,blockers):
                    if not pygame.sprite.spritecollideany(tower,self.towers):
                        if self.money >= 0 + tower.cost:
                            self.towers.add(tower)
                            self.money -= tower.cost
            if event.key == pygame.K_e:
                pass          
            if event.key == pygame.K_r:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_s:
                pass
            if event.key == pygame.K_d:
                pass
            if event.key == pygame.K_f:
                pass
            # Open towers menu
            if event.key == pygame.K_b:
                pass
            # 