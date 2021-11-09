import pygame




class Player:
    def __init__(self,screen):
        self.screen = screen
        self.health = 100
        self.money = 250
        self.health_icon = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\heart.png')
        self.money_icon = pygame.image.load(r'D:\Games\Tower-Defense-Game\resources\game\gold-ingots.png')
        # Fonts
        self.font = pygame.font.Font(r"D:\Games\Tower-Defense-Game\resources\fonts\IMMORTAL.ttf",24)

    def draw_player_resources(self,round):
        self.health_text = self.font.render("Health: "+str(self.health), 1, (0,0,0))
        self.money_text = self.font.render("Money: "+str(self.money), 1, (0,0,0))
        self.round_text = self.font.render("Round: "+str(round), 1, (0,0,0))
        self.screen.blit(self.health_text,(10,10))
        self.screen.blit(self.health_icon,(10 + self.health_text.get_width(),10))
        self.screen.blit(self.money_text,(10,40))
        self.screen.blit(self.money_icon,(10 + self.money_text.get_width(),40))
        self.screen.blit(self.round_text,(960 - (self.round_text.get_width()// 2),10))


