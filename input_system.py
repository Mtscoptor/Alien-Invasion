import pygame
import sys

class InputSystem:
    def __init__(self,ai_game):
        self.ai_game = ai_game

        self.attack_system = ai_game.attack_system
        self.ability_system = ai_game.ability_system
        self.ship = ai_game.ship
        self.game_stats = ai_game.game_stats
        self.ui_system = ai_game.ui_system

    def check_events(self):
        # 相应按键和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_mouse_button_down_events(event)
            elif event.type == pygame.KEYDOWN and self.game_stats.game_active:
                self.check_keydown_events(event)
            # elif event.type == pygame.KEYUP:
            #     self._check_keyup_events(event)

        if self.game_stats.game_active:
            # self.check_mouse_pressed_events()
            self.check_key_pressed_events()

    def check_mouse_button_down_events(self,event):
        mouse_pos = pygame.mouse.get_pos()
        self.ui_system.check_play_button(mouse_pos)

    # def check_mouse_pressed_events(self):
    #     mouse_buttons = pygame.mouse.get_pressed()
    #     if mouse_buttons[0]:
    #         self.attack_system.fire()

    def check_key_pressed_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            self.attack_system.fire()
        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.ship.move_dir[0] = 1
        if keys[pygame.K_a] and not keys[pygame.K_d]:
            self.ship.move_dir[0] = -1
        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.ship.move_dir[1] = 1
        if keys[pygame.K_s] and not keys[pygame.K_w]:
            self.ship.move_dir[1] = -1
        if keys[pygame.K_a] == keys[pygame.K_d]:
            self.ship.move_dir[0] = 0
        if keys[pygame.K_w] == keys[pygame.K_s]:
            self.ship.move_dir[1] = 0

    def check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        else:
            if event.key == pygame.K_e:
                self.ability_system.crazy_state(True)

    # def _check_keyup_events(self,event):