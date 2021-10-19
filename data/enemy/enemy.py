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
        # self.idle_sprites = load_sprites(path=r'D:\Games\Tower-Defense-Game\resources\sprites\enemies\0001\Idle')
        self.checkpoints = checkpoints
        self.current_sprite = 0
        self.image = pygame.Surface((32,48))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=(self.checkpoints[0]))
        print(self.rect)
        # self.image = self.idle_sprites[self.current_sprite]
        # self.rect = self.image.get_rect(center=(self.checkpoints[1]))

    # def sprite_animation(self):
    #     self.current_sprite += 0.2
    #     if int(self.current_sprite) >= len(self.idle_sprites):
    #         self.current_sprite = 0
    #     self.image = self.idle_sprites[int(self.current_sprite)]

    def movement(self):
        pass

    def update(self):
        self.speed = 2
        if self.rect.x < self.checkpoints[0][0]:
            print("walking right")
            self.rect.x += self.speed
        if self.rect.x > self.checkpoints[0][0]:
            print("walking left")
            self.rect.x -= self.speed
        if self.rect.y < self.checkpoints[0][1]:
            print("walking down")
            self.rect.y += self.speed
        if self.rect.y > self.checkpoints[0][1]:
            print("walking up")
            self.rect.y -= self.speed
        current_point = ((self.rect.x - self.checkpoints[0][0]),(self.rect.y - self.checkpoints[0][1]))
        if (current_point[0] / self.speed, current_point[1] / self.speed) == (0,0):
            self.checkpoints = self.checkpoints[1:]
        
        # self.sprite_animation()