#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gameFunc
from pygame.sprite import Group


def run_game():

    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船、一个子弹组，一个外星人组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gameFunc.create_fleet(ai_settings, screen, aliens)

    # 开始游戏主循环
    while True:
        gameFunc.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gameFunc.update_bullets(bullets)
        gameFunc.update_screen(ai_settings, screen, ship, bullets, aliens)
        pygame.display.flip()
        # 延迟执行下一循环
        pygame.time.delay(10)


run_game()
