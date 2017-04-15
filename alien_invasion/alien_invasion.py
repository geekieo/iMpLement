#!/usr/bin/env python
#coding=utf-8
import sys
import pygame


def run_game():

    # 初始化游戏并创建屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.type == pygame.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 让最近的屏幕可见
        pygame.display.flip()
    
run_game()
'''   

def run_game():

    pygame.display.set_caption("Alien Invasion")
    
    # 设置背景色
    bg_color = (230,230,230)
    
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        
        # 每次循环时都重绘屏幕
        screen.fill(bg_color)
        
        # 让最近的屏幕可见
        pygame.display.flip()

run_game()
'''