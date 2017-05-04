# -*- coding: utf-8 -*-
class Settings():
    """存储《外星人入侵》的所有设置"""

    def __init__(self):
        # self 为类的实例化对象
        """初始化游戏的设置"""
        # 屏幕初始化
        self.screen_width = 1000
        self.screen_height = 750
        self.bg_color = (230, 230, 230)

        # 计时设置
        self.press_waiting_time = 2000

        # 飞船设置
        self.ship_speed_factor = 2

        # 子弹设置
        self.bullet_speed_factor = 3.5
        self.bullet_widdth = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10

        # 外星人设置
        self.alien_speed_factor = 1
        # 右为正方向
        self.fleet_direction = 1
        self.fleet_drop_speed_factor = 10
