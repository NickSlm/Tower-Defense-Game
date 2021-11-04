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

        self.height = 48
        self.width = 32

        self.hp = 1
        self.damage = 1
        self.speed = 4
        self.money = 5

        self.current_sprite = 0
        self.image = pygame.Surface((32,48))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=(self.checkpoints[0][0],self.checkpoints[0][1] - (self.height /2)))
        # self.image = self.idle_sprites[self.current_sprite]
        # self.rect = self.image.get_rect(center=(self.checkpoints[1]))

    # def sprite_animation(self):
    #     self.current_sprite += 0.2
    #     if int(self.current_sprite) >= len(self.idle_sprites):
    #         self.current_sprite = 0
    #     self.image = self.idle_sprites[int(self.current_sprite)]

    def update(self):
        if self.checkpoints:
            current_point = ((self.rect.centerx - self.checkpoints[0][0]),(self.rect.centery - (self.checkpoints[0][1] - (self.height /2))))
            if self.rect.centerx < self.checkpoints[0][0]:
                self.rect.centerx += self.speed
            if self.rect.centerx > self.checkpoints[0][0]:
                self.rect.centerx -= self.speed
            if self.rect.centery < self.checkpoints[0][1] - (self.height /2):
                self.rect.centery += self.speed
            if self.rect.centery > self.checkpoints[0][1] - (self.height /2):
                self.rect.centery -= self.speed
            if (current_point[0] // self.speed, current_point[1] // self.speed) == (0,0):
                self.checkpoints = self.checkpoints[1:]
        else:
            self.kill()
            return True

        if self.hp <= 0:
            self.kill()

        return False


class Enemy2(pygame.sprite.Sprite):
    def __init__(self,checkpoints):
        super(Enemy2,self).__init__()
        self.checkpoints = checkpoints

        self.height = 64
        self.width = 64

        self.hp = 10
        self.damage = 10
        self.speed = 2
        self.money = 10

        self.current_sprite = 0
        self.image = pygame.Surface((64,64))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect(center=(self.checkpoints[0][0],self.checkpoints[0][1] - (self.height /2)))

    def update(self):
        if self.checkpoints:
            current_point = ((self.rect.centerx - self.checkpoints[0][0]),(self.rect.centery - (self.checkpoints[0][1] - (self.height /2))))
            if self.rect.centerx < self.checkpoints[0][0]:
                self.rect.centerx += self.speed
            if self.rect.centerx > self.checkpoints[0][0]:
                self.rect.centerx -= self.speed
            if self.rect.centery < self.checkpoints[0][1] - (self.height /2):
                self.rect.centery += self.speed
            if self.rect.centery > self.checkpoints[0][1] - (self.height /2):
                self.rect.centery -= self.speed
            if (current_point[0] // self.speed, current_point[1] // self.speed) == (0,0):
                self.checkpoints = self.checkpoints[1:]
        else:
            self.kill()
            return True

        if self.hp <= 0:
            self.kill()
            
        return False

class Enemy3(pygame.sprite.Sprite):
    def __init__(self,checkpoints):
        super(Enemy3,self).__init__()
        self.checkpoints = checkpoints

        self.height = 48
        self.width = 32

        self.hp = 4
        self.damage = 4
        self.speed = 8
        self.money = 20

        self.current_sprite = 0
        self.image = pygame.Surface((32,48))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(center=(self.checkpoints[0][0],self.checkpoints[0][1] - (self.height /2)))

    def update(self):
        if self.checkpoints:
            current_point = ((self.rect.centerx - self.checkpoints[0][0]),(self.rect.centery - (self.checkpoints[0][1] - (self.height /2))))
            if self.rect.centerx < self.checkpoints[0][0]:
                self.rect.centerx += self.speed
            if self.rect.centerx > self.checkpoints[0][0]:
                self.rect.centerx -= self.speed
            if self.rect.centery < self.checkpoints[0][1] - (self.height /2):
                self.rect.centery += self.speed
            if self.rect.centery > self.checkpoints[0][1] - (self.height /2):
                self.rect.centery -= self.speed
            if (current_point[0] // self.speed, current_point[1] // self.speed) == (0,0):
                self.checkpoints = self.checkpoints[1:]
        else:
            self.kill()
            return True

        if self.hp <= 0:
            self.kill()

        return False

