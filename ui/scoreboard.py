import pygame.font

from pygame.sprite import Group
from player.ship import Ship

class ScoreBoard:
    #显示得分等信息的类
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.game_stats = ai_game.game_stats

        self.text_color = self.settings.SCORE_TEXT_COLOR
        self.font = pygame.font.SysFont(None, self.settings.SCORE_TEXT_WORD_SIZE)

        self.ships = None
        self.cycle_image = None
        self.cycle_rect = None
        self.score_image = None
        self.score_rect = None
        self.highest_score_image = None
        self.highest_score_rect = None
        self.player_level_image = None
        self.player_level_rect = None
        self.xp_image = None
        self.xp_rect = None
        self.xp_bar_background_rect = None
        self.xp_bar_rect = None

        self.prep_highest_score()

    def prep_score(self):
        #将得分转换成一幅渲染的图像
        the_score_str = "{:,}".format(self.game_stats.score)
        score_str = f"Score : {the_score_str}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.BACKGROUND_COLOR)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.cycle_rect.right
        self.score_rect.top = self.settings.SCOREBOARD_TOP_DISTANCE_TO_CYCLE_BOARD_BOTTOM + self.cycle_rect.bottom

    def show_scores(self):
        self.screen.blit(self.cycle_image, self.cycle_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.player_level_image, self.player_level_rect)
        self.screen.blit(self.xp_image, self.xp_rect)
        self.ships.draw(self.screen)
        self.screen.fill(self.settings.XP_BAR_BACKGROUND_COLOR, self.xp_bar_background_rect)
        self.screen.fill(self.settings.XP_BAR_COLOR, self.xp_bar_rect)

    def prep_highest_score(self):
        #将得分转换成一幅渲染的图像
        high_score_str = "{:,}".format(self.game_stats.highest_score)
        highest_score_str = f"Highest Score: {high_score_str}"
        self.highest_score_image = self.font.render(highest_score_str, True,
                                                    self.text_color, self.settings.BACKGROUND_COLOR)

        #将最高得分放在屏幕顶部中央
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.screen_rect.top

    def prep_player_level(self):
        player_level_str = f"Level : {str(self.game_stats.player_level)}"
        self.player_level_image = self.font.render(player_level_str, True,
                                                   self.text_color, self.settings.BACKGROUND_COLOR)
        self.player_level_rect = self.player_level_image.get_rect()
        self.player_level_rect.right = self.score_rect.right
        self.player_level_rect.top = (self.score_rect.bottom +
                                      self.settings.LEVEL_BOARD_TOP_DISTANCE_TO_SCOREBOARD_BOTTOM)

    def prep_xp(self):
        xp_value_str = str(self.game_stats.xp_value)
        xp_value_max_str = str(self.game_stats.xp_value_max)
        xp_str = f"Experience : {xp_value_str}  /  {xp_value_max_str}"
        self.xp_image = self.font.render(xp_str, True,
                                         self.text_color, self.settings.BACKGROUND_COLOR)
        self.xp_rect = self.xp_image.get_rect()
        self.xp_rect.right = self.player_level_rect.right
        self.xp_rect.top = (self.player_level_rect.bottom +
                            self.settings.XP_BOARD_TOP_DISTANCE_TO_LEVEL_BOARD_BOTTOM)

    def prep_xp_bar(self):
        self.xp_bar_background_rect = pygame.Rect(0,0,0,0)
        self.xp_bar_background_rect.right = self.xp_rect.left
        self.xp_bar_background_rect.top = self.xp_rect.bottom + self.settings.XP_BAR_TOP_DISTANCE_TO_XP_BOARD_BOTTOM
        self.xp_bar_background_rect.width = self.xp_rect.width
        self.xp_bar_background_rect.height = self.settings.XP_BAR_HEIGHT

        self.xp_bar_rect = pygame.Rect(0,0,0,0)
        self.xp_bar_rect.left = self.xp_bar_background_rect.left
        self.xp_bar_rect.top = self.xp_bar_background_rect.top
        self.xp_bar_rect.height = self.xp_bar_background_rect.height
        self.xp_bar_rect.width = self.game_stats.xp_bar_value * self.xp_bar_background_rect.width

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.game_stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = self.settings.SHIPS_LEFT_BOARD_LEFT_DISTANCE_TO_LEFT + ship_number * ship.rect.width
            ship.rect.y = self.settings.SHIPS_LEFT_BOARD_LEFT_DISTANCE_TO_TOP
            self.ships.add(ship)

    def prep_alien_cycle(self):
        the_cycle_str = str(self.game_stats.alien_cycle)
        cycle_str = f"Cycle : {the_cycle_str}"
        self.cycle_image = self.font.render(cycle_str, True, self.text_color, self.settings.BACKGROUND_COLOR)

        self.cycle_rect = self.cycle_image.get_rect()
        self.cycle_rect.right = self.screen_rect.right - self.settings.CYCLE_BOARD_DISTANCE_TO_RIGHT
        self.cycle_rect.top = self.settings.CYCLE_BOARD_TOP_DISTANCE_TO_TOP

    def update(self):
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        if self.game_stats.game_active:
            self.show_scores()
