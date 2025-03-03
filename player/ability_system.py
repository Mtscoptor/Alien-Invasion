class AbilitySystem:
    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        self.ability_begin_time = 0.0

        self.is_act_ability = False
        self.isCrazy = False

    def crazy_state(self, state):
        # 狂暴状态
        if (self.game_stats.current_time > self.ability_begin_time + self.settings.crazy_state_lasting_time or
            not self.is_act_ability):
            if state:
                self.ability_begin_time = self.game_stats.current_time
                self.settings.bullet_fire_interval /= 5
                self.settings.ship_speed_x *= 2
                self.settings.ship_speed_y *= 2
                self.isCrazy = True
                if not self.is_act_ability:
                    self.is_act_ability = True
            else:
                if self.isCrazy:
                    self.settings.bullet_fire_interval *= 5
                    self.settings.ship_speed_x /= 2
                    self.settings.ship_speed_y /= 2
                    self.isCrazy = False

    def stop_abilities(self):
        self.crazy_state(False)