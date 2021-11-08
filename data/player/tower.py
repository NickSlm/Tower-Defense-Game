import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super(Tower,self).__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = pygame.Surface((64,64))
        self.image.fill((255,0,0))
        
        

        self.rect = self.image.get_rect(center=(pos_x,pos_y))

    def update(self):
        pass