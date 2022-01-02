from math import e
import pygame
from pygame import mouse
from data.player.tower import DwarfHunter, DwarfSlayer

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

        # Tower select menu buttons
        self.btn_1 = False
        self.btn_1_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1.png')
        self.btn_1_rect = self.btn_1_srf.get_rect(topleft=(48, 26))
        self.btn_1_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1_pressed.png')
        self.btn_1_pressed_rect = self.btn_1_pressed_srf.get_rect(topleft=(48, 26))

        self.btn_2 = False
        self.btn_2_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\2.png')
        self.btn_2_rect = self.btn_2_srf.get_rect(topleft=(144, 26))
        self.btn_2_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\2_pressed.png')
        self.btn_2_pressed_rect = self.btn_2_pressed_srf.get_rect(topleft=(144, 26))

        self.btn_3 = False
        self.btn_3_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1.png')
        self.btn_3_rect = self.btn_3_srf.get_rect(topleft=(242, 26))
        self.btn_3_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1_pressed.png')
        self.btn_3_pressed_rect = self.btn_3_pressed_srf.get_rect(topleft=(242, 26))

        self.btn_4 = False
        self.btn_4_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1.png')
        self.btn_4_rect = self.btn_4_srf.get_rect(topleft=(336, 26))
        self.btn_4_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1_pressed.png')
        self.btn_4_pressed_rect = self.btn_4_pressed_srf.get_rect(topleft=(336, 26))

        self.btn_5 = False
        self.btn_5_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1.png')
        self.btn_5_rect = self.btn_5_srf.get_rect(topleft=(48, 154))
        self.btn_5_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1_pressed.png')
        self.btn_5_pressed_rect = self.btn_5_pressed_srf.get_rect(topleft=(48, 154))

        self.btn_6 = False
        self.btn_6_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1.png')
        self.btn_6_rect = self.btn_6_srf.get_rect(topleft=(144, 154))
        self.btn_6_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1_pressed.png')
        self.btn_6_pressed_rect = self.btn_6_pressed_srf.get_rect(topleft=(144, 154))

        self.btn_7 = False
        self.btn_7_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1.png')
        self.btn_7_rect = self.btn_7_srf.get_rect(topleft=(242,154))
        self.btn_7_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1_pressed.png')
        self.btn_7_pressed_rect = self.btn_7_pressed_srf.get_rect(topleft=(242,154))

        self.btn_8 = False
        self.btn_8_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1.png')
        self.btn_8_rect = self.btn_8_srf.get_rect(topleft=(336,154))
        self.btn_8_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\1_pressed.png')
        self.btn_8_pressed_rect = self.btn_8_pressed_srf.get_rect(topleft=(336,154))

        # Start round button
        # self.start_btn = False
        # self.start_btn_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\start.png')
        # self.start_btn_rect = self.start_btn_srf.get_rect(topleft = (500,500))
        # self.start_btn_pressed_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\start_pressed.png')
        # self.start_btn_pressed_rect = self.start_btn_pressed_srf.get_rect(topleft = (500,500))

    def player_resources(self,round,health,money):
        health_text = self.font.render("Health: "+str(health), 1, TEXT_COLOR)
        money_text = self.font.render("Money: "+str(money), 1, TEXT_COLOR)
        round_text = self.font.render("Round: "+str(round), 1, TEXT_COLOR)
        self.screen.blit(health_text,(self.text_offset, self.text_offset))
        self.screen.blit(self.health_icon,(self.text_offset + health_text.get_width(), self.text_offset))
        self.screen.blit(money_text,(self.text_offset, health_text.get_height() + self.text_offset))
        self.screen.blit(self.money_icon,(self.text_offset + money_text.get_width(), health_text.get_height() + self.text_offset))
        self.screen.blit(round_text,((self.screen.get_width() // 2) - (round_text.get_width() // 2),self.text_offset))

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

        self.show_menu = True

        # Tower group
        self.towers = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def draw_gui(self,round):
        # Player resources
        self.gui.player_resources(round, self.health, self.money)
        # Tower select menu
        if self.show_menu:
            self.gui.tower_select_menu()
        # Tower stats/talents
        for tower in self.towers:
            if tower.clicked:
                tower.tower_profile.create_tower_profile(self.screen)
                   
    def update(self):
        # Show tower range on hover
        for tower in self.towers:
            if tower.rect.collidepoint(pygame.mouse.get_pos()):
                tower.hover = True
            else:
                tower.hover = False

    def events(self,event,blockers):
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            for tower in self.towers:
                if tower.clicked == False:
                    # Open tower profile
                    if tower.rect.collidepoint((mouse_x,mouse_y)):
                        tower.clicked = True
                elif tower.clicked == True:
                    # Open/Close talents
                    if tower.tower_profile.open_talents:
                        # Level up talents
                        if tower.skill_point > 0:
                            if tower.tower_profile.skill_1_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_1']['current_upgrades'] < tower.skill_tree['skill_1']['max_upgrades']:
                                    tower.skill_tree['skill_1']['current_upgrades'] += 1
                                    tower.skill_point -= 1
                                    tower.skill_tree['skill_1']['lvl_up'] = True
                            if tower.tower_profile.skill_2_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_2']['current_upgrades'] < tower.skill_tree['skill_2']['max_upgrades']:
                                    tower.skill_tree['skill_2']['current_upgrades'] += 1
                                    tower.skill_point -= 1
                                    tower.skill_tree['skill_2']['lvl_up'] = True
                            if tower.tower_profile.skill_3_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_3']['current_upgrades'] < tower.skill_tree['skill_3']['max_upgrades']:
                                    tower.skill_tree['skill_3']['current_upgrades'] += 1
                                    tower.skill_point -= 1
                            if tower.tower_profile.skill_4_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_4']['current_upgrades'] < tower.skill_tree['skill_4']['max_upgrades']:
                                    tower.skill_tree['skill_4']['current_upgrades'] += 1
                                    tower.skill_point -= 1   
                            if tower.tower_profile.skill_5_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_5']['current_upgrades'] < tower.skill_tree['skill_5']['max_upgrades']:
                                    tower.skill_tree['skill_5']['current_upgrades'] += 1
                                    tower.skill_point -= 1
                            if tower.tower_profile.skill_6_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_6']['current_upgrades'] < tower.skill_tree['skill_6']['max_upgrades']:
                                    tower.skill_tree['skill_6']['current_upgrades'] += 1
                                    tower.skill_point -= 1
                            if tower.tower_profile.skill_7_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_7']['current_upgrades'] < tower.skill_tree['skill_7']['max_upgrades']:
                                    tower.skill_tree['skill_7']['current_upgrades'] += 1
                                    tower.skill_point -= 1
                            if tower.tower_profile.skill_8_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_8']['current_upgrades'] < tower.skill_tree['skill_8']['max_upgrades']:
                                    tower.skill_tree['skill_8']['current_upgrades'] += 1
                                    tower.skill_point -= 1  
                            if tower.tower_profile.skill_9_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_9']['current_upgrades'] < tower.skill_tree['skill_9']['max_upgrades']:
                                    tower.skill_tree['skill_9']['current_upgrades'] += 1
                                    tower.skill_point -= 1   
                            if tower.tower_profile.skill_10_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_10']['current_upgrades'] < tower.skill_tree['skill_10']['max_upgrades']:
                                    tower.skill_tree['skill_10']['current_upgrades'] += 1
                                    tower.skill_point -= 1
                            if tower.tower_profile.skill_11_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_11']['current_upgrades'] < tower.skill_tree['skill_11']['max_upgrades']:
                                    tower.skill_tree['skill_11']['current_upgrades'] += 1
                                    tower.skill_point -= 1
                            if tower.tower_profile.skill_12_rect.collidepoint((mouse_x - 1111,mouse_y - 892)):
                                if tower.skill_tree['skill_12']['current_upgrades'] < tower.skill_tree['skill_12']['max_upgrades']:
                                    tower.skill_tree['skill_12']['current_upgrades'] += 1
                                    tower.skill_point -= 1                                                                                                                                          
                        if tower.tower_profile.close_talents_rect.collidepoint((mouse_x,mouse_y)):
                            tower.tower_profile.open_talents = False
                    else:
                        if tower.tower_profile.open_talents_rect.collidepoint((mouse_x,mouse_y)):
                            tower.tower_profile.open_talents = True
                    # Close tower profile
                    if not tower.tower_profile.tower_profile_rect.collidepoint((mouse_x,mouse_y)):
                        tower.clicked = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
                    
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