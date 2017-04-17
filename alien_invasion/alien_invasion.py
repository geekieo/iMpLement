#!/usr/bin/env python
#coding=utf-8
import sys
import pygame


def run_game():

    # 初始化游戏并创建屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # 设置背景色
    bg_color = (230, 230, 230)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)
        # 让最近的屏幕可见
        pygame.display.flip()
        # 延迟 33 毫秒执行下以循环，限制最高帧数为 30 FPS
        pygame.time.delay(33)

run_game()