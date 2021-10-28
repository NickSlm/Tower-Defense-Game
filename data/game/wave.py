import pygame
import json
from pygame import time
from data.enemy.enemy import Enemy, Enemy2, Enemy3

class Wave:
    ready = True
    def __init__(self,enemy_path):
        with open(r"D:\Games\Tower-Defense-Game\data\game\waves.json") as json_file:
            self.data = json.load(json_file)
        self.enemy_path = enemy_path
        self.s = 0
    def generate_wave(self,round,wave):
        for enm in self.data[str(round)]:
            amount = self.data[str(round)][enm]
            for i in range(amount):
                if enm == 'red':
                    wave.append(Enemy(self.enemy_path))
                if enm == 'blue':
                    wave.append(Enemy2(self.enemy_path))
                if enm == 'green':
                    wave.append(Enemy3(self.enemy_path))
                amount -= 1
        return wave

