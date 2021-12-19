from json import load
from os import stat
import pygame
import math

from pygame import image

from data.player.projectile import Arrow

FONT_COLOR = (0,0,0)



class TowerProfile:
    def __init__(self,screen,name,lvl,damage,attack_speed,skill_point,icon):
        font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",14)

        self.screen = screen
        self.name = name
        self.lvl = lvl
        self.damage = damage
        self.attack_speed = attack_speed
        self.skill_point = skill_point
        self.icon = icon

        self.profile_width = 224
        self.profile_height = 196
        icon_width,icon_height = self.icon.get_size()
        self.offset = 4

        self.icon_rect = icon.get_rect(topleft=(self.offset,self.offset))
        
        self.name_text = font.render(name, 1, FONT_COLOR)
        self.name_text_rect = self.name_text.get_rect(topleft = (((self.profile_width -(self.profile_width - icon_width - self.offset)) + (self.profile_width - icon_width - self.offset) // 2) - self.name_text.get_width() // 2,self.offset))

        self.lvl_text = font.render("Lvl: "+str(lvl), 1, FONT_COLOR)
        self.lvl_text_rect = self.lvl_text.get_rect(topleft = (icon_width + self.offset * 2, self.name_text.get_height() + self.offset))

        self.damage_text = font.render("Damage: "+str(damage), 1, FONT_COLOR)
        self.damage_text_rect = self.damage_text.get_rect(topleft = self.lvl_text_rect.bottomleft)

        self.attack_speed_text = font.render("AS: "+str(attack_speed // 500), 1, FONT_COLOR)
        self.attack_speed_text_rect = self.attack_speed_text.get_rect(topleft = self.damage_text_rect.bottomleft)

        self.skill_point_text = font.render("Skill Point: "+str(skill_point),1, FONT_COLOR)    
        self.skill_point_text_rect = self.skill_point_text.get_rect(topleft = (icon_width + self.offset * 2,(icon_height + self.offset) - self.skill_point_text.get_height()))        

        self.stats_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\tower_profile.png')
        self.stats_rect = self.stats_srf.get_rect(topleft=(((screen.get_width() // 2) - (self.stats_srf.get_width()// 2),screen.get_height() - self.stats_srf.get_height())))

        self.open_talents_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\open_talents.png')
        self.open_talents_rect = self.open_talents_srf.get_rect(topleft=(1072,screen.get_height() - self.stats_srf.get_height() + 83))
        # close_talents_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\close_talents.png')
        # close_talents_rect = close_talents_srf.get_rect(topleft=open_talents_rect.bottomleft)


    def create_tower_profile(self):
        stats_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\tower_profile.png')
        stats_rect = stats_srf.get_rect(topleft=(((self.screen.get_width() // 2) - (stats_srf.get_width()// 2),self.screen.get_height() - stats_srf.get_height())))
        
        stats_srf.blit(self.icon,self.icon_rect)
        stats_srf.blit(self.name_text, self.name_text_rect)
        # Stats border
        pygame.draw.rect(stats_srf,(0,0,0),[self.icon_width + self.offset + 2, self.name_text.get_height() + self.offset, (self.profile_width - self.icon_width - (self.offset * 2 + 2)), self.icon_height - self.name_text.get_height()],1)
        # Stats
        stats_srf.blit(self.lvl_text,self.lvl_text_rect)
        stats_srf.blit(self.damage_text,self.damage_text_rect)
        stats_srf.blit(self.attack_speed_text,self.attack_speed_text_rect)
        stats_srf.blit(self.skill_point_text,self.skill_point_text_rect)

        self.screen.blit(stats_srf,stats_rect)
        # If closed
        self.screen.blit(self.open_talents_srf,self.open_talents_rect)
        # If open
        # screen.blit(close_talents_srf,close_talents_rect)

def create_tower_profile(screen,name,lvl,damage,attack_speed,skill_point,icon):
    font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",14)

    profile_width = 224
    profile_height = 196
    icon_width,icon_height = icon.get_size()
    offset = 4

    icon_rect = icon.get_rect(topleft=(offset,offset))

    name_text = font.render(name, 1, FONT_COLOR)
    name_text_rect = name_text.get_rect(topleft = (((profile_width -(profile_width - icon_width - offset)) + (profile_width - icon_width - offset) // 2) - name_text.get_width() // 2,offset))

    lvl_text = font.render("Lvl: "+str(lvl), 1, FONT_COLOR)
    lvl_text_rect = lvl_text.get_rect(topleft = (icon_width + offset * 2, name_text.get_height() + offset))

    damage_text = font.render("Damage: "+str(damage), 1, FONT_COLOR)
    damage_text_rect = damage_text.get_rect(topleft = lvl_text_rect.bottomleft)

    attack_speed_text = font.render("AS: "+str(attack_speed), 1, FONT_COLOR)
    attack_speed_text_rect = attack_speed_text.get_rect(topleft = damage_text_rect.bottomleft)

    skill_point_text = font.render("Skill Point: "+str(skill_point),1, FONT_COLOR)    
    skill_point_text_rect = skill_point_text.get_rect(topleft = (icon_width + offset * 2,(icon_height + offset) - skill_point_text.get_height()))        

    stats_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\tower_profile.png')
    stats_rect = stats_srf.get_rect(topleft=(((screen.get_width() // 2) - (stats_srf.get_width()// 2),screen.get_height() - stats_srf.get_height())))

    open_talents_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\open_talents.png')
    open_talents_rect = open_talents_srf.get_rect(topleft=(1072,screen.get_height() - stats_srf.get_height() + 83))
    # close_talents_srf = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\close_talents.png')
    # close_talents_rect = close_talents_srf.get_rect(topleft=open_talents_rect.bottomleft)

    stats_srf.blit(icon,icon_rect)
    stats_srf.blit(name_text, name_text_rect)
    # Stats border
    pygame.draw.rect(stats_srf,(0,0,0),[icon_width + offset + 2, name_text.get_height() + offset, (profile_width - icon_width - (offset * 2 + 2)), icon_height - name_text.get_height()],1)
    # Stats
    stats_srf.blit(lvl_text,lvl_text_rect)
    stats_srf.blit(damage_text,damage_text_rect)
    stats_srf.blit(attack_speed_text,attack_speed_text_rect)
    stats_srf.blit(skill_point_text,skill_point_text_rect)

    screen.blit(stats_srf,stats_rect)
    # If closed
    screen.blit(open_talents_srf,open_talents_rect)
    # If open
    # screen.blit(close_talents_srf,close_talents_rect)

    return stats_rect

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
        self.font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",14)
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

        self.skill_tree = {"slow": 0,
        "fire": 0,
        "c": 1}
        
        self.stats_rect = None
        self.image = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\towerDefense_tile181.png')
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
            self.skill_point += 1
            self.xp = 0
            self.xp_required *= 1.5

    def attack(self,target):
        if not target == None:
            self.bullets.add(Arrow(self, target, self.projectile_speed, self.damage))

    def update(self,dt,enemy_sprites):
        # Cooldown between attacks
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
        self.attack_speed = 0.1
        self.projectile_speed = 20
        self.damage = 2
        self.cost = 75

        self.lvl = 1
        self.xp = 0 
        self.xp_required = 100

        self.skill_point = 0

        self.priority = None

        self.stats_rect = None
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
            self.skill_point += 1
            self.xp = 0
            self.xp_required *= 1.5  

    def attack(self,target):
        if not target == None:
            self.bullets.add(Arrow(self.rect.center, target, self.projectile_speed, self.damage))

    def update(self,dt,enemy_sprites):

        # Cooldown between attacks
        self.timer += dt
        if self.timer / 1000 >= self.attack_speed:
            self.timer -= self.attack_speed * 1000
            target = find_nearest_target(enemy_sprites,self)
            self.attack(target)
        
        # Tower Levels
        self.level_up()