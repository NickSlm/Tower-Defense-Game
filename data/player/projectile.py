import pygame
import math

class Arrow(pygame.sprite.Sprite):
    arrow = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\projectiles\Arrow.png')
    arrow = pygame.transform.rotate(pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\sprites\projectiles\Arrow.png'),-90)
    def __init__(self,tower, target):
        super(Arrow,self).__init__()

        self.SPEED = tower.projectile_speed
        self.DAMAGE = tower.damage

        self.target = target

        x, y = pygame.Vector2(target.rect.center) - tower.rect.center
        self.angle = math.degrees(math.atan2(y,x))

        offset = pygame.Vector2(10,0).rotate(self.angle)
        self.pos = pygame.Vector2(tower.rect.center) + offset

        self.image = pygame.transform.rotate(self.arrow,-self.angle)

        self.rect = self.image.get_rect(center=self.pos)
        self.velocity = pygame.Vector2(self.SPEED,0)
        self.velocity.rotate_ip(self.angle)

        self.cooldown = False

    def sprite_animation(self):
        pass

    def update(self,dt):
        self.pos += self.velocity
        self.rect.center = self.pos
        
        if self.rect.top < 0 or self.rect.top > 1088:
            self.kill()


