# -*- coding: utf-8 -*-
class Settings():
    """存储《外星人入侵》的所有设置"""

    def __init__(self):
        # self 为类的实例化对象
        """初始化游戏的设置"""
        # 屏幕初始化
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1.5
        self.bullet_widdth = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)