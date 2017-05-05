# -*- coding: utf-8 -*-
import pygame

'''
飞船对象
图形绘制、运动、状态
'''


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船，并设置初始位置"""
        self.screen = screen
        self.ai_setting = ai_settings

        # 加载飞船图像，并获取其外界矩形 rect，游戏操作都是对 rect 做处理
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动状态标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动状态标志调整飞船位置，参考系原点在左上角，'''
        # 更新ship暂存的center值，而不是ship.rect的center值
        # 位置调整指令存在并发可能，故用 if 而非 elif
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_setting.ship_speed_factor
        # 暂存中间值为浮点数，整数部分传给rect
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船，即在rect位置绘制飞船图像"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''在飞船撞到外星人后，飞船位置居中'''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery