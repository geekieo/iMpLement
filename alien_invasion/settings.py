# -*- coding: utf-8 -*-
class Settings():
    """存储《外星人入侵》的所有设置"""

    def __init__(self):
        # self 为类的实例化对象
        """初始化游戏的设置"""
        # 屏幕初始化
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # 计时设置
        self.press_waiting_time = 2000
        self.update_fleet_waiting_time = 1500

        # 飞船的设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_widdth = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 50

        # 外星人设置
        self.fleet_drop_speed_factor = 10
        # fleet_direction 为1表示向右,-1表示向左
        self.fleet_direction = 1

        # 加快游戏速度倍数
        self.speedup_scale = 1.1
        # 得分提高速度
        self.scoreup_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置项'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.scoreup_scale)