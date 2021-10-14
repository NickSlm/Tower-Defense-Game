import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self,checkpoints):
        super(Enemy,self).__init__()
        self.speed = 10

        self.checkpoints = checkpoints
        self.image = pygame.Surface((32,48))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center=(self.checkpoints[0]))



    def update(self):
        for checkpoint in self.checkpoints:
            print(checkpoint)
        


