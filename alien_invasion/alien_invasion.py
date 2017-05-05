#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame.sprite import Group

from game_functions import Game_Functions
from game_stats import GameStats
from settings import Settings
from ship import Ship


def run_game():

    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个子弹组，一个外星人组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf = Game_Functions()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.update_press_timing(ai_settings)
        gf.update_fleet_timing(ai_settings, screen, ship, bullets, aliens)
        ship.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(ai_settings, screen, ship, bullets, aliens, stats)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        pygame.display.flip()
        # 延迟执行下一循环
        pygame.time.delay(10)


run_game()
