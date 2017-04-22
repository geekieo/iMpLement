#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:
        gf.check_events
        gf.update_screen(ai_settings, screen, ship)
        # 让最近的屏幕可见
        pygame.display.flip()
        # 延迟 33 毫秒执行下以循环，限制最高帧数为 30 FPS
        pygame.time.delay(33)


run_game()
