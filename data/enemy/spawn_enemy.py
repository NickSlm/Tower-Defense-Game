import pygame
import json
from data.enemy.enemy import Enemy, Enemy2, Enemy3,Enemy4

class EnemyWave:
    def __init__(self,enemy_path):
        self.enemy_path = enemy_path
        with open(r"D:\Games\Tower-Defense-Game\data\game\round.json") as json_file:
            self.data = json.load(json_file)
        self.enemy_index = 0
        self.enemy_summoned = 0
        self.enemy_summoned_total = 0
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_spawn = False

    def generate_enemies(self,round):

        enemy_type = self.data[str(round)]["enemy_order_type"][self.enemy_index]
        amount = self.data[str(round)]["enemy_amount"][self.enemy_index]

        if self.enemy_summoned < amount:
            if enemy_type == "red":
                if not pygame.sprite.spritecollideany(Enemy(self.enemy_path),self.enemy_sprites):
                    self.enemy_sprites.add(Enemy(self.enemy_path))
                    self.enemy_summoned_total += 1
                    self.enemy_summoned += 1

            if enemy_type == "blue":
                if not pygame.sprite.spritecollideany(Enemy2(self.enemy_path),self.enemy_sprites):
                    self.enemy_sprites.add(Enemy2(self.enemy_path))
                    self.enemy_summoned_total += 1
                    self.enemy_summoned += 1

            if enemy_type == "green":
                if not pygame.sprite.spritecollideany(Enemy3(self.enemy_path),self.enemy_sprites):
                    self.enemy_sprites.add(Enemy3(self.enemy_path))
                    self.enemy_summoned_total += 1
                    self.enemy_summoned += 1

            if enemy_type == "black":
                if not pygame.sprite.spritecollideany(Enemy4(self.enemy_path),self.enemy_sprites):
                    self.enemy_sprites.add(Enemy4(self.enemy_path))
                    self.enemy_summoned_total += 1
                    self.enemy_summoned += 1

        if self.enemy_summoned == amount:
            self.enemy_summoned = 0 
            self.enemy_index +=1

        if self.enemy_summoned_total == sum(self.data[str(round)]["enemy_amount"]):
            self.enemy_summoned_total = 0
            self.enemy_index = 0
            self.enemy_spawn = False
