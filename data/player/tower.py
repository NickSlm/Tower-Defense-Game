import pygame
import math




class Bullet(pygame.sprite.Sprite):
    def __init__(self,tower_pos,target, angle):
        super(Bullet,self).__init__()

        self.SPEED = 10

        offset = pygame.Vector2(10,0).rotate(angle)
        self.pos = pygame.Vector2(tower_pos) + offset

        self.tower_angle = angle

        self.target = target


        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect(center=self.pos)

        self.velocity = pygame.Vector2(10,0)
        self.velocity.rotate_ip(self.tower_angle)


    def update(self):
        self.pos += self.velocity
        self.rect.center = self.pos



class Tower(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,bullets):
        super(Tower,self).__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bullets = bullets


        self.timer = 0

        self.hover = False

        self.attack_range = 256      
        self.attack_cooldown = 1000
        self.damage = 1
        self.cost = 50

        self.lvl = 1
        self.experience = 0 

        self.priority = None
        
        self.angle = 0
        self.image = pygame.Surface((64,64))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=(pos_x,pos_y))

    def draw_range(self,screen):
        if self.hover:
            range_image = pygame.Surface((self.attack_range * 2,self.attack_range * 2), pygame.SRCALPHA)
            pygame.draw.circle(range_image, (58,58,58,30), (self.attack_range, self.attack_range), self.attack_range)
            screen.blit(range_image, (self.pos_x - self.attack_range, self.pos_y - self.attack_range))

    def sprite_animation(self):
        pass

    def level_up(self):
        pass

    def find_nearest_target(self,enemy_sprites):
        target = [self.attack_range,None]
        for enemy in enemy_sprites:
            x,y = enemy.rect.centerx, enemy.rect.centery
            distance = math.sqrt(abs((x - self.rect.centerx) ** 2 + (y - self.rect.centery) ** 2))
            if distance < target[0]:
                target[0] = distance
                target[1] = enemy
        if target[1]:
            return target[1]

    def shoot(self,target):
        if not target == None:
            x, y = pygame.Vector2(target.rect.center) - self.rect.center
            self.angle = math.degrees(math.atan2(y,x))
            self.bullets.add(Bullet((self.rect.centerx,self.rect.centery),target, self.angle))
 
    def update(self,dt,enemy_sprites):
        """
        """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False

        self.timer += dt
        if self.timer   >= self.attack_cooldown:
            self.timer -= self.attack_cooldown
            target = self.find_nearest_target(enemy_sprites)
            self.shoot(target)
                    
