#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gameFunc


def run_game():

    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen,ai_settings)

    # 开始游戏主循环
    while True:
        gameFunc.check_events(ship)
        ship.update()

        # 更新屏幕
        gameFunc.update_screen(ai_settings, screen, ship)
        # 绘制屏幕
        pygame.display.flip()
        # 延迟执行下一循环
        pygame.time.delay(23)


run_game()
