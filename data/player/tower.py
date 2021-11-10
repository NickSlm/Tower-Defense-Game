import pygame
import math

class Tower(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super(Tower,self).__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.range = 128

        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(center=(pos_x,pos_y))

    def sprite_animation(self):
        pass

    def find_target(self,enemy_sprites):
        for enemy in enemy_sprites:
            x,y = enemy.rect.centerx, enemy.rect.centery
            distance = math.sqrt(abs((x - self.rect.centerx) ** 2 + (y - self.rect.centery) ** 2))
            if distance < self.range:
                enemy.hp -= 1
    def update(self):
        pass