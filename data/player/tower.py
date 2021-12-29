import json
from os import stat
import pygame
import math
from pygame import image

from data.player.projectile import Arrow

FONT_COLOR = (0,0,0)

class TowerProfile:
    def __init__(self,tower):
        self.font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",14)
        self.tower = tower
        self.profile_width = 224
        self.profile_height = 196
        self.icon = self.tower.icon
        self.icon_width,self.icon_height = self.icon.get_size()
        self.offset = 4

        self.open_talents = False

        self.tower_profile_srf = pygame.Surface((520,200))
        self.tower_profile_rect = self.tower_profile_srf.get_rect(topleft=(848,892))
    def create_tower_profile(self,screen):
        # Skill buttons
        self.skill_1_srf = pygame.image.load(self.tower.skill_tree['skill_1']['icon'])
        self.skill_1_rect = self.skill_1_srf.get_rect(topleft = (14,14))
        self.skill_1_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_1']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_1']['max_upgrades']), 1, (255,255,255))
        self.skill_1_srf.blit(self.skill_1_upgrades_text,(0,0))

        self.skill_2_srf = pygame.image.load(self.tower.skill_tree['skill_2']['icon'])
        self.skill_2_rect = self.skill_2_srf.get_rect(topleft = (14,76))
        self.skill_2_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_2']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_2']['max_upgrades']), 1, (255,255,255))
        self.skill_2_srf.blit(self.skill_2_upgrades_text,(0,0))

        self.skill_3_srf = pygame.image.load(self.tower.skill_tree['skill_3']['icon'])
        self.skill_3_rect = self.skill_3_srf.get_rect(topleft = (14,138))
        self.skill_3_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_3']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_3']['max_upgrades']), 1, (255,255,255))
        self.skill_3_srf.blit(self.skill_3_upgrades_text,(0,0))

        self.skill_4_srf = pygame.image.load(self.tower.skill_tree['skill_4']['icon'])
        self.skill_4_rect = self.skill_4_srf.get_rect(topleft = (76,14))
        self.skill_4_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_4']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_4']['max_upgrades']), 1, (255,255,255))
        self.skill_4_srf.blit(self.skill_4_upgrades_text,(0,0))

        self.skill_5_srf = pygame.image.load(self.tower.skill_tree['skill_5']['icon'])
        self.skill_5_rect = self.skill_5_srf.get_rect(topleft = (76,76))
        self.skill_5_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_5']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_5']['max_upgrades']), 1, (255,255,255))
        self.skill_5_srf.blit(self.skill_5_upgrades_text,(0,0))

        self.skill_6_srf = pygame.image.load(self.tower.skill_tree['skill_6']['icon'])
        self.skill_6_rect = self.skill_6_srf.get_rect(topleft = (76,138))
        self.skill_6_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_6']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_6']['max_upgrades']), 1, (255,255,255))
        self.skill_6_srf.blit(self.skill_6_upgrades_text,(0,0))

        self.skill_7_srf = pygame.image.load(self.tower.skill_tree['skill_7']['icon'])
        self.skill_7_rect = self.skill_7_srf.get_rect(topleft = (138,14))
        self.skill_7_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_7']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_7']['max_upgrades']), 1, (255,255,255))
        self.skill_7_srf.blit(self.skill_7_upgrades_text,(0,0))

        self.skill_8_srf = pygame.image.load(self.tower.skill_tree['skill_8']['icon'])
        self.skill_8_rect = self.skill_8_srf.get_rect(topleft = (138,76))
        self.skill_8_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_8']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_8']['max_upgrades']), 1, (255,255,255))
        self.skill_8_srf.blit(self.skill_8_upgrades_text,(0,0))

        self.skill_9_srf = pygame.image.load(self.tower.skill_tree['skill_9']['icon'])
        self.skill_9_rect = self.skill_9_srf.get_rect(topleft = (138,138))
        self.skill_9_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_9']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_9']['max_upgrades']), 1, (255,255,255))
        self.skill_9_srf.blit(self.skill_9_upgrades_text,(0,0))

        self.skill_10_srf = pygame.image.load(self.tower.skill_tree['skill_10']['icon'])
        self.skill_10_rect = self.skill_10_srf.get_rect(topleft = (200,14))
        self.skill_10_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_10']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_10']['max_upgrades']), 1, (255,255,255))
        self.skill_10_srf.blit(self.skill_10_upgrades_text,(0,0))

        self.skill_11_srf = pygame.image.load(self.tower.skill_tree['skill_11']['icon'])
        self.skill_11_rect = self.skill_11_srf.get_rect(topleft = (200,76))
        self.skill_11_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_11']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_11']['max_upgrades']), 1, (255,255,255))
        self.skill_11_srf.blit(self.skill_11_upgrades_text,(0,0))

        self.skill_12_srf = pygame.image.load(self.tower.skill_tree['skill_12']['icon'])
        self.skill_12_rect = self.skill_12_srf.get_rect(topleft = (200,138))
        self.skill_12_upgrades_text = self.font.render(str(self.tower.skill_tree['skill_12']['current_upgrades'])+"/"+str(self.tower.skill_tree['skill_12']['max_upgrades']), 1, (255,255,255))
        self.skill_12_srf.blit(self.skill_12_upgrades_text,(0,0))

        self.icon_rect = self.icon.get_rect(topleft=(self.offset,self.offset))

        # Stats text
        self.name_text = self.font.render(self.tower.name, 1, FONT_COLOR)
        self.name_text_rect = self.name_text.get_rect(topleft = (((self.profile_width -(self.profile_width - self.icon_width - self.offset)) + (self.profile_width - self.icon_width - self.offset) // 2) - self.name_text.get_width() // 2,self.offset))
        self.lvl_text = self.font.render("Lvl: "+str(self.tower.lvl), 1, FONT_COLOR)
        self.lvl_text_rect = self.lvl_text.get_rect(topleft = (self.icon_width + self.offset * 2, self.name_text.get_height() + self.offset))
        self.damage_text = self.font.render("Damage: "+str(self.tower.damage), 1, FONT_COLOR)
        self.damage_text_rect = self.damage_text.get_rect(topleft = self.lvl_text_rect.bottomleft)
        self.attack_speed_text = self.font.render("AS: " + "%.2f" % self.tower.attack_speed, 1, FONT_COLOR)
        self.attack_speed_text_rect = self.attack_speed_text.get_rect(topleft = self.damage_text_rect.bottomleft)
        self.skill_point_text = self.font.render("Skill Point: "+str(self.tower.skill_point),1, FONT_COLOR)    
        self.skill_point_text_rect = self.skill_point_text.get_rect(topleft = (self.icon_width + self.offset * 2,(self.icon_height + self.offset) - self.skill_point_text.get_height()))

        self.stats_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\tower_profile.png')
        self.stats_rect = self.stats_srf.get_rect(topleft=(((screen.get_width() // 2) - (self.stats_srf.get_width()// 2),screen.get_height() - self.stats_srf.get_height())))

        # Close/Open talents panel
        self.open_talents_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\open_talents.png')
        self.open_talents_rect = self.open_talents_srf.get_rect(topleft=(1072,screen.get_height() - self.stats_srf.get_height() + 83))
        self.close_talents_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\close_talents.png')
        self.close_talents_rect = self.close_talents_srf.get_rect(topleft=(1072,screen.get_height() - self.stats_srf.get_height() + 83))

        self.talents_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\talents_frame.png')
        self.talents_rect = self.talents_srf.get_rect(topleft=(self.open_talents_rect.x + self.open_talents_rect.width,self.stats_rect.y))

        stats_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\tower_profile.png')
        stats_rect = stats_srf.get_rect(topleft=(((screen.get_width() // 2) - (stats_srf.get_width()// 2),screen.get_height() - stats_srf.get_height())))
        
        stats_srf.blit(self.tower.icon,self.icon_rect)
        stats_srf.blit(self.name_text, self.name_text_rect)
        # Stats border
        pygame.draw.rect(stats_srf,(0,0,0),[self.icon_width + self.offset + 2, self.name_text.get_height() + self.offset, (self.profile_width - self.icon_width - (self.offset * 2 + 2)), self.icon_height - self.name_text.get_height()],1)
        # Stats
        stats_srf.blit(self.lvl_text,self.lvl_text_rect)
        stats_srf.blit(self.damage_text,self.damage_text_rect)
        stats_srf.blit(self.attack_speed_text,self.attack_speed_text_rect)
        stats_srf.blit(self.skill_point_text,self.skill_point_text_rect)

        screen.blit(stats_srf,stats_rect)

        self.talents_srf.blit(self.skill_1_srf,self.skill_1_rect)
        self.talents_srf.blit(self.skill_2_srf,self.skill_2_rect)
        self.talents_srf.blit(self.skill_3_srf,self.skill_3_rect)
        self.talents_srf.blit(self.skill_4_srf,self.skill_4_rect)
        self.talents_srf.blit(self.skill_5_srf,self.skill_5_rect)
        self.talents_srf.blit(self.skill_6_srf,self.skill_6_rect)
        self.talents_srf.blit(self.skill_7_srf,self.skill_7_rect)
        self.talents_srf.blit(self.skill_8_srf,self.skill_8_rect)
        self.talents_srf.blit(self.skill_9_srf,self.skill_9_rect)
        self.talents_srf.blit(self.skill_10_srf,self.skill_10_rect)
        self.talents_srf.blit(self.skill_11_srf,self.skill_11_rect)
        self.talents_srf.blit(self.skill_12_srf,self.skill_12_rect)

        if self.open_talents:
            screen.blit(self.close_talents_srf,self.close_talents_rect)
            screen.blit(self.talents_srf,self.talents_rect)
        else:
            screen.blit(self.open_talents_srf,self.open_talents_rect)
def find_nearest_target(enemy_sprites, tower):
    target = [tower.attack_range,None]
    for enemy in enemy_sprites:
        x,y = enemy.rect.centerx, enemy.rect.centery
        distance = math.sqrt(abs((x - tower.rect.centerx) ** 2 + (y - tower.rect.centery) ** 2))
        if distance < target[0]:
            target[0] = distance
            target[1] = enemy
    if target[1]:
        return target[1]
def find_farthest_target(enemy_sprites, tower):
    pass
def find_all_targets(enemy_sprites, tower):
    target = []
    for enemy in enemy_sprites:
        x,y = enemy.rect.centerx, enemy.rect.centery
        distance = math.sqrt(abs((x - tower.rect.centerx) ** 2 + (y - tower.rect.centery) ** 2))
        if distance <= tower.attack_range:
            target.append(enemy)
    return target

class DwarfHunter(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,bullets):
        super(DwarfHunter,self).__init__()
        self.icon = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\icon\tower_0001.png')

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bullets = bullets

        self.timer = 0

        self.hover = False
        self.clicked = False

        self.name = "Dwarf Hunter"
        self.attack_range = 256      
        self.attack_speed = 1
        self.projectile_speed = 20
        self.damage = 1
        self.cost = 50

        self.lvl = 1
        self.xp = 0 
        self.xp_required = 100

        self.skill_point = 0
        self.skill_tree = {
            "skill_1":{"name":"attack speed","max_upgrades": 3,"current_upgrades": 0,"lvl_up": False,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\attack_speed.png"},
            "skill_2":{"name":"damage","max_upgrades": 3,"current_upgrades": 0,"lvl_up": False,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\attack_dmg.png"},
            "skill_3":{"name":"critical chance","max_upgrades": 3,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\attack_crit.png"},
            "skill_4":{"name":"frost","max_upgrades": 3,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\horror-acid-1.png"},
            "skill_5":{"name":"fire","max_upgrades": 3,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\horror-eerie-1.png"},
            "skill_6":{"name":"poison","max_upgrades": 3,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\horror-red-1.png"},
            "skill_7":{"name":"ricochet","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\lighting-acid-1.png"}, 
            "skill_8":{"name":"pierce","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\lighting-eerie-1.png"}, 
            "skill_9":{"name":"homing","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\lighting-fire-1.png"},
            "skill_10":{"name":"double arrows","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\needles-acid-1.png"},
            "skill_11":{"name":"split","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\needles-blue-1.png"},
            "skill_12":{"name":"multishot","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\needles-blue-1.png"}
            }

        self.tower_profile = TowerProfile(self)
        
        self.image = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\towerDefense_tile181.png')
        self.rect = self.image.get_rect(center=(pos_x,pos_y))

    def sprite_animation(self):
        pass

    def draw_range(self,screen):
        if self.hover:
            range_image = pygame.Surface((self.attack_range * 2,self.attack_range * 2), pygame.SRCALPHA)
            pygame.draw.circle(range_image, (58,58,58,30), (self.attack_range, self.attack_range), self.attack_range)
            screen.blit(range_image, (self.pos_x - self.attack_range, self.pos_y - self.attack_range))

    def level_up(self):
        if self.xp >= self.xp_required and self.lvl < 13:
            self.lvl += 1
            self.attack_speed -= 0.025
            self.damage += 0.55
            self.skill_point += 1
            self.xp = 0
            self.xp_required *= 1.5

    def attack(self,target):
        if not target == None:
            self.bullets.add(Arrow(self, target))

    def update(self,dt,enemy_sprites):
        # Handle talents
        if self.skill_tree['skill_1']['lvl_up']:
            self.attack_speed -= 0.25
            self.skill_tree['skill_1']['lvl_up'] = False
        if self.skill_tree['skill_2']['lvl_up']:
            self.damage += 1
            self.skill_tree['skill_2']['lvl_up'] = False
        # Shine when tower has skill points
        if self.skill_point > 0:
            pass
        # Cooldown between attacks(attack speed)
        self.timer += dt
        if self.timer / 1000 >= self.attack_speed:
            self.timer -= self.attack_speed * 1000
            target = find_nearest_target(enemy_sprites,self)
            self.attack(target)
        # Tower Levels
        self.level_up()

class DwarfSlayer(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,bullets):
        super(DwarfSlayer,self).__init__()

        self.icon = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0002\icon\tower_0002.png')

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bullets = bullets
        self.timer = 0

        self.hover = False
        self.clicked = False

        self.name = "Dwarf Slayer"
        self.attack_range = 128      
        self.attack_speed = 0.75
        self.projectile_speed = 20
        self.damage = 2
        self.cost = 75

        self.lvl = 1
        self.xp = 0 
        self.xp_required = 100

        self.skill_point = 0

        self.priority = None

        self.skill_tree = {
            "skill_1":{"name": "attack_speed","max_upgrades": 3,"current_upgrades": 0,"lvl_up": False,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\enchant-acid-1.png"}, "skill_2":{"name":"damage","max_upgrades": 3,"current_upgrades": 0,"lvl_up":False,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\enchant-blue-1.png"}, "skill_3":{"name":"critical chance","max_upgrades": 3,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\enchant-red-1.png"},
            "skill_4":{"name": "frost","max_upgrades": 3,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\horror-acid-1.png"}, "skill_5":{"name": "fire","max_upgrades": 3,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\horror-eerie-1.png"}, "skill_6":{"name":"poison","max_upgrades": 3,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\horror-red-1.png"},
            "skill_7":{"name": "ricochet","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\lighting-acid-1.png"}, "skill_8":{"name":"pierce","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\lighting-eerie-1.png"}, "skill_9":{"name":"homing","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\lighting-fire-1.png"},
            "skill_10":{"name": "double arrows","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\needles-acid-1.png"}, "skill_11":{"name":"split","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\needles-blue-1.png"}, "skill_12":{"name":"multishot","max_upgrades": 1,"current_upgrades": 0,"icon":r"D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\skill-icon\needles-blue-1.png"}
            }

        self.tower_profile = TowerProfile(self)
        self.image = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0002\towerDefense_tile180.png')
        self.rect = self.image.get_rect(center=(pos_x,pos_y))

    def draw_range(self,screen):
        if self.hover:
            range_image = pygame.Surface((self.attack_range * 2,self.attack_range * 2), pygame.SRCALPHA)
            pygame.draw.circle(range_image, (58,58,58,30), (self.attack_range, self.attack_range), self.attack_range)
            screen.blit(range_image, (self.pos_x - self.attack_range, self.pos_y - self.attack_range))

    def sprite_animation(self):
        pass

    def level_up(self):
        if self.xp >= self.xp_required:
            self.lvl += 1
            self.attack_speed -= 0.025
            self.damage += 0.55
            self.skill_point += 1
            self.xp = 0
            self.xp_required *= 1.5  

    def attack(self,target):
        if not target == None:
            self.bullets.add(Arrow(self, target))

    def update(self,dt,enemy_sprites):
        # Handle talents
        if self.skill_tree['skill_1']['lvl_up']:
            self.attack_speed -= 0.25
            self.skill_tree['skill_1']['lvl_up'] = False
        if self.skill_tree['skill_2']['lvl_up']:
            self.damage += 1
            self.skill_tree['skill_2']['lvl_up'] = False
        # Shine when tower has skill_points
        if self.skill_point > 0:
            pass        
        # Cooldown between attacks
        self.timer += dt
        if self.timer / 1000 >= self.attack_speed:
            self.timer -= self.attack_speed * 1000
            target = find_nearest_target(enemy_sprites,self)
            self.attack(target)
        # Tower Levels
        self.level_up()