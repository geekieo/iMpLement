import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''表示单个外星人类'''

    def __init__(self, ai_settings, screen):
        '''初始化外星人并设置初始位置'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 外星人初始化位置为屏幕左上角附件，边距为一个rect的宽和长
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确位置
        self.x = float(self.rect.x)

    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image, self.rect)
