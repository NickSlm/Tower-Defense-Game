from json import load
import pygame
import math

from pygame import image

FONT_COLOR = (255,255,255)



def create_tower_profile(screen,name,lvl,damage,attack_speed,skill_point,icon):
    font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",14)

    profile_width = 224
    profile_height = 196
    icon_width,icon_height = icon.get_size()
    offset = 2

    name_text = font.render(name, 1, FONT_COLOR)
    lvl_text = font.render("Lvl: "+str(lvl), 1, (0,0,0))
    damage_text = font.render("Damage: "+str(damage), 1, (0,0,0))
    attack_speed_text = font.render("Attack Speed: "+str(attack_speed // 500), 1, (0,0,0))
    skill_point_text = font.render("Skill Point: "+str(skill_point),1, (0,0,0))            

    stats_srf = pygame.Surface((profile_width,profile_height),pygame.SRCALPHA)
    stats_srf.fill((58,58,58,226))
    stats_srf.blit(icon,(0,0))
    stats_srf.blit(name_text,(((icon_width + ((profile_width - icon_width) // 2) ) - (name_text.get_width() // 2),0)))

    # Stats border
    pygame.draw.rect(stats_srf,(0,0,0),[icon_width + offset, name_text.get_height(), (profile_width - icon_width - (offset * 2)), icon_height - name_text.get_height()],1)
    # Stats
    stats_srf.blit(lvl_text,(icon_width + offset * 2, name_text.get_height()))
    stats_srf.blit(damage_text,(icon_width + offset * 2, name_text.get_height() + lvl_text.get_height()))
    stats_srf.blit(attack_speed_text,(icon_width + offset * 2, name_text.get_height() + lvl_text.get_height() + damage_text.get_height()))
    stats_srf.blit(skill_point_text,(icon_width + offset * 2, icon_height - skill_point_text.get_height()))
    # Description border
    pygame.draw.rect(stats_srf,(0,0,0),[offset, icon_height + offset, profile_width - offset * 2, profile_height - icon_height - offset],1)
    screen.blit(stats_srf,((960 - (stats_srf.get_width()// 2),1088 - stats_srf.get_height())))


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

class Arrow(pygame.sprite.Sprite):
    arrow = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\projectiles\towerDefense_tile251.png')
    arrow = pygame.transform.rotate(pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\projectiles\towerDefense_tile251.png'),-90)
    def __init__(self,tower_pos, target, attack_speed, damage):
        super(Arrow,self).__init__()

        self.SPEED = attack_speed
        self.DAMAGE = damage

        self.target = target

        x, y = pygame.Vector2(target.rect.center) - tower_pos
        self.angle = math.degrees(math.atan2(y,x))

        offset = pygame.Vector2(10,0).rotate(self.angle)
        self.pos = pygame.Vector2(tower_pos) + offset

        self.image = pygame.transform.rotate(self.arrow,-self.angle)

        self.rect = self.image.get_rect(center=self.pos)
        self.velocity = pygame.Vector2(self.SPEED,0)
        self.velocity.rotate_ip(self.angle)

    def sprite_animation(self):
        pass

    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos
        
        if self.rect.top < 0 or self.rect.top > 1088:
            self.kill()


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
        self.attack_speed = 500
        self.projectile_speed = 10
        self.damage = 1
        self.cost = 50

        self.lvl = 1
        self.xp = 0 
        self.xp_required = 100

        self.skill_point = 0
        
        self.image = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0001\towerDefense_tile181.png')
        self.rect = self.image.get_rect(center=(pos_x,pos_y))

    def draw_range(self,screen):
        if self.hover:
            range_image = pygame.Surface((self.attack_range * 2,self.attack_range * 2), pygame.SRCALPHA)
            pygame.draw.circle(range_image, (58,58,58,30), (self.attack_range, self.attack_range), self.attack_range)
            screen.blit(range_image, (self.pos_x - self.attack_range, self.pos_y - self.attack_range))

    def draw_stats(self,screen):
        if self.clicked:
            create_tower_profile(screen,self.name,self.lvl,self.damage,self.attack_speed,self.skill_point,self.icon)
            talents_srf = pygame.Surface((264,132),pygame.SRCALPHA)
            talents_srf.fill((0,0,0,128))
            self.talents_rect = talents_srf.get_rect(center= (960 + 112,1088- talents_srf.get_height()))
            screen.blit(talents_srf,(960 + 112,1088- talents_srf.get_height()))
            
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
        # Show attack range on hover
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False


        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.clicked = True

        
        # Level up tower skills

        # Cooldown between attacks
        self.timer += dt
        if self.timer   >= self.attack_speed:
            self.timer -= self.attack_speed
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
        self.attack_speed = 1000
        self.projectile_speed = 20
        self.damage = 2
        self.cost = 75

        self.lvl = 1
        self.xp = 0 
        self.xp_required = 100

        self.skill_point = 0

        self.priority = None
        
        self.image = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\towers\tower_0002\towerDefense_tile180.png')
        self.rect = self.image.get_rect(center=(pos_x,pos_y))

    def draw_range(self,screen):
        if self.hover:
            range_image = pygame.Surface((self.attack_range * 2,self.attack_range * 2), pygame.SRCALPHA)
            pygame.draw.circle(range_image, (58,58,58,30), (self.attack_range, self.attack_range), self.attack_range)
            screen.blit(range_image, (self.pos_x - self.attack_range, self.pos_y - self.attack_range))

    def draw_stats(self,screen):
        if self.clicked:
            create_tower_profile(screen,self.name,self.lvl,self.damage,self.attack_speed,self.skill_point,self.icon)

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
        # Show attack range on hover
        # if self.rect.collidepoint(pygame.mouse.get_pos()):
        #     self.hover = True
        # else:
        #     self.hover = False
        #     if pygame.mouse.get_pressed()[0]:
        #         self.clicked = False

        # if pygame.mouse.get_pressed()[0]:
        #     if self.rect.collidepoint(pygame.mouse.get_pos()):
        #         self.clicked = True
        #     if not self.rect.collidepoint(pygame.mouse.get_pos()) or not self.


        

        # Level up tower skills

        # Cooldown between attacks
        self.timer += dt
        if self.timer   >= self.attack_speed:
            self.timer -= self.attack_speed
            target = find_nearest_target(enemy_sprites,self)
            self.attack(target)
        
        # Tower Levels
        self.level_up()