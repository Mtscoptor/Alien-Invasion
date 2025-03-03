import pygame

from player.bullet import Bullet

class AttackSystem:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        self.bullets = pygame.sprite.Group()
        self.aliens = ai_game.aliens

        self.last_fire_time = 0.0

    def fire(self):
        if self.game_stats.current_time - self.last_fire_time > self.settings.bullet_fire_interval:
            self.last_fire_time = self.game_stats.current_time
            self.fire_bullet()

    def fire_bullet(self):
        new_bullet = Bullet(self.ai_game)
        self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        killed_this_frame = sum(len(enemies) for enemies in collisions.values())
        self.game_stats.alien_killed += killed_this_frame
        self.game_stats.xp_value += killed_this_frame
        self.game_stats.xp_bar_value =self.game_stats.xp_value / self.game_stats.xp_value_max
        self.game_stats.score += (self.settings.alien_original_points *
                                  (1 + self.settings.score_increase_scale * (self.game_stats.alien_cycle - 1)) *
                                  killed_this_frame)
        self.game_stats.check_highest_score()
        self.ai_game.ui_system.scoreboard.prep_score()
        self.ai_game.ui_system.scoreboard.prep_xp()
        self.ai_game.ui_system.scoreboard.prep_xp_bar()