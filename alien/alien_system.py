import pygame

from alien.alien import Alien
from time import sleep

from settings import Settings


class AlienSystem:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.game_stats = ai_game.game_stats
        self.ability_system = ai_game.ability_system
        self.ship = ai_game.ship

        self.aliens = pygame.sprite.Group()

        self.alien_number_rows = 1
        self.alien_last_cycle_time = 0.0
        self.alien_create_interval = self.settings.alien_create_interval
        self.first_cycle = False

    def create_fleet(self):
        #创建外星人群
        alien = Alien(self.ai_game)

        #计算每行最多几个外星人
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.SCREEN_WIDTH - alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        #创建外星人群
        for row_number in range(self.alien_number_rows):
            for alien_number in range(number_aliens_x):
                alien_create_probability = ((self.settings.alien_original_create_probability +
                                (self.alien_number_rows - 1 - row_number) *
                                self.settings.alien_create_probability_increase_by_row_increase) *
                               (1 + self.settings.alien_create_probability_increase_by_cycle_increase *
                                self.game_stats.alien_cycle))
                alien_create_probability = min(alien_create_probability,1)
                self.create_alien(number_aliens_x - 1 - alien_number, row_number,
                          self.ai_game.random_bool(alien_create_probability))

    def create_alien(self, alien_number, row_number, alien_probability):
        # 创建一个外星人并加入当前行
        if alien_probability:
            alien = Alien(self.ai_game)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width * 1.5 + 2 * alien_width * alien_number
            alien.y = alien_height + 2 * alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            self.aliens.add(alien)

    def update_aliens(self):
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

        self.check_aliens_bottom()

        if (self.game_stats.current_time > self.alien_last_cycle_time + self.alien_create_interval or
                not self.first_cycle):
            if not self.first_cycle:
                self.first_cycle = True
            self.create_fleet()
            self.alien_last_cycle_time = self.game_stats.current_time
            self.game_stats.alien_cycle += 1
            self.ai_game.ui_system.scoreboard.prep_alien_cycle()
            if self.alien_number_rows <= self.settings.alien_number_rows_max:
                self.alien_number_rows = self.game_stats.alien_cycle // 5 + 1

    def ship_hit(self):
        self.game_stats.ships_left -= 1
        self.ai_game.ui_system.scoreboard.prep_ships()

        if self.game_stats.ships_left > 0:
            self.aliens.empty()
            self.ability_system.stop_abilities()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_stats.game_active = False
            self.ai_game.settings = Settings()
            self.settings = self.ai_game.settings
            pygame.mouse.set_visible(True)

    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens:
            if alien.rect.bottom > screen_rect.bottom:
                self.ship_hit()
                break