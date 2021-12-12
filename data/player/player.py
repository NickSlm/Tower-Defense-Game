from math import e
import pygame
from data.player.tower import DwarfHunter, DwarfSlayer, create_tower_profile

TEXT_COLOR = (0,0,0)


class GUI:
    text_offset = 10
    btn_pressed_offset = 6

    def __init__(self,screen):
        self.screen = screen
        # Fonts
        self.font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",24)
        # Images
        self.health_icon = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\heart.png')
        self.money_icon = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\gold-ingots.png')

        self.btn_1 = False
        self.btn_1_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button11.png')
        self.btn_1_rect = self.btn_1_srf.get_rect(topleft=(32, 32))
        self.btn_1_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button12.png')
        self.btn_1_pressed_rect = self.btn_1_pressed_srf.get_rect(topleft=(32, 32 + self.btn_pressed_offset))

        self.btn_2 = False
        self.btn_2_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button11.png')
        self.btn_2_rect = self.btn_2_srf.get_rect(topleft=(113, 32))
        self.btn_2_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button12.png')
        self.btn_2_pressed_rect = self.btn_2_pressed_srf.get_rect(topleft=(113, 32 + self.btn_pressed_offset))

        self.btn_3 = False
        self.btn_3_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button11.png')
        self.btn_3_rect = self.btn_3_srf.get_rect(topleft=(194, 32))
        self.btn_3_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button12.png')
        self.btn_3_pressed_rect = self.btn_3_pressed_srf.get_rect(topleft=(194, 32 + self.btn_pressed_offset))

        self.btn_4 = False
        self.btn_4_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button11.png')
        self.btn_4_rect = self.btn_4_srf.get_rect(topleft=(275, 32))
        self.btn_4_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button12.png')
        self.btn_4_pressed_rect = self.btn_4_pressed_srf.get_rect(topleft=(275, 32 + self.btn_pressed_offset))

        self.btn_5 = False
        self.btn_5_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button11.png')
        self.btn_5_rect = self.btn_5_srf.get_rect(topleft=(32, 113))
        self.btn_5_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button12.png')
        self.btn_5_pressed_rect = self.btn_5_pressed_srf.get_rect(topleft=(32, 113 + self.btn_pressed_offset))

        self.btn_6 = False
        self.btn_6_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button11.png')
        self.btn_6_rect = self.btn_6_srf.get_rect(topleft=(113, 113))
        self.btn_6_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button12.png')
        self.btn_6_pressed_rect = self.btn_6_pressed_srf.get_rect(topleft=(113, 113 + self.btn_pressed_offset))

        self.btn_7 = False
        self.btn_7_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button11.png')
        self.btn_7_rect = self.btn_7_srf.get_rect(topleft=(194,113))
        self.btn_7_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button12.png')
        self.btn_7_pressed_rect = self.btn_7_pressed_srf.get_rect(topleft=(194, 113 + self.btn_pressed_offset))

        self.btn_8 = False
        self.btn_8_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button11.png')
        self.btn_8_rect = self.btn_8_srf.get_rect(topleft=(275,113))
        self.btn_8_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\green_button12.png')
        self.btn_8_pressed_rect = self.btn_8_pressed_srf.get_rect(topleft=(275, 113 + self.btn_pressed_offset))

    def player_resources(self,round,health,money):
        health_text = self.font.render("Health: "+str(health), 1, TEXT_COLOR)
        money_text = self.font.render("Money: "+str(money), 1, TEXT_COLOR)
        round_text = self.font.render("Round: "+str(round), 1, TEXT_COLOR)
        self.screen.blit(health_text,(self.text_offset, self.text_offset))
        self.screen.blit(self.health_icon,(self.text_offset + health_text.get_width(), self.text_offset))
        self.screen.blit(money_text,(self.text_offset, health_text.get_height() + self.text_offset))
        self.screen.blit(self.money_icon,(self.text_offset + money_text.get_width(), health_text.get_height() + self.text_offset))
        self.screen.blit(round_text,((self.screen.get_width() // 2) - (round_text.get_width()// 2),self.text_offset))

    def tower_select_menu(self):
        self.menu = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\menu.png')
        self.menu_rect = self.menu.get_rect(topleft=(self.screen.get_width() - self.menu.get_width(),self.screen.get_height() - self.menu.get_height()))

        if not self.btn_1:
            self.menu.blit(self.btn_1_srf,self.btn_1_rect)
        if self.btn_1:
            self.menu.blit(self.btn_1_pressed_srf,self.btn_1_pressed_rect)

        if not self.btn_2:
            self.menu.blit(self.btn_2_srf,self.btn_2_rect)
        if self.btn_2:
            self.menu.blit(self.btn_2_pressed_srf,self.btn_2_pressed_rect)

        if not self.btn_3:
            self.menu.blit(self.btn_3_srf,self.btn_3_rect)
        if self.btn_3:
            self.menu.blit(self.btn_3_pressed_srf,self.btn_3_pressed_rect)

        if not self.btn_4:
            self.menu.blit(self.btn_4_srf,self.btn_4_rect)
        if self.btn_4:
            self.menu.blit(self.btn_4_pressed_srf,self.btn_4_pressed_rect)

        if not self.btn_5:
            self.menu.blit(self.btn_5_srf,self.btn_5_rect)
        if self.btn_5:
            self.menu.blit(self.btn_5_pressed_srf,self.btn_5_pressed_rect)

        if not self.btn_6:
            self.menu.blit(self.btn_6_srf,self.btn_6_rect)
        if self.btn_6:
            self.menu.blit(self.btn_6_pressed_srf,self.btn_6_pressed_rect)

        if not self.btn_7:
            self.menu.blit(self.btn_7_srf,self.btn_7_rect)
        if self.btn_7:
            self.menu.blit(self.btn_7_pressed_srf,self.btn_7_pressed_rect)

        if not self.btn_8:
            self.menu.blit(self.btn_8_srf,self.btn_8_rect)
        if self.btn_8:
            self.menu.blit(self.btn_8_pressed_srf,self.btn_8_pressed_rect)

        self.screen.blit(self.menu,self.menu_rect)

class Player:
    def __init__(self,screen):

        self.screen = screen
        self.health = 100
        self.money = 125

        self.gui = GUI(self.screen)

        self.show_menu = False

        # Tower group
        self.towers = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def draw_gui(self,round):
        # Player resources
        self.gui.player_resources(round,self.health,self.money)
        # Tower select menu
        if self.show_menu:
            self.gui.tower_select_menu()
        # Tower stats/talents
        for tower in self.towers:
            if tower.clicked:
                tower.stats_rect = create_tower_profile(self.screen,tower.name,tower.lvl,tower.damage,tower.attack_speed,tower.skill_point,tower.icon)

    def events(self,event,blockers):
        mouse_x,mouse_y = pygame.mouse.get_pos()

        # Tower events
        for tower in self.towers:
            # Select tower
            if event.type == pygame.MOUSEBUTTONUP:
                if tower.clicked == False:
                    if tower.rect.collidepoint((mouse_x,mouse_y)):
                        tower.clicked = True
                elif tower.clicked == True:
                    if not tower.stats_rect.collidepoint((mouse_x,mouse_y)):
                        tower.clicked = False
            # Hover on tower
            if tower.rect.collidepoint(pygame.mouse.get_pos()):
                tower.hover = True
            else:
                tower.hover = False

        # 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                self.gui.btn_1 = False
            if event.key == pygame.K_w:
                self.gui.btn_2 = False
            if event.key == pygame.K_e:
                self.gui.btn_3 = False
            if event.key == pygame.K_r:
                self.gui.btn_4 = False
            if event.key == pygame.K_a:
                self.gui.btn_5 = False
            if event.key == pygame.K_s:
                self.gui.btn_6 = False                
            if event.key == pygame.K_d:
                self.gui.btn_7 = False
            if event.key == pygame.K_f:
                self.gui.btn_8 = False                
        if event.type == pygame.KEYDOWN:
            # Summon towers
            if event.key == pygame.K_q:
                self.gui.btn_1 = True
                tower = DwarfHunter(mouse_x,mouse_y,self.bullets)
                if not pygame.sprite.spritecollideany(tower,blockers):
                    if not pygame.sprite.spritecollideany(tower,self.towers):
                        if self.money >= tower.cost:
                            self.towers.add(tower)
                            self.money -= tower.cost
            if event.key == pygame.K_w:
                self.gui.btn_2 = True
                tower = DwarfSlayer(mouse_x,mouse_y,self.bullets)
                if not pygame.sprite.spritecollideany(tower,blockers):
                    if not pygame.sprite.spritecollideany(tower,self.towers):
                        if self.money >= tower.cost:
                            self.towers.add(tower)
                            self.money -= tower.cost
            if event.key == pygame.K_e:
                self.gui.btn_3 = True
            if event.key == pygame.K_r:
                self.gui.btn_4 = True
            if event.key == pygame.K_a:
                self.gui.btn_5 = True
            if event.key == pygame.K_s:
                self.gui.btn_6 = True                
            if event.key == pygame.K_d:
                self.gui.btn_7 = True
            if event.key == pygame.K_f:
                self.gui.btn_8 = True

            if event.key == pygame.K_b:
                if self.show_menu == False:
                    self.show_menu = True
                else:
                    self.show_menu = False