import pygame

from ui.button import Button
from ui.scoreboard import ScoreBoard

class UISystem:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.game_stats = ai_game.game_stats
        self.ship = ai_game.ship

        self.play_button = Button(ai_game, "Play")
        self.scoreboard = ScoreBoard(ai_game)

        self.aliens = ai_game.aliens
        self.bullets = ai_game.bullets

    def draw_play_button(self):
        if not self.game_stats.game_active:
            self.play_button.draw_button()

    def check_play_button(self, mouse_pos):
        #单击Play按钮开始新游戏
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_stats.game_active:
            self.game_stats.reset_stats()
            self.game_stats.game_active = True

            self.bullets.empty()
            self.aliens.empty()

            self.ship.center_ship()

            #隐藏鼠标光标
            pygame.mouse.set_visible(False)

            self.ai_game.ui_system.scoreboard.prep_alien_cycle()
            self.ai_game.ui_system.scoreboard.prep_score()
            self.ai_game.ui_system.scoreboard.prep_ships()
            self.ai_game.ui_system.scoreboard.prep_player_level()
            self.ai_game.ui_system.scoreboard.prep_xp()

    def update(self):
        self.scoreboard.update()