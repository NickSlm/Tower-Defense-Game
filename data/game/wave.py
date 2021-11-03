import pygame
import json
from pygame import time
from data.enemy.enemy import Enemy, Enemy2, Enemy3

class Wave:
    ready = True
    def __init__(self,enemy_path, round):
        with open(r"D:\Games\Tower-Defense-Game\data\game\waves.json") as json_file:
            self.data = json.load(json_file)
        self.enemy_path = enemy_path
        self.round = round
        

