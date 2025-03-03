import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #管理子弹的类
    def __init__(self, ai_game):
        super().__init__()

        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats
        self.ai_game = ai_game
        self.screen = ai_game.screen

        self.color=self.settings.bullet_color

        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop

        self.y=float(self.rect.y)

    def update(self):
        #子弹移动
        self.y-=self.settings.bullet_speed
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)