import pygame
import math

class Projectile(pygame.sprite.Sprite):
    def __init__(self,tower_pos, target, attack_speed, damage):
        super(Projectile,self).__init__()

        self.SPEED = attack_speed
        self.DAMAGE = damage

        self.target = target

        x, y = pygame.Vector2(target.rect.center) - tower_pos
        self.angle = math.degrees(math.atan2(y,x))

        offset = pygame.Vector2(10,0).rotate(self.angle)
        self.pos = pygame.Vector2(tower_pos) + offset

        self.image = pygame.Surface((16,16))
        self.image.fill((58,58,58))
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

class HomingProjectile(pygame.sprite.Sprite):
    def __init__(self):
        super(HomingProjectile,self).__init__()
        pass

class Tower(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,bullets):
        super(Tower,self).__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.bullets = bullets

        self.timer = 0

        self.hover = False
        self.clicked = False

        self.attack_range = 256      
        self.attack_cooldown = 500
        self.attack_speed = 15
        self.damage = 1
        self.cost = 50

        self.lvl = 1
        self.xp = 0 
        self.xp_required = 100

        self.skill_point = 0

        self.priority = None
        
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
        if self.xp >= self.xp_required:
            self.lvl += 1
            self.skill_point += 1
            self.xp = 0
            self.xp_required *= 1.5  

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
            self.bullets.add(Projectile(self.rect.center, target, self.attack_speed, self.damage))
 
    def update(self,dt,enemy_sprites):
        # Show attack range on hover
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False

        # Cooldown between attacks
        self.timer += dt
        if self.timer   >= self.attack_cooldown:
            self.timer -= self.attack_cooldown
            target = self.find_nearest_target(enemy_sprites)
            self.shoot(target)
        
        # Tower Levels
        self.level_up()
                    
