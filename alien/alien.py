import pygame
import random

from pygame.sprite import Sprite

class Alien(Sprite):
    #表示单个外星人的类
    def __init__(self,ai_game):
        super().__init__()

        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.game_stats = ai_game.game_stats
        self.ai_game = ai_game

        self.image = pygame.image.load('./images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.last_change_velocity_time = 0.0

        self.velocity_factor_x = (random.random() - 0.5) * 2
        self.velocity_factor_y = random.random()

    def blitme(self):
        #在指定位置绘制外星人
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.game_stats.current_time > self.last_change_velocity_time + self.settings.alien_change_velocity_interval:
            self.velocity_factor_x = (random.random() - 0.5) * 2
            self.velocity_factor_y = random.random()
            self.last_change_velocity_time = self.game_stats.current_time

        self.y += self.settings.alien_speed_y_max * self.velocity_factor_y
        self.rect.y = self.y

        self.x += self.settings.alien_speed_x_max * self.velocity_factor_x
        self.rect.x = self.x

        if self.x < self.rect.width or self.settings.SCREEN_WIDTH - self.x < self.rect.width:
            self.velocity_factor_x *= -1