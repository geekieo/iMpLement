# -*- coding: utf-8 -*-
import pygame

'''
飞船对象
图形绘制、运动、状态
'''


class Ship():
    def __init__(self, screen):
        """初始化飞船，并设置初始位置"""
        self.screen = screen

        # 加载飞船图像，并获取其外界矩形 rect，游戏操作都是对 rect 做处理
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动状态标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动状态标志调整飞船位置，参考系原点在左上角，
        位置调整指令存在并发可能，故用 if 而非 elif'''
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        """在指定位置绘制飞船，即在rect位置绘制飞船图像"""
        self.screen.blit(self.image, self.rect)
