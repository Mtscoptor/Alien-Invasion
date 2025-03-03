import pygame
import random

from settings import Settings
from player.ship import Ship
from player.attack_system import AttackSystem
from alien.alien_system import AlienSystem
from input_system import InputSystem
from player.ability_system import AbilitySystem
from game_stats import GameStats
from ui.ui_system import UISystem

class AlienInvasion:
    #管理游戏资源和行为的类
    def __init__(self):
        #初始化游戏并创建游戏资源
        pygame.init()

        pygame.display.set_caption('Alien Invasion')

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))

        self.game_stats = GameStats(self)

        self.ship = Ship(self)

        self.ability_system = AbilitySystem(self)

        self.alien_system = AlienSystem(self)
        self.aliens = self.alien_system.aliens

        self.attack_system = AttackSystem(self)
        self.bullets = self.attack_system.bullets

        self.ui_system = UISystem(self)

        self.input_system = InputSystem(self)

    def run_game(self):
        #主循环
        while True:
            self.input_system.check_events()

            if self.game_stats.game_active:
                self.data_total_update()
                self.ability_system.stop_abilities()
                self.attack_system.update_bullets()
                self.alien_system.update_aliens()

            self._update_screen()



    def data_total_update(self):
        self.game_stats.run_time()
        self.game_stats.update()
        self.alien_system.update_aliens()
        self.ship.update()

    def _update_screen(self):
        # 每次循环重绘屏幕
        self.screen.fill(self.settings.BACKGROUND_COLOR)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens:
            alien.blitme()

        #打印Play按钮
        self.ui_system.draw_play_button()

        #更新UI界面信息
        self.ui_system.update()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def random_bool(self,probability):
        return True if random.random() < probability else False


if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()