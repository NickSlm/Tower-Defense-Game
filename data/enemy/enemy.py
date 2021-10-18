from sys import path
import pygame
import os

from pygame.image import load



def load_sprites(path):
    sprites = []
    for file_name in os.listdir(path):
        sprite = pygame.image.load(path + os.sep + file_name).convert_alpha()
        sprites.append(sprite)
    return sprites


class Enemy(pygame.sprite.Sprite):
    def __init__(self,checkpoints):
        super(Enemy,self).__init__()
        self.idle_sprites = load_sprites(path=r'D:\Games\Tower-Defense-Game\resources\sprites\enemies\0001\Idle')
        self.checkpoints = checkpoints
        self.current_sprite = 0
        self.image = self.idle_sprites[self.current_sprite]
        self.rect = self.image.get_rect(center=(self.checkpoints[0]))

    def sprite_animation(self):
        self.current_sprite += 0.2
        if int(self.current_sprite) >= len(self.idle_sprites):
            self.current_sprite = 0
            self.walk_animation = False
        self.image = self.idle_sprites[int(self.current_sprite)]

    def update(self):
        self.sprite_animation()
        
