import pygame

class GameStats:
    #跟踪游戏统计信息
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.settings

        self.ships_left = 0
        self.player_level = 1
        self.total_kill_for_next_player_level = 0
        self.current_time = 0
        self.game_active = False
        self.alien_killed = 0
        self.score = 0
        self.alien_cycle = 0
        self.highest_score = 0
        self.xp_value = 0
        self.xp_value_max = 0
        self.xp_bar_value =0

        self.reset_stats()

    def run_time(self):
        self.current_time = pygame.time.get_ticks()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.player_level = 1
        self.total_kill_for_next_player_level = self.settings.original_kills_to_next_level
        self.current_time = 0
        self.alien_killed = 0
        self.score = 0
        self.alien_cycle = 0
        self.xp_value = 0
        self.xp_value_max = self.settings.original_kills_to_next_level
        self.xp_bar_value = 0.0

    def player_level_up(self):
        if self.alien_killed >= self.total_kill_for_next_player_level:
            self.player_level += 1
            self.xp_value_max = int(self.settings.original_kills_to_next_level *
                                 (1 + self.settings.kills_to_next_level_increase_factor * (self.player_level - 1)))
            self.xp_value = self.alien_killed - self.total_kill_for_next_player_level
            self.xp_bar_value = self.xp_value / self.xp_value_max
            self.total_kill_for_next_player_level += self.xp_value_max

            self.ai_game.ui_system.scoreboard.prep_player_level()
            self.ship_level_up()
            self.bullet_level_up()

    def ship_level_up(self):
        self.settings.ship_speed_x = ((self.settings.player_speedup_scale * (self.player_level - 1) + 1) *
                                              self.settings.ship_original_speed_x)
        self.settings.ship_speed_y = ((self.settings.player_speedup_scale * (self.player_level - 1) + 1) *
                                              self.settings.ship_original_speed_y)
        self.settings.bullet_speed = ((self.settings.player_speedup_scale * (self.player_level - 1) + 1) *
                                              self.settings.bullet_original_speed)

    def bullet_level_up(self):
        self.settings.bullet_width = ((self.settings.player_speedup_scale * (self.player_level - 1) + 1) *
                                              self.settings.bullet_original_width)
        self.settings.bullet_height = ((self.settings.player_speedup_scale * (self.player_level - 1) + 1) *
                                               self.settings.bullet_original_height)

    def alien_speed_up(self):
        self.settings.alien_speed_x_max = ((self.settings.alien_speedup_scale *
                                                    (self.alien_cycle - 1) + 1) *
                                                   self.settings.alien_original_speed_x_max)
        self.settings.alien_speed_y_max = ((self.settings.alien_speedup_scale *
                                                    (self.alien_cycle - 1) + 1) *
                                                   self.settings.alien_original_speed_y_max)
        self.settings.alien_create_interval = ((self.settings.alien_speedup_scale *
                                                    (self.alien_cycle - 1) + 1) *
                                                       self.settings.alien_original_create_interval)

    def check_highest_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.ai_game.ui_system.scoreboard.prep_highest_score()

    def update(self):
        self.check_highest_score()
        self.player_level_up()
        self.alien_speed_up()