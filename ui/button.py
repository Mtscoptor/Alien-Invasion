import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.width = self.settings.BUTTON_WIDTH
        self.height = self.settings.BUTTON_HEIGHT
        self.button_color = self.settings.BUTTON_COLOR
        self.button_text_color = self.settings.BUTTON_TEXT_COLOR
        self.font = pygame.font.SysFont(None, self.settings.BUTTON_TEXT_WORD_SIZE)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #创建按钮标签
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        #将msg渲染为图像，并使其在按钮上居中
        self.msg_image = self.font.render(msg, True, self.button_text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
