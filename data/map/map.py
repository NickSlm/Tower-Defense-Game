import pygame
import pytmx

class Map:
    def __init__(self,screen):
        self.screen = screen
        self.map = pytmx.load_pygame(r"D:\Games\TD\resources\maps\map_1.tmx")
        
    def blockers(self):
        blockers = pygame.sprite.Group()
        for obj in self.map.objects:
            if obj.name == "block":
                x = obj.x
                y = obj.y
                width = obj.width
                height = obj.height
                blocker = pygame.sprite.Sprite()
                blocker.rect = pygame.Rect(x,y,width,height)
                blockers.add(blocker)
        return blockers

    def checkpoints(self):
        checkpoints = []
        for obj in self.map.objects:
            if obj.name == "point":
                x = obj.x
                y = obj.y
                checkpoints.append((x,y))
        return checkpoints

    def generate_map(self):
        for layer in self.map.visible_layers:
            for x,y,gid in layer:
                tile = self.map.get_tile_image_by_gid(gid)
                self.screen.blit(tile,(x * self.map.tilewidth, y * self.map.tileheight))
    