#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame

from settings import Settings
from ship import Ship
from game_functions import Game_Functions
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
    gf = Game_Functions()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        pygame.display.flip()
        # 延迟执行下一循环
        pygame.time.delay(10)


run_game()
