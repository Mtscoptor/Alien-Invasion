import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    #管理飞船的类
    def __init__(self,ai_game):
        #初始化飞船并设置初始位置
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()

        #将新飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #移动方向
        self.move_dir = [0,0]

    def update(self):
        if self.move_dir[0] == 1 and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_x
        if self.move_dir[0] == -1 and self.rect.left > 0:
            self.x -= self.settings.ship_speed_x
        if self.move_dir[1] == 1 and self.rect.top > 0:
            self.y -= self.settings.ship_speed_y
        if self.move_dir[1] == -1 and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed_y

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)