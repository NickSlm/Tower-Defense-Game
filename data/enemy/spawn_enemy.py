import pygame
import json


class EnemyWave:
    def __init__(self):
        with open(r"D:\Games\Tower-Defense-Game\data\game\round.json") as json_file:
            self.data = json.load(json_file)
        self.enemy_index = 0
        self.enemy_summoned = 0
        self.enemy_sprites = pygame.sprite.Group()

    def g(self):
        self.a += 1
        print(self.a)