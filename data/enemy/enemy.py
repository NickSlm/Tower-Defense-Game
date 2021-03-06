from sys import path
import pygame
import os
from pygame.image import load


def load_sprites(path):
    sprites_left = []
    sprites_right = []
    for file_name in os.listdir(path):
        sprite_left = pygame.image.load(path + os.sep + file_name).convert_alpha()
        sprite_right = pygame.transform.flip(sprite_left,True,False)
        sprites_right.append(sprite_right)
        sprites_left.append(sprite_left)
    return sprites_left,sprites_right

class Enemy(pygame.sprite.Sprite):
    def __init__(self,checkpoints):
        super(Enemy,self).__init__()
        self.checkpoints = checkpoints

        self.walk_left,self.walk_right = load_sprites(r'D:\Games\Tower-Defense-Game\resources\sprites\enemies\0001\walk')
        self.hp = 1
        self.damage = 1
        self.speed = 2
        self.money = 2
        self.xp = 1

        self.direction = None

        self.current_sprite = 0
        
        self.image = self.walk_right[self.current_sprite]
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect = self.image.get_rect(center=(self.checkpoints[0][0],self.checkpoints[0][1] - (self.height //3)))
        
    def sprite_animation(self,state):
        self.current_sprite += 0.2
        if state == "right":
            if int(self.current_sprite) >= len(self.walk_right):
                self.current_sprite = 0
            self.image = self.walk_right[int(self.current_sprite)]
        if state == "left":
            if int(self.current_sprite) >= len(self.walk_left):
                self.current_sprite = 0
            self.image = self.walk_left[int(self.current_sprite)]
        if state == "top":
            pass
        if state == "down":
            pass           

    def update(self):
        if self.checkpoints:
            current_point = ((self.rect.centerx - self.checkpoints[0][0]),(self.rect.centery - (self.checkpoints[0][1] - (self.height //3))))
            if self.rect.centerx < self.checkpoints[0][0]:
                self.direction = "right"
                self.sprite_animation("right")
                self.rect.centerx += self.speed
            if self.rect.centerx > self.checkpoints[0][0]:
                self.direction = "left"
                self.sprite_animation("left")
                self.rect.centerx -= self.speed
            if self.rect.centery < self.checkpoints[0][1] - (self.height // 3):
                self.direction = "down"
                self.sprite_animation("down")
                self.rect.centery += self.speed
            if self.rect.centery > self.checkpoints[0][1] - (self.height // 3):
                self.direction = "top"
                self.sprite_animation("top")
                self.rect.centery -= self.speed
            if (current_point[0] // self.speed, current_point[1] // self.speed) == (0,0):
                self.checkpoints = self.checkpoints[1:]
        else:
            self.kill()
            return True
        return False


class Enemy2(pygame.sprite.Sprite):
    def __init__(self,checkpoints):
        super(Enemy2,self).__init__()
        self.checkpoints = checkpoints

        self.walk_left,self.walk_right = load_sprites(r'D:\Games\Tower-Defense-Game\resources\sprites\enemies\0002\walk')
        self.hp = 5
        self.damage = 10
        self.speed = 2
        self.money = 6
        self.xp = 2

        self.current_sprite = 0
        self.image = self.walk_right[self.current_sprite]
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect = self.image.get_rect(center=(self.checkpoints[0][0],self.checkpoints[0][1] - (self.height //3)))

    def sprite_animation(self,state):
        self.current_sprite += 0.2
        if state == "right":
            if int(self.current_sprite) >= len(self.walk_right):
                self.current_sprite = 0
            self.image = self.walk_right[int(self.current_sprite)]
        if state == "left":
            if int(self.current_sprite) >= len(self.walk_left):
                self.current_sprite = 0
            self.image = self.walk_left[int(self.current_sprite)]    
        
    def update(self):
        if self.checkpoints:
            current_point = ((self.rect.centerx - self.checkpoints[0][0]),(self.rect.centery - (self.checkpoints[0][1] - (self.height //3))))
            if self.rect.centerx < self.checkpoints[0][0]:
                self.direction = "right"
                self.sprite_animation("right")
                self.rect.centerx += self.speed
            if self.rect.centerx > self.checkpoints[0][0]:
                self.direction = "left"
                self.sprite_animation("left")
                self.rect.centerx -= self.speed
            if self.rect.centery < self.checkpoints[0][1] - (self.height // 3):
                self.direction = "down"
                self.sprite_animation("down")
                self.rect.centery += self.speed
            if self.rect.centery > self.checkpoints[0][1] - (self.height // 3):
                self.direction = "top"
                self.sprite_animation("top")
                self.rect.centery -= self.speed
            if (current_point[0] // self.speed, current_point[1] // self.speed) == (0,0):
                self.checkpoints = self.checkpoints[1:]
        else:
            self.kill()
            return True
        return False

class Enemy3(pygame.sprite.Sprite):
    def __init__(self,checkpoints):
        super(Enemy3,self).__init__()
        self.checkpoints = checkpoints

        self.walk_left,self.walk_right = load_sprites(r'D:\Games\Tower-Defense-Game\resources\sprites\enemies\0003\walk')
        self.hp = 4
        self.damage = 4
        self.speed = 4
        self.money = 8
        self.xp = 4

        self.current_sprite = 0

        self.image = self.walk_right[self.current_sprite]
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect = self.image.get_rect(center=(self.checkpoints[0][0],self.checkpoints[0][1] - (self.image.get_height() // 3)))

    def sprite_animation(self,state):
        self.current_sprite += 0.2
        if state == "right":
            if int(self.current_sprite) >= len(self.walk_right):
                self.current_sprite = 0
            self.image = self.walk_right[int(self.current_sprite)]
        if state == "left":
            if int(self.current_sprite) >= len(self.walk_left):
                self.current_sprite = 0
            self.image = self.walk_left[int(self.current_sprite)]    

    def update(self):
        if self.checkpoints:
            current_point = ((self.rect.centerx - self.checkpoints[0][0]),(self.rect.centery - (self.checkpoints[0][1] - (self.height //3))))
            if self.rect.centerx < self.checkpoints[0][0]:
                self.direction = "right"
                self.sprite_animation("right")
                self.rect.centerx += self.speed
            if self.rect.centerx > self.checkpoints[0][0]:
                self.direction = "left"
                self.sprite_animation("left")
                self.rect.centerx -= self.speed
            if self.rect.centery < self.checkpoints[0][1] - (self.height // 3):
                self.direction = "down"
                self.sprite_animation("down")
                self.rect.centery += self.speed
            if self.rect.centery > self.checkpoints[0][1] - (self.height // 3):
                self.direction = "top"
                self.sprite_animation("top")
                self.rect.centery -= self.speed
            if (current_point[0] // self.speed, current_point[1] // self.speed) == (0,0):
                self.checkpoints = self.checkpoints[1:]
        else:
            self.kill()
            return True
        return False

class Enemy4(pygame.sprite.Sprite):
    def __init__(self,checkpoints):
        super(Enemy4,self).__init__()
        self.checkpoints = checkpoints

        self.walk_left,self.walk_right = load_sprites(r'D:\Games\Tower-Defense-Game\resources\sprites\enemies\0004\walk')
        self.hp = 15
        self.damage = 10
        self.speed = 2
        self.money = 16
        self.xp = 8
        self.type = None

        self.current_sprite = 0

        self.image = self.walk_right[self.current_sprite]
        self.rect = self.image.get_rect(center=(self.checkpoints[0][0],self.checkpoints[0][1] - (self.image.get_height() // 3)))

        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def sprite_animation(self,state):
        self.current_sprite += 0.2
        if state == "right":
            if int(self.current_sprite) >= len(self.walk_right):
                self.current_sprite = 0
            self.image = self.walk_right[int(self.current_sprite)]
        if state == "left":
            if int(self.current_sprite) >= len(self.walk_left):
                self.current_sprite = 0
            self.image = self.walk_left[int(self.current_sprite)]    

    def update(self):
        if self.checkpoints:
            current_point = ((self.rect.centerx - self.checkpoints[0][0]),(self.rect.centery - (self.checkpoints[0][1] - (self.height //3))))
            if self.rect.centerx < self.checkpoints[0][0]:
                self.direction = "right"
                self.sprite_animation("right")
                self.rect.centerx += self.speed
            if self.rect.centerx > self.checkpoints[0][0]:
                self.direction = "left"
                self.sprite_animation("left")
                self.rect.centerx -= self.speed
            if self.rect.centery < self.checkpoints[0][1] - (self.height // 3):
                self.direction = "down"
                self.sprite_animation("down")
                self.rect.centery += self.speed
            if self.rect.centery > self.checkpoints[0][1] - (self.height // 3):
                self.direction = "top"
                self.sprite_animation("top")
                self.rect.centery -= self.speed
            if (current_point[0] // self.speed, current_point[1] // self.speed) == (0,0):
                self.checkpoints = self.checkpoints[1:]
        else:
            self.kill()
            return True
        return False