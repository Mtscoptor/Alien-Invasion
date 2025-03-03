class Settings:
    #存储游戏设置
    def __init__(self):
        #初始化游戏的静态设置
        #屏幕设置
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 900
        self.BACKGROUND_COLOR = (230, 230, 230)

        #飞船设置
        self.ship_speed_x = 0.7
        self.ship_speed_y = 0.2
        self.ship_original_speed_x = 0.7
        self.ship_original_speed_y = 0.2
        self.ship_limit = 3
        self.original_kills_to_next_level = 5
        self.kills_to_next_level_increase_factor = 0.5

        #子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_original_speed = 1.0
        self.bullet_original_width = 3
        self.bullet_original_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_fire_interval = 200

        #技能设置
        self.crazy_state_lasting_time = 5000

        #外星人设置
        self.alien_original_create_probability = 0.1
        self.alien_create_probability_increase_by_row_increase = 0.1
        self.alien_speed_x_max = 0.2
        self.alien_speed_y_max = 0.1
        self.alien_original_speed_x_max = 0.2
        self.alien_original_speed_y_max = 0.1
        self.alien_number_rows_max = 5
        self.alien_create_interval = 3000
        self.alien_original_create_interval = 3000
        self.alien_change_velocity_interval = 1000
        self.alien_create_probability_increase_by_cycle_increase = 0.05
        self.alien_original_points = 50

        #按钮设置
        self.BUTTON_WIDTH = 200
        self.BUTTON_HEIGHT = 50
        self.BUTTON_COLOR = (0,255,0)
        self.BUTTON_TEXT_COLOR = (255,255,255)
        self.BUTTON_TEXT_WORD_SIZE = 48

        #游戏设置
        self.player_speedup_scale = 0.05
        self.alien_speedup_scale = 0.02
        self.score_increase_scale = 0.2

        #得分板信息
        self.SCORE_TEXT_COLOR = (30,30,30)
        self.SCORE_TEXT_WORD_SIZE = 48
        self.CYCLE_BOARD_DISTANCE_TO_RIGHT = 20
        self.CYCLE_BOARD_TOP_DISTANCE_TO_TOP = 20
        self.SCOREBOARD_TOP_DISTANCE_TO_CYCLE_BOARD_BOTTOM = 10
        self.LEVEL_BOARD_TOP_DISTANCE_TO_SCOREBOARD_BOTTOM = 10
        self.XP_BOARD_TOP_DISTANCE_TO_LEVEL_BOARD_BOTTOM = 10
        self.SHIPS_LEFT_BOARD_LEFT_DISTANCE_TO_LEFT = 10
        self.SHIPS_LEFT_BOARD_LEFT_DISTANCE_TO_TOP = 10
        self.XP_BAR_HEIGHT = 30
        self.XP_BAR_COLOR = (0,0,0)
        self.XP_BAR_BACKGROUND_COLOR = (211,211,211)
        self.XP_BAR_TOP_DISTANCE_TO_XP_BOARD_BOTTOM = 10