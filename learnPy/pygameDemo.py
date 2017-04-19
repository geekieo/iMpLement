#!/usr/bin/env python
#-*- coding:utf-8
import pygame
# 方便使用按钮参数：KEYDOWN, K_ESCAPE
from pygame.locals import *

# 定义 Player 类 调用 super 赋予它属性和方法
# 我们画在屏幕上的surface 现在是player的一个属性
class  Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

    def updata(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)

# 初始化 pygame
pygame.init()
# 创建屏幕对象
# 设定尺寸为 800x600
screen = pygame.display.set_mode((800, 600))

player = Player()
# 控制主循环的进行的变量
running = True
# 主循环
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    # #获取输入按钮
    # pressed_keys = pygame.event.get_presssed()
    # #响应输入按钮
    # play.update(pressed_keys)

    # 这一行表示：将player的surf画到屏幕 x：400.y:300的坐标上     
    screen.blit(player.surf,(400,300))
    # 显示画面
    pygame.display.flip()
