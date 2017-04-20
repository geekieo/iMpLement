# -*- coding: utf-8 -*-
import pygame


class Ship():
    def __init__(self, screen):
        """初始化飞船，并设置初始位置"""
        self.screen = screen

        #加载飞船图像，并获取其外界矩形 rect，游戏操作都是对 rect 做处理
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将飞船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船，即在rect位置绘制飞船图像"""
        self.screen.blit(self.image, self.rect)